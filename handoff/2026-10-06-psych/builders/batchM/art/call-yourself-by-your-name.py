A = dict(
    slug="call-yourself-by-your-name", seq=420,
    title="When you feel angry, call yourself by your name to calm down",
    title_ja="腹が立ったら、自分を名前で呼んでみると落ち着ける",
    label="Say Your Name", label_ja="名前で呼ぶ",
    float="🔥",
    alt="A chubby crocheted penguin looking calmly at a real small desk globe",
    mood=["lift"], tags=["psychology", "feelings", "tips"],
    src_no="98", src_title="セルフトーク（サードパーソン・セルフトーク）",
    center="腹が立ったら「私」ではなく自分の名前で話しかける。少し離れたところから自分を見られて、落ち着きやすい。",
    tone="素材の重さ：真面目（怒り・セルフトーク）\n→ 見せ方：ポップに（熱いコーラルから、落ち着いた青緑へ。名前スイッチでカメラが引いていく）",
    tone_css="真面目な話 → ポップに。コーラルから青緑へ",
    game_name="名前スイッチ",
    play="🔥 名前スイッチ：新しい白いシャツにコーヒーをこぼして、ペンギンの頭の上で 🔥 が燃えている（怒り 90%）。「😤『私、ムカつく！』と言う」を押すと、カメラがぐっと寄って 🔥 が大きくなり、怒りが上がる。「🐧 名前で言ってみる」を押すたびに、カメラが1段ずつ引いていく（アップ → 部屋 → 街 → 空）。セリフも「ペンゲッソ、いま怒ってるね」→「ただのコーヒーだよ。シャツは洗える」→「空から見たら小さなしみだ 🌏」と変わり、🔥 が小さくなって、背景が熱いコーラルから青緑に。空まで引くと「😌 落ち着いた。同じコーヒーなのに」🎉。",
    prompt="An extremely cute, chubby round penguin with a gentle face and a plain white belly (no rings or patterns on the belly), made of crocheted amigurumi yarn with visible soft stitches, sitting peacefully and looking with a calm, gentle smile at one realistic small desk globe on a polished wooden stand. Bright background that fades from soft warm coral at the top to a calm teal blue at the bottom with gentle depth, simple and uncluttered. Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering.",
    combo="ペンギン × あみぐるみ × 地球儀",
    pal=dict(bg="#fff6f2", text="#2e2433", muted="#7a6a76", a="#e8503a", b="#2a9d8f", c="#e9c46a", d="#5e60ce",
             big="#1f8577", bigdark="#9ee6dc", h1="#33202a", ink="#2e2433", shadowc="rgba(200,80,60,.15)",
             bg1="rgba(255,123,84,.22)", bg2="rgba(42,157,143,.16)", bg3="rgba(94,96,206,.12)", photo="#ffe6df",
             game="linear-gradient(160deg, #ff7b54 0%, #f0506e 45%, #8a4fd8 100%)"),
    cards=[
        dict(e="🔥", l="Into The Fire", lj="怒りの中へ", s=[(
            'When you get angry and say, "I am so mad!", you go deep into the anger.',
            "腹が立ったときに「私、ムカつく！」と言うと、怒りの中にどっぷり入ってしまいます。", False)]),
        dict(e="🏷️", l="Your Name", lj="名前で呼ぶ", s=[(
            "At times like that, try calling yourself by your name.",
            "そんなときは、自分を名前で呼んでみます。", False)]),
        dict(e="🐧", l="Like This", lj="こんなふうに", s=[(
            '"Pengesso, you are angry right now."',
            "「ペンゲッソ、いま怒ってるね」。", False)]),
        "GAME",
        dict(e="🔭", l="A Little Far", lj="少し離れて", s=[(
            "Research says you start to see yourself from a little far away, so you calm down more easily.",
            "少し離れたところから自分を見ているようになるので、落ち着きやすくなるという研究があります。", False)]),
        dict(e="✨", l="Just Swap", lj="変えるだけ", s=[(
            'You only change "I" to your name.',
            "「私」を名前に変えるだけです。", True)]),
    ],
    game_html=r'''
  <!-- ⚡ 触って遊べる部品：名前スイッチ（名前で話しかけるたびにカメラが引いて、🔥 が小さくなる） -->
  <section class="game" data-z="0" data-b="0" data-done="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">The name switch</div>
    <div class="game-hint">Oops! Coffee on your new white shirt. ☕</div>
    <div class="view">
      <div class="zoom-tag"><span class="z0">📷 Close-up</span><span class="z1">🛋️ Room</span><span class="z2">🏙️ Town</span><span class="z3">☁️ Sky</span></div>
      <div class="world" aria-hidden="true">
        <span class="it r3" style="left:8%;top:10%">☁️</span><span class="it r3" style="left:76%;top:6%">☁️</span><span class="it r3" style="left:46%;top:2%">🕊️</span>
        <span class="it r3" style="left:4%;top:80%">⛰️</span><span class="it r3" style="left:82%;top:78%">🌲</span>
        <span class="it r2" style="left:18%;top:28%">🏠</span><span class="it r2" style="left:70%;top:26%">🏢</span>
        <span class="it r2" style="left:20%;top:68%">🌳</span><span class="it r2" style="left:72%;top:66%">🚲</span>
        <span class="it r1" style="left:32%;top:40%">🪴</span><span class="it r1" style="left:60%;top:56%">🛋️</span>
        <span class="me"><span class="fire">🔥</span><span class="pg">🐧</span><span class="cup">☕</span></span>
      </div>
    </div>
    <div class="bubble">
      <span class="b0">Argh! My new shirt! I am SO mad!!</span>
      <span class="b4">I am SO mad!! Why me?! 😤</span>
      <span class="b1">Pengesso, you are angry right now.</span>
      <span class="b2">Pengesso, it is only coffee. Shirts can be washed.</span>
      <span class="b3">Pengesso, from the sky, it is a tiny spot. 🌏</span>
    </div>
    <div class="temp"><span class="t-l">🌡️ Anger:</span> <span class="t-bar" aria-hidden="true"><i></i></span> <span class="t-n">90</span><span class="t-u">%</span></div>
    <div class="ctrl">
      <button type="button" class="btn b-i">😤 Say "I am so mad!"</button>
      <button type="button" class="btn b-name">🐧 Say it with my name</button>
    </div>
    <div class="msg m-done">😌 Calm. Same coffee, but now you watch from a little far away.</div>
  </section>
''',
    game_ja={
        "The name switch": "名前スイッチ",
        "Oops! Coffee on your new white shirt. ☕": "あっ！新しい白いシャツにコーヒーが。☕",
        "📷 Close-up": "📷 アップ",
        "🛋️ Room": "🛋️ 部屋",
        "🏙️ Town": "🏙️ 街",
        "☁️ Sky": "☁️ 空",
        "Argh! My new shirt! I am SO mad!!": "あー！新しいシャツが！私、超ムカつく！！",
        "I am SO mad!! Why me?! 😤": "私、超ムカつく！！なんで私が！？😤",
        "Pengesso, you are angry right now.": "ペンゲッソ、いま怒ってるね。",
        "Pengesso, it is only coffee. Shirts can be washed.": "ペンゲッソ、ただのコーヒーだよ。シャツは洗えるよ。",
        "Pengesso, from the sky, it is a tiny spot. 🌏": "ペンゲッソ、空から見たら小さなしみだね。🌏",
        "🌡️ Anger:": "🌡️ 怒り：",
        "😤 Say \"I am so mad!\"": "😤「私、ムカつく！」と言う",
        "🐧 Say it with my name": "🐧 名前で言ってみる",
        "😌 Calm. Same coffee, but now you watch from a little far away.": "😌 落ち着いた。同じコーヒーなのに、今は少し離れたところから見ています。",
    },
    css=r'''
  /* 🔥 名前スイッチ */
  .game[data-z="2"], .game[data-z="3"] { background: linear-gradient(160deg, #3fb6a8 0%, #2a9d8f 45%, #5e60ce 100%); }
  .view { position: relative; height: 220px; max-width: 420px; margin: 14px auto 0; border-radius: 24px; overflow: hidden;
    background: linear-gradient(180deg, #dff3ff 0%, #f6fbff 60%, #e6f6e8 100%); }
  .zoom-tag { position: absolute; left: 10px; top: 10px; z-index: 2; padding: 4px 10px; border-radius: 999px; background: rgba(30,30,60,.72); color: #fff; font-size: 12.5px; font-weight: 900; }
  .zoom-tag span { display: none; }
  .game[data-z="0"] .z0, .game[data-z="1"] .z1, .game[data-z="2"] .z2, .game[data-z="3"] .z3 { display: inline; }
  .world { position: absolute; left: 50%; top: 50%; width: 420px; height: 420px; margin: -210px 0 0 -210px;
    transform: scale(1.9); transition: transform .8s cubic-bezier(.3,1.1,.4,1); }
  .game[data-z="1"] .world { transform: scale(1.15); }
  .game[data-z="2"] .world { transform: scale(.78); }
  .game[data-z="3"] .world { transform: scale(.52); }
  .it { position: absolute; font-size: 40px; line-height: 1; }
  .r3 { font-size: 54px; }
  .me { position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); display: grid; justify-items: center; }
  .fire { display: inline-block; font-size: 40px; line-height: 1; transition: font-size .5s ease; }
  .game[data-z="0"] .fire { animation: flick .5s ease-in-out infinite alternate; }
  @keyframes flick { from { transform: scale(1) rotate(-4deg); } to { transform: scale(1.12) rotate(4deg); } }
  .pg { font-size: 44px; line-height: 1; }
  .cup { position: absolute; right: -26px; bottom: 0; font-size: 22px; }
  .bubble { max-width: 420px; min-height: 58px; margin: 12px auto 0; padding: 10px 14px; border-radius: 18px; background: #fff; color: var(--ink);
    display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .bubble span { display: none; }
  .game[data-b="0"] .b0, .game[data-b="1"] .b1, .game[data-b="2"] .b2, .game[data-b="3"] .b3, .game[data-b="4"] .b4 { display: inline; animation: g-in .3s ease-out; }
  .game[data-b="0"] .bubble, .game[data-b="4"] .bubble { color: #c92a2a; }
  .temp { display: flex; align-items: center; justify-content: center; gap: 8px; max-width: 420px; margin: 12px auto 0; font-size: 15px; font-weight: 900; }
  .t-bar { position: relative; flex: 1; max-width: 200px; height: 14px; border-radius: 999px; background: rgba(255,255,255,.3); overflow: hidden; }
  .t-bar i { position: absolute; inset: 0 auto 0 0; width: 90%; border-radius: 999px; background: linear-gradient(90deg, #ffe066, #ff3b3b); transition: width .5s ease; }
  .t-n, .t-u { font-variant-numeric: tabular-nums; }
  .b-i { color: #c92a2a; }
  .b-name { color: #1f7a6e; }
  .m-done { display: none; }
  .game[data-done="1"] .m-done { display: block; animation: g-pop .45s cubic-bezier(.2,1.4,.4,1); }
''',
    dark=r'''
  html[data-theme="dark"] .view { background: linear-gradient(180deg, #cfe6f5 0%, #e8f0f6 60%, #d6ead8 100%); }
  html[data-theme="dark"] .bubble { background: #f1edf8; }
''',
    js=r'''
/* 🔥 名前スイッチ：JS は data-*・style（🔥 の大きさ・メーター）・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var fire = g.querySelector('.fire'), bar = g.querySelector('.t-bar i'), tn = g.querySelector('.t-n');
  var z = 0, anger = 90;
  function paint() {
    g.setAttribute('data-z', String(z));
    fire.style.fontSize = Math.round(14 + anger * 0.36) + 'px';
    bar.style.width = anger + '%'; tn.textContent = String(anger);
  }
  g.querySelector('.b-i').addEventListener('click', function () {
    z = 0; anger = Math.min(100, anger + 15);
    g.setAttribute('data-b', '4'); g.setAttribute('data-done', '0');
    var v = g.querySelector('.view'); v.classList.remove('shake'); void v.offsetWidth; v.classList.add('shake');
    if (navigator.vibrate) { try { navigator.vibrate(20); } catch (e) {} }
    paint();
  });
  g.querySelector('.b-name').addEventListener('click', function () {
    if (z < 3) z++;
    anger = [90, 60, 35, 12][z];
    g.setAttribute('data-b', String(z));
    paint();
    if (z === 3 && g.getAttribute('data-done') !== '1') {
      g.setAttribute('data-done', '1');
      if (window.pengessoPop) { var r = g.querySelector('.view').getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['😌', '🌏', '🐧', '☁️', '✨'], 20); }
    }
  });
  paint();
})();
''',
)
