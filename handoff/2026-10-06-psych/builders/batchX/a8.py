from gen import build

d = dict(
    slug="try-the-vague-interest", seq=529,
    title=("Use a little courage for the thing you are a little curious about",
           "なんとなく興味があることを、少しだけ勇気を出してやってみる"),
    label=("A Little Courage", "少しの勇気"),
    h1_emoji="🚪",
    alt="A chubby brushed mohair penguin peeking curiously at a real pottery wheel with a small clay bowl on it",
    section="一番大事なのは「戦わない」こと（③なんとなく興味があることを、勇気を出してやってみる）",
    message="人はすぐ「やらなくていい理由」を考える。なんとなく興味があることには、少しだけ勇気を出してみる。",
    tone="素材の重さ：真面目（生き方の考え方）\n→ 見せ方：ポップに（ラムネの水色とピーチ。言い訳のシャボン玉わりで遊べる）",
    game_ja="🫧 言い訳のシャボン玉：とびらの前に「時間がない」「もう年だし」「また今度」「どうせへただし」「準備がまだ」のシャボン玉がぷかぷか。押すとパチンとわれて、勇気メーターが1つ上がる。4秒ぼーっとしていると、言い訳が1つもどってくる（「待っていると、言い訳はもどってくる！」）。5つ全部わると、とびらが開いて「🏺 陶芸の体験教室、1回だけ予約した！」。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of soft brushed mohair with a "
            "fluffy halo, peeking curiously around the side of a realistic pottery wheel with a small wet clay bowl on it, one flipper "
            "slightly raised. Bright simple soda sky-blue and soft peach background with gentle depth. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × モヘア × 陶芸のろくろ",
    mood=["lift", "energy"], tags=["psychology", "mindset", "tips"],
    pal=dict(bg="#f2fbff", muted="#5f7686", acc="#1e9bd7", acc2="#ff8f6b", shadow="rgba(30,110,160,.16)",
             r1="rgba(255,160,130,.28)", r2="rgba(60,180,240,.22)", r3="rgba(255,220,120,.18)",
             h1="#103650", photo="#e0f3fc", big="#157fb3", bigdark="#9fdcff",
             game="linear-gradient(150deg, #33c3f0 0%, #4a8ff0 50%, #ff8f6b 100%)"),
    cards=[
        dict(emoji="🙈", label=("We Hate Change", "変化はきらい"),
             s=[("People do not like change, so we quickly think of reasons not to do something.",
                 "人は変化がきらいなので、すぐに「やらなくていい理由」を考えます。")]),
        dict(emoji="💬", label=("The Excuses", "言い訳"),
             s=[("\"I have no time,\" \"I am too old,\" \"Maybe next time.\"",
                 "「時間がない」「もう年だし」「また今度」。")]),
        dict(emoji="🚪", label=("Just a Little", "少しだけ"), big=True,
             s=[("If you are a little curious about something, use just a little courage there.",
                 "なんとなく興味があることがあったら、そこで少しだけ勇気を出してみます。")]),
        dict(emoji="🏺", label=("Small Step", "小さな一歩"),
             s=[("For example, just booking 1 pottery trial class is enough.",
                 "たとえば、気になっていた陶芸の体験教室を、1回だけ予約してみるくらいで十分です。")]),
    ],
    game_after=3,
    game_note="言い訳のシャボン玉（われるたびに勇気が出る）",
    game_html="""  <section class="game" data-n="0" data-back="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Pop the excuses</div>
    <div class="game-hint">Excuses are blocking the door. Tap them to pop!</div>
    <div class="yard">
      <div class="door" aria-hidden="true">
        <div class="behind"><span class="behind-e">🏺</span></div>
        <div class="panel"><span class="knob"></span></div>
      </div>
      <button type="button" class="bub b1"><span class="bt">⏰ No time</span></button>
      <button type="button" class="bub b2"><span class="bt">🎂 Too old</span></button>
      <button type="button" class="bub b3"><span class="bt">📅 Next time</span></button>
      <button type="button" class="bub b4"><span class="bt">😅 I will be bad at it</span></button>
      <button type="button" class="bub b5"><span class="bt">🧳 Not ready yet</span></button>
    </div>
    <div class="cm"><span class="cm-l">💪 Courage</span><span class="cm-bar"><i></i></span><span class="cm-n">0</span><span class="cm-of">/5</span></div>
    <div class="msg">
      <div class="m-play">Pop, pop, pop!</div>
      <div class="m-back">Oh no! If you wait, excuses come back. 🫧</div>
      <div class="m-open">🏺 The door opened! "I booked 1 pottery trial class!"</div>
    </div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Start over</button></div>
  </section>""",
    css="""
  /* 🫧 言い訳のシャボン玉 */
  .yard { position: relative; max-width: 360px; height: 300px; margin: 16px auto 0; border-radius: 26px; background: rgba(255,255,255,.18); }
  .door { position: absolute; left: 50%; top: 40px; width: 140px; height: 210px; transform: translateX(-50%); border-radius: 70px 70px 10px 10px;
    background: #fff3d6; box-shadow: inset 0 0 0 8px #c98a4b; overflow: hidden; }
  .behind { position: absolute; inset: 0; display: grid; place-items: center; font-size: 60px; background: radial-gradient(circle, #fff8c9, #ffd27a); }
  .panel { position: absolute; inset: 8px; border-radius: 62px 62px 4px 4px; background: linear-gradient(180deg, #e89a55, #c9733a);
    transform-origin: 0 50%; transition: transform .7s cubic-bezier(.3,1.3,.5,1); }
  .knob { position: absolute; right: 14px; top: 52%; width: 14px; height: 14px; border-radius: 50%; background: #ffe066; }
  .game[data-n="5"] .panel { transform: scaleX(.08); }
  .game[data-n="5"] .behind-e { display: inline-block; animation: boing .7s ease 2; }
  .bub { position: absolute; display: flex; align-items: center; min-height: 56px; max-width: 170px; padding: 0; border: 0; background: transparent; cursor: pointer;
    font: inherit; transition: transform .2s ease, opacity .2s ease;
    -webkit-tap-highlight-color: transparent; touch-action: manipulation; user-select: none; -webkit-user-select: none; }
  .bt { display: block; padding: 10px 14px; border-radius: 999px; font-size: 15px; font-weight: 900; line-height: 1.2; color: #24506b;
    background: radial-gradient(circle at 30% 25%, #ffffff 0 12%, rgba(225,245,255,.96) 40%, rgba(190,228,255,.96));
    box-shadow: 0 6px 16px rgba(0,60,100,.18), inset 0 0 0 2px rgba(255,255,255,.9); animation: bob 3s ease-in-out infinite alternate; }
  .b1 { left: 4%; top: 30px; } .b2 { right: 4%; top: 64px; } .b2 .bt { animation-delay: -.8s; }
  .b3 { left: 8%; top: 128px; } .b3 .bt { animation-delay: -1.6s; } .b4 { right: 2%; top: 170px; } .b4 .bt { animation-delay: -2.2s; }
  .b5 { left: 22%; top: 228px; } .b5 .bt { animation-delay: -1.1s; }
  @keyframes bob { from { transform: translateY(0); } to { transform: translateY(-8px); } }
  .bub.popped { transform: scale(1.5); opacity: 0; pointer-events: none; }
  .bub.popped .bt { animation: none; }
  .bub.back { animation: comeback .5s ease both; }
  @keyframes comeback { from { transform: scale(.2); opacity: 0; } to { transform: scale(1); opacity: 1; } }
  .cm { display: flex; align-items: center; gap: 8px; max-width: 340px; margin: 14px auto 0; font-size: 15px; font-weight: 900; }
  .cm-bar { position: relative; flex: 1; height: 14px; border-radius: 999px; background: rgba(255,255,255,.28); overflow: hidden; }
  .cm-bar i { position: absolute; inset: 0 auto 0 0; width: 0; border-radius: 999px; background: #ffe066; transition: width .35s cubic-bezier(.2,1.2,.4,1); }
  .msg { margin-top: 12px; min-height: 48px; font-size: 16.5px; font-weight: 900; line-height: 1.4; }
  .msg > div { display: none; }
  .game:not([data-n="5"])[data-back="0"] .m-play, .game:not([data-n="5"])[data-back="1"] .m-back, .game[data-n="5"] .m-open { display: block; animation: boing .45s ease; }
  .ctrl { margin-top: 10px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
""",
    dark="""  html[data-theme="dark"] .door { background: #3a2c22; }
  html[data-theme="dark"] .behind { background: radial-gradient(circle, #5a4a17, #3d3210); }
  html[data-theme="dark"] .bt { color: #0f3a52; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var bubs = [].slice.call(g.querySelectorAll('.bub')), bar = g.querySelector('.cm-bar i'), cn = g.querySelector('.cm-n'), idle = 0;
  function pop(el, list, n) {
    if (!window.pengessoPop) return;
    var r = el.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, n || 10);
  }
  function count() {
    var n = bubs.filter(function (b) { return b.classList.contains('popped'); }).length;
    cn.textContent = n; bar.style.width = (n / 5 * 100) + '%';
    g.setAttribute('data-n', String(n));
    return n;
  }
  function wait() {
    clearTimeout(idle);
    idle = setTimeout(function () {
      var gone = bubs.filter(function (b) { return b.classList.contains('popped'); });
      if (!gone.length || gone.length === 5) return;
      var b = gone[Math.floor(Math.random() * gone.length)];
      b.classList.remove('popped'); b.classList.remove('back'); void b.offsetWidth; b.classList.add('back');
      b.disabled = false;
      g.setAttribute('data-back', '1');
      count(); wait();
    }, 4000);
  }
  bubs.forEach(function (b) {
    b.addEventListener('click', function () {
      if (b.classList.contains('popped')) return;
      pop(b, ['🫧', '💥', '✨'], 8);
      b.classList.remove('back'); b.classList.add('popped'); b.disabled = true;
      g.setAttribute('data-back', '0');
      if (navigator.vibrate) { try { navigator.vibrate(12); } catch (e) {} }
      if (count() === 5) { clearTimeout(idle); setTimeout(function () { pop(g.querySelector('.door'), ['🏺', '🚪', '🐧', '✨', '💪'], 18); }, 450); }
      else wait();
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    clearTimeout(idle);
    bubs.forEach(function (b) { b.classList.remove('popped', 'back'); b.disabled = false; });
    g.setAttribute('data-back', '0'); count();
  });
})();
""",
    ja={
        "Pop the excuses": "言い訳のシャボン玉わり",
        "Excuses are blocking the door. Tap them to pop!": "言い訳が、とびらをふさいでいます。押してわってね！",
        "⏰ No time": "⏰ 時間がない",
        "🎂 Too old": "🎂 もう年だし",
        "📅 Next time": "📅 また今度",
        "😅 I will be bad at it": "😅 どうせへただし",
        "🧳 Not ready yet": "🧳 準備がまだ",
        "💪 Courage": "💪 勇気",
        "/5": "/5",
        "Pop, pop, pop!": "パチン、パチン、パチン！",
        "Oh no! If you wait, excuses come back. 🫧": "あっ！待っていると、言い訳はもどってくる。🫧",
        "🏺 The door opened! \"I booked 1 pottery trial class!\"": "🏺 とびらが開いた！「陶芸の体験教室、1回だけ予約した！」",
        "↺ Start over": "↺ 最初から",
    },
)
build(d)
