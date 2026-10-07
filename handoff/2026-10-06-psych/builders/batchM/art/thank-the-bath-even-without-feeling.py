OBJ = [("🛁", "Bath", "お風呂"), ("🚽", "Toilet", "トイレ"), ("📱", "Phone", "スマホ"),
       ("👣", "My feet", "自分の足"), ("🛏️", "Bed", "ベッド"), ("☕", "Coffee", "コーヒー")]
_objs = "\n".join(f'      <button type="button" class="obj"><span class="o-e" aria-hidden="true">{e}</span><span class="o-w">{en}</span><span class="o-n">0</span></button>' for e, en, ja in OBJ)

A = dict(
    slug="thank-the-bath-even-without-feeling", seq=417,
    title="Say thank you even without feeling it, and it slowly becomes real",
    title_ja="心がこもっていなくても「ありがとう」。言ううちに本物になる",
    label="Hollow Thanks", label_ja="形だけのありがとう",
    float="🛁",
    alt="A chubby alpaca wool penguin hugging a real wooden bath bucket with soft steam",
    mood=["lift"], tags=["psychology", "happiness", "tips"],
    src_no="18", src_title="感謝行",
    center="心がこもっていなくても「ありがとう」を口に出す。言い続けるうちに本物の感謝に変わる。",
    tone="素材の重さ：まじめ（感謝の習慣）\n→ 見せ方：ポップに（水色と青とピーチ。ありがとう連打で、空っぽのハートが育つ）",
    tone_css="真面目な話 → ポップに。水色とピーチ",
    game_name="ありがとう連打",
    play="🛁 ありがとう連打：6つのもの（🛁 お風呂・🚽 トイレ・📱 スマホ・👣 自分の足・🛏️ ベッド・☕ コーヒー）をタップするたびに「ありがとう！」の吹き出しがぴょこっと出て、もの自身もぷるんと揺れ、それぞれの回数が数字で増える。大きなハートのメーターが 🤍「ただの言葉（それでOK）」→ 💗「ん、ちょっとあったかい…」→ ❤️「あれ…ちょっと本気かも！」→ 12回で 💖「本物のありがとう！」に育つ。6つ全部に言うと「🌈 6つ全部にありがとう」。「↺ もう一回」。",
    prompt="An extremely cute, chubby round penguin with a gentle face and a plain white belly (no rings or patterns on the belly), made of fluffy alpaca wool with long soft fibers, sitting happily and hugging one realistic round wooden Japanese bath bucket made of light cypress with a small folded white towel on its rim, gentle steam rising. Bright clean background in soft aqua and warm peach with gentle depth, like a cozy bath room glow, simple and uncluttered. Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering.",
    combo="ペンギン × アルパカの毛 × 木の湯おけ",
    pal=dict(bg="#f0fbfc", text="#1e3640", muted="#5f7a84", a="#0a8a99", b="#ff8fab", c="#ffd166", d="#7d5fff",
             big="#08798a", bigdark="#9fe6ee", h1="#123642", ink="#1e3640", shadowc="rgba(20,120,140,.16)",
             bg1="rgba(255,143,171,.20)", bg2="rgba(255,209,102,.26)", bg3="rgba(10,138,153,.14)", photo="#dcf4f6",
             game="linear-gradient(155deg, #12a9bd 0%, #4d7cff 50%, #ef6f97 100%)"),
    cards=[
        dict(e="💬", l="Just Say It", lj="言うだけ", s=[(
            'It seems you can just say "thank you," even if your heart is not in it.',
            "「ありがとう」は、心がこもっていなくても、口に出すだけでいいそうです。", False)]),
        dict(e="🛁", l="Thank Everything", lj="なんにでも", s=[(
            'To the bath, to the toilet, to your phone, to your own feet: "Thank you."',
            "お風呂に、トイレに、スマホに、自分の足に、「ありがとう」。", False)]),
        "GAME",
        dict(e="🌱", l="At First", lj="最初は", s=[(
            "At first, it is just words.",
            "最初は、ただの口ぐせです。", False)]),
        dict(e="💖", l="It Grows", lj="育っていく", s=[(
            "But as you keep saying it, it slowly changes into real thanks.",
            "でも言い続けるうちに、だんだん本物の感謝に変わっていきます。", True)]),
    ],
    game_html=r'''
  <!-- ⚡ 触って遊べる部品：ありがとう連打（気持ちがなくてもタップ。空っぽのハートが育つ） -->
  <section class="game" data-st="0" data-every="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">The thank-you button</div>
    <div class="game-hint">Tap things and say thanks. You do not need to feel it.</div>
    <div class="meter-box">
      <span class="heart" aria-hidden="true">🤍</span>
      <div class="hm"><div class="hm-bar" aria-hidden="true"><i></i></div>
        <div class="hm-st"><span class="st0">🤍 Just words (and that is OK)</span><span class="st1">💗 Hmm, a little warm…</span><span class="st2">❤️ Wait… I kind of mean it!</span><span class="st3">💖 Real thanks! It grew from just words.</span></div>
      </div>
    </div>
    <div class="objs">
OBJS
    </div>
    <span class="ty" aria-hidden="true">Thank you!</span>
    <div class="cnt"><span class="cnt-l">Thanks said:</span> <span class="cnt-n">0</span></div>
    <div class="msg m-every">🌈 You thanked all 6 things!</div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Start again</button></div>
  </section>
'''.replace("OBJS", _objs),
    game_ja=dict({
        "The thank-you button": "ありがとう連打",
        "Tap things and say thanks. You do not need to feel it.": "ものをタップして「ありがとう」。気持ちはこもっていなくてOK。",
        "🤍 Just words (and that is OK)": "🤍 ただの言葉（それでOK）",
        "💗 Hmm, a little warm…": "💗 ん、ちょっとあったかい…",
        "❤️ Wait… I kind of mean it!": "❤️ あれ…ちょっと本気かも！",
        "💖 Real thanks! It grew from just words.": "💖 本物のありがとう！ただの言葉から育ちました。",
        "Thank you!": "ありがとう！",
        "Thanks said:": "言った「ありがとう」：",
        "🌈 You thanked all 6 things!": "🌈 6つ全部に「ありがとう」が言えた！",
        "↺ Start again": "↺ もう一回",
    }, **{en: ja for e, en, ja in OBJ}),
    css=r'''
  /* 🛁 ありがとう連打 */
  .meter-box { display: flex; align-items: center; gap: 12px; max-width: 420px; margin: 14px auto 0; padding: 12px 14px; border-radius: 22px; background: rgba(255,255,255,.2); text-align: left; }
  .heart { flex: 0 0 auto; font-size: 54px; line-height: 1; display: inline-block; filter: drop-shadow(0 4px 8px rgba(0,0,0,.18)); }
  .hm { flex: 1; min-width: 0; }
  .hm-bar { position: relative; height: 16px; border-radius: 999px; background: rgba(255,255,255,.3); overflow: hidden; }
  .hm-bar i { position: absolute; inset: 0 auto 0 0; width: 0; border-radius: 999px; background: linear-gradient(90deg, #fff, #ffd1dc 40%, #ff5c8a);
    transition: width .35s cubic-bezier(.2,1.2,.4,1); }
  .hm-st { margin-top: 6px; font-size: 15px; font-weight: 900; line-height: 1.4; }
  .hm-st span { display: none; }
  .game[data-st="0"] .st0, .game[data-st="1"] .st1, .game[data-st="2"] .st2, .game[data-st="3"] .st3 { display: inline; animation: g-in .3s ease-out; }
  .objs { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; max-width: 380px; margin: 14px auto 0; }
  .obj { position: relative; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; min-height: 96px; padding: 10px 4px;
    border: 0; border-radius: 22px; background: #fff; color: var(--ink); font: inherit; font-weight: 900; cursor: pointer;
    box-shadow: 0 6px 0 rgba(0,0,0,.14), 0 12px 20px rgba(0,0,0,.10); -webkit-tap-highlight-color: transparent; touch-action: manipulation;
    user-select: none; -webkit-user-select: none; transition: transform .08s ease; }
  .obj:active { transform: translateY(3px) scale(.97); }
  .obj:focus-visible { outline: 4px solid #fff; outline-offset: 3px; }
  .o-e { font-size: 38px; line-height: 1; display: inline-block; }
  .o-w { font-size: 13.5px; line-height: 1.2; }
  .o-n { position: absolute; top: 6px; right: 8px; min-width: 22px; padding: 1px 6px; border-radius: 999px; background: #e7f6f8; color: #0a8a99;
    font-size: 12px; font-variant-numeric: tabular-nums; }
  .obj.got { background: #fff4f7; }
  .obj.got .o-n { background: #ff5c8a; color: #fff; }
  @keyframes jelly { 0% { transform: scale(1); } 30% { transform: scale(1.25, .8); } 55% { transform: scale(.88, 1.12); } 80% { transform: scale(1.05, .96); } 100% { transform: scale(1); } }
  .o-e.jelly { animation: jelly .45s ease; }
  .ty { position: absolute; left: 0; top: 0; z-index: 3; padding: 6px 12px; border-radius: 999px; background: #fff; color: #e64980; font-size: 15px; font-weight: 900;
    width: max-content; max-width: 220px; pointer-events: none; opacity: 0; transform: translate(-50%, -100%); }
  @keyframes ty-up { 0% { opacity: 0; transform: translate(-50%, -60%) scale(.7); } 25% { opacity: 1; transform: translate(-50%, -110%) scale(1.05); } 100% { opacity: 0; transform: translate(-50%, -190%) scale(1); } }
  .ty.fly { animation: ty-up .8s ease-out both; }
  .cnt { margin-top: 14px; font-size: 15.5px; font-weight: 900; }
  .cnt-n { font-variant-numeric: tabular-nums; display: inline-block; }
  .m-every { display: none; }
  .game[data-every="1"] .m-every { display: block; animation: g-pop .45s cubic-bezier(.2,1.4,.4,1); }
  @media (prefers-reduced-motion: reduce) { html:not([data-motion="on"]) .ty { display: none; } }
  html[data-motion="off"] .ty { display: none; }
''',
    dark=r'''
  html[data-theme="dark"] .obj { background: #f1edf8; }
  html[data-theme="dark"] .obj.got { background: #fde6ee; }
  html[data-theme="dark"] .ty { background: #f1edf8; }
''',
    js=r'''
/* 🛁 ありがとう連打：JS は data-*・class・style（位置とメーター）・絵文字・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var objs = [].slice.call(g.querySelectorAll('.obj')), heart = g.querySelector('.heart'), bar = g.querySelector('.hm-bar i'),
      cnt = g.querySelector('.cnt-n'), ty = g.querySelector('.ty');
  var GOAL = 12, total = 0, counts = objs.map(function () { return 0; });
  var HEART = ['🤍', '💗', '❤️', '💖'];
  function stage(n) { return n >= GOAL ? 3 : n >= 8 ? 2 : n >= 4 ? 1 : 0; }
  function bump(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function paint() {
    var st = stage(total), old = g.getAttribute('data-st');
    g.setAttribute('data-st', String(st));
    heart.textContent = HEART[st];
    if (String(st) !== old) bump(heart, 'pop');
    bar.style.width = Math.min(100, total / GOAL * 100) + '%';
    cnt.textContent = String(total);
    return String(st) !== old ? st : -1;
  }
  objs.forEach(function (o, i) {
    o.addEventListener('click', function () {
      total++; counts[i]++;
      o.querySelector('.o-n').textContent = String(counts[i]);
      o.classList.add('got');
      bump(o.querySelector('.o-e'), 'jelly');
      var gr = g.getBoundingClientRect(), r = o.getBoundingClientRect();
      ty.style.left = (r.left - gr.left + r.width / 2) + 'px';
      ty.style.top = (r.top - gr.top + 10) + 'px';
      bump(ty, 'fly');
      var changed = paint();
      if (changed === 3 && window.pengessoPop) {
        var h = heart.getBoundingClientRect();
        window.pengessoPop(h.left + h.width / 2, h.top + h.height / 2, ['💖', '🛁', '☕', '🐧', '✨'], 22);
        if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
      }
      if (g.getAttribute('data-every') !== '1' && counts.every(function (c) { return c > 0; })) {
        g.setAttribute('data-every', '1');
        if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🌈', '✨'], 10);
      }
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    total = 0; counts = objs.map(function () { return 0; });
    objs.forEach(function (o) { o.classList.remove('got'); o.querySelector('.o-n').textContent = '0'; });
    g.setAttribute('data-every', '0'); ty.classList.remove('fly'); paint();
  });
  paint();
})();
''',
)
