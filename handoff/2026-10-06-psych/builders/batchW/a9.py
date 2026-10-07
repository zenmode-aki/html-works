from gen import build

d = dict(
    slug="habits-before-skills", seq=520,
    title=("Grow your daily habits first, and skills will follow by themselves",
           "スキルより先に、毎日の習慣。そうすれば、スキルは自然についてくる"),
    label=("Roots First", "根っこが先"),
    h1_emoji="🌳",
    alt="A chubby chenille yarn penguin watering a small potted tree with a real metal watering can",
    section="幸せに大切な2つ",
    message="スキルより、どう生きたいかという考え方と毎日の習慣。根っこが育てば、スキルはあとから自然についてくる。",
    tone="素材の重さ：真面目（スキルと習慣）\n→ 見せ方：ポップに（緑とオレンジ。実をテープではっても落ちる／根っこに水をやると実が自然になる）",
    game_ja="🌳 根っこと実：「🍎 スキルをテープではる」を押すと、木に実がつくけれど、根っこがないのでポトッと落ちる（落ちた数が増える）。「💧 根っこに水をやる」を押すと、地面の下で根っこがのびて「どう生きたいか」「毎日の習慣」の名前が出る。水を2回やるごとに、実が1つ自然になって、もう落ちない。4つなったら、まとめの一言。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of soft chenille yarn, "
            "carefully watering a small young tree in a pot with a realistic galvanized metal watering can, a few red apples on the tree. "
            "Bright simple fresh green and warm orange background with soft depth. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × シェニール糸 × じょうろ",
    mood=["lift", "learn"], tags=["psychology", "study", "mindset"],
    pal=dict(bg="#f5fff1", muted="#64805a", acc="#258a3c", acc2="#ff6b3d", shadow="rgba(40,110,50,.16)",
             r1="rgba(255,190,80,.28)", r2="rgba(37,138,60,.18)", r3="rgba(255,107,61,.14)",
             h1="#173a1f", photo="#e3f7dc", big="#1f7a33", bigdark="#9be8a8",
             game="linear-gradient(170deg, #4fc3ff 0%, #39b56a 52%, #a0682e 100%)"),
    cards=[
        dict(emoji="🍎", label=("Skills Alone", "スキルだけ"),
             s=[("It is said that skills alone do not change your life very much.",
                 "スキルだけを身につけても、人生はそこまで大きく変わらないそうです。")]),
        dict(emoji="🌱", label=("What Matters", "大事なもの"),
             s=[("What matters is your idea of how you want to live, and your daily habits.",
                 "大事なのは、どう生きたいかという考え方と、毎日の習慣です。")]),
        dict(emoji="🌳", label=("Roots First", "根っこが先"), big=True,
             s=[("When these roots grow, the fruit called skills comes later by itself.",
                 "この根っこが育つと、スキルという実は、あとから自然についてきます。")]),
        dict(emoji="☕", label=("10 Minutes", "10分から"),
             s=[("Even for a certificate exam, I think it is fine to start with a habit like \"10 minutes every morning with coffee.\"",
                 "資格の勉強も、まずは「毎朝コーヒーを飲みながら10分」という習慣からでいいと思います。")]),
    ],
    game_after=3,
    game_note="根っこと実（テープの実は落ちる・根っこが育つと実が自然になる）",
    game_html="""  <section class="game" data-msg="" data-f="0" data-end="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Roots and fruit</div>
    <div class="game-hint">Try both buttons. Which fruit stays on the tree?</div>
    <div class="yard">
      <div class="crown"></div>
      <div class="trunk"></div>
      <span class="fruit f1">🍎</span><span class="fruit f2">🍎</span><span class="fruit f3">🍎</span><span class="fruit f4">🍎</span>
      <div class="taped"><span class="tp-e">🍎</span><span class="tp-t">🩹</span></div>
      <div class="soil">
        <svg class="roots" viewBox="0 0 200 90" preserveAspectRatio="none" aria-hidden="true">
          <path class="rt" pathLength="100" d="M100 0 C100 30 70 40 40 80" />
          <path class="rt" pathLength="100" d="M100 0 C100 40 100 60 100 88" />
          <path class="rt" pathLength="100" d="M100 0 C100 30 130 40 160 80" />
        </svg>
        <span class="rl rl1">🧭 How I want to live</span>
        <span class="rl rl2">⏰ Daily habits</span>
      </div>
    </div>
    <div class="msg">
      <span class="m-0">Which fruit stays on the tree?</span>
      <span class="m-drop">Plop! No roots, so it fell. 🍂</span>
      <span class="m-water">💧 The roots grow a little deeper.</span>
      <span class="m-grow">🍎 A fruit grew by itself!</span>
    </div>
    <div class="ctl">
      <button type="button" class="btn b-tape">🍎 Tape on a skill</button>
      <button type="button" class="btn b-water">💧 Water the roots</button>
    </div>
    <div class="score"><span class="s-f">🍂 Fell:</span> <span class="nfall">0</span> <span class="s-sep">·</span> <span class="s-g">🍎 Stayed:</span> <span class="nf">0</span> <span class="s-of">/ 4</span></div>
    <div class="end">🌳 4 fruits grew by themselves. Roots first, then fruit!</div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Start over</button></div>
  </section>""",
    css="""
  /* 🌳 根っこと実 */
  .yard { position: relative; height: 300px; max-width: 420px; margin: 16px auto 0; border-radius: 24px; overflow: hidden; background: #dff3ff; }
  .crown { position: absolute; left: 50%; top: 18px; width: 200px; height: 130px; margin-left: -100px; border-radius: 50%; background: #5cc95f;
    box-shadow: inset 0 -12px 0 rgba(0,0,0,.08); }
  .trunk { position: absolute; left: 50%; top: 130px; width: 26px; height: 60px; margin-left: -13px; border-radius: 6px; background: #9a6332; }
  .fruit { position: absolute; font-size: 30px; line-height: 1; opacity: 0; transform: scale(.2); transition: opacity .4s ease, transform .5s cubic-bezier(.3,1.6,.5,1); }
  .f1 { left: calc(50% - 74px); top: 60px; } .f2 { left: calc(50% + 40px); top: 50px; } .f3 { left: calc(50% - 30px); top: 34px; } .f4 { left: calc(50% + 2px); top: 92px; }
  .game[data-f="1"] .f1, .game[data-f="2"] .f1, .game[data-f="2"] .f2, .game[data-f="3"] .f1, .game[data-f="3"] .f2, .game[data-f="3"] .f3,
  .game[data-f="4"] .fruit { opacity: 1; transform: scale(1); }
  .taped { position: absolute; left: calc(50% + 50px); top: 96px; display: flex; align-items: center; opacity: 0; pointer-events: none; }
  .tp-e { font-size: 30px; line-height: 1; } .tp-t { font-size: 18px; margin-left: -14px; transform: rotate(-30deg); }
  .taped.go { animation: drop 1.3s ease-in forwards; }
  @keyframes drop { 0% { opacity: 0; transform: scale(.4); } 15% { opacity: 1; transform: scale(1.1); } 45% { opacity: 1; transform: rotate(-12deg); }
    85% { opacity: 1; transform: translateY(88px) rotate(40deg); } 100% { opacity: 0; transform: translateY(92px) rotate(50deg); } }
  .soil { position: absolute; left: 0; right: 0; bottom: 0; height: 110px; background: #a87445; border-top: 8px solid #6cbf45; }
  .roots { position: absolute; left: 50%; top: 0; width: 220px; height: 96px; margin-left: -110px; }
  .rt { fill: none; stroke: #f3d9a8; stroke-width: 7; stroke-linecap: round; stroke-dasharray: 100; stroke-dashoffset: 100; transition: stroke-dashoffset .6s ease; }
  .rl { position: absolute; padding: 3px 8px; border-radius: 10px; background: rgba(255,255,255,.88); color: #4a2c10; font-size: 12.5px; font-weight: 900;
    line-height: 1.25; max-width: 44%; opacity: 0; transform: translateY(6px); transition: opacity .4s ease, transform .4s ease; }
  .rl1 { left: 8px; bottom: 10px; } .rl2 { right: 8px; bottom: 10px; text-align: right; }
  .game.d1 .rl1, .game.d2 .rl2 { opacity: 1; transform: none; }
  .msg { min-height: 32px; margin-top: 12px; font-size: 16px; font-weight: 900; }
  .msg span { display: none; }
  .game[data-msg=""] .m-0, .game[data-msg="drop"] .m-drop, .game[data-msg="water"] .m-water, .game[data-msg="grow"] .m-grow { display: inline; }
  .ctl { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 420px; margin: 8px auto 0; }
  .ctl .btn { min-height: 62px; border-radius: 18px; font-size: 15px; padding: 8px 10px; }
  .b-tape { background: #ffe1d6; color: #7a2a0e; }
  .b-water { background: #d6f1ff; color: #0d4f7a; }
  .score { margin-top: 14px; font-size: 15px; font-weight: 900; }
  .nfall, .nf { display: inline-block; min-width: 1.4em; padding: 1px 8px; border-radius: 999px; background: rgba(255,255,255,.3); }
  .end { display: none; margin: 14px auto 0; max-width: 420px; padding: 12px 14px; border-radius: 18px; background: #fff; color: #1d5a2a; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .game[data-end="1"] .end { display: block; animation: boing .5s ease; }
  .ctrl { margin-top: 12px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
""",
    dark="""  html[data-theme="dark"] .yard { background: #1d2f45; }
  html[data-theme="dark"] .crown { background: #2f7a36; }
  html[data-theme="dark"] .soil { background: #5a3e24; border-top-color: #3f6b2c; }
  html[data-theme="dark"] .rl { background: rgba(30,32,44,.9); color: #f3d9a8; }
  html[data-theme="dark"] .b-tape { background: #4a2418; color: #ffd0be; }
  html[data-theme="dark"] .b-water { background: #1f3a50; color: #cfeaff; }
  html[data-theme="dark"] .end { background: #2b2d3a; color: #b8f0c4; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var depth = 0, fruits = 0, fell = 0, MAX = 8;
  var taped = g.querySelector('.taped'), rts = g.querySelectorAll('.rt');
  function again(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function paint() {
    [].forEach.call(rts, function (r) { r.style.strokeDashoffset = String(100 - depth * 12.5); });
    g.classList.toggle('d1', depth >= 1); g.classList.toggle('d2', depth >= 2);
    g.setAttribute('data-f', String(fruits));
    g.querySelector('.nf').textContent = fruits; g.querySelector('.nfall').textContent = fell;
  }
  g.querySelector('.b-tape').addEventListener('click', function () {
    again(taped, 'go');
    fell++; g.setAttribute('data-msg', 'drop');
    setTimeout(paint, 900);
  });
  g.querySelector('.b-water').addEventListener('click', function () {
    if (depth >= MAX) return;
    depth++;
    var grew = depth % 2 === 0;
    if (grew) fruits = depth / 2;
    g.setAttribute('data-msg', grew ? 'grow' : 'water');
    paint();
    if (window.pengessoPop) {
      var y = grew ? g.querySelector('.crown').getBoundingClientRect() : g.querySelector('.soil').getBoundingClientRect();
      window.pengessoPop(y.left + y.width / 2, y.top + 30, grew ? ['🍎', '✨'] : ['💧'], grew ? 10 : 5);
    }
    if (fruits === 4 && g.getAttribute('data-end') !== '1') {
      g.setAttribute('data-end', '1');
      setTimeout(function () { if (window.pengessoPop) { var c = g.querySelector('.crown').getBoundingClientRect(); window.pengessoPop(c.left + c.width / 2, c.top + 40, ['🌳', '🍎', '🐧', '✨'], 20); } }, 400);
    }
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    depth = 0; fruits = 0; fell = 0; taped.classList.remove('go');
    g.setAttribute('data-msg', ''); g.setAttribute('data-end', '0'); paint();
  });
})();
""",
    ja={
        "Roots and fruit": "根っこと実",
        "Try both buttons. Which fruit stays on the tree?": "両方のボタンを押してみてね。木に残るのは、どっちの実？",
        "🧭 How I want to live": "🧭 どう生きたいか",
        "⏰ Daily habits": "⏰ 毎日の習慣",
        "Which fruit stays on the tree?": "木に残るのは、どっちの実？",
        "Plop! No roots, so it fell. 🍂": "ポトッ！根っこがないので、落ちました 🍂",
        "💧 The roots grow a little deeper.": "💧 根っこが少し深くのびました。",
        "🍎 A fruit grew by itself!": "🍎 実が自然になった！",
        "🍎 Tape on a skill": "🍎 スキルをテープではる",
        "💧 Water the roots": "💧 根っこに水をやる",
        "🍂 Fell:": "🍂 落ちた：",
        "·": "·",
        "🍎 Stayed:": "🍎 残った：",
        "/ 4": "/ 4",
        "🌳 4 fruits grew by themselves. Roots first, then fruit!": "🌳 実が4つ、自然になりました。根っこが先、実はあと！",
        "↺ Start over": "↺ 最初から",
    },
)
build(d)
