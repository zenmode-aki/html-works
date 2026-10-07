from gen import build

d = dict(
    slug="we-learned-to-always-fight", seq=523,
    title=("We learned to fight from games where only one side wins",
           "「誰かが勝つと誰かが負ける」ゲームで、戦わなきゃと思いこんできた"),
    label=("One Cake Game", "ケーキ1つのゲーム"),
    h1_emoji="🍰",
    alt="A chubby plush corduroy and felt penguin holding a fork next to a real strawberry shortcake on a small plate",
    section="一番大事なのは「戦わない」こと",
    message="受験や大会のような「誰かが勝つと誰かが負ける」ゲームをくり返して、「戦わなきゃ」と思いこんできた。でも大人の毎日は、そんなゲームばかりではない。",
    tone="素材の重さ：真面目（生き方の考え方）\n→ 見せ方：ポップに（いちごのピンクとクリーム色。ケーキの引っぱり合いで遊べる）",
    game_ja="🍰 ケーキ1つ、フォーク2本：まん中にケーキが1つ。「🍴 左が引っぱる」「🍴 右が引っぱる」を押すと、ケーキがその方へ1歩ずつ動く。端まで行くと、そっちのペンギンは 😋、もう片方は 😢（「1人が勝つと、1人が負ける」）。すると「🎂 もう1つケーキを焼く！」ボタンが出て、押すとケーキが2つになり、2羽とも 😋。「うれしいペンギン：2/2」。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of plush toy corduroy and felt "
            "with visible soft stitching, sitting at a small table and holding a little fork, smiling at a realistic strawberry shortcake "
            "with whipped cream on a white plate. Bright simple strawberry pink and cream background with soft depth. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × コーデュロイとフェルトのぬいぐるみ × いちごのショートケーキ",
    mood=["lift", "think"], tags=["psychology", "mindset", "school"],
    pal=dict(bg="#fff6f8", muted="#8a6772", acc="#e8457a", acc2="#ffb347", shadow="rgba(160,60,90,.16)",
             r1="rgba(255,120,160,.26)", r2="rgba(255,200,120,.26)", r3="rgba(140,220,200,.16)",
             h1="#4a1a2c", photo="#ffe6ee", big="#c92f63", bigdark="#ffb0cb",
             game="linear-gradient(150deg, #ff6f9c 0%, #f0508a 50%, #ffb347 100%)"),
    cards=[
        dict(emoji="🏆", label=("Never Give Up", "諦めない"),
             s=[("In Japan, \"Never give up and fight to the end\" is often seen as a good thing.",
                 "日本では、「諦めずに最後まで戦う」ことが、よいこととされがちです。")]),
        dict(emoji="📝", label=("Win or Lose", "勝ちと負け"),
             s=[("Entrance exams and club tournaments are games where if someone wins, someone loses.",
                 "受験や部活の大会は、誰かが勝つと、誰かが負けるゲームです。")]),
        dict(emoji="🔁", label=("Again and Again", "何度も"),
             s=[("We played games like that many times, so we may believe, \"I must fight even if I cannot win.\"",
                 "そんなゲームを何度もくり返すうちに、「勝てなくても戦わなきゃ」と思いこんでいるのかもしれません。")]),
        dict(emoji="🎂", label=("More Cakes", "ケーキは増やせる"), big=True,
             s=[("But in grown-up life, not every game has only 1 cake.",
                 "でも、大人の毎日は、ケーキが1つしかないゲームばかりではありません。")]),
    ],
    game_after=3,
    game_note="ケーキ1つ、フォーク2本（引っぱり合いと、もう1つ焼く）",
    game_html="""  <section class="game" data-s="tug" data-pos="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">One cake, two forks</div>
    <div class="game-hint">Pull the cake to one side. What happens to the other penguin?</div>
    <div class="table" aria-hidden="true">
      <div class="pg pg-l"><span class="face fl">🙂</span><span class="pg-e">🐧</span></div>
      <div class="track"><div class="cake"><span class="cake-e">🍰</span></div><div class="cake2"><span class="cake-e2">🍰</span></div></div>
      <div class="pg pg-r"><span class="face fr">🙂</span><span class="pg-e">🐧</span></div>
    </div>
    <div class="pull">
      <button type="button" class="btn tug tl">🍴 Left pulls</button>
      <button type="button" class="btn tug tr">🍴 Right pulls</button>
    </div>
    <div class="msg">
      <div class="m-tug">Tap fast! The cake moves 1 step each time.</div>
      <div class="m-won">One penguin wins, one penguin loses. 😢 Is this the only game?</div>
      <div class="m-two">Now there are 2 cakes. Both penguins win! 🎉</div>
    </div>
    <button type="button" class="btn bake">🎂 Bake one more cake!</button>
    <div class="score"><span class="sc-l">😋 Happy penguins:</span> <span class="hn">0</span><span class="sc-of">/2</span></div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Start over</button></div>
  </section>""",
    css="""
  /* 🍰 ケーキ1つ、フォーク2本 */
  .table { display: grid; grid-template-columns: 64px 1fr 64px; align-items: end; gap: 6px; max-width: 380px; margin: 18px auto 0;
    padding: 16px 10px 14px; border-radius: 24px; background: #fff3e0; box-shadow: inset 0 -12px 0 #f5d2a6; }
  .pg { display: grid; justify-items: center; gap: 2px; }
  .pg-e { font-size: 42px; line-height: 1; }
  .face { font-size: 26px; line-height: 1; transition: transform .2s ease; }
  .track { position: relative; height: 70px; }
  .cake, .cake2 { position: absolute; top: 10px; left: 50%; font-size: 44px; line-height: 1; transform: translateX(-50%); transition: left .18s ease, opacity .3s ease; }
  .cake2 { opacity: 0; }
  .game[data-pos="-3"] .cake { left: 4%; } .game[data-pos="-2"] .cake { left: 19%; } .game[data-pos="-1"] .cake { left: 34%; }
  .game[data-pos="1"] .cake { left: 66%; } .game[data-pos="2"] .cake { left: 81%; } .game[data-pos="3"] .cake { left: 96%; }
  .game[data-s="two"] .cake { left: 4%; } .game[data-s="two"] .cake2 { left: 96%; opacity: 1; }
  .game[data-s="two"] .cake-e2 { display: inline-block; animation: boing .6s ease; }
  .face.happy { animation: boing .5s ease; }
  .pull { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 380px; margin: 14px auto 0; }
  .tug { min-height: 64px; background: #fff; color: #7a2241; }
  .tug.hit { animation: boing .25s ease; }
  .game[data-s="two"] .pull { opacity: .4; }
  .msg { margin-top: 12px; min-height: 50px; font-size: 16.5px; font-weight: 900; line-height: 1.4; }
  .msg > div { display: none; }
  .game[data-s="tug"] .m-tug, .game[data-s="won"] .m-won, .game[data-s="two"] .m-two { display: block; animation: boing .45s ease; }
  .bake { display: none; margin: 4px auto 0; min-height: 60px; font-size: 18px; background: #ffe066; color: #4a3500; }
  .game[data-s="won"] .bake { display: inline-flex; animation: boing .6s ease; }
  .score { margin-top: 12px; font-size: 15.5px; font-weight: 900; }
  .hn { display: inline-block; min-width: 1.4em; padding: 2px 8px; border-radius: 999px; background: rgba(255,255,255,.3); }
  .ctrl { margin-top: 10px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
""",
    dark="""  html[data-theme="dark"] .table { background: #3a2c22; box-shadow: inset 0 -12px 0 #5a4030; }
  html[data-theme="dark"] .game .tug { background: #2b2d3a; color: #ffd0de; }
  html[data-theme="dark"] .game .bake { background: #4a3c12; color: #ffe39a; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var pos = 0, fl = g.querySelector('.fl'), fr = g.querySelector('.fr'), hn = g.querySelector('.hn');
  function pop(el, list) {
    if (!window.pengessoPop) return;
    var r = el.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, 16);
  }
  function face(el, e) { el.textContent = e; el.classList.remove('happy'); void el.offsetWidth; el.classList.add('happy'); }
  function pull(dir, btn) {
    if (g.getAttribute('data-s') !== 'tug') return;
    btn.classList.remove('hit'); void btn.offsetWidth; btn.classList.add('hit');
    pos = Math.max(-3, Math.min(3, pos + dir));
    g.setAttribute('data-pos', String(pos));
    fl.textContent = pos < 0 ? '😆' : pos > 0 ? '😣' : '🙂';
    fr.textContent = pos > 0 ? '😆' : pos < 0 ? '😣' : '🙂';
    if (Math.abs(pos) === 3) {
      g.setAttribute('data-s', 'won');
      face(pos < 0 ? fl : fr, '😋'); face(pos < 0 ? fr : fl, '😢');
      hn.textContent = '1';
      if (navigator.vibrate) { try { navigator.vibrate(20); } catch (e) {} }
    }
  }
  g.querySelector('.tl').addEventListener('click', function () { pull(-1, this); });
  g.querySelector('.tr').addEventListener('click', function () { pull(1, this); });
  g.querySelector('.bake').addEventListener('click', function () {
    g.setAttribute('data-s', 'two');
    face(fl, '😋'); face(fr, '😋'); hn.textContent = '2';
    [].forEach.call(g.querySelectorAll('.tug'), function (b) { b.disabled = true; });
    pop(g.querySelector('.track'), ['🍰', '🎂', '🐧', '✨', '🍓']);
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    pos = 0; g.setAttribute('data-pos', '0'); g.setAttribute('data-s', 'tug');
    fl.textContent = '🙂'; fr.textContent = '🙂'; hn.textContent = '0';
    [].forEach.call(g.querySelectorAll('.tug'), function (b) { b.disabled = false; });
  });
})();
""",
    ja={
        "One cake, two forks": "ケーキ1つ、フォーク2本",
        "Pull the cake to one side. What happens to the other penguin?": "ケーキをどちらかに引っぱってね。もう1羽のペンギンはどうなる？",
        "🍴 Left pulls": "🍴 左が引っぱる",
        "🍴 Right pulls": "🍴 右が引っぱる",
        "Tap fast! The cake moves 1 step each time.": "どんどん押して！1回で1歩、ケーキが動きます。",
        "One penguin wins, one penguin loses. 😢 Is this the only game?": "1羽が勝って、1羽が負けた。😢 ゲームって、これしかないの？",
        "Now there are 2 cakes. Both penguins win! 🎉": "ケーキが2つになった。2羽とも勝ち！🎉",
        "🎂 Bake one more cake!": "🎂 もう1つケーキを焼く！",
        "😋 Happy penguins:": "😋 うれしいペンギン：",
        "/2": "/2",
        "↺ Start over": "↺ 最初から",
    },
)
build(d)
