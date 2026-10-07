from gen import build

d = dict(
    slug="find-a-place-you-can-win", seq=524,
    title=("Stop the fight you cannot win, and find your own sea",
           "勝てない戦いをやめると、自分が勝てる場所が見つかる"),
    label=("Your Own Sea", "自分の海"),
    h1_emoji="🌊",
    alt="A chubby crocheted amigurumi penguin wearing real swimming goggles, ready to jump into clear blue water",
    section="一番大事なのは「戦わない」こと",
    message="勝てない戦いをやめると、自分でルールを作れる場所や、自分が勝てる場所が見つかる。",
    tone="素材の重さ：真面目（生き方の考え方）\n→ 見せ方：ポップに（砂の黄色と海の青。チーターとのかけっこで遊べる）",
    game_ja="🏁 陸のかけっこ／海の競泳：「🏃 走る！」を連打してペンギンを進めるが、チーターは勝手にビューンとゴールしてしまい、何度やっても負ける（負けた回数が増える）。1回負けると「🌊 このレースをやめて、海へ」ボタンが出る。海に切りかえると、同じ連打でペンギンはぐんぐん進み、チーターは水が苦手でゆっくり。「🥇 海の中なら、あなたがチャンピオン！」",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of crocheted amigurumi yarn "
            "with visible stitches, wearing realistic blue swimming goggles pushed up on its head, standing at the edge of a calm swimming "
            "pool and smiling, ready to dive. Bright simple sunny yellow and clear sea-blue background with soft depth. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × あみぐるみ × 水泳ゴーグル",
    mood=["lift", "energy"], tags=["psychology", "mindset", "happiness"],
    pal=dict(bg="#f2f9ff", muted="#5d7489", acc="#1b7fd6", acc2="#ffb52e", shadow="rgba(30,90,160,.16)",
             r1="rgba(255,200,80,.30)", r2="rgba(40,150,240,.20)", r3="rgba(80,220,230,.18)",
             h1="#132f4c", photo="#e1f0ff", big="#1668b3", bigdark="#9ccfff",
             game="linear-gradient(150deg, #f6b73c 0%, #f08a3a 40%, #1b8fe0 100%)"),
    cards=[
        dict(emoji="🏳️", label=("Stop Fighting", "戦いをやめる"),
             s=[("When you stop a fight you cannot win, you begin to see new places.",
                 "勝てない戦いをやめると、新しい場所が見えてきます。")]),
        dict(emoji="📏", label=("Your Rules", "自分のルール"),
             s=[("They are places where you can make the rules, or places where you can win.",
                 "自分でルールを作れる場所や、自分が勝てる場所です。")]),
        dict(emoji="🐆", label=("On Land", "陸の上"),
             s=[("On land, a penguin cannot beat a cheetah.",
                 "ペンギンは、陸の上ではチーターに勝てません。"),
                ("But in the sea, a penguin swims surprisingly fast.",
                 "でも、海の中なら、びっくりするほど速く泳ぎます。")]),
        dict(emoji="🌊", label=("More Fun", "もっと面白く"), big=True,
             s=[("The more you avoid head-on fights, the more fun life becomes.",
                 "真正面からの勝負をさけるほど、人生は面白くなります。")]),
    ],
    game_after=3,
    game_note="陸のかけっこ／海の競泳（勝てない場所から、勝てる場所へ）",
    game_html="""  <section class="game" data-f="land" data-s="ready" data-lost="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Race the cheetah</div>
    <div class="game-hint">Tap "Run!" as fast as you can. Can the penguin win?</div>
    <div class="field" aria-hidden="true">
      <div class="lane l1"><span class="run rc"><span class="run-e">🐆</span></span><span class="goal">🏁</span></div>
      <div class="lane l2"><span class="run rp"><span class="run-e">🐧</span></span><span class="goal">🏁</span></div>
    </div>
    <div class="where"><span class="w-land">🏜️ Field: land</span><span class="w-sea">🌊 Field: the sea</span></div>
    <button type="button" class="btn go"><span class="g-land">🏃 Run!</span><span class="g-sea">🏊 Swim!</span></button>
    <div class="msg">
      <div class="m-ready">The race starts when you tap.</div>
      <div class="m-race">Go, go, go!</div>
      <div class="m-lose">The cheetah wins again. 💨</div>
      <div class="m-win">🥇 In the sea, you are the champion!</div>
    </div>
    <div class="lost"><span class="lost-l">😵 Races lost on land:</span> <span class="ln">0</span></div>
    <div class="ctrl">
      <button type="button" class="btn ghost b-again">↺ Race again</button>
      <button type="button" class="btn b-sea">🌊 Leave this race, go to the sea</button>
      <button type="button" class="btn ghost b-land">🏜️ Back to land</button>
    </div>
  </section>""",
    css="""
  /* 🏁 陸のかけっこ／海の競泳 */
  .field { max-width: 380px; margin: 16px auto 0; padding: 10px; border-radius: 22px; background: #f7dd9a; transition: background .4s ease; }
  .game[data-f="sea"] .field { background: linear-gradient(180deg, #7fd3ff, #2a8fe0); }
  .lane { position: relative; height: 58px; margin: 4px 0; border-radius: 14px; background: rgba(255,255,255,.4); }
  .run { position: absolute; top: 50%; left: 0; transform: translateY(-50%); font-size: 38px; line-height: 1; transition: left .12s linear; }
  .rc .run-e { display: inline-block; transform: scaleX(-1); }
  .goal { position: absolute; right: 4px; top: 50%; transform: translateY(-50%); font-size: 26px; line-height: 1; }
  .where { margin-top: 10px; font-size: 15px; font-weight: 900; }
  .w-sea, .game[data-f="sea"] .w-land { display: none; }
  .game[data-f="sea"] .w-sea { display: inline; }
  .go { display: flex; width: min(320px, 100%); min-height: 96px; margin: 12px auto 0; font-size: clamp(26px, 7vw, 34px); background: #fff; color: #7a3d00;
    box-shadow: 0 9px 0 rgba(0,0,0,.2); }
  .go:active { transform: translateY(7px); box-shadow: 0 2px 0 rgba(0,0,0,.2); }
  .game[data-f="sea"] .go { color: #0d4f8a; }
  .g-sea, .game[data-f="sea"] .g-land { display: none; }
  .game[data-f="sea"] .g-sea { display: inline; }
  .msg { margin-top: 12px; min-height: 48px; font-size: 17px; font-weight: 900; line-height: 1.4; }
  .msg > div { display: none; }
  .game[data-s="ready"] .m-ready, .game[data-s="race"] .m-race, .game[data-s="lose"] .m-lose, .game[data-s="win"] .m-win { display: block; animation: boing .45s ease; }
  .lost { font-size: 15px; font-weight: 900; }
  .ln { display: inline-block; min-width: 1.4em; padding: 2px 8px; border-radius: 999px; background: rgba(255,255,255,.3); }
  .ctrl { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-top: 12px; }
  .ctrl .btn { display: none; }
  .game[data-s="lose"] .b-again, .game[data-s="win"] .b-again { display: inline-flex; }
  .game[data-f="land"][data-lost="1"]:not([data-s="race"]) .b-sea { display: inline-flex; background: #ffe066; color: #4a3500; animation: boing .6s ease; }
  .game[data-f="sea"][data-s="win"] .b-land { display: inline-flex; }
  .game[data-s="win"] .rp .run-e { display: inline-block; animation: boing .6s ease 2; }
""",
    dark="""  html[data-theme="dark"] .field { background: #5a4a26; }
  html[data-theme="dark"] .game[data-f="sea"] .field { background: linear-gradient(180deg, #1e5a82, #123c5e); }
  html[data-theme="dark"] .game .go { background: #2b2d3a; color: #ffe0b8; }
  html[data-theme="dark"] .game[data-f="sea"] .go { color: #b8e2ff; }
  html[data-theme="dark"] .game .b-sea { background: #4a3c12; color: #ffe39a; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var rc = g.querySelector('.rc'), rp = g.querySelector('.rp'), ln = g.querySelector('.ln');
  var c = 0, p = 0, lost = 0, raf = 0, last = 0, END = 84;
  function pop(el, list) {
    if (!window.pengessoPop) return;
    var r = el.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, 18);
  }
  function draw() { rc.style.left = c + '%'; rp.style.left = p + '%'; }
  function reset() { cancelAnimationFrame(raf); c = 0; p = 0; draw(); g.setAttribute('data-s', 'ready'); }
  function tick(t) {
    var dt = last ? Math.min(60, t - last) : 16; last = t;
    var sea = g.getAttribute('data-f') === 'sea';
    c += dt * (sea ? 0.006 : 0.045);          /* 陸のチーターは約2秒でゴール。海ではとてもゆっくり */
    if (c >= END) { c = END; draw(); finish(false); return; }
    draw();
    raf = requestAnimationFrame(tick);
  }
  function finish(win) {
    cancelAnimationFrame(raf);
    if (win) {
      g.setAttribute('data-s', 'win');
      pop(rp, ['🥇', '🐧', '🌊', '✨', '🐟']);
    } else {
      g.setAttribute('data-s', 'lose');
      if (g.getAttribute('data-f') === 'land') { lost++; ln.textContent = lost; g.setAttribute('data-lost', '1'); }
      if (navigator.vibrate) { try { navigator.vibrate([20, 40, 20]); } catch (e) {} }
    }
  }
  g.querySelector('.go').addEventListener('click', function () {
    var s = g.getAttribute('data-s');
    if (s === 'lose' || s === 'win') return;
    if (s === 'ready') { g.setAttribute('data-s', 'race'); last = 0; raf = requestAnimationFrame(tick); }
    p += g.getAttribute('data-f') === 'sea' ? 12 : 3;
    if (p >= END) { p = END; draw(); finish(true); return; }
    draw();
  });
  g.querySelector('.b-again').addEventListener('click', reset);
  g.querySelector('.b-sea').addEventListener('click', function () { g.setAttribute('data-f', 'sea'); reset(); });
  g.querySelector('.b-land').addEventListener('click', function () { g.setAttribute('data-f', 'land'); reset(); });
})();
""",
    ja={
        "Race the cheetah": "チーターとかけっこ",
        "Tap \"Run!\" as fast as you can. Can the penguin win?": "「走る！」をできるだけ速く連打してね。ペンギンは勝てるかな？",
        "🏜️ Field: land": "🏜️ 場所：陸",
        "🌊 Field: the sea": "🌊 場所：海",
        "🏃 Run!": "🏃 走る！",
        "🏊 Swim!": "🏊 泳ぐ！",
        "The race starts when you tap.": "押したら、レース開始です。",
        "Go, go, go!": "いけ、いけ、いけー！",
        "The cheetah wins again. 💨": "またチーターの勝ち。💨",
        "🥇 In the sea, you are the champion!": "🥇 海の中なら、あなたがチャンピオン！",
        "😵 Races lost on land:": "😵 陸で負けた回数：",
        "↺ Race again": "↺ もう一回",
        "🌊 Leave this race, go to the sea": "🌊 このレースをやめて、海へ",
        "🏜️ Back to land": "🏜️ 陸にもどる",
    },
)
build(d)
