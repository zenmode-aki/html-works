from gen import build

SQ = """url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='44' height='16'%3E%3Cpath d='M0 9 Q5 1 11 8 T22 8 Q27 14 33 6 T44 9' fill='none' stroke='%235a63d8' stroke-width='2.6' stroke-linecap='round'/%3E%3C/svg%3E")"""

d = dict(
    slug="three-morning-pages", seq=564, path="morningpages",
    title=("Write 3 pages every morning, and do not stop your pen",
           "毎朝3ページ。ペンを止めずに、頭の中を書き出す"),
    label=("Morning Pages", "モーニングページ"),
    h1_emoji="📓",
    alt="A chubby crocheted amigurumi penguin writing in a realistic open notebook with a pen in soft morning light",
    section="⑦「毎朝3ページ」",
    message="毎朝3ページ、ペンを止めずに書く。書くことがなければ「書くことがない」でいい。頭の中を外から見られる。",
    tone="素材の重さ：ふつう（習慣の紹介）\n→ 見せ方：ポップに（朝のオレンジと青。ノートを3ページ埋めて遊べる）",
    game_ja="📓 3ページ・チャレンジ：「✍️ ぐるぐる書く」か「😶 書くことがない」を押すたびに、ノートの行が1本ずつ埋まる（どちらでも1行進む。「書くことがない」の行には、その言葉が書かれる）。5行で1ページ、ページがめくれて、3ページ（15行）で完成。書くほど、上の「頭の中」のもやもや（メール・お金・洗濯・時計・ぐるぐる）が1つずつ消えて、最後は☀️。「頭が軽くなった。さあ、朝ごはん」。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of crocheted amigurumi yarn, "
            "sitting at a small table and happily writing in a realistic open paper notebook with a ballpoint pen, a cup of coffee beside it. "
            "Bright simple warm morning-orange and soft sky-blue background with depth, gentle sunrise light. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × かぎ針編みのあみぐるみ × 開いたノートとペン",
    mood=["lift"], tags=["books", "rest", "tips"],
    pal=dict(bg="#fffaf0", muted="#7d6a5a", acc="#d9661f", acc2="#5b6cff", shadow="rgba(140,90,40,.16)",
             r1="rgba(255,190,80,.34)", r2="rgba(91,108,255,.16)", r3="rgba(255,120,120,.14)",
             h1="#3d2410", photo="#ffeed6", big="#c4561a", bigdark="#ffc08f",
             game="linear-gradient(150deg, #f08a24 0%, #e8566b 52%, #5b6cff 100%)"),
    cards=[
        dict(emoji="📓", label=("Morning Pages", "モーニングページ"),
             s=[("Morning pages means this: every morning, you fill 3 notebook pages by hand.",
                 "「モーニングページ」とは、毎朝ノート3ページを手書きで埋めることです。")]),
        dict(emoji="🖊️", label=("One Rule", "ルールは1つ"),
             s=[("The only rule is: do not stop your pen.", "ルールは「ペンを止めない」ことだけです。"),
                ("If you have nothing, write \"I have nothing to write.\"", "書くことがなければ、「書くことがない」と書きます。")]),
        dict(emoji="🪞", label=("Outside View", "外から見る"), big=True,
             s=[("On paper, you can see your worries like someone else's worries.",
                 "紙に出すと、自分の悩みを、他人の悩みのように外から見られます。")]),
        dict(emoji="☕", label=("His Joke", "ノリツッコミ"),
             s=[("Oliver Burkeman jokes, \"I get up at 6 every morning… no, that is a lie.\"",
                 "オリバー・バークマンさんは、「毎朝6時に起きて…というのは嘘です」とノリツッコミしています。"),
                ("He writes about 4 days a week.", "実際は、週に4日くらいだそうです。")]),
    ],
    game_after=2,
    game_note="3ページ・チャレンジ（ペンを止めない）",
    game_html="""  <section class="game" data-s="idle" data-m="hint" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Fill 3 pages. Don't stop your pen!</div>
    <div class="brain">
      <span class="br-l">🧠 My head:</span>
      <span class="wzs" aria-hidden="true"><span class="wz">📧</span><span class="wz">💸</span><span class="wz">🧺</span><span class="wz">⏰</span><span class="wz">🌀</span><span class="wz">😟</span><span class="sun">☀️</span></span>
    </div>
    <div class="book">
      <div class="bk-h"><span class="pg-l">📓 Page</span> <span class="pgn">1</span> <span class="pg-of">/ 3</span></div>
      <div class="ln"><span class="sq"></span><span class="nw">I have nothing to write.</span></div>
      <div class="ln"><span class="sq"></span><span class="nw">I have nothing to write.</span></div>
      <div class="ln"><span class="sq"></span><span class="nw">I have nothing to write.</span></div>
      <div class="ln"><span class="sq"></span><span class="nw">I have nothing to write.</span></div>
      <div class="ln"><span class="sq"></span><span class="nw">I have nothing to write.</span></div>
      <div class="bar" aria-hidden="true"><i></i></div>
    </div>
    <div class="msgs">
      <div class="m-hint">Tap either button. Any words are OK.</div>
      <div class="m-go">Keep going! Don't stop your pen. ✍️</div>
      <div class="m-done">3 pages! Your head feels light. ☀️ Now, breakfast.</div>
    </div>
    <div class="ctrl">
      <button type="button" class="btn b-s">✍️ Scribble</button>
      <button type="button" class="btn b-n">😶 Nothing to write</button>
    </div>
    <div class="ctrl2"><button type="button" class="btn ghost b-reset">↺ Tomorrow morning</button></div>
  </section>""",
    css="""
  /* 📓 3ページ・チャレンジ */
  .brain { display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 8px; max-width: 420px; margin: 14px auto 0;
    padding: 10px 12px; border-radius: 20px; background: rgba(255,255,255,.2); font-size: 15px; font-weight: 900; }
  .wzs { position: relative; display: inline-flex; gap: 4px; min-height: 34px; align-items: center; }
  .wz { display: inline-block; font-size: 24px; line-height: 1; transition: opacity .45s ease, transform .45s ease; }
  .wz.gone { opacity: 0; transform: translateY(26px) scale(.4); }
  .sun { position: absolute; left: 50%; top: 50%; font-size: 34px; line-height: 1; opacity: 0; transform: translate(-50%, -50%) scale(.3); transition: opacity .5s ease, transform .6s cubic-bezier(.3,1.6,.5,1); }
  .game[data-s="done"] .sun { opacity: 1; transform: translate(-50%, -50%) scale(1); }
  .book { position: relative; max-width: 400px; margin: 14px auto 0; padding: 12px 16px 14px 30px; border-radius: 10px 18px 18px 10px; text-align: left;
    background: #fffdf6; color: #3a3550; box-shadow: 0 8px 0 rgba(0,0,0,.16), inset 6px 0 0 #ffb3a7; transform-origin: 0 50%; }
  .book.turn { animation: turn .5s ease; }
  @keyframes turn { 0% { transform: none; } 45% { transform: perspective(700px) rotateY(-60deg); opacity: .4; } 100% { transform: none; } }
  .bk-h { font-size: 13.5px; font-weight: 900; color: #8a6d4a; margin-bottom: 4px; }
  .ln { position: relative; height: 34px; border-bottom: 2px solid #c9d6f2; overflow: hidden; }
  .sq { position: absolute; left: 0; bottom: 5px; height: 16px; width: 0; background: """ + SQ + """ repeat-x left center; }
  .ln.f-s .sq { width: 100%; transition: width .35s ease-out; }
  .nw { position: absolute; left: 0; bottom: 4px; right: 0; font-size: 15px; font-weight: 800; color: #5a63d8; font-style: italic; line-height: 1.2;
    opacity: 0; clip-path: inset(0 100% 0 0); }
  .ln.f-n .nw { opacity: 1; clip-path: inset(0 0 0 0); transition: clip-path .4s ease-out; }
  .bar { height: 8px; margin-top: 10px; border-radius: 999px; background: #efe6d4; overflow: hidden; }
  .bar i { display: block; height: 100%; width: 0; border-radius: 999px; background: linear-gradient(90deg, #ffb627, #e8566b); transition: width .3s ease; }
  .msgs { min-height: 54px; margin-top: 10px; }
  .msgs > div { display: none; font-size: 16px; font-weight: 900; line-height: 1.45; padding: 6px 4px; }
  .game[data-m="hint"] .m-hint, .game[data-m="go"] .m-go, .game[data-m="done"] .m-done { display: block; animation: boing .45s ease; }
  .ctrl { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; }
  .ctrl .btn { flex: 1 1 150px; max-width: 220px; min-height: 60px; }
  .b-s { background: #fff; color: #3a3550; }
  .b-n { background: #ffe9a8; color: #5a3d00; }
  .game[data-s="done"] .ctrl { display: none; }
  .ctrl2 { margin-top: 10px; min-height: 48px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
  .game[data-s="idle"] .b-reset { visibility: hidden; }
""",
    dark="""  html[data-theme="dark"] .book { background: #262838; color: #ece8ff; box-shadow: 0 8px 0 rgba(0,0,0,.3), inset 6px 0 0 #7a4a44; }
  html[data-theme="dark"] .ln { border-bottom-color: #3d4466; }
  html[data-theme="dark"] .nw { color: #aab2ff; }
  html[data-theme="dark"] .bk-h { color: #e0c39c; }
  html[data-theme="dark"] .bar { background: #3a3c4e; }
  html[data-theme="dark"] .game .b-n { background: #5a4a17; color: #ffe39a; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var lines = [].slice.call(g.querySelectorAll('.ln')), wz = [].slice.call(g.querySelectorAll('.wz'));
  var book = g.querySelector('.book'), pgn = g.querySelector('.pgn'), bar = g.querySelector('.bar i');
  var PER = lines.length, TOTAL = PER * 3, n = 0, busy = false, turnT = 0;
  function clearLines() { lines.forEach(function (l) { l.classList.remove('f-s', 'f-n'); }); }
  function reset() {
    clearTimeout(turnT); busy = false; n = 0; clearLines(); pgn.textContent = '1'; bar.style.width = '0';
    wz.forEach(function (w) { w.classList.remove('gone'); });
    g.setAttribute('data-s', 'idle'); g.setAttribute('data-m', 'hint');
  }
  function write(kind) {
    if (busy || n >= TOTAL) return;
    var l = lines[n % PER]; l.classList.add(kind === 'n' ? 'f-n' : 'f-s');
    n++; bar.style.width = (n / TOTAL * 100) + '%';
    var gone = Math.floor(n * wz.length / TOTAL);
    wz.forEach(function (w, i) { w.classList.toggle('gone', i < gone); });
    g.setAttribute('data-s', 'writing'); g.setAttribute('data-m', 'go');
    if (navigator.vibrate) { try { navigator.vibrate(8); } catch (e) {} }
    if (n === TOTAL) {
      g.setAttribute('data-s', 'done'); g.setAttribute('data-m', 'done');
      if (window.pengessoPop) { var r = g.querySelector('.brain').getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['☀️', '📓', '🐧', '✨', '☕'], 18); }
    } else if (n % PER === 0) {
      busy = true;
      turnT = setTimeout(function () {
        book.classList.remove('turn'); void book.offsetWidth; book.classList.add('turn');
        setTimeout(function () { clearLines(); pgn.textContent = n / PER + 1; busy = false; }, 220);
      }, 300);
    }
  }
  g.querySelector('.b-s').addEventListener('click', function () { write('s'); });
  g.querySelector('.b-n').addEventListener('click', function () { write('n'); });
  g.querySelector('.b-reset').addEventListener('click', reset);
  reset();
})();
""",
    ja={
        "Fill 3 pages. Don't stop your pen!": "3ページ埋めよう。ペンを止めないで！",
        "🧠 My head:": "🧠 頭の中：",
        "📓 Page": "📓",
        "/ 3": "/ 3 ページ",
        "I have nothing to write.": "書くことがない。",
        "Tap either button. Any words are OK.": "どちらのボタンでもいいよ。どんな言葉でもOK。",
        "Keep going! Don't stop your pen. ✍️": "その調子！ペンを止めないで ✍️",
        "3 pages! Your head feels light. ☀️ Now, breakfast.": "3ページ書けた！頭が軽くなった ☀️ さあ、朝ごはん。",
        "✍️ Scribble": "✍️ ぐるぐる書く",
        "😶 Nothing to write": "😶 書くことがない",
        "↺ Tomorrow morning": "↺ また明日の朝",
    },
)

if __name__ == "__main__":
    build(d)
