from gen import build

FPS = "".join('<span class="fp" aria-hidden="true">👣</span>' for _ in range(5))
CHKS = "\n".join('        <span class="ck">✓ I can handle it</span>' for _ in range(5))

d = dict(
    slug="move-then-your-mind-changes", seq=571, path="anythingcouldhappen",
    title=("Moving first is easier than changing your mind first",
           "考え方を変えてから動くより、動いて考え方を変えるほうが簡単"),
    label=("Move First", "先に動く"),
    h1_emoji="👣",
    alt="A chubby plush corduroy and felt penguin taking one small step forward in realistic tiny red sneakers on a sunny path",
    section="⑩「何が起きてもおかしくない。でも、たぶん何とかなる」",
    message="不安が消えるのを待たない。小さく1歩動くたびに「何とかできる」の証拠が増える。不安は残っていてもいい。",
    tone="素材の重さ：重め（不安）\n→ 見せ方：やさしいポップ（若草色と空色。小さな1歩で遊べる）",
    game_ja="👣 考える？動く？：「🤔 勇気が出るまで考える」を押すと、勇気メーターが少しだけ上がって、すぐ元に戻る（ぐるぐる🔄。回数だけ増える）。「👣 小さく1歩」を押すと、足あとが1つ付いてペンギンが進み、「✓ 何とかできる」の証拠が1つ増えて、勇気メーターがぐんと上がる。ペンギンの上の不安の雲☁️は、最後まで消えない（それでいい）。5歩でゴールの旗🚩。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of plush toy corduroy and felt, "
            "wearing realistic tiny red canvas sneakers and taking one small brave step forward on a sunny dirt path. "
            "Bright simple fresh-green and soft sky-blue background with gentle depth. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × コーデュロイとフェルトのぬいぐるみ × 小さなスニーカー",
    mood=["lift"], tags=["books", "feelings", "mindset"],
    pal=dict(bg="#f4fbf2", muted="#667a62", acc="#3d9a3a", acc2="#2f9ae0", shadow="rgba(50,110,50,.16)",
             r1="rgba(120,210,110,.26)", r2="rgba(47,154,224,.18)", r3="rgba(255,210,90,.18)",
             h1="#1d3a1b", photo="#e2f5de", big="#2f8a2c", bigdark="#a4ec9f",
             game="linear-gradient(150deg, #57b947 0%, #2f9ae0 60%, #6f7bf7 100%)"),
    cards=[
        dict(emoji="😟", label=("Waiting Room", "待っていると"),
             s=[("If you wait until your worry is gone, you can never move.",
                 "不安が消えるのを待ってから動こうとすると、いつまでも動けません。")]),
        dict(emoji="👣", label=("Move First", "先に動く"),
             s=[("Oliver Burkeman says that moving and then changing your mind is easier than changing your mind and then moving.",
                 "オリバー・バークマンさんによると、考え方を変えてから動くより、動いて考え方を変えるほうが簡単だそうです。")]),
        dict(emoji="✅", label=("Proof Grows", "証拠が増える"),
             s=[("Each small step adds one piece of proof: \"I can handle it.\"",
                 "小さく1歩動くたびに、「何とかできる」という証拠が1つ増えます。")]),
        dict(emoji="☁️", label=("Worry Can Stay", "不安はいてもいい"), big=True,
             s=[("It is OK if the worry is still there.", "不安は、残っていてもいいんです。")]),
    ],
    game_after=2,
    game_note="考える？動く？（勇気メーターと足あと）",
    game_html="""  <section class="game" data-s="idle" data-m="hint" style="--step:0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Think first, or move first?</div>
    <div class="road">
      <div class="fps">""" + FPS + """<span class="flag" aria-hidden="true">🚩</span></div>
      <div class="walker"><span class="cloud"><span class="cl-e" aria-hidden="true">☁️</span> <span class="cl-t">Worry</span></span><span class="wk" aria-hidden="true">🐧</span><span class="spin" aria-hidden="true">🔄</span></div>
    </div>
    <div class="meter-l"><span class="ml">💪 Courage</span></div>
    <div class="meter" aria-hidden="true"><i></i></div>
    <div class="loops"><span class="lp-l">🔄 Thinking loops:</span> <span class="lp">0</span></div>
    <div class="cks">
""" + CHKS + """
    </div>
    <div class="msgs">
      <div class="m-hint">Your worry is here. What will you do?</div>
      <div class="m-think">Hmm… a little braver… no, back again. 🔄</div>
      <div class="m-loop">The thinking goes round and round. Still not brave. 🔄</div>
      <div class="m-step1">One step! The worry is still here, but you moved. ✓</div>
      <div class="m-step">Another piece of proof: "I can handle it." ✓</div>
      <div class="m-done">🚩 You made it! The worry is still here, and that is OK. 🎉</div>
    </div>
    <div class="ctrl">
      <button type="button" class="btn b-think">🤔 Think until I feel brave</button>
      <button type="button" class="btn b-step">👣 Take one small step</button>
    </div>
    <div class="ctrl2"><button type="button" class="btn ghost b-reset">↺ Again</button></div>
  </section>""",
    css="""
  /* 👣 考える？動く？ */
  .road { position: relative; height: 150px; max-width: 440px; margin: 16px auto 0; border-radius: 22px; overflow: hidden;
    background: linear-gradient(180deg, #e3f4ff 0%, #f6fcff 58%, #d5efc6 58%, #c2e7ae 100%); }
  .fps { position: absolute; left: 4%; right: 4%; bottom: 14px; display: grid; grid-template-columns: repeat(6, 1fr); align-items: end; }
  .game .fps .fp { display: block; text-align: center; font-size: 22px; line-height: 1; opacity: 0; transform: scale(.4) rotate(-20deg); }
  .game .fps .fp.on { opacity: .85; transform: rotate(-20deg); transition: opacity .3s ease, transform .4s cubic-bezier(.3,1.7,.5,1); }
  .flag { text-align: center; font-size: 30px; line-height: 1; }
  .walker { position: absolute; bottom: 40px; left: calc(4% + (92% / 6) * var(--step)); width: calc(92% / 6); display: flex; flex-direction: column; align-items: center;
    transition: left .55s cubic-bezier(.3,1.3,.5,1); }
  .wk { font-size: 40px; line-height: 1; display: inline-block; }
  .walker.hop .wk { animation: boing .45s ease; }
  .cloud { display: inline-flex; align-items: center; gap: 2px; margin-bottom: 2px; padding: 2px 8px; border-radius: 999px; background: rgba(255,255,255,.9); color: #4a5568;
    font-size: 12px; font-weight: 900; white-space: nowrap; }
  .cl-e { font-size: 16px; }
  .spin { position: absolute; right: -14px; top: 18px; font-size: 20px; opacity: 0; }
  .game[data-m="think"] .spin, .game[data-m="loop"] .spin { opacity: 1; animation: rot 1s linear infinite; }
  @keyframes rot { to { transform: rotate(360deg); } }
  .meter-l { margin-top: 12px; font-size: 14.5px; font-weight: 900; }
  .meter { position: relative; height: 16px; max-width: 360px; margin: 6px auto 0; border-radius: 999px; background: rgba(255,255,255,.25); overflow: hidden; }
  .meter i { position: absolute; inset: 0 auto 0 0; width: 0; border-radius: 999px; background: #ffe066; transition: width .45s cubic-bezier(.2,1.2,.4,1); }
  .loops { margin-top: 8px; font-size: 14px; font-weight: 900; opacity: .9; }
  .lp { display: inline-block; min-width: 1.4em; padding: 0 8px; border-radius: 999px; background: rgba(255,255,255,.22); }
  .cks { display: flex; flex-wrap: wrap; justify-content: center; gap: 6px; max-width: 440px; margin: 10px auto 0; min-height: 34px; }
  .ck { display: none; padding: 5px 10px; border-radius: 999px; background: #fff; color: #2f6d2c; font-size: 13.5px; font-weight: 900; line-height: 1.2; }
  .ck.on { display: inline-block; animation: boing .45s ease; }
  .msgs { min-height: 54px; margin-top: 10px; }
  .msgs > div { display: none; font-size: 16px; font-weight: 900; line-height: 1.45; padding: 4px; }
  .game[data-m="hint"] .m-hint, .game[data-m="think"] .m-think, .game[data-m="loop"] .m-loop, .game[data-m="step1"] .m-step1,
  .game[data-m="step"] .m-step, .game[data-m="done"] .m-done { display: block; animation: boing .45s ease; }
  .ctrl { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; }
  .ctrl .btn { flex: 1 1 150px; max-width: 220px; min-height: 60px; }
  .b-think { background: rgba(255,255,255,.2); color: #fff; box-shadow: inset 0 0 0 2px rgba(255,255,255,.7); }
  .b-step { background: #fff; color: #2f6d2c; }
  .game[data-s="done"] .ctrl { display: none; }
  .ctrl2 { margin-top: 10px; min-height: 48px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
  .game[data-s="idle"] .b-reset { visibility: hidden; }
""",
    dark="""  html[data-theme="dark"] .road { background: linear-gradient(180deg, #24384a 0%, #2b4053 58%, #2a4a26 58%, #244022 100%); }
  html[data-theme="dark"] .cloud { background: rgba(34,36,47,.9); color: #e6edf5; }
  html[data-theme="dark"] .ck { background: #1d4a33; color: #b8f3d0; }
  html[data-theme="dark"] .game .b-step { background: #1d4a33; color: #b8f3d0; }
  html[data-theme="dark"] .game .b-think { background: rgba(255,255,255,.1); color: #fff; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var fps = [].slice.call(g.querySelectorAll('.fp')), cks = [].slice.call(g.querySelectorAll('.ck'));
  var bar = g.querySelector('.meter i'), lp = g.querySelector('.lp'), walker = g.querySelector('.walker');
  var step = 0, loops = 0, backT = 0;
  function msg(m) { g.setAttribute('data-m', ''); void g.offsetWidth; g.setAttribute('data-m', m); }
  function level() { return step * 20; }
  function reset() {
    clearTimeout(backT); step = 0; loops = 0; lp.textContent = '0'; bar.style.width = '0';
    fps.forEach(function (f) { f.classList.remove('on'); }); cks.forEach(function (c) { c.classList.remove('on'); });
    g.style.setProperty('--step', 0); g.setAttribute('data-s', 'idle'); msg('hint');
  }
  g.querySelector('.b-think').addEventListener('click', function () {
    if (g.getAttribute('data-s') === 'done') return;
    g.setAttribute('data-s', 'play');
    loops++; lp.textContent = loops;
    clearTimeout(backT);
    bar.style.width = (level() + 4) + '%';
    backT = setTimeout(function () { bar.style.width = level() + '%'; }, 650);
    msg(loops >= 3 ? 'loop' : 'think');
  });
  g.querySelector('.b-step').addEventListener('click', function () {
    if (g.getAttribute('data-s') === 'done' || step >= fps.length) return;
    clearTimeout(backT);
    fps[step].classList.add('on'); cks[step].classList.add('on');
    step++; g.style.setProperty('--step', step); bar.style.width = level() + '%';
    walker.classList.remove('hop'); void walker.offsetWidth; walker.classList.add('hop');
    if (navigator.vibrate) { try { navigator.vibrate(12); } catch (e) {} }
    if (step >= fps.length) {
      g.setAttribute('data-s', 'done'); msg('done');
      if (window.pengessoPop) { var r = g.querySelector('.flag').getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top, ['🚩', '👣', '🐧', '✨', '💪'], 18); }
    } else { g.setAttribute('data-s', 'play'); msg(step === 1 ? 'step1' : 'step'); }
  });
  g.querySelector('.b-reset').addEventListener('click', reset);
  reset();
})();
""",
    ja={
        "Think first, or move first?": "先に考える？それとも先に動く？",
        "Worry": "不安",
        "💪 Courage": "💪 勇気",
        "🔄 Thinking loops:": "🔄 ぐるぐる考えた回数：",
        "✓ I can handle it": "✓ 何とかできる",
        "Your worry is here. What will you do?": "不安があります。どうする？",
        "Hmm… a little braver… no, back again. 🔄": "うーん…ちょっと勇気が出た…と思ったら、元に戻った 🔄",
        "The thinking goes round and round. Still not brave. 🔄": "考えはぐるぐる回るだけ。まだ勇気は出ない 🔄",
        "One step! The worry is still here, but you moved. ✓": "1歩！不安はまだあるけど、動けた ✓",
        "Another piece of proof: \"I can handle it.\" ✓": "また1つ証拠が増えた：「何とかできる」✓",
        "🚩 You made it! The worry is still here, and that is OK. 🎉": "🚩 ゴール！不安はまだいるけど、それでいい 🎉",
        "🤔 Think until I feel brave": "🤔 勇気が出るまで考える",
        "👣 Take one small step": "👣 小さく1歩",
        "↺ Again": "↺ もう一回",
    },
)

if __name__ == "__main__":
    build(d)
