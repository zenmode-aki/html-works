from gen import build

d = dict(
    slug="help-without-wanting-anything-back", seq=534,
    title=("Helping without wanting anything back keeps your heart light",
           "見返りを求めずに助けると、心が軽い"),
    label=("No Strings", "見返りなし"),
    h1_emoji="🎁",
    alt="A chubby corduroy and felt plush penguin happily skipping away after leaving a real kraft paper gift box with a ribbon",
    section="「反応しない心」",
    message="見返りを求めずに役に立つと、「お返しがほしい」というこだわりが生まれないので、心が軽い。",
    tone="素材の重さ：ふつう（人との関わり方）\n→ 見せ方：ポップに（ひまわり色とラベンダー。プレゼントに「お返しよろしく」の札を付けるか外すかで、帰り道の空が変わる）",
    game_ja="🎁 札を付ける？外す？：プレゼントに「🏷 お返しよろしくね」の札が付いている。札を付けたまま「🎁 わたす」と、帰り道ずっと☁️雲がついてきて「まだかな…」メーターがじわじわ上がる（相手はたまたま気づかない）。札を外してわたすと、ペンギンは☀️の下でスキップして帰る。両方ためすと「同じプレゼントでも、心の重さがちがう」。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of plush toy corduroy and felt, "
            "happily skipping away with a little hop after leaving a realistic small kraft paper gift box tied with a soft yellow ribbon on a doorstep. "
            "Bright simple sunflower yellow and lavender background with soft depth and warm afternoon light. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × コーデュロイとフェルト × クラフト紙のプレゼント箱",
    mood=["lift", "think"], tags=["psychology", "friends", "happiness"],
    pal=dict(bg="#fffbef", muted="#80705a", acc="#e08a00", acc2="#8a63e0", shadow="rgba(180,130,30,.16)",
             r1="rgba(255,204,60,.34)", r2="rgba(138,99,224,.16)", r3="rgba(255,140,90,.14)",
             h1="#4a3200", photo="#fff0c8", big="#b86d00", bigdark="#ffd27a",
             game="linear-gradient(160deg, #ffb341 0%, #ff8a6b 45%, #9a6bff 100%)"),
    cards=[
        dict(emoji="🎁", label=("Just Help", "ただ助ける"),
             s=[("Helping someone without wanting anything back makes it easy to feel happy, it is said.",
                 "見返りを求めずに誰かの役に立つと、幸せを感じやすいそうです。"),
                ("This is because you do not start holding on to \"I want something back.\"",
                 "「お返しがほしい」というこだわりが、生まれないからです。")]),
        dict(emoji="☁️", label=("Holding More", "こだわりが増える"),
             s=[("When you think, \"I try so hard, so why don't they see it?\", you may be holding on more.",
                 "「こんなに頑張っているのに、どうして認めてくれないの？」と思うときは、こだわりが増えているのかもしれません。")]),
        dict(emoji="🪶", label=("Stay Light", "軽いまま"), big=True,
             s=[("Once you give it, it ends there.", "渡したら、そこでおしまい。"),
                ("That way, your heart stays light.", "そのくらいのほうが、心が軽いままでいられます。")]),
    ],
    game_after=2,
    game_note="札を付ける？外す？（「お返しよろしく」の札があると、帰り道に雲がついてくる）",
    game_html="""  <section class="game" data-tag="1" data-go="0" data-tried="" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Tag or no tag?</div>
    <div class="game-hint">Give the same gift two times: once with the tag, once without. Watch the way home.</div>
    <div class="gift">
      <span class="box-e">🎁</span>
      <span class="htag">🏷 "You owe me one!"</span>
    </div>
    <button type="button" class="btn b-tag"><span class="bt-on">✂️ Take off the tag</span><span class="bt-off">🏷 Put the tag back on</span></button>
    <div class="road">
      <div class="sky-e"><span class="cloud">☁️</span><span class="sun">☀️</span></div>
      <div class="walker"><span class="pg">🐧</span></div>
      <div class="home-e">🏠</div>
    </div>
    <div class="wait">
      <div class="wt-head"><span class="wt-l">⏳ "Not yet…?" meter</span> <span class="wt-n">0</span></div>
      <div class="wt-bar" aria-hidden="true"><i></i></div>
    </div>
    <button type="button" class="btn b-give">🎁 Give it</button>
    <div class="res">
      <div class="rs0">Your friend is busy today and may not say thank you.</div>
      <div class="rs1">☁️ "Did they notice? Not yet…" The cloud follows you all the way home.</div>
      <div class="rs2">☀️ You gave it, and that is the end. You skip all the way home.</div>
    </div>
    <div class="both">🐧 The same gift. But your heart feels so different.</div>
  </section>""",
    css="""
  /* 🎁 札を付ける？外す？ */
  .gift { display: flex; align-items: center; justify-content: center; gap: 10px; max-width: 420px; min-height: 90px; margin: 14px auto 0;
    padding: 10px; border-radius: 22px; background: rgba(255,255,255,.2); flex-wrap: wrap; }
  .game .box-e { font-size: 54px; line-height: 1; }
  .htag { display: inline-block; padding: 6px 12px; border-radius: 10px; background: #fff; color: #8a3a00; font-size: 15.5px; font-weight: 900;
    transform: rotate(-6deg); transition: transform .4s cubic-bezier(.3,1.4,.5,1), opacity .3s ease; }
  .game[data-tag="0"] .htag { opacity: 0; transform: rotate(-30deg) translateY(30px) scale(.6); }
  .b-tag { margin-top: 10px; }
  .b-tag > span { display: none; }
  .game[data-tag="1"] .bt-on, .game[data-tag="0"] .bt-off { display: inline; }
  .road { position: relative; height: 150px; max-width: 420px; margin: 14px auto 0; border-radius: 22px; overflow: hidden;
    background: linear-gradient(#bfe6ff 0 62%, #8fd17a 62%); }
  .sky-e { position: absolute; left: 14px; top: 10px; transition: left 2.2s ease-in-out; }
  .game .cloud, .game .sun { font-size: 38px; line-height: 1; opacity: 0; transition: opacity .4s ease; }
  .game .sun { position: absolute; left: 0; top: 0; }
  .game[data-go="1"][data-tag="1"] .cloud, .game[data-go="2"][data-tag="1"] .cloud { opacity: 1; }
  .game[data-go="1"][data-tag="0"] .sun, .game[data-go="2"][data-tag="0"] .sun { opacity: 1; }
  .game[data-go="1"][data-tag="1"] .road, .game[data-go="2"][data-tag="1"] .road { background: linear-gradient(#a9b4c4 0 62%, #8aa883 62%); }
  .walker { position: absolute; left: 14px; bottom: 26px; transition: left 2.2s ease-in-out; }
  .game .pg { display: inline-block; font-size: 44px; line-height: 1; }
  .game[data-go="1"] .walker, .game[data-go="2"] .walker { left: calc(100% - 120px); }
  .game[data-go="1"] .sky-e, .game[data-go="2"] .sky-e { left: calc(100% - 118px); }
  .game[data-go="1"][data-tag="0"] .pg { animation: skip .38s ease-in-out infinite alternate; }
  .game[data-go="1"][data-tag="1"] .pg { animation: trudge .7s ease-in-out infinite alternate; }
  @keyframes skip { from { transform: translateY(0) rotate(-6deg); } to { transform: translateY(-16px) rotate(6deg); } }
  @keyframes trudge { from { transform: rotate(-3deg); } to { transform: rotate(3deg) translateY(2px); } }
  .home-e { position: absolute; right: 16px; bottom: 22px; font-size: 44px; line-height: 1; }
  .wait { max-width: 420px; margin: 12px auto 0; padding: 10px 14px; border-radius: 18px; background: rgba(255,255,255,.18); }
  .wt-head { display: flex; justify-content: space-between; font-size: 15px; font-weight: 900; }
  .wt-bar { position: relative; height: 14px; margin-top: 6px; border-radius: 999px; background: rgba(255,255,255,.3); overflow: hidden; }
  .wt-bar i { position: absolute; inset: 0 auto 0 0; width: 0; border-radius: 999px; background: #6b7a90; transition: width 2.2s linear; }
  .b-give { margin-top: 14px; width: min(320px, 100%); min-height: 60px; font-size: 19px; background: #fff3c4; color: #5a3d00; }
  .res { max-width: 420px; margin: 12px auto 0; min-height: 50px; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .res > div { display: none; }
  .game[data-go="0"] .rs0, .game[data-go="1"] .rs0 { display: block; }
  .game[data-go="2"][data-tag="1"] .rs1, .game[data-go="2"][data-tag="0"] .rs2 { display: block; animation: boing .45s ease; }
  .both { display: none; max-width: 420px; margin: 10px auto 0; padding: 12px 14px; border-radius: 18px; background: #fff; color: #9a5a00;
    font-size: 16px; font-weight: 900; line-height: 1.45; }
  .game[data-tried="both"] .both { display: block; animation: boing .5s ease; }
""",
    dark="""  html[data-theme="dark"] .htag { background: #2b2d3a; color: #ffcf9a; }
  html[data-theme="dark"] .road { background: linear-gradient(#2c3c55 0 62%, #2f4a2c 62%); }
  html[data-theme="dark"] .game .b-give { background: #4a3c12; color: #ffe39a; }
  html[data-theme="dark"] .both { background: #2b2d3a; color: #ffd27a; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var bar = g.querySelector('.wt-bar i'), num = g.querySelector('.wt-n'), tried = {}, timer = 0, busy = false;
  function set(k, v) { g.setAttribute('data-' + k, String(v)); }
  function reset() { clearTimeout(timer); clearInterval(busy); busy = false; set('go', 0); bar.style.width = '0'; num.textContent = '0'; }
  g.querySelector('.b-tag').addEventListener('click', function () {
    reset(); set('tag', g.getAttribute('data-tag') === '1' ? 0 : 1);
  });
  g.querySelector('.b-give').addEventListener('click', function () {
    reset();
    var tag = g.getAttribute('data-tag') === '1';
    setTimeout(function () {
      set('go', 1);
      if (tag) {
        bar.style.width = '92%';
        var n = 0; busy = setInterval(function () { n = Math.min(92, n + 8); num.textContent = String(n); }, 190);
      }
      timer = setTimeout(function () {
        clearInterval(busy); busy = false;
        set('go', 2); num.textContent = tag ? '92' : '0';
        tried[tag ? 'a' : 'b'] = 1; if (tried.a && tried.b) set('tried', 'both');
        var w = g.querySelector('.walker').getBoundingClientRect();
        if (!tag && window.pengessoPop) window.pengessoPop(w.left + w.width / 2, w.top + w.height / 2, ['☀️', '🐧', '💛', '✨'], 16);
      }, 2300);
    }, 60);
  });
})();
""",
    ja={
        "Tag or no tag?": "札を付ける？外す？",
        "Give the same gift two times: once with the tag, once without. Watch the way home.": "同じプレゼントを2回わたしてみてね。札ありと、札なし。帰り道を見ていて。",
        "🏷 \"You owe me one!\"": "🏷「お返しよろしくね！」",
        "✂️ Take off the tag": "✂️ 札を外す",
        "🏷 Put the tag back on": "🏷 札を付けなおす",
        "⏳ \"Not yet…?\" meter": "⏳「まだかな…？」メーター",
        "🎁 Give it": "🎁 わたす",
        "Your friend is busy today and may not say thank you.": "友達は今日いそがしくて、お礼を言わないかもしれません。",
        "☁️ \"Did they notice? Not yet…\" The cloud follows you all the way home.": "☁️「気づいたかな？まだかな…」家までずっと、雲がついてきます。",
        "☀️ You gave it, and that is the end. You skip all the way home.": "☀️ わたしたら、そこでおしまい。家までスキップで帰れます。",
        "🐧 The same gift. But your heart feels so different.": "🐧 同じプレゼント。でも、心の重さがこんなにちがう。",
    },
)
build(d)
