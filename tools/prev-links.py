#!/usr/bin/env python3
"""⏮ 全記事に「前の記事へ」ボタンを付ける（2026-09-25 本人の要望）。

前の記事 ＝ その記事を「次の記事」に指している記事。
何本もあるときは seq（公開順）がすぐ前のもの。どこからも指されていないときは seq がひとつ前の記事。
何度走らせても同じ結果になる（前に入れたボタンは消してから入れ直す）。

使い方: python3 tools/prev-links.py     （記事を足したり、次の記事を変えたら走らせる → そのあと tools/i18n.py）
"""
import json, pathlib, re, html

ROOT = pathlib.Path(__file__).resolve().parent.parent
WORKS = ROOT / "works"

START, END = "<!-- ⏮ 前の記事へ（tools/prev-links.py） -->", "<!-- /⏮ -->"
CSS = """<style id="prev-css">
  /* ⏮ 前の記事へ（tools/prev-links.py が入れる） */
  .prev { display: flex; align-items: center; gap: 12px; margin-top: 12px; min-height: 44px; padding: 13px 18px;
    border-radius: 20px; text-decoration: none; color: inherit; background: rgba(255,255,255,.72);
    border: 2px dashed rgba(0,0,0,.14); transition: transform .18s ease, background .18s ease; }
  .prev:hover, .prev:focus-visible { transform: translateX(-4px); background: rgba(255,255,255,.95); }
  .prev-arrow { flex: none; display: grid; place-items: center; width: 34px; height: 34px; border-radius: 50%;
    background: rgba(0,0,0,.07); font-size: 17px; font-weight: 900; }
  .prev-kicker { font-size: 11px; font-weight: 900; letter-spacing: .16em; opacity: .65; }
  .prev-title { margin-top: 2px; font-size: 15px; font-weight: 800; line-height: 1.35; }
  html[data-theme="dark"] .prev { background: #22242f; border-color: rgba(255,255,255,.16); color: #ece8f3; }
  html[data-theme="dark"] .prev-arrow { background: rgba(255,255,255,.1); }
  @media (prefers-reduced-motion: reduce) { .prev { transition: none; } }
</style>
"""
NEXT_RE = re.compile(r'<a class="next" href="\.\./([^/"]+)/index\.html"')
BLOCK_RE = re.compile(r"\n?[ \t]*" + re.escape(START) + r".*?" + re.escape(END) + r"\n?", re.S)
CSS_RE = re.compile(r'<style id="prev-css">.*?</style>\n?', re.S)


def main():
    posts = {}
    for d in sorted(WORKS.iterdir()):
        if (d / "index.html").exists() and (d / "meta.json").exists():
            posts[d.name] = json.loads((d / "meta.json").read_text())
    seq = {s: m.get("seq", 0) for s, m in posts.items()}
    by_seq = sorted(posts, key=lambda s: seq[s])

    incoming = {}
    for s in posts:
        m = NEXT_RE.search((WORKS / s / "index.html").read_text())
        if m and m.group(1) in posts and m.group(1) != s:
            incoming.setdefault(m.group(1), []).append(s)

    changed = 0
    for s in posts:
        cands = incoming.get(s, [])
        if cands:
            before = [c for c in cands if seq[c] < seq[s]]
            prev = max(before or cands, key=lambda c: seq[c])
        else:
            i = by_seq.index(s)
            prev = by_seq[i - 1] if i > 0 else None

        p = WORKS / s / "index.html"
        doc = p.read_text()
        new = CSS_RE.sub("", BLOCK_RE.sub("\n", doc))
        if prev:
            title = html.escape(posts[prev]["title"], quote=False)
            block = (f"  {START}\n"
                     f'  <a class="prev" href="../{prev}/index.html">\n'
                     f'    <span class="prev-arrow" aria-hidden="true">←</span>\n'
                     f'    <div>\n      <div class="prev-kicker">PREVIOUS POST</div>\n'
                     f'      <div class="prev-title">{title}</div>\n    </div>\n  </a>\n  {END}\n')
            m = re.search(r'<a class="next"[^>]*>.*?</a>\n?', new, re.S)
            if m:
                new = new[:m.end()] + block + new[m.end():]
            else:
                i = new.rindex("</main>")
                new = new[:i] + block + new[i:]
            new = new.replace("</head>", CSS + "</head>", 1)
        if new != doc:
            p.write_text(new)
            changed += 1
    print(f"⏮ 前の記事へ：{len(posts)}本を確認、{changed}本を書き換え")

    # 📚 そのあとで、秒数の札と「一覧に戻る」ボタンを入れ直す（前の記事ボタンのすぐ下に置くので、ここで呼ぶ）
    import importlib.util as _ilu
    _s = _ilu.spec_from_file_location("post_bottom", ROOT / "tools" / "post-bottom.py")
    _m = _ilu.module_from_spec(_s); _s.loader.exec_module(_m); _m.main()


if __name__ == "__main__":
    main()
