#!/usr/bin/env python3
"""Chay luong review tu dong bang CLI cua tung agent, khong goi API.

Moi luot goi CLI tuong ung o che do headless, lay stdout lam file vong, roi
cap nhat THREAD.md. Luot review chay che do chi doc; chi luot tac gia moi duoc
sua artifact. Xem AGENTS.md muc 8.

    python scripts/orchestrate.py doctor            # CLI nao dung duoc
    python scripts/orchestrate.py doctor --probe    # goi thu mot cau ngan
    python scripts/orchestrate.py turn <slug>       # chay dung mot luot
    python scripts/orchestrate.py run <slug>        # chay den khi hoi tu
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import thread as th  # noqa: E402

CONFIG = Path(__file__).resolve().parents[1] / "coordination" / "agents.json"
MAX_TURNS = 12

# Dau hieu het quota / bi chan toc do trong dau ra cua CLI. Phan biet voi loi
# that vi cach xu ly khac han: doi, doi tai khoan, hoac de agent khac nhan luot.
QUOTA_MARKS = ("429", "quota", "rate limit", "ratelimit", "resource_exhausted",
               "resource exhausted", "usage limit", "overloaded", "too many requests")


def looks_like_quota(*chunks: str) -> bool:
    blob = " ".join(c or "" for c in chunks).lower()
    return any(m in blob for m in QUOTA_MARKS)

PREAMBLE_READ = """Ban dang chay o che do TU DONG, khong co nguoi doc man hinh cua ban.

Luat cua che do nay:
- KHONG tao hay sua bat ky file nao. Ban chi doc.
- KHONG sua THREAD.md. Orchestrator lo viec do.
- In TOAN BO noi dung file vong ra stdout, khong in gi khac ngoai no.
- Bat buoc co mot khoi ```points``` o cuoi, moi diem mot dong.

"""

PREAMBLE_WRITE = """Ban dang chay o che do TU DONG, khong co nguoi doc man hinh cua ban.

Luat cua che do nay:
- Ban DUOC sua file artifact neu luot nay yeu cau sua.
- KHONG tao file vong tren dia va KHONG sua THREAD.md. Orchestrator lo viec do.
- In TOAN BO noi dung file vong ra stdout, khong in gi khac ngoai no.
- Bat buoc co mot khoi ```points``` o cuoi, moi diem mot dong.

"""

POINTS_CONTRACT = """

Khoi points o cuoi file, dinh dang moi dong: D<so> | <trang thai> | <cho> | <tom tat>

```points
D01 | mở | scripts/vi-du.md:44 | Gan trang thai tam ly khong co nguon
```

Trang thai hop le, chep dung nguyen van mot trong cac chuoi sau:
  mở
  đã sửa ở v<N>
  tác giả phản bác — chờ <agent>
  chốt: đã sửa
  chốt: giữ nguyên
  đẩy lên Tú
