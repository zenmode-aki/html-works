from gen import build

d = dict(
    slug="feelings-start-in-the-body", seq=532,
    title=("Before a feeling comes, your body reacts a little first",
           "感情の前に、体が少しだけ先に反応している"),
    label=("Body First", "体が先"),
    h1_emoji="💓",
    alt="A chubby felted wool penguin calmly resting one flipper on its chest beside a ceramic bowl of water with one soft ripple",
    section="「反応しない心」",
    message="感情の前に、体に小さな反応が出る。そこで観察すると、感情にならずに消えていく。",
    tone="素材の重さ：ふつう（心の仕組み）\n→ 見せ方：ポップに（ミントと紫。小さな波が「出来事 → 体 → 感情」と流れていくのを、体のところでつかまえる）",
    game_ja="💓 体でキャッチ：スタートを押すと出来事（列に割りこまれる／既読なのに返事がない／洗濯の日に雨）が出て、小さな波が「⚡出来事 → 💓体 → 🌋感情」と流れていく。波が💓体のところにいるあいだに「👀 見る」を押すと、波はふっと消えて🍃。遅いと🌋大きな感情に、早すぎると「まだ何も来ていない」。3回で、いくつキャッチできたか。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of soft felted wool, "
            "sitting calmly with its eyes half closed and one flipper resting on its chest, beside a realistic small handmade ceramic bowl of clear water with one soft ripple. "
            "Bright simple mint green and lavender background with soft depth and gentle morning light. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × フェルト羊毛 × 波紋の水の陶器のボウル",
    mood=["lift", "learn"], tags=["psychology", "feelings", "mindset"],
    pal=dict(bg="#f3fff9", muted="#5f7f74", acc="#1f9f80", acc2="#7a5cff", shadow="rgba(40,120,100,.16)",
             r1="rgba(47,211,167,.28)", r2="rgba(122,92,255,.16)", r3="rgba(255,111,145,.12)",
             h1="#123f35", photo="#ddf7ee", big="#16806a", bigdark="#8fe9cf",
             game="linear-gradient(155deg, #18a684 0%, #3f8fd8 50%, #7a5cff 100%)"),
    cards=[
        dict(emoji="⚡", label=("Usual Idea", "ふつうの考え"),
             s=[("Usually we think, \"Something happens, and then a feeling comes.\"",
                 "ふつうは「出来事があって、感情が動く」と思いますよね。")]),
        dict(emoji="💓", label=("Body Signal", "体のサイン"),
             s=[("But it is said there is a small reaction in the body between them.",
                 "でも本当は、そのあいだに体の小さな反応があるそうです。"),
                ("For example, your chest feels uneasy, or your stomach feels heavy.",
                 "たとえば、胸がざわっとする、おなかが重くなる、のような感じです。")],
             extra='<div class="flow" aria-hidden="true"><span class="fl f1">⚡</span><span class="fa">→</span><span class="fl f2">💓</span><span class="fa">→</span><span class="fl f3">🌋</span></div>'),
        dict(emoji="🍃", label=("Just Watch", "ただ見る"), big=True,
             s=[("If you watch it at that point, like \"Oh, I felt uneasy just now,\" it seems to fade before it becomes a feeling.",
                 "その段階で「あ、今ざわっとしたな」と見ていると、感情になる前に消えていくそうです。")]),
    ],
    game_after=2,
    game_note="体でキャッチ（波が体にいるうちに見ると、感情にならない）",
    game_html="""  <section class="game" data-s="idle" data-b="start" data-e="0" data-z="0" data-done="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Catch it in the body</div>
    <div class="game-hint">A small wave runs from the event to your feelings. Tap "Watch it" while it is in the body.</div>
    <div class="ev">
      <span class="ev0">Press start. Something will happen.</span>
      <span class="ev1">🛒 Someone cuts in line at the store.</span>
      <span class="ev2">📱 Your message was read, but there is no reply.</span>
      <span class="ev3">☔ It starts to rain on laundry day.</span>
    </div>
    <div class="lane">
      <div class="z z1"><span class="zi">⚡</span><span class="zl">Event</span></div>
      <div class="z z2"><span class="zi">💓</span><span class="zl">Body</span></div>
      <div class="z z3"><span class="zi">🌋</span><span class="zl">Feeling</span></div>
      <div class="wave" aria-hidden="true"><i></i></div>
    </div>
    <div class="sense">
      <span class="sn1">💓 My chest feels uneasy…</span>
      <span class="sn2">🪨 My stomach feels heavy…</span>
      <span class="sn3">🧱 My shoulders feel stiff…</span>
    </div>
    <button class="tap" type="button">
      <span class="t-start">▶ Start</span>
      <span class="t-run">👀 Watch it</span>
      <span class="t-next">▶ Next event</span>
      <span class="t-again">↺ Play again</span>
    </button>
    <div class="result">
      <div class="r-hint">Not too early, not too late. Just watch.</div>
      <div class="r-calm">🍃 You watched it. It faded before it became a feeling.</div>
      <div class="r-late">🌋 Too late! It became a big feeling.</div>
      <div class="r-early">🙈 Too early. Nothing has reached your body yet.</div>
    </div>
    <div class="score"><span class="sc-l">🍃 Caught in the body:</span> <span class="sc">0</span><span class="sc-of">/ 3</span></div>
    <div class="end">🐧 When you notice the body first, the wave stays small.</div>
  </section>""",
    css="""
  /* 小さな流れ図 */
  .flow { display: flex; align-items: center; justify-content: center; gap: 8px; margin-top: 14px; }
  .card .flow .fl { display: grid; text-align: center; line-height: 54px; place-items: center; width: 54px; height: 54px; border-radius: 18px; font-size: 28px; background: #eef9f5; }
  .card .flow .f2 { background: #fff0f4; box-shadow: 0 0 0 3px #ff8fab; }
  .flow .fa { font-size: 22px; font-weight: 900; color: #9ab8ae; }

  /* 💓 体でキャッチ */
  .ev { max-width: 440px; margin: 14px auto 0; min-height: 52px; padding: 12px 14px; border-radius: 18px; background: #fff; color: #23423a;
    font-size: 16.5px; font-weight: 900; line-height: 1.4; display: flex; align-items: center; justify-content: center; }
  .ev > span { display: none; }
  .game[data-e="0"] .ev0, .game[data-e="1"] .ev1, .game[data-e="2"] .ev2, .game[data-e="3"] .ev3 { display: inline; }
  .lane { position: relative; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; max-width: 440px; margin: 12px auto 0; padding: 6px;
    border-radius: 22px; background: rgba(255,255,255,.18); }
  .z { position: relative; z-index: 1; display: grid; justify-items: center; gap: 2px; padding: 10px 4px 12px; border-radius: 16px;
    background: rgba(255,255,255,.14); transition: background .2s ease, transform .2s ease; }
  .zi { font-size: 26px; line-height: 1.1; }
  .zl { font-size: 13px; font-weight: 900; letter-spacing: .04em; }
  .game[data-z="1"] .z1 { background: rgba(255,255,255,.34); }
  .game[data-z="2"] .z2 { background: #ff8fab; transform: scale(1.05); box-shadow: 0 0 0 3px #fff; }
  .game[data-z="3"] .z3, .game[data-s="late"] .z3 { background: #ff6b3d; }
  .game[data-s="late"] .z3 { animation: shake .4s ease; }
  .game[data-s="calm"] .z2 { background: #b6f5dc; color: #12503f; }
  .wave { position: absolute; z-index: 2; top: 50%; left: 6px; width: 34px; height: 34px; margin: -17px 0 0 -17px; pointer-events: none;
    opacity: 0; transition: opacity .3s ease; }
  .wave i { position: absolute; inset: 0; border-radius: 50%; background: radial-gradient(circle, #fff 0 30%, rgba(255,255,255,.55) 31% 60%, rgba(255,255,255,0) 61%);
    transform: scale(var(--w, .7)); }
  .game[data-s="run"] .wave { opacity: 1; }
  .game[data-z="3"] .wave i { background: radial-gradient(circle, #ffe08a 0 30%, rgba(255,107,61,.6) 31% 60%, rgba(255,107,61,0) 61%); }
  .game[data-s="calm"] .wave { opacity: 0; transition: opacity 1s ease; }
  .sense { max-width: 440px; margin: 10px auto 0; min-height: 30px; font-size: 15.5px; font-weight: 900; }
  .sense > span { display: none; }
  .game[data-z="2"][data-e="1"] .sn1, .game[data-z="2"][data-e="2"] .sn2, .game[data-z="2"][data-e="3"] .sn3 { display: inline; animation: boing .4s ease; }
  .tap { display: block; width: min(320px, 100%); min-height: 84px; margin: 10px auto 0; border: 0; border-radius: 999px; cursor: pointer;
    font: inherit; font-size: clamp(22px, 6vw, 30px); font-weight: 900; color: #123f35; background: #b6f5dc;
    box-shadow: 0 9px 0 #5cc9a3, 0 16px 26px rgba(0,0,0,.16); transition: transform .08s ease, box-shadow .08s ease;
    -webkit-tap-highlight-color: transparent; touch-action: manipulation; user-select: none; -webkit-user-select: none; }
  .tap:active { transform: translateY(7px); box-shadow: 0 2px 0 #5cc9a3, 0 6px 12px rgba(0,0,0,.16); }
  .tap:focus-visible { outline: 4px solid #fff; outline-offset: 4px; }
  .tap > span { display: none; }
  .game[data-b="start"] .t-start, .game[data-b="run"] .t-run, .game[data-b="next"] .t-next, .game[data-b="again"] .t-again { display: inline; }
  .game[data-b="run"] .tap { background: #fff; color: #7a2a4a; box-shadow: 0 9px 0 #ff8fab, 0 16px 26px rgba(0,0,0,.16); }
  .result { margin-top: 14px; min-height: 50px; font-size: 16.5px; font-weight: 900; line-height: 1.45; }
  .result > div { display: none; }
  .game[data-s="idle"] .r-hint, .game[data-s="run"] .r-hint, .game[data-s="calm"] .r-calm, .game[data-s="late"] .r-late, .game[data-s="early"] .r-early { display: block; }
  .game[data-s="calm"] .r-calm, .game[data-s="late"] .r-late, .game[data-s="early"] .r-early { animation: boing .45s ease; }
  .score { display: inline-block; margin-top: 6px; padding: 6px 14px; border-radius: 999px; background: rgba(255,255,255,.2); font-size: 15px; font-weight: 900; }
  .sc { display: inline-block; min-width: 1.2em; }
  .sc-of { margin-left: 4px; opacity: .85; }
  .end { display: none; max-width: 440px; margin: 12px auto 0; padding: 12px 14px; border-radius: 18px; background: #fff; color: #16806a;
    font-size: 16px; font-weight: 900; line-height: 1.45; }
  .game[data-done="1"] .end { display: block; animation: boing .5s ease; }
""",
    dark="""  html[data-theme="dark"] .flow .fl { background: #2a3a36; }
  html[data-theme="dark"] .flow .f2 { background: #3e2a33; }
  html[data-theme="dark"] .ev { background: #23302c; color: #e6fff6; }
  html[data-theme="dark"] .tap { background: #1f5a4a; color: #e6fff6; }
  html[data-theme="dark"] .game[data-b="run"] .tap { background: #3e2a33; color: #ffd6e2; }
  html[data-theme="dark"] .end { background: #23302c; color: #9ff0d6; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var btn = g.querySelector('.tap'), wave = g.querySelector('.wave'), waveI = wave.querySelector('i'), sc = g.querySelector('.sc');
  var e = 0, score = 0, x = 0, t0 = 0, raf = 0, DUR = 2700;
  function set(k, v) { g.setAttribute('data-' + k, String(v)); }
  function zone(p) { return p < 34 ? 1 : p < 67 ? 2 : 3; }
  function place() {
    var w = g.querySelector('.lane').clientWidth - 12;
    wave.style.left = (6 + w * x / 100) + 'px';
    waveI.style.setProperty('--w', (0.6 + x / 100 * 0.9).toFixed(2));
  }
  function tick(t) {
    if (!t0) t0 = t;
    x = Math.min(100, (t - t0) / DUR * 100);
    set('z', zone(x)); place();
    if (x >= 100) { end('late'); return; }
    raf = requestAnimationFrame(tick);
  }
  function run() {
    e = (e % 3) + 1;
    if (e === 1) { score = 0; sc.textContent = '0'; set('done', 0); }
    x = 0; t0 = 0; set('e', e); set('s', 'run'); set('b', 'run'); set('z', 1); place();
    cancelAnimationFrame(raf); raf = requestAnimationFrame(tick);
  }
  function end(r) {
    cancelAnimationFrame(raf);
    if (r === 'calm') {
      score++; sc.textContent = String(score);
      if (window.pengessoPop) { var k = wave.getBoundingClientRect(); window.pengessoPop(k.left + k.width / 2, k.top + k.height / 2, ['🍃', '🐧', '✨'], 12); }
    }
    set('s', r); set('b', e === 3 ? 'again' : 'next');
    if (r !== 'late') set('z', r === 'calm' ? 2 : 1);
    if (e === 3) set('done', 1);
  }
  btn.addEventListener('pointerdown', function () {
    if (g.getAttribute('data-s') !== 'run') return;
    var z = zone(x); end(z === 1 ? 'early' : z === 2 ? 'calm' : 'late');
    btn.setAttribute('data-skip', '1');
  });
  btn.addEventListener('click', function () {
    if (btn.getAttribute('data-skip') === '1') { btn.removeAttribute('data-skip'); return; }
    var s = g.getAttribute('data-s');
    if (s === 'run') { var z = zone(x); end(z === 1 ? 'early' : z === 2 ? 'calm' : 'late'); return; }
    run();
  });
  window.addEventListener('resize', place);
})();
""",
    ja={
        "Catch it in the body": "体でキャッチ",
        "A small wave runs from the event to your feelings. Tap \"Watch it\" while it is in the body.": "小さな波が、出来事から感情へ流れていきます。波が「体」にいるあいだに「見る」を押してね。",
        "Press start. Something will happen.": "スタートを押してね。何かが起きます。",
        "🛒 Someone cuts in line at the store.": "🛒 お店の列に、割りこまれた。",
        "📱 Your message was read, but there is no reply.": "📱 メッセージが既読なのに、返事がない。",
        "☔ It starts to rain on laundry day.": "☔ 洗濯の日に、雨がふってきた。",
        "Event": "出来事",
        "Body": "体",
        "Feeling": "感情",
        "💓 My chest feels uneasy…": "💓 胸がざわっ…",
        "🪨 My stomach feels heavy…": "🪨 おなかが重い…",
        "🧱 My shoulders feel stiff…": "🧱 肩がかたくなる…",
        "▶ Start": "▶ スタート",
        "👀 Watch it": "👀 見る",
        "▶ Next event": "▶ 次の出来事",
        "↺ Play again": "↺ もう一回",
        "Not too early, not too late. Just watch.": "早すぎず、遅すぎず。ただ見るだけ。",
        "🍃 You watched it. It faded before it became a feeling.": "🍃 見ていたら、感情になる前に消えていきました。",
        "🌋 Too late! It became a big feeling.": "🌋 遅かった！大きな感情になっちゃった。",
        "🙈 Too early. Nothing has reached your body yet.": "🙈 早すぎ。まだ体に何も来ていません。",
        "🍃 Caught in the body:": "🍃 体でキャッチ：",
        "/ 3": "/ 3",
        "🐧 When you notice the body first, the wave stays small.": "🐧 体で先に気づくと、波は小さいままです。",
    },
)
build(d)
