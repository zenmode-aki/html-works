from gen import build

d = dict(
    slug="decide-whats-right-yourself", seq=525,
    title=("Decide what is right for yourself, and step off the race",
           "何が正しいかは自分で決める。オンリーワンを目指すと競争から降りられる"),
    label=("Only One", "オンリーワン"),
    h1_emoji="🏝️",
    alt="A chubby felted wool penguin sitting happily beside a real small wooden ladder lying on the sand of a tiny sunny island",
    section="一番大事なのは「戦わない」こと（①自分の価値観で生きる）",
    message="何が正しいかは自分で決めていい。オンリーワンを目指すと、競争から降りられる。",
    tone="素材の重さ：真面目（生き方の考え方）\n→ 見せ方：ポップに（夕日のオレンジと南の島のミント。ランキングのはしごで遊べる）",
    game_ja="🪜 ランキングのはしご：ペンギンがぎゅうぎゅうのはしご（1位〜5位）を「⬆ のぼる」。でも上に行くと「ドン！」と押し戻されて5位にもどる（押し戻された回数が増える）。3回のぼると「🏝️ 自分の島にジャンプ」ボタンが出る。島では、4つの旗（🍩 ドーナツ／🎸 ギター／🌻 お花／📚 本）から自分の旗を選ぶ → 島に旗が立って「順位：オンリーワン ⭐／競争：なし」。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of soft felted wool with a fuzzy "
            "texture, sitting happily on the sand of a tiny sunny island next to a realistic small wooden ladder lying on its side, "
            "calm turquoise water around. Bright simple sunset orange and mint background with soft depth. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × フェルト羊毛 × 木のはしご",
    mood=["lift", "think"], tags=["psychology", "mindset", "happiness"],
    pal=dict(bg="#fff8f0", muted="#82705e", acc="#e66a1f", acc2="#16b6a0", shadow="rgba(150,90,40,.16)",
             r1="rgba(255,160,80,.28)", r2="rgba(30,200,170,.20)", r3="rgba(255,220,100,.20)",
             h1="#47250c", photo="#ffeedd", big="#c9560f", bigdark="#ffc08f",
             game="linear-gradient(150deg, #ff9a4d 0%, #f26b5b 45%, #17b8a2 100%)"),
    cards=[
        dict(emoji="⚖️", label=("Your Call", "自分で決める"),
             s=[("I think you can decide what is right for yourself.",
                 "何が正しいかは、自分で決めていいと思います。")]),
        dict(emoji="🪜", label=("Same Ladder", "同じはしご"),
             s=[("If you aim for the same No. 1 as everyone, the race never ends.",
                 "みんなと同じ1位を目指すと、競争はずっと続きます。")]),
        dict(emoji="🏝️", label=("Step Off", "降りられる"), big=True,
             s=[("But if you aim to be the only one, you can step off that race.",
                 "でも、オンリーワンを目指すと、その競争から降りられます。")]),
        dict(emoji="🚩", label=("Nobody Copies", "まねできない"),
             s=[("The more you follow your own values, the more you become someone nobody can copy.",
                 "自分の価値観に従うほど、誰にもまねされない自分らしさが生まれます。")]),
    ],
    game_after=2,
    game_note="ランキングのはしご（のぼっても押し戻される → 自分の島へ）",
    game_html="""  <section class="game" data-v="ladder" data-r="5" data-climb="0" data-flag="" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">The ranking ladder</div>
    <div class="game-hint">Climb to No. 1! But the ladder is very crowded…</div>
    <div class="scene" aria-hidden="true">
      <div class="ladder">
        <div class="rung r1"><span class="rk-n">#1</span><span class="crowd">🐧🐧🐧</span></div>
        <div class="rung r2"><span class="rk-n">#2</span><span class="crowd">🐧🐧🐧</span></div>
        <div class="rung r3"><span class="rk-n">#3</span><span class="crowd">🐧🐧</span></div>
        <div class="rung r4"><span class="rk-n">#4</span><span class="crowd">🐧🐧</span></div>
        <div class="rung r5"><span class="rk-n">#5</span><span class="crowd">🐧</span></div>
        <div class="me"><span class="me-e">🐧</span></div>
        <div class="bump"><span class="bump-e">💥</span></div>
      </div>
      <div class="island">
        <div class="sun"><span class="sun-e">☀️</span></div>
        <div class="pole"><span class="flag-e">🏳️</span></div>
        <div class="me2"><span class="me2-e">🐧</span></div>
        <div class="sand"></div>
      </div>
    </div>
    <div class="stat st-l"><span class="st-a">Your rank:</span> <span class="st-hash">#</span><span class="rn">5</span> <span class="st-sep">·</span> <span class="st-b">Pushed down:</span> <span class="pn">0</span></div>
    <div class="stat st-i"><span class="st-c">Rank: only one ⭐ · Race: none</span></div>
    <div class="msg">
      <div class="m-ladder">Tap "Climb" and go up.</div>
      <div class="m-bump">Bump! Someone pushed you down. 😵</div>
      <div class="m-up">Up 1 step! Keep going?</div>
      <div class="m-island">You hopped to your own island. Now pick your flag.</div>
      <div class="m-flag">This is your island. Nobody needs to win here. 🎉</div>
    </div>
    <div class="ctrl c-ladder">
      <button type="button" class="btn climb">⬆ Climb</button>
      <button type="button" class="btn hop">🏝️ Hop to my own island</button>
    </div>
    <div class="ctrl c-island flags">
      <button type="button" class="btn fl" data-e="🍩">🍩 Donuts</button>
      <button type="button" class="btn fl" data-e="🎸">🎸 Guitar</button>
      <button type="button" class="btn fl" data-e="🌻">🌻 Flowers</button>
      <button type="button" class="btn fl" data-e="📚">📚 Books</button>
    </div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Start over</button></div>
  </section>""",
    css="""
  /* 🪜 ランキングのはしご */
  .scene { position: relative; max-width: 340px; height: 290px; margin: 16px auto 0; border-radius: 24px; overflow: hidden;
    background: linear-gradient(180deg, #ffe7c7, #ffd3a8); }
  .ladder, .island { position: absolute; inset: 0; transition: opacity .45s ease, transform .45s ease; }
  .ladder { padding: 12px 18px; display: grid; grid-template-rows: repeat(5, 1fr); gap: 0;
    background: linear-gradient(90deg, transparent 18%, #b5793d 18% 21%, transparent 21% 79%, #b5793d 79% 82%, transparent 82%); }
  .rung { display: flex; align-items: center; gap: 8px; padding: 0 14%; border-bottom: 7px solid #b5793d; }
  .rk-n { flex: 0 0 auto; min-width: 2em; font-size: 15px; font-weight: 900; color: #7a3d00; }
  .crowd { font-size: 24px; letter-spacing: -6px; line-height: 1; }
  .me { position: absolute; right: 26%; font-size: 36px; line-height: 1; transition: top .3s cubic-bezier(.3,1.4,.5,1); top: 82%; transform: translateY(-50%); }
  .me-e { display: inline-block; border-radius: 50%; box-shadow: 0 0 0 4px #ffe066, 0 0 16px #ffe066; background: rgba(255,224,102,.35); }
  .game[data-r="4"] .me { top: 63%; } .game[data-r="3"] .me { top: 44%; } .game[data-r="2"] .me { top: 25%; } .game[data-r="1"] .me { top: 7%; }
  .bump { position: absolute; right: 12%; top: 30%; font-size: 40px; opacity: 0; transform: scale(.3); }
  .game.bumped .bump { animation: bumpIn .7s ease both; }
  .game.bumped .scene { animation: shake .4s ease; }
  @keyframes bumpIn { 0% { opacity: 0; transform: scale(.3); } 30% { opacity: 1; transform: scale(1.3); } 100% { opacity: 0; transform: scale(1); } }
  .island { opacity: 0; transform: translateY(30px); pointer-events: none; background: linear-gradient(180deg, #9ff0ff, #5fd3e6); }
  .game[data-v="island"] .ladder { opacity: 0; transform: translateY(-30px); pointer-events: none; }
  .game[data-v="island"] .island { opacity: 1; transform: none; }
  .sand { position: absolute; left: 14%; right: 14%; bottom: 14%; height: 70px; border-radius: 50% 50% 40% 40%; background: #ffe4a3; box-shadow: 0 10px 0 #f2c873; }
  .sun { position: absolute; right: 10%; top: 8%; font-size: 40px; line-height: 1; }
  .pole { position: absolute; left: 40%; bottom: 30%; width: 6px; height: 110px; border-radius: 3px; background: #8a5a2b; z-index: 1; }
  .flag-e { position: absolute; left: 6px; top: -4px; font-size: 40px; line-height: 1; transform-origin: left center; }
  .game[data-flag="1"] .flag-e { animation: wave 1.6s ease-in-out infinite alternate; }
  @keyframes wave { from { transform: rotate(-6deg); } to { transform: rotate(6deg); } }
  .me2 { position: absolute; left: 52%; bottom: 26%; font-size: 46px; line-height: 1; z-index: 1; }
  .game[data-flag="1"] .me2-e { display: inline-block; animation: boing .6s ease 2; }
  .stat { margin-top: 12px; font-size: 15.5px; font-weight: 900; }
  .rn, .pn { display: inline-block; min-width: 1.2em; padding: 2px 8px; border-radius: 999px; background: rgba(255,255,255,.3); }
  .st-i, .game[data-v="island"] .st-l { display: none; }
  .game[data-v="island"] .st-i { display: block; }
  .msg { margin-top: 10px; min-height: 48px; font-size: 16.5px; font-weight: 900; line-height: 1.4; }
  .msg > div { display: none; }
  .game[data-v="ladder"][data-climb="0"] .m-ladder, .game[data-v="ladder"][data-climb="up"] .m-up, .game[data-v="ladder"][data-climb="bump"] .m-bump,
  .game[data-v="island"][data-flag=""] .m-island, .game[data-v="island"][data-flag="1"] .m-flag { display: block; animation: boing .45s ease; }
  .ctrl { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-top: 10px; }
  .climb { min-width: 180px; min-height: 60px; font-size: 19px; background: #fff; color: #7a3d00; }
  .hop { display: none; background: #ffe066; color: #4a3500; }
  .game[data-hop="1"] .hop { display: inline-flex; animation: boing .6s ease; }
  .c-island, .game[data-v="island"] .c-ladder { display: none; }
  .game[data-v="island"] .c-island { display: grid; grid-template-columns: 1fr 1fr; max-width: 360px; margin-left: auto; margin-right: auto; }
  .fl { background: #fff; color: #0d5c52; }
  .fl.on { background: #ffe066; color: #4a3500; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
""",
    dark="""  html[data-theme="dark"] .scene { background: linear-gradient(180deg, #4a3826, #3a2a1c); }
  html[data-theme="dark"] .rk-n { color: #ffd6a8; }
  html[data-theme="dark"] .island { background: linear-gradient(180deg, #1f5a66, #164550); }
  html[data-theme="dark"] .sand { background: #8a7444; box-shadow: 0 10px 0 #6a5630; }
  html[data-theme="dark"] .game .climb { background: #2b2d3a; color: #ffd6a8; }
  html[data-theme="dark"] .game .hop, html[data-theme="dark"] .game .fl.on { background: #4a3c12; color: #ffe39a; }
  html[data-theme="dark"] .game .fl:not(.on) { background: #2b2d3a; color: #b8f0e6; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  /* のぼる → 3位や2位まで行くと「ドン！」と5位へ。1位にはたどり着けない */
  var PATH = [4, 3, 5, 4, 3, 2, 5, 4, 3, 5];
  var step = 0, pushes = 0, rn = g.querySelector('.rn'), pn = g.querySelector('.pn'), flagE = g.querySelector('.flag-e');
  function pop(el, list) {
    if (!window.pengessoPop) return;
    var r = el.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, 16);
  }
  g.querySelector('.climb').addEventListener('click', function () {
    var cur = +g.getAttribute('data-r'), nxt = PATH[step % PATH.length];
    step++;
    g.classList.remove('bumped'); void g.offsetWidth;
    if (nxt > cur) {
      pushes++; pn.textContent = pushes; g.classList.add('bumped'); g.setAttribute('data-climb', 'bump');
      if (navigator.vibrate) { try { navigator.vibrate([20, 40, 20]); } catch (e) {} }
    } else g.setAttribute('data-climb', 'up');
    g.setAttribute('data-r', String(nxt)); rn.textContent = nxt;
    if (step >= 3) g.setAttribute('data-hop', '1');
  });
  g.querySelector('.hop').addEventListener('click', function () {
    g.setAttribute('data-v', 'island');
    pop(g.querySelector('.scene'), ['🏝️', '☀️', '🐧']);
  });
  [].forEach.call(g.querySelectorAll('.fl'), function (b) {
    b.addEventListener('click', function () {
      [].forEach.call(g.querySelectorAll('.fl'), function (x) { x.classList.remove('on'); });
      b.classList.add('on');
      flagE.textContent = b.getAttribute('data-e');
      g.setAttribute('data-flag', '1');
      pop(g.querySelector('.pole'), [b.getAttribute('data-e'), '⭐', '🐧', '✨']);
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    step = 0; pushes = 0; pn.textContent = '0'; rn.textContent = '5'; flagE.textContent = '🏳️';
    g.setAttribute('data-r', '5'); g.setAttribute('data-climb', '0'); g.setAttribute('data-v', 'ladder');
    g.setAttribute('data-flag', ''); g.removeAttribute('data-hop'); g.classList.remove('bumped');
    [].forEach.call(g.querySelectorAll('.fl'), function (x) { x.classList.remove('on'); });
  });
})();
""",
    ja={
        "The ranking ladder": "ランキングのはしご",
        "Climb to No. 1! But the ladder is very crowded…": "1位までのぼろう！でも、はしごはぎゅうぎゅう…",
        "#1": "#1", "#2": "#2", "#3": "#3", "#4": "#4", "#5": "#5",
        "Your rank:": "あなたの順位：",
        "#": "#",
        "·": "·",
        "Pushed down:": "押し戻された：",
        "Rank: only one ⭐ · Race: none": "順位：オンリーワン ⭐ · 競争：なし",
        "Tap \"Climb\" and go up.": "「のぼる」を押して、上へ行こう。",
        "Bump! Someone pushed you down. 😵": "ドン！押し戻されちゃった。😵",
        "Up 1 step! Keep going?": "1段のぼった！まだ行く？",
        "You hopped to your own island. Now pick your flag.": "自分の島にジャンプした。旗を選んでね。",
        "This is your island. Nobody needs to win here. 🎉": "ここはあなたの島。ここでは、誰も勝たなくていい。🎉",
        "⬆ Climb": "⬆ のぼる",
        "🏝️ Hop to my own island": "🏝️ 自分の島にジャンプ",
        "🍩 Donuts": "🍩 ドーナツ",
        "🎸 Guitar": "🎸 ギター",
        "🌻 Flowers": "🌻 お花",
        "📚 Books": "📚 本",
        "↺ Start over": "↺ 最初から",
    },
)
build(d)
