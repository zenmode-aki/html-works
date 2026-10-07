from gen import build

d = dict(
    slug="you-cant-control-the-result", seq=512,
    title=("You cannot control the result or other people's hearts, only your actions",
           "結果と人の心はコントロールできない。できるのは自分の行動だけ"),
    label=("Your Remote", "自分のリモコン"),
    h1_emoji="📺",
    alt="A chubby matte plastic model kit penguin holding a real TV remote control and pressing a big button",
    section="幸せは「自立」から",
    message="結果と人の心にはリモコンが効かない。効くのは自分の行動と信じること。そこに集中する。",
    tone="素材の重さ：真面目（生き方の考え方）\n→ 見せ方：ポップに（水色とオレンジ。テレビのリモコンで遊べる）",
    game_ja="📺 リモコン・テスト：リモコンの4つのボタン（自分の行動／自分の言葉／結果／相手の心）を押す。自分の行動と言葉は画面がパッと明るくなって「効いた！」。結果と相手の心は砂嵐で「📡 電波なし…」と画面がゆれる。4つ全部試すと「🎯 集中モード」ボタンが出て、押すと効かない2つのボタンが暗くなり、効く2つだけが光る。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made as a matte plastic model kit "
            "with soft rounded parts, sitting on a sofa cushion and pointing a realistic black TV remote control forward with both flippers, "
            "looking calm and focused. Bright simple sky-blue and warm orange background with soft depth, an empty sofa edge blurred behind. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × マットなプラモデル × テレビのリモコン",
    mood=["lift", "think"], tags=["psychology", "mindset", "happiness"],
    pal=dict(bg="#f1fbfd", muted="#5f7c86", acc="#0b95aa", acc2="#ff8a3d", shadow="rgba(20,90,110,.16)",
             r1="rgba(255,170,90,.30)", r2="rgba(15,181,201,.20)", r3="rgba(59,124,255,.14)",
             h1="#113a48", photo="#dff6fa", big="#08788a", bigdark="#86e6f2",
             game="linear-gradient(150deg, #10b6ca 0%, #3b7cff 58%, #ff8a3d 100%)"),
    cards=[
        dict(emoji="📡", label=("No Signal", "電波なし"),
             s=[("The result and other people's hearts do not obey your remote control, however hard you try.",
                 "結果と人の心には、どんなに頑張ってもリモコンが効きません。")]),
        dict(emoji="✅", label=("It Works", "効くもの"),
             s=[("But your actions and what you believe do obey it.",
                 "でも、自分の行動と、自分が信じることには、ちゃんと効きます。")]),
        dict(emoji="🎯", label=("Focus Here", "ここに集中"), big=True,
             s=[("So I do not expect too much from what does not obey, and I focus on what does.",
                 "だから、効かないものには期待しすぎず、効くものに集中します。")]),
        dict(emoji="🎧", label=("English Test", "英語のテスト"),
             s=[("For an English test, I point the remote at \"listen for 20 minutes a day,\" not at the score.",
                 "英語のテストなら、点数ではなく「毎日20分聞く」にリモコンを向けます。")]),
    ],
    game_after=2,
    game_note="リモコン・テスト（効くボタンと、効かないボタン）",
    game_html="""  <section class="game" data-ch="idle" data-all="0" data-focus="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">The remote control test</div>
    <div class="game-hint">Press each button. Which ones really work?</div>
    <div class="tv">
      <div class="screen">
        <div class="sc sc-idle"><span class="sc-e">📺</span><span class="sc-t">Press a button on the remote.</span></div>
        <div class="sc sc-act"><span class="sc-e">🐧📚</span><span class="sc-t">You study for 20 minutes. It works!</span></div>
        <div class="sc sc-word"><span class="sc-e">🐧💬</span><span class="sc-t">You say "thank you" first. It works!</span></div>
        <div class="sc sc-result"><span class="sc-e">📡</span><span class="sc-t">No signal… The score is not on your remote.</span></div>
        <div class="sc sc-heart"><span class="sc-e">📡</span><span class="sc-t">No signal… Their heart has its own remote.</span></div>
        <div class="sc sc-focus"><span class="sc-e">🎯🐧</span><span class="sc-t">Focus mode: only the buttons that work. So much lighter!</span></div>
      </div>
      <div class="tv-leg" aria-hidden="true"></div>
    </div>
    <div class="remote">
      <div class="ir" aria-hidden="true"></div>
      <div class="keys">
        <button type="button" class="btn rk ok" data-k="act">⚡ My actions</button>
        <button type="button" class="btn rk ok" data-k="word">💬 My words</button>
        <button type="button" class="btn rk ng" data-k="result">🏁 The result</button>
        <button type="button" class="btn rk ng" data-k="heart">💗 Their heart</button>
      </div>
    </div>
    <div class="tally"><span class="tl-w">✅ It works:</span> <span class="nw">0</span> <span class="tl-sep">·</span> <span class="tl-n">📡 No signal:</span> <span class="nn">0</span></div>
    <div class="focus-row">
      <div class="f-hint">Try all 4 buttons.</div>
      <button type="button" class="btn b-focus">🎯 Focus mode</button>
      <div class="f-done">🎉 Now you only press what works.</div>
    </div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Start over</button></div>
  </section>""",
    css="""
  /* 📺 リモコン・テスト */
  .tv { max-width: 380px; margin: 16px auto 0; padding: 12px; border-radius: 24px; background: #1d2336; box-shadow: 0 10px 0 rgba(0,0,0,.18); }
  .screen { position: relative; min-height: 150px; display: grid; place-items: center; border-radius: 16px; overflow: hidden;
    background: radial-gradient(circle at 50% 40%, #e9fdff, #aeeef7); color: #15303b; transition: background .25s ease; }
  .tv-leg { width: 90px; height: 10px; margin: 10px auto 0; border-radius: 999px; background: #3a4260; }
  .sc { display: none; position: relative; z-index: 1; padding: 14px 16px; }
  .sc-e { display: block; font-size: 46px; line-height: 1.1; margin-bottom: 6px; }
  .sc-t { display: block; font-size: 17px; font-weight: 900; line-height: 1.4; }
  .game[data-ch="idle"] .sc-idle, .game[data-ch="act"] .sc-act, .game[data-ch="word"] .sc-word,
  .game[data-ch="result"] .sc-result, .game[data-ch="heart"] .sc-heart, .game[data-ch="focus"] .sc-focus { display: block; animation: boing .45s ease; }
  .game[data-ch="act"] .screen, .game[data-ch="word"] .screen { background: radial-gradient(circle at 50% 40%, #fffbe0, #ffd36b); }
  .game[data-ch="focus"] .screen { background: radial-gradient(circle at 50% 40%, #f2fff7, #8ff0c3); }
  /* 砂嵐（横じま。点々は使わない） */
  .screen::before { content: ""; position: absolute; inset: 0; opacity: 0; transition: opacity .2s ease;
    background: repeating-linear-gradient(0deg, rgba(255,255,255,.55) 0 3px, rgba(120,130,150,.55) 3px 7px, rgba(220,225,235,.6) 7px 9px);
    background-size: 100% 18px; }
  .game[data-ch="result"] .screen, .game[data-ch="heart"] .screen { background: #9aa3b5; color: #1d2336; animation: shake .4s ease; }
  .game[data-ch="result"] .screen::before, .game[data-ch="heart"] .screen::before { opacity: .75; animation: snow .35s steps(3) infinite; }
  .game[data-ch="result"] .sc-t, .game[data-ch="heart"] .sc-t { background: rgba(255,255,255,.85); border-radius: 12px; padding: 6px 10px; }
  @keyframes snow { to { background-position: 0 18px; } }

  .remote { max-width: 300px; margin: 16px auto 0; padding: 14px 14px 16px; border-radius: 34px 34px 46px 46px; background: #2b2f42;
    box-shadow: 0 8px 0 rgba(0,0,0,.22), inset 0 2px 0 rgba(255,255,255,.12); }
  .ir { width: 18px; height: 10px; margin: 0 auto 12px; border-radius: 999px; background: #ff5c5c; box-shadow: 0 0 10px #ff5c5c; opacity: .5; transition: opacity .1s; }
  .remote.blink .ir { opacity: 1; }
  .keys { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
  .rk { min-height: 64px; padding: 8px 8px; border-radius: 18px; font-size: 15px; }
  .rk.ok { background: #fff3c4; color: #5a3f00; }
  .rk.ng { background: #e6ecf7; color: #33405c; }
  .game[data-focus="1"] .rk.ok { background: #ffd34d; box-shadow: 0 6px 0 #c99a00, 0 0 18px rgba(255,211,77,.8); }
  .game[data-focus="1"] .rk.ng { opacity: .3; filter: grayscale(1); }

  .tally { margin-top: 14px; font-size: 15px; font-weight: 900; }
  .nw, .nn { display: inline-block; min-width: 1.4em; padding: 2px 8px; border-radius: 999px; background: rgba(255,255,255,.25); }
  .focus-row { margin-top: 12px; min-height: 56px; }
  .f-hint, .f-done { font-size: 15px; font-weight: 900; padding-top: 14px; }
  .b-focus, .f-done { display: none; }
  .game[data-all="1"] .f-hint { display: none; }
  .game[data-all="1"][data-focus="0"] .b-focus { display: inline-flex; background: #ffe066; color: #4a3500; animation: boing .6s ease; }
  .game[data-focus="1"] .f-done { display: block; }
  .ctrl { margin-top: 10px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
""",
    dark="""  html[data-theme="dark"] .screen { background: radial-gradient(circle at 50% 40%, #2c4a5a, #1b3340); color: #e6f8ff; }
  html[data-theme="dark"] .game[data-ch="act"] .screen, html[data-theme="dark"] .game[data-ch="word"] .screen { background: radial-gradient(circle at 50% 40%, #5a4a17, #3d3210); }
  html[data-theme="dark"] .game[data-ch="focus"] .screen { background: radial-gradient(circle at 50% 40%, #1f5a43, #133b2c); }
  html[data-theme="dark"] .game[data-ch="result"] .sc-t, html[data-theme="dark"] .game[data-ch="heart"] .sc-t { background: rgba(30,34,48,.9); color: #f4f0fa; }
  html[data-theme="dark"] .rk.ok { background: #4a3c12; color: #ffe39a; }
  html[data-theme="dark"] .rk.ng { background: #2c3446; color: #c9d3e8; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var remote = g.querySelector('.remote'), tried = {}, nw = 0, nn = 0, blinkT = 0;
  function count() { g.querySelector('.nw').textContent = nw; g.querySelector('.nn').textContent = nn; }
  function pop(el, list) {
    if (!window.pengessoPop) return;
    var r = el.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, 14);
  }
  function show(ch) {
    g.setAttribute('data-ch', 'idle'); void g.offsetWidth;   /* 同じボタンでも、もう一度アニメーションさせる */
    g.setAttribute('data-ch', ch);
  }
  [].forEach.call(g.querySelectorAll('.rk'), function (b) {
    b.addEventListener('click', function () {
      var k = b.getAttribute('data-k'), works = b.classList.contains('ok');
      if (g.getAttribute('data-focus') === '1' && !works) return;
      remote.classList.add('blink'); clearTimeout(blinkT); blinkT = setTimeout(function () { remote.classList.remove('blink'); }, 160);
      show(k); tried[k] = 1;
      if (works) { nw++; pop(g.querySelector('.screen'), ['✨', '🐧', '⭐']); }
      else { nn++; if (navigator.vibrate) { try { navigator.vibrate([20, 40, 20]); } catch (e) {} } }
      count();
      if (Object.keys(tried).length === 4) g.setAttribute('data-all', '1');
    });
  });
  g.querySelector('.b-focus').addEventListener('click', function () {
    g.setAttribute('data-focus', '1'); show('focus');
    [].forEach.call(g.querySelectorAll('.rk.ng'), function (b) { b.disabled = true; });
    pop(g.querySelector('.screen'), ['🎯', '🐧', '✨', '💪']);
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    tried = {}; nw = 0; nn = 0; count();
    g.setAttribute('data-all', '0'); g.setAttribute('data-focus', '0'); show('idle');
    [].forEach.call(g.querySelectorAll('.rk'), function (b) { b.disabled = false; });
  });
})();
""",
    ja={
        "The remote control test": "リモコン・テスト",
        "Press each button. Which ones really work?": "ボタンを1つずつ押してみてね。本当に効くのはどれ？",
        "Press a button on the remote.": "リモコンのボタンを押してね。",
        "You study for 20 minutes. It works!": "20分勉強した。効いた！",
        "You say \"thank you\" first. It works!": "自分から「ありがとう」と言えた。効いた！",
        "No signal… The score is not on your remote.": "電波なし…点数は、あなたのリモコンには入っていません。",
        "No signal… Their heart has its own remote.": "電波なし…相手の心には、相手のリモコンがあります。",
        "Focus mode: only the buttons that work. So much lighter!": "集中モード：効くボタンだけ。すごく気持ちが軽い！",
        "⚡ My actions": "⚡ 自分の行動",
        "💬 My words": "💬 自分の言葉",
        "🏁 The result": "🏁 結果",
        "💗 Their heart": "💗 相手の心",
        "✅ It works:": "✅ 効いた：",
        "·": "·",
        "📡 No signal:": "📡 電波なし：",
        "Try all 4 buttons.": "4つのボタンを全部ためしてね。",
        "🎯 Focus mode": "🎯 集中モード",
        "🎉 Now you only press what works.": "🎉 これで、効くボタンだけを押せます。",
        "↺ Start over": "↺ 最初から",
    },
)
build(d)
