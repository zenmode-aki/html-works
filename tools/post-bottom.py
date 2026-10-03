#!/usr/bin/env python3
"""
📚 記事の「読むのにかかる秒数」と、いちばん下の「一覧に戻る」ボタン（2026-09-26 本人の要望）

  python3 tools/post-bottom.py        全記事（tools/prev-links.py がいつも最後に呼ぶ）

1. 題の上の札を、その記事の本当の秒数にする（前は全部「⚡ 15 SEC」と決め打ちだった）。
   秒数は tools/check.py と同じ数え方（本文の語数 ÷ 1分180語）。右上の「○ words · ○ sec」と同じ数字になる
2. いちばん下（次の記事・前の記事のあと）に「← 一覧に戻る」ボタンを置く。
   前は、下まで読んでも「次」「前」しかなくて、一覧に戻るには上まで戻る必要があった。
   押すと、トップの一覧の、さっき見ていたところに戻る（トップが場所を覚えている）

3. 「一覧に戻る」の上に「✨ こちらもどうぞ」を5本出す（2026-09-26 本人の要望）。
   下まで読んだ人が、次に読むものを選べるように。選び方（毎回同じ結果になる）：
     ・同じシリーズ（knowledge-metabo-1/2/3 など）＞ 同じ話題 ＞ 同じ場所（名古屋は弱め）・同じ章 ＞ 同じ部屋 で点数をつけて上位4本
     ・5本目は「🎲 ちょっと違う話」。話題も場所もちがう記事から1本（slug から決まるので毎回同じ）
     ・自分・次の記事・前の記事・日本語だけの記事（meta.json の "only"）は出さない
   サムネはトップと同じ assets/thumbs/<slug>.jpg を CSS の背景で出す（飾りなので、無くても文字は読める）
4. ~~画面のいちばん上の、読んだところまでの線（CSS 版）~~ → 2026-10-03 やめた。i18n_runtime.js の虹色の線（JS 版）と
   2本重なっていた（Chrome では紫だけ、Safari では虹色）。虹色の1本だけにした
5. 全記事に効く小さな見た目の直し（<style id="shared-fix-css">。2026-10-03 の UI 見直し）
   ・PC では表紙（h1 のすぐ下の写真）を切らずに少し小さく → 本文が最初の画面に近づく
   ・「次の記事」ボタンの左側を少し暗くして、白い字を読みやすく（金色・黄色の記事で薄かった）
   ・日本語のときだけ、11px 前後の小さい札を 12.5px に（太い丸ゴシックだとつぶれた）
   ・読み込み中だけ見えていた「PUBLIC」の札を、最初から隠す

何度走らせても同じ結果になる。ボタンの文字は「← Back to all works」で、40言語の訳がすでにある。
"""
import html
import importlib.util
import json
import zlib
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
REL_START, REL_END = "<!-- ✨ こちらもどうぞ（tools/post-bottom.py） -->", "<!-- /✨ -->"
REL_RE = re.compile(r"\n?[ \t]*" + re.escape(REL_START) + r".*?" + re.escape(REL_END) + r"\n?", re.S)
REL_CSS = """<style id="related-css">
  /* ✨ こちらもどうぞ（tools/post-bottom.py が入れる）。色は記事ごとの --purple / --text に合わせる */
  .related { margin: 34px 0 0; }
  .related-h { margin: 0 0 12px; font-size: 18px; font-weight: 900; letter-spacing: .02em; color: var(--text, #232c48); }
  .related-list { list-style: none; margin: 0; padding: 0; display: grid; gap: 10px; }
  .rel-card { display: flex; align-items: center; gap: 14px; padding: 10px 14px 10px 10px; border-radius: 20px;
    text-decoration: none; color: var(--text, #232c48); background: rgba(255,255,255,.92);
    border: 2px solid var(--line, rgba(35,44,72,.1)); box-shadow: 0 8px 22px -14px rgba(35,44,72,.45);
    transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease; }
  .rel-card:hover, .rel-card:focus-visible { transform: translateY(-2px); border-color: var(--purple, #8b6de8);
    box-shadow: 0 14px 26px -14px rgba(35,44,72,.5); }
  .rel-card:focus-visible { outline: 3px solid var(--purple, #8b6de8); outline-offset: 3px; }
  .rel-thumb { flex: 0 0 auto; width: 68px; height: 68px; border-radius: 16px; background-color: #f1ecf8;
    background-size: cover; background-position: center; box-shadow: inset 0 0 0 1px rgba(0,0,0,.06); }
  .rel-body { min-width: 0; display: flex; flex-direction: column; gap: 4px; }
  .rel-kicker { display: flex; flex-wrap: wrap; align-items: center; gap: 6px; font-size: 11.5px; font-weight: 900;
    letter-spacing: .08em; color: var(--purple, #6b4fd0); }
  .rel-chip { padding: 2px 8px; border-radius: 999px; background: var(--purple, #6b4fd0); color: #fff; letter-spacing: .02em; }
  .rel-title { font-size: 15.5px; font-weight: 800; line-height: 1.38; overflow-wrap: anywhere; }
  .rel-go { margin-left: auto; flex: 0 0 auto; font-size: 18px; opacity: .55; }
  html[data-theme="dark"] .related-h { color: #f4f0fa; }
  html[data-theme="dark"] .rel-card { background: #22242f; color: #f4f0fa; border-color: rgba(255,255,255,.14); }
  html[data-theme="dark"] .rel-thumb { background-color: #2e3140; }
  html[dir="rtl"] .rel-go { transform: scaleX(-1); }
  @media (prefers-reduced-motion: reduce) { .rel-card { transition: none; } .rel-card:hover { transform: none; } }
</style>
"""


