A = dict(
    slug="act-first-heart-follows", seq=415,
    title="Do good things first, because your heart follows your body",
    title_ja="いい人になる前に、いい行いを。心は体の動きについてくる",
    label="Body First", label_ja="体が先",
    float="🎵",
    alt="A chubby felted wool penguin skipping happily next to a real pair of bright sneakers",
    mood=["lift", "energy"], tags=["psychology", "feelings", "mindset"],
    src_no="16", src_title="性格は変えられる（②いい人になる前に、いい行いをする）",
    center="いい人になるのを待たずに、先にいい行いをする。心は体の動きにあとからついてくる。",
    tone="素材の重さ：真面目（性格を変える方法）\n→ 見せ方：ポップに（オレンジとラズベリーと紫。「落ち込んだままでいられるか？」の気分エレベーターで遊べる）",
    tone_css="真面目な話 → ポップに。オレンジとラズベリー",
    game_name="気分エレベーター",
    play="🛗 気分エレベーター：ペンギンは地下2階「😞 どんより」から「今日は落ち込んだままでいるぞ。止められるかな…」と挑戦してくる。体を動かすボタン（🎵 スキップ／🌅 大きく背伸び／😄 にっこり笑う）を押すと、ペンギンがその動きをして、セリフが「落ち込めない！」系に変わり、エレベーターが1階ずつ上がる（顔も 😞→😐→🙂→😊→😆）。「🛋️ 座って考えこむ」だけは1階下がる。屋上（3F ☀️）に着くと「体が先に動いて、心がついてきた」🎉。「↺ 地下2階に戻る」。",
    prompt="An extremely cute, chubby round penguin with a gentle face and a plain white belly (no rings or patterns on the belly), made of soft felted wool with a fuzzy needle-felted texture, caught mid-skip with both feet off the ground and flippers swinging happily, next to one realistic pair of bright orange and white running sneakers with neat laces. Bright warm background in sunny yellow and soft coral with a gentle morning glow and depth, simple and uncluttered. Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering.",
    combo="ペンギン × 羊毛フェルト × スニーカー",
    pal=dict(bg="#fff8ec", text="#3a2530", muted="#856a74", a="#d6336c", b="#ffb800", c="#3ac3ff", d="#8f5bff",
             big="#c2255c", bigdark="#ffb3cb", h1="#3d1e2b", ink="#3a2530", shadowc="rgba(170,60,90,.16)",
             bg1="rgba(255,184,0,.28)", bg2="rgba(214,51,108,.14)", bg3="rgba(143,91,255,.14)", photo="#ffe8ef",
             game="linear-gradient(160deg, #f08c00 0%, #e8436a 55%, #9c42e8 100%)"),
    cards=[
        dict(e="🐾", l="Do It First", lj="先にやる", s=[(
            "Do not wait to become a good person; do good things first.",
            "いい人になるのを待たずに、先にいい行いをします。", False)]),
        dict(e="🧲", l="Body Leads", lj="体が先", s=[(
            "It seems your heart comes after the moves of your body.",
            "心は、体の動きにあとからついてくるそうです。", False)]),
        dict(e="🎵", l="Cannot Do Both", lj="同時は無理", s=[(
            "You cannot get angry while you laugh, and you cannot feel down while you skip.",
            "笑いながら怒ることはできないし、スキップしながら落ち込むこともできません。", False)]),
        "GAME",
        dict(e="🌅", l="Morning Stretch", lj="朝の背伸び", s=[(
            'In the morning, stretch and say, "What a fresh morning!" and your heart looks forward too.',
            "朝、「すがすがしい朝だ〜」と背伸びをすると、心も前を向きます。", True)]),
    ],
    game_html=r'''
  <!-- ⚡ 触って遊べる部品：気分エレベーター（体を動かすと1階ずつ上がる。座って考えこむと下がる） -->
  <section class="game" data-f="0" data-a="0" data-top="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Can the penguin stay gloomy?</div>
    <div class="game-hint">Move the body. Watch the mood elevator.</div>
    <div class="lift">
      <ol class="floors">
        <li class="fl" data-n="4"><span class="fl-n">3F</span><span class="fl-w">☀️ Great</span><span class="car" aria-hidden="true">🐧</span></li>
        <li class="fl" data-n="3"><span class="fl-n">2F</span><span class="fl-w">😊 Good</span><span class="car" aria-hidden="true">🐧</span></li>
        <li class="fl" data-n="2"><span class="fl-n">1F</span><span class="fl-w">🙂 Okay</span><span class="car" aria-hidden="true">🐧</span></li>
        <li class="fl" data-n="1"><span class="fl-n">B1</span><span class="fl-w">😐 Meh</span><span class="car" aria-hidden="true">🐧</span></li>
        <li class="fl" data-n="0"><span class="fl-n">B2</span><span class="fl-w">😞 Gloomy</span><span class="car" aria-hidden="true">🐧</span></li>
      </ol>
      <div class="stage-box">
        <div class="pg-wrap" aria-hidden="true"><span class="pg">🐧</span><span class="face">😞</span></div>
        <div class="bubble">
          <span class="b0">Today I will stay gloomy. Try to stop me… 😞</span>
          <span class="b1">Gloomy… gloo… hop, hop! I cannot feel down while I skip! 🎵</span>
          <span class="b2">Mmmmm… What a fresh morning! 🌅</span>
          <span class="b3">I try to be grumpy… but I cannot while I smile. 😄</span>
          <span class="b4">Hmm… why… and why… and why… 🌀 The elevator goes down.</span>
          <span class="b5">☀️ Rooftop! My body moved first, and my heart came along.</span>
        </div>
      </div>
    </div>
    <div class="acts">
      <button type="button" class="btn act" data-a="1">🎵 Skip</button>
      <button type="button" class="btn act" data-a="2">🌅 Big stretch</button>
      <button type="button" class="btn act" data-a="3">😄 Big smile</button>
      <button type="button" class="btn act act-think" data-a="4">🛋️ Sit and think</button>
    </div>
    <div class="moves"><span class="mv-l">Moves:</span> <span class="mv">0</span></div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Back to B2</button></div>
  </section>
''',
    game_ja={
        "Can the penguin stay gloomy?": "ペンギンは落ち込んだままでいられる？",
        "Move the body. Watch the mood elevator.": "体を動かしてみて。気分のエレベーターを見ていてね。",
        "3F": "3階", "2F": "2階", "1F": "1階", "B1": "地下1階", "B2": "地下2階",
        "☀️ Great": "☀️ 最高", "😊 Good": "😊 いい感じ", "🙂 Okay": "🙂 まあまあ", "😐 Meh": "😐 うーん", "😞 Gloomy": "😞 どんより",
        "Today I will stay gloomy. Try to stop me… 😞": "今日は落ち込んだままでいるぞ。止められるかな… 😞",
        "Gloomy… gloo… hop, hop! I cannot feel down while I skip! 🎵": "どんより…どん…ぴょん、ぴょん！スキップしながら落ち込めない！🎵",
        "Mmmmm… What a fresh morning! 🌅": "んー…すがすがしい朝だ〜！🌅",
        "I try to be grumpy… but I cannot while I smile. 😄": "怒ろうとしても…笑いながらだと無理。😄",
        "Hmm… why… and why… and why… 🌀 The elevator goes down.": "うーん…なんで…なんで…なんで… 🌀 エレベーターが下がった。",
        "☀️ Rooftop! My body moved first, and my heart came along.": "☀️ 屋上！体が先に動いて、心がついてきた。",
        "🎵 Skip": "🎵 スキップ",
        "🌅 Big stretch": "🌅 大きく背伸び",
        "😄 Big smile": "😄 にっこり笑う",
        "🛋️ Sit and think": "🛋️ 座って考えこむ",
        "Moves:": "動いた回数：",
        "↺ Back to B2": "↺ 地下2階に戻る",
    },
    css=r'''
  /* 🛗 気分エレベーター */
  .lift { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.25fr); gap: 10px; max-width: 440px; margin: 14px auto 0; text-align: left; }
  .floors { list-style: none; margin: 0; padding: 8px; border-radius: 20px; background: rgba(255,255,255,.18); display: grid; gap: 6px; }
  .fl { position: relative; display: flex; align-items: center; gap: 6px; min-height: 40px; padding: 4px 8px; border-radius: 12px;
    font-size: 13.5px; font-weight: 900; opacity: .6; transition: background .3s ease, opacity .3s ease; }
  .fl-n { flex: 0 0 auto; min-width: 30px; padding: 2px 5px; border-radius: 8px; background: rgba(0,0,0,.18); text-align: center; font-size: 12px; }
  .fl-w { min-width: 0; line-height: 1.2; }
  .car { margin-left: auto; font-size: 20px; visibility: hidden; }
  .fl.on { background: #fff; color: var(--ink); opacity: 1; }
  .fl.on .fl-n { background: var(--a); color: #fff; }
  .fl.on .car { visibility: visible; animation: g-pop .4s cubic-bezier(.2,1.4,.4,1); }
  .stage-box { display: flex; flex-direction: column; align-items: center; gap: 10px; padding: 10px; border-radius: 20px; background: rgba(255,255,255,.18); }
  .pg-wrap { position: relative; width: 96px; height: 96px; display: grid; place-items: center; border-radius: 50%; background: rgba(255,255,255,.25); }
  .pg { font-size: 58px; line-height: 1; display: inline-block; transform-origin: 50% 100%; }
  .face { position: absolute; right: -6px; top: -6px; font-size: 32px; line-height: 1; }
  @keyframes skip { 0%, 100% { transform: translateY(0) rotate(0); } 25% { transform: translateY(-22px) rotate(-10deg); } 50% { transform: translateY(0) rotate(0); } 75% { transform: translateY(-22px) rotate(10deg); } }
  @keyframes stretch { 0%, 100% { transform: scale(1, 1); } 45%, 70% { transform: scale(.92, 1.3); } }
  @keyframes wiggle { 0%, 100% { transform: rotate(0); } 25% { transform: rotate(-12deg) scale(1.08); } 75% { transform: rotate(12deg) scale(1.08); } }
  @keyframes droop { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(8px) scale(1, .9); } }
  .pg.a1 { animation: skip .9s ease-in-out; }
  .pg.a2 { animation: stretch 1s ease-in-out; }
  .pg.a3 { animation: wiggle .7s ease-in-out; }
  .pg.a4 { animation: droop 1.2s ease-in-out; filter: grayscale(.5); }
  .bubble { width: 100%; padding: 10px 12px; border-radius: 16px; background: #fff; color: var(--ink); font-size: 15px; font-weight: 900; line-height: 1.45; min-height: 74px; }
  .bubble span { display: none; }
  .game[data-a="0"] .b0, .game[data-a="1"] .b1, .game[data-a="2"] .b2, .game[data-a="3"] .b3, .game[data-a="4"] .b4, .game[data-a="5"] .b5 { display: inline; }
  .game[data-a="5"] .bubble { background: #fff3a8; }
  .acts { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 440px; margin: 16px auto 0; }
  .act { padding: 12px 10px; font-size: 16px; color: #b02a5b; }
  .act-think { color: #5a5470; background: #ece9f3; }
  .moves { margin-top: 12px; font-size: 15px; font-weight: 900; }
  .mv { font-variant-numeric: tabular-nums; }
  @media (max-width: 380px) { .lift { grid-template-columns: 1fr; } .floors { grid-template-columns: 1fr; } }
''',
    dark=r'''
  html[data-theme="dark"] .fl.on, html[data-theme="dark"] .bubble { background: #f1edf8; }
  html[data-theme="dark"] .game[data-a="5"] .bubble { background: #fff3a8; }
  html[data-theme="dark"] .act-think { background: #d9d5e3; }
''',
    js=r'''
/* 🛗 気分エレベーター：JS は data-*・class・絵文字・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var fls = [].slice.call(g.querySelectorAll('.fl')), pg = g.querySelector('.pg'), face = g.querySelector('.face'), mv = g.querySelector('.mv');
  var FACE = ['😞', '😐', '🙂', '😊', '😆'];
  var floor = 0, moves = 0;
  function paint() {
    fls.forEach(function (f) { f.classList.toggle('on', parseInt(f.getAttribute('data-n'), 10) === floor); });
    face.textContent = FACE[floor];
    face.classList.remove('pop'); void face.offsetWidth; face.classList.add('pop');
    g.setAttribute('data-f', String(floor));
    mv.textContent = String(moves);
  }
  function play(a) { pg.className = 'pg'; void pg.offsetWidth; pg.className = 'pg a' + a; }
  [].forEach.call(g.querySelectorAll('.act'), function (b) {
    b.addEventListener('click', function () {
      var a = parseInt(b.getAttribute('data-a'), 10);
      moves++;
      play(a);
      if (a === 4) { floor = Math.max(0, floor - 1); g.setAttribute('data-top', '0'); g.setAttribute('data-a', '4'); }
      else {
        floor = Math.min(4, floor + 1);
        if (floor === 4) {
          g.setAttribute('data-a', '5');
          if (g.getAttribute('data-top') !== '1') {
            g.setAttribute('data-top', '1');
            if (window.pengessoPop) { var r = pg.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['☀️', '🎵', '🐧', '✨', '🌅'], 20); }
            if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
          }
        } else { g.setAttribute('data-a', String(a)); }
      }
      paint();
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    floor = 0; moves = 0; pg.className = 'pg';
    g.setAttribute('data-a', '0'); g.setAttribute('data-top', '0'); paint();
  });
  paint();
})();
''',
)
