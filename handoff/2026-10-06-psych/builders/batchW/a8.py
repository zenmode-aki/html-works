from gen import build

d = dict(
    slug="small-wins-grow-self-worth", seq=519,
    title=("Self-esteem can grow at any age through small wins of helping people",
           "自己肯定感は、人の役に立つ小さな成功で、大人になってからでも育つ"),
    label=("Small Wins", "小さな成功"),
    h1_emoji="🧱",
    alt="A chubby brushed mohair penguin standing proudly on top of a small tower of real colorful wooden toy blocks",
    section="幸せに大切な2つ",
    message="自己肯定感は、大人になってからでも、工夫して人の役に立つ小さな成功で育つ。",
    tone="素材の重さ：真面目（自己肯定感）\n→ 見せ方：ポップに（むらさきとオレンジ。「ありがとう」のブロックを積んで高くなる）",
    game_ja="🧱 ありがとうタワー：6つの小さな親切（道を教える／スマホの便利ワザを教える／友達にごはんを作る／傘を貸す／宿題を説明する／ドアを押さえる）を押すたびに「ありがとう！」が出て、ブロックが1つ積まれ、ペンギンが少し高いところに立つ。レベルが「小さい→育ってる→高い→いい景色！」と上がり、6つで景色に虹。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of soft brushed mohair, "
            "standing proudly on top of a small tower of realistic colorful wooden toy building blocks (five blocks, big and simple), "
            "flippers slightly raised, looking at a wide view. Bright simple purple and warm orange background with soft depth. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × ブラッシュドモヘア × 木のつみき",
    mood=["lift", "energy"], tags=["psychology", "happiness", "tips"],
    pal=dict(bg="#fcf6ff", muted="#80709a", acc="#9036e0", acc2="#ff7a45", shadow="rgba(110,50,170,.16)",
             r1="rgba(255,150,90,.28)", r2="rgba(144,54,224,.18)", r3="rgba(120,220,120,.14)",
             h1="#35195a", photo="#f0e4ff", big="#7a26c9", bigdark="#d2a8ff",
             game="linear-gradient(160deg, #9036e0 0%, #e0549b 55%, #ff9a3c 100%)"),
    cards=[
        dict(emoji="🌱", label=("Any Age", "何歳からでも"),
             s=[("It is said you can grow your self-esteem even as an adult.",
                 "自己肯定感は、大人になってからでも育てられるそうです。")]),
        dict(emoji="💛", label=("The Trick", "コツ"),
             s=[("The trick is to help people with a small idea, and pile up small \"thank you\" wins.",
                 "コツは、ちょっと工夫して人の役に立ち、「ありがとう」の小さな成功を重ねることです。")]),
        dict(emoji="🗺️", label=("For Example", "たとえば"),
             s=[("For example, show a lost person the way on a map app, or teach a friend a phone trick.",
                 "たとえば、道に迷った人に地図アプリで道を教える、友達にスマホの便利ワザを教える、などです。")]),
        dict(emoji="🧱", label=("Block By Block", "1つずつ"), big=True,
             s=[("Each \"thank you\" becomes 1 block, and the place you stand gets a little higher.",
                 "1つの「ありがとう」が1つのブロックになって、自分の足場が少しずつ高くなります。")]),
    ],
    game_after=3,
    game_note="ありがとうタワー（小さな親切でブロックが積まれる）",
    game_html="""  <section class="game" data-n="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">The thank-you tower</div>
    <div class="game-hint">Tap a small kind act. Each "thank you" adds 1 block.</div>
    <div class="tw">
      <div class="sky" aria-hidden="true"><span class="rainbow"></span></div>
      <div class="stack">
        <div class="blk" data-b="1"><span class="blk-e"></span></div>
        <div class="blk" data-b="2"><span class="blk-e"></span></div>
        <div class="blk" data-b="3"><span class="blk-e"></span></div>
        <div class="blk" data-b="4"><span class="blk-e"></span></div>
        <div class="blk" data-b="5"><span class="blk-e"></span></div>
        <div class="blk" data-b="6"><span class="blk-e"></span></div>
        <div class="pgw">
          <div class="thx">Thank you! 💛</div>
          <span class="pg-e">🐧</span>
        </div>
      </div>
    </div>
    <div class="lvl">
      <span class="lv lv0">🌱 Level: just starting</span>
      <span class="lv lv1">🌿 Level: growing</span>
      <span class="lv lv2">🌳 Level: tall</span>
      <span class="lv lv3">🌈 Level: what a view!</span>
      <span class="cnt"><span class="cl">🧱 Blocks:</span> <span class="nb">0</span> <span class="co">/ 6</span></span>
    </div>
    <div class="acts">
      <button type="button" class="btn act" data-e="🗺️">🗺️ Show the way</button>
      <button type="button" class="btn act" data-e="📱">📱 Teach a phone trick</button>
      <button type="button" class="btn act" data-e="🍳">🍳 Cook for a friend</button>
      <button type="button" class="btn act" data-e="☂️">☂️ Lend an umbrella</button>
      <button type="button" class="btn act" data-e="📚">📚 Explain homework</button>
      <button type="button" class="btn act" data-e="🚪">🚪 Hold the door</button>
    </div>
    <div class="end">🎉 6 small wins. You stand higher, and you can see far.</div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Start over</button></div>
  </section>""",
    css="""
  /* 🧱 ありがとうタワー */
  .tw { position: relative; height: 290px; max-width: 420px; margin: 16px auto 0; border-radius: 24px; overflow: hidden;
    background: linear-gradient(#e9f6ff, #fff6e6 80%); border-bottom: 10px solid #8bd27a; }
  .sky { position: absolute; inset: 0; }
  .rainbow { position: absolute; left: 50%; top: 40px; width: 300px; height: 150px; margin-left: -150px; border-radius: 150px 150px 0 0; opacity: 0;
    background: radial-gradient(circle at 50% 100%, transparent 52%, #8f7bff 52% 60%, #4cc3ff 60% 68%, #6fe07a 68% 76%, #ffd84a 76% 84%, #ff7b6b 84% 92%, transparent 92%);
    transition: opacity .8s ease; }
  .game[data-n="6"] .rainbow { opacity: .75; }
  .stack { position: absolute; left: 50%; bottom: 0; width: 132px; margin-left: -66px; display: flex; flex-direction: column-reverse; align-items: center; }
  .blk { width: 116px; height: 0; border-radius: 8px; overflow: hidden; display: grid; place-items: center; transition: height .35s cubic-bezier(.3,1.5,.5,1); }
  .blk.on { height: 26px; margin-top: 3px; box-shadow: inset 0 -5px 0 rgba(0,0,0,.14); }
  .blk[data-b="1"] { background: #ff7b6b; } .blk[data-b="2"] { background: #ffb347; } .blk[data-b="3"] { background: #ffd84a; }
  .blk[data-b="4"] { background: #6fe07a; } .blk[data-b="5"] { background: #4cc3ff; } .blk[data-b="6"] { background: #8f7bff; }
  .blk-e { font-size: 18px; line-height: 1; }
  .pgw { position: relative; display: grid; justify-items: center; }
  .pg-e { font-size: 56px; line-height: 1; }
  .thx { position: absolute; bottom: 100%; left: 50%; transform: translate(-50%, 8px) scale(.6); width: max-content; max-width: 200px;
    padding: 5px 10px; border-radius: 14px; background: #fff; color: #b0306b; font-size: 14px; font-weight: 900; opacity: 0; }
  .pgw.yay .thx { animation: thx 1.1s ease; }
  @keyframes thx { 0% { opacity: 0; transform: translate(-50%, 8px) scale(.6); } 25% { opacity: 1; transform: translate(-50%, -4px) scale(1); } 80% { opacity: 1; transform: translate(-50%, -10px) scale(1); } 100% { opacity: 0; transform: translate(-50%, -18px) scale(1); } }
  .pgw.yay .pg-e { animation: boing .5s ease; }
  .lvl { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 6px 10px; max-width: 420px; margin: 12px auto 0; font-size: 15px; font-weight: 900; }
  .lv { display: none; }
  .game[data-n="0"] .lv0, .game[data-n="1"] .lv0, .game[data-n="2"] .lv1, .game[data-n="3"] .lv1,
  .game[data-n="4"] .lv2, .game[data-n="5"] .lv2, .game[data-n="6"] .lv3 { display: inline; }
  .nb { display: inline-block; min-width: 1.4em; padding: 1px 8px; border-radius: 999px; background: rgba(255,255,255,.3); }
  .acts { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 420px; margin: 12px auto 0; }
  .act { min-height: 58px; border-radius: 18px; font-size: 14.5px; padding: 8px 10px; }
  .act[disabled] { opacity: .5; }
  .end { display: none; margin: 14px auto 0; max-width: 420px; padding: 12px 14px; border-radius: 18px; background: #fff; color: #6a1fb0; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .game[data-n="6"] .end { display: block; animation: boing .5s ease; }
  .ctrl { margin-top: 12px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
""",
    dark="""  html[data-theme="dark"] .tw { background: linear-gradient(#1f2c45, #3a3326 80%); border-bottom-color: #3f6b2c; }
  html[data-theme="dark"] .thx { background: #2b2d3a; color: #ffb3d4; }
  html[data-theme="dark"] .end { background: #2b2d3a; color: #e0c2ff; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var n = 0, pg = g.querySelector('.pgw'), blks = g.querySelectorAll('.blk');
  function again(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  [].forEach.call(g.querySelectorAll('.act'), function (b) {
    b.addEventListener('click', function () {
      if (b.disabled || n >= 6) return;
      b.disabled = true;
      var blk = blks[n];
      blk.querySelector('.blk-e').textContent = b.getAttribute('data-e');
      blk.classList.add('on');
      n++;
      g.querySelector('.nb').textContent = n;
      g.setAttribute('data-n', String(n));
      again(pg, 'yay');
      setTimeout(function () {
        if (!window.pengessoPop) return;
        var r = pg.getBoundingClientRect();
        window.pengessoPop(r.left + r.width / 2, r.top, n === 6 ? ['🌈', '💛', '🐧', '✨', '🧱'] : ['💛', '✨'], n === 6 ? 22 : 7);
      }, 200);
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    n = 0; g.querySelector('.nb').textContent = 0; g.setAttribute('data-n', '0');
    [].forEach.call(blks, function (k) { k.classList.remove('on'); k.querySelector('.blk-e').textContent = ''; });
    [].forEach.call(g.querySelectorAll('.act'), function (b) { b.disabled = false; });
  });
})();
""",
    ja={
        "The thank-you tower": "ありがとうタワー",
        "Tap a small kind act. Each \"thank you\" adds 1 block.": "小さな親切を押してね。「ありがとう」1つで、ブロックが1つ積まれます。",
        "Thank you! 💛": "ありがとう！💛",
        "🌱 Level: just starting": "🌱 レベル：はじめたばかり",
        "🌿 Level: growing": "🌿 レベル：育ってきた",
        "🌳 Level: tall": "🌳 レベル：高い！",
        "🌈 Level: what a view!": "🌈 レベル：いい景色！",
        "🧱 Blocks:": "🧱 ブロック：",
        "/ 6": "/ 6",
        "🗺️ Show the way": "🗺️ 道を教える",
        "📱 Teach a phone trick": "📱 スマホの便利ワザを教える",
        "🍳 Cook for a friend": "🍳 友達にごはんを作る",
        "☂️ Lend an umbrella": "☂️ 傘を貸す",
        "📚 Explain homework": "📚 宿題を説明する",
        "🚪 Hold the door": "🚪 ドアを押さえる",
        "🎉 6 small wins. You stand higher, and you can see far.": "🎉 小さな成功が6つ。高いところに立てて、遠くまで見えます。",
        "↺ Start over": "↺ 最初から",
    },
)
build(d)
