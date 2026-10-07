from gen import build

d = dict(
    slug="life-never-gets-sorted", seq=581, url="https://www.oliverburkeman.com/never",
    title=("Life never gets fully sorted, and that is OK",
           "人生は一生「整わない」。それでOK"),
    label=("Never Sorted", "一生整わない"),
    h1_emoji="🌻",
    alt="A chubby layered cut paper penguin standing in a small sunny garden beside a real wooden garden door that opens onto more flowers",
    section="⑮「人生は一生『整わない』。それでOK」",
    message="「全部整ったら本当の人生」の日は来ない。悩みは堆肥。認めると肩の荷が下りて、今を生きられる。",
    tone="素材の重さ：ちょっと重い（人生の考え方）\n→ 見せ方：ポップに（夕焼けの紫とオレンジ → 最後は庭の緑。ドアを開けても開けても次のドアが出てくる）",
    game_ja="🚪 終わらないドア：「本当の人生」に行くために「🚪 ドアを開ける」を押す → 開けるたびに「受信箱が空になったら…」「部屋が片付いたら…」など次の「〜したら」のドアが出てきて、虹の「本当の人生」の看板はどんどん小さく遠くなる。「🌻 今を生きる」を押すと、ドアが消えて庭になり、開けたドアの数だけ悩み（堆肥）から花が咲く。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made as a layered cut paper diorama "
            "with soft paper edges and gentle shadows between layers, standing happily in a small sunny garden next to a realistic "
            "old wooden garden door that stands open onto a few bright sunflowers. Bright simple warm orange and fresh green background "
            "with soft depth. Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. "
            "Centered composition. No humans, no text, no lettering."),
    combo="ペンギン × 切り絵のジオラマ × 木の庭のドア",
    mood=["lift"], tags=["books", "mindset", "happiness"],
    pal=dict(bg="#fff8ef", muted="#86705f", acc="#e2662f", acc2="#7b5cff", shadow="rgba(120,70,40,.16)",
             r1="rgba(255,170,90,.30)", r2="rgba(123,92,255,.16)", r3="rgba(59,178,115,.18)",
             h1="#3d2418", photo="#ffe9d6", big="#c4501f", bigdark="#ffb48a",
             game="linear-gradient(160deg, #7b5cff 0%, #c25bd6 50%, #ff8a4c 100%)"),
    cards=[
        dict(emoji="🚪", label=("The Waiting Room", "待合室"),
             s=[("We often think, \"When everything is sorted, my real life will start.\"",
                 "私たちはつい「全部整ったら、本当の人生が始まる」と思ってしまいます。")]),
        dict(emoji="📅", label=("That Day", "その日"),
             s=[("But that day never, ever comes.",
                 "でも、その日は一生来ません。")]),
        dict(emoji="😤", label=("Not The Deal", "話が違う"),
             s=[("Burkeman writes that when he noticed this, he first got upset: \"I did not sign up for this!\"",
                 "バークマンさんは、これに気づいたとき、まず「そんな契約してないんだけど！」とムッとしたそうです。")]),
        dict(emoji="🌱", label=("Worry Compost", "悩みは堆肥"),
             s=[("Worries are like compost.", "悩みは「堆肥」みたいなものです。"),
                ("They smell a little, but they help things grow.", "ちょっと臭いけど、ちゃんと何かを育ててくれます。")]),
        dict(emoji="🎒", label=("Lighter Now", "肩が軽い"), big=True,
             s=[("When you accept this, the weight comes off your shoulders, and you can live now.",
                 "それを認めてしまうと、肩の荷が下りて、今を生きられます。")]),
    ],
    game_after=3,
    game_note="終わらないドア（開けても開けても次のドア → 今を生きると庭になる）",
    game_html="""  <section class="game" data-s="hall" data-d="0" data-k="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">The door to real life</div>
    <div class="game-hint">Real life starts behind the door. Open it!</div>
    <div class="hall">
      <div class="goal-wrap"><div class="goal">🌈 Real life</div></div>
      <div class="door-row">
        <div class="door">
          <div class="sign">
            <span class="sg sg0">Once my inbox is empty…</span>
            <span class="sg sg1">Once my room is clean…</span>
            <span class="sg sg2">Once I pass the test…</span>
            <span class="sg sg3">Once I feel ready…</span>
            <span class="sg sg4">Once this busy week ends…</span>
          </div>
          <i class="knob"></i>
        </div>
        <div class="me" aria-hidden="true"><span class="me-e">🐧</span></div>
      </div>
      <div class="cnt"><span class="cl">Doors opened:</span> <b class="n">0</b></div>
    </div>
    <div class="garden">
      <div class="garden-sky" aria-hidden="true"><span class="sun">☀️</span><span class="me2">🐧</span></div>
      <div class="beds">
        <div class="plot"><i class="pile"></i><span class="fl">🌱</span></div>
        <div class="plot"><i class="pile"></i><span class="fl">🌱</span></div>
        <div class="plot"><i class="pile"></i><span class="fl">🌱</span></div>
        <div class="plot"><i class="pile"></i><span class="fl">🌱</span></div>
        <div class="plot"><i class="pile"></i><span class="fl">🌱</span></div>
        <div class="plot"><i class="pile"></i><span class="fl">🌱</span></div>
      </div>
      <div class="cnt"><span class="cl">Flowers from worry compost:</span> <b class="fn">0</b></div>
    </div>
    <div class="msg">
      <div class="m m0">Real life is just behind this door… maybe.</div>
      <div class="m m1">Oh. Another door. 🚪</div>
      <div class="m m3">Real life keeps getting farther away… 😤</div>
      <div class="m mg">The worries became compost, and flowers grew. Real life was here all along. 🌻</div>
    </div>
    <div class="btns">
      <button class="btn b-open" type="button">🚪 Open the door</button>
      <button class="btn b-live" type="button">🌻 Live now</button>
      <button class="btn ghost b-again" type="button">↺ Try again</button>
    </div>
  </section>""",
    css=r"""
  /* 🚪 終わらないドア */
  .hall { margin: 16px auto 0; max-width: 420px; padding: 14px 10px 12px; border-radius: 24px; background: rgba(255,255,255,.14); }
  .goal-wrap { height: 46px; display: flex; align-items: center; justify-content: center; }
  .goal { display: inline-block; padding: 7px 14px; border-radius: 999px; background: linear-gradient(90deg, #ffe066, #ffb3c7, #a5d8ff);
    color: #3b2a55; font-size: 15px; font-weight: 900; transition: transform .45s cubic-bezier(.2,1.2,.4,1), opacity .45s ease; }
  .door-row { display: flex; align-items: flex-end; justify-content: center; gap: 10px; margin-top: 8px; }
  .door { position: relative; width: 156px; height: 196px; border-radius: 16px 16px 6px 6px; padding: 18px 12px;
    background: linear-gradient(180deg, #b8692f, #8f4d1f); box-shadow: inset 0 0 0 6px rgba(255,255,255,.14), 0 10px 0 rgba(0,0,0,.18);
    transform-origin: left center; display: flex; align-items: flex-start; justify-content: center; }
  .sign { width: 100%; min-height: 76px; padding: 9px 8px; border-radius: 12px; background: #fff7e6; color: #5b3414;
    font-size: 14.5px; font-weight: 900; line-height: 1.35; display: flex; align-items: center; justify-content: center; }
  .game .sg { display: none; }
  .game[data-d="0"] .sg0, .game[data-d="1"] .sg1, .game[data-d="2"] .sg2, .game[data-d="3"] .sg3, .game[data-d="4"] .sg4 { display: inline; }
  .knob { position: absolute; right: 16px; top: 112px; width: 14px; height: 14px; border-radius: 50%; background: #ffd34d; box-shadow: 0 2px 0 #b98a00; }
  .door.swing { animation: swing .56s ease-in-out; }
  @keyframes swing { 0% { transform: perspective(700px) rotateY(0); } 45%, 55% { transform: perspective(700px) rotateY(-78deg); opacity: .35; } 100% { transform: perspective(700px) rotateY(0); opacity: 1; } }
  .me { font-size: 44px; line-height: 1; }
  .door.swing + .me { animation: boing .5s ease; }
  .cnt { margin-top: 12px; font-size: 15px; font-weight: 900; }
  .cnt b { display: inline-block; min-width: 1.6em; padding: 2px 8px; border-radius: 999px; background: #fff; color: #7b3fd0; }

  .game .garden { display: none; }
  .game[data-s="garden"] .hall { display: none; }
  .game[data-s="garden"] .garden { display: block; }
  .game[data-s="garden"] { background: linear-gradient(165deg, #6fd3ff 0%, #8fe08a 55%, #3bb273 100%); }
  .game { transition: background .6s ease; }
  .garden { margin: 16px auto 0; max-width: 420px; padding: 12px 10px 12px; border-radius: 24px; background: rgba(255,255,255,.18); }
  .garden-sky { display: flex; justify-content: space-between; align-items: center; padding: 0 8px; font-size: 34px; }
  .garden-sky .me2 { font-size: 44px; animation: boing 1.2s ease 2; }
  .beds { display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; margin-top: 8px; padding: 10px 6px 0; border-radius: 18px;
    background: linear-gradient(180deg, transparent 52%, #8a5a33 52%); }
  .game .plot:not(.on) { display: none; }
  .plot { position: relative; width: 58px; height: 78px; display: flex; align-items: flex-end; justify-content: center; }
  .pile { position: absolute; left: 6px; right: 6px; bottom: 0; height: 22px; border-radius: 50% 50% 8px 8px; background: #5e3a1d; }
  .fl { position: relative; display: inline-block; font-size: 38px; line-height: 1; margin-bottom: 14px; transform-origin: 50% 100%; transform: scale(.4); transition: transform .5s cubic-bezier(.2,1.5,.4,1); }
  .fl.bloom { transform: scale(1); }
  .garden .cnt b { color: #1f8a52; }

  .msg { margin-top: 12px; min-height: 52px; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .msg .m { display: none; }
  .game[data-s="hall"][data-k="0"] .m0, .game[data-s="hall"][data-k="1"] .m1, .game[data-s="hall"][data-k="3"] .m3,
  .game[data-s="garden"] .mg { display: block; }
  .btns { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-top: 12px; }
  .game .b-again { display: none; }
  .game[data-s="garden"] .b-open, .game[data-s="garden"] .b-live { display: none; }
  .game[data-s="garden"] .b-again { display: inline-flex; }
  .b-live { background: #ffe066; color: #4a3500; }
  .game[data-k="3"] .b-live { animation: boing 1s ease infinite; }
""",
    dark="""  html[data-theme="dark"] .game .b-live { background: #ffe066; color: #4a3500; }
  html[data-theme="dark"] .sign { background: #fff1d6; }""",
    js=r"""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var door = g.querySelector('.door'), n = g.querySelector('.n'), goal = g.querySelector('.goal'), fn = g.querySelector('.fn');
  var plots = [].slice.call(g.querySelectorAll('.plot'));
  var FL = ['🌻', '🌷', '🌼', '🌸', '🌻', '🌷'];
  var opened = 0, busy = false, timers = [];
  function setK() { g.setAttribute('data-k', opened === 0 ? '0' : opened < 3 ? '1' : '3'); }
  g.querySelector('.b-open').addEventListener('click', function () {
    if (busy || g.getAttribute('data-s') !== 'hall') return;
    busy = true;
    door.classList.remove('swing'); void door.offsetWidth; door.classList.add('swing');
    setTimeout(function () {
      opened++;
      g.setAttribute('data-d', String(opened % 5));
      n.textContent = opened;
      var sc = Math.max(.42, 1 - opened * .12);
      goal.style.transform = 'scale(' + sc + ')';
      goal.style.opacity = String(Math.max(.45, 1 - opened * .1));
      setK();
    }, 270);
    setTimeout(function () { busy = false; door.classList.remove('swing'); }, 580);
  });
  g.querySelector('.b-live').addEventListener('click', function (e) {
    g.setAttribute('data-s', 'garden');
    var count = Math.min(plots.length, Math.max(1, opened));
    fn.textContent = '0';
    plots.forEach(function (p, i) {
      var f = p.querySelector('.fl');
      f.textContent = '🌱'; f.classList.remove('bloom');
      p.classList.toggle('on', i < count);
      if (i < count) {
        timers.push(setTimeout(function () { f.textContent = FL[i]; f.classList.add('bloom'); fn.textContent = String(i + 1); }, 450 + i * 260));
      }
    });
    var b = g.getBoundingClientRect();
    timers.push(setTimeout(function () {
      if (window.pengessoPop) window.pengessoPop(b.left + b.width / 2, Math.max(80, b.top + 160), ['🌻', '🌷', '🐧', '✨'], 18);
    }, 500 + count * 260));
  });
  g.querySelector('.b-again').addEventListener('click', function () {
    timers.forEach(clearTimeout); timers = [];
    opened = 0; n.textContent = '0';
    goal.style.transform = ''; goal.style.opacity = '';
    g.setAttribute('data-d', '0'); g.setAttribute('data-s', 'hall'); setK();
  });
})();
""",
    ja={
        "The door to real life": "本当の人生へのドア",
        "Real life starts behind the door. Open it!": "ドアの向こうで、本当の人生が始まります。開けてみて！",
        "🌈 Real life": "🌈 本当の人生",
        "Once my inbox is empty…": "受信箱が空になったら…",
        "Once my room is clean…": "部屋が片付いたら…",
        "Once I pass the test…": "テストに受かったら…",
        "Once I feel ready…": "準備ができたと思えたら…",
        "Once this busy week ends…": "この忙しい週が終わったら…",
        "Doors opened:": "開けたドア：",
        "Flowers from worry compost:": "悩みの堆肥から咲いた花：",
        "Real life is just behind this door… maybe.": "本当の人生は、このドアのすぐ向こう…のはず。",
        "Oh. Another door. 🚪": "あれ。またドアだ 🚪",
        "Real life keeps getting farther away… 😤": "本当の人生が、どんどん遠くなっていく… 😤",
        "The worries became compost, and flowers grew. Real life was here all along. 🌻": "悩みが堆肥になって、花が咲きました。本当の人生は、最初からここにありました 🌻",
        "🚪 Open the door": "🚪 ドアを開ける",
        "🌻 Live now": "🌻 今を生きる",
        "↺ Try again": "↺ もう一回",
    },
)

if __name__ == "__main__":
    build(d)
