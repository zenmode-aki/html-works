from gen import build

d = dict(
    slug="expecting-is-leaning", seq=514,
    title=("Expecting is like leaning on a wall that can move at any time",
           "期待は、いつ動くか分からない壁に寄りかかること"),
    label=("Leaning", "寄りかかり"),
    h1_emoji="🧱",
    alt="A chubby felted wool penguin standing up straight on its own feet next to a real wooden garden fence",
    section="幸せは「自立」から",
    message="期待は、結果や人の心に寄りかかること。楽だけど、壁が動くたびに少しずつ苦しくなる。",
    tone="素材の重さ：真面目（依存と自立）\n→ 見せ方：ポップに（コーラルと空色。風が吹くと壁が動く）",
    game_ja="🌬️ 風と壁：ペンギンが「期待」の壁（返事がすぐ来るはず／ぜったい勝てるはず／ほめてもらえるはず）に寄りかかっている。「風がふく」を押すと壁がぐらっと動いて、寄りかかったペンギンは転ぶ（転んだ回数が増える）。「🐾 自分の足で立つ」に切りかえてから風を吹かせると、壁が動いてもペンギンは平気。3回たえると、まとめの一言。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of soft felted wool, "
            "standing up straight and steady on its own two feet beside a realistic short wooden garden fence that is tilting away, "
            "the penguin not touching it, looking calm and a little proud. Bright simple coral and sky-blue background with soft depth, "
            "a soft grassy ground. Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. "
            "Centered composition. No humans, no text, no lettering."),
    combo="ペンギン × ふわふわ羊毛フェルト × 木の柵",
    mood=["lift", "think"], tags=["psychology", "mindset", "feelings"],
    pal=dict(bg="#fff6f2", muted="#8a6f6a", acc="#e0485a", acc2="#2fa8f0", shadow="rgba(160,70,60,.16)",
             r1="rgba(255,150,120,.30)", r2="rgba(47,168,240,.18)", r3="rgba(255,206,90,.18)",
             h1="#4a1f24", photo="#ffe7e0", big="#c93347", bigdark="#ffadb8",
             game="linear-gradient(160deg, #3fb6ff 0%, #6f8dff 50%, #ff6f7d 100%)"),
    cards=[
        dict(emoji="🧱", label=("What It Is", "期待とは"),
             s=[("To \"expect\" something is to lean on the result or on other people's hearts.",
                 "何かに「期待する」というのは、結果や人の心に寄りかかることです。")]),
        dict(emoji="🛋️", label=("Easy At First", "最初は楽"),
             s=[("When you lean, if things go wrong, you can be \"poor me, pushed around,\" so it is a little easy.",
                 "寄りかかっていると、うまくいかないときに「振り回される、かわいそうな私」でいられるので、ちょっと楽です。")]),
        dict(emoji="🌬️", label=("Then It Hurts", "だんだん苦しい"),
             s=[("But every time the wall moves, you wobble, and little by little it gets hard.",
                 "でも、壁が動くたびにぐらぐらして、少しずつ苦しくなります。")]),
        dict(emoji="🐾", label=("Own Feet", "自分の足"), big=True,
             s=[("If you stand on your own feet, you do not fall when the wall moves.",
                 "自分の足で立っていれば、壁が動いても転びません。")]),
    ],
    game_after=2,
    game_note="風と壁（寄りかかると転ぶ・自分の足なら平気）",
    game_html="""  <section class="game" data-st="lean" data-fx="" data-w="1" data-end="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">The wind and the wall</div>
    <div class="game-hint">The penguin is leaning on an "I expect…" wall. Let the wind blow.</div>
    <div class="scene">
      <div class="say">
        <span class="s-lean">Leaning feels so easy… 😌</span>
        <span class="s-fall">Oops! The wall moved. 💫</span>
        <span class="s-stand">I am standing on my own feet.</span>
        <span class="s-ok">The wall moved, but I am OK!</span>
      </div>
      <div class="ground" aria-hidden="true"></div>
      <div class="pg"><span class="pg-e">🐧</span></div>
      <div class="wall">
        <span class="w-t w1">They will reply soon.</span>
        <span class="w-t w2">I will surely win.</span>
        <span class="w-t w3">They will praise me.</span>
      </div>
      <div class="gust" aria-hidden="true"></div>
    </div>
    <div class="ctl">
      <button type="button" class="btn b-wind">🌬️ The wind blows</button>
      <button type="button" class="btn b-stand"><span class="bs-a">🐾 Stand on my own feet</span><span class="bs-b">🛋️ Lean again</span></button>
    </div>
    <div class="score"><span class="sc-f">💫 Falls:</span> <span class="nf">0</span> <span class="sc-sep">·</span> <span class="sc-s">🐾 Steady:</span> <span class="ns">0</span><span class="sc-of"> / 3</span></div>
    <div class="end">🎉 The wall still moves. But now you do not fall.</div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Start over</button></div>
  </section>""",
    css="""
  /* 🌬️ 風と壁 */
  .scene { position: relative; height: 250px; max-width: 420px; margin: 16px auto 0; border-radius: 24px; overflow: hidden;
    background: linear-gradient(#bfe9ff, #e9f8ff 70%); }
  .ground { position: absolute; left: 0; right: 0; bottom: 0; height: 46px; background: #8fd36b; border-top: 4px solid #6cbf45; }
  .say { position: absolute; left: 12px; right: 12px; top: 12px; min-height: 44px; display: flex; align-items: center; justify-content: center;
    padding: 8px 12px; border-radius: 16px; background: #fff; color: #2f2a3a; font-size: 15.5px; font-weight: 900; line-height: 1.35; }
  .say span { display: none; }
  .game[data-st="lean"][data-fx=""] .s-lean, .game[data-fx="fall"] .s-fall,
  .game[data-st="stand"][data-fx=""] .s-stand, .game[data-fx="ok"] .s-ok { display: inline; }
  .pg { position: absolute; z-index: 1; left: 33%; bottom: 40px; font-size: 72px; line-height: 1; transform-origin: 70% 100%;
    transition: transform .35s cubic-bezier(.3,1.4,.5,1); }
  .game[data-st="lean"] .pg { transform: rotate(16deg); }
  .game[data-st="stand"] .pg { transform: none; }
  .game[data-fx="fall"] .pg { transform: rotate(95deg) translate(-10px, -18px); transition: transform .45s cubic-bezier(.5,0,.8,.4); }
  .wall { position: absolute; left: 58%; bottom: 44px; width: 116px; height: 140px; display: grid; place-items: center; padding: 10px;
    border-radius: 14px 14px 4px 4px; background: #ffb46b; border: 4px solid #e58b35; box-shadow: inset 0 -10px 0 rgba(0,0,0,.08);
    color: #5a2c00; font-size: 14px; font-weight: 900; line-height: 1.3; transform-origin: 50% 100%; }
  .w-t { display: none; }
  .game[data-w="1"] .w1, .game[data-w="2"] .w2, .game[data-w="3"] .w3 { display: block; }
  .game[data-fx="fall"] .wall, .game[data-fx="ok"] .wall { animation: wallgo 1.2s ease; }
  @keyframes wallgo { 0% { transform: none; } 30% { transform: translateX(60px) rotate(14deg); } 60% { transform: translateX(46px) rotate(9deg); } 100% { transform: none; } }
  .gust { position: absolute; left: -40%; top: 90px; width: 40%; height: 46px; opacity: 0;
    background: repeating-linear-gradient(180deg, transparent 0 9px, rgba(255,255,255,.95) 9px 13px); border-radius: 999px; }
  .game[data-fx="fall"] .gust, .game[data-fx="ok"] .gust { animation: gust .9s ease-out; }
  @keyframes gust { 0% { left: -40%; opacity: 0; } 20% { opacity: 1; } 100% { left: 110%; opacity: 0; } }
  .game[data-fx="ok"] .pg { animation: boing .5s .3s ease; }

  .ctl { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 420px; margin: 16px auto 0; }
  .ctl .btn { min-height: 60px; border-radius: 18px; font-size: 15px; padding: 8px 10px; }
  .b-wind { background: #e8f6ff; color: #0d4f7a; }
  .b-stand { background: #fff1a8; color: #5a4300; }
  .bs-b { display: none; }
  .game[data-st="stand"] .bs-a { display: none; } .game[data-st="stand"] .bs-b { display: inline; }
  .game[data-st="stand"] .b-stand { background: rgba(255,255,255,.22); color: #fff; box-shadow: inset 0 0 0 2px rgba(255,255,255,.7); }
  .score { margin-top: 14px; font-size: 15px; font-weight: 900; }
  .nf, .ns { display: inline-block; min-width: 1.4em; padding: 1px 8px; border-radius: 999px; background: rgba(255,255,255,.28); }
  .end { display: none; margin: 14px auto 0; max-width: 420px; padding: 12px 14px; border-radius: 18px; background: #fff; color: #7a1f2c; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .game[data-end="1"] .end { display: block; animation: boing .5s ease; }
  .ctrl { margin-top: 12px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
  @media (max-width: 380px) { .wall { width: 100px; font-size: 13px; } .pg { font-size: 62px; left: 30%; } }
""",
    dark="""  html[data-theme="dark"] .scene { background: linear-gradient(#1f3550, #2a4560 70%); }
  html[data-theme="dark"] .ground { background: #3f6b2c; border-top-color: #4f8a35; }
  html[data-theme="dark"] .say { background: #2b2d3a; color: #f4f0fa; }
  html[data-theme="dark"] .wall { background: #8a5a2a; border-color: #b0773e; color: #ffe9cf; }
  html[data-theme="dark"] .b-wind { background: #1f3a50; color: #cfeaff; }
  html[data-theme="dark"] .b-stand { background: #4a3c12; color: #ffe39a; }
  html[data-theme="dark"] .end { background: #2b2d3a; color: #ffc2cf; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var nf = 0, ns = 0, w = 1, busy = false, t = 0;
  function num() { g.querySelector('.nf').textContent = nf; g.querySelector('.ns').textContent = ns; }
  g.querySelector('.b-wind').addEventListener('click', function () {
    if (busy) return; busy = true;
    var st = g.getAttribute('data-st');
    g.setAttribute('data-fx', st === 'lean' ? 'fall' : 'ok');
    if (st === 'lean') { nf++; if (navigator.vibrate) { try { navigator.vibrate(40); } catch (e) {} } }
    else ns++;
    num();
    clearTimeout(t);
    t = setTimeout(function () {
      g.setAttribute('data-fx', '');
      w = w % 3 + 1; g.setAttribute('data-w', String(w));   /* 次の「期待」の壁へ */
      busy = false;
      if (ns >= 3 && g.getAttribute('data-end') !== '1') {
        g.setAttribute('data-end', '1');
        if (window.pengessoPop) { var r = g.querySelector('.pg').getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top, ['🐧', '🐾', '✨', '🎉'], 16); }
      }
    }, st === 'lean' ? 1500 : 1250);
  });
  g.querySelector('.b-stand').addEventListener('click', function () {
    if (busy) return;
    g.setAttribute('data-st', g.getAttribute('data-st') === 'lean' ? 'stand' : 'lean');
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    clearTimeout(t); busy = false; nf = 0; ns = 0; w = 1; num();
    g.setAttribute('data-st', 'lean'); g.setAttribute('data-fx', ''); g.setAttribute('data-w', '1'); g.setAttribute('data-end', '0');
  });
})();
""",
    ja={
        "The wind and the wall": "風と壁",
        "The penguin is leaning on an \"I expect…\" wall. Let the wind blow.": "ペンギンが「期待」の壁に寄りかかっています。風を吹かせてみて。",
        "Leaning feels so easy… 😌": "寄りかかるのって、楽だなあ… 😌",
        "Oops! The wall moved. 💫": "わっ！壁が動いた 💫",
        "I am standing on my own feet.": "自分の足で立っています。",
        "The wall moved, but I am OK!": "壁は動いたけど、平気！",
        "They will reply soon.": "すぐ返事が来るはず。",
        "I will surely win.": "ぜったい勝てるはず。",
        "They will praise me.": "ほめてもらえるはず。",
        "🌬️ The wind blows": "🌬️ 風がふく",
        "🐾 Stand on my own feet": "🐾 自分の足で立つ",
        "🛋️ Lean again": "🛋️ また寄りかかる",
        "💫 Falls:": "💫 転んだ：",
        "·": "·",
        "🐾 Steady:": "🐾 平気だった：",
        "/ 3": "/ 3",
        "🎉 The wall still moves. But now you do not fall.": "🎉 壁はやっぱり動きます。でも、もう転びません。",
        "↺ Start over": "↺ 最初から",
    },
)
build(d)
