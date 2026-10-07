from gen import build

d = dict(
    slug="you-find-yourself-by-trying", seq=531,
    title=("You find your values and strengths by trying things",
           "自分の価値観や強みは、挑戦するなかで見えてくる"),
    label=("Find by Trying", "やって見つける"),
    h1_emoji="🗺️",
    alt="A chubby matte plastic model kit penguin looking through a real brass telescope toward a bright horizon",
    section="一番大事なのは「戦わない」こと（③…価値観や強みは挑戦のなかで見えてくる）",
    message="自分の価値観や強みは、考えているだけでは見えない。挑戦するなかで、少しずつ見えてくる。",
    tone="素材の重さ：真面目（生き方の考え方）\n→ 見せ方：ポップに（朝の空の水色と、たからものの金色。霧の地図で遊べる）",
    game_ja="🗺️ 霧の地図：6つのマスが霧でかくれた「自分の地図」。「🤔 じっと考える」を押しても、💭 がくるくるするだけで霧は晴れない（考えた回数だけ増える）。「🚶 やってみる」を押すと、マスが1つ晴れて、たからものが出る（🎨 絵をかく ⭐ 好き！／🏃 ランニング 💧 私には合わない など）。全部晴れると「地図が完成！⭐ 好き3つ、💧 合わない3つ。どっちも宝物」。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made as a matte plastic model kit "
            "with smooth rounded parts, standing on a small grassy hill and looking through a realistic brass telescope toward a bright "
            "morning horizon, curious and hopeful. Bright simple morning sky-blue and warm gold background with soft depth. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × マットなプラモデル × 真ちゅうの望遠鏡",
    mood=["lift", "energy"], tags=["psychology", "mindset", "happiness"],
    pal=dict(bg="#f2f8ff", muted="#5f7088", acc="#2f7be0", acc2="#f2b200", shadow="rgba(40,90,170,.16)",
             r1="rgba(255,205,60,.28)", r2="rgba(60,140,240,.20)", r3="rgba(120,220,200,.18)",
             h1="#132a4c", photo="#e2eeff", big="#2466c2", bigdark="#a8cbff",
             game="linear-gradient(150deg, #4aa3ff 0%, #5a6ff0 50%, #f2b200 100%)"),
    cards=[
        dict(emoji="🤔", label=("Not by Thinking", "考えるだけでは"),
             s=[("You cannot see your values and strengths just by thinking in your head.",
                 "自分の価値観や強みは、頭で考えているだけでは見えてきません。")]),
        dict(emoji="🚶", label=("While Trying", "やりながら"),
             s=[("They become clear little by little while you try things.",
                 "挑戦しているうちに、少しずつ見えてくるものです。")]),
        dict(emoji="⭐", label=("Like or Not", "好きか、違うか"),
             s=[("Sometimes you find \"I like this,\" and sometimes you find \"This is not for me.\"",
                 "やってみて「好き」がわかることもあれば、「これは違う」がわかることもあります。")]),
        dict(emoji="🗺️", label=("Both Treasures", "どちらも宝物"), big=True,
             s=[("Both are treasures that make your map bigger.",
                 "どちらも、自分の地図を広げてくれる宝物です。")]),
    ],
    game_after=2,
    game_note="霧の地図（考えるだけでは晴れない。やってみると晴れる）",
    game_html="""  <section class="game" data-open="0" data-think="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">The foggy map of me</div>
    <div class="game-hint">Clear the fog. Which button works?</div>
    <div class="map">
      <div class="tile" data-v="like"><span class="tl-e">🎨</span><span class="tl-n">Drawing</span><span class="tl-v">⭐ I like it!</span><span class="fog"></span></div>
      <div class="tile" data-v="no"><span class="tl-e">🏃</span><span class="tl-n">Running</span><span class="tl-v">💧 Not for me</span><span class="fog"></span></div>
      <div class="tile" data-v="like"><span class="tl-e">🍳</span><span class="tl-n">Cooking</span><span class="tl-v">⭐ I like it!</span><span class="fog"></span></div>
      <div class="tile" data-v="no"><span class="tl-e">🎤</span><span class="tl-n">Karaoke</span><span class="tl-v">💧 Not for me</span><span class="fog"></span></div>
      <div class="tile" data-v="like"><span class="tl-e">📷</span><span class="tl-n">Photos</span><span class="tl-v">⭐ I like it!</span><span class="fog"></span></div>
      <div class="tile" data-v="no"><span class="tl-e">🧩</span><span class="tl-n">Puzzles</span><span class="tl-v">💧 Not for me</span><span class="fog"></span></div>
      <div class="think-bub" aria-hidden="true"><span class="tb-e">💭</span></div>
    </div>
    <div class="count"><span class="ct-a">🤔 Thought:</span> <span class="nt">0</span> <span class="ct-sep">·</span> <span class="ct-b">🚶 Tried:</span> <span class="no">0</span><span class="ct-of">/6</span></div>
    <div class="msg">
      <div class="m-idle">Thinking or trying. Which one clears the fog?</div>
      <div class="m-think">Hmm… still foggy. Thinking alone does not clear it.</div>
      <div class="m-try">The fog cleared! You found something new.</div>
      <div class="m-end">🗺️ Map complete! ⭐ 3 likes and 💧 3 not-for-me. Both are treasures.</div>
    </div>
    <div class="acts">
      <button type="button" class="btn think">🤔 Just think</button>
      <button type="button" class="btn try">🚶 Try something</button>
    </div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Start over</button></div>
  </section>""",
    css="""
  /* 🗺️ 霧の地図 */
  .map { position: relative; display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; max-width: 360px; margin: 16px auto 0; padding: 10px;
    border-radius: 24px; background: linear-gradient(160deg, #d9f5c8, #b9e7a5); }
  .tile { position: relative; display: grid; justify-items: center; align-content: center; gap: 2px; min-height: 112px; padding: 8px 4px;
    border-radius: 18px; background: #fffbe9; color: #24324a; overflow: hidden; }
  .tile[data-v="no"] { background: #eef3fa; }
  .tl-e { font-size: 32px; line-height: 1.1; }
  .tl-n { font-size: 13.5px; font-weight: 900; }
  .tl-v { font-size: 12.5px; font-weight: 900; line-height: 1.25; color: #8a6400; }
  .tile[data-v="no"] .tl-v { color: #3d6aa8; }
  .fog { position: absolute; inset: -6px; border-radius: 18px;
    background: radial-gradient(circle at 30% 35%, #ffffff 0 22%, transparent 48%), radial-gradient(circle at 72% 62%, #f4f7fb 0 26%, transparent 52%),
      linear-gradient(160deg, #e6ebf2, #cfd8e4);
    transition: opacity .6s ease, transform .6s ease; }
  .tile.clear .fog { opacity: 0; transform: scale(1.4) translateX(20%); }
  .tile.clear .tl-e { display: inline-block; animation: boing .6s ease; }
  .game.wiggle .fog { animation: fogwig .5s ease; }
  @keyframes fogwig { 30% { transform: translateX(-4px); } 70% { transform: translateX(4px); } }
  .think-bub { position: absolute; left: 50%; top: 50%; font-size: 54px; line-height: 1; opacity: 0; transform: translate(-50%, -50%) scale(.4); pointer-events: none; }
  .game.wiggle .think-bub { animation: thinkpop 1s ease both; }
  @keyframes thinkpop { 0% { opacity: 0; transform: translate(-50%, -50%) scale(.4) rotate(0); } 30% { opacity: 1; transform: translate(-50%, -50%) scale(1.1) rotate(-20deg); }
    70% { opacity: 1; transform: translate(-50%, -50%) scale(1) rotate(200deg); } 100% { opacity: 0; transform: translate(-50%, -50%) scale(.6) rotate(360deg); } }
  .count { margin-top: 12px; font-size: 15px; font-weight: 900; }
  .nt, .no { display: inline-block; min-width: 1.2em; padding: 2px 8px; border-radius: 999px; background: rgba(255,255,255,.3); }
  .msg { margin-top: 10px; min-height: 52px; font-size: 16.5px; font-weight: 900; line-height: 1.4; }
  .msg > div { display: none; }
  .game[data-last=""] .m-idle, .game:not([data-last]) .m-idle, .game[data-last="think"]:not([data-open="6"]) .m-think,
  .game[data-last="try"]:not([data-open="6"]) .m-try, .game[data-open="6"] .m-end { display: block; animation: boing .45s ease; }
  .acts { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 380px; margin: 8px auto 0; }
  .think { background: rgba(255,255,255,.25); color: #fff; box-shadow: inset 0 0 0 2px rgba(255,255,255,.7); }
  .try { min-height: 60px; font-size: 17px; background: #ffe066; color: #4a3500; }
  .game[data-open="6"] .try { opacity: .4; pointer-events: none; }
  .ctrl { margin-top: 10px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
""",
    dark="""  html[data-theme="dark"] .map { background: linear-gradient(160deg, #2c4a2a, #203a20); }
  html[data-theme="dark"] .tile { background: #3a3320; color: #f4f0fa; }
  html[data-theme="dark"] .tile[data-v="no"] { background: #263246; }
  html[data-theme="dark"] .tl-v { color: #ffe39a; }
  html[data-theme="dark"] .tile[data-v="no"] .tl-v { color: #b8d4ff; }
  html[data-theme="dark"] .fog { background: radial-gradient(circle at 30% 35%, #8a93a3 0 22%, transparent 48%), radial-gradient(circle at 72% 62%, #7a8494 0 26%, transparent 52%), linear-gradient(160deg, #5a6272, #464e5e); }
  html[data-theme="dark"] .game .think { background: rgba(255,255,255,.12); color: #fff; }
  html[data-theme="dark"] .game .try { background: #4a3c12; color: #ffe39a; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var tiles = [].slice.call(g.querySelectorAll('.tile')), nt = g.querySelector('.nt'), no = g.querySelector('.no'), thought = 0;
  function pop(el, list, n) {
    if (!window.pengessoPop) return;
    var r = el.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, n || 12);
  }
  g.setAttribute('data-last', '');
  g.querySelector('.think').addEventListener('click', function () {
    thought++; nt.textContent = thought;
    g.setAttribute('data-last', 'think');
    g.classList.remove('wiggle'); void g.offsetWidth; g.classList.add('wiggle');
  });
  g.querySelector('.try').addEventListener('click', function () {
    var hid = tiles.filter(function (t) { return !t.classList.contains('clear'); });
    if (!hid.length) return;
    var t = hid[Math.floor(Math.random() * hid.length)];
    t.classList.add('clear');
    var n = 6 - hid.length + 1;
    no.textContent = n; g.setAttribute('data-open', String(n));
    g.setAttribute('data-last', 'try');
    pop(t, t.getAttribute('data-v') === 'like' ? ['⭐', '✨'] : ['💧', '✨'], 8);
    if (n === 6) setTimeout(function () { pop(g.querySelector('.map'), ['🗺️', '⭐', '🐧', '🚩', '✨'], 20); }, 350);
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    thought = 0; nt.textContent = '0'; no.textContent = '0';
    tiles.forEach(function (t) { t.classList.remove('clear'); });
    g.setAttribute('data-open', '0'); g.setAttribute('data-last', ''); g.classList.remove('wiggle');
  });
})();
""",
    ja={
        "The foggy map of me": "霧につつまれた「自分の地図」",
        "Clear the fog. Which button works?": "霧を晴らそう。効くのはどっちのボタン？",
        "Drawing": "絵をかく",
        "Running": "ランニング",
        "Cooking": "料理",
        "Karaoke": "カラオケ",
        "Photos": "写真",
        "Puzzles": "パズル",
        "⭐ I like it!": "⭐ 好き！",
        "💧 Not for me": "💧 私には合わない",
        "🤔 Thought:": "🤔 考えた：",
        "·": "·",
        "🚶 Tried:": "🚶 やってみた：",
        "/6": "/6",
        "Thinking or trying. Which one clears the fog?": "考える？やってみる？霧が晴れるのはどっち？",
        "Hmm… still foggy. Thinking alone does not clear it.": "うーん…まだ霧の中。考えるだけでは晴れません。",
        "The fog cleared! You found something new.": "霧が晴れた！新しい自分を見つけた。",
        "🗺️ Map complete! ⭐ 3 likes and 💧 3 not-for-me. Both are treasures.": "🗺️ 地図が完成！⭐ 好きが3つ、💧 合わないが3つ。どっちも宝物。",
        "🤔 Just think": "🤔 じっと考える",
        "🚶 Try something": "🚶 やってみる",
        "↺ Start over": "↺ 最初から",
    },
)
build(d)
