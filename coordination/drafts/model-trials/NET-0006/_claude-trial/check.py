#!/usr/bin/env python3
"""Kiem phan dem duoc cua mot ban thu kich ban NET-0006.

    python check.py opus sonnet haiku astra sol

Hai tang:
  CHAN  - lech may moc, khong can doc tay: so nhip, thu tu, ban doc sach khong
          khop ban chu thich, ngay viet dang so, ten nghi pham lo som, CTA.
  DOC   - tu khoa dang nghi, in kem ngu canh de nguoi doc tu ket luan. Nhieu
          ban viet dung lai trung tu khoa (vi du "khong co loi thu toi"), nen
          may khong tu ket luan o tang nay.

Khong cham van chuong - phan do Tu doc.
"""
import re
import sys
import unicodedata
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
BEATS = [f"B{i:02d}" for i in range(1, 15)]


def fold(s):
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn").replace("đ", "d")


def strip_comments(s):
    return re.sub(r"<!--.*?-->", " ", s, flags=re.S)


MARKER = re.compile(r"<!--\s*NARRATION_START\s*-->(.*?)<!--\s*NARRATION_END\s*-->", re.S)


def marker_pairs(md_text):
    """So cap moc NARRATION. 1 = dung nhu prompt yeu cau; 14 = dat quanh tung nhip."""
    return len(MARKER.findall(md_text))


def beat_narration(beat_text):
    """Loi ke cua mot nhip, chiu ca hai dang dat moc."""
    inner = MARKER.findall(beat_text)
    return strip_comments(" ".join(inner) if inner else beat_text)


def split_beats(md_text):
    """{'B01': loi ke, ...} - tach ca file theo heading nhip, roi lay loi ke tung nhip.

    Chiu ca hai dang dat moc NARRATION: mot cap quanh ca bai (dang prompt yeu cau)
    thi cat theo cap do truoc khi tach nhip - de danh muc nguon sau NARRATION_END
    khong bi tinh vao B14. Nhieu cap (mot cap moi nhip) thi lay phan trong tung nhip.
    Phan mo dau truoc B01 (tieu de, dong ghi chu ban thu) bi bo, dung y muon.
    """
    if marker_pairs(md_text) == 1:
        md_text = MARKER.search(md_text).group(1)
    out, order = {}, []
    parts = re.split(r"^#{2,6}\s*(B\d{2})\b[^\n]*$", md_text, flags=re.M)
    for i in range(1, len(parts), 2):
        order.append(parts[i])
        out[parts[i]] = beat_narration(parts[i + 1])
    return out, order


def narration(md_text):
    beats, order = split_beats(md_text)
    if order:
        return " ".join(beats[c] for c in order)
    m = MARKER.search(md_text)
    return strip_comments(m.group(1) if m else md_text)


def words(s):
    return len([w for w in s.split() if w.strip()])


def ctx(text, *keywords, width=110, exact=False):
    """Cac doan van co tu khoa, kem ngu canh hai ben.

    exact=True thi so khop co dau. Can cho nhung tu ma dau quyet dinh nghia:
    bo dau thi "dan dung" trung voi "dan dung" trong "loai dan dung trong vu an",
    va bo kiem se bao sai la lo loi giai truoc B11.
    """
    hay = text.lower() if exact else fold(text)
    hits = []
    for kw in keywords:
        needle = kw.lower() if exact else fold(kw)
        for m in re.finditer(re.escape(needle), hay):
            a, b = max(0, m.start() - width), min(len(text), m.end() + width)
            hits.append((kw, " ".join(text[a:b].split())))
    return hits