def _series(slug):
    return re.sub(r"-\d+$", "", slug)


def load_all():
    """全記事の meta と秒数（こちらもどうぞ用）"""
    out = {}
    for d in sorted(WORKS.iterdir()):
        p = d / "index.html"
        if not p.exists() or not (d / "meta.json").exists():
            continue
        meta = json.loads((d / "meta.json").read_text(encoding="utf-8"))
        out[d.name] = {"meta": meta, "sec": seconds(p.read_text(encoding="utf-8"))}
    return out


def pick_related(slug, doc, info):
    me = info[slug]["meta"]
    skip = {slug} | set(re.findall(r'<a class="(?:next|prev)"[^>]*href="\.\./([^/]+)/index\.html"', doc))
    pool = [s for s, v in info.items() if s not in skip and not v["meta"].get("only")]

    def score(s):
        m = info[s]["meta"]
        pts = 0
        if _series(s) == _series(slug) and _series(s) != s:
            pts += 20                                   # 同じシリーズ（Part 1/2/3）
        if m.get("series") and m.get("series") == me.get("series"):
            pts += 20                                   # meta.json の "series" が同じ（名古屋ドームの4本など）
        pts += 6 * len(set(m.get("tags", [])) & set(me.get("tags", [])))   # 同じタグ（"baseball" など）
        if m.get("topic") and m.get("topic") == me.get("topic"):
            pts += 5                                    # 同じ話題（仕事・旅・暮らし…）
        if m.get("place") and m.get("place") == me.get("place"):
            pts += 1 if m.get("place") == "nagoya" else 3   # 名古屋は記事の半分なので弱め
        if m.get("chapter") and m.get("chapter") == me.get("chapter"):
            pts += 3
        if m.get("room") and m.get("room") == me.get("room"):
            pts += 2                                    # トップの同じ部屋（好き・考えごと…）
        return pts

    seq = lambda s: info[s]["meta"].get("seq") or 0
    ranked = sorted(pool, key=lambda s: (-score(s), abs(seq(s) - seq(slug)), s))
    top = ranked[:4]
    other = [s for s in pool if s not in top
             and info[s]["meta"].get("topic") != me.get("topic")
             and info[s]["meta"].get("place") != me.get("place")]
    if not other:
        other = [s for s in ranked[4:]]
    surprise = sorted(other)[zlib.crc32(slug.encode()) % len(other)] if other else None
    return top, surprise


def related_block(slug, doc, info):
    top, surprise = pick_related(slug, doc, info)
    items = [(s, False) for s in top] + ([(surprise, True)] if surprise else [])
    lis = []
    for s, odd in items:
        t = html.escape(info[s]["meta"]["title"], quote=False)
        chip = '\n            <span class="rel-chip">🎲 Something different</span>' if odd else ""
        lis.append(
            '      <li>\n'
            f'        <a class="rel-card" href="../{s}/index.html">\n'
            f'          <span class="rel-thumb" aria-hidden="true" style="background-image:url(\'../../assets/thumbs/{s}.jpg\')"></span>\n'
            '          <div class="rel-body">\n'
            f'            <div class="rel-kicker"><span class="rel-sec">⚡ {info[s]["sec"]} SEC</span>{chip}</div>\n'
            f'            <div class="rel-title">{t}</div>\n'
            '          </div>\n'
            '          <span class="rel-go" aria-hidden="true">→</span>\n'
            '        </a>\n'
            '      </li>\n')
    return (f"  {REL_START}\n"
            '  <section class="related" aria-labelledby="related-h">\n'
            '    <h2 class="related-h" id="related-h">✨ You might also like</h2>\n'
            '    <ul class="related-list">\n' + "".join(lis) +
            "    </ul>\n  </section>\n"
            f"  {REL_END}\n")


