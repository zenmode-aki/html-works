from gen import build

d = dict(
    slug="strategy-means-skipping-the-fight", seq=522,
    title=("Strategy means finding a way to skip the fight",
           "「戦略」は戦いを略すこと。勝ち方より、戦わずに済む方法を考える"),
    label=("Skip the Fight", "戦いを略す"),
    h1_emoji="🗺️",
    alt="A chubby low-poly wood and paper penguin looking at a real folded paper map with two roads to a toy castle",
    section="一番大事なのは「戦わない」こと",
    message="「戦略」は戦いを略すこと。「どう勝つか」より先に「どうすれば戦わずに済むか」を考える。",
    tone="素材の重さ：真面目（生き方の考え方）\n→ 見せ方：ポップに（草原の緑と夕焼けのオレンジ。お城までの2本の道で遊べる）",
    game_ja="🗺️ お城までの2本の道：ペンギンがお城をめざす。「⚔️ まっすぐの道」を選ぶと、道のまん中の大きなカニとバトルになり、HP が 100 → 25 に減ってヘトヘトで到着。「🌿 わき道」を選ぶと、ぐるっと遠回りして HP 100 のまま元気に到着（🎉）。2本とも試すと、下に「まっすぐ：25 HP／わき道：100 HP」の記録が並び、「戦わない道のほうが、元気に着ける」とわかる。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of low-poly 3D wood and paper "
            "with soft faceted shapes, standing on a grassy paper hill and holding open a realistic folded paper road map with both flippers, "
            "looking thoughtful and pleased. Far behind, a small soft-focus toy castle on a green hill. Bright simple fresh green and warm "
            "sunset orange background with gentle depth. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × 低ポリの木と紙 × 紙の道路地図",
    mood=["lift", "think"], tags=["psychology", "mindset", "tips"],
    pal=dict(bg="#f4fbef", muted="#647a5c", acc="#2f9e4f", acc2="#ff8a3d", shadow="rgba(40,110,60,.16)",
             r1="rgba(255,180,90,.30)", r2="rgba(80,200,110,.22)", r3="rgba(255,214,90,.18)",
             h1="#1d4026", photo="#e3f6dc", big="#23803f", bigdark="#9be7ad",
             game="linear-gradient(150deg, #32b35a 0%, #1f9a8a 55%, #ff9a3d 100%)"),
    cards=[
        dict(emoji="✍️", label=("The Word", "言葉の意味"),
             s=[("The Japanese word for \"strategy\" is written \"skip the fight.\"",
                 "「戦略」という言葉は、「戦いを略す」と書きます。")]),
        dict(emoji="🧭", label=("What It Means", "つまり"),
             s=[("So it means thinking of a way to get results with as little fighting as possible.",
                 "つまり、できるだけ戦わずに結果を出す方法を考えることです。")]),
        dict(emoji="🌿", label=("Ask First", "先に考える"), big=True,
             s=[("So before \"How can I win?\", I ask, \"How can I skip the fight?\"",
                 "だから「どう勝つか」より先に、「どうすれば戦わずに済むか」を考えます。")]),
        dict(emoji="☕", label=("Cafe Example", "カフェなら"),
             s=[("For example, at a popular cafe, I go in the quiet morning instead of fighting the long line.",
                 "たとえば人気のカフェなら、長い行列と戦うより、すいている朝に行きます。")]),
    ],
    game_after=2,
    game_note="お城までの2本の道（戦う道と、戦わない道）",
    game_html="""  <section class="game" data-s="idle" data-ta="0" data-tb="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Two roads to the castle</div>
    <div class="game-hint">Pick a road. How much HP is left when you arrive?</div>
    <div class="hp"><span class="hp-l">❤️ HP</span><span class="hp-bar"><i></i></span><span class="hpn">100</span></div>
    <div class="map" aria-hidden="true">
      <div class="road-a"></div>
      <div class="road-b"></div>
      <div class="castle"><span class="castle-e">🏰</span></div>
      <div class="foe"><span class="foe-e">🦀</span></div>
      <div class="clash"><span class="clash-e">⚔️</span></div>
      <div class="walker"><span class="walker-e">🐧</span></div>
    </div>
    <div class="msg">
      <div class="m-idle">The big crab is waiting on the straight road.</div>
      <div class="m-run">Walking… 🐾</div>
      <div class="m-a">You won the fight… but only 25 HP is left. So tired! 😵</div>
      <div class="m-b">You arrived with full HP. No fight at all! 🎉</div>
    </div>
    <div class="picks">
      <button type="button" class="btn pick pa">⚔️ Straight road (fight)</button>
      <button type="button" class="btn pick pb">🌿 Side path (no fight)</button>
    </div>
    <div class="log">
      <div class="lg lg-a"><span class="lg-l">⚔️ Straight road:</span> <span class="lg-n">25</span> <span class="lg-u">HP</span></div>
      <div class="lg lg-b"><span class="lg-l">🌿 Side path:</span> <span class="lg-n">100</span> <span class="lg-u">HP</span></div>
    </div>
    <div class="both">🧭 The road with no fight gets you there with energy left.</div>
  </section>""",
    css="""
  /* 🗺️ お城までの2本の道 */
  .hp { display: flex; align-items: center; gap: 8px; max-width: 320px; margin: 14px auto 0; font-weight: 900; font-size: 15px; }
  .hp-bar { position: relative; flex: 1; height: 16px; border-radius: 999px; background: rgba(255,255,255,.3); overflow: hidden; }
  .hp-bar i { position: absolute; inset: 0 auto 0 0; width: 100%; border-radius: 999px; background: #ff5f7e; transition: width .35s ease; }
  .hpn { min-width: 2.4em; text-align: right; font-size: 18px; }
  .map { position: relative; max-width: 320px; height: 270px; margin: 12px auto 0; border-radius: 26px; overflow: hidden;
    background: radial-gradient(circle at 30% 30%, #d8f8c8, #9fe08e 70%); box-shadow: inset 0 0 0 4px rgba(255,255,255,.5); }
  .road-a { position: absolute; left: 50%; top: 24%; bottom: 12%; width: 30px; transform: translateX(-50%); border-radius: 16px; background: #f3d79d; }
  .road-b { position: absolute; left: 50%; right: 9%; top: 23%; bottom: 9%; border: 14px solid #f3d79d; border-left: 0; border-radius: 0 70px 70px 0; }
  .castle { position: absolute; left: 50%; top: 1%; transform: translateX(-50%); font-size: 44px; line-height: 1; }
  .foe { position: absolute; left: 50%; top: 54%; transform: translate(-50%, -50%); font-size: 40px; line-height: 1; transition: transform .3s ease, opacity .4s ease; }
  .clash { position: absolute; left: 50%; top: 46%; transform: translate(-50%, -50%) scale(0); font-size: 46px; line-height: 1; opacity: 0; }
  .walker { position: absolute; left: 50%; top: 86%; transform: translate(-50%, -50%); font-size: 40px; line-height: 1; z-index: 2; }
  .game[data-s="a-run"] .walker { animation: walkA 2.6s ease-in-out both; }
  .game[data-s="b-run"] .walker { animation: walkB 2.6s ease-in-out both; }
  .game[data-s="a-run"] .clash { animation: clash 2.6s ease both; }
  .game[data-s="a-run"] .foe { animation: foeHit 2.6s ease both; }
  .game[data-s="a-done"] .walker, .game[data-s="b-done"] .walker { top: 28%; }
  .game[data-s="a-done"] .foe { opacity: .35; transform: translate(-50%, -50%) rotate(180deg) scale(.8); }
  .game[data-s="a-done"] .walker-e { filter: saturate(.4); }
  .game[data-s="b-done"] .walker-e { display: inline-block; animation: boing .6s ease 2; }
  @keyframes walkA { 0% { top: 86%; } 30% { top: 66%; } 34% { top: 66%; left: 47%; } 40% { left: 53%; } 46% { left: 47%; } 52% { left: 53%; } 58% { left: 50%; top: 66%; } 100% { top: 28%; left: 50%; } }
  @keyframes walkB { 0% { left: 50%; top: 86%; } 25% { left: 85%; top: 86%; } 75% { left: 85%; top: 28%; } 100% { left: 50%; top: 28%; } }
  @keyframes clash { 0%, 30% { opacity: 0; transform: translate(-50%, -50%) scale(0); } 38%, 54% { opacity: 1; transform: translate(-50%, -50%) scale(1.2) rotate(12deg); } 62%, 100% { opacity: 0; transform: translate(-50%, -50%) scale(0); } }
  @keyframes foeHit { 0%, 56% { opacity: 1; } 70%, 100% { opacity: .35; transform: translate(-50%, -50%) rotate(180deg) scale(.8); } }
  .msg { margin-top: 12px; min-height: 50px; font-size: 16.5px; font-weight: 900; line-height: 1.4; }
  .msg > div { display: none; }
  .game[data-s="idle"] .m-idle, .game[data-s$="run"] .m-run, .game[data-s="a-done"] .m-a, .game[data-s="b-done"] .m-b { display: block; animation: boing .45s ease; }
  .picks { display: grid; gap: 10px; max-width: 360px; margin: 10px auto 0; }
  .pa { background: #ffe3e3; color: #7a1f2a; }
  .pb { background: #fff5c7; color: #5a4200; }
  .log { display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; margin-top: 14px; }
  .lg { display: none; padding: 8px 14px; border-radius: 999px; background: rgba(255,255,255,.25); font-size: 14.5px; font-weight: 900; }
  .game[data-ta="1"] .lg-a, .game[data-tb="1"] .lg-b { display: block; }
  .both { display: none; margin: 12px auto 0; max-width: 380px; padding: 12px 14px; border-radius: 18px; background: #fff; color: #1d4026; font-weight: 900; font-size: 15.5px; line-height: 1.45; }
  .game[data-ta="1"][data-tb="1"] .both { display: block; animation: boing .5s ease; }
""",
    dark="""  html[data-theme="dark"] .map { background: radial-gradient(circle at 30% 30%, #3c6a3a, #22432a 70%); }
  html[data-theme="dark"] .road-a { background: #8a7444; }
  html[data-theme="dark"] .road-b { border-color: #8a7444; }
  html[data-theme="dark"] .game .pa { background: #4a2228; color: #ffd0d6; }
  html[data-theme="dark"] .game .pb { background: #4a3c12; color: #ffe39a; }
  html[data-theme="dark"] .both { background: #22242f; color: #d8f5dd; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var bar = g.querySelector('.hp-bar i'), hpn = g.querySelector('.hpn'), picks = g.querySelectorAll('.pick'), timers = [];
  function hp(v) { bar.style.width = v + '%'; hpn.textContent = v; }
  function lock(on) { [].forEach.call(picks, function (b) { b.disabled = on; }); }
  function later(fn, ms) { timers.push(setTimeout(fn, ms)); }
  function pop(el, list) {
    if (!window.pengessoPop) return;
    var r = el.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, 16);
  }
  function go(road) {
    timers.forEach(clearTimeout); timers = [];
    hp(100); lock(true);
    g.setAttribute('data-s', 'idle'); void g.offsetWidth;
    g.setAttribute('data-s', road + '-run');
    if (road === 'a') {
      later(function () { hp(70); if (navigator.vibrate) { try { navigator.vibrate(25); } catch (e) {} } }, 1000);
      later(function () { hp(45); }, 1250);
      later(function () { hp(25); }, 1450);
    }
    later(function () {
      g.setAttribute('data-s', road + '-done');
      g.setAttribute(road === 'a' ? 'data-ta' : 'data-tb', '1');
      lock(false);
      if (road === 'b') pop(g.querySelector('.castle'), ['🎉', '🐧', '🏰', '✨']);
      else pop(g.querySelector('.foe'), ['💦', '⚔️']);
    }, 2650);
  }
  g.querySelector('.pa').addEventListener('click', function () { go('a'); });
  g.querySelector('.pb').addEventListener('click', function () { go('b'); });
})();
""",
    ja={
        "Two roads to the castle": "お城までの2本の道",
        "Pick a road. How much HP is left when you arrive?": "道を選んでね。お城に着いたとき、HP はいくつ残っている？",
        "❤️ HP": "❤️ HP",
        "The big crab is waiting on the straight road.": "まっすぐの道には、大きなカニが待ちかまえています。",
        "Walking… 🐾": "てくてく… 🐾",
        "You won the fight… but only 25 HP is left. So tired! 😵": "戦いには勝った…けど、残りの HP は25。ヘトヘト！😵",
        "You arrived with full HP. No fight at all! 🎉": "HP 満タンで到着。戦いはゼロ！🎉",
        "⚔️ Straight road (fight)": "⚔️ まっすぐの道（戦う）",
        "🌿 Side path (no fight)": "🌿 わき道（戦わない）",
        "⚔️ Straight road:": "⚔️ まっすぐの道：",
        "🌿 Side path:": "🌿 わき道：",
        "HP": "HP",
        "🧭 The road with no fight gets you there with energy left.": "🧭 戦わない道のほうが、元気なまま着けます。",
    },
)
build(d)
