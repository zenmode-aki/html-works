Q = [("🧦 My room is messy.", "🧦 部屋がちらかっている。"),
     ("📓 My diary stopped on day 3.", "📓 日記が3日で止まった。"),
     ("🌙 I get lonely easily.", "🌙 すぐさみしくなる。"),
     ("🍰 I cannot stop eating sweets.", "🍰 甘いものがやめられない。"),
     ("☕ People say I am weak and plain.", "☕ 影がうすいと言われる。")]
JOKE = ('"Not weak. Call me Americano!" …Are you coffee?! ☕', "「うすいんじゃなくて、アメリカンと呼んで！」…コーヒーかい！☕")
import html as _h
_q = "\n".join(
    f'      <button type="button" class="q"><span class="q-t">{_h.escape(en, quote=False)}</span>'
    + (f'<span class="joke">{_h.escape(JOKE[0], quote=False)}</span>' if i == 4 else "")
    + '<span class="okst">OK♪</span></button>' for i, (en, ja) in enumerate(Q))

A = dict(
    slug="this-me-is-ok", seq=421,
    title='Even if you are messy, you can say "I am OK as I am"',
    title_ja="だらしなくても三日坊主でも、「このままの自分でOK♪」",
    label="OK As I Am", label_ja="このままでOK",
    float="☕",
    alt="A chubby boucle wool penguin relaxing next to a real mug of americano coffee",
    mood=["lift", "laugh"], tags=["psychology", "feelings", "mindset"],
    src_no="97", src_title="自己受容",
    center="だらしなくても三日坊主でも、良い悪いを決めずに認めて、笑いにする。「このままの自分でOK♪」をくり返す。",
    tone="素材の重さ：真面目（自分を受け入れる）\n→ 見せ方：ポップに（オレンジとピンクとコーヒー色。クセのカードに「OK♪」のハンコを押して遊べる）",
    tone_css="真面目な話 → ポップに。オレンジとコーヒー色",
    game_name="OK♪スタンプ",
    play="💮 OK♪スタンプ：クセのカード5枚（🧦 部屋がちらかっている／📓 日記が3日で止まった／🌙 すぐさみしくなる／🍰 甘いものがやめられない／☕ 影がうすいと言われる）をタップすると、赤い「OK♪」のハンコがドンと押される。1枚押すごとに、上のペンギンの顔が 😣→😕→🙂→😌→😊→🥰 とゆるみ、プルプルしていた体がゆらゆらに変わって、セリフも「全部直さなきゃ…」から「このままの自分でOK♪」へ。☕ のカードだけ、押すと「うすいんじゃなくて、アメリカンと呼んで！」…コーヒーかい！ のオチが出る。5枚で 🥰🎉。「↺ もう一回」。",
    prompt="An extremely cute, chubby round penguin with a gentle face and a plain white belly (no rings or patterns on the belly), made of cozy boucle wool with soft looped texture, leaning back in a relaxed, happy way with half-closed content eyes next to one realistic white ceramic mug of hot americano coffee with gentle steam. Bright warm background in soft orange, peach and a touch of pink with gentle depth, simple and uncluttered. Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering.",
    combo="ペンギン × ブークレウール × アメリカンコーヒー",
    pal=dict(bg="#fff7ef", text="#3a2a24", muted="#80695e", a="#e8590c", b="#8d5a3b", c="#ffd23f", d="#ff4f9a",
             big="#c2410c", bigdark="#ffc6a0", h1="#3a2118", ink="#3a2a24", shadowc="rgba(141,90,59,.16)",
             bg1="rgba(255,79,154,.14)", bg2="rgba(255,210,63,.28)", bg3="rgba(141,90,59,.12)", photo="#ffe9d8",
             game="linear-gradient(155deg, #f59f00 0%, #f76707 45%, #e64980 100%)"),
    cards=[
        dict(e="🧦", l="My Quirks", lj="私のクセ", s=[(
            "Messy, quitting after 3 days, easily lonely, and a little spoiled.",
            "だらしない、三日坊主、さみしがり、甘えん坊。", False)]),
        dict(e="🏷️", l="Just Accept", lj="認めるだけ", s=[(
            'Do not judge it good or bad; just accept, "I have this side."',
            "良い・悪いを決めずに、「私にはこういうところがある」と認めます。", False)]),
        dict(e="☕", l="Laugh It Off", lj="笑いにする", s=[(
            'If you can laugh like "I am not weak, I am an Americano," that is even better.',
            "「私はうすいんじゃなくて、アメリカンなの」みたいに笑いにできたら、もっといいです。", False)]),
        "GAME",
        dict(e="🪄", l="Magic Words", lj="魔法の言葉", s=[(
            'The magic words: "I am OK as I am ♪."',
            "魔法の言葉は、「このままの自分でOK♪」。", True)]),
        dict(e="🔁", l="Say It Again", lj="くり返す", s=[(
            "Even if you cannot think so at first, you slowly can as you repeat it.",
            "最初はそう思えなくても、くり返すうちに、だんだん思えてきます。", False)]),
    ],
    game_html=r'''
  <!-- ⚡ 触って遊べる部品：OK♪スタンプ（クセのカードにハンコを押すたびに、ペンギンがゆるんでいく） -->
  <section class="game" data-lv="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">The "OK♪" stamp</div>
    <div class="game-hint">Tap each quirk and stamp it "OK♪".</div>
    <div class="me">
      <div class="pg-box" aria-hidden="true"><span class="pg">🐧</span><span class="mood">😣</span></div>
      <div class="bubble">
        <span class="s0">I should fix all of these… 😣</span>
        <span class="s1">Hmm. Maybe this is just me.</span>
        <span class="s2">It is OK. That is my style.</span>
        <span class="s3">Ha ha, I am kind of funny.</span>
        <span class="s4">This me is not so bad.</span>
        <span class="s5">I am OK as I am ♪</span>
      </div>
    </div>
    <div class="qs">
QS
    </div>
    <div class="relax"><span class="rl">Relaxed:</span> <span class="rn">0</span>/5</div>
    <div class="msg m-done">🥰 I am OK as I am ♪ Say it again tomorrow, too.</div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Again</button></div>
  </section>
'''.replace("QS", _q),
    game_ja=dict({
        "The \"OK♪\" stamp": "「OK♪」スタンプ",
        "Tap each quirk and stamp it \"OK♪\".": "クセのカードをタップして、「OK♪」のハンコを押そう。",
        "I should fix all of these… 😣": "これ全部、直さなきゃ… 😣",
        "Hmm. Maybe this is just me.": "うーん。これが私なのかも。",
        "It is OK. That is my style.": "まあいいか。それが私のスタイル。",
        "Ha ha, I am kind of funny.": "ははっ、私ってちょっと面白い。",
        "This me is not so bad.": "このままの私も、悪くない。",
        "I am OK as I am ♪": "このままの自分でOK♪",
        "OK♪": "OK♪",
        JOKE[0]: JOKE[1],
        "Relaxed:": "ゆるんだ度：",
        "🥰 I am OK as I am ♪ Say it again tomorrow, too.": "🥰 このままの自分でOK♪ 明日もまた言ってね。",
        "↺ Again": "↺ もう一回",
    }, **dict(Q)),
    css=r'''
  /* 💮 OK♪スタンプ */
  .me { display: flex; align-items: center; gap: 12px; max-width: 420px; margin: 14px auto 0; text-align: left; }
  .pg-box { position: relative; flex: 0 0 auto; width: 84px; height: 84px; display: grid; place-items: center; border-radius: 50%; background: rgba(255,255,255,.25); }
  .pg { font-size: 52px; line-height: 1; display: inline-block; transform-origin: 50% 100%; }
  .mood { position: absolute; right: -6px; top: -6px; font-size: 28px; line-height: 1; display: inline-block; }
  @keyframes tense { 0%, 100% { transform: translateX(0); } 25% { transform: translateX(-2px); } 75% { transform: translateX(2px); } }
  @keyframes sway { 0%, 100% { transform: rotate(-6deg); } 50% { transform: rotate(6deg); } }
  .game[data-lv="0"] .pg, .game[data-lv="1"] .pg { animation: tense .25s linear infinite; }
  .game[data-lv="3"] .pg, .game[data-lv="4"] .pg, .game[data-lv="5"] .pg { animation: sway 2.4s ease-in-out infinite; }
  .bubble { flex: 1; min-width: 0; min-height: 58px; padding: 10px 14px; border-radius: 18px 18px 18px 6px; background: #fff; color: var(--ink);
    display: flex; align-items: center; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .bubble span { display: none; }
  .game[data-lv="0"] .s0, .game[data-lv="1"] .s1, .game[data-lv="2"] .s2, .game[data-lv="3"] .s3, .game[data-lv="4"] .s4, .game[data-lv="5"] .s5 { display: inline; animation: g-in .3s ease-out; }
  .qs { display: grid; gap: 10px; max-width: 400px; margin: 14px auto 0; }
  .q { position: relative; display: block; width: 100%; min-height: 58px; padding: 12px 84px 12px 16px; border: 0; border-radius: 18px; background: #fff; color: var(--ink);
    font: inherit; font-size: 16px; font-weight: 900; line-height: 1.4; text-align: left; cursor: pointer; overflow: hidden;
    box-shadow: 0 5px 0 rgba(0,0,0,.14), 0 10px 18px rgba(0,0,0,.10); -webkit-tap-highlight-color: transparent; touch-action: manipulation;
    user-select: none; -webkit-user-select: none; transition: transform .08s ease, background .3s ease; }
  .q:active { transform: translateY(3px); }
  .q:focus-visible { outline: 4px solid #fff; outline-offset: 3px; }
  .q-t, .joke { display: block; }
  .joke { display: none; margin-top: 6px; font-size: 14.5px; color: #8d5a3b; }
  .q.on .joke { display: block; animation: g-in .35s ease-out .2s both; }
  .okst { position: absolute; right: 12px; top: 50%; width: 62px; height: 62px; display: grid; place-items: center; border: 4px solid #e03131; border-radius: 50%;
    color: #e03131; font-size: 16px; font-weight: 900; letter-spacing: -.02em; transform: translateY(-50%) rotate(-14deg); opacity: 0; pointer-events: none; }
  @keyframes thump { 0% { opacity: 0; transform: translateY(-50%) rotate(-14deg) scale(2.2); } 60% { opacity: 1; transform: translateY(-50%) rotate(-14deg) scale(.9); } 100% { opacity: .92; transform: translateY(-50%) rotate(-14deg) scale(1); } }
  .q.on { background: #fff6e6; }
  .q.on .okst { opacity: .92; animation: thump .35s cubic-bezier(.2,1.2,.4,1); }
  .relax { margin-top: 14px; font-size: 15.5px; font-weight: 900; }
  .rn { font-variant-numeric: tabular-nums; display: inline-block; }
  .m-done { display: none; }
  .game[data-lv="5"] .m-done { display: block; animation: g-pop .45s cubic-bezier(.2,1.4,.4,1); }
''',
    dark=r'''
  html[data-theme="dark"] .bubble, html[data-theme="dark"] .q { background: #f1edf8; }
  html[data-theme="dark"] .q.on { background: #f8ead6; }
''',
    js=r'''
/* 💮 OK♪スタンプ：JS は data-lv・class・絵文字・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var qs = [].slice.call(g.querySelectorAll('.q')), mood = g.querySelector('.mood'), rn = g.querySelector('.rn');
  var FACE = ['😣', '😕', '🙂', '😌', '😊', '🥰'];
  function paint() {
    var n = qs.filter(function (q) { return q.classList.contains('on'); }).length;
    g.setAttribute('data-lv', String(n));
    mood.textContent = FACE[n];
    mood.classList.remove('pop'); void mood.offsetWidth; mood.classList.add('pop');
    rn.textContent = String(n);
    return n;
  }
  qs.forEach(function (q) {
    q.addEventListener('click', function () {
      if (q.classList.contains('on')) return;
      q.classList.add('on');
      if (navigator.vibrate) { try { navigator.vibrate(20); } catch (e) {} }
      var n = paint(), r = q.getBoundingClientRect();
      if (window.pengessoPop) {
        if (n === 5) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['💮', '🐧', '☕', '🧦', '🍰', '✨'], 24);
        else window.pengessoPop(r.right - 40, r.top + r.height / 2, ['💮', '✨'], 6);
      }
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    qs.forEach(function (q) { q.classList.remove('on'); }); paint();
  });
})();
''',
)
