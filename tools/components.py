#!/usr/bin/env python3
"""
🧩 記事に「地図・動画・スライド」の部品を足す

  python3 tools/components.py           全記事に部品を入れる
  python3 tools/components.py <slug>    1本だけ

記事のCSSはHTMLの中に直接書いてある（外部CSSを持たない方針）ので、
新しい部品を足すときは全記事の <style> に同じものを入れて回る必要がある。
それを手でやると必ずズレるので、この道具が入れて回る。

⚠️ すでに入っている記事は飛ばす。二重に入らない。
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MARK = "/* ⬇️ tools/components.py */"
# ◀ ▶ のボタンだけ後から足したので、別の目印にしてある（2026-09-11）
ARROW_MARK = "/* ⬇️ tools/components.py : slides-arrow */"

CSS = MARK + """
  /* 🗺 地図 — 上空からその場所の雰囲気がわかるようにする */
  .map-card, .video-card { margin: 18px 0 0; overflow: hidden;
       border: 7px solid rgba(255,255,255,.8); border-radius: 30px;
       box-shadow: var(--shadow); background: #dde7ea; }
  .map-card iframe { display: block; width: 100%;
       height: clamp(220px, 45vw, 330px); border: 0; }
  .video-card { background: #000; }
  .video-card .ratio { position: relative; width: 100%; padding-top: 56.25%; }
  .video-card iframe { position: absolute; inset: 0; width: 100%; height: 100%; border: 0; }
  .map-card figcaption, .video-card figcaption {
       display: flex; align-items: center; gap: 8px; flex-wrap: wrap;
       padding: 11px 16px 13px; background: #fff; color: var(--muted);
       font-size: 12.5px; font-family: "Trebuchet MS", sans-serif; }
  .map-card figcaption a, .video-card figcaption a {
       color: var(--accent, #2f8fbf); font-weight: 700; text-decoration: none; }
  .map-card figcaption a:hover, .video-card figcaption a:hover { text-decoration: underline; }

  /* 🎞 スライド — 写真を全部縦に流さず、横にスワイプして見る */
  .slides { margin: 18px 0 0; }
  .slides-track { display: flex; gap: 12px; overflow-x: auto; padding: 4px 2px 12px;
       scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch;
       scrollbar-width: none; }
  .slides-track::-webkit-scrollbar { display: none; }
  .slides-track figure { flex: 0 0 86%; margin: 0; scroll-snap-align: center;
       overflow: hidden; background: #fff; border: 6px solid rgba(255,255,255,.85);
       border-radius: 24px; box-shadow: var(--shadow); }
  .slides-track img { display: block; width: 100%; height: clamp(200px, 52vw, 280px);
       object-fit: cover; }
  .slides-track figcaption { padding: 9px 14px 11px; color: var(--muted);
       font-size: 12px; font-family: "Trebuchet MS", sans-serif; }
  .slides-dots { display: flex; justify-content: center; align-items: center; gap: 7px; }
  /* 記事ごとに明るい配色と暗い配色があるので、色を決め打ちしない。
     currentColor（その記事の文字色）を薄めて使えば、どちらでも必ず見える */
  .slides-dots i { width: 7px; height: 7px; border-radius: 50%;
       background: currentColor; opacity: .28;
       transition: transform .3s ease, opacity .3s ease; }
  .slides-dots i.on { opacity: 1; transform: scale(1.55); }
  .slides-hint { margin-top: 9px; text-align: center; color: var(--muted);
       font-size: 11.5px; letter-spacing: .1em; font-family: "Trebuchet MS", sans-serif; }
"""

# スライドの丸ぽち。IntersectionObserver だけで書く（外部ライブラリを足さない約束）
JS = """
  /* 🎞 スライド：いま何枚目を見ているかを丸で出す */
  document.querySelectorAll('.slides').forEach(function (box) {
    var track = box.querySelector('.slides-track');
    var dots  = box.querySelector('.slides-dots');
    if (!track || !dots) return;
    var figs = Array.prototype.slice.call(track.children);
    figs.forEach(function () { dots.appendChild(document.createElement('i')); });
    var marks = Array.prototype.slice.call(dots.children);
    if (marks[0]) marks[0].className = 'on';
    if (!('IntersectionObserver' in window)) return;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var i = figs.indexOf(e.target);
        marks.forEach(function (m, j) { m.className = (i === j) ? 'on' : ''; });
      });
    }, { root: track, threshold: 0.6 });
    figs.forEach(function (f) { io.observe(f); });
  });
