from gen import build

d = dict(
    slug="independence-is-like-a-diet", seq=515,
    title=("Standing on your own feet is like a diet: it slips back easily",
           "自立はダイエットと同じ。気をゆるめると、すぐ戻る"),
    label=("Small Steps", "小さな一歩"),
    h1_emoji="⚖️",
    alt="A chubby crocheted amigurumi penguin stepping onto a real bathroom scale with a small proud smile",
    section="幸せは「自立」から",
    message="自立はダイエットと同じ。意識しないとすぐ戻るので、小さく毎日続ける。",
    tone="素材の重さ：真面目（自立には時間がかかる）\n→ 見せ方：ポップに（ミントとピンク。7日間のスタンプカード）",
    game_ja="📅 7日間チャレンジ：「寄りかかり度」のメーターが、ほうっておくと上がっていく。1日ごとに、小さな行動（本当の気持ちを1つ言う／行ったことのないカフェに1人で入る／お昼を自分で決める）を押すと⭐スタンプが押されてメーターが下がる（でも夜のあいだに少し戻る）。「今日はお休み」だと☁️スタンプでメーターが上がる。7日目のあとに結果。戻っても「それがふつう」とやさしく言う。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of crocheted amigurumi yarn, "
            "carefully stepping onto a realistic white bathroom scale with one foot, looking determined and a little shy. "
            "Bright simple mint green and soft pink background with soft depth, a clean light floor. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × かぎ針編みのあみぐるみ × 体重計",
    mood=["lift", "energy"], tags=["psychology", "mindset", "tips"],
    pal=dict(bg="#f2fffa", muted="#5f857a", acc="#e83f7f", acc2="#19bf9b", shadow="rgba(30,120,100,.16)",
             r1="rgba(255,140,180,.26)", r2="rgba(25,191,155,.20)", r3="rgba(255,214,90,.18)",
             h1="#173d35", photo="#dcf8ef", big="#d02f6c", bigdark="#ffadc9",
             game="linear-gradient(155deg, #19c3a0 0%, #3aa0ff 55%, #ff5c9a 100%)"),
    cards=[
        dict(emoji="⏳", label=("Takes Time", "時間がかかる"),
             s=[("It takes time to stand on your own feet.",
                 "自分の足で立つ「自立」には、時間がかかります。")]),
        dict(emoji="⚖️", label=("Like A Diet", "ダイエットと同じ"),
             s=[("Like a diet, if you relax, it soon goes back.",
                 "ダイエットと同じで、気をゆるめるとすぐ元に戻ってしまいます。")]),
        dict(emoji="🌱", label=("Start Small", "小さく始める"),
             s=[("So it is OK to start with small things.",
                 "だから、小さなことから始めて大丈夫です。")]),
        dict(emoji="☕", label=("For Example", "たとえば"),
             s=[("For example, say just 1 true feeling, or go alone into a cafe you have never been to.",
                 "たとえば、本当の気持ちを1つだけ言ってみる、行ったことのないカフェに1人で入ってみる、などです。")]),
        dict(emoji="📅", label=("Every Day", "毎日"), big=True,
             s=[("A little every day works best.",
                 "毎日ちょっとずつが、いちばん効きます。")]),
    ],
    game_after=3,
    game_note="7日間チャレンジ（寄りかかり度メーターとスタンプ）",
    game_html="""  <section class="game" data-day="1" data-r="" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">The 7-day challenge</div>
    <div class="game-hint">Each day, pick 1 small step. Watch the meter.</div>
    <div class="cal">
      <div class="stamp" data-i="1"><span class="st-n">1</span><span class="st-e"></span></div>
      <div class="stamp" data-i="2"><span class="st-n">2</span><span class="st-e"></span></div>
      <div class="stamp" data-i="3"><span class="st-n">3</span><span class="st-e"></span></div>
      <div class="stamp" data-i="4"><span class="st-n">4</span><span class="st-e"></span></div>
      <div class="stamp" data-i="5"><span class="st-n">5</span><span class="st-e"></span></div>
      <div class="stamp" data-i="6"><span class="st-n">6</span><span class="st-e"></span></div>
      <div class="stamp" data-i="7"><span class="st-n">7</span><span class="st-e"></span></div>
    </div>
    <div class="lean">
      <div class="lean-head"><span class="lean-l">🛋️ Leaning level</span> <span class="lv">60</span></div>
      <div class="lean-bar" aria-hidden="true"><i></i></div>
      <div class="lean-scale" aria-hidden="true"><span class="ls-a">🐾 On my own feet</span><span class="ls-b">🛋️ Leaning</span></div>
    </div>
    <div class="today"><span class="dl">📅 Today: day</span> <span class="dn">1</span> <span class="dof">/ 7</span></div>
    <div class="acts">
      <button type="button" class="btn act" data-v="-13">💬 Say 1 true feeling</button>
      <button type="button" class="btn act" data-v="-13">☕ Try a new cafe alone</button>
      <button type="button" class="btn act" data-v="-13">🍙 Choose my lunch myself</button>
      <button type="button" class="btn act skip" data-v="15">😴 Skip today</button>
    </div>
    <div class="night">🌙 At night, the meter goes back a little.</div>
    <div class="res">
      <div class="r-good">🎉 7 days of small steps! You are standing well.</div>
      <div class="r-back">🙂 It went back a little. That is normal. Start small again tomorrow.</div>
    </div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Start over</button></div>
  </section>""",
    css="""
  /* 📅 7日間チャレンジ */
  .cal { display: grid; grid-template-columns: repeat(7, 1fr); gap: 6px; max-width: 420px; margin: 16px auto 0; }
  .stamp { position: relative; aspect-ratio: 1; border-radius: 14px; background: rgba(255,255,255,.22); box-shadow: inset 0 0 0 2px rgba(255,255,255,.55); }
  .st-n { position: absolute; left: 6px; top: 3px; font-size: 11px; font-weight: 900; opacity: .9; }
  .st-e { position: absolute; inset: 0; display: grid; place-items: center; font-size: clamp(18px, 5vw, 26px); }
  .stamp.on { background: #fff; color: #2f2a3a; animation: boing .45s ease; }
  .stamp.cur { box-shadow: inset 0 0 0 3px #ffe066; }
  .lean { max-width: 420px; margin: 14px auto 0; padding: 12px 14px; border-radius: 20px; background: rgba(255,255,255,.18); }
  .lean-head { display: flex; justify-content: space-between; align-items: center; font-size: 15px; font-weight: 900; }
  .lv { display: inline-block; min-width: 2.2em; padding: 1px 8px; border-radius: 999px; background: rgba(255,255,255,.3); }
  .lean-bar { position: relative; height: 18px; margin-top: 8px; border-radius: 999px; background: rgba(255,255,255,.3); overflow: hidden; }
  .lean-bar i { position: absolute; inset: 0 auto 0 0; width: 60%; border-radius: 999px; background: #ffe066; transition: width .45s cubic-bezier(.2,1.3,.4,1); }
  .lean-scale { display: flex; justify-content: space-between; gap: 8px; margin-top: 4px; font-size: 11.5px; font-weight: 900; opacity: .9; }
  .today { margin-top: 14px; font-size: 20px; font-weight: 900; }
  .acts { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 420px; margin: 10px auto 0; }
  .act { min-height: 60px; border-radius: 18px; font-size: 14.5px; padding: 8px 10px; }
  .act.skip { background: rgba(255,255,255,.2); color: #fff; box-shadow: inset 0 0 0 2px rgba(255,255,255,.7); }
  .night { margin-top: 10px; font-size: 13.5px; font-weight: 800; opacity: .9; }
  .night.go { animation: shake .45s ease; }
  .res > div { display: none; margin: 14px auto 0; max-width: 420px; padding: 12px 14px; border-radius: 18px; background: #fff; color: #7a1f4a; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .game[data-r="good"] .r-good, .game[data-r="back"] .r-back { display: block; animation: boing .5s ease; }
  .game[data-day="8"] .acts, .game[data-day="8"] .today, .game[data-day="8"] .night { display: none; }
  .ctrl { margin-top: 12px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
""",
    dark="""  html[data-theme="dark"] .stamp.on { background: #2b2d3a; color: #f4f0fa; }
  html[data-theme="dark"] .res > div { background: #2b2d3a; color: #ffc2d8; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var day = 1, lv = 60, busy = false, t1 = 0, t2 = 0;
  var bar = g.querySelector('.lean-bar i'), lvEl = g.querySelector('.lv'), night = g.querySelector('.night');
  var stamps = g.querySelectorAll('.stamp');
  function paint() {
    lvEl.textContent = lv; bar.style.width = Math.max(3, lv) + '%';
    g.querySelector('.dn').textContent = Math.min(day, 7);
    [].forEach.call(stamps, function (s, i) { s.classList.toggle('cur', i + 1 === day); });
  }
  paint();
  [].forEach.call(g.querySelectorAll('.act'), function (b) {
    b.addEventListener('click', function () {
      if (busy || day > 7) return; busy = true;
      var v = parseInt(b.getAttribute('data-v'), 10), skip = b.classList.contains('skip');
      var s = stamps[day - 1];
      s.querySelector('.st-e').textContent = skip ? '☁️' : '⭐';
      s.classList.add('on');
      lv = Math.max(0, Math.min(100, lv + v)); paint();
      if (!skip && window.pengessoPop) { var r = s.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['⭐', '🐧', '✨'], 8); }
      /* 夜のあいだに、少し戻る（ダイエットと同じ） */
      clearTimeout(t1);
      t1 = setTimeout(function () {
        lv = Math.min(100, lv + 4);
        night.classList.remove('go'); void night.offsetWidth; night.classList.add('go');
        day++; paint(); busy = false;
        if (day > 7) {
          g.setAttribute('data-day', '8');
          g.setAttribute('data-r', lv <= 30 ? 'good' : 'back');
          if (lv <= 30 && window.pengessoPop) { var q = g.querySelector('.res').getBoundingClientRect(); window.pengessoPop(q.left + q.width / 2, q.top, ['🎉', '🐧', '⭐', '✨'], 18); }
        }
      }, 650);
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    clearTimeout(t1); busy = false; day = 1; lv = 60;
    [].forEach.call(stamps, function (s) { s.classList.remove('on'); s.querySelector('.st-e').textContent = ''; });
    g.setAttribute('data-day', '1'); g.setAttribute('data-r', ''); paint();
  });
})();
""",
    ja={
        "The 7-day challenge": "7日間チャレンジ",
        "Each day, pick 1 small step. Watch the meter.": "1日に1つ、小さな一歩を選んでね。メーターを見ていて。",
        "🛋️ Leaning level": "🛋️ 寄りかかり度",
        "🐾 On my own feet": "🐾 自分の足で立つ",
        "🛋️ Leaning": "🛋️ 寄りかかり",
        "📅 Today: day": "📅 今日：",
        "/ 7": "日目 / 7",
        "💬 Say 1 true feeling": "💬 本当の気持ちを1つ言う",
        "☕ Try a new cafe alone": "☕ 初めてのカフェに1人で入る",
        "🍙 Choose my lunch myself": "🍙 お昼を自分で決める",
        "😴 Skip today": "😴 今日はお休み",
        "🌙 At night, the meter goes back a little.": "🌙 夜のあいだに、メーターが少し戻ります。",
        "🎉 7 days of small steps! You are standing well.": "🎉 7日間の小さな一歩！ちゃんと立てています。",
        "🙂 It went back a little. That is normal. Start small again tomorrow.": "🙂 ちょっと戻りました。それがふつうです。明日また小さく始めよう。",
        "↺ Start over": "↺ 最初から",
    },
)
build(d)
