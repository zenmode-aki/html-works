from gen import build

d = dict(
    slug="notice-what-can-be-automated", seq=541,
    title=("Noticing \"a machine could do this\" is a real strength",
           "「これ、機械にできるかも」と気づけるのは強い"),
    label=("Spot It", "気づく力"),
    h1_emoji="🤖",
    alt="A chubby chenille yarn penguin smiling beside a real small tin wind-up toy robot",
    section="仕事との向き合い方（一般論）の「テクノロジー」",
    message="くり返しの作業を見て「これ、機械にできるかも」と気づけるだけで強み。小さくても、ゼロから自分で作った経験は強い。",
    tone="素材の重さ：ふつう（テクノロジーとのつきあい方。本人の仕事の話にはしない。例は旅行の写真や家計簿）\n→ 見せ方：ポップに（ミントとオレンジ。毎日のこまごました作業を「🤖 機械」と「🐧 自分」に分けると、ういた時間がたまっていく）",
    game_ja="🤖 機械？自分？：毎日のこまごました作業のカードが1まいずつ出てくる（旅行の写真50枚の名前を変える／レシート40枚を足し算／友達の誕生日プレゼントを選ぶ／毎朝同じ時間に部屋の電気をつける／スープの味見をして塩を足す／12か月ぶんのカレンダーに同じ予定を書く）。「🤖 機械におまかせ」か「🐧 自分でやる」を押して分ける。機械のほうに正しく入れると、ロボットのペンギンが一瞬で片づけて「ういた時間」が増える。まちがえるとカードがぷるっとふるえて、もう一度。最後に「ういた時間で、🐧のことをゆっくりできる」。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of fluffy chenille yarn, "
            "smiling and pointing a flipper at a realistic small vintage tin wind-up toy robot standing beside it. "
            "Bright simple mint green and warm orange background with soft depth and cheerful light. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × シェニール糸 × ブリキのおもちゃのロボット",
    mood=["lift", "learn"], tags=["psychology", "productivity", "tips"],
    pal=dict(bg="#f2fdf8", muted="#5d7a6c", acc="#14a06a", acc2="#ff8a2a", shadow="rgba(20,140,100,.15)",
             r1="rgba(60,220,160,.26)", r2="rgba(255,138,42,.16)", r3="rgba(100,170,255,.14)",
             h1="#0e3a28", photo="#d9f6ea", big="#0f8558", bigdark="#8ff0c4",
             game="linear-gradient(160deg, #1fbf86 0%, #2a9fd6 55%, #ff8a2a 120%)"),
    cards=[
        dict(emoji="🔁", label=("Spot Repeats", "くり返しに気づく"),
             s=[("It is said that just noticing \"a machine could do this\" when you see a repeated task is a real strength.",
                 "くり返しの作業を見て「これ、機械にできるかも」と気づけるだけで、立派な強みになるそうです。")]),
        dict(emoji="📸", label=("For Example", "たとえば"),
             s=[("For example, the task of renaming 50 travel photos 1 by 1.",
                 "たとえば、旅行の写真50枚の名前を、1枚ずつ変える作業です。")]),
        dict(emoji="🛠️", label=("Make It", "作ってみる"),
             s=[("It is said that the experience of making something yourself from zero is strong, even if it is small.",
                 "小さなものでも、ゼロから自分で作った経験は強いそうです。")]),
        dict(emoji="👀", label=("First Step", "最初の一歩"), big=True,
             s=[("First, start by noticing, \"This is the same every time.\"",
                 "まずは「これ、毎回同じだな」と気づくところから。")]),
    ],
    game_after=2,
    game_note="機械？自分？（くり返しの作業を機械に分けると、ういた時間がたまる）",
    game_html="""  <section class="game" data-q="0" data-fb="" data-end="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Machine or me?</div>
    <div class="game-hint">Sort each task. Give the boring repeats to the robot.</div>
    <div class="taskbox">
      <div class="qn"><span class="qi">1</span><span class="qof">/ 6</span></div>
      <div class="tasks">
        <span class="tk t1">📸 Rename 50 travel photos</span>
        <span class="tk t2">🧾 Add up 40 receipts</span>
        <span class="tk t3">🎁 Choose a birthday gift for a friend</span>
        <span class="tk t4">💡 Turn on the room light at the same time every morning</span>
        <span class="tk t5">🍲 Taste the soup and add a little salt</span>
        <span class="tk t6">📅 Write the same plan in 12 months of a calendar</span>
        <span class="tk t7">✨ All sorted!</span>
      </div>
      <div class="bot"><span class="bot-e">🤖</span><span class="bot-z">⚡</span></div>
    </div>
    <div class="bins">
      <button type="button" class="btn bin b-bot" data-a="m">🤖 Give it to a machine</button>
      <button type="button" class="btn bin b-me" data-a="p">🐧 I will do it myself</button>
    </div>
    <div class="fb">
      <div class="fb-m">🤖 Zip! Done in 1 second.</div>
      <div class="fb-p">🐧 Yes. This one needs your heart.</div>
      <div class="fb-x">🤔 Hmm, look again. Is it the same thing again and again?</div>
    </div>
    <div class="saved"><span class="sv-l">⏱ Time saved:</span> <span class="sv-n">0</span> <span class="sv-u">min</span></div>
    <div class="end">🐧 With the time you saved, you can slowly enjoy the 🐧 things.</div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Play again</button></div>
  </section>""",
    css="""
  /* 🤖 機械？自分？ */
  .taskbox { position: relative; max-width: 440px; margin: 14px auto 0; padding: 12px 12px 14px; border-radius: 24px; background: rgba(255,255,255,.2); }
  .qn { font-size: 13.5px; font-weight: 900; opacity: .9; }
  .qof { margin-left: 4px; }
  .tasks { display: flex; align-items: center; justify-content: center; min-height: 96px; margin-top: 8px; padding: 12px 14px; border-radius: 18px;
    background: #fff; color: #0e3a28; font-size: 17.5px; font-weight: 900; line-height: 1.4; }
  .tk { display: none; }
  .game[data-q="0"] .t1, .game[data-q="1"] .t2, .game[data-q="2"] .t3, .game[data-q="3"] .t4, .game[data-q="4"] .t5, .game[data-q="5"] .t6, .game[data-q="6"] .t7 { display: inline; animation: boing .35s ease; }
  .game[data-fb="x"] .tasks { animation: shake .4s ease; }
  .game[data-q="6"] .qn { visibility: hidden; }
  .bot { position: absolute; right: 8px; top: 4px; }
  .game .bot-e { display: inline-block; font-size: 30px; line-height: 1; }
  .game .bot-z { position: absolute; left: -16px; top: 4px; font-size: 18px; opacity: 0; }
  .game[data-fb="m"] .bot-e { animation: zip .5s ease; }
  .game[data-fb="m"] .bot-z { animation: zap .5s ease; }
  @keyframes zip { 0% { transform: none; } 40% { transform: translateX(-160px) rotate(-20deg); } 100% { transform: none; } }
  @keyframes zap { 0%, 100% { opacity: 0; } 40% { opacity: 1; } }
  .bins { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 440px; margin: 14px auto 0; }
  .bin { min-height: 64px; font-size: 15.5px; }
  .b-bot { background: #d9f6ff; color: #0d3d57; }
  .b-me { background: #fff1d6; color: #6a3a00; }
  .game[data-q="6"] .bin { opacity: .4; pointer-events: none; }
  .fb { max-width: 440px; margin: 12px auto 0; min-height: 50px; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .fb > div { display: none; }
  .game[data-fb="m"] .fb-m, .game[data-fb="p"] .fb-p, .game[data-fb="x"] .fb-x { display: block; }
  .saved { display: inline-block; padding: 6px 14px; border-radius: 999px; background: rgba(255,255,255,.22); font-size: 15.5px; font-weight: 900; }
  .sv-n { display: inline-block; min-width: 1.4em; }
  .end { display: none; max-width: 440px; margin: 12px auto 0; padding: 12px 14px; border-radius: 18px; background: #fff; color: #0f8558;
    font-size: 16px; font-weight: 900; line-height: 1.45; }
  .game[data-end="1"] .end { display: block; animation: boing .5s ease; }
  .ctrl { margin-top: 12px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
""",
    dark="""  html[data-theme="dark"] .tasks { background: #22302a; color: #e6fff3; }
  html[data-theme="dark"] .game .b-bot { background: #1f3a4a; color: #cdeeff; }
  html[data-theme="dark"] .game .b-me { background: #4a3a1a; color: #ffe0b0; }
  html[data-theme="dark"] .end { background: #22302a; color: #8ff0c4; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var ANS = ['m', 'm', 'p', 'm', 'p', 'm'], MIN = [40, 30, 0, 5, 0, 20];
  var q = 0, saved = 0, qi = g.querySelector('.qi'), sv = g.querySelector('.sv-n');
  function paint() { g.setAttribute('data-q', String(q)); qi.textContent = String(Math.min(q + 1, 6)); sv.textContent = String(saved); }
  [].forEach.call(g.querySelectorAll('.bin'), function (b) {
    b.addEventListener('click', function () {
      if (q >= 6) return;
      var a = b.getAttribute('data-a');
      g.setAttribute('data-fb', '');
      void g.offsetWidth;   /* 同じ答えが続いても、動きをもう一度 */
      if (a !== ANS[q]) { g.setAttribute('data-fb', 'x'); return; }
      g.setAttribute('data-fb', a);
      saved += MIN[q]; q++; paint();
      if (q === 6) {
        g.setAttribute('data-end', '1');
        if (window.pengessoPop) { var r = g.querySelector('.taskbox').getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🤖', '⏱', '🐧', '✨'], 20); }
      } else if (a === 'm' && window.pengessoPop) {
        var k = b.getBoundingClientRect(); window.pengessoPop(k.left + k.width / 2, k.top + k.height / 2, ['⚡', '🤖'], 6);
      }
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    q = 0; saved = 0; g.setAttribute('data-fb', ''); g.setAttribute('data-end', '0'); paint();
  });
  paint();
})();
""",
    ja={
        "Machine or me?": "機械？自分？",
        "Sort each task. Give the boring repeats to the robot.": "作業を1つずつ分けてね。たいくつなくり返しは、ロボットにおまかせ。",
        "📸 Rename 50 travel photos": "📸 旅行の写真50枚の名前を変える",
        "🧾 Add up 40 receipts": "🧾 レシート40枚を足し算する",
        "🎁 Choose a birthday gift for a friend": "🎁 友達の誕生日プレゼントを選ぶ",
        "💡 Turn on the room light at the same time every morning": "💡 毎朝同じ時間に、部屋の電気をつける",
        "🍲 Taste the soup and add a little salt": "🍲 スープの味見をして、塩を少し足す",
        "📅 Write the same plan in 12 months of a calendar": "📅 12か月ぶんのカレンダーに、同じ予定を書く",
        "✨ All sorted!": "✨ ぜんぶ分けられた！",
        "🤖 Give it to a machine": "🤖 機械におまかせ",
        "🐧 I will do it myself": "🐧 自分でやる",
        "🤖 Zip! Done in 1 second.": "🤖 シュッ！1秒で終わりました。",
        "🐧 Yes. This one needs your heart.": "🐧 そう。これは、あなたの心が必要な作業。",
        "🤔 Hmm, look again. Is it the same thing again and again?": "🤔 うーん、もう一度見てみて。同じことの、くり返しかな？",
        "⏱ Time saved:": "⏱ ういた時間：",
        "min": "分",
        "🐧 With the time you saved, you can slowly enjoy the 🐧 things.": "🐧 ういた時間で、🐧の作業をゆっくり楽しめます。",
        "↺ Play again": "↺ もう一回",
        "/ 6": "/ 6",
    },
)
build(d)