"""


ARROW_CSS = ARROW_MARK + """
  /* ◀ ▶ スライドのボタン（2026-09-11 に本人が要望）
     「写真をスライドさせるのはマウスだと難しいから、
      右とか左にクリックでスライドさせられる機能もつけて」
     ボタンのHTMLは書かない。下のJSがスライドを見つけて自分で足す */
  .slides { position: relative; }
  .slides-arrow {
    position: absolute; top: calc(50% - 34px); transform: translateY(-50%);
    display: grid; place-items: center; width: 46px; height: 46px; padding: 0;
    border: 0; border-radius: 50%; cursor: pointer;
    background: rgba(255,255,255,.94); color: #4a3350;
    font-size: 26px; line-height: 1; font-family: inherit;
    box-shadow: 0 6px 18px rgba(0,0,0,.22);
    transition: transform .16s ease, opacity .16s ease;
  }
  .slides-arrow:hover  { transform: translateY(-50%) scale(1.08); }
  .slides-arrow:disabled { opacity: .28; cursor: default; }
  .slides-prev { left: 6px; }
  .slides-next { right: 6px; }
  @media (max-width: 600px) {
    .slides-arrow { width: 40px; height: 40px; font-size: 23px; }
  }
"""

ARROW_JS = """
  /* ◀ ▶ スライドに、クリックで動かせるボタンを足す（2026-09-11） */
  document.querySelectorAll('.slides').forEach(function (box) {
    var track = box.querySelector('.slides-track');
    if (!track || box.querySelector('.slides-arrow')) return;
    if (track.children.length < 2) return;

    function step() {
      var first = track.children[0];
      return first ? first.getBoundingClientRect().width + 12 : track.clientWidth;
    }
    var made = [];
    [['prev', '\\u2039', 'Previous photo'], ['next', '\\u203a', 'Next photo']]
      .forEach(function (spec) {
        var b = document.createElement('button');
        b.type = 'button';
        b.className = 'slides-arrow slides-' + spec[0];
        b.textContent = spec[1];
        b.setAttribute('aria-label', spec[2]);
        b.addEventListener('click', function () {
          track.scrollBy({ left: spec[0] === 'prev' ? -step() : step(), behavior: 'smooth' });
        });
        box.appendChild(b);
        made.push(b);
      });

    /* 端まで来たボタンは薄くして押せなくする */
    function sync() {
      var max = track.scrollWidth - track.clientWidth - 2;
      made[0].disabled = track.scrollLeft <= 2;
      made[1].disabled = track.scrollLeft >= max;
    }
    track.addEventListener('scroll', sync);
    window.addEventListener('resize', sync);
    sync();
  });
"""


def inject_arrows(path: pathlib.Path) -> str:
    """スライドのある記事に ◀ ▶ のボタンを足す。"""
    doc = path.read_text(encoding="utf-8")
    # ⚠️ 上の CSS の中にも "slides-track" という文字は出てくるので、
    #    **本文に実際のスライドがあるか**で判定する。ここを間違えると全記事に入る
    if '<div class="slides-track">' not in doc:
        return ""                      # スライドが無い記事は何もしない
    if ARROW_MARK in doc:
        return "◀▶ すでに入っています"
    doc = doc.replace("</style>", ARROW_CSS + "\n</style>", 1)
    tail = doc.rfind("</script>")
    doc = doc[:tail] + ARROW_JS + doc[tail:]
    doc = doc.replace("SWIPE FOR MORE →", "◀ ▶ OR SWIPE")
    path.write_text(doc, encoding="utf-8")
    return "✅ ◀▶ ボタンを入れました"


def inject(path: pathlib.Path) -> str:
    doc = path.read_text(encoding="utf-8")
    if MARK in doc:
        return "すでに入っています"

    if "</style>" not in doc:
        return "❌ <style> が見つかりません"
    doc = doc.replace("</style>", CSS + "\n</style>", 1)

    # JS は本文いちばん下の <script> の中に足す。無ければ作る
    tail = doc.rfind("</script>")
    if tail == -1:
        doc = doc.replace("</body>", "<script>\n" + JS + "</script>\n</body>", 1)
    else:
        doc = doc[:tail] + JS + doc[tail:]

    path.write_text(doc, encoding="utf-8")
    return "✅ 部品を入れました"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    base = ROOT / "works"
    slugs = args or sorted(p.name for p in base.iterdir() if p.is_dir())
    for slug in slugs:
        idx = base / slug / "index.html"
        if not idx.exists():
            print(f"  ❔ {slug}: index.html がありません")
            continue
        print(f"  {inject(idx)}  {slug}")
        arrows = inject_arrows(idx)
        if arrows:
            print(f"  {arrows}  {slug}")


if __name__ == "__main__":
    main()
