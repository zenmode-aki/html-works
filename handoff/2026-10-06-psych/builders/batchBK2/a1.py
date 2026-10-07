from gen import build

d = dict(
    slug="real-life-already-started", seq=562, path="reality",
    title=("Your real life does not start after the chores, because it already started",
           "「雑用が片付いたら本当の人生」の日は来ない。もう始まっている"),
    label=("Real Life Now", "もう本番"),
    h1_emoji="🌷",
    alt="A chubby chenille yarn penguin walking through an open wooden garden gate onto a sunny flower path",
    section="⑥「人生の『管制塔』には登れない」",
    message="「これが片付いたら本当の人生」の日は一生来ない。本当の人生は、もう始まっている。",
    tone="素材の重さ：真面目（生き方の考え方）\n→ 見せ方：ポップに（若葉の緑とオレンジ。逃げていく門で遊べる）",
    game_ja="🚪 逃げていく門：「✅ 雑用を1つ片付ける」を押すと、洗濯・お皿・メールなどのチップが1つずつ消える。3つ全部片付けると、新しい雑用が3つ出てきて、「本当の人生」の門が遠くへ逃げていく（距離の数字が増えて、門が小さくなる）。3回くり返すと「雑用は終わらない…もう1つのボタンは？」。「🚶 今から始める」を押すと、雑用も門も消えて、道に花が咲き、ペンギンがそのまま歩いていく。「門はなかった。もう本当の人生の中にいた」。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of soft chenille yarn, "
            "happily stepping through a realistic open wooden garden gate onto a sunny path lined with a few tulips. "
            "Bright simple fresh-green and warm orange background with soft depth, a blurred meadow behind. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × シェニール糸 × 木の庭の門",
    mood=["lift", "think"], tags=["books", "mindset", "happiness"],
    pal=dict(bg="#f5fbef", muted="#617a5f", acc="#24914f", acc2="#ff9f43", shadow="rgba(40,110,60,.16)",
             r1="rgba(255,190,90,.30)", r2="rgba(60,190,110,.20)", r3="rgba(80,170,255,.14)",
             h1="#173d26", photo="#e3f5e2", big="#1d7d43", bigdark="#8fe6ad",
             game="linear-gradient(150deg, #34b56a 0%, #1fa0c9 58%, #ffa04a 100%)"),
    cards=[
        dict(emoji="🧺", label=("Someday Thinking", "いつか思考"),
             s=[("Do you think, \"When these chores are done, my real life will start\"?",
                 "「この雑用が片付いたら、本当の人生が始まる」と思っていませんか。")]),
        dict(emoji="🔁", label=("Chores Return", "また出てくる"),
             s=[("But even when you finish the chores, new ones come again and again.",
                 "でも、雑用は片付けても片付けても、また出てきます。")]),
        dict(emoji="🗓️", label=("No Such Day", "その日は来ない"),
             s=[("Oliver Burkeman says that the day your \"real life starts\" will never come.",
                 "オリバー・バークマンさんによると、その「本当の人生が始まる日」は、一生来ないそうです。"),
                ("I am a perfectionist, so this really hit me.",
                 "完璧主義の私には、これが刺さりました。")]),
        dict(emoji="🌷", label=("Already Here", "もう始まってる"), big=True,
             s=[("Your real life has already started.",
                 "本当の人生は、もう始まっています。")]),
    ],
    game_after=2,
    game_note="逃げていく門（雑用を片付けても、門は遠くへ）",
    game_html="""  <section class="game" data-s="idle" data-m="hint" style="--far:0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Can you reach the gate of real life?</div>
    <div class="game-hint">Finish the chores first… then real life starts. Right?</div>
    <div class="scene">
      <div class="gate"><span class="gate-sign">Real life →</span><span class="gate-e" aria-hidden="true">🚪</span></div>
      <div class="chores">
        <span class="ch" data-i="0"><span class="ch-e">🧺</span> <span class="ch-t">Laundry</span></span>
        <span class="ch" data-i="1"><span class="ch-e">🍽️</span> <span class="ch-t">Dishes</span></span>
        <span class="ch" data-i="2"><span class="ch-e">📧</span> <span class="ch-t">Emails</span></span>
        <span class="ch" data-i="3"><span class="ch-e">🧾</span> <span class="ch-t">Bills</span></span>
        <span class="ch" data-i="4"><span class="ch-e">🧹</span> <span class="ch-t">Cleaning</span></span>
        <span class="ch" data-i="5"><span class="ch-e">🛒</span> <span class="ch-t">Shopping</span></span>
        <span class="ch" data-i="6"><span class="ch-e">📦</span> <span class="ch-t">Returns</span></span>
        <span class="ch" data-i="7"><span class="ch-e">🪴</span> <span class="ch-t">Water the plants</span></span>
        <span class="ch" data-i="8"><span class="ch-e">📱</span> <span class="ch-t">App updates</span></span>
      </div>
      <div class="flowers" aria-hidden="true"><span class="fl">🌷</span><span class="fl">🌼</span><span class="fl">🌷</span><span class="fl">🌻</span></div>
      <div class="road" aria-hidden="true"></div>
      <div class="pg" aria-hidden="true"><span class="pg-e">🐧</span></div>
    </div>
    <div class="stats"><span class="st-l">✅ Chores done:</span> <span class="cnt">0</span> <span class="st-sep">·</span> <span class="st-g">📏 Gate:</span> <span class="dist">10</span> <span class="st-m">m away</span></div>
    <div class="msgs">
      <div class="m-hint">Tap ✅ to finish the chores.</div>
      <div class="m-more">New chores came! The gate moved further away. 😮</div>
      <div class="m-tired">The chores never end… Maybe try the other button? 👀</div>
      <div class="m-now">There was no gate. You were already in real life. 🌷</div>
    </div>
    <div class="ctrl">
      <button type="button" class="btn b-do">✅ Finish a chore</button>
      <button type="button" class="btn b-go">🚶 Start now</button>
    </div>
    <div class="ctrl2"><button type="button" class="btn ghost b-reset">↺ Again</button></div>
  </section>""",
    css="""
  /* 🚪 逃げていく門 */
  .scene { position: relative; height: 210px; max-width: 440px; margin: 16px auto 0; border-radius: 22px; overflow: hidden;
    background: linear-gradient(180deg, #dff3ff 0%, #f4fbff 55%, #e9d9b8 55%, #dcc89e 100%); color: #2f2a3a; transition: background .6s ease; }
  .road { position: absolute; left: 0; right: 0; bottom: 30px; height: 10px; background: rgba(150,120,70,.35); }
  .gate { position: absolute; right: 14px; bottom: 34px; display: flex; flex-direction: column; align-items: center; gap: 2px;
    transform-origin: 50% 100%; transform: translateX(calc(var(--far) * 4px)) scale(calc(1 - var(--far) * .15));
    opacity: calc(1 - var(--far) * .12); transition: transform .7s cubic-bezier(.3,1.4,.5,1), opacity .5s ease; }
  .gate-sign { padding: 3px 8px; border-radius: 8px; background: #ffe48a; color: #5a3d00; font-size: 12px; font-weight: 900; line-height: 1.25; max-width: 92px; }
  .gate-e { font-size: 50px; line-height: 1; }
  .chores { position: absolute; left: 10px; right: 108px; top: 10px; display: flex; flex-wrap: wrap; gap: 6px; align-content: flex-start; }
  .ch { display: none; align-items: center; gap: 2px; padding: 6px 10px; border-radius: 999px; background: #fff; color: #2f2a3a;
    font-size: 14px; font-weight: 900; line-height: 1.2; box-shadow: 0 3px 0 rgba(0,0,0,.12); }
  .ch.on { display: inline-flex; animation: chin .35s cubic-bezier(.3,1.5,.5,1) both; }
  .ch.on.done { opacity: .25; text-decoration: line-through; transform: scale(.9); transition: opacity .3s ease, transform .3s ease; }
  @keyframes chin { from { opacity: 0; transform: translateY(-10px) scale(.7); } to { opacity: 1; transform: none; } }
  .pg { position: absolute; left: 14px; bottom: 30px; font-size: 46px; line-height: 1; transition: transform 1.6s ease-in-out; }
  .pg-e { display: inline-block; }
  .flowers { position: absolute; left: 0; right: 0; bottom: 6px; display: flex; justify-content: space-around; font-size: 26px; opacity: 0; transition: opacity .8s ease; }
  .game[data-s="now"] .scene { background: linear-gradient(180deg, #fff6d6 0%, #fffbe9 55%, #bfe8a4 55%, #a6dd8a 100%); }
  .game[data-s="now"] .chores { opacity: 0; transform: scale(.6); transition: opacity .5s ease, transform .5s ease; }
  .game[data-s="now"] .gate { opacity: 0; transform: scale(.2); }
  .game[data-s="now"] .flowers { opacity: 1; }
  .game[data-s="now"] .pg { transform: translateX(min(230px, 52vw)); }
  .game[data-s="now"] .pg-e { animation: waddle .4s ease-in-out 4 alternate; }
  @keyframes waddle { from { transform: rotate(-9deg); } to { transform: rotate(9deg); } }
  .gate.jump { animation: shake .45s ease; }
  .stats { margin-top: 12px; font-size: 15px; font-weight: 900; line-height: 1.5; }
  .cnt, .dist { display: inline-block; min-width: 1.5em; padding: 1px 8px; border-radius: 999px; background: rgba(255,255,255,.25); }
  .msgs { min-height: 54px; margin-top: 8px; }
  .msgs > div { display: none; font-size: 16px; font-weight: 900; line-height: 1.45; padding: 6px 4px; }
  .game[data-m="hint"] .m-hint, .game[data-m="more"] .m-more, .game[data-m="tired"] .m-tired, .game[data-m="now"] .m-now { display: block; animation: boing .45s ease; }
  .ctrl { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-top: 6px; }
  .ctrl .btn { flex: 1 1 150px; max-width: 220px; min-height: 58px; }
  .b-do { background: #fff; color: #1d5c34; }
  .b-go { background: #ffe066; color: #5a3d00; }
  .game[data-m="tired"] .b-go { animation: boing .7s ease 2; box-shadow: 0 6px 0 rgba(0,0,0,.18), 0 0 0 4px rgba(255,255,255,.8); }
  .game[data-s="now"] .ctrl { display: none; }
  .ctrl2 { margin-top: 10px; min-height: 48px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
  .game[data-s="idle"] .b-reset { visibility: hidden; }
""",
    dark="""  html[data-theme="dark"] .scene { background: linear-gradient(180deg, #24364a 0%, #2b3f55 55%, #4a3f2c 55%, #3e3424 100%); }
  html[data-theme="dark"] .game[data-s="now"] .scene { background: linear-gradient(180deg, #4a4226 0%, #3f3a24 55%, #2f5a2c 55%, #284d25 100%); }
  html[data-theme="dark"] .ch { background: #2b2d3a; color: #f4f0fa; }
  html[data-theme="dark"] .gate-sign { background: #5a4a17; color: #ffe39a; }
  html[data-theme="dark"] .game .b-go { background: #5a4a17; color: #ffe39a; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var chips = [].slice.call(g.querySelectorAll('.ch')), gate = g.querySelector('.gate');
  var cnt = g.querySelector('.cnt'), dist = g.querySelector('.dist');
  var round = 0, done = 0, shown = [], busy = false, waitT = 0;
  function show(r) {
    chips.forEach(function (c) { c.classList.remove('on', 'done'); });
    shown = [0, 1, 2].map(function (k) { return chips[(r * 3 + k) % chips.length]; });
    shown.forEach(function (c) { c.classList.add('on'); });
  }
  function reset() {
    clearTimeout(waitT); busy = false; round = 0; done = 0;
    g.setAttribute('data-s', 'idle'); g.setAttribute('data-m', 'hint'); g.style.setProperty('--far', 0);
    cnt.textContent = '0'; dist.textContent = '10'; show(0);
  }
  reset();
  g.querySelector('.b-do').addEventListener('click', function () {
    if (busy || g.getAttribute('data-s') === 'now') return;
    g.setAttribute('data-s', 'chores');
    var left = shown.filter(function (c) { return !c.classList.contains('done'); });
    if (!left.length) return;
    left[0].classList.add('done'); done++; cnt.textContent = done;
    if (left.length === 1) {
      busy = true;
      waitT = setTimeout(function () {
        round++;
        g.style.setProperty('--far', Math.min(round, 5));
        dist.textContent = 10 + round * 10;
        gate.classList.remove('jump'); void gate.offsetWidth; gate.classList.add('jump');
        g.setAttribute('data-m', 'hint'); void g.offsetWidth;
        g.setAttribute('data-m', round >= 3 ? 'tired' : 'more');
        show(round); busy = false;
        if (navigator.vibrate) { try { navigator.vibrate(25); } catch (e) {} }
      }, 450);
    }
  });
  g.querySelector('.b-go').addEventListener('click', function () {
    clearTimeout(waitT); busy = false;
    g.setAttribute('data-s', 'now'); g.setAttribute('data-m', 'now');
    setTimeout(function () {
      if (g.getAttribute('data-s') !== 'now' || !window.pengessoPop) return;
      var r = g.querySelector('.scene').getBoundingClientRect();
      window.pengessoPop(r.left + r.width * .6, r.top + r.height * .6, ['🌷', '🌼', '🐧', '✨', '🌻'], 18);
    }, 900);
  });
  g.querySelector('.b-reset').addEventListener('click', reset);
})();
""",
    ja={
        "Can you reach the gate of real life?": "「本当の人生」の門まで、たどり着ける？",
        "Finish the chores first… then real life starts. Right?": "まず雑用を片付けて…それから本当の人生。だよね？",
        "Real life →": "本当の人生 →",
        "Laundry": "洗濯",
        "Dishes": "お皿洗い",
        "Emails": "メール",
        "Bills": "支払い",
        "Cleaning": "掃除",
        "Shopping": "買い物",
        "Returns": "返品",
        "Water the plants": "植物の水やり",
        "App updates": "アプリの更新",
        "✅ Chores done:": "✅ 片付けた雑用：",
        "·": "·",
        "📏 Gate:": "📏 門まで：",
        "m away": "m",
        "Tap ✅ to finish the chores.": "✅ を押して、雑用を片付けよう。",
        "New chores came! The gate moved further away. 😮": "新しい雑用が来た！門がもっと遠くへ逃げた 😮",
        "The chores never end… Maybe try the other button? 👀": "雑用が終わらない…もう1つのボタンを押してみる？ 👀",
        "There was no gate. You were already in real life. 🌷": "門なんて、なかった。もう本当の人生の中にいたんです 🌷",
        "✅ Finish a chore": "✅ 雑用を1つ片付ける",
        "🚶 Start now": "🚶 今から始める",
        "↺ Again": "↺ もう一回",
    },
)

if __name__ == "__main__":
    build(d)
