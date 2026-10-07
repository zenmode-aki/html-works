from gen import build

d = dict(
    slug="holding-on-makes-it-hurt", seq=533,
    title=("Holding on too tight is what makes it hurt",
           "強くにぎりしめるほど、苦しくなる"),
    label=("Loose Grip", "ゆるくにぎる"),
    h1_emoji="🎈",
    alt="A chubby crocheted amigurumi penguin loosely holding the string of a real red balloon that sways in a light breeze",
    section="「反応しない心」",
    message="苦しさは「自分のもの」へのこだわりから。物も夢も関係も変わっていくので、ふわっと持つくらいがちょうどいい。",
    tone="素材の重さ：ふつう（こだわりの話）\n→ 見せ方：ポップに（空色とさくらんぼ色。風船をにぎる強さを変えて、風が吹いたときの痛さをくらべる）",
    game_ja="🎈 にぎる強さ：ペンギンが風船（お気に入りのマグカップ／夢／友達との関係）のひもを持っている。「－」「＋」でにぎる強さを4段階で変えて、「🌬 風が吹く（変わるとき）」を押す。ぎゅっとにぎっていると、ペンギンが引っぱられて「いたい」メーターがぐんと上がる。ふわっと持っていると、風船はゆれるだけで、いたさはほとんどない。風船の中身は押すたびに変わる。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of crocheted amigurumi yarn, "
            "standing relaxed and loosely holding the string of a realistic shiny red rubber balloon that sways gently in a light breeze. "
            "Bright simple sky blue background with soft white clouds, soft depth and gentle sunshine. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × あみぐるみ × 赤い風船",
    mood=["lift", "think"], tags=["psychology", "mindset", "feelings"],
    pal=dict(bg="#f2f9ff", muted="#5f7590", acc="#2f7fe0", acc2="#ff5d73", shadow="rgba(47,127,224,.16)",
             r1="rgba(120,190,255,.32)", r2="rgba(255,93,115,.14)", r3="rgba(255,214,90,.18)",
             h1="#15325a", photo="#dcecff", big="#2565b8", bigdark="#a9cdff",
             game="linear-gradient(170deg, #59b6ff 0%, #4f86f0 55%, #8a6cff 100%)"),
    cards=[
        dict(emoji="🪢", label=("The Cause", "原因"),
             s=[("It is said the cause of pain is holding on to \"things that are mine.\"",
                 "苦しさの原因は、「自分のもの」へのこだわりだそうです。")]),
        dict(emoji="🍂", label=("Things Change", "変わっていく"),
             s=[("Things, dreams, and relationships with people change little by little as time passes.",
                 "物も、夢も、人との関係も、時間がたつと少しずつ変わります。"),
                ("The tighter you hold them, the more it hurts when they change.",
                 "強くにぎりしめるほど、変わったときに痛くなります。")]),
        dict(emoji="🎈", label=("Hold Softly", "ふわっと持つ"), big=True,
             s=[("Maybe it is just right to hold them softly.",
                 "ふわっと持っておくくらいが、ちょうどいいのかもしれません。")]),
    ],
    game_after=2,
    game_note="にぎる強さ（ぎゅっとにぎるほど、風が吹いたときに痛い）",
    game_html="""  <section class="game" data-g="1" data-w="0" data-t="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">How tight is your grip?</div>
    <div class="game-hint">Choose your grip. Then let the wind blow. The wind is "change."</div>
    <div class="sky">
      <div class="bal"><span class="bal-e">🎈</span><span class="tag"><span class="tg0">☕ My favorite mug</span><span class="tg1">🌠 My dream</span><span class="tg2">🤝 A friendship</span></span></div>
      <div class="str" aria-hidden="true"></div>
      <div class="pen"><span class="pen-e">🐧</span><span class="sweat">💦</span></div>
      <div class="gust" aria-hidden="true"><span class="gust-e">🌬️</span></div>
    </div>
    <div class="grip">
      <button type="button" class="btn sq b-minus" aria-label="Softer">－</button>
      <div class="glv">
        <span class="gl1">🪶 Very soft</span><span class="gl2">🤲 Soft</span><span class="gl3">✊ Tight</span><span class="gl4">🔒 Very tight</span>
        <span class="dots" aria-hidden="true"><i></i><i></i><i></i><i></i></span>
      </div>
      <button type="button" class="btn sq b-plus" aria-label="Tighter">＋</button>
    </div>
    <div class="ouch">
      <div class="ou-head"><span class="ou-l">😣 Ouch meter</span> <span class="ou-n">0</span></div>
      <div class="ou-bar" aria-hidden="true"><i></i></div>
    </div>
    <button type="button" class="btn b-wind">🌬️ The wind blows (things change)</button>
    <div class="res">
      <div class="rs0">Things change. How will your grip feel?</div>
      <div class="rs1">😌 It sways, but you are OK. You can enjoy it while it is here.</div>
      <div class="rs2">😣 Ouch! It pulls you. Holding tight hurts when things change.</div>
    </div>
  </section>""",
    css="""
  /* 🎈 にぎる強さ */
  .sky { position: relative; height: 230px; max-width: 420px; margin: 14px auto 0; border-radius: 24px; overflow: hidden;
    background: linear-gradient(#bfe3ff, #eaf6ff); }
  .bal { position: absolute; left: 50%; top: 14px; width: 150px; margin-left: -75px; display: grid; justify-items: center; gap: 2px;
    transform-origin: 50% 160px; transition: transform .6s cubic-bezier(.3,1.4,.5,1); }
  .game .bal-e { font-size: 64px; line-height: 1; }
  .tag { display: block; padding: 3px 10px; border-radius: 999px; background: #fff; color: #23406a; font-size: 13.5px; font-weight: 900; line-height: 1.35; }
  .tag > span { display: none; }
  .game[data-t="0"] .tg0, .game[data-t="1"] .tg1, .game[data-t="2"] .tg2 { display: inline; }
  .str { position: absolute; left: 50%; top: 104px; width: 3px; height: 64px; margin-left: -1px; background: #fff; border-radius: 3px;
    transform-origin: 50% 100%; transition: transform .6s cubic-bezier(.3,1.4,.5,1); }
  .pen { position: absolute; left: 50%; bottom: 8px; width: 70px; margin-left: -35px; text-align: center; transition: transform .5s ease; }
  .game .pen-e { font-size: 52px; line-height: 1; }
  .game .sweat { position: absolute; right: -4px; top: -4px; font-size: 22px; opacity: 0; transition: opacity .3s ease; }
  .game .gust { position: absolute; left: 6px; top: 70px; font-size: 40px; opacity: 0; transform: translateX(-40px); transition: opacity .3s ease, transform .6s ease; }
  .game[data-w="1"] .gust, .game[data-w="2"] .gust { opacity: 1; transform: translateX(10px); }
  .game[data-w="1"] .bal { transform: rotate(16deg); }
  .game[data-w="1"] .str { transform: rotate(14deg); }
  .game[data-w="2"] .bal { transform: rotate(24deg) translateX(10px); }
  .game[data-w="2"] .str { transform: rotate(22deg); background: #ff5d73; }
  .game[data-w="2"] .pen { transform: translateX(28px) rotate(12deg); animation: shake .45s ease 2; }
  .game[data-w="2"] .sweat { opacity: 1; }
  .grip { display: grid; grid-template-columns: 56px 1fr 56px; align-items: center; gap: 10px; max-width: 420px; margin: 14px auto 0; }
  .btn.sq { min-height: 56px; padding: 0; font-size: 26px; }
  .glv { padding: 8px 6px; border-radius: 18px; background: rgba(255,255,255,.2); font-size: 16px; font-weight: 900; line-height: 1.3; }
  .glv > span:not(.dots) { display: none; }
  .game[data-g="1"] .gl1, .game[data-g="2"] .gl2, .game[data-g="3"] .gl3, .game[data-g="4"] .gl4 { display: block; }
  .dots { display: flex; justify-content: center; gap: 6px; margin-top: 6px; }
  .dots i { width: 22px; height: 8px; border-radius: 999px; background: rgba(255,255,255,.35); }
  .game[data-g="1"] .dots i:nth-child(-n+1), .game[data-g="2"] .dots i:nth-child(-n+2),
  .game[data-g="3"] .dots i:nth-child(-n+3), .game[data-g="4"] .dots i:nth-child(-n+4) { background: #fff; }
  .game[data-g="3"] .dots i:nth-child(-n+3), .game[data-g="4"] .dots i:nth-child(-n+4) { background: #ffd0d7; }
  .ouch { max-width: 420px; margin: 12px auto 0; padding: 10px 14px; border-radius: 18px; background: rgba(255,255,255,.18); }
  .ou-head { display: flex; justify-content: space-between; font-size: 15px; font-weight: 900; }
  .ou-bar { position: relative; height: 14px; margin-top: 6px; border-radius: 999px; background: rgba(255,255,255,.3); overflow: hidden; }
  .ou-bar i { position: absolute; inset: 0 auto 0 0; width: 0; border-radius: 999px; background: #ff5d73; transition: width .6s cubic-bezier(.2,1.3,.4,1); }
  .b-wind { margin-top: 14px; width: min(360px, 100%); min-height: 60px; font-size: 17px; background: #fff3c4; color: #5a3d00; }
  .res { max-width: 420px; margin: 12px auto 0; min-height: 50px; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .res > div { display: none; }
  .game[data-w="0"] .rs0, .game[data-w="1"] .rs1, .game[data-w="2"] .rs2 { display: block; }
  .game[data-w="1"] .rs1, .game[data-w="2"] .rs2 { animation: boing .45s ease; }
""",
    dark="""  html[data-theme="dark"] .sky { background: linear-gradient(#26364f, #34465f); }
  html[data-theme="dark"] .tag { background: #22242f; color: #d6e6ff; }
  html[data-theme="dark"] .game .b-wind { background: #4a3c12; color: #ffe39a; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var grip = 1, t = 0, bar = g.querySelector('.ou-bar i'), num = g.querySelector('.ou-n'), PAIN = [0, 5, 15, 65, 100];
  function set(k, v) { g.setAttribute('data-' + k, String(v)); }
  function calm() { set('w', 0); bar.style.width = '0'; num.textContent = '0'; }
  function setGrip(v) {
    grip = Math.max(1, Math.min(4, v)); set('g', grip); calm();
    g.querySelector('.b-minus').disabled = grip === 1; g.querySelector('.b-plus').disabled = grip === 4;
  }
  g.querySelector('.b-minus').addEventListener('click', function () { setGrip(grip - 1); });
  g.querySelector('.b-plus').addEventListener('click', function () { setGrip(grip + 1); });
  g.querySelector('.b-wind').addEventListener('click', function () {
    set('w', 0);
    setTimeout(function () {
      var p = PAIN[grip];
      set('w', grip >= 3 ? 2 : 1);
      bar.style.width = p + '%'; num.textContent = String(p);
      var b = g.querySelector('.bal').getBoundingClientRect();
      if (window.pengessoPop) window.pengessoPop(b.left + b.width / 2, b.top + 40, grip >= 3 ? ['💦', '🎈'] : ['🎈', '✨', '🐧'], grip >= 3 ? 8 : 12);
      setTimeout(function () { t = (t + 1) % 3; set('t', t); }, 1600);
    }, 60);
  });
  setGrip(1);
})();
""",
    ja={
        "How tight is your grip?": "どのくらい、ぎゅっとにぎる？",
        "Choose your grip. Then let the wind blow. The wind is \"change.\"": "にぎる強さを選んでから、風を吹かせてみてね。風は「変化」です。",
        "☕ My favorite mug": "☕ お気に入りのマグカップ",
        "🌠 My dream": "🌠 私の夢",
        "🤝 A friendship": "🤝 友達との関係",
        "Softer": "ゆるく",
        "Tighter": "強く",
        "🪶 Very soft": "🪶 とてもふわっと",
        "🤲 Soft": "🤲 ふわっと",
        "✊ Tight": "✊ ぎゅっと",
        "🔒 Very tight": "🔒 ぎゅうぎゅう",
        "😣 Ouch meter": "😣 いたいメーター",
        "🌬️ The wind blows (things change)": "🌬️ 風が吹く（変わるとき）",
        "Things change. How will your grip feel?": "物ごとは変わります。にぎる手は、どう感じるかな？",
        "😌 It sways, but you are OK. You can enjoy it while it is here.": "😌 ゆれるけど、だいじょうぶ。ここにあるあいだ、楽しめます。",
        "😣 Ouch! It pulls you. Holding tight hurts when things change.": "😣 いたっ！引っぱられる。ぎゅっとにぎっていると、変わるときに痛い。",
    },
)
build(d)
