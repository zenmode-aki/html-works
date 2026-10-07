from gen import build

DAYS = [("📝", "A big test", "大事なテスト"), ("🧳", "Lost in a new city", "知らない街で迷子"),
        ("🤒", "Sick on a trip", "旅先で体調をくずした"), ("💥", "A big mistake", "大きな失敗"),
        ("🌧️", "A really bad week", "本当にひどい1週間")]
TILES = "\n".join(
    f'        <button type="button" class="hd"><span class="tf"><span class="tf-e" aria-hidden="true">{e}</span><span class="tf-t">{en}</span></span><span class="tb">✓ Made it</span></button>'
    for e, en, _ in DAYS)

d = dict(
    slug="you-made-it-through-before", seq=570, path="anythingcouldhappen",
    title=("You cannot control the future, but you have made it through before",
           "未来はコントロールできない。でも今まで、何とかなってきた"),
    label=("Track Record", "これまでの実績"),
    h1_emoji="🛟",
    alt="A chubby alpaca wool penguin sitting calmly next to a realistic orange and white life ring on a sunny beach",
    section="⑩「何が起きてもおかしくない。でも、たぶん何とかなる」",
    message="未来をコントロールできたことは一度もない。でも今まで人生に完全につぶされたこともない。コントロールは、そもそも必要なかったのかも。",
    tone="素材の重さ：重め（不安）\n→ 見せ方：やさしいポップ（夕焼けのオレンジと水色。勝ち負けのない、確かめるだけの遊び）",
    game_ja="🎬 映画と現実＋これまでの実績：①「🎬 映画」と「🌤️ 現実」を切り替える。映画モードでは音符が流れて「何かが起きるぞ…」の予告が出る。現実モードは音楽も予告もなく、ふつうの1日。②下の「これまでの大変だった日」（大事なテスト・知らない街で迷子・旅先で体調をくずした・大きな失敗・ひどい1週間）を1枚ずつ押すと、くるっと裏返って「✓ 乗りこえた」。5枚全部で「5回中5回。毎回ちゃんと乗りこえてきた」。勝ち負けではなく、安心を確かめるだけの遊び。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of soft alpaca wool, "
            "sitting calmly and smiling next to a realistic orange and white life ring resting on smooth sand. "
            "Bright simple warm sunset-orange and soft sky-blue background with a calm sea horizon giving depth. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × アルパカウール × 浮き輪",
    mood=["lift", "think"], tags=["books", "feelings", "mindset"],
    pal=dict(bg="#fff8f1", muted="#7d6b5f", acc="#e8762c", acc2="#3aa6d8", shadow="rgba(150,90,40,.16)",
             r1="rgba(255,170,90,.30)", r2="rgba(58,166,216,.18)", r3="rgba(255,220,120,.18)",
             h1="#40220c", photo="#ffe9d6", big="#c9611f", bigdark="#ffc79a",
             game="linear-gradient(160deg, #ff9a52 0%, #e8762c 45%, #3aa6d8 100%)"),
    cards=[
        dict(emoji="🎬", label=("Movie Music", "映画の音楽"),
             s=[("In movies, scary music plays before something bad happens.",
                 "映画では、何かが起きる前に、不穏な音楽が流れます。")]),
        dict(emoji="🔇", label=("No Music", "音楽はない"),
             s=[("But real life has no music.", "でも、現実には音楽がありません。"),
                ("Sad things can happen suddenly.", "悲しいことは、突然起きることもあります。")]),
        dict(emoji="🎛️", label=("No Control", "コントロールできない"),
             s=[("Oliver Burkeman says we have never been able to control the future.",
                 "オリバー・バークマンさんによると、私たちは未来をコントロールできたことが、一度もないそうです。")]),
        dict(emoji="🛟", label=("Still Here", "それでも、ここにいる"),
             s=[("But until now, life has never completely crushed us, either.",
                 "でも今まで、人生に完全につぶされたことも、ありません。")]),
        dict(emoji="🌱", label=("Maybe Not Needed", "必要なかったのかも"), big=True,
             s=[("Maybe we never needed control in the first place.",
                 "そもそも、コントロールは必要なかったのかもしれません。")]),
    ],
    game_after=2,
    game_note="映画と現実＋これまでの実績（裏返すカード）",
    game_html="""  <section class="game" data-v="movie" data-all="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Movie or real life?</div>
    <div class="modes">
      <button type="button" class="btn mode md-movie" data-v="movie">🎬 Movie</button>
      <button type="button" class="btn mode md-real" data-v="real">🌤️ Real life</button>
    </div>
    <div class="film">
      <span class="nt nt1" aria-hidden="true">🎵</span><span class="nt nt2" aria-hidden="true">🎶</span><span class="nt nt3" aria-hidden="true">🎻</span>
      <div class="walker" aria-hidden="true"><span class="wk">🐧</span></div>
      <div class="cap c-movie">🎻 Dun, dun, dunnn… Something is coming! Get ready!</div>
      <div class="cap c-real">🔇 No music. No warning. Just a normal day.</div>
    </div>
    <div class="rec-h">📜 Your track record: the hard days so far</div>
    <div class="hint2">Tap each card.</div>
    <div class="days">
""" + TILES + """
    </div>
    <div class="score"><span class="sc-n">0</span> <span class="sc-of">/ 5 ✓</span></div>
    <div class="fin">Track record: 5 out of 5. You made it through every time. 🐧</div>
    <div class="ctrl2"><button type="button" class="btn ghost b-reset">↺ Again</button></div>
  </section>""",
    css="""
  /* 🎬 映画と現実＋これまでの実績 */
  .modes { display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; margin-top: 14px; }
  .mode { flex: 1 1 130px; max-width: 200px; min-height: 52px; background: rgba(255,255,255,.18); color: #fff; box-shadow: inset 0 0 0 2px rgba(255,255,255,.6); }
  .game[data-v="movie"] .md-movie, .game[data-v="real"] .md-real { background: #fff; color: #8a3f0e; box-shadow: 0 5px 0 rgba(0,0,0,.2); }
  .film { position: relative; height: 150px; max-width: 440px; margin: 12px auto 0; border-radius: 20px; overflow: hidden;
    background: linear-gradient(180deg, #2b2340 0%, #4b2f52 100%); transition: background .6s ease; }
  .game[data-v="real"] .film { background: linear-gradient(180deg, #bfe6ff 0%, #f2fbff 70%, #cde9b8 70%, #b8de9e 100%); }
  .walker { position: absolute; left: 0; bottom: 40px; font-size: 40px; line-height: 1; animation: walk 6s linear infinite; }
  .wk { display: inline-block; animation: waddle .45s ease-in-out infinite alternate; }
  @keyframes walk { from { transform: translateX(-50px); } to { transform: translateX(min(470px, 100vw)); } }
  @keyframes waddle { from { transform: rotate(-8deg); } to { transform: rotate(8deg); } }
  .game .film .nt { position: absolute; font-size: 22px; opacity: 0; transition: opacity .4s ease; }
  .nt1 { left: 14%; top: 14%; } .nt2 { left: 46%; top: 8%; } .nt3 { right: 14%; top: 16%; }
  .game[data-v="movie"] .film .nt { opacity: 1; animation: bob 1.4s ease-in-out infinite alternate; }
  .game[data-v="movie"] .nt2 { animation-delay: .4s; } .game[data-v="movie"] .nt3 { animation-delay: .8s; }
  @keyframes bob { from { transform: translateY(0) rotate(-8deg); } to { transform: translateY(-10px) rotate(8deg); } }
  .cap { position: absolute; left: 8px; right: 8px; bottom: 6px; display: none; padding: 5px 8px; border-radius: 10px; font-size: 13.5px; font-weight: 900; line-height: 1.3; }
  .c-movie { background: rgba(0,0,0,.55); color: #ffd8a8; }
  .c-real { background: rgba(255,255,255,.88); color: #2f3a46; }
  .game[data-v="movie"] .c-movie, .game[data-v="real"] .c-real { display: block; }
  .rec-h { margin-top: 18px; font-size: 17px; font-weight: 900; line-height: 1.35; }
  .hint2 { font-size: 14px; font-weight: 800; opacity: .9; }
  .days { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; max-width: 440px; margin: 10px auto 0; }
  .hd { min-height: 64px; padding: 8px 10px; border: 0; border-radius: 16px; cursor: pointer; font: inherit; font-weight: 900; font-size: 15px; line-height: 1.25;
    background: #fff; color: #40220c; box-shadow: 0 5px 0 rgba(0,0,0,.18); -webkit-tap-highlight-color: transparent; touch-action: manipulation; }
  .hd:last-child { grid-column: 1 / -1; }
  .hd:focus-visible { outline: 4px solid #fff; outline-offset: 3px; }
  .hd.flip { animation: flipx .36s ease-in-out; }
  @keyframes flipx { 0% { transform: scaleX(1); } 50% { transform: scaleX(0); } 100% { transform: scaleX(1); } }
  .game .hd .tf { display: inline-flex; align-items: center; gap: 6px; }
  .tf-e { font-size: 22px; }
  .game .hd .tb { display: none; }
  .game .hd.shown .tf { display: none; }
  .game .hd.shown .tb { display: inline; }
  .hd.shown { background: #d7f7e3; color: #17663c; }
  .score { margin-top: 12px; font-size: 18px; font-weight: 900; }
  .sc-n { display: inline-block; min-width: 1.4em; padding: 1px 8px; border-radius: 999px; background: rgba(255,255,255,.25); }
  .fin { display: none; margin-top: 8px; font-size: 17px; font-weight: 900; line-height: 1.45; }
  .game[data-all="1"] .fin { display: block; animation: boing .5s ease; }
  .ctrl2 { margin-top: 10px; min-height: 48px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
""",
    dark="""  html[data-theme="dark"] .game[data-v="real"] .film { background: linear-gradient(180deg, #2b4560 0%, #34506a 70%, #2c4a2a 70%, #284426 100%); }
  html[data-theme="dark"] .c-real { background: rgba(34,36,47,.9); color: #eef4ff; }
  html[data-theme="dark"] .hd { background: #22242f; color: #ffe9d6; }
  html[data-theme="dark"] .hd.shown { background: #1d4a33; color: #b8f3d0; }
  html[data-theme="dark"] .game[data-v="movie"] .md-movie, html[data-theme="dark"] .game[data-v="real"] .md-real { background: #ffe9d6; color: #8a3f0e; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var tiles = [].slice.call(g.querySelectorAll('.hd')), scn = g.querySelector('.sc-n'), n = 0;
  [].forEach.call(g.querySelectorAll('.mode'), function (b) {
    b.addEventListener('click', function () { g.setAttribute('data-v', b.getAttribute('data-v')); });
  });
  tiles.forEach(function (t) {
    t.addEventListener('click', function () {
      if (t.classList.contains('shown')) return;
      t.classList.remove('flip'); void t.offsetWidth; t.classList.add('flip');
      setTimeout(function () {   /* 半分まわったところで表と裏を入れかえる（鏡文字にならない） */
        t.classList.add('shown'); n++; scn.textContent = n;
        if (n === tiles.length) {
          g.setAttribute('data-all', '1');
          if (window.pengessoPop) { var r = g.querySelector('.days').getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['✓', '🛟', '🐧', '🌱', '✨'], 18); }
        }
      }, 180);
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    n = 0; scn.textContent = '0'; g.setAttribute('data-all', '0'); g.setAttribute('data-v', 'movie');
    tiles.forEach(function (t) { t.classList.remove('shown', 'flip'); });
  });
})();
""",
    ja=dict({
        "Movie or real life?": "映画？それとも現実？",
        "🎬 Movie": "🎬 映画",
        "🌤️ Real life": "🌤️ 現実",
        "🎻 Dun, dun, dunnn… Something is coming! Get ready!": "🎻 ジャン、ジャン、ジャーン…何かが起きるぞ！心の準備を！",
        "🔇 No music. No warning. Just a normal day.": "🔇 音楽なし。予告なし。ただのふつうの1日。",
        "📜 Your track record: the hard days so far": "📜 これまでの実績：今までの大変だった日",
        "Tap each card.": "1枚ずつ押してみてね。",
        "✓ Made it": "✓ 乗りこえた",
        "/ 5 ✓": "/ 5 ✓",
        "Track record: 5 out of 5. You made it through every time. 🐧": "実績：5回中5回。毎回ちゃんと乗りこえてきた 🐧",
        "↺ Again": "↺ もう一回",
    }, **{en: ja for _, en, ja in DAYS}),
)

if __name__ == "__main__":
    build(d)
