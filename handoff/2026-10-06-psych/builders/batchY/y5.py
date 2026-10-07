from gen import build

d = dict(
    slug="dont-run-on-being-thanked", seq=536,
    title=("If being thanked is your only fuel, you will run out",
           "感謝されることだけを燃料にすると、ガス欠になる"),
    label=("Own Fuel", "自分の燃料"),
    h1_emoji="⛽",
    alt="A chubby matte plastic model kit penguin next to a real small red metal fuel can and a green sprout in a pot",
    section="感謝を習慣に",
    message="感謝されることをやる気の燃料にすると、他の人の気分しだいになる。信じたことをやりきる燃料は、自分の中でまた満ちる。",
    tone="素材の重さ：ふつう（やる気の源）\n→ 見せ方：ポップに（青緑とトマト色。2つの燃料タンクで5日間すごしてみる）",
    game_ja="⛽ 2つのタンクで5日間：カレンダーの曜日を月→金の順に押してスタンプ。日によって「💐 ありがとうと言われた日」と「🍃 だれも何も言わない日」がある。「感謝される」タンクは、言われた日だけ増えて、静かな日にどんどん減り、水曜には空っぽでペンギンがへたりこむ。「信じたことをやる」タンクは、毎日自分でまた満ちる。金曜まで押すと、まとめの一言。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of matte plastic model kit pieces, "
            "standing proudly beside a realistic small red metal fuel can and a little terracotta pot with a fresh green sprout. "
            "Bright simple teal and warm tomato red background with soft depth and gentle daylight. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × プラモデル × 赤い燃料缶と芽",
    mood=["lift", "energy"], tags=["psychology", "mindset", "happiness"],
    pal=dict(bg="#f0fbfa", muted="#5c7a78", acc="#0f9a90", acc2="#ff6247", shadow="rgba(20,120,110,.16)",
             r1="rgba(40,200,190,.26)", r2="rgba(255,98,71,.14)", r3="rgba(255,206,84,.18)",
             h1="#0d3a37", photo="#d8f4f1", big="#0c7d74", bigdark="#8ee8df",
             game="linear-gradient(160deg, #13b3a5 0%, #2d82c9 55%, #ff6247 120%)"),
    cards=[
        dict(emoji="💐", label=("Feels Nice", "うれしい"),
             s=[("It feels nice when someone says \"thank you\" to you, right?",
                 "「ありがとう」と言われると、うれしいですよね。")]),
        dict(emoji="🎢", label=("Up and Down", "上がったり下がったり"),
             s=[("But if you make it the fuel for your energy, you depend on how other people feel.",
                 "でも、それをやる気の燃料にすると、他の人の気分しだいになってしまいます。"),
                ("On days when nobody says anything, your tank is empty.",
                 "誰も何も言わない日は、燃料が空っぽです。")]),
        dict(emoji="🌱", label=("Your Own Fuel", "自分の燃料"), big=True,
             s=[("It is said that even if nobody notices, you can be happy if you do what you believe in all the way.",
                 "誰にも認められなくても、自分が信じたことをやりきれたら、それで幸せになれるそうです。")]),
    ],
    game_after=2,
    game_note="2つのタンクで5日間（感謝される燃料は、静かな日に空っぽになる）",
    game_html="""  <section class="game" data-day="0" data-alow="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">5 days with 2 fuel tanks</div>
    <div class="game-hint">Tap the days in order, Monday to Friday. Some days, nobody says thank you.</div>
    <div class="cal">
      <button type="button" class="day" data-i="1" data-st="0"><span class="dw">Mon</span><span class="dk dk1">💐 Thanked</span></button>
      <button type="button" class="day" data-i="2" data-st="0"><span class="dw">Tue</span><span class="dk dk0">🍃 Quiet</span></button>
      <button type="button" class="day" data-i="3" data-st="0"><span class="dw">Wed</span><span class="dk dk0">🍃 Quiet</span></button>
      <button type="button" class="day" data-i="4" data-st="0"><span class="dw">Thu</span><span class="dk dk1">💐 Thanked</span></button>
      <button type="button" class="day" data-i="5" data-st="0"><span class="dw">Fri</span><span class="dk dk0">🍃 Quiet</span></button>
    </div>
    <div class="tanks">
      <div class="tk tk-a">
        <div class="tk-name">⛽ Fuel: being thanked</div>
        <div class="tk-body" aria-hidden="true"><i></i></div>
        <div class="tk-pg"><span class="pg-e">🐧</span></div>
        <div class="tk-st"><span class="sa-ok">Running!</span><span class="sa-low">🪫 Out of energy…</span></div>
      </div>
      <div class="tk tk-b">
        <div class="tk-name">🌱 Fuel: doing what I believe</div>
        <div class="tk-body" aria-hidden="true"><i></i></div>
        <div class="tk-pg"><span class="pg-e">🐧</span></div>
        <div class="tk-st"><span class="sb-ok">It fills up again by itself.</span></div>
      </div>
    </div>
    <div class="end">🐧 Thanks is a nice bonus. But your own fuel keeps you going every day.</div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Start a new week</button></div>
  </section>""",
    css="""
  /* ⛽ 2つのタンクで5日間 */
  .cal { display: grid; grid-template-columns: repeat(5, 1fr); gap: 6px; max-width: 440px; margin: 14px auto 0; }
  .day { display: grid; justify-items: center; align-content: start; gap: 4px; min-height: 84px; padding: 8px 2px; border: 0; border-radius: 16px;
    background: rgba(255,255,255,.2); color: #fff; font: inherit; cursor: pointer; -webkit-tap-highlight-color: transparent; touch-action: manipulation; }
  .day:focus-visible { outline: 3px solid #fff; outline-offset: 2px; }
  .dw { font-size: 15px; font-weight: 900; }
  .dk { display: none; font-size: 11.5px; font-weight: 900; line-height: 1.25; }
  .day[data-st="1"] { background: #fff; color: #0d3a37; animation: boing .4s ease; cursor: default; }
  .day[data-st="1"] .dk { display: block; }
  .day[data-st="1"] .dk1 { color: #c2410c; }
  .day[data-st="1"] .dk0 { color: #2f7a55; }
  .game[data-day="0"] .day[data-i="1"], .game[data-day="1"] .day[data-i="2"], .game[data-day="2"] .day[data-i="3"],
  .game[data-day="3"] .day[data-i="4"], .game[data-day="4"] .day[data-i="5"] { box-shadow: 0 0 0 3px #ffe066; animation: nudge 1s ease-in-out infinite alternate; }
  @keyframes nudge { from { box-shadow: 0 0 0 3px #ffe066; } to { box-shadow: 0 0 0 6px rgba(255,224,102,.55); } }
  .tanks { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 440px; margin: 14px auto 0; }
  .tk { display: grid; justify-items: center; gap: 6px; padding: 12px 8px; border-radius: 20px; background: rgba(255,255,255,.18); }
  .tk-name { min-height: 2.6em; font-size: 13.5px; font-weight: 900; line-height: 1.3; }
  .tk-body { position: relative; width: 64px; height: 110px; border-radius: 16px; background: rgba(0,0,0,.18); border: 3px solid #fff; overflow: hidden; }
  .tk-body i { position: absolute; left: 0; right: 0; bottom: 0; height: 60%; transition: height .7s cubic-bezier(.2,1.2,.4,1), background .4s ease; }
  .tk-a .tk-body i { background: #ffb347; }
  .tk-b .tk-body i { background: #7ef0a8; height: 90%; }
  .game[data-alow="1"] .tk-a .tk-body i { background: #ff6247; }
  .tk-pg { height: 40px; }
  .game .pg-e { display: inline-block; font-size: 34px; line-height: 1; transition: transform .4s ease; }
  .game[data-alow="1"] .tk-a .pg-e { transform: rotate(80deg) translateX(8px); }
  .game[data-day="1"] .tk-b .pg-e, .game[data-day="2"] .tk-b .pg-e, .game[data-day="3"] .tk-b .pg-e, .game[data-day="4"] .tk-b .pg-e, .game[data-day="5"] .tk-b .pg-e { animation: hop .5s ease-in-out infinite alternate; }
  @keyframes hop { from { transform: translateY(0); } to { transform: translateY(-8px); } }
  .tk-st { min-height: 2.6em; font-size: 13.5px; font-weight: 900; line-height: 1.3; }
  .tk-st > span { display: none; }
  .game:not([data-day="0"])[data-alow="0"] .sa-ok, .game[data-alow="1"] .sa-low, .game:not([data-day="0"]) .sb-ok { display: block; }
  .game[data-alow="1"] .sa-low { animation: shake .45s ease; }
  .end { display: none; max-width: 440px; margin: 12px auto 0; padding: 12px 14px; border-radius: 18px; background: #fff; color: #0c7d74;
    font-size: 16px; font-weight: 900; line-height: 1.45; }
  .game[data-day="5"] .end { display: block; animation: boing .5s ease; }
  .ctrl { margin-top: 12px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
  @media (max-width: 380px) { .dk { font-size: 10.5px; } .cal { gap: 4px; } }
""",
    dark="""  html[data-theme="dark"] .day[data-st="1"] { background: #22302f; color: #e6fffb; }
  html[data-theme="dark"] .day[data-st="1"] .dk1 { color: #ffb38a; }
  html[data-theme="dark"] .day[data-st="1"] .dk0 { color: #9fe8bf; }
  html[data-theme="dark"] .end { background: #22302f; color: #8ee8df; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var days = [].slice.call(g.querySelectorAll('.day')), fa = g.querySelector('.tk-a .tk-body i'), fb = g.querySelector('.tk-b .tk-body i');
  var THANKED = [0, 1, 0, 0, 1, 0], day = 0, a = 60;
  function paint() {
    g.setAttribute('data-day', String(day));
    g.setAttribute('data-alow', a <= 15 ? '1' : '0');
    fa.style.height = a + '%';
    fb.style.height = day ? '96%' : '90%';
  }
  days.forEach(function (b) {
    b.addEventListener('click', function () {
      var i = +b.getAttribute('data-i');
      if (i !== day + 1) return;
      day = i; b.setAttribute('data-st', '1');
      a = THANKED[i] ? Math.min(100, a + 40) : Math.max(5, a - 45);
      paint();
      fb.style.height = '70%'; setTimeout(function () { fb.style.height = '96%'; }, 380);   /* 使って少し減り、すぐ自分でまた満ちる */
      if (window.pengessoPop) {
        var r = b.getBoundingClientRect();
        window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, day === 5 ? ['🌱', '🐧', '✨', '💚'] : (THANKED[i] ? ['💐'] : ['🍃']), day === 5 ? 18 : 6);
      }
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    day = 0; a = 60; days.forEach(function (b) { b.setAttribute('data-st', '0'); }); paint();
  });
  paint();
})();
""",
    ja={
        "5 days with 2 fuel tanks": "2つのタンクで5日間",
        "Tap the days in order, Monday to Friday. Some days, nobody says thank you.": "月曜から金曜まで、順番に押してね。誰も「ありがとう」と言わない日もあります。",
        "Mon": "月", "Tue": "火", "Wed": "水", "Thu": "木", "Fri": "金",
        "💐 Thanked": "💐 感謝された",
        "🍃 Quiet": "🍃 静かな日",
        "⛽ Fuel: being thanked": "⛽ 燃料：感謝されること",
        "🌱 Fuel: doing what I believe": "🌱 燃料：信じたことをやる",
        "Running!": "走ってる！",
        "🪫 Out of energy…": "🪫 ガス欠…",
        "It fills up again by itself.": "自分で、また満ちてくる。",
        "🐧 Thanks is a nice bonus. But your own fuel keeps you going every day.": "🐧 感謝されるのは、うれしいおまけ。でも毎日動かしてくれるのは、自分の燃料です。",
        "↺ Start a new week": "↺ 新しい1週間",
    },
)
build(d)
