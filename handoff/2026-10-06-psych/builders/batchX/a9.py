from gen import build

d = dict(
    slug="pay-first-so-you-dont-quit", seq=530,
    title=("Pay first so you do not quit before the fun begins",
           "面白くなる前にやめないよう、先にお金を払って引くに引けなくする"),
    label=("Pay First", "先に払う"),
    h1_emoji="🎟️",
    alt="A chubby alpaca wool penguin hugging a real brand-new ukulele with a happy, determined face",
    section="一番大事なのは「戦わない」こと（③なんとなく興味があることを、勇気を出してやってみる）",
    message="新しいことは面白さに気づく前にやめやすい。スクールや道具に先にお金を払って、引くに引けなくするのも手（無理のない金額で）。",
    tone="素材の重さ：真面目（生き方の考え方）\n→ 見せ方：ポップに（ウクレレの木の色とライムグリーン。1日ずつ進める「やめたいグラフ」で遊べる）",
    game_ja="📈 やめたいグラフ：ウクレレを始めたペンギンの10日間。まず「💸 まだ払っていない」か「🎟️ 教室代をもう払った」を選んで、「▶ 次の日」を押していく。「やめたい気持ち」の棒が日ごとにのびる。払っていないと、やめるラインが低くて3日目に「💤 やめちゃった。面白さは7日目に待っていたのに…」。払ってあると、「もったいない！」でラインが高くなり、7日目に ⭐「面白くなってきた！」。お金のアドバイスはしない（「無理のない金額で」と本文に書く）。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of soft alpaca wool with a "
            "fluffy texture, hugging a realistic brand-new wooden ukulele with both flippers, looking happy and determined. "
            "Bright simple warm wood beige and lime green background with soft depth. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × アルパカの毛 × ウクレレ",
    mood=["lift", "learn"], tags=["psychology", "tips", "study"],
    pal=dict(bg="#f8fbef", muted="#6f7a58", acc="#5a9e1a", acc2="#e8913a", shadow="rgba(80,120,30,.16)",
             r1="rgba(232,145,58,.26)", r2="rgba(140,210,60,.22)", r3="rgba(255,214,90,.20)",
             h1="#2a3d0f", photo="#eef6dc", big="#4a8714", bigdark="#c3ec8f",
             game="linear-gradient(150deg, #7cc63a 0%, #3fae6a 45%, #e8913a 100%)"),
    cards=[
        dict(emoji="🌱", label=("Easy to Quit", "やめやすい"),
             s=[("With new things, it is easy to quit before you find the fun.",
                 "新しいことは、面白さに気づく前に、やめてしまいやすいです。"),
                ("At first, you are bad at it, and it is boring.",
                 "最初は、へたで、つまらないからです。")]),
        dict(emoji="🎟️", label=("Pay First", "先に払う"), big=True,
             s=[("So paying for a class or tools first, so you cannot easily quit, is a good idea too.",
                 "だから、スクールや道具に先にお金を払って、引くに引けない状況を作るのも手です。")]),
        dict(emoji="😤", label=("What a Waste", "もったいない"),
             s=[("The feeling \"What a waste!\" pushes you until it gets fun.",
                 "「もったいない！」という気持ちが、面白くなるまで背中を押してくれます。")]),
        dict(emoji="👛", label=("Not Too Much", "無理なく"),
             s=[("Of course, only an amount that is OK for you.",
                 "もちろん、無理のない金額で。")]),
    ],
    game_after=3,
    game_note="やめたいグラフ（払っていない／もう払った）",
    game_html="""  <section class="game" data-m="free" data-day="0" data-end="" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">The "I want to quit" chart</div>
    <div class="game-hint">A penguin starts the ukulele. Pick one, then go day by day.</div>
    <div class="mode">
      <button type="button" class="btn md md-free">💸 Not paid yet</button>
      <button type="button" class="btn md md-paid">🎟️ Already paid for the class</button>
    </div>
    <div class="chart" aria-hidden="true">
      <div class="qline"><span class="ql-t">🏳️ Quit line</span></div>
      <div class="cols">
        <div class="col"><i></i></div><div class="col"><i></i></div><div class="col"><i></i></div><div class="col"><i></i></div><div class="col"><i></i></div>
        <div class="col"><i></i></div><div class="col c7"><i></i><span class="fun"><span class="fun-e">⭐</span></span></div><div class="col"><i></i></div><div class="col"><i></i></div><div class="col"><i></i></div>
      </div>
    </div>
    <div class="legend"><span class="lg-bar"></span><span class="lg-t">😩 I want to quit</span></div>
    <div class="daylbl"><span class="dl-t">📅 Days:</span> <span class="dn">0</span><span class="dl-of">/10</span></div>
    <button type="button" class="btn nextday">▶ Next day</button>
    <div class="msg">
      <div class="m-start">Day 1 to day 10. Can the penguin reach the fun part?</div>
      <div class="m-go">Practice, practice… 🎶</div>
      <div class="m-quit">💤 Day 3: the penguin quit. The fun was waiting on day 7…</div>
      <div class="m-fun">⭐ Day 7: it got fun! "What a waste!" kept the penguin going.</div>
    </div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Try again</button></div>
  </section>""",
    css="""
  /* 📈 やめたいグラフ */
  .mode { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; max-width: 380px; margin: 14px auto 0; }
  .md { min-height: 60px; padding: 8px 10px; font-size: 14.5px; background: rgba(255,255,255,.25); color: #fff; box-shadow: inset 0 0 0 2px rgba(255,255,255,.6); }
  .game[data-m="free"] .md-free, .game[data-m="paid"] .md-paid { background: #fff; color: #2a3d0f; box-shadow: 0 5px 0 rgba(0,0,0,.18); }
  .chart { position: relative; max-width: 360px; height: 190px; margin: 16px auto 0; padding: 10px 10px 0; border-radius: 22px; background: #fff; }
  .cols { position: absolute; left: 10px; right: 10px; bottom: 0; top: 10px; display: grid; grid-template-columns: repeat(10, 1fr); gap: 6px; align-items: end; }
  .col { position: relative; height: 100%; }
  .col i { position: absolute; left: 0; right: 0; bottom: 0; height: 0; border-radius: 8px 8px 0 0; background: #ff8a65; transition: height .35s cubic-bezier(.2,1.3,.4,1); }
  .col.over i { background: #e8455a; }
  .col.ok i { background: #9ad06a; }
  .fun { position: absolute; left: 50%; top: 4px; transform: translateX(-50%) scale(0); font-size: 26px; line-height: 1; transition: transform .4s cubic-bezier(.2,1.6,.4,1); }
  .game[data-end="fun"] .fun { transform: translateX(-50%) scale(1.2); }
  .qline { position: absolute; left: 4px; right: 4px; bottom: 66%; border-top: 4px dashed #e8455a; z-index: 1; transition: bottom .4s ease; }
  .game[data-m="paid"] .qline { bottom: 88%; border-top-color: #3a8a1a; }
  .ql-t { position: absolute; right: 0; top: -26px; padding: 2px 8px; border-radius: 999px; background: #ffe3e3; color: #8a1f2f; font-size: 12px; font-weight: 900; }
  .game[data-m="paid"] .ql-t { background: #e2f5cf; color: #2a5a0f; }
  .legend { display: flex; justify-content: center; align-items: center; gap: 6px; margin-top: 8px; font-size: 13.5px; font-weight: 900; }
  .lg-bar { width: 14px; height: 14px; border-radius: 4px; background: #ff8a65; }
  .nextday { display: flex; flex-wrap: wrap; width: min(320px, 100%); min-height: 64px; margin: 12px auto 0; font-size: 19px; background: #ffe066; color: #4a3500; }
  .daylbl { margin-top: 10px; font-size: 16px; font-weight: 900; }
  .dn { display: inline-block; padding: 2px 8px; border-radius: 999px; background: rgba(255,255,255,.3); }
  .game[data-end]:not([data-end=""]) .nextday { opacity: .4; pointer-events: none; }
  .msg { margin-top: 12px; min-height: 52px; font-size: 16.5px; font-weight: 900; line-height: 1.4; }
  .msg > div { display: none; }
  .game[data-day="0"] .m-start, .game:not([data-day="0"])[data-end=""] .m-go, .game[data-end="quit"] .m-quit, .game[data-end="fun"] .m-fun { display: block; animation: boing .45s ease; }
  .game[data-end="quit"] .chart { animation: shake .4s ease; }
  .ctrl { margin-top: 10px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
""",
    dark="""  html[data-theme="dark"] .chart { background: #22242f; }
  html[data-theme="dark"] .game[data-m="free"] .md-free, html[data-theme="dark"] .game[data-m="paid"] .md-paid { background: #f4f0fa; color: #2a3d0f; }
  html[data-theme="dark"] .ql-t { background: #4a2228; color: #ffd0d6; }
  html[data-theme="dark"] .game[data-m="paid"] .ql-t { background: #24401a; color: #d4f5b8; }
  html[data-theme="dark"] .game .nextday { background: #4a3c12; color: #ffe39a; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var QUIT = [3, 5, 7, 8, 8, 6, 4, 3, 2, 1];          /* 「やめたい」は最初の数日がいちばん強い（10点満点） */
  var LINE = { free: 6.6, paid: 8.8 };                /* グラフの線の高さ（CSS の bottom: 66% / 88% と同じ） */
  var cols = g.querySelectorAll('.col'), dn = g.querySelector('.dn'), day = 0;
  function pop(el, list) {
    if (!window.pengessoPop) return;
    var r = el.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, 18);
  }
  function reset() {
    day = 0; dn.textContent = '0';
    g.setAttribute('data-day', '0'); g.setAttribute('data-end', '');
    [].forEach.call(cols, function (c) { c.classList.remove('over', 'ok'); c.querySelector('i').style.height = '0'; });
  }
  [['.md-free', 'free'], ['.md-paid', 'paid']].forEach(function (p) {
    g.querySelector(p[0]).addEventListener('click', function () { g.setAttribute('data-m', p[1]); reset(); });
  });
  g.querySelector('.nextday').addEventListener('click', function () {
    if (g.getAttribute('data-end') || day >= 10) return;
    day++; dn.textContent = day; g.setAttribute('data-day', String(day));
    var q = QUIT[day - 1], c = cols[day - 1], line = LINE[g.getAttribute('data-m')];
    c.querySelector('i').style.height = (q * 10) + '%';
    if (q >= line) {
      c.classList.add('over'); g.setAttribute('data-end', 'quit');
      if (navigator.vibrate) { try { navigator.vibrate([20, 40, 20]); } catch (e) {} }
    } else {
      if (day >= 7) c.classList.add('ok');
      if (day === 7) { g.setAttribute('data-end', 'fun'); pop(g.querySelector('.c7'), ['⭐', '🎶', '🐧', '✨', '🎉']); }
    }
  });
  g.querySelector('.b-reset').addEventListener('click', reset);
})();
""",
    ja={
        "The \"I want to quit\" chart": "「やめたい」グラフ",
        "A penguin starts the ukulele. Pick one, then go day by day.": "ペンギンがウクレレを始めました。どちらかを選んで、1日ずつ進めてね。",
        "💸 Not paid yet": "💸 まだ払っていない",
        "🎟️ Already paid for the class": "🎟️ 教室代をもう払った",
        "🏳️ Quit line": "🏳️ やめるライン",
        "😩 I want to quit": "😩 やめたい気持ち",
        "▶ Next day": "▶ 次の日",
        "📅 Days:": "📅 日数：",
        "/10": "/10",
        "Day 1 to day 10. Can the penguin reach the fun part?": "1日目から10日目まで。ペンギンは、面白くなるところまで行けるかな？",
        "Practice, practice… 🎶": "練習、練習… 🎶",
        "💤 Day 3: the penguin quit. The fun was waiting on day 7…": "💤 3日目：ペンギンはやめちゃった。面白さは7日目に待っていたのに…",
        "⭐ Day 7: it got fun! \"What a waste!\" kept the penguin going.": "⭐ 7日目：面白くなってきた！「もったいない！」が、ペンギンを続けさせてくれた。",
        "↺ Try again": "↺ もう一回",
    },
)
build(d)
