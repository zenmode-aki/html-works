#!/usr/bin/env python3
"""
📱 記事に埋め込んだ写真（base64）を、別のファイル（記事フォルダの img/）に出す（2026-10-04）

  python3 tools/unembed.py              全記事（works/ と draft/）
  python3 tools/unembed.py pawapuro     1本だけ
  python3 tools/unembed.py --check      まだ埋め込んだままの写真がないか見るだけ

なぜ：本人「パソコンは十分だけど、iPhone で開くとなぜかあかん」。
  記事の重さの91%が埋め込みの写真だった（真ん中の記事で308KB、500KB超えが59本、最大1.5MB）。
  埋め込みだと、写真を全部読み終わるまで本文の訳も動きも始まらず、iPhone では重い HTML を
  メモリに抱えたままになる。別ファイルにすると、本文がすぐ出て、写真はスクロールに合わせて読む。

やること
  - <img src="data:image/…;base64,…"> と style の url(data:image/…) を、img/<中身の指紋>.jpg などに書き出す
    （写真のデータは1バイトも変えない＝画質はそのまま。同じ写真は同じ名前＝何度走らせても同じ結果）
  - <img> に width / height を付ける（読み込み中に下の文がガタッと動かないように）
  - 1枚目（表紙）はすぐ読む（fetchpriority="high"）。2枚目からはスクロールして近づいてから（loading="lazy"）
  - 小さい飾り（4KB 未満）は埋め込みのまま（ファイルを増やすほうが遅い）
"""
import base64, hashlib, io, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MIN_BYTES = 4 * 1024
EXT = {"jpeg": "jpg", "jpg": "jpg", "png": "png", "webp": "webp", "gif": "gif", "avif": "avif"}
B64 = r"data:image/(jpeg|jpg|png|webp|gif|avif);base64,([A-Za-z0-9+/=\s]+)"
IMG_RE = re.compile(r"<img\b[^>]*>", re.S)
SRC_RE = re.compile(r'\bsrc="' + B64 + '"')
URL_RE = re.compile(r"url\((['\"]?)" + B64 + r"\1\)")

try:
    from PIL import Image
except Exception:            # PIL がなくても動く（width/height を付けないだけ）
    Image = None


def size_of(raw):
    if not Image:
        return None
    try:
        with Image.open(io.BytesIO(raw)) as im:
            return im.size
    except Exception:
        return None


def write(page_dir, kind, data):
    raw = base64.b64decode(re.sub(r"\s+", "", data))
    if len(raw) < MIN_BYTES:
        return None, raw
    name = hashlib.sha1(raw).hexdigest()[:12] + "." + EXT[kind]
    out = page_dir / "img" / name
    if not out.exists():
        out.parent.mkdir(exist_ok=True)
        out.write_bytes(raw)
    return "img/" + name, raw


def process(page: pathlib.Path):
    doc = page.read_text(encoding="utf-8")
    d = page.parent
    n = [0, 0]                                   # [書き出した数, 書き出した写真の中で何枚目か]

    def fix_img(m):
        tag = m.group(0)
        s = SRC_RE.search(tag)
        if not s:
            return tag
        path, raw = write(d, s.group(1), s.group(2))
        if not path:
            return tag
        n[0] += 1; n[1] += 1
        tag = tag[:s.start()] + f'src="{path}"' + tag[s.end():]
        wh = size_of(raw)
        if wh and not re.search(r"\bwidth=", tag):
            tag = re.sub(r"^<img\b", f'<img width="{wh[0]}" height="{wh[1]}"', tag)
        if "decoding=" not in tag:
            tag = re.sub(r"^<img\b", '<img decoding="async"', tag)
        if "loading=" not in tag and "fetchpriority=" not in tag:
            # 1枚目は表紙（題のすぐ下）。すぐ読む。2枚目からはスクロールして近づいてから
            extra = 'fetchpriority="high"' if n[1] == 1 else 'loading="lazy"'
            tag = re.sub(r"^<img\b", f"<img {extra}", tag)
        return tag

    def fix_url(m):
        path, _ = write(d, m.group(2), m.group(3))
        if not path:
            return m.group(0)
        n[0] += 1
        return f"url('{path}')"

    new = IMG_RE.sub(fix_img, doc)
    new = URL_RE.sub(fix_url, new)
    if new != doc:
        page.write_text(new, encoding="utf-8")
    return n[0], len(doc.encode()), len(new.encode())


def leftovers(page):
    doc = page.read_text(encoding="utf-8")
    big = 0
    for m in re.finditer(B64, doc):
        if len(m.group(2)) * 3 // 4 >= MIN_BYTES:
            big += 1
    return big


def pages(args):
    slugs = [a for a in args if not a.startswith("--")]
    out = []
    for base in ("works", "draft"):
        for p in sorted((ROOT / base).glob("*/index.html")):
            if not slugs or p.parent.name in slugs:
                out.append(p)
    return out


def main():
    args = sys.argv[1:]
    if "--check" in args:
        bad = [(p, leftovers(p)) for p in pages(args)]
        bad = [(p, k) for p, k in bad if k]
        if bad:
            print("❌ 写真が HTML に埋め込まれたままです → python3 tools/unembed.py")
            for p, k in bad[:20]:
                print(f"   {p.relative_to(ROOT)}（{k}枚）")
            sys.exit(1)
        print("✅ 写真はぜんぶ別ファイル（img/）です")
        return
    tot_n = tot_a = tot_b = 0
    for p in pages(args):
        k, a, b = process(p)
        if k:
            tot_n += k; tot_a += a; tot_b += b
            print(f"  📸 {p.relative_to(ROOT)}: {k}枚  {a // 1024}KB → {b // 1024}KB")
    if tot_n:
        print(f"✅ {tot_n}枚を img/ に出した。HTML の合計 {tot_a / 1e6:.1f}MB → {tot_b / 1e6:.1f}MB")
    else:
        print("✅ 埋め込みの写真はありません")


if __name__ == "__main__":
    main()