"""


def load_config() -> dict:
    if not CONFIG.exists():
        sys.exit(f"khong tim thay {CONFIG}")
    return json.loads(CONFIG.read_text(encoding="utf-8"))["agents"]


PROBE_TIMEOUT = 60
IS_WIN = os.name == "nt"


def kill_tree(proc: subprocess.Popen) -> None:
    """Giet ca cay tien trinh. Giet moi tien trinh cha khong du: cac CLI la
    shim goi node, va con chau con song se giu ong dan mai."""
    if IS_WIN:
        subprocess.run(["taskkill", "/F", "/T", "/PID", str(proc.pid)],
                       capture_output=True)
        return
    try:
        os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
    except (ProcessLookupError, PermissionError):
        proc.kill()


def run_cli(spec: dict, prompt: str, write: bool, timeout: int | None = None):
    """Goi CLI, tra ve (ma thoat, stdout, stderr, giay)."""
    template = spec["write_cmd" if write else "cmd"]
    cmd = [prompt if part == "{prompt}" else part.replace("{prompt}", prompt)
           for part in template]
    # Tren Windows, subprocess khong tu ap dung PATHEXT: "gemini" khong chay,
    # phai la duong dan day du toi gemini.CMD.
    resolved = shutil.which(cmd[0])
    if resolved:
        cmd[0] = resolved
    secs_cap = timeout or spec.get("timeout", 600)
    t0 = time.time()
    try:
        proc = subprocess.Popen(
            cmd, cwd=th.repo_root(),
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            # Khong co stdin: cac CLI headless doi du lieu ong dan va treo
            # 3-30s neu de mac dinh.
            stdin=subprocess.DEVNULL,
            text=True, encoding="utf-8", errors="replace",
            **({} if IS_WIN else {"start_new_session": True}))
    except FileNotFoundError:
        return 127, "", f"khong tim thay lenh {cmd[0]!r}", 0.0

    try:
        out, err = proc.communicate(timeout=secs_cap)
        return proc.returncode, out or "", err or "", time.time() - t0
    except subprocess.TimeoutExpired:
        # subprocess.run(timeout=) mot minh khong du: no giet tien trinh cha
        # nhung con chau van giu ong dan, va communicate() cho vo han. Cac CLI
        # nay deu la shim goi node nen luon co con chau.
        kill_tree(proc)
        try:
            out, err = proc.communicate(timeout=15)
        except subprocess.TimeoutExpired:
            out, err = "", ""
        return 124, out or "", (err or "") + f"\nqua {secs_cap}s — da giet cay tien trinh", \
            time.time() - t0


def cmd_doctor(args) -> int:
    agents = load_config()
    bad = 0
    for name, spec in agents.items():
        installed = shutil.which(spec["bin"]) is not None
        mark = "co" if installed else "CHUA CAI"
        flag = "" if spec.get("verified") else "  [co CHUA KIEM CHUNG]"
        print(f"{name:<8} {mark:<9}{flag}")
        if spec.get("note"):
            print(f"         {spec['note']}")
        if not installed:
            bad += 1
            continue
        if args.probe:
            code, out, err, secs = run_cli(spec, "Tra loi dung mot tu: OK",
                                           write=False, timeout=PROBE_TIMEOUT)
            first = (out.strip().splitlines() or [""])[0][:60]
            if code == 0 and first:
                print(f"         probe: OK ({secs:.1f}s) — {first!r}")
            elif looks_like_quota(err, out):
                bad += 1
                print(f"         probe: HET QUOTA / BI CHAN TOC DO ({secs:.0f}s)")
            else:
                bad += 1
                msg = (err.strip().splitlines() or ["khong co stderr"])[-1][:120]
                print(f"         probe: LOI (ma {code}, {secs:.0f}s) — {msg}")
    return 1 if bad else 0


def one_turn(slug: str, agents: dict, dry: bool) -> str:
    """Chay mot luot. Tra ve status cua luong sau luot do."""
    d, data, text = th.read_thread(slug)
    t = th.turn_prompt(d, data)
    if t is None:
        print(f"Luong {slug} dang {data.get('status')} — khong co luot nao de chay.")
        return str(data.get("status"))

    agent = t["turn"]
    spec = agents.get(agent)
    if spec is None:
        sys.exit(f"coordination/agents.json khong co cau hinh cho {agent!r}.")
    if shutil.which(spec["bin"]) is None:
        print(f"DUNG: toi luot {agent} nhung chua cai {spec['bin']!r}.")
        print(f"      {spec.get('note', '')}")
        return "blocked-cli"

    preamble = PREAMBLE_WRITE if t["needs_write"] else PREAMBLE_READ
    prompt = preamble + t["prompt"] + POINTS_CONTRACT

    print(f"--- vong {t['round']}/{th.MAX_ROUND} · {agent} ({t['role']}) "
          f"-> {t['file']} {'[sua duoc artifact]' if t['needs_write'] else '[chi doc]'}")
    if dry:
        print(prompt)
        return "dry"

    code, out, err, secs = run_cli(spec, prompt, write=t["needs_write"])
    if code != 0 or not out.strip():
        if looks_like_quota(err, out):
            print(f"    HET QUOTA hoac BI CHAN TOC DO sau {secs:.0f}s.")
            print("    Phan lon thoi gian do la CLI tu thu lai, khong phai lam viec.")
            print("    Doi quota hoi, doi tai khoan, hoac de agent khac nhan luot nay.")
            print("    THREAD.md khong bi doi — chay lai lenh nay sau la duoc.")
            return "quota"
        print(f"    LOI: ma thoat {code} sau {secs:.0f}s")
        for line in (err.strip().splitlines() or ["khong co stderr"])[-5:]:
            print(f"    {line[:160]}")
        return "error"

    t["path"].write_text(out, encoding="utf-8")
    print(f"    da ghi {t['path'].relative_to(th.repo_root()).as_posix()} ({secs:.0f}s)")

    block = th.parse_points_block(out)
    if block is None or isinstance(block, str):
        reason = block if isinstance(block, str) else "khong co khoi ```points```"
        print(f"    KHONG AP DUNG DUOC: {reason}")
        print("    File vong da giu lai. Sua tay roi chay: "
              f"python scripts/thread.py apply {slug} {t['file']}")
        return "needs-human"

    new_text, notes, status = th.advance(
        d, data, text, agent, block, bump_version=(t["kind"] == "response"))
    (d / "THREAD.md").write_text(new_text, encoding="utf-8")
    for n in notes:
        print(f"    ghi chu: {n}")
    print(f"    {len(block)} diem · luong -> {status}")
    return status


def cmd_turn(args) -> int:
    status = one_turn(args.slug, load_config(), args.dry_run)
    return 0 if status in ("open", "settled", "dry") else 1


def cmd_run(args) -> int:
    agents = load_config()
    for i in range(args.max_turns):
        status = one_turn(args.slug, agents, dry=False)
        if status != "open":
            print(f"\nDung o luot {i + 1}: {status}")
            if status == "settled":
                print("Luong da chot. Doc lai cac file vong truoc khi tin ket qua.")
            elif status == "blocked":
                print("Con diem mo sau khi het tran vong — can Tu quyet.")
            elif status == "quota":
                print("Luong giu nguyen trang thai. Chay lai `run` sau khi quota hoi.")
            return 0 if status == "settled" else 1
    print(f"\nDung vi cham tran {args.max_turns} luot.")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p_doc = sub.add_parser("doctor", help="kiem tra CLI nao dung duoc")
    p_doc.add_argument("--probe", action="store_true", help="goi thu mot cau ngan")
    p_doc.set_defaults(func=cmd_doctor)

    p_turn = sub.add_parser("turn", help="chay dung mot luot")
    p_turn.add_argument("slug")
    p_turn.add_argument("--dry-run", action="store_true", help="chi in prompt, khong goi CLI")
    p_turn.set_defaults(func=cmd_turn)

    p_run = sub.add_parser("run", help="chay den khi hoi tu hoac het tran")
    p_run.add_argument("slug")
    p_run.add_argument("--max-turns", type=int, default=MAX_TURNS)
    p_run.set_defaults(func=cmd_run)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