FIX_CSS = """<style id="shared-fix-css">
  /* 🧰 全記事に効く小さな直し（tools/post-bottom.py が入れる。2026-10-03 の UI 見直し） */
  /* 🖥 PC では表紙を切らずに少し小さく。1280×800 で、本文が2画面目からだった */
  @media (min-width: 700px) {
    h1 + figure.photo { width: min(100%, calc(44vh * 4 / 3 + 14px)); margin-left: auto; margin-right: auto; }
  }
  /* ➡️「次の記事」：左側（文字のあるところ）を少し暗くして、白い字を読みやすく */
  .next { position: relative; isolation: isolate; }
  .next::before { content: ""; position: absolute; inset: 0; z-index: -1; border-radius: inherit; pointer-events: none;
    background: linear-gradient(90deg, rgba(28,14,48,.36), rgba(28,14,48,.16) 62%, rgba(28,14,48,0)); }
  html[dir="rtl"] .next::before { background: linear-gradient(270deg, rgba(28,14,48,.36), rgba(28,14,48,.16) 62%, rgba(28,14,48,0)); }
  .next .next-kicker { opacity: 1; }
  /* 🇯🇵 日本語の太い丸ゴシックは 11px だとつぶれる */
  html:lang(ja) .topic, html:lang(ja) .next-kicker, html:lang(ja) .prev-kicker, html:lang(ja) .rel-kicker { font-size: 12.5px; }
  /* 読む人には関係ない「PUBLIC」の札は、読み込み中も見せない（HTML には残す。check.py が確かめるため） */
  .stage-public { display: none !important; }
</style>
"""


BLOCK_RE = re.compile(r"\n?[ \t]*" + re.escape(START) + r".*?" + re.escape(END) + r"\n?", re.S)
CSS_RE = re.compile(r'<style id="tolist-css">.*?</style>\n?', re.S)
REL_CSS_RE = re.compile(r'<style id="related-css">.*?</style>\n?', re.S)
FIX_CSS_RE = re.compile(r'<style id="shared-fix-css">.*?</style>\n?', re.S)
LABEL_RE = re.compile(r'(<div class="label">(?:\s*<span class="topic">.*?</span>)?\s*)[⚡⏱][^<]*(</div>)', re.S)
PREV_END = "<!-- /⏮ -->"


def seconds(doc: str) -> int:
    return max(1, round(len(chk.body_words(doc)) / (chk.WPM / 60)))


def fix(doc: str, slug: str = None, info: dict = None) -> str:
    sec = seconds(doc)
    doc = LABEL_RE.sub(lambda m: f"{m.group(1)}⚡ {sec} SEC{m.group(2)}", doc, count=1)

    doc = CSS_RE.sub("", BLOCK_RE.sub("\n", doc))
    doc = REL_CSS_RE.sub("", REL_RE.sub("\n", doc))
    doc = FIX_CSS_RE.sub("", doc)
    k = doc.find(PREV_END)
    if k >= 0:
        at = doc.find("\n", k) + 1
    else:
        m = re.search(r'<a class="next"[^>]*>.*?</a>\n?', doc, re.S)
        at = m.end() if m else doc.rindex("</main>")
    rel = related_block(slug, doc, info) if slug and info and slug in info else ""
    doc = doc[:at] + rel + BLOCK + doc[at:]
    css = (REL_CSS if rel else "") + CSS + FIX_CSS
    # 🌐 i18n.py は自分の埋め込みを </head> の直前に置く。こちらはその前に置いて、
    #    2つの道具がお互いの順番を入れ替え合わないようにする（何度走らせても同じ結果）
    i18n_at = doc.find("<!-- 🌐 i18n:start")
    if 0 <= i18n_at < doc.find("</head>"):
        return doc[:i18n_at] + css + doc[i18n_at:]
    return doc.replace("</head>", css + "</head>", 1)


def main():
    changed = 0
    posts = [d for d in sorted(WORKS.iterdir()) if (d / "index.html").exists()]
    info = load_all()
    for d in posts:
        p = d / "index.html"
        doc = p.read_text(encoding="utf-8")
        new = fix(doc, d.name, info)
        if new != doc:
            p.write_text(new, encoding="utf-8")
            changed += 1
    print(f"📚 秒数の札・こちらもどうぞ・「一覧に戻る」：{len(posts)}本を確認、{changed}本を書き換え")


if __name__ == "__main__":
    main()
