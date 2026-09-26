#!/usr/bin/env python3
"""
📚 記事の「読むのにかかる秒数」と、いちばん下の「一覧に戻る」ボタン（2026-09-26 本人の要望）

  python3 tools/post-bottom.py        全記事（tools/prev-links.py がいつも最後に呼ぶ）

1. 題の上の札を、その記事の本当の秒数にする（前は全部「⚡ 15 SEC」と決め打ちだった）。
   秒数は tools/check.py と同じ数え方（本文の語数 ÷ 1分180語）。右上の「○ words · ○ sec」と同じ数字になる
2. いちばん下（次の記事・前の記事のあと）に「← 一覧に戻る」ボタンを置く。
   前は、下まで読んでも「次」「前」しかなくて、一覧に戻るには上まで戻る必要があった。
   押すと、トップの一覧の、さっき見ていたところに戻る（トップが場所を覚えている）

何度走らせても同じ結果になる。ボタンの文字は「← Back to all works」で、40言語の訳がすでにある。
"""
import importlib.util
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
WORKS = ROOT / "works"

_spec = importlib.util.spec_from_file_location("chk", ROOT / "tools" / "check.py")
chk = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(chk)

START, END = "<!-- 📚 一覧に戻る（tools/post-bottom.py） -->", "<!-- /📚 -->"
BLOCK = (f"  {START}\n"
         '  <a class="to-list" href="../../index.html#posts">\n'
         '    <span class="to-list-ic" aria-hidden="true">📚</span>\n'
         '    <span class="to-list-t">← Back to all works</span>\n'
         f"  </a>\n  {END}\n")
CSS = """<style id="tolist-css">
  /* 📚 一覧に戻る（tools/post-bottom.py が入れる）。次・前の記事とは形を変えて、迷わないように */
  .to-list { display: flex; align-items: center; justify-content: center; gap: 10px; margin: 18px auto 0; min-height: 52px;
    width: fit-content; max-width: 100%; padding: 13px 26px; border-radius: 999px; text-decoration: none;
    color: #232c48; background: #fff; border: 2px solid rgba(35,44,72,.12); box-shadow: 0 8px 20px -10px rgba(35,44,72,.35);
    font-size: 15.5px; font-weight: 900; transition: transform .18s ease, box-shadow .18s ease; }
  .to-list:hover, .to-list:focus-visible { transform: translateY(-2px); box-shadow: 0 12px 24px -10px rgba(35,44,72,.45); }
  .to-list:focus-visible { outline: 3px solid #8b6de8; outline-offset: 3px; }
  .to-list-ic { font-size: 20px; line-height: 1; }
  html[data-theme="dark"] .to-list { background: #22242f; color: #f4f0fa; border-color: rgba(255,255,255,.16); }
  @media (prefers-reduced-motion: reduce) { .to-list { transition: none; } }
</style>
"""
BLOCK_RE = re.compile(r"\n?[ \t]*" + re.escape(START) + r".*?" + re.escape(END) + r"\n?", re.S)
CSS_RE = re.compile(r'<style id="tolist-css">.*?</style>\n?', re.S)
LABEL_RE = re.compile(r'(<div class="label">(?:\s*<span class="topic">.*?</span>)?\s*)[⚡⏱][^<]*(</div>)', re.S)
PREV_END = "<!-- /⏮ -->"


def seconds(doc: str) -> int:
    return max(1, round(len(chk.body_words(doc)) / (chk.WPM / 60)))


def fix(doc: str) -> str:
    sec = seconds(doc)
    doc = LABEL_RE.sub(lambda m: f"{m.group(1)}⚡ {sec} SEC{m.group(2)}", doc, count=1)

    doc = CSS_RE.sub("", BLOCK_RE.sub("\n", doc))
    k = doc.find(PREV_END)
    if k >= 0:
        at = doc.find("\n", k) + 1
    else:
        m = re.search(r'<a class="next"[^>]*>.*?</a>\n?', doc, re.S)
        at = m.end() if m else doc.rindex("</main>")
    doc = doc[:at] + BLOCK + doc[at:]
    return doc.replace("</head>", CSS + "</head>", 1)


def main():
    changed = 0
    posts = [d for d in sorted(WORKS.iterdir()) if (d / "index.html").exists()]
    for d in posts:
        p = d / "index.html"
        doc = p.read_text(encoding="utf-8")
        new = fix(doc)
        if new != doc:
            p.write_text(new, encoding="utf-8")
            changed += 1
    print(f"📚 秒数の札と「一覧に戻る」：{len(posts)}本を確認、{changed}本を書き換え")


if __name__ == "__main__":
    main()
