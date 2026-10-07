A = dict(
    slug="tap-the-happy-pictures", seq=413,
    title="The habit of seeing bad things first can change with practice",
    title_ja="イヤなものに目がいくクセは、いいものを探す練習で変わる",
    label="Happy Hunt", label_ja="いいもの探し",
    float="🎈",
    alt="A chubby chenille yarn penguin happily pointing up at a real red balloon",
    mood=["lift", "energy"], tags=["psychology", "mindset", "happiness"],
    src_no="15", src_title="注意バイアス",
    center="イヤなものに目がいくクセは、いいものを素早く見つける練習で変えられる。",
    tone="素材の重さ：真面目（人付き合いが苦手な人の目のクセ）\n→ 見せ方：ポップに（青と紫とピンク。本物の「うれしい絵さがし」ゲームで遊べる）",
    tone_css="真面目な話 → ポップに。青とピンク",
    game_name="うれしい絵さがし",
    play="🎈 うれしい絵さがし：大きなタイルが6枚（3×2。細かいマス目にしない）。5枚はどんより（🌧️🧾🗑️🥀🌪️💸🪫🌩️）、1枚だけうれしい絵（🌸☀️🍰🌈🎁🍦🐶🎈🍓🌻 からランダム）。うれしい1枚をできるだけ速くタップ ×8回。まちがえるとタイルがプルプル（ミスの数）。最後に平均の秒数と ⭐、最後の3回が最初の3回より速ければ「📈 目が速くなった！」。自己ベストを端末に覚える。",
    prompt="An extremely cute, chubby round penguin with a gentle face and a plain white belly (no rings or patterns on the belly), made of soft chenille yarn with a plush velvety texture, standing on a small rounded step and happily pointing one flipper up at one realistic shiny red helium balloon on a thin white string, eyes sparkling as if it just found something nice. Bright sky-blue background with a soft lavender-pink gradient and gentle depth, simple and uncluttered. Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering.",
    combo="ペンギン × シェニール糸 × 赤い風船",
    pal=dict(bg="#f3f8ff", text="#1f2a44", muted="#66708a", a="#2f6fed", b="#ff5fa2", c="#ffcf33", d="#20c997",
             big="#2f6fed", bigdark="#a9c4ff", h1="#1d2b55", ink="#1f2a44", shadowc="rgba(50,90,180,.16)",
             bg1="rgba(255,207,51,.30)", bg2="rgba(255,95,162,.16)", bg3="rgba(47,111,237,.14)", photo="#e5efff",
             game="linear-gradient(155deg, #2f80ed 0%, #6c5ce7 55%, #e84393 100%)"),
    cards=[
        dict(e="👀", l="Eye Habit", lj="目のクセ", s=[(
            "It seems that if you find people hard, your eyes naturally go to bad things.",
            "人付き合いが苦手だと、イヤなものに自然と目がいきやすいそうです。", False)]),
        dict(e="🌧️", l="Scary World", lj="怖く見える世界", s=[(
            "If this goes on, the world starts to look more dangerous than it really is.",
            "それが続くと、世の中が本当よりも危なく見えてきます。", False)]),
        dict(e="🎯", l="Good News", lj="いい知らせ", s=[(
            "But they say this habit can change if you practice finding good things fast.",
            "でも、いいものを素早く見つける練習で、このクセは変わるそうです。", False)]),
        dict(e="🎮", l="A Real Game", lj="本当にあるゲーム", s=[(
            "It seems psychology even has a game where you tap happy pictures fast.",
            "心理学には、うれしい絵をすばやくタップするゲームまであるそうです。", False)]),
        "GAME",
        dict(e="✨", l="Eyes Learn", lj="目は育つ", s=[(
            "Your eyes get better with practice, too.",
            "目も、練習すれば上手になります。", True)]),
    ],
    game_html=r'''
  <!-- ⚡ 触って遊べる部品：うれしい絵さがし（6枚の中から、うれしい1枚をすばやくタップ ×8回） -->
  <section class="game" data-s="idle" data-r="" data-learn="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Happy picture hunt</div>
    <div class="game-hint">Only 1 picture is happy. Find it and tap it fast. 8 rounds!</div>
    <div class="hud">
      <div class="hud-box"><span class="hl">Round</span> <span class="rn">0</span>/8</div>
      <div class="hud-box"><span class="hk" aria-hidden="true">⏱</span> <span class="clock">0.0</span></div>
      <div class="hud-box"><span class="hl">Misses</span> <span class="ms">0</span></div>
    </div>
    <div class="tiles">
      <button type="button" class="tile">🌧️</button>
      <button type="button" class="tile">🧾</button>
      <button type="button" class="tile">☀️</button>
      <button type="button" class="tile">🗑️</button>
      <button type="button" class="tile">🥀</button>
      <button type="button" class="tile">🌪️</button>
    </div>
    <div class="result">
      <div class="r-hint">Do not stare at the rain. Hunt for the sun! ☀️</div>
      <div class="r-play">Where is the happy one? 👀</div>
      <div class="r-done">
        <div class="avg-row"><span class="avg-l">Average:</span> <span class="avg">0.00</span> <span class="avg-u">sec</span></div>
        <div class="stars" aria-hidden="true">☆☆☆</div>
        <div class="verdict v-gold">🥇 Super eyes! You find good things fast.</div>
        <div class="verdict v-ok">🥈 Nice! Your eyes are learning.</div>
        <div class="verdict v-slow">🥉 Good start! Play again, and your eyes will get faster.</div>
        <div class="verdict v-learn">📈 Your last 3 rounds were faster than your first 3!</div>
      </div>
    </div>
    <div class="ctrl">
      <button type="button" class="btn b-start"><span class="t-start">▶ Start</span><span class="t-again">↺ Play again</span></button>
    </div>
    <div class="best" hidden><span class="bl">🏆 Your best:</span> <span class="best-v">0.00</span> <span class="bu">sec</span></div>
  </section>
''',
    game_ja={
        "Happy picture hunt": "うれしい絵さがし",
        "Only 1 picture is happy. Find it and tap it fast. 8 rounds!": "うれしい絵は1枚だけ。見つけたら、すばやくタップ。全8回！",
        "Round": "ラウンド",
        "Misses": "ミス",
        "Do not stare at the rain. Hunt for the sun! ☀️": "雨をじっと見ないで。お日さまを探そう！☀️",
        "Where is the happy one? 👀": "うれしいのはどれ？ 👀",
        "Average:": "平均：",
        "sec": "秒",
        "🥇 Super eyes! You find good things fast.": "🥇 すごい目！いいものを見つけるのが速い。",
        "🥈 Nice! Your eyes are learning.": "🥈 いいね！目が覚えてきています。",
        "🥉 Good start! Play again, and your eyes will get faster.": "🥉 いいスタート！もう一回やると、目がもっと速くなります。",
        "📈 Your last 3 rounds were faster than your first 3!": "📈 最後の3回は、最初の3回より速かった！",
        "▶ Start": "▶ スタート",
        "↺ Play again": "↺ もう一回",
        "🏆 Your best:": "🏆 自己ベスト：",
    },
    css=r'''
  /* 🎈 うれしい絵さがし */
  .hud { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; max-width: 400px; margin: 14px auto 0; }
  .hud-box { display: flex; align-items: center; justify-content: center; gap: 4px; flex-wrap: wrap; min-height: 44px; padding: 6px 8px;
    border-radius: 14px; background: rgba(255,255,255,.2); font-size: 15px; font-weight: 900; }
  .rn, .clock, .ms, .avg, .best-v { font-variant-numeric: tabular-nums; }
  .tiles { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; max-width: 360px; margin: 14px auto 0; }
  .tile { aspect-ratio: 1 / 1; min-height: 88px; border: 0; border-radius: 24px; background: #fff; font-size: clamp(40px, 12vw, 54px); line-height: 1;
    cursor: pointer; box-shadow: 0 6px 0 rgba(0,0,0,.14), 0 12px 20px rgba(0,0,0,.12); -webkit-tap-highlight-color: transparent; touch-action: manipulation;
    user-select: none; -webkit-user-select: none; transition: transform .08s ease, opacity .2s ease, background .2s ease; }
  .tile:active { transform: translateY(3px) scale(.97); }
  .tile:focus-visible { outline: 4px solid #fff; outline-offset: 3px; }
  .game[data-s="idle"] .tile, .game[data-s="done"] .tile { opacity: .55; }
  @keyframes deal { from { opacity: 0; transform: scale(.7) rotate(-6deg); } to { opacity: 1; transform: none; } }
  .tile.deal { animation: deal .26s cubic-bezier(.2,1.3,.4,1) both; }
  .tile.good { background: #fff3a8; animation: g-pop .3s cubic-bezier(.2,1.4,.4,1); box-shadow: 0 0 0 5px #ffe066, 0 10px 24px rgba(0,0,0,.18); }
  .tile.bad { background: #e3e6ef; opacity: .6; animation: g-shake .35s ease; }
  .result { min-height: 76px; margin-top: 16px; }
  .result > div { display: none; }
  .game[data-s="idle"] .r-hint, .game[data-s="play"] .r-play, .game[data-s="done"] .r-done { display: block; animation: g-in .35s ease-out; }
  .r-hint, .r-play { font-size: 16.5px; font-weight: 900; padding-top: 8px; }
  .avg-row { font-size: 17px; font-weight: 900; }
  .avg { font-size: clamp(36px, 10vw, 52px); letter-spacing: -.03em; }
  .stars { font-size: 26px; letter-spacing: .12em; margin-top: 2px; }
  .verdict { display: none; margin-top: 6px; font-size: 16.5px; font-weight: 900; line-height: 1.45; }
  .game[data-r="gold"] .v-gold, .game[data-r="ok"] .v-ok, .game[data-r="slow"] .v-slow, .game[data-learn="1"] .v-learn { display: block; }
  .v-learn { display: none; margin: 10px auto 0; max-width: 400px; padding: 8px 12px; border-radius: 14px; background: rgba(255,255,255,.2); }
  .b-start { color: #5b3cc4; min-width: 200px; }
  .b-start span { display: none; }
  .game[data-s="idle"] .t-start, .game[data-s="done"] .t-again { display: inline; }
  .game[data-s="play"] .ctrl { visibility: hidden; }
  .best { margin-top: 12px; font-size: 13.5px; font-weight: 900; opacity: .92; }
  .best[hidden] { display: none; }
''',
    dark=r'''
  html[data-theme="dark"] .tile { background: #f1edf8; }
  html[data-theme="dark"] .tile.good { background: #fff3a8; }
  html[data-theme="dark"] .tile.bad { background: #c9ccd8; }
''',
    js=r'''
/* 🎈 うれしい絵さがし：JS は data-*・class・絵文字・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var tiles = [].slice.call(g.querySelectorAll('.tile'));
  var rn = g.querySelector('.rn'), ms = g.querySelector('.ms'), clock = g.querySelector('.clock'),
      avgEl = g.querySelector('.avg'), stars = g.querySelector('.stars'), best = g.querySelector('.best');
  var HAPPY = ['🌸', '☀️', '🍰', '🌈', '🎁', '🍦', '🐶', '🎈', '🍓', '🌻'];
  var GLOOM = ['🌧️', '🧾', '🗑️', '🥀', '🌪️', '💸', '🪫', '🌩️'];
  var KEY = 'pengesso-tap-the-happy-pictures-best';
  var ROUNDS = 8, round = 0, misses = 0, times = [], happyAt = -1, t0 = 0, lock = true, tick = 0, happyList = [];
  function now() { return (window.performance && performance.now) ? performance.now() : Date.now(); }
  function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function set(s) { g.setAttribute('data-s', s); }
  function showBest() {
    var b = 0; try { b = parseFloat(localStorage.getItem(KEY)) || 0; } catch (e) {}
    if (b) { best.hidden = false; best.querySelector('.best-v').textContent = b.toFixed(2); }
  }
  function deal() {
    round++; rn.textContent = String(round);
    var gl = shuffle(GLOOM);
    happyAt = Math.floor(Math.random() * tiles.length);
    var k = 0;
    tiles.forEach(function (t, i) {
      t.classList.remove('good', 'bad', 'deal');
      t.textContent = i === happyAt ? happyList[round - 1] : gl[k++];
      void t.offsetWidth; t.classList.add('deal');
    });
    t0 = now(); lock = false;
  }
  function start() {
    round = 0; misses = 0; times = []; ms.textContent = '0';
    happyList = shuffle(HAPPY);
    g.setAttribute('data-r', ''); g.setAttribute('data-learn', '0');
    set('play'); deal();
    clearInterval(tick);
    tick = setInterval(function () { if (!lock) clock.textContent = ((now() - t0) / 1000).toFixed(1); }, 100);
  }
  function mean(a) { var s = 0; for (var i = 0; i < a.length; i++) s += a[i]; return a.length ? s / a.length : 0; }
  function finish() {
    clearInterval(tick); lock = true;
    var avg = mean(times) / 1000;
    var r = avg < 0.9 ? 'gold' : avg < 1.5 ? 'ok' : 'slow';
    avgEl.textContent = avg.toFixed(2);
    stars.textContent = r === 'gold' ? '⭐⭐⭐' : r === 'ok' ? '⭐⭐☆' : '⭐☆☆';
    var learn = mean(times.slice(-3)) < mean(times.slice(0, 3)) * 0.92;
    g.setAttribute('data-learn', learn ? '1' : '0');
    g.setAttribute('data-r', r);
    set('done');
    try { var b = parseFloat(localStorage.getItem(KEY)) || 0; if (!b || avg < b) localStorage.setItem(KEY, avg.toFixed(2)); } catch (e) {}
    showBest();
    if (window.pengessoPop && (r !== 'slow' || learn)) {
      var q = stars.getBoundingClientRect();
      window.pengessoPop(q.left + q.width / 2, q.top + q.height / 2, ['🌸', '☀️', '🌈', '🎈', '🐧', '✨'], r === 'gold' ? 24 : 14);
    }
  }
  tiles.forEach(function (t, i) {
    t.addEventListener('click', function () {
      if (lock || g.getAttribute('data-s') !== 'play') return;
      if (i === happyAt) {
        lock = true;
        var dt = now() - t0; times.push(dt);
        clock.textContent = (dt / 1000).toFixed(1);
        t.classList.remove('deal'); t.classList.add('good');
        if (window.pengessoPop) { var q = t.getBoundingClientRect(); window.pengessoPop(q.left + q.width / 2, q.top + q.height / 2, ['✨', t.textContent], 6); }
        setTimeout(function () { if (round < ROUNDS) deal(); else finish(); }, 320);
      } else if (!t.classList.contains('bad')) {
        misses++; ms.textContent = String(misses);
        t.classList.remove('deal'); t.classList.add('bad');
        if (navigator.vibrate) { try { navigator.vibrate(15); } catch (e) {} }
      }
    });
  });
  g.querySelector('.b-start').addEventListener('click', function () {
    var s = g.getAttribute('data-s');
    if (s === 'idle' || s === 'done') start();
  });
  showBest();
})();
''',
)
