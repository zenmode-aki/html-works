OU = [("1", "🦷 Toothache", "🦷 歯が痛い"), ("2", "🌀 Growling tummy", "🌀 お腹がぐう"),
      ("3", "😪 So tired", "😪 へとへと"), ("4", "🧦 Smelly socks", "🧦 くつしたがくさい")]
SG = [("3", "🛏️ Take a rest", "🛏️ 休けいする"), ("1", "📅 Book the dentist", "📅 歯医者さんを予約"),
      ("4", "🧼 Wash them", "🧼 洗う"), ("2", "🍚 Eat something", "🍚 何か食べる")]
_ou = "\n".join(f'        <button type="button" class="pc ou" data-k="{k}">{en}</button>' for k, en, ja in OU)
_sg = "\n".join(f'        <button type="button" class="pc sg" data-k="{k}">{en}</button>' for k, en, ja in SG)

A = dict(
    slug="pain-is-a-signal", seq=419,
    title="Pain is not bad luck; it is a signal that protects you",
    title_ja="苦しさは「ツイてない」ではなく、自分を守る合図",
    label="Pain Signal", label_ja="苦しさは合図",
    float="🚦",
    alt="A chubby mohair penguin smiling next to a real miniature traffic light glowing green",
    mood=["lift", "learn"], tags=["psychology", "feelings", "health"],
    src_no="20", src_title="苦痛は「合図」",
    center="苦しさは自分を悩ませるためではなく、守るための「合図」。合図だと思えば、やることが見える。",
    tone="素材の重さ：真面目（痛い・つらい）\n→ 見せ方：ポップに（信号の赤・黄・緑。「いたた」と合図を組み合わせる解読機で遊べる）。健康の話はやわらかく、アドバイスはしない",
    tone_css="真面目な話 → ポップに。信号の赤と緑",
    game_name="合図の解読機",
    play="🚦 合図の解読機：左に「いたた」4つ（🦷 歯が痛い／🌀 お腹がぐう／😪 へとへと／🧦 くつしたがくさい）、右に合図4つ（並びはバラバラ：🛏️ 休けいする／📅 歯医者さんを予約／🧼 洗う／🍚 何か食べる）。1つ選んで、相手をタップ。合っていれば2つとも緑になって ✅、ちがうとプルプル「🤔 その合図じゃないみたい」。4組そろうと 🚨 が 🛡️ に変わって「いたたは全部、守ってくれる味方だった」🎉。どちらの列から選んでもOK。",
    prompt="An extremely cute, chubby round penguin with a gentle face and a plain white belly (no rings or patterns on the belly), made of soft brushed mohair with a light fuzzy halo, standing calmly with a kind smile next to one realistic miniature traffic light on a short pole, its green light glowing softly while the red and yellow lights are off. Bright background in warm cream, soft mint green and a touch of sunny yellow with gentle depth, simple and uncluttered. Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering.",
    combo="ペンギン × ブラッシュモヘア × ミニチュアの信号機",
    pal=dict(bg="#fbfaf0", text="#2a2b24", muted="#6e6f5f", a="#d63a4a", b="#1f9e5f", c="#ffbe0b", d="#3a86ff",
             big="#168a52", bigdark="#a6efc6", h1="#2b2620", ink="#2a2b24", shadowc="rgba(120,100,40,.16)",
             bg1="rgba(255,190,11,.26)", bg2="rgba(214,58,74,.12)", bg3="rgba(31,158,95,.16)", photo="#eef6e6",
             game="linear-gradient(150deg, #e8505b 0%, #f08c2e 45%, #1f9e5f 100%)"),
    cards=[
        dict(e="🦷", l="Bad Luck?", lj="ツイてない？", s=[(
            'When your tooth hurts, thinking "The worst! I am so unlucky!" only makes it harder.',
            "歯が痛いとき、「最悪、ツイてない」と思うと、つらくなるだけです。", False)]),
        dict(e="📅", l="A Signal", lj="合図", s=[(
            'If you think it is a signal to "book the dentist," you can see what to do.',
            "「歯医者さんを予約しよう」という合図だと思えば、やることが見えてきます。", False)]),
        dict(e="🍙", l="More Signals", lj="ほかの合図", s=[(
            "Feeling hungry is a signal to eat, and feeling tired is a signal to rest.",
            "お腹がすいたら食事の合図、疲れたら休けいの合図です。", False)]),
        "GAME",
        dict(e="🛡️", l="Here To Help", lj="守るため", s=[(
            "It seems pain is here not to trouble us, but to protect us.",
            "苦しさは、私たちを困らせるためではなく、守るためにあるそうです。", True)]),
    ],
    game_html=r'''
  <!-- ⚡ 触って遊べる部品：合図の解読機（「いたた」と、それが送っている合図を組み合わせる） -->
  <section class="game" data-w="0" data-all="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title"><span class="siren" aria-hidden="true">🚨</span> Signal decoder</div>
    <div class="game-hint">Tap an "ouch," then tap the signal it is sending.</div>
    <div class="board">
      <div class="col">
        <div class="col-h">🚨 Ouch</div>
OUS
      </div>
      <div class="col">
        <div class="col-h">🚦 Signal</div>
SGS
      </div>
    </div>
    <div class="say"><span class="w0">Pick 1 from either side. 👆</span><span class="w1">🤔 Not that signal. Try another one!</span><span class="w2">✅ Yes! That ouch was a helper.</span></div>
    <div class="score"><span class="sc-l">Signals decoded:</span> <span class="sc-n">0</span>/4</div>
    <div class="msg m-all">🛡️ All 4 "ouch" were helpers. They were protecting you!</div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Again</button></div>
  </section>
'''.replace("OUS", _ou).replace("SGS", _sg),
    game_ja=dict({
        "Signal decoder": "合図の解読機",
        "Tap an \"ouch,\" then tap the signal it is sending.": "「いたた」をタップして、それが送っている合図をタップ。",
        "🚨 Ouch": "🚨 いたた",
        "🚦 Signal": "🚦 合図",
        "Pick 1 from either side. 👆": "どちらの列からでも、1つ選んでね。👆",
        "🤔 Not that signal. Try another one!": "🤔 その合図じゃないみたい。別のを試して！",
        "✅ Yes! That ouch was a helper.": "✅ そう！その「いたた」は味方でした。",
        "Signals decoded:": "解読した合図：",
        "🛡️ All 4 \"ouch\" were helpers. They were protecting you!": "🛡️ 4つの「いたた」は全部、味方でした。あなたを守っていたんです！",
        "↺ Again": "↺ もう一回",
    }, **{en: ja for k, en, ja in OU + SG}),
    css=r'''
  /* 🚦 合図の解読機 */
  .siren { display: inline-block; }
  .board { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 440px; margin: 14px auto 0; }
  .col { display: grid; gap: 10px; align-content: start; }
  .col-h { padding: 6px 8px; border-radius: 12px; background: rgba(0,0,0,.16); font-size: 13.5px; font-weight: 900; letter-spacing: .04em; }
  .pc { position: relative; min-height: 60px; padding: 10px 10px; border: 0; border-radius: 18px; font: inherit; font-size: 15px; font-weight: 900; line-height: 1.3;
    cursor: pointer; text-align: left; color: var(--ink); background: #fff; box-shadow: 0 5px 0 rgba(0,0,0,.14), 0 10px 18px rgba(0,0,0,.10);
    -webkit-tap-highlight-color: transparent; touch-action: manipulation; user-select: none; -webkit-user-select: none; transition: transform .08s ease, background .25s ease; }
  .pc:active { transform: translateY(3px); }
  .pc:focus-visible { outline: 4px solid #fff; outline-offset: 3px; }
  .ou { background: #fff0f0; color: #a61e2d; }
  .sg { background: #f2fbf5; color: #136b40; }
  .pc.sel { box-shadow: 0 0 0 4px #ffe066, 0 5px 0 rgba(0,0,0,.14); transform: translateY(-2px); }
  .pc.done { background: #d3f5e2; color: #0d6b3d; pointer-events: none; opacity: .92; }
  .pc.done::after { content: "✅"; position: absolute; top: -8px; right: -6px; font-size: 18px; }
  .say { min-height: 50px; margin: 14px auto 0; max-width: 420px; display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .say span { display: none; }
  .game[data-w="0"] .w0, .game[data-w="1"] .w1, .game[data-w="2"] .w2 { display: inline; animation: g-in .3s ease-out; }
  .score { font-size: 15.5px; font-weight: 900; }
  .sc-n { font-variant-numeric: tabular-nums; display: inline-block; }
  .m-all { display: none; }
  .game[data-all="1"] .m-all { display: block; animation: g-pop .45s cubic-bezier(.2,1.4,.4,1); }
  .game[data-all="1"] .say { display: none; }
''',
    dark=r'''
  html[data-theme="dark"] .ou { background: #f7e4e6; }
  html[data-theme="dark"] .sg { background: #e2f2e8; }
  html[data-theme="dark"] .pc.done { background: #c3ebd5; }
''',
    js=r'''
/* 🚦 合図の解読機：JS は data-*・class・絵文字・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var pcs = [].slice.call(g.querySelectorAll('.pc')), scn = g.querySelector('.sc-n'), siren = g.querySelector('.siren');
  var sel = null, got = 0, wt = 0;
  function side(el) { return el.classList.contains('ou') ? 'ou' : 'sg'; }
  function shake(el) { el.classList.remove('shake'); void el.offsetWidth; el.classList.add('shake'); }
  function say(w) { g.setAttribute('data-w', w); clearTimeout(wt); if (w !== '0') wt = setTimeout(function () { g.setAttribute('data-w', '0'); }, 1800); }
  pcs.forEach(function (p) {
    p.addEventListener('click', function () {
      if (p.classList.contains('done')) return;
      if (!sel || side(sel) === side(p)) {
        if (sel) sel.classList.remove('sel');
        sel = (sel === p) ? null : p;
        if (sel) sel.classList.add('sel');
        return;
      }
      var a = sel; sel = null; a.classList.remove('sel');
      if (a.getAttribute('data-k') === p.getAttribute('data-k')) {
        a.classList.add('done'); p.classList.add('done', 'pop'); a.classList.add('pop');
        got++; scn.textContent = String(got);
        say('2');
        var r = p.getBoundingClientRect();
        if (got >= 4) {
          g.setAttribute('data-all', '1'); siren.textContent = '🛡️';
          siren.classList.remove('pop'); void siren.offsetWidth; siren.classList.add('pop');
          if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🛡️', '🚦', '🐧', '✨', '💚'], 22);
          if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
        } else if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['💚', '✨'], 8);
      } else {
        shake(a); shake(p); say('1');
        if (navigator.vibrate) { try { navigator.vibrate(15); } catch (e) {} }
      }
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    sel = null; got = 0; scn.textContent = '0'; siren.textContent = '🚨';
    pcs.forEach(function (p) { p.classList.remove('done', 'sel', 'pop', 'shake'); });
    clearTimeout(wt); g.setAttribute('data-w', '0'); g.setAttribute('data-all', '0');
  });
})();
''',
)
