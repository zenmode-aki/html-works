from gen import build

d = dict(
    slug="dailyish", seq=586, url="https://www.oliverburkeman.com/dailyish",
    title=("Doing it dailyish lasts longer than doing it every day",
           "「毎日」より「だいたい毎日」のほうが続く"),
    label=("Dailyish", "だいたい毎日"),
    h1_emoji="🌤️",
    alt="A chubby crocheted amigurumi penguin pointing at a real paper desk calendar with hand-drawn check marks and one empty day",
    section="⑰「習慣は『だいたい毎日』」",
    message="「毎日絶対」は1回サボると終わる。「だいたい毎日」のほうが結局たくさんできる。",
    tone="素材の重さ：ふつう（習慣の考え方）\n→ 見せ方：ポップに（ひまわりの黄色と空色。2つのカレンダーを4週間走らせて比べる）",
    game_ja="📅 4週間レース：「毎日絶対」と「だいたい毎日」の2つのカレンダーが、同時に1日ずつ進む。疲れた日（3回）は勝手にやってくるし、「😴 今日は休む」で自分でも休める。「毎日絶対」は1回休んだ瞬間に ✕ がついて「🙄 もういいや…」で止まる。「だいたい毎日」は休んでも次の日に ✓ が続く。最後に ✓ の数を比べる。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made as crocheted amigurumi yarn with visible "
            "stitches, pointing happily with one flipper at a realistic paper desk calendar standing on a table, the calendar covered with "
            "hand-drawn green check marks and one empty day. Bright simple sunny yellow and sky blue background with soft depth. Realistic 3D "
            "render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering."),
    combo="ペンギン × あみぐるみ × 卓上カレンダー",
    mood=["lift"], tags=["books", "productivity", "tips"],
    pal=dict(bg="#fffbec", muted="#86775a", acc="#e07b00", acc2="#3a9be0", shadow="rgba(150,100,10,.16)",
             r1="rgba(255,183,3,.28)", r2="rgba(77,171,247,.20)", r3="rgba(124,214,140,.18)",
             h1="#3a2a05", photo="#fff1c9", big="#c86a00", bigdark="#ffc773",
             game="linear-gradient(155deg, #ffb703 0%, #fb8500 48%, #3a9be0 100%)"),
    cards=[
        dict(emoji="⛓️", label=("The Strict Rule", "きびしいルール"),
             s=[("If you decide \"every single day,\" you often give up on everything the moment you skip once.",
                 "「毎日絶対やる」と決めると、1回サボった瞬間に、全部どうでもよくなりがちです。")]),
        dict(emoji="🌤️", label=("Almost Daily", "だいたい毎日"),
             s=[("Burkeman suggests \"dailyish\": almost every day.", "バークマンさんのおすすめは「だいたい毎日（dailyish）」です。")]),
        dict(emoji="💪", label=("Not Lazy", "甘えじゃない"),
             s=[("This is not being lazy.", "これは甘えではありません。"),
                ("Once or twice a week does not build speed, so you still push yourself.", "週に1、2回では勢いがつかないので、ちゃんと自分にプレッシャーはかけます。"),
                ("But you do not force it.", "ただ、強制はしません。")]),
        dict(emoji="📈", label=("More In Total", "合計で多い"), big=True,
             s=[("In the end, dailyish gets more done.", "結局、だいたい毎日のほうが、たくさんできます。")]),
    ],
    game_after=2,
    game_note="4週間レース（毎日絶対 vs だいたい毎日）",
    game_html="""  <section class="game" data-s="idle" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">The 4-week race</div>
    <div class="game-hint">Watch 4 weeks. Some days you will be tired. You can also tap "Skip today."</div>
    <div class="cals">
      <div class="cal cal-a">
        <div class="cal-h">📏 Every day, no matter what</div>
        <div class="grid g-a"></div>
        <div class="giveup">🙄 Forget it…</div>
        <div class="tot"><span class="tl">✓ Done:</span> <b class="na">0</b></div>
      </div>
      <div class="cal cal-b">
        <div class="cal-h">🌤️ Dailyish</div>
        <div class="grid g-b"></div>
        <div class="tot"><span class="tl">✓ Done:</span> <b class="nb">0</b></div>
      </div>
    </div>
    <div class="msg">
      <div class="m m-idle">Same person, same tired days. Only the rule is different.</div>
      <div class="m m-run"><span class="dl">📅 Days passed:</span> <b class="dn">1</b><span class="of">/28</span></div>
      <div class="m m-end">🌤️ Dailyish just keeps going after a skip. More ✓ in total! 🎉</div>
    </div>
    <div class="btns">
      <button class="btn b-play" type="button">▶ Play 4 weeks</button>
      <button class="btn b-skip" type="button">😴 Skip today</button>
      <button class="btn ghost b-again" type="button">↺ Try again</button>
    </div>
  </section>""",
    css=r"""
  /* 📅 4週間レース */
  .cals { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 440px; margin: 16px auto 0; }
  .cal { position: relative; padding: 10px 8px 10px; border-radius: 20px; background: #fff; color: #3a2a05; }
  .cal-h { min-height: 38px; display: flex; align-items: center; justify-content: center; font-size: 13.5px; font-weight: 900; line-height: 1.25; }
  .grid { display: grid; grid-template-columns: repeat(7, 1fr); gap: 3px; margin-top: 6px; }
  .grid i { position: relative; aspect-ratio: 1; border-radius: 6px; background: #f1ece0; font-style: normal; }
  .grid i::after { position: absolute; inset: 0; display: grid; place-items: center; font-size: 13px; font-weight: 900; line-height: 1; }
  .grid i.ok { background: #57c27a; } .grid i.ok::after { content: "✓"; color: #fff; }
  .grid i.skip { background: #ffd6a5; } .grid i.skip::after { content: "·"; color: #a05a00; font-size: 20px; }
  .grid i.x { background: #ff6b6b; } .grid i.x::after { content: "✕"; color: #fff; }
  .grid i.dead { background: #ddd8cf; opacity: .5; }
  .grid i.today { box-shadow: 0 0 0 2px #fb8500; animation: boing .3s ease; }
  .giveup { position: absolute; left: 6px; right: 6px; top: 46%; padding: 8px 6px; border-radius: 14px; background: #3a3540; color: #fff; font-size: 15px; font-weight: 900;
    opacity: 0; transform: scale(.7) rotate(-6deg); transition: opacity .3s ease, transform .35s cubic-bezier(.2,1.5,.4,1); pointer-events: none; }
  .cal-a.broken .giveup { opacity: 1; transform: rotate(-6deg); }
  .tot { margin-top: 8px; font-size: 15px; font-weight: 900; }
  .tot b { font-size: 22px; }
  .game[data-s="end"] .cal-b { box-shadow: 0 0 0 4px #ffe066; }
  .msg { margin-top: 14px; min-height: 48px; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .msg .m { display: none; }
  .game[data-s="idle"] .m-idle, .game[data-s="run"] .m-run, .game[data-s="end"] .m-end { display: block; }
  .btns { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-top: 12px; }
  .game .b-skip, .game .b-again { display: none; }
  .game:not([data-s="idle"]) .b-play { display: none; }
  .game[data-s="run"] .b-skip { display: inline-flex; min-width: 210px; background: #ffe066; color: #4a3500; }
  .game[data-s="end"] .b-again { display: inline-flex; }
  @media (max-width: 380px) { .cal { padding: 8px 5px; } .grid { gap: 2px; } }
""",
    dark="""  html[data-theme="dark"] .cal { background: #2b2d3a; color: #f4f0fa; }
  html[data-theme="dark"] .grid i { background: #3a3c4a; }
  html[data-theme="dark"] .grid i.ok { background: #3fae66; }
  html[data-theme="dark"] .grid i.skip { background: #8a5a20; }
  html[data-theme="dark"] .grid i.x { background: #e05555; }
  html[data-theme="dark"] .game .b-skip { background: #ffe066; color: #4a3500; }""",
    js=r"""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var ga = g.querySelector('.g-a'), gb = g.querySelector('.g-b'), calA = g.querySelector('.cal-a');
  var na = g.querySelector('.na'), nb = g.querySelector('.nb'), dn = g.querySelector('.dn');
  var A = [], B = [], i, day = 0, a = 0, b = 0, broken = false, skipNext = false, tm = 0;
  var TIRED = [5, 14, 21];
  for (i = 0; i < 28; i++) { A.push(ga.appendChild(document.createElement('i'))); B.push(gb.appendChild(document.createElement('i'))); }
  function clear() {
    A.concat(B).forEach(function (c) { c.className = ''; });
    day = 0; a = 0; b = 0; broken = false; skipNext = false;
    na.textContent = '0'; nb.textContent = '0'; dn.textContent = '1'; calA.classList.remove('broken');
  }
  function step() {
    if (day > 0) { A[day - 1].classList.remove('today'); B[day - 1].classList.remove('today'); }
    if (day >= 28) { end(); return; }
    var skip = skipNext || TIRED.indexOf(day) >= 0; skipNext = false;
    dn.textContent = day + 1;
    B[day].classList.add(skip ? 'skip' : 'ok', 'today');
    if (!skip) { b++; nb.textContent = b; }
    if (broken) A[day].classList.add('dead');
    else if (skip) {
      A[day].classList.add('x', 'today'); broken = true; calA.classList.add('broken');
      for (var k = day + 1; k < 28; k++) A[k].classList.add('dead');
    } else { A[day].classList.add('ok', 'today'); a++; na.textContent = a; }
    day++;
    tm = setTimeout(step, 260);
  }
  function end() {
    g.setAttribute('data-s', 'end');
    var r = gb.getBoundingClientRect();
    if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['✅', '🌤️', '🐧', '✨'], 18);
  }
  g.querySelector('.b-play').addEventListener('click', function () { clear(); g.setAttribute('data-s', 'run'); step(); });
  g.querySelector('.b-skip').addEventListener('click', function () { skipNext = true; });
  g.querySelector('.b-again').addEventListener('click', function () { clearTimeout(tm); clear(); g.setAttribute('data-s', 'idle'); });
})();
""",
    ja={
        "The 4-week race": "4週間レース",
        "Watch 4 weeks. Some days you will be tired. You can also tap \"Skip today.\"": "4週間を見てみよう。疲れた日もあります。「今日は休む」を押して休んでもOK。",
        "📏 Every day, no matter what": "📏 毎日、絶対やる",
        "🌤️ Dailyish": "🌤️ だいたい毎日",
        "🙄 Forget it…": "🙄 もういいや…",
        "✓ Done:": "✓ できた日：",
        "Same person, same tired days. Only the rule is different.": "同じ人、同じ疲れた日。ちがうのはルールだけ。",
        "📅 Days passed:": "📅 たった日数：",
        "🌤️ Dailyish just keeps going after a skip. More ✓ in total! 🎉": "🌤️ だいたい毎日は、休んでもそのまま続く。✓ の合計も多い！🎉",
        "▶ Play 4 weeks": "▶ 4週間スタート",
        "😴 Skip today": "😴 今日は休む",
        "↺ Try again": "↺ もう一回",
    },
)

if __name__ == "__main__":
    build(d)