def check(slug):
    md = ROOT / slug / f"02-script-vi-{slug}.md"
    folder = ROOT / slug
    txt = None
    if folder.exists():
        cands = sorted(folder.glob("02b-*.txt"))
        txt = cands[0] if cands else None
    print(f"\n{'=' * 70}\n  {slug.upper()}\n{'=' * 70}")
    if not md.exists():
        print(f"  THIEU FILE: {md}")
        return None
    text = md.read_text(encoding="utf-8")
    beats, order = split_beats(text)
    nar = narration(text)
    hard, look, thieu = [], [], []

    def seg(*c):
        return " ".join(beats.get(x, "") for x in c)

    # ---- tang CHAN -------------------------------------------------------
    if order != BEATS:
        hard.append(f"nhip lech: doc duoc {len(order)} heading, thieu "
                    f"{[b for b in BEATS if b not in order] or 'khong'}, "
                    f"lap {sorted(b for b in set(order) if order.count(b) > 1) or 'khong'}")

    wn = words(nar)
    if not 3000 <= wn <= 5200:
        hard.append(f"do dai {wn:,} tu - ngoai khoang da yeu cau (3.500-4.500)")

    leak = ctx(seg("B01", "B02", "B03", "B04", "B05"), "Lazarus", "Stephanie")
    if leak:
        hard.append(f"ten nghi pham lo truoc B06 ({len(leak)} cho)")
        look += [("ten lo som", c) for _, c in leak[:3]]

    if ctx(beats.get("B01", ""), "BMW"):
        hard.append("B01 neu chiec BMW - hook chi dung C03 (beat sheet D01/D12)")

    if re.search(r"\b(?:0?9[/.-]10|10[/.-]0?9)(?:[/.-]20?26)?\b", nar):
        hard.append("ngay dieu tran viet dang so - beat sheet D16 buoc viet bang chu")

    b14 = beats.get("B14", "")
    sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", b14.strip()) if s.strip()]
    cta = [s for s in sents if ctx(s, "dang ky", "theo doi kenh", "bam chuong", "kenh nay", "kenh cua")]
    if len(cta) != 1:
        hard.append(f"CTA phai dung mot cau, dem duoc {len(cta)}")
    elif sents and cta[0] != sents[-1]:
        hard.append("cau CTA khong dat cuoi B14")

    wt = None
    if txt is None or not txt.exists():
        hard.append("thieu ban doc sach 02b-*.txt")
    else:
        t = txt.read_text(encoding="utf-8")
        wt = words(t)
        if "<!--" in t:
            hard.append("ban doc sach con chu thich HTML")
        stray = sorted(set(re.findall(r"\b(?:B\d{2}|C\d{2}|S\d{2})\b", t)))
        if stray:
            hard.append(f"ban doc sach con ma ky thuat: {stray}")
        if re.search(r"^#{1,6}\s", t, re.M):
            hard.append("ban doc sach con heading markdown")
        drift = abs(wt - wn) / max(wn, 1)
        if drift > 0.06:
            hard.append(f"ban doc sach lech {drift:.0%} so voi loi ke ({wt:,} vs {wn:,} tu) "
                        f"- dau hieu viet lai lan hai thay vi loc ra")

    # ---- tang DOC --------------------------------------------------------
    probes = [
        ("dan dung truoc B11", seg(*BEATS[:10]), ("dàn dựng", "dựng hiện trường", "sắp đặt hiện trường"), True),
        ("nghe canh sat o B04", beats.get("B04", ""), ("LAPD", "tham tu", "si quan", "dong nghiep", "nu canh sat"), False),
        ("tu thu toi", nar, ("thú tội", "nhận tội"), True),
        ("13 loci o B09", beats.get("B09", ""), ("13 vi tri", "muoi ba vi tri", "13 loci"), False),
        ("cover-up o B12", beats.get("B12", ""), ("bao che", "am muu"), False),
    ]
    for label, text_, kws, exact in probes:
        for kw, snippet in ctx(text_, *kws, exact=exact)[:3]:
            look.append((f"{label} [{kw}]", snippet))

    # Bac thang cang chinh cua tap: nghi pham la tham tu LAPD duong chuc. Khung suon
    # dat o B06 ("nang muc cang vi nghi pham o trong nganh"). Kiem nay them sau khi
    # doc tay phat hien mot ban khong he neu chi tiet nay o bat ky dau.
    if not ctx(nar, "LAPD", "tham tu", "si quan canh sat"):
        thieu.append("CA BAI: khong he neu nghi pham la tham tu LAPD - mat bac thang cang chinh")
    elif not ctx(beats.get("B06", ""), "LAPD", "tham tu"):
        thieu.append("B06: khong neu tu cach tham tu LAPD (khung suon dat o day)")

    # Cac moc so loci va phan phan bien: cach dien dat bien thien qua nhieu de may tu
    # ket luan la thieu. Vi du Opus viet "khong phai muoi mot vi tri doc duoc, ma muoi
    # ba. Khop ca muoi ba" va goi van tay la "dau tay" — bo kiem ban dau bao thieu sai
    # ca hai. Tang nay chi in ra chinh cai no tim duoc, nguoi doc tu xac nhan.
    def near(text_, number_forms, dna_words, window=70):
        """Tim mot dang so nam gan mot tu thuoc ngu canh DNA."""
        f = fold(text_)
        for nf in number_forms:
            for m in re.finditer(re.escape(fold(nf)), f):
                a, b = max(0, m.start() - window), min(len(f), m.end() + window)
                if any(fold(w) in f[a:b] for w in dna_words):
                    s, e = max(0, m.start() - 90), min(len(text_), m.end() + 90)
                    return " ".join(text_[s:e].split())
        return None

    DNA = ("vi tri", "loci", "khop", "ho so", "profile")
    for label, where, forms in [
        ("11 (mau coc) o B07", beats.get("B07", ""), ("11", "muoi mot")),
        ("13 (mau truc tiep) o B10", beats.get("B10", ""), ("13", "muoi ba")),
        ("15 (SERI) o B10", beats.get("B10", ""), ("15", "muoi lam")),
    ]:
        found = near(where, forms, DNA)
        look.append((f"moc {label}", found if found else ">>> KHONG TIM THAY <<<"))

    for k, alts in [("phong bi", ("phong bi",)), ("sung", ("sung", "Model 49")),
                    ("dau tay/van tay", ("van tay", "dau tay"))]:
        hits = ctx(beats.get("B10", ""), *alts)
        look.append((f"phan bien B10 [{k}]",
                     hits[0][1] if hits else ">>> KHONG TIM THAY <<<"))
    if not ctx(beats.get("B13", ""), "thang 10 nam 2026", "thang Muoi nam 2026"):
        thieu.append("B13: khong thay ngay dieu tran dang chu")
    if not ctx(beats.get("B11", ""), "loi khai", "chuyen gia", "theo cong to", "Safarik"):
        thieu.append("B11: khong thay quy nguon cho chuyen gia cong to")

    # ---- in ra -----------------------------------------------------------
    pairs = marker_pairs(text)
    print(f"  nhip      : {len(order)}/14 {'dung thu tu' if order == BEATS else 'LECH'}")
    print(f"  tu loi ke : {wn:,}" + (f"   |  ban doc sach: {wt:,}" if wt else ""))
    print(f"  cau CTA   : {len(cta)}")
    print(f"  cap moc   : {pairs} " + ("(dung nhu prompt)" if pairs == 1
                                       else "(prompt yeu cau 1 cap quanh ca bai)"))
    print()
    for h in hard:
        print(f"  CHAN : {h}")
    for t_ in thieu:
        print(f"  THIEU: {t_}")
    if look:
        print("\n  -- doc tay (tu khoa dang nghi, may khong tu ket luan) --")
        for label, snippet in look:
            print(f"  DOC  : {label}\n         ...{snippet}...")
    if not hard and not thieu:
        print("  OK   : khong lech may moc, khong thieu moc bat buoc")
    print(f"\n  tong: {len(hard)} CHAN, {len(thieu)} THIEU, {len(look)} diem doc tay")
    return {"slug": slug, "words": wn, "clean": wt, "beats": len(order),
            "order_ok": order == BEATS, "hard": len(hard), "thieu": len(thieu)}


if __name__ == "__main__":
    rows = [r for r in (check(s) for s in (sys.argv[1:] or ["opus", "sonnet", "haiku"])) if r]
    if len(rows) > 1:
        print(f"\n{'=' * 70}\n  BANG TOM\n{'=' * 70}")
        print(f"  {'ban':10} {'nhip':>6} {'tu':>8} {'sach':>8} {'CHAN':>6} {'THIEU':>6}")
        for r in rows:
            print(f"  {r['slug']:10} {r['beats']:>4}/14 {r['words']:>8,} "
                  f"{(r['clean'] or 0):>8,} {r['hard']:>6} {r['thieu']:>6}")
