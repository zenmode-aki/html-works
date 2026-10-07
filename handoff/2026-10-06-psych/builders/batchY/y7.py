from gen import build

d = dict(
    slug="growth-chasing-is-an-endless-sprint", seq=538,
    title=("Chasing only growth turns life into a sprint with no end",
           "成長だけを追いかけると、終わりのない短距離走になる"),
    label=("No Finish", "ゴールがない"),
    h1_emoji="🏁",
    alt="A chubby brushed mohair penguin stepping off a real small treadmill to look at a bright yellow flower",
    section="仕事との向き合い方（一般論）",
    message="成長だけを追いかけると、ゴールのない短距離走になって、大切な人の声も聞こえなくなる。人生の目的は、幸せに生きること。",
    tone="素材の重さ：真面目（生き方の話。本人の仕事の話にはしない）\n→ 見せ方：ポップに（ライムとスカイブルー。ランニングマシンで「もっと速く！」を押すほど、ゴールが遠くなる）",
    game_ja="🏁 終わらない短距離走：ランニングマシンのペンギン。「💨 もっと速く！」を押すとスピードメーターがたまっていくのに、ゴールの旗までの距離はどんどん「のびる」（上には上がいる）。速くなるほど、友達の声のふきだし（ごはん行こう！／見て、にじ！）がうすくなって消える。「🌼 まわりを見る」を押すと止まって、友達の声がはっきり聞こえて、にじが出る。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of soft brushed mohair, "
            "stepping off a realistic small home treadmill with a happy smile to look at a bright yellow flower in a pot beside it. "
            "Bright simple lime green and sky blue background with soft depth and gentle sunshine. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × モヘア × ランニングマシンと黄色い花",
    mood=["lift", "think"], tags=["psychology", "mindset", "happiness"],
    pal=dict(bg="#f6fdf0", muted="#667a5a", acc="#4d9b12", acc2="#2f8fe0", shadow="rgba(80,150,30,.15)",
             r1="rgba(160,230,80,.3)", r2="rgba(47,143,224,.16)", r3="rgba(255,214,90,.2)",
             h1="#20380c", photo="#e6f8d6", big="#3f8410", bigdark="#bdf08c",
             game="linear-gradient(160deg, #6cc72d 0%, #2fb5c9 50%, #3f7fe6 100%)"),
    cards=[
        dict(emoji="👟", label=("Endless Race", "終わらない"),
             s=[("If you chase only growth, it becomes like a sprint with no end.",
                 "成長だけを追いかけていると、終わりのない短距離走みたいになります。")]),
        dict(emoji="🏁", label=("Far Away", "遠いまま"),
             s=[("There is always someone better, so the finish line always stays far away.",
                 "上には上がいるので、ゴールはいつまでも遠いままです。")]),
        dict(emoji="🔇", label=("Lost Voices", "聞こえない"),
             s=[("When you run so hard, you cannot even hear the voices of important people around you.",
                 "走るのに必死だと、まわりの大切な人の声も聞こえなくなります。")]),
        dict(emoji="🌼", label=("The Real Goal", "本当の目的"), big=True,
             s=[("It is said the goal of life is not growth, but living happily.",
                 "人生の目的は、成長ではなく、幸せに生きることだそうです。")]),
    ],
    game_after=3,
    game_note="終わらない短距離走（速くするほどゴールが遠くなり、友達の声が消える）",
    game_html="""  <section class="game" data-sp="0" data-stop="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">The sprint with no end</div>
    <div class="game-hint">Tap "Faster!" again and again. Watch the finish line and your friends.</div>
    <div class="track">
      <div class="voices">
        <span class="vc vc1">🍜 "Let's eat together!"</span>
        <span class="vc vc2">🌈 "Look, a rainbow!"</span>
      </div>
      <div class="belt" aria-hidden="true"></div>
      <div class="runner"><span class="rn-e">🐧</span><span class="rn-s">💦</span></div>
      <div class="flag"><span class="fl-e">🏁</span><span class="fl-d"><span class="dist">100</span><span class="fl-u">m</span></span></div>
      <div class="rainbow" aria-hidden="true"></div>
    </div>
    <div class="speed">
      <div class="sp-head"><span class="sp-l">💨 Speed</span> <span class="sp-n">0</span></div>
      <div class="sp-bar" aria-hidden="true"><i></i></div>
    </div>
    <div class="ctrl2">
      <button type="button" class="btn b-fast">💨 Faster!</button>
      <button type="button" class="btn b-look">🌼 Look around</button>
    </div>
    <div class="res">
      <div class="rs0">Your goal is the flag. How far is it?</div>
      <div class="rs1">🏁 Faster… but the finish line moves farther away!</div>
      <div class="rs2">💦 Full speed! The flag is even farther, and your friends' voices are gone.</div>
      <div class="rs3">🌼 You stopped. Now you can hear your friends again.</div>
    </div>
  </section>""",
    css="""
  /* 🏁 終わらない短距離走 */
  .track { position: relative; height: 210px; max-width: 440px; margin: 14px auto 0; border-radius: 24px; overflow: hidden;
    background: linear-gradient(#d8f2ff 0 70%, #b8e39a 70%); }
  .voices { position: absolute; left: 10px; right: 10px; top: 10px; display: flex; flex-wrap: wrap; gap: 6px; justify-content: flex-start; z-index: 2; }
  .vc { display: inline-block; padding: 5px 10px; border-radius: 14px 14px 14px 4px; background: #fff; color: #2a3a20; font-size: 14px; font-weight: 900;
    line-height: 1.3; transition: opacity .4s ease, filter .4s ease; }
  .game[data-sp="1"] .vc, .game[data-sp="2"] .vc { opacity: .75; }
  .game[data-sp="3"] .vc, .game[data-sp="4"] .vc { opacity: .45; filter: blur(1px); }
  .game[data-sp="5"] .vc, .game[data-sp="6"] .vc { opacity: .15; filter: blur(2px); }
  .game[data-stop="1"] .vc { opacity: 1; filter: none; animation: boing .45s ease; }
  .belt { position: absolute; left: 14px; width: 150px; bottom: 26px; height: 16px; border-radius: 999px;
    background: repeating-linear-gradient(90deg, #3a4a5a 0 14px, #55677a 14px 28px); }
  .game:not([data-sp="0"]):not([data-stop="1"]) .belt { animation: belt .5s linear infinite; }
  .game[data-sp="4"]:not([data-stop="1"]) .belt, .game[data-sp="5"]:not([data-stop="1"]) .belt, .game[data-sp="6"]:not([data-stop="1"]) .belt { animation-duration: .2s; }
  @keyframes belt { to { background-position: -28px 0; } }
  .runner { position: absolute; left: 60px; bottom: 38px; }
  .game .rn-e { display: inline-block; font-size: 52px; line-height: 1; transition: transform .4s ease; }
  .game:not([data-sp="0"]):not([data-stop="1"]) .rn-e { animation: run .3s ease-in-out infinite alternate; }
  @keyframes run { from { transform: translateY(0) rotate(-6deg); } to { transform: translateY(-6px) rotate(6deg); } }
  .game .rn-s { position: absolute; right: -14px; top: -6px; font-size: 20px; opacity: 0; transition: opacity .3s ease; }
  .game[data-sp="4"] .rn-s, .game[data-sp="5"] .rn-s, .game[data-sp="6"] .rn-s { opacity: 1; }
  .game[data-stop="1"] .rn-s { opacity: 0; }
  .flag { position: absolute; right: 12px; bottom: 34px; display: grid; justify-items: center; gap: 2px; transition: transform .5s ease; }
  .game .fl-e { font-size: 34px; line-height: 1; }
  .fl-d { padding: 2px 8px; border-radius: 999px; background: #fff; color: #2a3a20; font-size: 13.5px; font-weight: 900; }
  .fl-u { margin-left: 2px; }
  .game[data-sp="2"] .flag, .game[data-sp="3"] .flag { transform: scale(.85); }
  .game[data-sp="4"] .flag, .game[data-sp="5"] .flag { transform: scale(.7); }
  .game[data-sp="6"] .flag { transform: scale(.55); }
  .rainbow { position: absolute; right: 70px; bottom: 40px; width: 140px; height: 70px; border-radius: 140px 140px 0 0; opacity: 0;
    background: radial-gradient(circle at 50% 100%, transparent 0 44px, #8f6bff 44px 50px, #3fa0ff 50px 56px, #4cd16a 56px 62px, #ffd23f 62px 66px, #ff6b6b 66px 70px, transparent 70px);
    transition: opacity .6s ease; }
  .game[data-stop="1"] .rainbow { opacity: .9; }
  .speed { max-width: 440px; margin: 12px auto 0; padding: 10px 14px; border-radius: 18px; background: rgba(255,255,255,.18); }
  .sp-head { display: flex; justify-content: space-between; font-size: 15px; font-weight: 900; }
  .sp-bar { position: relative; height: 14px; margin-top: 6px; border-radius: 999px; background: rgba(255,255,255,.3); overflow: hidden; }
  .sp-bar i { position: absolute; inset: 0 auto 0 0; width: 0; border-radius: 999px; background: #ffe066; transition: width .3s ease; }
  .ctrl2 { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 440px; margin: 14px auto 0; }
  .b-fast { min-height: 64px; font-size: 18px; background: #fff3c4; color: #5a3d00; }
  .b-look { min-height: 64px; font-size: 16px; }
  .res { max-width: 440px; margin: 12px auto 0; min-height: 50px; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .res > div { display: none; }
  .game[data-sp="0"][data-stop="0"] .rs0 { display: block; }
  .game:not([data-sp="0"]):not([data-sp="6"])[data-stop="0"] .rs1 { display: block; }
  .game[data-sp="6"][data-stop="0"] .rs2 { display: block; animation: shake .45s ease; }
  .game[data-stop="1"] .rs3 { display: block; animation: boing .45s ease; }
""",
    dark="""  html[data-theme="dark"] .track { background: linear-gradient(#24364a 0 70%, #2c4a24 70%); }
  html[data-theme="dark"] .vc, html[data-theme="dark"] .fl-d { background: #22242f; color: #e6f4dc; }
  html[data-theme="dark"] .game .b-fast { background: #4a3c12; color: #ffe39a; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var sp = 0, dist = 100, bar = g.querySelector('.sp-bar i'), num = g.querySelector('.sp-n'), dEl = g.querySelector('.dist');
  function paint() {
    g.setAttribute('data-sp', String(sp));
    bar.style.width = Math.round(sp / 6 * 100) + '%';
    num.textContent = String(sp * 5);
    dEl.textContent = String(dist);
  }
  g.querySelector('.b-fast').addEventListener('click', function () {
    g.setAttribute('data-stop', '0');
    sp = Math.min(6, sp + 1);
    dist += 40 + sp * 30;   /* 速くするほど、ゴールが遠くなる（上には上がいる） */
    paint();
  });
  g.querySelector('.b-look').addEventListener('click', function () {
    sp = 0; dist = 100; paint();
    g.setAttribute('data-stop', '1');
    if (window.pengessoPop) {
      var r = g.querySelector('.track').getBoundingClientRect();
      window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🌼', '🌈', '🐧', '💛'], 16);
    }
  });
  paint();
})();
""",
    ja={
        "The sprint with no end": "終わらない短距離走",
        "Tap \"Faster!\" again and again. Watch the finish line and your friends.": "「もっと速く！」を何回も押してみてね。ゴールと、友達を見ていて。",
        "🍜 \"Let's eat together!\"": "🍜「いっしょにごはん行こう！」",
        "🌈 \"Look, a rainbow!\"": "🌈「見て、にじだよ！」",
        "m": "m",
        "💨 Speed": "💨 スピード",
        "💨 Faster!": "💨 もっと速く！",
        "🌼 Look around": "🌼 まわりを見る",
        "Your goal is the flag. How far is it?": "ゴールは旗です。あと、どのくらい？",
        "🏁 Faster… but the finish line moves farther away!": "🏁 速くなった…のに、ゴールがもっと遠くなった！",
        "💦 Full speed! The flag is even farther, and your friends' voices are gone.": "💦 全速力！旗はもっと遠く、友達の声も聞こえなくなりました。",
        "🌼 You stopped. Now you can hear your friends again.": "🌼 止まったら、友達の声がまた聞こえてきました。",
    },
)
build(d)
