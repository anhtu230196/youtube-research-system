#!/usr/bin/env python3
"""Kiem tra tinh nhat quan cua registry.json va luu snapshot truoc khi sua.

Dung chung cho moi agent (Codex, Claude, Gemini). Xem AGENTS.md muc 5 va 10.

    python scripts/registry.py check
    python scripts/registry.py check --diff-base origin/main
    python scripts/registry.py snapshot
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ID_RE = re.compile(r"^NET-(\d{4})$")
DIR_RE = re.compile(r"^NET-(\d{4})-[a-z0-9][a-z0-9-]*$")
NEEDS_EPISODE_DIR = {"researching", "awaiting_review", "scripted", "published"}
REQUIRED_TOP_KEYS = ["schema_version", "channel", "next_case_number", "statuses", "cases", "batches"]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def system_dir() -> Path:
    root = repo_root()
    hits = [h for h in sorted(root.glob("**/YouTube-Research-System/registry.json"))
            if ".git" not in h.parts]
    if not hits:
        sys.exit("Khong tim thay */YouTube-Research-System/registry.json trong repo.")
    if len(hits) > 1:
        sys.exit("Tim thay nhieu registry.json: " + ", ".join(str(h) for h in hits))
    return hits[0].parent


def load_registry(path: Path) -> dict:
    try:
        with path.open(encoding="utf-8") as fh:
            return json.load(fh)
    except json.JSONDecodeError as exc:
        sys.exit(f"registry.json khong phai JSON hop le: {exc}")


def git(*args: str):
    try:
        out = subprocess.run(["git", *args], cwd=repo_root(),
                             capture_output=True, text=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    return out.stdout


def check_snapshot_rule(base, sysdir, problems, notes) -> None:
    """Sua registry.json thi phai kem mot snapshot moi trong history/."""
    if git("rev-parse", "--verify", base) is None:
        notes.append(f"Bo qua luat snapshot: khong doc duoc ref {base!r}.")
        return
    diff = git("diff", "--name-status", base, "HEAD")
    if diff is None:
        notes.append("Bo qua luat snapshot: khong chay duoc git diff.")
        return
    rel = sysdir.relative_to(repo_root()).as_posix()
    touched_registry = False
    added_snapshot = False
    for line in diff.splitlines():
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        state, path = parts[0], parts[-1]
        if path == f"{rel}/registry.json":
            touched_registry = True
        if state.startswith("A") and path.startswith(f"{rel}/history/registry-"):
            added_snapshot = True
    if touched_registry and not added_snapshot:
        problems.append(
            f"registry.json doi so voi {base} nhung khong them snapshot moi trong history/. "
            "Chay: python scripts/registry.py snapshot"
        )


def cmd_check(args) -> int:
    sysdir = system_dir()
    data = load_registry(sysdir / "registry.json")
    problems = []
    notes = []

    for key in REQUIRED_TOP_KEYS:
        if key not in data:
            problems.append(f"Thieu khoa bat buoc {key!r} o registry.json.")
    if problems:
        return report(problems, notes)

    statuses = set(data["statuses"])
    cases = data["cases"]
    seen_ids = set()
    numbers = set()

    for case in cases:
        cid = case.get("id") or ""
        m = ID_RE.match(cid)
        if not m:
            problems.append(f"Ma khong dung dinh dang NET-xxxx: {cid!r}.")
            continue
        if cid in seen_ids:
            problems.append(f"Ma {cid} xuat hien nhieu lan trong cases.")
        seen_ids.add(cid)
        numbers.add(int(m.group(1)))

        status = case.get("status")
        if status not in statuses:
            problems.append(f"{cid}: status {status!r} khong nam trong danh sach statuses.")

        history = case.get("history") or []
        if not history:
            problems.append(f"{cid}: history rong. Moi lan doi trang thai phai ghi lai.")
        for i, h in enumerate(history):
            missing = [k for k in ("date", "status", "reason") if not h.get(k)]
            if missing:
                problems.append(f"{cid}: history[{i}] thieu {', '.join(missing)}.")
        if history and history[-1].get("status") != status:
            problems.append(
                f"{cid}: status hien tai {status!r} khac muc history cuoi "
                f"{history[-1].get('status')!r}."
            )
        if status == "published" and not case.get("published_url"):
            problems.append(f"{cid}: status published nhung published_url rong.")

        ep = case.get("episode_path")
        if ep and not (sysdir / ep).exists():
            if status in NEEDS_EPISODE_DIR:
                problems.append(f"{cid}: status {status!r} nhung khong co thu muc {ep}.")
            else:
                notes.append(f"{cid}: episode_path {ep} chua ton tai (status {status!r}).")

    episodes_dir = sysdir / "episodes"
    if episodes_dir.is_dir():
        for child in sorted(p for p in episodes_dir.iterdir() if p.is_dir()):
            m = DIR_RE.match(child.name)
            if not m:
                problems.append(f"Thu muc tap sai dinh dang NET-xxxx-slug: episodes/{child.name}")
                continue
            cid = f"NET-{m.group(1)}"
            numbers.add(int(m.group(1)))
            case = next((c for c in cases if c.get("id") == cid), None)
            if case is None:
                problems.append(
                    f"episodes/{child.name} ton tai nhung khong co case {cid} trong registry.json. "
                    "So trang thai phai biet moi tap dang lam."
                )
                continue
            expected = f"episodes/{child.name}"
            if case.get("episode_path") not in (None, expected):
                problems.append(
                    f"{cid}: episode_path {case.get('episode_path')!r} khong tro toi {expected}."
                )

    highest = max(numbers) if numbers else 0
    nxt = data.get("next_case_number")
    if not isinstance(nxt, int):
        problems.append(f"next_case_number phai la so nguyen, dang la {nxt!r}.")
    elif nxt <= highest:
        problems.append(
            f"next_case_number = {nxt} nhung ma cao nhat dang dung la NET-{highest:04d}. "
            f"Se cap trung ma. Dat next_case_number >= {highest + 1}."
        )

    for batch in data.get("batches", []):
        for cid in batch.get("case_ids", []):
            if cid not in seen_ids:
                problems.append(f"batch {batch.get('id')}: case_id {cid} khong co trong cases.")

    fingerprints = {}
    for case in cases:
        fp = case.get("fingerprint")
        if not fp:
            continue
        if fp in fingerprints:
            problems.append(
                f"fingerprint trung giua {fingerprints[fp]} va {case.get('id')}: {fp!r}. "
                "Nhieu kha nang la cung mot cau chuyen."
            )
        else:
            fingerprints[fp] = case.get("id", "?")

    if args.diff_base:
        check_snapshot_rule(args.diff_base, sysdir, problems, notes)

    return report(problems, notes)


def report(problems, notes) -> int:
    for note in notes:
        print(f"  ghi chu: {note}")
    if problems:
        print(f"\nregistry: {len(problems)} van de")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("registry: khong phat hien van de")
    return 0


def cmd_snapshot(args) -> int:
    sysdir = system_dir()
    src = sysdir / "registry.json"
    load_registry(src)  # tu choi snapshot mot file JSON hong
    history = sysdir / "history"
    history.mkdir(exist_ok=True)
    now = datetime.now()
    dest = history / f"registry-{now:%Y%m%d-%H%M%S}-{now.microsecond // 1000:03d}.json"
    shutil.copy2(src, dest)
    print(f"da luu {dest.relative_to(repo_root()).as_posix()}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    sub = parser.add_subparsers(dest="command", required=True)
    p_check = sub.add_parser("check", help="kiem tra tinh nhat quan cua so trang thai")
    p_check.add_argument("--diff-base", metavar="REF",
                         help="ref goc de kiem tra luat snapshot, vi du origin/main")
    p_check.set_defaults(func=cmd_check)
    p_snap = sub.add_parser("snapshot", help="luu ban sao co dau thoi gian vao history/")
    p_snap.set_defaults(func=cmd_snapshot)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
