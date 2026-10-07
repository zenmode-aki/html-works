from gen import build

SEGS = [("memo", "📝", 1), ("think", "🤔", 3), ("worry", "😟", 4), ("night", "🌙", 5),
        ("again", "🔔", 1), ("think", "🤔", 3), ("worry", "😟", 4), ("night", "🌙", 5), ("again", "🔔", 1)]
SEG_HTML = "".join(f'<i class="sg sg-{k}" data-m="{m}" aria-hidden="true">{e}</i>' for k, e, m in SEGS)

d = dict(
    slug="do-it-in-two-minutes", seq=568, path="justdo",
    title=("If it takes 2 minutes, do it now, because later costs more",
           "2分で終わることは今やる。後回しのほうが時間がかかる"),
    label=("2-Minute Rule", "2分ルール"),
    h1_emoji="⏱️",
    alt="A chubby boucle wool penguin happily pressing a realistic red kitchen timer on a bright simple table",
    section="⑨「考える前に、やっちゃう」",
    message="2分で終わることは今やる。後回しにすると、考える・気にする・午前3時に思い出す時間のほうが長くなる。",
    tone="素材の重さ：ふつう（生活のコツ）\n→ 見せ方：ポップに（赤と黄色。「あとで」のコストが積み上がる棒グラフで遊べる）",
    game_ja="⏱️ 「あとで」の本当のコスト：お題は「🛒 掃除機の紙パックを注文する（2分）」。「⏰ あとで」を押すたびに、横の棒グラフに📝リマインダー＋1分・🤔考える＋3分・😟気にする＋4分・🌙午前3時に思い出す＋5分・🔔同じリマインダーをまた作る＋1分…が積み上がり、合計の分数とペンギンの顔がどんどん重くなる。「⚡ 今やる」を押すと、棒は緑の2分だけに縮んで、風船🎈がふわっと飛んでいく。「『あとで』はもう◯分かかっていた！」と比べられる。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of cozy boucle wool, "
            "cheerfully tapping a realistic red kitchen timer on a small wooden table. "
            "Bright simple warm yellow and coral background with soft depth. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × ブークレウール × キッチンタイマー",
    mood=["lift", "laugh"], tags=["books", "productivity", "tips"],
    pal=dict(bg="#fff7f2", muted="#86695e", acc="#e0483e", acc2="#ffb703", shadow="rgba(160,70,50,.16)",
             r1="rgba(255,183,3,.28)", r2="rgba(224,72,62,.16)", r3="rgba(60,200,140,.14)",
             h1="#47170f", photo="#ffe6dc", big="#c93b31", bigdark="#ffaba4",
             game="linear-gradient(150deg, #ff6b5a 0%, #e0483e 50%, #ff9f1c 100%)"),
    cards=[
        dict(emoji="⏱️", label=("Two Minutes", "2分"),
             s=[("If it takes 2 minutes, do it now.", "2分で終わることは、今やりましょう。")]),
        dict(emoji="📝", label=("Heavy Memo", "メモが重い"),
             s=[("Writing it in a memo can be more work than just doing it.",
                 "メモに書く手間のほうが、やるより重いことがあります。")]),
        dict(emoji="🌙", label=("Real Cost", "本当の時間"),
             s=[("The real time is 2 minutes, plus time to think, time to worry, and time to remember it at 3 a.m.",
                 "本当にかかる時間は、やる2分＋考える時間＋気にする時間＋午前3時に思い出す時間です。")]),
        dict(emoji="😂", label=("His Joke", "紙パック事件"),
             s=[("Oliver Burkeman made a reminder to \"order vacuum cleaner bags\" 3 separate times.",
                 "オリバー・バークマンさんは、「掃除機の紙パックを注文する」というリマインダーを、3回も別々に作っていたそうです。"),
                ("Ordering them was faster.", "注文したほうが早かったのに。")]),
        dict(emoji="⚡", label=("Now Is Easy", "今がラク"), big=True,
             s=[("Doing it now is the easiest.", "今やるのが、いちばんラクです。")]),
    ],
    game_after=3,
    game_note="「あとで」の本当のコスト（積み上がる棒グラフ）",
    game_html="""  <section class="game" data-s="idle" data-m="hint" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">The real cost of "later"</div>
    <div class="task">
      <span class="tk-mood" aria-hidden="true"><span class="mood">😊</span></span>
      <span class="tk-t">🛒 Order vacuum bags</span>
      <span class="tk-m">⏱️ 2 min</span>
      <span class="bl" aria-hidden="true">🎈</span>
    </div>
    <div class="tbar"><i class="sg sg-do" aria-hidden="true">✅</i>""" + SEG_HTML + """</div>
    <div class="scale" aria-hidden="true"><span>0</span><span>15</span><span>30</span></div>
    <div class="legend">
      <div class="lg lg-memo">📝 Write a reminder · +1 min</div>
      <div class="lg lg-think">🤔 Think about it · +3 min</div>
      <div class="lg lg-worry">😟 Worry about it · +4 min</div>
      <div class="lg lg-night">🌙 Remember it at 3 a.m. · +5 min</div>
      <div class="lg lg-again">🔔 Make the same reminder again · +1 min</div>
    </div>
    <div class="total"><span class="to-l">⏱️ Real cost:</span> <span class="tot">2</span> <span class="to-u">min</span></div>
    <div class="msgs">
      <div class="m-hint">It is a 2-minute task. Now, or later?</div>
      <div class="m-later">Okay, later… 📝</div>
      <div class="m-heavy">A 2-minute task is getting so heavy! 😵</div>
      <div class="m-quick">✅ Done in 2 minutes! Nothing left to carry. 🎈</div>
      <div class="m-done"><span class="d1">✅ Done in 2 minutes. "Later" had already cost</span> <span class="lt">0</span> <span class="lt-u">min! 🎈</span></div>
    </div>
    <div class="ctrl">
      <button type="button" class="btn b-later">⏰ Later</button>
      <button type="button" class="btn b-do">⚡ Do it now</button>
    </div>
    <div class="ctrl2"><button type="button" class="btn ghost b-reset">↺ Try again</button></div>
  </section>""",
    css="""
  /* ⏱️ 「あとで」の本当のコスト */
  .task { position: relative; display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 8px; max-width: 420px; margin: 14px auto 0;
    padding: 12px 14px; border-radius: 20px; background: #fff; color: #47170f; font-size: 17px; font-weight: 900; line-height: 1.3; }
  .tk-mood { font-size: 34px; line-height: 1; }
  .mood { display: inline-block; }
  .mood.bump { animation: boing .4s ease; }
  .tk-m { padding: 3px 10px; border-radius: 999px; background: #e6f8ee; color: #17663c; font-size: 14px; }
  .bl { position: absolute; right: 10px; top: 4px; font-size: 30px; line-height: 1; opacity: 0; }
  .game[data-s="done"] .bl { animation: balloon 2.2s ease-out forwards; }
  @keyframes balloon { 0% { opacity: 1; transform: translateY(0); } 100% { opacity: 0; transform: translateY(-120px) rotate(10deg); } }
  .tbar { display: flex; max-width: 420px; height: 46px; margin: 14px auto 0; padding: 4px; border-radius: 14px; background: rgba(255,255,255,.25); overflow: hidden; }
  .game .tbar .sg { display: grid; place-items: center; flex: 0 0 auto; width: 0; height: 100%; overflow: hidden; font-style: normal; font-size: 18px; line-height: 1;
    border-radius: 9px; transition: width .45s cubic-bezier(.3,1.3,.5,1); }
  .sg.on { box-shadow: inset 0 0 0 2px rgba(255,255,255,.5); }
  .sg-do { width: 6.67%; background: #2fd38a; }
  .sg-memo, .sg-again { background: #ffe066; }
  .sg-think { background: #b8a6ff; }
  .sg-worry { background: #ff9fb0; }
  .sg-night { background: #3b3f8f; }
  .scale { display: flex; justify-content: space-between; max-width: 420px; margin: 4px auto 0; font-size: 11.5px; font-weight: 900; opacity: .85; }
  .legend { max-width: 420px; margin: 10px auto 0; text-align: left; }
  .lg { display: none; padding: 3px 4px; font-size: 14.5px; font-weight: 900; line-height: 1.35; }
  .lg.on { display: block; animation: slide-in .35s ease-out; }
  .game[data-s="done"] .legend { opacity: .35; text-decoration: line-through; }
  .total { margin-top: 10px; font-size: 18px; font-weight: 900; }
  .tot { display: inline-block; min-width: 2em; padding: 2px 10px; border-radius: 999px; background: #fff; color: #c93b31; font-size: 24px; }
  .msgs { min-height: 54px; margin-top: 10px; }
  .msgs > div { display: none; font-size: 16px; font-weight: 900; line-height: 1.45; padding: 4px; }
  .game[data-m="hint"] .m-hint, .game[data-m="later"] .m-later, .game[data-m="heavy"] .m-heavy, .game[data-m="quick"] .m-quick, .game[data-m="done"] .m-done { display: block; animation: boing .45s ease; }
  .lt { display: inline-block; padding: 0 8px; border-radius: 999px; background: rgba(255,255,255,.28); }
  .ctrl { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-top: 4px; }
  .ctrl .btn { flex: 1 1 140px; max-width: 210px; min-height: 58px; }
  .b-later { background: rgba(255,255,255,.2); color: #fff; box-shadow: inset 0 0 0 2px rgba(255,255,255,.7); }
  .b-do { background: #fff; color: #17663c; }
  .game[data-s="done"] .ctrl { display: none; }
  .ctrl2 { margin-top: 10px; min-height: 48px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
  .game[data-s="idle"] .b-reset { visibility: hidden; }
""",
    dark="""  html[data-theme="dark"] .task { background: #22242f; color: #ffe6dc; }
  html[data-theme="dark"] .tk-m { background: #1d4a33; color: #b8f3d0; }
  html[data-theme="dark"] .tot { background: #22242f; color: #ffaba4; }
  html[data-theme="dark"] .game .b-do { background: #1d4a33; color: #b8f3d0; }
  html[data-theme="dark"] .game .b-later { background: rgba(255,255,255,.1); color: #fff; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var segs = [].slice.call(g.querySelectorAll('.sg:not(.sg-do)')), mood = g.querySelector('.mood');
  var tot = g.querySelector('.tot'), FACES = ['😊', '😐', '😕', '😩', '😵'], n = 0, later = 0;
  function pct(m) { return (m / 30 * 100) + '%'; }
  function face(k) { mood.textContent = FACES[Math.min(k, FACES.length - 1)]; mood.classList.remove('bump'); void mood.offsetWidth; mood.classList.add('bump'); }
  function msg(m) { g.setAttribute('data-m', ''); void g.offsetWidth; g.setAttribute('data-m', m); }
  function reset() {
    n = 0; later = 0;
    segs.forEach(function (s) { s.style.width = '0'; s.classList.remove('on'); });
    [].forEach.call(g.querySelectorAll('.lg'), function (l) { l.classList.remove('on'); });
    tot.textContent = '2'; mood.textContent = FACES[0];
    g.setAttribute('data-s', 'idle'); msg('hint');
  }
  g.querySelector('.b-later').addEventListener('click', function () {
    if (g.getAttribute('data-s') === 'done') return;
    g.setAttribute('data-s', 'later');
    if (n < segs.length) {
      var s = segs[n], m = +s.getAttribute('data-m');
      s.style.width = pct(m); s.classList.add('on'); later += m; n++;
      var key = s.className.match(/sg-(\\w+)/)[1];
      var lg = g.querySelector('.lg-' + key); if (lg) lg.classList.add('on');
    }
    tot.textContent = 2 + later;
    face(Math.ceil(n / 2));
    msg(n >= 4 ? 'heavy' : 'later');
    if (navigator.vibrate) { try { navigator.vibrate(15); } catch (e) {} }
  });
  g.querySelector('.b-do').addEventListener('click', function () {
    var had = later;
    segs.forEach(function (s) { s.style.width = '0'; });
    tot.textContent = '2'; mood.textContent = '😄';
    g.querySelector('.lt').textContent = had;
    g.setAttribute('data-s', 'done'); msg(had ? 'done' : 'quick');
    if (window.pengessoPop) { var r = g.querySelector('.task').getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🎈', '✅', '🐧', '✨'], 16); }
  });
  g.querySelector('.b-reset').addEventListener('click', reset);
  reset();
})();
""",
    ja={
        "The real cost of \"later\"": "「あとで」の本当のコスト",
        "🛒 Order vacuum bags": "🛒 掃除機の紙パックを注文する",
        "⏱️ 2 min": "⏱️ 2分",
        "📝 Write a reminder · +1 min": "📝 リマインダーを書く · ＋1分",
        "🤔 Think about it · +3 min": "🤔 そのことを考える · ＋3分",
        "😟 Worry about it · +4 min": "😟 そのことを気にする · ＋4分",
        "🌙 Remember it at 3 a.m. · +5 min": "🌙 午前3時に思い出す · ＋5分",
        "🔔 Make the same reminder again · +1 min": "🔔 同じリマインダーをまた作る · ＋1分",
        "⏱️ Real cost:": "⏱️ 本当にかかった時間：",
        "min": "分",
        "It is a 2-minute task. Now, or later?": "2分で終わること。今やる？あとでやる？",
        "Okay, later… 📝": "じゃあ、あとで… 📝",
        "A 2-minute task is getting so heavy! 😵": "2分のことが、どんどん重くなってる！ 😵",
        "✅ Done in 2 minutes! Nothing left to carry. 🎈": "✅ 2分で終わった！もう何も背負ってない 🎈",
        "✅ Done in 2 minutes. \"Later\" had already cost": "✅ 2分で終わった。「あとで」は、もう",
        "min! 🎈": "分もかかっていた！ 🎈",
        "⏰ Later": "⏰ あとで",
        "⚡ Do it now": "⚡ 今やる",
        "↺ Try again": "↺ もう一回",
    },
)

if __name__ == "__main__":
    build(d)
