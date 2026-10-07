from gen import build

d = dict(
    slug="measure-by-doing-what-you-believed", seq=513,
    title=("Measure success by whether you did what you believed, not by the result",
           "成功の物差しを「信じたことをやり抜いたか」にすると、失敗が怖くなくなる"),
    label=("New Ruler", "新しい物差し"),
    h1_emoji="📏",
    alt="A chubby plush corduroy and felt penguin holding a real wooden ruler up high with a proud, calm smile",
    section="幸せは「自立」から",
    message="成功の物差しを「信じたことをやり抜いたか」に変えると、失敗が怖くなくなる。",
    tone="素材の重さ：真面目（生き方の考え方）\n→ 見せ方：ポップに（むらさきと黄緑。2本の物差しで同じ3日を測りくらべる）",
    game_ja="📏 2本の物差し：3つの日（バドミントンの試合に負けた／ケーキがふくらまなかった／英語のテストに合格した）を押して測る。「結果の物差し」だと2つが❌、合格の日も「次はどうしよう😰」で、怖さメーターが上がってゆれる。「やり抜いた？の物差し」に持ちかえると、同じ3日が全部✅になって、メーターが下がる。両方の物差しで3日とも測ると、まとめの一言が出る。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of plush toy corduroy and felt, "
            "proudly holding a realistic long wooden ruler up with both flippers like a trophy, calm happy smile. "
            "Bright simple lavender and lime green background with soft depth, a blurred soft floor. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × コーデュロイとフェルトのぬいぐるみ × 木の物差し",
    mood=["lift", "think"], tags=["psychology", "mindset", "mistakes"],
    pal=dict(bg="#f8f6ff", muted="#77709a", acc="#6f3cf0", acc2="#22c066", shadow="rgba(90,60,170,.16)",
             r1="rgba(160,240,90,.30)", r2="rgba(111,60,240,.18)", r3="rgba(34,192,102,.14)",
             h1="#2b1f5c", photo="#ece6ff", big="#5a2fd6", bigdark="#c2adff",
             game="linear-gradient(150deg, #6f3cf0 0%, #9b5cff 50%, #22c066 100%)"),
    cards=[
        dict(emoji="😰", label=("Old Ruler", "古い物差し"),
             s=[("If you measure success only by the result, you always worry, \"What if I fail?\"",
                 "人生の成功を結果だけで測ると、いつも「失敗したらどうしよう」とドキドキします。")]),
        dict(emoji="📏", label=("New Ruler", "新しい物差し"),
             s=[("So I change the ruler to \"Did I do what I believed in until the end?\"",
                 "そこで、物差しを「信じたことを、最後までやり抜いたか」に変えてみます。")]),
        dict(emoji="✅", label=("Always Pass", "いつでも合格"), big=True,
             s=[("With this ruler, a day I did it all is a pass, whatever the result.",
                 "この物差しなら、結果がどうでも、やり切った日は合格です。")]),
        dict(emoji="🤝", label=("Not Careless", "投げやりではない"),
             s=[("It does not mean the result does not matter.",
                 "結果がどうでもいい、という意味ではありません。"),
                ("I just accept that I cannot decide the final result.",
                 "最後の結果は自分では決められない、と覚悟するだけです。")]),
    ],
    game_after=2,
    game_note="2本の物差し（同じ3日を、ちがう物差しで測る）",
    game_html="""  <section class="game" data-ru="r" data-m1="0" data-m2="0" data-m3="0" data-end="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Same 3 days, 2 rulers</div>
    <div class="game-hint">Tap each day to measure it. Then switch the ruler.</div>
    <div class="rulers">
      <button type="button" class="btn ru ru-r" data-ru="r">📏 Result ruler</button>
      <button type="button" class="btn ru ru-d" data-ru="d">✅ "Did I do it all?" ruler</button>
    </div>
    <div class="tape" aria-hidden="true"></div>
    <div class="days">
      <button type="button" class="btn day" data-n="1">
        <span class="d-ev">🏸 I lost the badminton match.</span>
        <span class="d-q">Tap to measure</span>
        <span class="d-v v-r v-bad">❌ Fail</span>
        <span class="d-v v-d">✅ I practiced every day. Pass!</span>
      </button>
      <button type="button" class="btn day" data-n="2">
        <span class="d-ev">🎂 My cake came out flat.</span>
        <span class="d-q">Tap to measure</span>
        <span class="d-v v-r v-bad">❌ Fail</span>
        <span class="d-v v-d">✅ I tried a new recipe. Pass!</span>
      </button>
      <button type="button" class="btn day" data-n="3">
        <span class="d-ev">📝 I passed the English test.</span>
        <span class="d-q">Tap to measure</span>
        <span class="d-v v-r">⭕ Pass… but what about next time? 😰</span>
        <span class="d-v v-d">✅ I studied to the end. Pass!</span>
      </button>
    </div>
    <div class="fear">
      <div class="fear-head"><span class="fear-l">😱 Fear meter</span> <span class="fear-e"><span class="fe fe-r">😰</span><span class="fe fe-d">😌</span></span></div>
      <div class="fear-bar" aria-hidden="true"><i></i></div>
      <div class="pass"><span class="pass-l">Pass:</span> <span class="pn">0</span> <span class="pass-of">/ 3</span></div>
    </div>
    <div class="end">🐧 Same 3 days. With the new ruler, there is nothing to be afraid of.</div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Start over</button></div>
  </section>""",
    css="""
  /* 📏 2本の物差し */
  .rulers { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 460px; margin: 16px auto 0; }
  .ru { min-height: 60px; padding: 8px 10px; border-radius: 18px; font-size: 14.5px; background: rgba(255,255,255,.22); color: #fff;
    box-shadow: inset 0 0 0 2px rgba(255,255,255,.6); }
  .game[data-ru="r"] .ru-r { background: #fff; color: #4b2aa8; box-shadow: 0 6px 0 rgba(0,0,0,.2); }
  .game[data-ru="d"] .ru-d { background: #d8ff6b; color: #244a00; box-shadow: 0 6px 0 rgba(0,0,0,.2); }
  /* 物差しの目もり（線だけ） */
  .tape { height: 20px; max-width: 460px; margin: 14px auto 6px; border-radius: 6px; transition: background-color .3s ease;
    background-color: #ffe27a;
    background-image: repeating-linear-gradient(90deg, rgba(60,40,0,.55) 0 2px, transparent 2px 23px),
      repeating-linear-gradient(90deg, rgba(60,40,0,.35) 0 1px, transparent 1px 11.5px);
    background-size: 100% 100%, 100% 55%; background-repeat: no-repeat; }
  .game[data-ru="d"] .tape { background-color: #c9ff63; }
  .days { display: grid; gap: 10px; max-width: 460px; margin: 10px auto 0; }
  .day { display: grid; gap: 4px; justify-items: start; text-align: left; width: 100%; min-height: 70px; padding: 12px 16px; border-radius: 20px; }
  .d-ev { font-size: 16px; }
  .d-q { font-size: 13px; color: #7b6fa8; }
  .d-v { display: none; font-size: 15.5px; padding: 4px 10px; border-radius: 12px; }
  .v-r { background: #ffe6ea; color: #a1123a; }
  .v-r:not(.v-bad) { background: #fff3cf; color: #6e4b00; }
  .v-d { background: #e3ffd1; color: #1d5a00; }
  .game[data-m1="1"] .day[data-n="1"] .d-q, .game[data-m2="1"] .day[data-n="2"] .d-q, .game[data-m3="1"] .day[data-n="3"] .d-q { display: none; }
  .game[data-ru="r"][data-m1="1"] .day[data-n="1"] .v-r, .game[data-ru="d"][data-m1="1"] .day[data-n="1"] .v-d,
  .game[data-ru="r"][data-m2="1"] .day[data-n="2"] .v-r, .game[data-ru="d"][data-m2="1"] .day[data-n="2"] .v-d,
  .game[data-ru="r"][data-m3="1"] .day[data-n="3"] .v-r, .game[data-ru="d"][data-m3="1"] .day[data-n="3"] .v-d { display: inline-block; animation: boing .45s ease; }
  .day.flip { animation: flipy .45s ease; }
  @keyframes flipy { 0% { transform: rotateX(0); } 50% { transform: rotateX(80deg); } 100% { transform: rotateX(0); } }

  .fear { max-width: 460px; margin: 16px auto 0; padding: 12px 14px; border-radius: 20px; background: rgba(255,255,255,.18); }
  .fear-head { display: flex; justify-content: space-between; align-items: center; font-size: 15px; font-weight: 900; }
  .fe { font-size: 26px; transition: opacity .25s ease; }
  .fe-d { position: absolute; opacity: 0; }
  .fear-e { position: relative; display: inline-block; width: 30px; height: 30px; }
  .fe { position: absolute; left: 0; top: 0; }
  .game[data-ru="d"] .fe-r { opacity: 0; } .game[data-ru="d"] .fe-d { opacity: 1; }
  .fear-bar { position: relative; height: 16px; margin-top: 8px; border-radius: 999px; background: rgba(255,255,255,.3); overflow: hidden; }
  .fear-bar i { position: absolute; inset: 0 auto 0 0; width: 0; border-radius: 999px; background: #ff5d7a; transition: width .5s cubic-bezier(.2,1.2,.4,1), background-color .3s ease; }
  .game[data-ru="d"] .fear-bar i { background: #d8ff6b; }
  .fear.shaky { animation: shake .45s ease; }
  .pass { margin-top: 8px; font-size: 16px; font-weight: 900; }
  .pn { display: inline-block; min-width: 1.4em; padding: 1px 8px; border-radius: 999px; background: rgba(255,255,255,.28); }
  .end { display: none; margin: 14px auto 0; max-width: 440px; padding: 12px 14px; border-radius: 18px; background: #fff; color: #3a2a7a; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .game[data-end="1"] .end { display: block; animation: boing .5s ease; }
  .ctrl { margin-top: 12px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
""",
    dark="""  html[data-theme="dark"] .game[data-ru="r"] .ru-r { background: #2b2d3a; color: #e4dcff; }
  html[data-theme="dark"] .game[data-ru="d"] .ru-d { background: #3d5a12; color: #eaffc2; }
  html[data-theme="dark"] .d-q { color: #b9b0de; }
  html[data-theme="dark"] .v-r { background: #4a1c2a; color: #ffc2cf; }
  html[data-theme="dark"] .v-r:not(.v-bad) { background: #4a3c12; color: #ffe39a; }
  html[data-theme="dark"] .v-d { background: #234015; color: #d4ffb8; }
  html[data-theme="dark"] .end { background: #2b2d3a; color: #e4dcff; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var seen = { r: false, d: false };
  var bar = g.querySelector('.fear-bar i'), fear = g.querySelector('.fear');
  var PASS_R = { 1: 0, 2: 0, 3: 1 };
  function m(n) { return g.getAttribute('data-m' + n) === '1'; }
  function update(shake) {
    var ru = g.getAttribute('data-ru'), cnt = 0, pass = 0;
    for (var n = 1; n <= 3; n++) if (m(n)) { cnt++; pass += ru === 'd' ? 1 : PASS_R[n]; }
    g.querySelector('.pn').textContent = pass;
    bar.style.width = (ru === 'r' ? cnt * 30 : cnt * 3) + '%';
    if (cnt === 3) seen[ru] = true;
    if (shake && ru === 'r' && cnt) { fear.classList.remove('shaky'); void fear.offsetWidth; fear.classList.add('shaky'); }
    if (seen.r && seen.d && g.getAttribute('data-end') !== '1') {
      g.setAttribute('data-end', '1');
      if (window.pengessoPop) { var r = g.querySelector('.end').getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top, ['✅', '🐧', '📏', '✨'], 16); }
    }
  }
  [].forEach.call(g.querySelectorAll('.day'), function (b) {
    b.addEventListener('click', function () {
      var n = b.getAttribute('data-n');
      g.setAttribute('data-m' + n, '1');
      b.classList.remove('flip'); void b.offsetWidth; b.classList.add('flip');
      update(true);
      if (g.getAttribute('data-ru') === 'd' && window.pengessoPop) { var r = b.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['✅', '✨'], 8); }
    });
  });
  [].forEach.call(g.querySelectorAll('.ru'), function (b) {
    b.addEventListener('click', function () {
      g.setAttribute('data-ru', b.getAttribute('data-ru'));
      [].forEach.call(g.querySelectorAll('.day'), function (d) { if (m(d.getAttribute('data-n'))) { d.classList.remove('flip'); void d.offsetWidth; d.classList.add('flip'); } });
      update(true);
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    seen = { r: false, d: false };
    g.setAttribute('data-ru', 'r'); g.setAttribute('data-end', '0');
    for (var n = 1; n <= 3; n++) g.setAttribute('data-m' + n, '0');
    update(false);
  });
})();
""",
    ja={
        "Same 3 days, 2 rulers": "同じ3日を、2本の物差しで",
        "Tap each day to measure it. Then switch the ruler.": "1日ずつ押して測ってみてね。そのあと物差しを持ちかえてみて。",
        "📏 Result ruler": "📏 結果の物差し",
        "✅ \"Did I do it all?\" ruler": "✅「やり抜いた？」の物差し",
        "🏸 I lost the badminton match.": "🏸 バドミントンの試合に負けた。",
        "🎂 My cake came out flat.": "🎂 ケーキがふくらまなかった。",
        "📝 I passed the English test.": "📝 英語のテストに合格した。",
        "Tap to measure": "押して測る",
        "❌ Fail": "❌ 失敗",
        "✅ I practiced every day. Pass!": "✅ 毎日練習した。合格！",
        "✅ I tried a new recipe. Pass!": "✅ 新しいレシピに挑戦した。合格！",
        "⭕ Pass… but what about next time? 😰": "⭕ 合格…でも次はどうしよう？😰",
        "✅ I studied to the end. Pass!": "✅ 最後まで勉強した。合格！",
        "😱 Fear meter": "😱 怖さメーター",
        "Pass:": "合格：",
        "/ 3": "/ 3",
        "🐧 Same 3 days. With the new ruler, there is nothing to be afraid of.": "🐧 同じ3日なのに、新しい物差しなら、怖いものがありません。",
        "↺ Start over": "↺ 最初から",
    },
)
build(d)
