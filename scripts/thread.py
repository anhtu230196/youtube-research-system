#!/usr/bin/env python3
"""Luong review nhieu vong giua cac agent tren mot san pham trung gian.

Dung chung cho moi agent (Codex, Claude, Gemini). Xem AGENTS.md muc 8.

    python scripts/thread.py new net-0007-khung-suon \\
        --artifact t-i/outputs/.../scripts/01-beat-sheet.md \\
        --author claude --reviewers gemini,codex \\
        --question "Khung nay co nut that nao khong co chung cu do khong?"
    python scripts/thread.py status
    python scripts/thread.py next net-0007-khung-suon
    python scripts/thread.py check
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

AGENTS = ["codex", "claude", "gemini"]
STATUSES = ["open", "blocked", "settled"]
ROLES = ["author", "reviewer"]
MAX_ROUND = 3
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
FILE_RE = re.compile(r"^r(\d+)-(\d{2})-(proposal|review|response)-([a-z]+)\.md$")
POINT_RE = re.compile(r"^\|\s*(D\d+)\s*\|")
OPEN_POINT_MARKS = ("mở", "chờ")

REQUIRED = ["id", "artifact", "artifact_version", "author", "reviewers",
            "round", "turn", "turn_role", "status", "opened", "updated"]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def threads_dir() -> Path:
    return repo_root() / "coordination" / "threads"


def parse_front_matter(text: str):
    """Doc frontmatter YAML phang: key: value va danh sach '- muc'."""
    if not text.startswith("---"):
        return None, "khong co frontmatter mo dau bang ---"
    end = text.find("\n---", 3)
    if end == -1:
        return None, "frontmatter khong duoc dong bang ---"
    data, key = {}, None
    for raw in text[3:end].splitlines():
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.lstrip().startswith("- ") and key:
            data.setdefault(key, [])
            if isinstance(data[key], list):
                data[key].append(line.lstrip()[2:].strip())
            continue
        if ":" not in line:
            return None, f"dong khong doc duoc trong frontmatter: {line!r}"
        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip()
        data[key] = value if value else []
    return data, None


def open_points(text: str):
    """Cac diem tranh luan chua dong, doc tu bang trong THREAD.md."""
    out = []
    for line in text.splitlines():
        m = POINT_RE.match(line)
        if not m:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        status = cells[-1] if cells else ""
        if any(mark in status for mark in OPEN_POINT_MARKS):
            out.append((m.group(1), status))
    return out


def load_threads():
    out = []
    if not threads_dir().is_dir():
        return out
    for d in sorted(threads_dir().iterdir()):
        if not d.is_dir() or d.name.startswith("_"):
            continue
        f = d / "THREAD.md"
        if not f.exists():
            out.append((d, None, None, "thieu THREAD.md"))
            continue
        text = f.read_text(encoding="utf-8")
        data, err = parse_front_matter(text)
        out.append((d, data, text, err))
    return out


def participants(data) -> list:
    reviewers = data.get("reviewers") or []
    if isinstance(reviewers, str):
        reviewers = [r.strip() for r in reviewers.split(",") if r.strip()]
    return [data.get("author")] + reviewers


def next_index(d: Path, rnd: int) -> int:
    return sum(1 for p in d.glob(f"r{rnd}-*.md") if FILE_RE.match(p.name))


def cmd_new(args) -> int:
    slug = args.slug
    if not SLUG_RE.match(slug):
        sys.exit("slug chi gom chu thuong, so va dau gach ngang.")
    if args.author not in AGENTS:
        sys.exit(f"author phai thuoc {AGENTS}.")
    reviewers = [r.strip() for r in args.reviewers.split(",") if r.strip()]
    bad = [r for r in reviewers if r not in AGENTS]
    if bad:
        sys.exit(f"reviewer khong hop le: {bad}")
    if args.author in reviewers:
        sys.exit("tac gia khong duoc dong thoi la nguoi review cua chinh minh.")
    if not reviewers:
        sys.exit("can it nhat mot nguoi review.")

    d = threads_dir() / slug
    if d.exists():
        sys.exit(f"{d.relative_to(repo_root()).as_posix()} da ton tai.")
    artifact = Path(args.artifact)
    if not (repo_root() / artifact).exists():
        print(f"  canh bao: chua co {artifact.as_posix()} — tac gia se tao o luot dau.")

    d.mkdir(parents=True)
    today = date.today().isoformat()
    reviewer_lines = "\n".join(f"  - {r}" for r in reviewers)
    (d / "THREAD.md").write_text(
        f"""---
id: {slug}
step: {args.step or ""}
artifact: {artifact.as_posix()}
artifact_version: 1
author: {args.author}
reviewers:
{reviewer_lines}
round: 1
turn: {args.author}
turn_role: author
status: open
opened: {today}
updated: {today}
---

# {slug}

**Sản phẩm đang review:** `{artifact.as_posix()}`

## Câu hỏi luồng này phải trả lời

