from gen import build

d = dict(
    slug="you-dont-have-to-endure-weaknesses", seq=528,
    title=("You do not have to endure your weak points; shine somewhere else",
           "苦手は耐えなくていい。弱みが出ない場所で光ればいい"),
    label=("Shine Backstage", "裏方で光る"),
    h1_emoji="🎛️",
    alt="A chubby hand-embroidered felt penguin happily operating a real theater spotlight from backstage",
    section="一番大事なのは「戦わない」こと（②強みを活かし、弱みが出ないことをする）",
    message="「苦手なことも耐えてやり抜くべき」は捨てていい。人前が苦手なら、裏方で光ればいい。",
    tone="素材の重さ：真面目（生き方の考え方）\n→ 見せ方：ポップに（劇場の深い紫とスポットライトの黄色。舞台と裏方の切りかえで遊べる）",
    game_ja="🎭 舞台と裏方：「🎤 舞台の上」では、人前で話すのが苦手なペンギンがスポットライトの下。「🎤 セリフを言う」を押すたびにドキドキメーターが上がって汗が増え、「え、えっと…」。3回で「😵 ここは私の場所じゃないかも」。「🎛️ 裏方」に切りかえると、同じペンギンが照明係。🔴🟡🔵 のライトを押すと舞台の色が変わり、3色そろうと拍手メーターが満タンで「🎉 劇は大成功！裏方から光っている」。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of hand-embroidered felt with "
            "visible colorful stitches, standing backstage and happily aiming a realistic black theater spotlight on a stand, a warm beam "
            "of light going toward a soft-focus stage curtain. Bright simple deep violet and spotlight yellow background with soft depth. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × 手刺しゅうのフェルト × 舞台のスポットライト",
    mood=["lift", "laugh"], tags=["psychology", "mindset", "school"],
    pal=dict(bg="#f8f4ff", muted="#6f6585", acc="#7a3fd1", acc2="#ffc23c", shadow="rgba(80,40,150,.18)",
             r1="rgba(255,200,60,.30)", r2="rgba(120,70,220,.20)", r3="rgba(255,110,140,.16)",
             h1="#26164a", photo="#ece2ff", big="#6631bf", bigdark="#cdb4ff",
             game="linear-gradient(150deg, #3b1f7a 0%, #6b35c8 55%, #ffb03c 100%)"),
    cards=[
        dict(emoji="🗑️", label=("Throw It Away", "捨てていい"),
             s=[("I think you can throw away the idea, \"You should endure the things you are bad at.\"",
                 "「苦手なことも、耐えてやり抜くべき」という考えは、捨てていいと思います。")]),
        dict(emoji="💪", label=("Use Strengths", "強みを使う"),
             s=[("What matters is using your strengths and doing things where your weak points do not show.",
                 "大事なのは、強みを活かして、弱みが出ないことをすることです。")]),
        dict(emoji="🎛️", label=("Go Backstage", "裏方へ"), big=True,
             s=[("For example, if you are bad at speaking in front of people, you can shine backstage.",
                 "たとえば、人前で話すのが苦手なら、裏方で力を発揮すればいいのです。")]),
        dict(emoji="🎭", label=("School Play", "学校の劇"),
             s=[("In a school play, the light team is just as important as the main role.",
                 "学校の劇なら、照明係も、主役と同じくらい大事です。")]),
    ],
    game_after=2,
    game_note="舞台と裏方（同じペンギンが、場所を変えると光る）",
    game_html="""  <section class="game" data-v="stage" data-nerve="0" data-lights="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">On stage or backstage?</div>
    <div class="game-hint">This penguin is bad at speaking in front of people. Try both places.</div>
    <div class="tabs">
      <button type="button" class="btn tab tb-stage">🎤 On stage</button>
      <button type="button" class="btn tab tb-back">🎛️ Backstage</button>
    </div>
    <div class="theater" aria-hidden="true">
      <div class="curtain cl"></div><div class="curtain cr"></div>
      <div class="beam"></div>
      <div class="v-stage">
        <div class="star"><span class="sweat">💦</span><span class="star-e">🐧</span></div>
        <div class="crowd"><span class="crowd-e">🐧🐧🐧🐧🐧</span></div>
      </div>
      <div class="v-back">
        <div class="actors"><span class="actors-e">🐧🐧</span></div>
        <div class="desk"><span class="tech-e">🐧</span><span class="desk-e">🎛️</span></div>
      </div>
    </div>
    <div class="meter-row mr-n"><span class="mr-l">💓 Nervous</span><span class="mbar"><i class="nb"></i></span></div>
    <div class="meter-row mr-c"><span class="mr-l">🎉 Cheers</span><span class="mbar"><i class="cb"></i></span></div>
    <div class="msg">
      <div class="m-s0">Tap "Say your lines."</div>
      <div class="m-s1">"Uh… um… hello…" 💦</div>
      <div class="m-s2">"The… the night is…" 💦💦</div>
      <div class="m-s3">😵 This may not be my place.</div>
      <div class="m-b0">Same penguin. Now tap the lights!</div>
      <div class="m-b1">Nice! The stage is glowing. More colors?</div>
      <div class="m-b3">🎉 The show is a hit! You shine from backstage.</div>
    </div>
    <div class="acts a-stage"><button type="button" class="btn say">🎤 Say your lines</button></div>
    <div class="acts a-back">
      <button type="button" class="btn lt" data-c="r">🔴 Red</button>
      <button type="button" class="btn lt" data-c="y">🟡 Yellow</button>
      <button type="button" class="btn lt" data-c="b">🔵 Blue</button>
    </div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Start over</button></div>
  </section>""",
    css="""
  /* 🎭 舞台と裏方 */
  .tabs { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; max-width: 360px; margin: 14px auto 0; padding: 6px; border-radius: 999px; background: rgba(255,255,255,.18); }
  .tab { min-height: 50px; padding: 8px 10px; font-size: 15px; background: transparent; color: #fff; box-shadow: none; }
  .game[data-v="stage"] .tb-stage, .game[data-v="back"] .tb-back { background: #fff; color: #3b1f7a; box-shadow: 0 4px 0 rgba(0,0,0,.18); }
  .game[data-nerve="3"][data-v="stage"] .tb-back { animation: boing .7s ease 3; background: #ffe066; color: #4a3500; }
  .theater { position: relative; max-width: 360px; height: 220px; margin: 14px auto 0; border-radius: 22px; overflow: hidden; background: #1c1236;
    box-shadow: inset 0 -40px 0 #5a3a1c; }
  .curtain { position: absolute; top: 0; bottom: 40px; width: 16%; background: linear-gradient(90deg, #b3203c, #e0405c, #b3203c); z-index: 2; }
  .cl { left: 0; border-radius: 0 0 30px 0; } .cr { right: 0; border-radius: 0 0 0 30px; }
  .beam { position: absolute; left: 50%; top: -20px; width: 180px; height: 230px; transform: translateX(-50%);
    background: radial-gradient(ellipse at 50% 100%, rgba(255,240,170,.75), rgba(255,240,170,0) 70%); transition: background .3s ease; }
  .v-stage, .v-back { position: absolute; inset: 0; transition: opacity .35s ease; }
  .v-back, .game[data-v="back"] .v-stage { opacity: 0; }
  .game[data-v="back"] .v-back { opacity: 1; }
  .star { position: absolute; left: 50%; bottom: 52px; transform: translateX(-50%); font-size: 50px; line-height: 1; }
  .sweat { position: absolute; right: -18px; top: -6px; font-size: 22px; opacity: 0; transition: opacity .2s ease; }
  .game[data-nerve="1"] .sweat { opacity: .5; } .game[data-nerve="2"] .sweat, .game[data-nerve="3"] .sweat { opacity: 1; }
  .game[data-nerve="2"] .star-e, .game[data-nerve="3"] .star-e { display: inline-block; animation: shiver .25s linear infinite; }
  @keyframes shiver { 25% { transform: translateX(-2px); } 75% { transform: translateX(2px); } }
  .crowd { position: absolute; left: 0; right: 0; bottom: 4px; text-align: center; font-size: 26px; letter-spacing: 2px; line-height: 1; opacity: .85; }
  .actors { position: absolute; left: 50%; bottom: 52px; transform: translateX(-50%); font-size: 42px; line-height: 1; letter-spacing: 6px; }
  .desk { position: absolute; right: 18%; bottom: 4px; font-size: 30px; line-height: 1; }
  .game[data-v="back"] .beam { background: radial-gradient(ellipse at 50% 100%, rgba(255,255,255,.25), rgba(255,255,255,0) 70%); }
  .game[data-v="back"] .theater.c-r .beam { background: radial-gradient(ellipse at 50% 100%, rgba(255,90,110,.8), rgba(255,90,110,0) 70%); }
  .game[data-v="back"] .theater.c-y .beam { background: radial-gradient(ellipse at 50% 100%, rgba(255,226,90,.85), rgba(255,226,90,0) 70%); }
  .game[data-v="back"] .theater.c-b .beam { background: radial-gradient(ellipse at 50% 100%, rgba(90,170,255,.85), rgba(90,170,255,0) 70%); }
  .game[data-lights="3"] .actors-e { display: inline-block; animation: boing .6s ease infinite; }
  .meter-row { display: flex; align-items: center; gap: 8px; max-width: 340px; margin: 12px auto 0; font-size: 14.5px; font-weight: 900; }
  .mr-l { flex: 0 0 auto; }
  .mbar { position: relative; flex: 1; height: 14px; border-radius: 999px; background: rgba(255,255,255,.25); overflow: hidden; }
  .mbar i { position: absolute; inset: 0 auto 0 0; width: 0; border-radius: 999px; transition: width .35s cubic-bezier(.2,1.2,.4,1); }
  .nb { background: #ff6b8a; } .cb { background: #ffe066; }
  .mr-c, .game[data-v="back"] .mr-n { display: none; }
  .game[data-v="back"] .mr-c { display: flex; }
  .msg { margin-top: 12px; min-height: 48px; font-size: 16.5px; font-weight: 900; line-height: 1.4; }
  .msg > div { display: none; }
  .game[data-v="stage"][data-nerve="0"] .m-s0, .game[data-v="stage"][data-nerve="1"] .m-s1, .game[data-v="stage"][data-nerve="2"] .m-s2,
  .game[data-v="stage"][data-nerve="3"] .m-s3, .game[data-v="back"][data-lights="0"] .m-b0, .game[data-v="back"][data-lights="1"] .m-b1,
  .game[data-v="back"][data-lights="2"] .m-b1, .game[data-v="back"][data-lights="3"] .m-b3 { display: block; animation: boing .45s ease; }
  .acts { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-top: 8px; }
  .a-back, .game[data-v="back"] .a-stage { display: none; }
  .game[data-v="back"] .a-back { display: flex; }
  .say { min-width: 220px; min-height: 60px; font-size: 18px; background: #fff; color: #3b1f7a; }
  .lt { min-width: 96px; background: #fff; color: #3b1f7a; }
  .lt.on { background: #ffe066; color: #4a3500; }
  .ctrl { margin-top: 10px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
""",
    dark="""  html[data-theme="dark"] .game .tab { background: transparent; color: #fff; }
  html[data-theme="dark"] .game[data-v="stage"] .tb-stage, html[data-theme="dark"] .game[data-v="back"] .tb-back { background: #f4f0fa; color: #3b1f7a; }
  html[data-theme="dark"] .game .say, html[data-theme="dark"] .game .lt { background: #2b2d3a; color: #e6dcff; }
  html[data-theme="dark"] .game .lt.on { background: #4a3c12; color: #ffe39a; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var nerve = 0, lit = {}, nb = g.querySelector('.nb'), cb = g.querySelector('.cb'), th = g.querySelector('.theater');
  function pop(el, list) {
    if (!window.pengessoPop) return;
    var r = el.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, 18);
  }
  g.querySelector('.tb-stage').addEventListener('click', function () { g.setAttribute('data-v', 'stage'); });
  g.querySelector('.tb-back').addEventListener('click', function () { g.setAttribute('data-v', 'back'); });
  g.querySelector('.say').addEventListener('click', function () {
    nerve = Math.min(3, nerve + 1);
    g.setAttribute('data-nerve', String(nerve));
    nb.style.width = (nerve / 3 * 100) + '%';
    if (navigator.vibrate) { try { navigator.vibrate(15 * nerve); } catch (e) {} }
  });
  [].forEach.call(g.querySelectorAll('.lt'), function (b) {
    b.addEventListener('click', function () {
      var c = b.getAttribute('data-c');
      lit[c] = 1; b.classList.add('on');
      th.classList.remove('c-r', 'c-y', 'c-b'); th.classList.add('c-' + c);
      var n = Object.keys(lit).length;
      cb.style.width = (n / 3 * 100) + '%';
      var was = g.getAttribute('data-lights');
      g.setAttribute('data-lights', String(n));
      if (n === 3 && was !== '3') pop(th, ['🎉', '🐧', '⭐', '✨', '🎭']);
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    nerve = 0; lit = {}; nb.style.width = '0'; cb.style.width = '0';
    th.classList.remove('c-r', 'c-y', 'c-b');
    g.setAttribute('data-v', 'stage'); g.setAttribute('data-nerve', '0'); g.setAttribute('data-lights', '0');
    [].forEach.call(g.querySelectorAll('.lt'), function (b) { b.classList.remove('on'); });
  });
})();
""",
    ja={
        "On stage or backstage?": "舞台の上？それとも裏方？",
        "This penguin is bad at speaking in front of people. Try both places.": "このペンギンは、人前で話すのが苦手。両方の場所をためしてみてね。",
        "🎤 On stage": "🎤 舞台の上",
        "🎛️ Backstage": "🎛️ 裏方",
        "💓 Nervous": "💓 ドキドキ",
        "🎉 Cheers": "🎉 拍手",
        "Tap \"Say your lines.\"": "「セリフを言う」を押してね。",
        "\"Uh… um… hello…\" 💦": "「え、えっと…こ、こんにちは…」💦",
        "\"The… the night is…\" 💦💦": "「よ、夜が…その…」💦💦",
        "😵 This may not be my place.": "😵 ここは、私の場所じゃないかも。",
        "Same penguin. Now tap the lights!": "同じペンギンです。ライトを押してみて！",
        "Nice! The stage is glowing. More colors?": "いいね！舞台が光ってる。ほかの色も？",
        "🎉 The show is a hit! You shine from backstage.": "🎉 劇は大成功！裏方から光っています。",
        "🎤 Say your lines": "🎤 セリフを言う",
        "🔴 Red": "🔴 赤",
        "🟡 Yellow": "🟡 黄色",
        "🔵 Blue": "🔵 青",
        "↺ Start over": "↺ 最初から",
    },
)
build(d)
