#!/usr/bin/env python3
"""⏭ 全記事の「次の記事へ」を、1本の道にそろえる（2026-09-25 本人の要望：次へを押していくとループする）。

前は、記事ごとに手で「次」を決めていたので、
  ・A → B → A のようにループする
  ・どこからも「次」で来られない記事がある
  ・「次」がない記事がある
が起きていた。これからは手で決めない。この道具が並べる。

並べ方：トップの一覧と同じ「新しい順」。
ただしシリーズ（Part 1・2・3 や、韓国の野球場のように同じ帯の記事）は、
そのシリーズのいちばん新しい記事の位置に、Part 1 → 2 → 3 の順でまとめて入れる。
いちばん最後（いちばん古い記事）の「次」は、トップの一覧へ。

使い方: python3 tools/next-links.py   → そのあと tools/prev-links.py → tools/i18n.py
何度走らせても同じ結果になる。記事を足したら毎回走らせる。
"""
import html, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
WORKS = ROOT / "works"

NEXT_RE = re.compile(r'[ \t]*(?:<!-- ⚡ 次の記事へ[^\n]*-->\s*)?<a class="next"[^>]*>.*?</a>[ \t]*\n?', re.S)
CSS_MARK = "/* ⏭ 次の記事へ（tools/next-links.py） */"
CSS = CSS_MARK + """
  .next { display: flex; align-items: center; justify-content: space-between; gap: 14px;
    margin-top: 34px; min-height: 44px; padding: 20px 24px; border-radius: 28px; text-decoration: none;
    background: linear-gradient(135deg, var(--purple, #8b6de8), var(--pink, #ff6fae)); color: #fff;
    box-shadow: 0 20px 55px rgba(0,0,0,.14); transition: transform .18s ease; }
  .next:hover, .next:focus-visible { transform: translateY(-4px); }
  .next-kicker { font-size: 11.5px; font-weight: 900; letter-spacing: .18em; opacity: .82; }
  .next-title { margin-top: 4px; font-size: clamp(17px, 3vw, 21px); line-height: 1.3; }
  .next-arrow { font-size: 26px; flex: 0 0 auto; }
  @media (prefers-reduced-motion: reduce) { .next { transition: none; } }
"""


def series_key(doc):
    m = re.search(r'<nav class="part-nav"[^>]*aria-label="([^"]*)"', doc)
    if m:
        return "nav:" + m.group(1)
    m = re.search(r'<div class="series"[^>]*>([^<]*)</div>', doc)
    if m:
        return "band:" + m.group(1).strip()
    return None


def order():
    posts = {}
    for d in WORKS.iterdir():
        if (d / "index.html").exists() and (d / "meta.json").exists():
            m = json.loads((d / "meta.json").read_text())
            posts[d.name] = {"seq": m.get("seq", 0), "title": m.get("title", d.name),
                             "series": series_key((d / "index.html").read_text())}
    groups = {}
    for s, p in posts.items():
        if p["series"]:
            groups.setdefault(p["series"], []).append(s)
    out, done = [], set()
    for s in sorted(posts, key=lambda x: -posts[x]["seq"]):
        if s in done:
            continue
        g = posts[s]["series"]
        members = sorted(groups[g], key=lambda x: posts[x]["seq"]) if g else [s]
        for x in members:
            out.append(x); done.add(x)
    return posts, out


def block(target, posts):
    if target is None:
        return ('  <a class="next" href="../../index.html">\n    <div>\n'
                '      <div class="next-kicker">NEXT · ALL POSTS</div>\n'
                '      <div class="next-title">See all 15-second posts</div>\n    </div>\n'
                '    <div class="next-arrow" aria-hidden="true">⚡</div>\n  </a>\n')
    t = html.escape(posts[target]["title"], quote=False)
    return (f'  <a class="next" href="../{target}/index.html">\n    <div>\n'
            '      <div class="next-kicker">NEXT · 15 SEC</div>\n'
            f'      <div class="next-title">{t}</div>\n    </div>\n'
            '    <div class="next-arrow" aria-hidden="true">⚡</div>\n  </a>\n')


def main():
    posts, seq = order()
    changed = 0
    for i, s in enumerate(seq):
        target = seq[i + 1] if i + 1 < len(seq) else None
        p = WORKS / s / "index.html"
        doc = p.read_text()
        new_block = block(target, posts)
        main_end = doc.rindex("</main>")
        m = NEXT_RE.search(doc, 0, main_end)
        if m:
            new = doc[:m.start()] + new_block + doc[m.end():]
        else:
            k = doc.find("<!-- ⏮ 前の記事へ", 0, main_end)
            at = k if k >= 0 else main_end
            new = doc[:at] + new_block + doc[at:]
        if not re.search(r"\.next\s*\{", new) and CSS_MARK not in new:
            new = new.replace("</style>", CSS + "</style>", 1)
        if new != doc:
            p.write_text(new)
            changed += 1
    print(f"⏭ 次の記事へ：{len(seq)}本を1本の道に並べた（{changed}本を書き換え）。最初は {seq[0]}、最後は {seq[-1]} → トップ")


def verify():
    """check.py から呼ぶ：ループ・行き止まり・たどり着けない記事がないか"""
    posts, _ = order()
    nx = {}
    for s in posts:
        m = re.search(r'<a class="next" href="\.\./([^/"]+)/index\.html"', (WORKS / s / "index.html").read_text())
        nx[s] = m.group(1) if m and m.group(1) != ".." else None
    problems = [f"{s}：次の記事がありません" for s in posts if s not in nx]
    heads = [s for s in posts if s not in set(nx.values())]
    if len(heads) != 1:
        problems.append(f"「次」でたどり着けない記事が {len(heads)} 本あります（1本だけのはず）: {heads[:5]}")
    seen, cur = set(), heads[0] if heads else None
    while cur and cur not in seen:
        seen.add(cur); cur = nx.get(cur)
    if cur:
        problems.append(f"ループしています：{cur} に戻ってきます")
    elif len(seen) != len(posts):
        problems.append(f"1本の道にならず、{len(posts) - len(seen)} 本がはぐれています")
    return problems


if __name__ == "__main__":
    main()