{args.question}

## Điểm tranh luận

| ID | Nêu bởi | Vòng | Nội dung | Trạng thái |
| --- | --- | --- | --- | --- |

## Nhật ký vòng

- r1 · {args.author} (tác giả) · **đang chờ**

## Ngoài lượt

Việc gấp phát hiện khi chưa tới lượt mình thì ghi một dòng ở đây, không viết file vòng.
""",
        encoding="utf-8",
    )
    print(f"da tao {(d / 'THREAD.md').relative_to(repo_root()).as_posix()}")
    print(f"Buoc tiep: python scripts/thread.py next {slug}")
    return 0


def cmd_status(args) -> int:
    rows = []
    for d, data, text, err in load_threads():
        if err or not data:
            rows.append((d.name, "?", "?", "?", f"loi: {err}"))
            continue
        if args.slug and data.get("id") != args.slug:
            continue
        pts = open_points(text or "")
        rows.append((
            str(data.get("id")),
            f"r{data.get('round')}",
            f"{data.get('turn')} ({data.get('turn_role')})",
            str(data.get("status")),
            f"{len(pts)} diem mo" + (": " + ", ".join(p[0] for p in pts) if pts else ""),
        ))
    if not rows:
        print("khong co luong nao")
        return 0
    w = [max(len(r[i]) for r in rows) for i in range(4)]
    for r in rows:
        print(f"{r[0]:<{w[0]}}  {r[1]:<{w[1]}}  {r[2]:<{w[2]}}  {r[3]:<{w[3]}}  {r[4]}")
    return 0


def cmd_next(args) -> int:
    for d, data, text, err in load_threads():
        if not data or data.get("id") != args.slug:
            continue
        if err:
            sys.exit(f"THREAD.md hong: {err}")

        status = data.get("status")
        if status == "settled":
            print(f"Luong {args.slug} da chot. Khong con luot nao.")
            return 0
        if status == "blocked":
            pts = open_points(text or "")
            print(f"Luong {args.slug} dang blocked — cho Tu quyet.")
            for pid, st in pts:
                print(f"  {pid}: {st}")
            return 0

        turn, role = data.get("turn"), data.get("turn_role")
        rnd = int(data.get("round", 1))
        rel = d.relative_to(repo_root()).as_posix()
        nn = next_index(d, rnd)
        kind = "proposal" if (role == "author" and rnd == 1) else (
            "response" if role == "author" else "review")
        fname = f"r{rnd}-{nn:02d}-{kind}-{turn}.md"

        print(f"=== Toi luot: {turn} ({role}) · vong {rnd}/{MAX_ROUND} ===\n")
        print("Dan nguyen doan duoi day cho agent do:\n")
        print("-" * 68)
        if role == "author" and rnd == 1:
            exists = (repo_root() / str(data.get("artifact"))).exists()
            step = (f"San pham da co san o {data.get('artifact')}. Doc lai va bo sung nhung gi\n"
                    f"con thieu de nguoi khac review duoc."
                    if exists else
                    f"Viet san pham vao {data.get('artifact')}.")
            print(f"""Doc {rel}/THREAD.md va AGENTS.md muc 8 truoc.

Ban la TAC GIA buoc nay. {step}

Sau do viet {rel}/{fname}: ban da quyet dinh gi va vi sao, cho nao ban tu
thay yeu nhat, va cau hoi nao ban muon nguoi review tra loi.

Cuoi cung cap nhat {rel}/THREAD.md: turn -> nguoi review dau tien,
turn_role -> reviewer, updated -> hom nay.""")
        elif role == "author":
            print(f"""Doc {rel}/THREAD.md, AGENTS.md muc 8 va
.claude/skills/deliberation/SKILL.md truoc. Doc tat ca file vong truoc trong {rel}/.

Ban la TAC GIA. Tra loi TUNG diem dang mo trong bang diem: chap nhan va sua,
hoac phan bac bang mot trong bon ly do o muc 8. Khong im lang bo qua diem nao,
va khong sua lay le cho diem bien mat.

Sua {data.get('artifact')} cho cac diem ban chap nhan, roi bump artifact_version
trong THREAD.md.

Viet {rel}/{fname} ghi ro tung diem: da sua o dau, hoac phan bac vi ly do gi.
Cap nhat bang diem va turn trong THREAD.md.""")
        else:
            print(f"""Doc {rel}/THREAD.md, AGENTS.md muc 8 va
.claude/skills/deliberation/SKILL.md truoc. Doc {data.get('artifact')}
(ban v{data.get('artifact_version')}) va cac file vong truoc trong {rel}/.

Ban REVIEW buoc nay. Viet {rel}/{fname}.

Moi y mot ma D** moi, mot nhan CHAN/SUA/HOI/OK, kem file:dong va claim_id
hoac source_id neu noi ve noi dung. Chi neu nhung gi muc 8 cho phep neu —
khac gu khong phai loi. Neu tac gia da phan bac mot diem cua ban o vong truoc:
chap nhan, dua chung cu moi, hoac day len Tu; khong lap lai y cu.

