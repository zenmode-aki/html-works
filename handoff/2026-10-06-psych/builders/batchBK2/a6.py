from gen import build

CARDS = [
    ("fl", "✏️", "A typo in my message", "メッセージの誤字"),
    ("imp", "🍼", "Feed the baby", "赤ちゃんにミルク"),
    ("fl", "👟", "What people thought of my shoes", "みんなが私の靴をどう思ったか"),
    ("fl", "📱", "My post got only 3 likes", "投稿のいいねが3つだけ"),
    ("imp", "🏠", "Pay the rent", "家賃を払う"),
    ("fl", "🍽️", "I said \"You too!\" when the waiter said \"Enjoy your meal.\"", "店員さんの「ごゆっくりどうぞ」に「そちらも！」と返した"),
    ("fl", "🌂", "I forgot my umbrella", "傘を忘れた"),
]
DECK = "\n".join(
    f'        <div class="wc" data-k="{k}"><span class="wc-e" aria-hidden="true">{e}</span><span class="wc-t">{en.replace(chr(34), "&quot;")}</span></div>'
    for k, e, en, _ in CARDS)
PINS = "".join(f'<span class="be" aria-hidden="true">{e}</span>' for _, e, _, _ in CARDS)

d = dict(
    slug="the-ruler-changes", seq=567, path="nobigdeal",
    title=("Important things stay important, and only the ruler changes",
           "大事なことは大事なまま。変わるのは「ものさし」"),
    label=("The Ruler", "ものさし"),
    h1_emoji="📏",
    alt="A chubby matte plastic model kit penguin holding a realistic yellow tape measure, with a few balloons floating up behind",
    section="⑧「宇宙から見れば、ちっぽけ」",
    message="ちっぽけでも、大事なことは大事なまま。変わるのはものさし。新しいものさしなら、悩みの99%は悩む価値がない。",
    tone="素材の重さ：真面目（不安・悩み）\n→ 見せ方：ポップに（空色と赤い風船。悩みの仕分けで遊べる）",
    game_ja="📏 宇宙のものさしで仕分け：悩みのカードが1枚ずつ出てくる（誤字・赤ちゃんにミルク・靴・いいね3つ・家賃・「ごゆっくり」に「そちらも！」・傘を忘れた）。「📌 大事なまま」か「🎈 飛ばす」を押す。大事なものは左のボードにピンでとまり、小さな悩みは風船で空へ飛んでいく。迷って小さな悩みを「大事」にしても、宇宙のものさしが「ちっぽけ！」と測って飛ばしてくれる。最後は「7枚のうち5つが飛んでいった。大事なことは残った」。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made as a matte plastic model kit, "
            "holding out a realistic yellow tape measure and looking at it with a calm smile, two red balloons floating up softly behind it. "
            "Bright simple sky-blue background with soft clouds giving depth. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × マットなプラモデル × メジャー（巻き尺）",
    mood=["lift", "think"], tags=["books", "mindset", "feelings"],
    pal=dict(bg="#f0f8ff", muted="#5c7088", acc="#1f7bd6", acc2="#ff5a5f", shadow="rgba(30,90,160,.16)",
             r1="rgba(255,90,95,.20)", r2="rgba(31,123,214,.20)", r3="rgba(255,200,60,.18)",
             h1="#132f4d", photo="#ddeeff", big="#1a69b8", bigdark="#9fd0ff",
             game="linear-gradient(160deg, #36a3f7 0%, #1f7bd6 55%, #ff7a7f 100%)"),
    cards=[
        dict(emoji="🌌", label=("Not Nothing", "どうでもよくはない"),
             s=[("Being tiny in the universe does not mean that nothing is important.",
                 "宇宙から見ればちっぽけ、と言っても、何も大事じゃなくなるわけではありません。")]),
        dict(emoji="🍼", label=("Still Important", "大事なまま"),
             s=[("Feeding a baby and paying the rent stay important.",
                 "赤ちゃんにミルクをあげることや、家賃を払うことは、大事なままです。")]),
        dict(emoji="📏", label=("New Ruler", "新しいものさし"),
             s=[("What changes is the ruler that measures what is important.",
                 "変わるのは、「何が大事か」を測るものさしです。")]),
        dict(emoji="🎈", label=("99 Percent", "99%"), big=True,
             s=[("Oliver Burkeman says that with the new ruler, 99% of our worries are not worth worrying about.",
                 "オリバー・バークマンさんによると、新しいものさしで測ると、悩みの99%は、悩む価値がないそうです。")]),
    ],
    game_after=3,
    game_note="宇宙のものさしで仕分け（大事なまま／飛ばす）",
    game_html="""  <section class="game" data-s="play" data-m="hint" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Sort your worries with the universe ruler</div>
    <div class="bins">
      <div class="bin pin"><div class="bin-h">📌 Still important</div><div class="bes">""" + PINS + """</div></div>
      <div class="bin sky"><div class="bin-h">🎈 Floated away</div><div class="bes">""" + PINS + """</div></div>
    </div>
    <div class="deck">
""" + DECK + """
      <div class="deck-end"><span class="de-e" aria-hidden="true">📏</span></div>
    </div>
    <div class="msgs">
      <div class="m-hint">Is it still important, even from space?</div>
      <div class="m-okimp">📌 Yes. That one stays.</div>
      <div class="m-okfl">🎈 Bye-bye, little worry!</div>
      <div class="m-fiximp">📌 Wait! This one stays important. Even the universe agrees.</div>
      <div class="m-fixfl">📏 The universe ruler says: tiny! Let it float. 🎈</div>
      <div class="m-end"><span class="e1">All sorted!</span> <span class="nf">0</span> <span class="e2">worries floated away, and the important things stayed. 📏</span></div>
    </div>
    <div class="ctrl">
      <button type="button" class="btn b-imp">📌 Still important</button>
      <button type="button" class="btn b-fl">🎈 Let it float away</button>
    </div>
    <div class="ctrl2"><button type="button" class="btn ghost b-reset">↺ Sort again</button></div>
  </section>""",
    css="""
  /* 📏 宇宙のものさしで仕分け */
  .bins { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 440px; margin: 14px auto 0; }
  .bin { min-height: 82px; padding: 8px; border-radius: 18px; }
  .pin { background: #fff4d6; color: #5a3d00; }
  .sky { background: linear-gradient(180deg, #d7efff, #f2faff); color: #164a7a; }
  .bin-h { font-size: 13.5px; font-weight: 900; line-height: 1.25; }
  .bes { display: flex; flex-wrap: wrap; justify-content: center; gap: 2px; min-height: 34px; margin-top: 6px; }
  .game .bes .be { display: none; font-size: 24px; line-height: 1.2; }
  .game .bes .be.on { display: inline-block; animation: boing .5s ease; }
  .game .sky .be.on { animation: drift 2.4s ease-in-out infinite alternate; }
  @keyframes drift { from { transform: translateY(2px); } to { transform: translateY(-4px); } }
  .deck { position: relative; height: 150px; max-width: 360px; margin: 14px auto 0; }
  .wc { position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; padding: 12px 16px;
    border-radius: 22px; background: #fff; color: #23324a; box-shadow: 0 8px 0 rgba(0,0,0,.15); opacity: 0; pointer-events: none; transform: scale(.9) translateY(10px); }
  .wc.cur { opacity: 1; transform: none; transition: opacity .3s ease, transform .35s cubic-bezier(.3,1.5,.5,1); }
  .wc.up { opacity: 0; transform: translateY(-140px) scale(.5) rotate(8deg); transition: opacity .7s ease, transform .8s ease-in; }
  .wc.left { opacity: 0; transform: translate(-120px, -60px) scale(.4); transition: opacity .5s ease, transform .5s ease-in; }
  .wc-e { font-size: 40px; line-height: 1; }
  .wc-t { font-size: 18px; font-weight: 900; line-height: 1.35; }
  .deck-end { position: absolute; inset: 0; display: grid; place-items: center; opacity: 0; transition: opacity .4s ease; }
  .de-e { font-size: 70px; }
  .game[data-s="end"] .deck-end { opacity: 1; }
  .msgs { min-height: 54px; margin-top: 12px; }
  .msgs > div { display: none; font-size: 16px; font-weight: 900; line-height: 1.45; padding: 4px; }
  .game[data-m="hint"] .m-hint, .game[data-m="okimp"] .m-okimp, .game[data-m="okfl"] .m-okfl, .game[data-m="fiximp"] .m-fiximp,
  .game[data-m="fixfl"] .m-fixfl, .game[data-m="end"] .m-end { display: block; animation: boing .45s ease; }
  .nf { display: inline-block; padding: 0 8px; border-radius: 999px; background: rgba(255,255,255,.28); }
  .ctrl { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-top: 4px; }
  .ctrl .btn { flex: 1 1 140px; max-width: 210px; min-height: 58px; }
  .b-imp { background: #fff4d6; color: #5a3d00; }
  .b-fl { background: #fff; color: #164a7a; }
  .game[data-s="end"] .ctrl { display: none; }
  .ctrl2 { margin-top: 10px; min-height: 48px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
  .game[data-s="play"] .b-reset { visibility: hidden; }
""",
    dark="""  html[data-theme="dark"] .pin { background: #4a3c12; color: #ffe39a; }
  html[data-theme="dark"] .sky { background: linear-gradient(180deg, #1d3a57, #22303f); color: #cfe8ff; }
  html[data-theme="dark"] .wc { background: #22242f; color: #eef4ff; }
  html[data-theme="dark"] .game .b-imp { background: #4a3c12; color: #ffe39a; }
  html[data-theme="dark"] .game .b-fl { background: #2b2d3a; color: #cfe8ff; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var cards = [].slice.call(g.querySelectorAll('.wc'));
  var pins = [].slice.call(g.querySelectorAll('.pin .be')), sky = [].slice.call(g.querySelectorAll('.sky .be'));
  var i = 0, nf = 0, busy = false;
  function msg(m) { g.setAttribute('data-m', ''); void g.offsetWidth; g.setAttribute('data-m', m); }
  function reset() {
    i = 0; nf = 0; busy = false;
    cards.forEach(function (c, k) { c.className = 'wc' + (k === 0 ? ' cur' : ''); });
    pins.concat(sky).forEach(function (b) { b.classList.remove('on'); });
    g.setAttribute('data-s', 'play'); msg('hint');
  }
  function pick(choice) {
    if (busy || g.getAttribute('data-s') !== 'play') return;
    var c = cards[i], k = c.getAttribute('data-k');
    msg(k === choice ? (k === 'imp' ? 'okimp' : 'okfl') : (k === 'imp' ? 'fiximp' : 'fixfl'));
    busy = true;
    c.classList.remove('cur'); c.classList.add(k === 'imp' ? 'left' : 'up');
    (k === 'imp' ? pins : sky)[i].classList.add('on');
    if (k === 'fl') {
      nf++;
      if (window.pengessoPop) { var r = c.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + 20, ['🎈'], 6); }
    }
    setTimeout(function () {
      i++; busy = false;
      if (i < cards.length) { cards[i].classList.add('cur'); return; }
      g.querySelector('.nf').textContent = nf;
      g.setAttribute('data-s', 'end'); msg('end');
      if (window.pengessoPop) { var r = g.querySelector('.deck').getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🎈', '📏', '🐧', '✨'], 18); }
    }, 650);
  }
  g.querySelector('.b-imp').addEventListener('click', function () { pick('imp'); });
  g.querySelector('.b-fl').addEventListener('click', function () { pick('fl'); });
  g.querySelector('.b-reset').addEventListener('click', reset);
  reset();
})();
""",
    ja=dict({
        "Sort your worries with the universe ruler": "宇宙のものさしで、悩みを仕分けしよう",
        "📌 Still important": "📌 大事なまま",
        "🎈 Floated away": "🎈 飛んでいった",
        "Is it still important, even from space?": "宇宙から見ても、まだ大事？",
        "📌 Yes. That one stays.": "📌 うん。それは残そう。",
        "🎈 Bye-bye, little worry!": "🎈 バイバイ、小さな悩み！",
        "📌 Wait! This one stays important. Even the universe agrees.": "📌 待って！これは大事なまま。宇宙もそう言ってるよ。",
        "📏 The universe ruler says: tiny! Let it float. 🎈": "📏 宇宙のものさしで測ると…ちっぽけ！飛ばしちゃおう 🎈",
        "All sorted!": "仕分け完了！",
        "worries floated away, and the important things stayed. 📏": "個の悩みが飛んでいって、大事なことは残った 📏",
        "🎈 Let it float away": "🎈 飛ばす",
        "↺ Sort again": "↺ もう一回",
    }, **{en: ja for _, _, en, ja in CARDS}),
)

if __name__ == "__main__":
    build(d)
