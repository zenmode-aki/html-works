from gen import build

d = dict(
    slug="three-books-one-answer", seq=516,
    title=("3 very different books all arrive at the same answer: independence",
           "ちがう3冊の本が、同じ答え「自立」にたどり着く"),
    label=("3 Books", "3冊の本"),
    h1_emoji="📚",
    alt="A chubby layered cut paper penguin sitting on top of a real stack of three hardcover books like a small mountain",
    section="幸せは「自立」から",
    message="『嫌われる勇気』『7つの習慣』『反応しない練習』は、出どころがちがうのに、行き着く先はどれも「自立」。",
    tone="素材の重さ：真面目（本の話）\n→ 見せ方：ポップに（青と山吹色。3本の山道が1つの頂上で出会う）",
    game_ja="⛰️ 3本の山道：3冊の本のボタンを押すと、その本の色のペンギンが自分の山道をてくてく登る。頂上に着くと、その本の考え方が一言で出る（相手がどう思うかは相手の課題／起きたことと反応のあいだで選べる／まず心に気づいて、すぐ反応しない）。3羽とも着くと、頂上の旗が「自分の足で立つ」に変わって、紙吹雪。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made as a layered cut paper diorama figure, "
            "sitting happily on top of a realistic stack of three closed hardcover books (blue, green and orange covers with blank spines), "
            "a tiny paper flag beside it. Bright simple sky-blue and warm yellow background with soft layered paper hills for depth. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × 切り絵のジオラマ × 3冊の本",
    mood=["lift", "learn"], tags=["psychology", "books", "mindset"],
    pal=dict(bg="#f3f8ff", muted="#5f7090", acc="#2470d8", acc2="#ffaa1f", shadow="rgba(40,90,170,.16)",
             r1="rgba(255,190,70,.30)", r2="rgba(36,112,216,.18)", r3="rgba(70,200,140,.16)",
             h1="#132c55", photo="#e2edff", big="#1f5fc0", bigdark="#9cc4ff",
             game="linear-gradient(170deg, #4aa3ff 0%, #6b7cff 50%, #ffb04a 100%)"),
    cards=[
        dict(emoji="📚", label=("3 Books", "3冊の本"),
             s=[("There are 3 books: \"The Courage to Be Disliked,\" \"The 7 Habits,\" and \"The Practice of Not Reacting.\"",
                 "『嫌われる勇気』『7つの習慣』『反応しない練習』という3冊の本があります。")]),
        dict(emoji="🧭", label=("Different Roots", "ちがう出どころ"),
             s=[("They come from different ideas: Adler's psychology, American life principles, and the Buddha's teachings.",
                 "もとになっている考え方は、アドラー心理学、アメリカの人生の原則、ブッダの教えと、ばらばらです。")]),
        dict(emoji="🚩", label=("Same Answer", "同じ答え"), big=True,
             s=[("But when you read them, all 3 reach the same place: \"independence,\" standing on your own feet.",
                 "でも読んでみると、3冊とも行き着く先は同じ「自立」、つまり自分の足で立つことです。")]),
        dict(emoji="⛰️", label=("One Mountain", "1つの山"),
             s=[("The roads are different, but it is like reaching the same mountain top.",
                 "道はちがっても、同じ山のてっぺんに着くみたいです。")]),
    ],
    game_after=2,
    game_note="3本の山道（3冊の本が1つの頂上で出会う）",
    game_html="""  <section class="game" data-a="0" data-b="0" data-c="0" data-end="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">3 roads, 1 mountain top</div>
    <div class="game-hint">Tap a book. Its penguin climbs its own road.</div>
    <div class="mt">
      <svg class="mt-svg" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">
        <polygon class="hill" points="0,100 50,8 100,100" />
        <polyline class="rd ra" points="10,92 22,64 36,38 47,14" />
        <polyline class="rd rb" points="50,94 62,68 42,42 50,12" />
        <polyline class="rd rc" points="90,92 78,62 64,36 53,14" />
      </svg>
      <div class="flag"><span class="fl-q">❓ Where do they go?</span><span class="fl-t">🚩 Standing on your own feet!</span></div>
      <div class="wk wa"><span class="wk-p">🐧</span><span class="wk-b">📘</span></div>
      <div class="wk wb"><span class="wk-p">🐧</span><span class="wk-b">📗</span></div>
      <div class="wk wc"><span class="wk-p">🐧</span><span class="wk-b">📙</span></div>
    </div>
    <div class="books">
      <button type="button" class="btn bk bk-a" data-k="a"><span class="bk-t">📘 The Courage to Be Disliked</span><span class="bk-l">Whether people like you is their task, not yours.</span></button>
      <button type="button" class="btn bk bk-b" data-k="b"><span class="bk-t">📗 The 7 Habits</span><span class="bk-l">Between what happens and how you react, you can choose.</span></button>
      <button type="button" class="btn bk bk-c" data-k="c"><span class="bk-t">📙 The Practice of Not Reacting</span><span class="bk-l">First, notice your mind. Do not react right away.</span></button>
    </div>
    <div class="end">🎉 3 different roads. 1 same answer.</div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Start over</button></div>
  </section>""",
    css="""
  /* ⛰️ 3本の山道 */
  .mt { position: relative; height: 270px; max-width: 420px; margin: 16px auto 0; border-radius: 24px; overflow: hidden;
    background: linear-gradient(#bfe2ff, #eef7ff 75%); }
  .mt-svg { position: absolute; inset: 0; width: 100%; height: 100%; }
  .hill { fill: #8fd88a; }
  .rd { fill: none; stroke-width: 6; stroke-linecap: round; stroke-linejoin: round; vector-effect: non-scaling-stroke; opacity: .9; }
  .ra { stroke: #2f7bff; } .rb { stroke: #23b26b; } .rc { stroke: #ff8a1f; }
  .flag { position: absolute; left: 50%; top: 6px; transform: translateX(-50%); width: max-content; max-width: 92%; padding: 5px 12px; border-radius: 999px;
    background: #fff; color: #23345a; font-size: 13.5px; font-weight: 900; line-height: 1.3; z-index: 2; }
  .fl-t { display: none; }
  .game[data-end="1"] .fl-q { display: none; }
  .game[data-end="1"] .fl-t { display: inline; }
  .game[data-end="1"] .flag { background: #ffe066; color: #4a3500; animation: boing .6s ease; }
  .wk { position: absolute; z-index: 1; display: flex; align-items: flex-end; transform: translate(-50%, -85%);
    transition: left .45s ease-in-out, top .45s ease-in-out; }
  .wk-p { font-size: 34px; line-height: 1; }
  .wk-b { font-size: 18px; line-height: 1; margin-left: -6px; }
  .wk.step .wk-p { animation: hopw .45s ease; }
  @keyframes hopw { 50% { transform: translateY(-8px) rotate(-6deg); } }
  /* 歩く場所（%）：0=ふもと 1・2=とちゅう 3=頂上 */
  .game[data-a="0"] .wa { left: 10%; top: 92%; } .game[data-a="1"] .wa { left: 22%; top: 64%; } .game[data-a="2"] .wa { left: 36%; top: 38%; } .game[data-a="3"] .wa { left: 43%; top: 26%; }
  .game[data-b="0"] .wb { left: 50%; top: 94%; } .game[data-b="1"] .wb { left: 62%; top: 68%; } .game[data-b="2"] .wb { left: 42%; top: 42%; } .game[data-b="3"] .wb { left: 50%; top: 24%; }
  .game[data-c="0"] .wc { left: 90%; top: 92%; } .game[data-c="1"] .wc { left: 78%; top: 62%; } .game[data-c="2"] .wc { left: 64%; top: 36%; } .game[data-c="3"] .wc { left: 57%; top: 26%; }

  .books { display: grid; gap: 10px; max-width: 420px; margin: 14px auto 0; }
  .bk { display: grid; gap: 4px; justify-items: start; text-align: left; width: 100%; min-height: 60px; padding: 10px 16px; border-radius: 18px; }
  .bk-t { font-size: 16px; }
  .bk-l { display: none; font-size: 14.5px; font-weight: 800; color: #3d4766; line-height: 1.4; }
  .bk-a { border-left: 8px solid #2f7bff; } .bk-b { border-left: 8px solid #23b26b; } .bk-c { border-left: 8px solid #ff8a1f; }
  .game[data-a="3"] .bk-a .bk-l, .game[data-b="3"] .bk-b .bk-l, .game[data-c="3"] .bk-c .bk-l { display: block; animation: boing .45s ease; }
  .end { display: none; margin: 14px auto 0; max-width: 420px; padding: 12px 14px; border-radius: 18px; background: #fff; color: #1f3f7a; font-size: 17px; font-weight: 900; line-height: 1.45; }
  .game[data-end="1"] .end { display: block; animation: boing .5s ease; }
  .ctrl { margin-top: 12px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
""",
    dark="""  html[data-theme="dark"] .mt { background: linear-gradient(#1c2f4a, #2a3d58 75%); }
  html[data-theme="dark"] .hill { fill: #3c6b3a; }
  html[data-theme="dark"] .flag { background: #2b2d3a; color: #e4ecff; }
  html[data-theme="dark"] .game[data-end="1"] .flag { background: #4a3c12; color: #ffe39a; }
  html[data-theme="dark"] .bk-l { color: #c9d3ee; }
  html[data-theme="dark"] .end { background: #2b2d3a; color: #cfe0ff; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var walking = {}, timers = [];
  function pos(k) { return parseInt(g.getAttribute('data-' + k), 10) || 0; }
  function checkEnd() {
    if (pos('a') === 3 && pos('b') === 3 && pos('c') === 3 && g.getAttribute('data-end') !== '1') {
      g.setAttribute('data-end', '1');
      if (window.pengessoPop) { var r = g.querySelector('.flag').getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height, ['🚩', '🐧', '📘', '📗', '📙', '✨'], 22); }
    }
  }
  [].forEach.call(g.querySelectorAll('.bk'), function (b) {
    b.addEventListener('click', function () {
      var k = b.getAttribute('data-k'), w = g.querySelector('.w' + k);
      if (walking[k] || pos(k) === 3) return;
      walking[k] = true;
      (function step() {
        var p = pos(k) + 1;
        g.setAttribute('data-' + k, String(p));
        w.classList.remove('step'); void w.offsetWidth; w.classList.add('step');
        if (p < 3) timers.push(setTimeout(step, 480));
        else {
          walking[k] = false;
          if (window.pengessoPop) { var r = w.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top, ['✨', w.querySelector('.wk-b').textContent], 8); }
          timers.push(setTimeout(checkEnd, 300));
        }
      })();
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    timers.forEach(clearTimeout); timers = []; walking = {};
    ['a', 'b', 'c'].forEach(function (k) { g.setAttribute('data-' + k, '0'); });
    g.setAttribute('data-end', '0');
  });
})();
""",
    ja={
        "3 roads, 1 mountain top": "3本の道、1つの頂上",
        "Tap a book. Its penguin climbs its own road.": "本を押してね。その本のペンギンが、自分の道を登ります。",
        "❓ Where do they go?": "❓ どこに着くかな？",
        "🚩 Standing on your own feet!": "🚩 自分の足で立つ！",
        "📘 The Courage to Be Disliked": "📘 嫌われる勇気",
        "📗 The 7 Habits": "📗 7つの習慣",
        "📙 The Practice of Not Reacting": "📙 反応しない練習",
        "Whether people like you is their task, not yours.": "人があなたを好きかどうかは、相手の課題。あなたの課題ではありません。",
        "Between what happens and how you react, you can choose.": "起きたことと、どう反応するかのあいだで、自分で選べます。",
        "First, notice your mind. Do not react right away.": "まず自分の心に気づく。すぐに反応しない。",
        "🎉 3 different roads. 1 same answer.": "🎉 ちがう3本の道。答えは1つ。",
        "↺ Start over": "↺ 最初から",
    },
)
build(d)
