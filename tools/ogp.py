#!/usr/bin/env python3
"""
🔗 LINE・X・Slack などにリンクを貼ったときの「カード」（OGP）を入れる

  python3 tools/ogp.py           全記事とトップ
  python3 tools/ogp.py <slug>    1本だけ

リンクを送ると、表紙のペンギンの絵・タイトル・最初の一文がカードで出る。
何も入れていないと、URL の文字だけが出る（2026-09-26 まで全ページそうだった）。

  絵      assets/thumbs-src/<slug>.jpg（1000×750 の表紙）
  題      meta.json の title
  説明    本文の最初のカードの、最初の文（英語）

<head> の中の目印にはさまれた部分だけを書き替える。手で書かない。
    <!-- ⬇️ OGP（tools/ogp.py） --> … <!-- ⬆️ OGP -->
"""
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://15-second-blog.com/"
START, END = "<!-- ⬇️ OGP（tools/ogp.py） -->", "<!-- ⬆️ OGP -->"
BLOCK = re.compile(re.escape(START) + r".*?" + re.escape(END) + r"\n?", re.S)


def first_sentence(doc: str) -> str:
    """最初のカードの最初の <p> の文字だけを取り出す。長ければ切る。"""
    m = re.search(r'<section class="card[^"]*"[^>]*>.*?<p[^>]*>(.*?)</p>', doc, re.S)
    if not m:
        return ""
    text = re.sub(r"<[^>]+>", "", m.group(1))
    text = re.sub(r"\s+", " ", html.unescape(text)).strip()
    return text if len(text) <= 150 else text[:147].rstrip() + "…"


def tags(title, desc, url, image, alt, kind, own_desc=False):
    a = lambda s: html.escape(s, quote=True)
    out = [START,
           # 手で書いた description がすでにある記事は、それを残して二重にしない
           f'<meta name="description" content="{a(desc)}" />' if desc and not own_desc else "",
           f'<meta property="og:type" content="{kind}" />',
           '<meta property="og:site_name" content="Pengesso ⚡ 15 Second Blog" />',
           f'<meta property="og:title" content="{a(title)}" />',
           f'<meta property="og:description" content="{a(desc)}" />' if desc else "",
           f'<meta property="og:url" content="{a(url)}" />',
           f'<meta property="og:image" content="{a(image)}" />',
           f'<meta property="og:image:alt" content="{a(alt)}" />' if alt else "",
           '<meta name="twitter:card" content="summary_large_image" />',
           END]
    return "\n".join(t for t in out if t) + "\n"


def put(page: pathlib.Path, block: str) -> bool:
    doc = before = page.read_text(encoding="utf-8")
    if START in doc:
        doc = BLOCK.sub(lambda _: block, doc, count=1)
    else:
        # <title> のすぐ下に入れる
        doc = re.sub(r"(<title>.*?</title>\n)", lambda m: m.group(1) + block, doc, count=1, flags=re.S)
        if START not in doc:
            raise SystemExit(f"❌ {page}: <title> が見つかりません")
    if doc != before:
        page.write_text(doc, encoding="utf-8")
        return True
    return False


def post(slug: str) -> bool:
    d = ROOT / "works" / slug
    meta = json.loads((d / "meta.json").read_text(encoding="utf-8"))
    idx = d / "index.html"
    doc = idx.read_text(encoding="utf-8")
    own = 'name="description"' in BLOCK.sub("", doc)
    img = ROOT / "assets" / "thumbs-src" / f"{slug}.jpg"
    if not img.exists():
        img = ROOT / "assets" / "thumbs" / f"{slug}.jpg"
    block = tags(meta.get("title", slug), first_sentence(doc),
                 f"{SITE}works/{slug}/", SITE + img.relative_to(ROOT).as_posix(),
                 meta.get("thumbAlt", ""), "article", own)
    return put(idx, block)


def top() -> bool:
    block = tags("Pengesso ⚡ 15 Second Blog",
                 "A penguin writes short posts for his owner. Every post takes about 15 seconds to read.",
                 SITE, SITE + "assets/pengesso/pengesso-01.jpg",
                 "Pengesso, a plush penguin in a blue cap and sunglasses", "website")
    return put(ROOT / "index.html", block)


def main_all():
    """build-site.py から呼ぶ。引数を見ずに全記事とトップ"""
    return run([])


def main():
    return run([a for a in sys.argv[1:] if not a.startswith("--")])


def run(args):
    slugs = args or sorted(p.name for p in (ROOT / "works").iterdir()
                           if (p / "meta.json").exists() and (p / "index.html").exists())
    n = sum(post(s) for s in slugs)
    if not args:
        n += top()
    print(f"✅ OGP を入れた／更新したページ: {n}")


if __name__ == "__main__":
    main()
