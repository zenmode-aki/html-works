from gen import build

d = dict(
    slug="write-the-next-physical-action", seq=588, url="https://www.oliverburkeman.com/physical",
    title=("On your to-do list, write the next action your hands can do",
           "やることリストには「手でできる次の行動」を書く"),
    label=("Hand Actions", "手でできる行動"),
    h1_emoji="📞",
    alt="A chubby boucle wool penguin happily holding the handset of a real red vintage telephone",
    section="⑱「『次に手を動かすこと』を書く」",
    message="やることリストには、ふわっとした目標ではなく、手でできる次の行動を書く。",
    tone="素材の重さ：ふつう（やることリストのコツ）\n→ 見せ方：ポップに（グレーの雲 → オレンジと青。ふわふわのタスクを変換マシンに入れて遊べる）",
    game_ja="🔧 行動に変える機械：「車を直す」「下調べをする」「旅行のことを決める」「計画を立てる」のふわふわした雲のカードをタップすると、機械がガタガタ動いて、カードがくるっと回り「整備士に電話する」「5ページのまとめを印刷する」「決めたことを1ページに書く」「2ページの計画を印刷して手に持つ」に変わる。4枚全部変えると「全部、ヒレでできることになった！」",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of cozy boucle wool with a soft looped "
            "texture, happily holding the handset of a realistic glossy red vintage telephone to its head with one flipper. Bright simple "
            "warm orange and sky blue background with soft depth. Realistic 3D render, studio lighting, shallow depth of field, physically "
            "based materials, photographic. Centered composition. No humans, no text, no lettering."),
    combo="ペンギン × ブークレウール × 赤いレトロな電話",
    mood=["think"], tags=["books", "productivity", "tips"],
    pal=dict(bg="#fff7f1", muted="#80705f", acc="#f0612e", acc2="#3a86ff", shadow="rgba(150,70,30,.16)",
             r1="rgba(255,140,66,.24)", r2="rgba(58,134,255,.16)", r3="rgba(154,165,184,.20)",
             h1="#3b1d0e", photo="#ffe8da", big="#d9501f", bigdark="#ffb08a",
             game="linear-gradient(155deg, #8e9ab0 0%, #6c8cff 45%, #ff8c42 100%)"),
    cards=[
        dict(emoji="☁️", label=("Cloudy Tasks", "ふわふわのタスク"),
             s=[("If you write \"fix the car\" on your list, it is hard to start.", "リストに「車を直す」と書くと、なかなか動けません。")]),
        dict(emoji="📞", label=("Hand Actions", "手でできる行動"),
             s=[("\"Call the mechanic\" is something your hands can do now.", "「整備士に電話する」なら、今すぐ手でできます。"),
                ("\"Do research\" gets easy as \"print a summary of up to 5 pages.\"", "「下調べをする」は、「5ページ以内のまとめを印刷する」にすると動けます。")]),
        dict(emoji="📋", label=("David Allen Too", "アレンさんも"),
             s=[("David Allen of \"GTD\" says a good to-do is \"the next action your hands and feet can do.\"",
                 "『GTD』のデビッド・アレンは、いいToDoは「手足でできる次の行動」だと言っています。")]),
        dict(emoji="✏️", label=("Next Time", "次からは"), big=True,
             s=[("Next time, I will write things my hands can do.", "次にリストを書くときは、手でできることを書いてみます。")]),
    ],
    game_after=2,
    game_note="行動に変える機械（ふわふわのタスク → 手でできる行動）",
    game_html="""  <section class="game" data-k="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">The action machine</div>
    <div class="game-hint">Tap a cloudy task. The machine turns it into something your flippers can do.</div>
    <div class="machine" aria-hidden="true"><span class="gear g1">⚙️</span><span class="mlabel">🔧</span><span class="gear g2">⚙️</span></div>
    <div class="tasks">
      <button class="tk" type="button"><span class="front">☁️ Fix the car</span><span class="back">📞 Call the mechanic</span></button>
      <button class="tk" type="button"><span class="front">☁️ Do research</span><span class="back">🖨️ Print a 5-page summary</span></button>
      <button class="tk" type="button"><span class="front">☁️ Decide on the trip</span><span class="back">📝 Write the decision on 1 page</span></button>
      <button class="tk" type="button"><span class="front">☁️ Make a plan</span><span class="back">🖨️ Print a 2-page plan and hold it</span></button>
    </div>
    <div class="cnt"><span class="cl">🐧 Flipper-ready:</span> <b class="kn">0</b><span class="of">/4</span></div>
    <div class="msg">
      <div class="m m0">Cloudy tasks float. It is hard to grab them.</div>
      <div class="m m1">See? Now you know exactly what to do first.</div>
      <div class="m m4">🎉 All 4 are things your flippers can do right now!</div>
    </div>
    <div class="btns"><button class="btn ghost b-again" type="button">↺ Try again</button></div>
  </section>""",
    css=r"""
  /* 🔧 行動に変える機械 */
  .machine { display: flex; align-items: center; justify-content: center; gap: 10px; margin: 14px auto 0; width: 180px; padding: 8px 12px; border-radius: 18px;
    background: rgba(255,255,255,.2); box-shadow: inset 0 0 0 3px rgba(255,255,255,.5); font-size: 30px; }
  .gear { display: inline-block; line-height: 1; }
  .mlabel { font-size: 34px; }
  .game.work .g1 { animation: spin .5s linear; } .game.work .g2 { animation: spin .5s linear reverse; }
  .game.work .machine { animation: shake .4s ease; }
  @keyframes spin { to { transform: rotate(360deg); } }
  .tasks { display: grid; gap: 10px; max-width: 420px; margin: 14px auto 0; }
  .tk { min-height: 60px; padding: 10px 14px; border: 0; border-radius: 20px; font: inherit; font-size: 17px; font-weight: 900; line-height: 1.35; cursor: pointer;
    text-align: left; color: #556074; background: rgba(240,244,250,.92); box-shadow: 0 5px 0 rgba(0,0,0,.14);
    border: 2px dashed #9aa5b8; touch-action: manipulation; -webkit-tap-highlight-color: transparent; }
  .tk:active { transform: translateY(3px); box-shadow: 0 2px 0 rgba(0,0,0,.14); }
  .tk .front { display: block; filter: blur(.3px); }
  .game .tk .back { display: none; }
  .game .tk.done { color: #3b1d0e; background: #fff1c2; border: 2px solid #ffb703; text-align: left; }
  .game .tk.done .front { display: none; }
  .game .tk.done .back { display: block; }
  .tk.turn { animation: turn .38s ease-in-out; }
  @keyframes turn { 0% { transform: scaleX(1); } 50% { transform: scaleX(0); } 100% { transform: scaleX(1); } }
  .cnt { margin-top: 12px; font-size: 16px; font-weight: 900; }
  .cnt b { display: inline-block; min-width: 1.4em; padding: 1px 8px; border-radius: 999px; background: #fff; color: #d9501f; }
  .msg { margin-top: 10px; min-height: 48px; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .msg .m { display: none; }
  .game[data-k="0"] .m0, .game[data-k="1"] .m1, .game[data-k="2"] .m1, .game[data-k="3"] .m1, .game[data-k="4"] .m4 { display: block; }
  .btns { display: flex; justify-content: center; margin-top: 10px; }
  .game .b-again { display: none; }
  .game[data-k="4"] .b-again { display: inline-flex; }
""",
    dark="""  html[data-theme="dark"] .tk { background: rgba(240,244,250,.92); color: #556074; }
  html[data-theme="dark"] .game .tk.done { background: #fff1c2; color: #3b1d0e; }""",
    js=r"""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var tks = [].slice.call(g.querySelectorAll('.tk')), kn = g.querySelector('.kn'), wt = 0;
  function count() { var k = g.querySelectorAll('.tk.done').length; kn.textContent = k; g.setAttribute('data-k', String(k)); return k; }
  tks.forEach(function (t) {
    t.addEventListener('click', function () {
      if (t.classList.contains('done') || t.classList.contains('turn')) return;
      g.classList.remove('work'); void g.offsetWidth; g.classList.add('work');
      clearTimeout(wt); wt = setTimeout(function () { g.classList.remove('work'); }, 520);
      t.classList.add('turn');
      /* 回転の真ん中（横向きで見えないとき）に中身を入れかえる */
      setTimeout(function () {
        t.classList.add('done');
        var k = count(), r = t.getBoundingClientRect();
        if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, k === 4 ? ['🐧', '✅', '✨', '🔧'] : ['✨', '🔧'], k === 4 ? 18 : 6);
      }, 190);
      setTimeout(function () { t.classList.remove('turn'); }, 400);
    });
  });
  g.querySelector('.b-again').addEventListener('click', function () {
    tks.forEach(function (t) { t.classList.remove('done', 'turn'); }); count();
  });
})();
""",
    ja={
        "The action machine": "行動に変える機械",
        "Tap a cloudy task. The machine turns it into something your flippers can do.": "ふわふわのタスクをタップしてね。機械が、ヒレでできることに変えてくれます。",
        "☁️ Fix the car": "☁️ 車を直す",
        "📞 Call the mechanic": "📞 整備士に電話する",
        "☁️ Do research": "☁️ 下調べをする",
        "🖨️ Print a 5-page summary": "🖨️ 5ページのまとめを印刷する",
        "☁️ Decide on the trip": "☁️ 旅行のことを決める",
        "📝 Write the decision on 1 page": "📝 決めたことを1ページに書く",
        "☁️ Make a plan": "☁️ 計画を立てる",
        "🖨️ Print a 2-page plan and hold it": "🖨️ 2ページの計画を印刷して、手に持つ",
        "🐧 Flipper-ready:": "🐧 ヒレでできる：",
        "Cloudy tasks float. It is hard to grab them.": "ふわふわのタスクは、浮いていてつかめません。",
        "See? Now you know exactly what to do first.": "ほら。最初に何をするか、はっきりわかります。",
        "🎉 All 4 are things your flippers can do right now!": "🎉 4つ全部、今すぐヒレでできることになりました！",
        "↺ Try again": "↺ もう一回",
    },
)

if __name__ == "__main__":
    build(d)
