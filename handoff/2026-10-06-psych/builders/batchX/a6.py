from gen import build

d = dict(
    slug="strength-is-what-makes-you-forget-time", seq=527,
    title=("Your strength is the thing that makes you forget the time",
           "強みは、時間を忘れて夢中になれること"),
    label=("Forget the Clock", "時計を忘れる"),
    h1_emoji="⏰",
    alt="A chubby chenille yarn penguin happily drawing, with a real red twin-bell alarm clock beside it",
    section="一番大事なのは「戦わない」こと（②強みを活かす）",
    message="強みとは、時間を忘れて夢中になれること。今はへたでも、夢中になれるならすぐうまくなる。",
    tone="素材の重さ：真面目（生き方の考え方）\n→ 見せ方：ポップに（トマトの赤とミントグリーン。時計の針で遊べる）",
    game_ja="⏰ ペンギンの1日：ペンギンの4つの用事（🧺 洗濯物をたたむ／🗺️ 地図をかく／📄 書類を書く／🍳 新しいレシピ）を押す。つまらない用事だと時計の針がカチ…カチ…とのろのろ動いて「まだ2分…1時間くらいに感じる 😪」。夢中になれる用事だと針がぐるぐる回って時計がうすくなり「えっ、もう2時間？ ✨」。夢中の用事を見つけるたびに「⭐ 強み発見 1/2」。2つ見つけると「あなたが時計を忘れるのは、どんなとき？」。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of soft chenille yarn with a "
            "velvety texture, sitting at a small desk happily drawing with a pencil, with a realistic red twin-bell alarm clock standing beside it. "
            "Bright simple tomato red and mint green background with soft depth. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × シェニール糸 × 赤い目覚まし時計",
    mood=["lift", "energy"], tags=["psychology", "mindset", "study"],
    pal=dict(bg="#fff6f3", muted="#86675f", acc="#e2483d", acc2="#22c39a", shadow="rgba(160,60,50,.16)",
             r1="rgba(255,120,100,.24)", r2="rgba(40,210,160,.20)", r3="rgba(255,210,90,.20)",
             h1="#4a1612", photo="#ffe5df", big="#c63a30", bigdark="#ffb3a8",
             game="linear-gradient(150deg, #ff6a5b 0%, #ff9248 45%, #1fc29a 100%)"),
    cards=[
        dict(emoji="⏰", label=("What It Is", "強みとは"),
             s=[("A strength is something you love so much that you forget the time.",
                 "強みとは、時間を忘れて夢中になれることです。")]),
        dict(emoji="🌱", label=("Bad Now OK", "今はへたでも"),
             s=[("Even if you are worse than others now, you will get better fast if you love it.",
                 "今は人よりへたでも、夢中になれるなら、すぐにうまくなります。")]),
        dict(emoji="🏃", label=("Love Wins", "夢中が勝つ"),
             s=[("Because hard work cannot win against loving something.",
                 "努力は、夢中には勝てないからです。")]),
        dict(emoji="🔍", label=("Find Yours", "見つけ方"), big=True,
             s=[("If you forgot to look at the clock, that may be your strength.",
                 "時計を見るのを忘れていたら、それがあなたの強みかもしれません。")]),
    ],
    game_after=3,
    game_note="ペンギンの1日（時計がのろのろ／時計がぐるぐる）",
    game_html="""  <section class="game" data-p="" data-r="" data-found="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">A penguin's day</div>
    <div class="game-hint">Tap a thing to do. Watch the clock!</div>
    <div class="clock" aria-hidden="true">
      <div class="tick t12"></div><div class="tick t3"></div><div class="tick t6"></div><div class="tick t9"></div>
      <div class="hand h-long"></div>
      <div class="hand h-short"></div>
      <div class="pin"></div>
      <div class="pface"><span class="pf">🐧</span></div>
    </div>
    <div class="msg">
      <div class="m-idle">Which one makes the clock disappear?</div>
      <div class="m-play">…</div>
      <div class="m-slow">Only 2 minutes passed… but it felt like 1 hour. 😪</div>
      <div class="m-fast">What?! 2 hours passed in a blink! ✨ This is a strength.</div>
    </div>
    <div class="todo">
      <button type="button" class="btn job" data-k="slow" data-n="0">🧺 Folding laundry</button>
      <button type="button" class="btn job" data-k="fast" data-n="1">🗺️ Drawing maps</button>
      <button type="button" class="btn job" data-k="slow" data-n="2">📄 Filling in forms</button>
      <button type="button" class="btn job" data-k="fast" data-n="3">🍳 A new recipe</button>
    </div>
    <div class="found"><span class="fd-l">⭐ Strengths found:</span> <span class="fn">0</span><span class="fd-of">/2</span></div>
    <div class="end">🐧 This penguin's strengths: maps and cooking. And you? When do you forget the clock?</div>
  </section>""",
    css="""
  /* ⏰ ペンギンの1日 */
  .clock { position: relative; width: 200px; height: 200px; margin: 18px auto 0; border-radius: 50%; background: #fff;
    box-shadow: 0 0 0 10px #ffd6cf, 0 12px 0 10px rgba(0,0,0,.12); transition: opacity .6s ease, transform .6s ease; }
  .tick { position: absolute; left: 50%; top: 50%; width: 6px; height: 16px; margin: -8px 0 0 -3px; border-radius: 3px; background: #e2483d; }
  .t12 { transform: rotate(0deg) translateY(-82px); } .t3 { transform: rotate(90deg) translateY(-82px); }
  .t6 { transform: rotate(180deg) translateY(-82px); } .t9 { transform: rotate(270deg) translateY(-82px); }
  .hand { position: absolute; left: 50%; bottom: 50%; border-radius: 4px; transform-origin: 50% 100%; transform: rotate(var(--a, 0deg)); }
  .h-long { width: 6px; height: 74px; margin-left: -3px; background: #2f2a3a; }
  .h-short { width: 8px; height: 48px; margin-left: -4px; background: #e2483d; --a: 60deg; }
  .pin { position: absolute; left: 50%; top: 50%; width: 16px; height: 16px; margin: -8px 0 0 -8px; border-radius: 50%; background: #2f2a3a; }
  .pface { position: absolute; left: 50%; top: 66%; transform: translateX(-50%); font-size: 34px; line-height: 1; }
  .game[data-p="slow"] .h-long { animation: slowTick 2.4s steps(2, end) both; }
  .game[data-p="fast"] .h-long { animation: spinLong 2.4s ease-in both; }
  .game[data-p="fast"] .h-short { animation: spinShort 2.4s ease-in both; }
  .game[data-p="fast"] .clock { opacity: .25; transform: scale(.9) rotate(-6deg); }
  .game[data-r="fast"] .clock { opacity: .35; }
  .game[data-p="slow"] .clock { animation: drowsy 2.4s ease-in-out both; }
  @keyframes slowTick { from { transform: rotate(0deg); } to { transform: rotate(12deg); } }
  @keyframes spinLong { from { transform: rotate(0deg); } to { transform: rotate(1440deg); } }
  @keyframes spinShort { from { transform: rotate(60deg); } to { transform: rotate(180deg); } }
  @keyframes drowsy { 0%, 100% { transform: none; } 30% { transform: rotate(-3deg); } 60% { transform: rotate(3deg); } }
  .msg { margin-top: 16px; min-height: 52px; font-size: 16.5px; font-weight: 900; line-height: 1.4; }
  .msg > div { display: none; }
  .game[data-p=""][data-r=""] .m-idle, .game[data-p="slow"] .m-play, .game[data-p="fast"] .m-play,
  .game[data-p=""][data-r="slow"] .m-slow, .game[data-p=""][data-r="fast"] .m-fast { display: block; animation: boing .45s ease; }
  .todo { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 380px; margin: 10px auto 0; }
  .job { min-height: 60px; padding: 8px 10px; font-size: 15px; background: #fff; color: #5a2019; }
  .job.seen-fast { background: #fff1b3; color: #5a4200; }
  .job.seen-slow { background: #e9e6ee; color: #5c5666; }
  .found { margin-top: 12px; font-size: 15.5px; font-weight: 900; }
  .fn { display: inline-block; min-width: 1.2em; padding: 2px 8px; border-radius: 999px; background: rgba(255,255,255,.3); }
  .end { display: none; margin: 12px auto 0; max-width: 380px; padding: 12px 14px; border-radius: 18px; background: #fff; color: #4a1612; font-size: 15.5px; font-weight: 900; line-height: 1.45; }
  .game[data-found="2"] .end { display: block; animation: boing .5s ease; }
""",
    dark="""  html[data-theme="dark"] .clock { background: #2b2d3a; box-shadow: 0 0 0 10px #5a2a26, 0 12px 0 10px rgba(0,0,0,.25); }
  html[data-theme="dark"] .h-long, html[data-theme="dark"] .pin { background: #f4f0fa; }
  html[data-theme="dark"] .game .job { background: #2b2d3a; color: #ffd6cf; }
  html[data-theme="dark"] .game .job.seen-fast { background: #4a3c12; color: #ffe39a; }
  html[data-theme="dark"] .game .job.seen-slow { background: #34364a; color: #c9c3d6; }
  html[data-theme="dark"] .end { background: #22242f; color: #ffd6cf; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var pf = g.querySelector('.pf'), fn = g.querySelector('.fn'), jobs = g.querySelectorAll('.job'), found = {}, t = 0;
  function pop(el, list) {
    if (!window.pengessoPop) return;
    var r = el.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, 16);
  }
  [].forEach.call(jobs, function (b) {
    b.addEventListener('click', function () {
      if (g.getAttribute('data-p')) return;
      var k = b.getAttribute('data-k');
      [].forEach.call(jobs, function (x) { x.disabled = true; });
      g.setAttribute('data-r', '');
      g.setAttribute('data-p', k);
      pf.textContent = k === 'fast' ? '🤩' : '😪';
      clearTimeout(t);
      t = setTimeout(function () {
        g.setAttribute('data-p', ''); g.setAttribute('data-r', k);
        b.classList.add('seen-' + k);
        [].forEach.call(jobs, function (x) { x.disabled = false; });
        if (k === 'fast') {
          found[b.getAttribute('data-n')] = 1;
          var n = Object.keys(found).length;
          fn.textContent = n; g.setAttribute('data-found', String(n));
          pop(g.querySelector('.clock'), ['⭐', '✨', '🐧', '⏰']);
        } else pf.textContent = '🥱';
      }, 2450);
    });
  });
})();
""",
    ja={
        "A penguin's day": "ペンギンの1日",
        "Tap a thing to do. Watch the clock!": "用事を押してね。時計に注目！",
        "Which one makes the clock disappear?": "時計が消えちゃうのは、どれかな？",
        "…": "…",
        "Only 2 minutes passed… but it felt like 1 hour. 😪": "まだ2分…なのに、1時間くらいに感じる。😪",
        "What?! 2 hours passed in a blink! ✨ This is a strength.": "えっ、あっという間に2時間たってた！✨ これが強み。",
        "🧺 Folding laundry": "🧺 洗濯物をたたむ",
        "🗺️ Drawing maps": "🗺️ 地図をかく",
        "📄 Filling in forms": "📄 書類を書く",
        "🍳 A new recipe": "🍳 新しいレシピ",
        "⭐ Strengths found:": "⭐ 見つけた強み：",
        "/2": "/2",
        "🐧 This penguin's strengths: maps and cooking. And you? When do you forget the clock?": "🐧 このペンギンの強みは、地図と料理。あなたは？時計を忘れるのは、どんなとき？",
    },
)
build(d)
