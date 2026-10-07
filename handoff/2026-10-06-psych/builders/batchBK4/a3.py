from gen import build

d = dict(
    slug="coming-back-is-the-practice", seq=583, url="https://www.oliverburkeman.com/never",
    title=("In meditation, coming back to your breath is the practice itself",
           "瞑想は、雑念ゼロではなく「戻ること」そのものが練習"),
    label=("Coming Back", "戻る練習"),
    h1_emoji="🫧",
    alt="A chubby brushed mohair penguin sitting calmly with closed eyes on a real round meditation cushion",
    section="⑮「人生は一生『整わない』。それでOK」（瞑想とランニングの話）",
    message="瞑想は雑念ゼロではなく、気が散ったら戻ることのくり返し。ランニングも、サボった次の日に戻れればいい。",
    tone="素材の重さ：ふつう（練習の考え方）\n→ 見せ方：やさしいポップ（青とミント。ふくらむ呼吸の丸に、雑念が勝手にやってくる）",
    game_ja="🫧 呼吸に戻る：スタートを押すと20秒の瞑想。呼吸の丸がゆっくりふくらんだりしぼんだりする。「お昼なに食べよう？」「鍵しめたっけ？」などの雑念が勝手に浮かんで、ペンギンがふらふらする。「🌬️ 呼吸に戻る」を押すと雑念がはじけて「戻れた回数」が+1。点数は集中した時間ではなく、戻れた回数。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of soft brushed mohair with a fuzzy halo, "
            "sitting calmly with eyes gently closed on a realistic round navy blue meditation cushion. Bright simple pale blue and mint "
            "background with soft depth and gentle light. Realistic 3D render, studio lighting, shallow depth of field, physically based "
            "materials, photographic. Centered composition. No humans, no text, no lettering."),
    combo="ペンギン × ブラッシュモヘア × 瞑想用のクッション",
    mood=["lift"], tags=["books", "rest", "mindset"],
    pal=dict(bg="#f3f6ff", muted="#66708f", acc="#4a5ee0", acc2="#2fbfae", shadow="rgba(60,80,170,.16)",
             r1="rgba(127,168,255,.26)", r2="rgba(95,212,196,.22)", r3="rgba(255,214,102,.16)",
             h1="#1e2754", photo="#e4eaff", big="#3c4fd0", bigdark="#b3bfff",
             game="linear-gradient(160deg, #5b6cff 0%, #7fa8ff 55%, #4fcfbf 100%)"),
    cards=[
        dict(emoji="🎯", label=("Not Zero", "ゼロじゃない"),
             s=[("It seems the goal of meditation is not zero thoughts.", "瞑想のゴールは、雑念をゼロにすることではないそうです。")]),
        dict(emoji="🔁", label=("Come Back", "戻る"),
             s=[("When your mind wanders, you come back to your breath.", "気が散ったら、また呼吸に戻る。"),
                ("Coming back again and again is meditation itself.", "その「戻る」をくり返すことが、瞑想そのものです。")]),
        dict(emoji="👟", label=("Running Too", "ランニングも"),
             s=[("Running is the same: the goal can be \"getting good at starting again the day after you skip.\"",
                 "ランニングも同じで、目標は「サボった次の日に、また始めるのがうまくなること」でいいそうです。")]),
        dict(emoji="💙", label=("Every Return", "戻るたびに"), big=True,
             s=[("Each time you come back is one more practice.", "戻れた回数が、そのまま練習の回数です。")]),
    ],
    game_after=2,
    game_note="呼吸に戻る（雑念が勝手に来る → 戻った回数が点数）",
    game_html="""  <section class="game" data-s="idle" data-t="off" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Come back to the breath</div>
    <div class="game-hint">20 seconds of meditation. Thoughts will come by themselves. That is OK!</div>
    <div class="pond">
      <div class="breath" aria-hidden="true"><div class="ring"></div><span class="pen">🐧</span></div>
      <div class="thought">
        <span class="th th0">Lunch… what should I eat?</span>
        <span class="th th1">Did I lock the door?</span>
        <span class="th th2">I should reply to that message…</span>
        <span class="th th3">What was the baseball score?</span>
        <span class="th th4">Coffee sounds good…</span>
        <span class="th th5">Am I doing this right?</span>
      </div>
      <div class="already">You are already here. 🙂</div>
    </div>
    <div class="clock" aria-hidden="true"><i></i></div>
    <div class="score">
      <div class="sc"><span class="sl">🌬️ Comebacks</span> <b class="cb">0</b></div>
      <div class="sc sc2"><span class="sl">💭 Thoughts</span> <b class="tc">0</b></div>
    </div>
    <div class="result">
      <div class="r-big"><span class="rl">🌟 Practices done:</span> <b class="rn">0</b></div>
      <div class="r-t">Every comeback is one practice. Focus time is not even counted! 🙂</div>
    </div>
    <div class="btns">
      <button class="btn b-start" type="button">▶ Start (20 sec)</button>
      <button class="btn big-back b-back" type="button">🌬️ Come back</button>
      <button class="btn ghost b-again" type="button">↺ Try again</button>
    </div>
  </section>""",
    css=r"""
  /* 🫧 呼吸に戻る */
  .pond { position: relative; height: 210px; margin: 14px auto 0; max-width: 400px; border-radius: 26px; background: rgba(255,255,255,.14); overflow: hidden; }
  .breath { position: absolute; left: 50%; top: 50%; width: 150px; height: 150px; margin: -75px 0 0 -75px; display: grid; place-items: center; }
  .ring { position: absolute; inset: 0; border-radius: 50%; background: radial-gradient(circle, rgba(255,255,255,.9) 0%, rgba(255,255,255,.45) 55%, rgba(255,255,255,.12) 100%);
    box-shadow: 0 0 40px rgba(255,255,255,.55); transform: scale(.82); transition: filter .4s ease, opacity .4s ease; }
  .game[data-s="run"] .ring { animation: breathe 4s ease-in-out infinite alternate; }
  @keyframes breathe { from { transform: scale(.78); } to { transform: scale(1.08); } }
  .pen { position: relative; display: inline-block; font-size: 52px; line-height: 1; transition: transform .6s ease; }
  .game[data-t="on"] .ring { filter: grayscale(1); opacity: .45; }
  .game[data-t="on"] .pen { transform: translate(52px, -30px) rotate(18deg); }
  .thought { position: absolute; left: 10px; right: 10px; top: 12px; padding: 10px 12px; border-radius: 20px 20px 20px 6px; background: #fff; color: #3a3f66;
    font-size: 15px; font-weight: 900; line-height: 1.35; opacity: 0; transform: translateY(-10px) scale(.9); transition: opacity .3s ease, transform .3s ease; pointer-events: none; }
  .game[data-t="on"] .thought { opacity: 1; transform: none; }
  .game .th { display: none; }
  .game[data-w="0"] .th0, .game[data-w="1"] .th1, .game[data-w="2"] .th2, .game[data-w="3"] .th3, .game[data-w="4"] .th4, .game[data-w="5"] .th5 { display: inline; }
  .already { position: absolute; left: 0; right: 0; bottom: 10px; font-size: 14px; font-weight: 900; opacity: 0; transition: opacity .3s ease; }
  .game.here .already { opacity: 1; }
  .clock { height: 10px; max-width: 400px; margin: 12px auto 0; border-radius: 999px; background: rgba(255,255,255,.25); overflow: hidden; }
  .clock i { display: block; height: 100%; width: 100%; border-radius: 999px; background: #fff; transform-origin: left; }
  .score { display: flex; justify-content: center; gap: 10px; margin-top: 12px; flex-wrap: wrap; }
  .sc { padding: 8px 14px; border-radius: 999px; background: #fff; color: #3c4fd0; font-size: 15px; font-weight: 900; }
  .sc2 { background: rgba(255,255,255,.22); color: #fff; }
  .sc b { font-size: 20px; }
  .sc.bump { animation: boing .4s ease; }
  .result { display: none; margin-top: 12px; }
  .game[data-s="end"] .result { display: block; }
  .r-big { font-size: 22px; font-weight: 900; }
  .r-big b { font-size: 34px; color: #ffe066; }
  .r-t { margin-top: 6px; font-size: 15px; font-weight: 900; line-height: 1.45; }
  .btns { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-top: 14px; }
  .game .b-back, .game .b-again { display: none; }
  .game[data-s="run"] .b-start, .game[data-s="end"] .b-start { display: none; }
  .game[data-s="run"] .b-back { display: inline-flex; }
  .game[data-s="end"] .b-again { display: inline-flex; }
  .big-back { min-height: 72px; min-width: 240px; font-size: 22px; background: #ffe066; color: #3b2c00; }
  .game[data-t="on"] .big-back { animation: boing .8s ease infinite; }
""",
    dark="""  html[data-theme="dark"] .game .big-back { background: #ffe066; color: #3b2c00; }
  html[data-theme="dark"] .game .sc:not(.sc2) { background: #2b2d3a; color: #c9d1ff; }
  html[data-theme="dark"] .thought { background: #f1f3ff; }""",
    js=r"""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var cbEl = g.querySelector('.cb'), tcEl = g.querySelector('.tc'), rn = g.querySelector('.rn'), clock = g.querySelector('.clock i');
  var LEN = 20000, cb = 0, tc = 0, t0 = 0, tick = 0, nextT = 0, last = -1, hereT = 0;
  function now() { return Date.now(); }
  function bump(el) { var s = el.parentNode; s.classList.remove('bump'); void s.offsetWidth; s.classList.add('bump'); }
  function thought() {
    var w; do { w = Math.floor(Math.random() * 6); } while (w === last);
    last = w; tc++; tcEl.textContent = tc; bump(tcEl);
    g.setAttribute('data-w', String(w)); g.setAttribute('data-t', 'on');
  }
  function loop() {
    var el = now() - t0;
    clock.style.transform = 'scaleX(' + Math.max(0, 1 - el / LEN) + ')';
    if (el >= LEN) { end(); return; }
    if (g.getAttribute('data-t') === 'off' && now() >= nextT) thought();
    tick = setTimeout(loop, 100);
  }
  function start() {
    cb = 0; tc = 0; cbEl.textContent = '0'; tcEl.textContent = '0';
    g.setAttribute('data-s', 'run'); g.setAttribute('data-t', 'off');
    t0 = now(); nextT = t0 + 1800; loop();
  }
  function back() {
    if (g.getAttribute('data-s') !== 'run') return;
    if (g.getAttribute('data-t') === 'on') {
      g.setAttribute('data-t', 'off'); cb++; cbEl.textContent = cb; bump(cbEl);
      nextT = now() + 1600 + Math.random() * 1600;
      var r = g.querySelector('.pond').getBoundingClientRect();
      if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + 40, ['🫧', '💭', '✨'], 8);
    } else {
      g.classList.add('here'); clearTimeout(hereT); hereT = setTimeout(function () { g.classList.remove('here'); }, 1100);
    }
  }
  function end() {
    clearTimeout(tick); g.setAttribute('data-t', 'off'); g.setAttribute('data-s', 'end');
    rn.textContent = cb;
    var r = g.getBoundingClientRect();
    if (cb > 0 && window.pengessoPop) window.pengessoPop(r.left + r.width / 2, Math.max(80, r.top + 200), ['🌟', '🐧', '🫧', '💙'], 18);
  }
  g.querySelector('.b-start').addEventListener('click', start);
  g.querySelector('.b-back').addEventListener('click', back);
  g.querySelector('.b-again').addEventListener('click', start);
})();
""",
    ja={
        "Come back to the breath": "呼吸に戻ろう",
        "20 seconds of meditation. Thoughts will come by themselves. That is OK!": "20秒の瞑想です。雑念は勝手にやってきます。それでOK！",
        "Lunch… what should I eat?": "お昼、なに食べよう…？",
        "Did I lock the door?": "鍵、しめたっけ？",
        "I should reply to that message…": "あのメッセージ、返さなきゃ…",
        "What was the baseball score?": "野球、何点だったかな？",
        "Coffee sounds good…": "コーヒー飲みたいな…",
        "Am I doing this right?": "これ、ちゃんとできてる？",
        "You are already here. 🙂": "もう、ちゃんとここにいますよ 🙂",
        "🌬️ Comebacks": "🌬️ 戻れた回数",
        "💭 Thoughts": "💭 雑念",
        "🌟 Practices done:": "🌟 できた練習：",
        "Every comeback is one practice. Focus time is not even counted! 🙂": "戻るたびに、練習1回。集中できた時間は、数えてもいません！🙂",
        "▶ Start (20 sec)": "▶ スタート（20秒）",
        "🌬️ Come back": "🌬️ 呼吸に戻る",
        "↺ Try again": "↺ もう一回",
    },
)

if __name__ == "__main__":
    build(d)
