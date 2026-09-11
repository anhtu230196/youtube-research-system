#!/usr/bin/env python3
"""Tao ban an nhan de doc mu.

    python blind.py opus sonnet haiku

Copy ban doc sach cua tung model thanh A.txt / B.txt / C.txt trong blind/,
tron ngau nhien, va ghi so tra o blind/KEY.md. Doc A/B/C truoc, mo KEY.md sau -
de nhan xet khong bi ten model dat truoc.
"""
import random
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent / "blind"
LABELS = "ABCDEF"


def clean_of(slug):
    folder = ROOT / slug
    cands = sorted(folder.glob("02b-*.txt")) if folder.exists() else []
    return cands[0] if cands else None


def main(slugs):
    pairs = []
    for s in slugs:
        p = clean_of(s)
        if p is None:
            print(f"  bo qua {s}: khong co ban doc sach")
            continue
        pairs.append((s, p))
    if len(pairs) < 2:
        print("  can it nhat hai ban de doc mu")
        return
    random.shuffle(pairs)
    OUT.mkdir(exist_ok=True)
    for old in OUT.glob("*.txt"):
        old.unlink()
    key = []
    for label, (slug, path) in zip(LABELS, pairs):
        text = path.read_text(encoding="utf-8")
        # bo dong tieu de / dong ghi ten model neu co, de khong lo nhan
        text = re.sub(r"(?im)^.*\b(opus|sonnet|haiku|astra|sol|gemini|claude|gpt)\b.*$\n?", "", text)
        body = f"# Ban {label}\n\n" + text.lstrip()
        (OUT / f"{label}.txt").write_text(body, encoding="utf-8")
        words = len([w for w in text.split() if w.strip()])
        key.append((label, slug, words))
        print(f"  {label}.txt  <-  {slug}  ({words:,} tu)")
    lines = [
        "# So tra ban an nhan",
        "",
        "Doc ba file `A.txt`, `B.txt`, `C.txt` truoc khi mo bang nay.",
        "",
        "| Ban | Model | So tu loi ke |",
        "| --- | --- | --- |",
    ]
    for label, slug, words in key:
        lines.append(f"| {label} | {slug} | {words:,} |")
    (OUT / "KEY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\n  so tra: {OUT / 'KEY.md'}")


if __name__ == "__main__":
    main(sys.argv[1:] or ["opus", "sonnet", "haiku"])