Ghi ro ban da KHONG kiem cai gi.

Cap nhat {rel}/THREAD.md: them diem moi vao bang, doi turn sang nguoi ke tiep,
updated -> hom nay.""")
        print("-" * 68)
        return 0
    sys.exit(f"khong tim thay luong {args.slug!r}. Chay: python scripts/thread.py status")


def cmd_check(args) -> int:
    problems, notes = [], []
    for d, data, text, err in load_threads():
        rel = d.relative_to(repo_root()).as_posix()
        if err or not data:
            problems.append(f"{rel}: {err or 'khong doc duoc THREAD.md'}")
            continue

        missing = [k for k in REQUIRED if not data.get(k) and data.get(k) != 0]
        if missing:
            problems.append(f"{rel}: frontmatter thieu {', '.join(missing)}.")
            continue

        if data["id"] != d.name:
            problems.append(f"{rel}: id {data['id']!r} khong trung ten thu muc.")
        if data["author"] not in AGENTS:
            problems.append(f"{rel}: author {data['author']!r} khong hop le.")
        people = participants(data)
        if data["author"] in people[1:]:
            problems.append(f"{rel}: tac gia dong thoi la nguoi review cua chinh minh.")
        for r in people[1:]:
            if r not in AGENTS:
                problems.append(f"{rel}: reviewer {r!r} khong hop le.")
        if data["status"] not in STATUSES:
            problems.append(f"{rel}: status {data['status']!r} khong thuoc {STATUSES}.")
        if data["turn_role"] not in ROLES:
            problems.append(f"{rel}: turn_role {data['turn_role']!r} khong thuoc {ROLES}.")
        if data["turn"] not in people:
            problems.append(f"{rel}: turn {data['turn']!r} khong phai nguoi tham gia luong.")
        if data["turn_role"] == "author" and data["turn"] != data["author"]:
            problems.append(f"{rel}: turn_role la author nhung turn khong phai tac gia.")

        try:
            rnd = int(data["round"])
        except (TypeError, ValueError):
            problems.append(f"{rel}: round phai la so nguyen.")
            rnd = 0
        if rnd > MAX_ROUND and data["status"] == "open":
            problems.append(
                f"{rel}: da qua vong {MAX_ROUND} ma status van open. "
                "Het tran thi chuyen blocked va day diem mo len Tu."
            )

        if not (repo_root() / str(data["artifact"])).exists():
            if rnd == 1 and data["turn_role"] == "author":
                notes.append(f"{rel}: artifact chua ton tai, tac gia se tao o luot dau.")
            else:
                problems.append(f"{rel}: khong thay artifact {data['artifact']}.")

        for f in sorted(d.glob("*.md")):
            if f.name == "THREAD.md":
                continue
            m = FILE_RE.match(f.name)
            if not m:
                problems.append(
                    f"{rel}/{f.name}: sai dinh dang r<vong>-<NN>-<proposal|review|response>-<agent>.md"
                )
                continue
            if m.group(4) not in people:
                problems.append(f"{rel}/{f.name}: {m.group(4)} khong tham gia luong nay.")
            if int(m.group(1)) > MAX_ROUND:
                problems.append(f"{rel}/{f.name}: vong {m.group(1)} vuot tran {MAX_ROUND}.")

        pts = open_points(text or "")
        if data["status"] == "settled" and pts:
            problems.append(
                f"{rel}: status settled nhung con {len(pts)} diem mo "
                f"({', '.join(p[0] for p in pts)})."
            )

    if notes:
        for n in notes:
            print(f"  ghi chu: {n}")
    if problems:
        print(f"\nthreads: {len(problems)} van de")
        for p in problems:
            print(f"  - {p}")
        return 1
    print(f"threads: khong phat hien van de ({len(load_threads())} luong)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_new = sub.add_parser("new", help="mo mot luong review moi")
    p_new.add_argument("slug")
    p_new.add_argument("--artifact", required=True, help="duong dan san pham dang review")
    p_new.add_argument("--author", required=True, choices=AGENTS)
    p_new.add_argument("--reviewers", required=True, help="vi du gemini,codex")
    p_new.add_argument("--question", required=True, help="cau hoi luong nay phai tra loi")
    p_new.add_argument("--step", help="so buoc trong bang o AGENTS.md muc 8")
    p_new.set_defaults(func=cmd_new)

    p_status = sub.add_parser("status", help="liet ke luong va diem con mo")
    p_status.add_argument("slug", nargs="?")
    p_status.set_defaults(func=cmd_status)

    p_next = sub.add_parser("next", help="in cau can dan cho agent toi luot")
    p_next.add_argument("slug")
    p_next.set_defaults(func=cmd_next)

    p_check = sub.add_parser("check", help="kiem tra tinh nhat quan cua cac luong")
    p_check.set_defaults(func=cmd_check)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
