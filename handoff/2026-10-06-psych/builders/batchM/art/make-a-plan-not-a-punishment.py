A = dict(
    slug="make-a-plan-not-a-punishment", seq=412,
    title="Instead of blaming yourself, make a small plan for next time",
    title_ja="自分を責める反省より、次の小さな対策を考えよう",
    label="Plan, Not Blame", label_ja="責めずに対策",
    float="⏰",
    alt="A chubby corduroy penguin setting a real twin-bell alarm clock in warm morning light",
    mood=["lift", "think"], tags=["psychology", "mistakes", "mindset"],
    src_no="13", src_title="反省は心の無駄使い",
    center="自分を責める「反省」は心に傷を増やすだけ。「次はどうする？」の小さな対策を考える。",
    tone="素材の重さ：真面目（自分を責めるクセ）\n→ 見せ方：ポップに（朝焼けのオレンジと紫。遅刻ループのゲームで遊べる）",
    tone_css="真面目な話 → ポップに。朝焼けのオレンジ",
    game_name="遅刻ループ",
    play="⏰ 遅刻ループ：9:05、また遅刻。「😣 自分を責める」を押すと、心のハートに 🩹 が1つ増えて、次の朝もやっぱり 9:05 に着く（📅 の日数だけ進む。3回責めると「責めても時計は動かない」）。「📝 対策を立てる」を押すと、小さな対策を3つから1つ選べる（目覚まし10分早く／服を前の夜に出す／カバンを前の夜に用意）→ 次の朝のリプレイで 8:55 に到着、「ON TIME」のハンコと 💖。「↺ もう一回」。",
    prompt="An extremely cute, chubby round penguin with a gentle face and a plain white belly (no rings or patterns on the belly), made of plush toy corduroy and felt with soft visible ribs, standing next to one realistic classic twin-bell alarm clock in shiny red metal and reaching out a flipper to set it, with a calm, determined little smile. Bright warm background in sunrise orange and soft butter yellow with gentle depth and a soft glow, simple and uncluttered. Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering.",
    combo="ペンギン × コーデュロイとフェルトのぬいぐるみ × 目覚まし時計",
    pal=dict(bg="#fff7ef", text="#3a2a22", muted="#85705f", a="#e8590c", b="#7b61ff", c="#ffd23f", d="#19b5a5",
             big="#d9480f", bigdark="#ffc9a3", h1="#3b2418", ink="#3a2a22", shadowc="rgba(150,80,30,.16)",
             bg1="rgba(255,170,80,.30)", bg2="rgba(123,97,255,.16)", bg3="rgba(25,181,165,.14)", photo="#ffe9d6",
             game="linear-gradient(150deg, #ef5f0a 0%, #e8436a 55%, #6a4cff 100%)"),
    cards=[
        dict(e="🔁", l="The Loop", lj="くり返し", s=[(
            'It seems that if you keep thinking, "Late again. I am no good," you become timid.',
            "「また遅刻した。私はダメだ」と反省ばかりしていると、臆病になっていくそうです。", False)]),
        dict(e="📋", l="A Study", lj="調査", s=[(
            "A study found that less confident people thought about their mistakes more.",
            "自信のない人ほど、よく反省していたという調査があります。", False)]),
        dict(e="🩹", l="Small Scratches", lj="小さな傷", s=[(
            "Each time you blame yourself, your heart gets a small scratch.",
            "自分を責めるたびに、心に小さな傷がつきます。", False)]),
        "GAME",
        dict(e="🧭", l="Ask Next", lj="次はどうする", s=[(
            'So instead of "I am no good," think "What will I do next?"',
            "だから「私はダメだ」ではなく、「次はどうする？」を考えます。", True)]),
        dict(e="⏰", l="Small Plan", lj="小さな対策", s=[(
            'For example, a small, clear plan like "alarm 10 minutes earlier" is good.',
            "たとえば「目覚ましを10分早く」のような、小さくて具体的な対策がいいです。", False)]),
    ],
    game_html=r'''
  <!-- ⚡ 触って遊べる部品：遅刻ループ（責めても次の朝は同じ。小さな対策を1つ選ぶと、次の朝が変わる） -->
  <section class="game" data-s="late" data-r="" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Late again! What will you do?</div>
    <div class="hud">
      <div class="hud-box hud-day" aria-hidden="true">📅 <span class="dn">1</span></div>
      <div class="hud-box hud-heart" aria-hidden="true"><span class="hh">❤️</span><span class="sc"></span><span class="sc"></span><span class="sc"></span></div>
      <div class="hud-box hud-plan"><span class="pl-w">Plan:</span> <span class="pl-e">❔</span></div>
    </div>
    <div class="road">
      <div class="road-top">
        <div class="clock"><span class="ck-e" aria-hidden="true">🕘</span><span class="tm">9:05</span></div>
        <div class="bell">🔔 Class starts at 9:00</div>
      </div>
      <div class="lane">
        <span class="lane-home" aria-hidden="true">🏠</span>
        <span class="lane-goal" aria-hidden="true">🏫</span>
        <span class="runner" aria-hidden="true">🐧</span>
        <span class="stamp st-late">LATE</span>
        <span class="stamp st-ok">ON TIME</span>
      </div>
    </div>
    <div class="say">
      <span class="s-late">Oh no, 9:05. Late again! What will you do?</span>
      <span class="s-blame">"I am no good… I am always like this." 😣</span>
      <span class="s-run">The next morning… 🌅</span>
      <span class="s-again">A new scratch on your heart… and the same morning again. 🔁</span>
      <span class="s-again3">3 scratches, and still late. Blaming does not move the clock. ⏰</span>
      <span class="s-choose">Good! Pick 1 small plan for tomorrow.</span>
      <span class="s-win">8:55. On time! ✨ A small plan changed tomorrow.</span>
    </div>
    <div class="ctrls">
      <div class="ctrl c-main">
        <button type="button" class="btn b-blame">😣 Blame myself</button>
        <button type="button" class="btn b-plan">📝 Make a plan</button>
      </div>
      <div class="ctrl c-plans">
        <button type="button" class="btn pick" data-e="⏰">⏰ Set the alarm 10 min earlier</button>
        <button type="button" class="btn pick" data-e="👕">👕 Lay out my clothes at night</button>
        <button type="button" class="btn pick" data-e="🎒">🎒 Pack my bag at night</button>
      </div>
      <div class="ctrl c-end">
        <button type="button" class="btn ghost b-reset">↺ Try again</button>
      </div>
    </div>
  </section>
''',
    game_ja={
        "Late again! What will you do?": "また遅刻！どうする？",
        "Plan:": "対策：",
        "🔔 Class starts at 9:00": "🔔 授業は9:00から",
        "LATE": "遅刻",
        "ON TIME": "間に合った",
        "Oh no, 9:05. Late again! What will you do?": "あっ、9:05。また遅刻！どうする？",
        "\"I am no good… I am always like this.\" 😣": "「私はダメだ…いつもこうだ」😣",
        "The next morning… 🌅": "次の朝… 🌅",
        "A new scratch on your heart… and the same morning again. 🔁": "心に傷が1つ増えた…そして、また同じ朝。🔁",
        "3 scratches, and still late. Blaming does not move the clock. ⏰": "傷が3つ。それでも遅刻。責めても時計は動きません。⏰",
        "Good! Pick 1 small plan for tomorrow.": "いいね！明日のための小さな対策を1つ選んで。",
        "8:55. On time! ✨ A small plan changed tomorrow.": "8:55。間に合った！✨ 小さな対策が、明日を変えました。",
        "😣 Blame myself": "😣 自分を責める",
        "📝 Make a plan": "📝 対策を立てる",
        "⏰ Set the alarm 10 min earlier": "⏰ 目覚ましを10分早くする",
        "👕 Lay out my clothes at night": "👕 服を前の夜に出しておく",
        "🎒 Pack my bag at night": "🎒 カバンを前の夜に用意する",
        "↺ Try again": "↺ もう一回",
    },
    css=r'''
  /* ⏰ 遅刻ループ */
  .hud { display: grid; grid-template-columns: auto auto 1fr; gap: 8px; max-width: 440px; margin: 14px auto 0; }
  .hud-box { display: flex; align-items: center; justify-content: center; gap: 3px; min-height: 44px; padding: 6px 10px;
    border-radius: 14px; background: rgba(255,255,255,.2); font-size: 16px; font-weight: 900; }
  .dn, .tm { font-variant-numeric: tabular-nums; }
  .hh { font-size: 20px; display: inline-block; }
  .sc { font-size: 15px; display: inline-block; min-width: 4px; }
  .sc:not(:empty) { animation: g-pop .45s cubic-bezier(.2,1.4,.4,1); }
  .pl-e { display: inline-block; font-size: 20px; }
  .road { max-width: 440px; margin: 12px auto 0; padding: 12px 12px 14px; border-radius: 22px; background: #fff; color: var(--ink); text-align: left; }
  .road-top { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 4px 10px; }
  .clock { display: flex; align-items: center; gap: 6px; font-size: 32px; font-weight: 900; letter-spacing: -.02em; }
  .ck-e { font-size: 26px; }
  .bell { font-size: 14px; font-weight: 900; color: #85705f; }
  .lane { position: relative; height: 70px; margin-top: 10px; border-radius: 999px; background: linear-gradient(180deg, #ffe8d2, #ffd6b0); overflow: hidden; }
  .lane-home, .lane-goal { position: absolute; top: 50%; transform: translateY(-50%); font-size: 30px; line-height: 1; }
  .lane-home { left: 10px; }
  .lane-goal { right: 10px; }
  .runner { position: absolute; top: 15px; left: 78%; font-size: 36px; line-height: 1; transition: left 1.5s linear; }
  .game.running .runner { animation: g-bounce .38s ease-in-out infinite; }
  .stamp { position: absolute; left: 50%; top: 50%; padding: 4px 12px; border: 4px solid currentColor; border-radius: 12px; background: rgba(255,255,255,.9);
    font-size: 19px; font-weight: 900; letter-spacing: .06em; transform: translate(-50%, -50%) rotate(-10deg); opacity: 0; pointer-events: none; }
  .st-late { color: #e03131; }
  .st-ok { color: #0c9b66; }
  @keyframes stamp-in { 0% { opacity: 0; transform: translate(-50%, -50%) rotate(-10deg) scale(2); } 100% { opacity: 1; transform: translate(-50%, -50%) rotate(-10deg) scale(1); } }
  .game[data-s="late"] .st-late, .game[data-s="blame"] .st-late, .game[data-s="win"] .st-ok { opacity: 1; animation: stamp-in .35s cubic-bezier(.2,1.3,.4,1); }
  .say { display: flex; align-items: center; justify-content: center; max-width: 440px; min-height: 60px; margin: 12px auto 0; padding: 10px 14px;
    border-radius: 18px; background: rgba(255,255,255,.18); font-size: 16.5px; font-weight: 900; line-height: 1.45; }
  .say span { display: none; }
  .game[data-s="late"][data-r=""] .s-late, .game[data-s="late"][data-r="again"] .s-again, .game[data-s="late"][data-r="again3"] .s-again3,
  .game[data-s="blame"] .s-blame, .game[data-s="run"] .s-run, .game[data-s="choose"] .s-choose, .game[data-s="win"] .s-win { display: inline; animation: g-in .35s ease-out; }
  .game[data-s="blame"] .say { background: rgba(40,20,60,.28); }
  .ctrls { min-height: 68px; }
  .ctrls .ctrl { display: none; }
  .game[data-s="late"] .c-main, .game[data-s="blame"] .c-main, .game[data-s="run"] .c-main, .game[data-s="win"] .c-end { display: flex; }
  .game[data-s="blame"] .c-main, .game[data-s="run"] .c-main { opacity: .45; pointer-events: none; }
  .game[data-s="choose"] .c-plans { display: flex; flex-direction: column; align-items: stretch; max-width: 360px; margin-inline: auto; }
  .b-blame { color: #7a3b52; }
  .b-plan { color: #c2410c; }
''',
    dark=r'''
  html[data-theme="dark"] .road { background: #f1edf8; }
  html[data-theme="dark"] .stamp { background: #f1edf8; }
''',
    js=r'''
/* ⏰ 遅刻ループ：JS は data-s / data-r・絵文字・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var tm = g.querySelector('.tm'), ck = g.querySelector('.ck-e'), runner = g.querySelector('.runner'), dn = g.querySelector('.dn'),
      hh = g.querySelector('.hh'), scs = g.querySelectorAll('.sc'), ple = g.querySelector('.pl-e');
  var day = 1, scratches = 0, busy = false, timers = [], ivs = [];
  function calm() { try { return !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches); } catch (e) { return false; } }
  function later(fn, ms) { timers.push(setTimeout(fn, calm() ? 0 : ms)); }
  function stopAll() { timers.forEach(clearTimeout); ivs.forEach(clearInterval); timers = []; ivs = []; g.classList.remove('running'); }
  function set(s, r) { g.setAttribute('data-s', s); if (r !== undefined) g.setAttribute('data-r', r); }
  function fmt(min) { var h = Math.floor(min / 60), m = min % 60; return h + ':' + (m < 10 ? '0' : '') + m; }
  function place(p, instant) {
    if (instant) runner.style.transition = 'none';
    runner.style.left = (5 + p * 73) + '%';
    if (instant) { void runner.offsetWidth; runner.style.transition = ''; }
  }
  function bump(el) { el.classList.remove('pop'); void el.offsetWidth; el.classList.add('pop'); }
  function paintHeart() { for (var i = 0; i < scs.length; i++) scs[i].textContent = i < scratches ? '🩹' : ''; }
  function pop(list, n) {
    if (!window.pengessoPop) return;
    var r = runner.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, n);
  }
  /* 次の朝のリプレイ：家から出発して、時計の数字を進める */
  function replay(from, to, done) {
    day++; dn.textContent = String(day); bump(dn);
    set('run'); ck.textContent = '🕗';
    place(0, true); tm.textContent = fmt(from);
    if (calm()) { place(1, true); tm.textContent = fmt(to); done(); return; }
    g.classList.add('running');
    later(function () {
      place(1);
      var t0 = Date.now(), dur = 1500;
      var iv = setInterval(function () {
        var k = Math.min(1, (Date.now() - t0) / dur);
        tm.textContent = fmt(Math.round(from + (to - from) * k));
        if (k >= 1) { clearInterval(iv); g.classList.remove('running'); done(); }
      }, 50);
      ivs.push(iv);
    }, 450);
  }
  g.querySelector('.b-blame').addEventListener('click', function () {
    if (busy || g.getAttribute('data-s') !== 'late') return;
    busy = true;
    scratches = Math.min(3, scratches + 1); paintHeart();
    hh.classList.remove('shake'); void hh.offsetWidth; hh.classList.add('shake');
    set('blame');
    if (navigator.vibrate) { try { navigator.vibrate(20); } catch (e) {} }
    later(function () {
      replay(525, 545, function () { ck.textContent = '🕘'; set('late', scratches >= 3 ? 'again3' : 'again'); busy = false; });
    }, 1500);
  });
  g.querySelector('.b-plan').addEventListener('click', function () {
    if (busy || g.getAttribute('data-s') !== 'late') return;
    set('choose');
  });
  [].forEach.call(g.querySelectorAll('.pick'), function (b) {
    b.addEventListener('click', function () {
      if (busy || g.getAttribute('data-s') !== 'choose') return;
      busy = true;
      ple.textContent = b.getAttribute('data-e'); bump(ple);
      replay(515, 535, function () {
        ck.textContent = '🕣'; hh.textContent = '💖'; bump(hh);
        set('win'); busy = false;
        pop(['⏰', '✨', '🐧', '🌅', '💖'], 18);
        if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
      });
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    stopAll(); busy = false; day = 1; scratches = 0;
    dn.textContent = '1'; paintHeart(); hh.textContent = '❤️'; ple.textContent = '❔'; ck.textContent = '🕘';
    tm.textContent = '9:05'; place(1, true); set('late', '');
  });
  place(1, true);
})();
''',
)
