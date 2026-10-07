from gen import build

d = dict(
    slug="cosmic-insignificance-therapy", seq=566, path="nobigdeal",
    title=("From the universe, you are tiny, and that makes you free",
           "宇宙から見れば、自分はちっぽけ。だから自由になれる"),
    label=("Tiny Me", "ちっぽけな私"),
    h1_emoji="🌌",
    alt="A chubby brushed mohair penguin standing on a snowy hill looking up through a realistic small brass telescope at a pastel dusk sky",
    section="⑧「宇宙から見れば、ちっぽけ」",
    message="宇宙から見れば自分はちっぽけな点。だから失敗しても終わりじゃない。自由になれる。",
    tone="素材の重さ：真面目（不安・ストレス）\n→ 見せ方：ポップに（雪の白から宇宙の紺へ。ズームアウトで遊べる）",
    game_ja="🔭 ズームアウト：「誤字のまま送っちゃった！」という悩みの吹き出しとペンギン。「🔭 ズームアウト」を押すたびに、雪の庭 → 街 → 国 → 地球 → 宇宙と世界が広がり、背景の色も変わる。悩みの吹き出しは同じ大きさのまま、世界だけが大きくなるので、どんどん小さな点になる（悩みの大きさ 100% → 0.001%）。宇宙まで行くと「あ、大丈夫じゃん」と星が弾ける。「🔍 ズームイン」で戻れる（+/− のステッパー）。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of soft brushed mohair, "
            "standing on a gentle snowy hill and looking up through a realistic small brass telescope on a wooden tripod. "
            "Bright simple pastel dusk sky in soft lavender and pale blue with depth, a calm wide horizon. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × ブラッシュドモヘア × 真ちゅうの望遠鏡",
    mood=["lift", "laugh"], tags=["books", "mindset", "feelings"],
    pal=dict(bg="#f3f5ff", muted="#64698f", acc="#4a4fd6", acc2="#29b6f6", shadow="rgba(50,60,150,.16)",
             r1="rgba(140,170,255,.30)", r2="rgba(74,79,214,.18)", r3="rgba(41,182,246,.14)",
             h1="#1d1f4d", photo="#e4e8ff", big="#3f44c4", bigdark="#b6baff",
             game="linear-gradient(160deg, #4a4fd6 0%, #2b2f8f 60%, #141742 100%)"),
    cards=[
        dict(emoji="🏔️", label=("Big Views", "大きな景色"),
             s=[("When you see heavy snow or a huge view, your stress can suddenly go away.",
                 "大雪や大きな景色を見ると、ストレスがすっと消えることがあります。")]),
        dict(emoji="🌌", label=("A Tiny Dot", "小さな点"),
             s=[("This is because you remember that you are a tiny dot in the universe.",
                 "自分は宇宙の中の小さな点だと、思い出すからです。")]),
        dict(emoji="™️", label=("His Joke", "商標登録"),
             s=[("Oliver Burkeman calls this \"cosmic insignificance therapy,\" and says he trademarked it (he did not).",
                 "オリバー・バークマンさんはこれを「宇宙的ちっぽけさセラピー」と呼んで、「商標登録した（してない）」と書いています。")]),
        dict(emoji="🕊️", label=("Free To Try", "だから自由"), big=True,
             s=[("If you are tiny, a mistake is not the end of the world, so you become free.",
                 "ちっぽけなら、失敗しても世界は終わらないので、自由になれます。")]),
    ],
    game_after=2,
    game_note="ズームアウト（世界が広がって、悩みが点になる）",
    game_html="""  <section class="game" data-z="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Zoom out from your worry</div>
    <div class="space">
      <span class="bd bd0" aria-hidden="true">🏡</span>
      <span class="bd bd1" aria-hidden="true">🏙️</span>
      <span class="bd bd2" aria-hidden="true">🗾</span>
      <span class="bd bd3" aria-hidden="true">🌍</span>
      <span class="bd bd4" aria-hidden="true">🪐</span>
      <span class="sn sn1" aria-hidden="true">❄️</span><span class="sn sn2" aria-hidden="true">❄️</span>
      <span class="st st1" aria-hidden="true">✨</span><span class="st st2" aria-hidden="true">✨</span><span class="st st3" aria-hidden="true">⭐</span>
      <div class="me">
        <div class="wb">😣 I sent a message with a typo!</div>
        <div class="me-p" aria-hidden="true">🐧</div>
      </div>
      <div class="here">📍 You are here</div>
    </div>
    <div class="lv">
      <span class="lv0">❄️ A snowy garden</span>
      <span class="lv1">🏙️ The city</span>
      <span class="lv2">🗾 The country</span>
      <span class="lv3">🌍 The Earth</span>
      <span class="lv4">🌌 The universe</span>
    </div>
    <div class="size"><span class="sz-l">😣 Size of my worry:</span> <span class="pct">100</span><span class="pc">%</span></div>
    <div class="steps" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div>
    <div class="ctrl">
      <button type="button" class="btn b-in">🔍 Zoom in</button>
      <button type="button" class="btn b-out">🔭 Zoom out</button>
    </div>
    <div class="msgs">
      <div class="m0">Tap 🔭 to zoom out.</div>
      <div class="m1">The world gets bigger. The worry stays the same size.</div>
      <div class="m4">Oh. It's fine. 🌌 (Cosmic insignificance therapy™… not really trademarked.)</div>
    </div>
  </section>""",
    css="""
  /* 🔭 ズームアウト */
  .space { position: relative; height: 250px; max-width: 440px; margin: 16px auto 0; border-radius: 24px; overflow: hidden;
    background: linear-gradient(180deg, #e9f3ff 0%, #ffffff 70%, #eef4fb 100%); transition: background .8s ease; }
  .game[data-z="1"] .space { background: linear-gradient(180deg, #bfe0ff 0%, #dff0ff 70%, #c7d7ea 100%); }
  .game[data-z="2"] .space { background: linear-gradient(180deg, #9fd3ff 0%, #c8f0d2 70%, #8fd6a6 100%); }
  .game[data-z="3"] .space { background: radial-gradient(circle at 50% 55%, #2c3c8f 0%, #141a4d 70%, #0b0e2c 100%); }
  .game[data-z="4"] .space { background: radial-gradient(circle at 50% 55%, #3b2a7a 0%, #160f3d 60%, #07061a 100%); }
  .game .space .bd { position: absolute; left: 50%; top: 50%; font-size: 120px; line-height: 1; opacity: 0; transform: translate(-50%, -50%) scale(.6);
    transition: opacity .6s ease, transform .8s ease; }
  .game[data-z="0"] .bd0, .game[data-z="1"] .bd1, .game[data-z="2"] .bd2, .game[data-z="3"] .bd3, .game[data-z="4"] .bd4 { opacity: .55; transform: translate(-50%, -50%) scale(1.15); }
  .game[data-z="3"] .bd3 { opacity: .95; transform: translate(-50%, -50%) scale(.9); }
  .game[data-z="4"] .bd4 { opacity: .9; transform: translate(-50%, -50%) scale(.7); }
  .sn, .st { position: absolute; font-size: 18px; line-height: 1; opacity: 0; transition: opacity .6s ease; }
  .sn1 { left: 14%; top: 18%; } .sn2 { right: 16%; top: 30%; }
  .st1 { left: 12%; top: 16%; } .st2 { right: 14%; top: 22%; } .st3 { left: 20%; bottom: 14%; }
  .game[data-z="0"] .sn { opacity: .9; }
  .game[data-z="3"] .st, .game[data-z="4"] .st { opacity: .9; }
  .me { position: absolute; left: 50%; top: 50%; width: 230px; margin-left: -115px; margin-top: -62px; transform-origin: 50% 50%;
    transform: scale(var(--s, 1)); transition: transform .8s cubic-bezier(.3,1.2,.4,1); }
  .wb { padding: 10px 12px; border-radius: 16px 16px 16px 4px; background: #fff; color: #2f2a3a; font-size: 15.5px; font-weight: 900; line-height: 1.35;
    box-shadow: 0 6px 0 rgba(0,0,0,.12); }
  .me-p { margin-top: 6px; font-size: 44px; line-height: 1; }
  .here { position: absolute; left: 50%; top: 50%; transform: translate(-50%, 14px); padding: 4px 10px; border-radius: 999px; background: #ffd23f; color: #3b2c00;
    font-size: 13px; font-weight: 900; line-height: 1.2; opacity: 0; transition: opacity .5s .4s ease; }
  .game[data-z="4"] .here { opacity: 1; }
  .game[data-z="4"] .me::after { content: ""; position: absolute; left: 50%; top: 50%; width: 600px; height: 600px; margin: -300px 0 0 -300px; border-radius: 50%;
    border: 40px solid rgba(255,210,63,.75); animation: ring 1.6s ease-out infinite; }
  @keyframes ring { from { transform: scale(1.3); opacity: 1; } to { transform: scale(3); opacity: 0; } }
  .lv { margin-top: 12px; min-height: 28px; font-size: 18px; font-weight: 900; }
  .lv > span { display: none; }
  .game[data-z="0"] .lv0, .game[data-z="1"] .lv1, .game[data-z="2"] .lv2, .game[data-z="3"] .lv3, .game[data-z="4"] .lv4 { display: inline; animation: boing .45s ease; }
  .size { margin-top: 6px; font-size: 15px; font-weight: 900; }
  .pct { display: inline-block; min-width: 2.4em; padding: 1px 8px; border-radius: 999px; background: rgba(255,255,255,.22); font-variant-numeric: tabular-nums; }
  .steps { display: flex; justify-content: center; gap: 8px; margin-top: 10px; }
  .steps i { width: 30px; height: 8px; border-radius: 999px; background: rgba(255,255,255,.25); transition: background .3s ease; }
  .steps i.on { background: #ffd23f; }
  .ctrl { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-top: 12px; }
  .ctrl .btn { flex: 1 1 140px; max-width: 210px; min-height: 58px; }
  .b-out { background: #ffd23f; color: #3b2c00; }
  .b-in { background: rgba(255,255,255,.18); color: #fff; box-shadow: inset 0 0 0 2px rgba(255,255,255,.6); }
  .msgs { min-height: 54px; margin-top: 10px; }
  .msgs > div { display: none; font-size: 16px; font-weight: 900; line-height: 1.45; padding: 4px; }
  .game[data-z="0"] .m0, .game[data-z="1"] .m1, .game[data-z="2"] .m1, .game[data-z="3"] .m1, .game[data-z="4"] .m4 { display: block; }
  .game[data-z="4"] .m4 { animation: boing .5s ease; }
""",
    dark="""  html[data-theme="dark"] .game[data-z="0"] .space { background: linear-gradient(180deg, #2a3550 0%, #39445e 70%, #2c3550 100%); }
  html[data-theme="dark"] .game[data-z="1"] .space { background: linear-gradient(180deg, #23405e 0%, #2d4a66 70%, #283a4f 100%); }
  html[data-theme="dark"] .game[data-z="2"] .space { background: linear-gradient(180deg, #23405e 0%, #24503a 70%, #1e4430 100%); }
  html[data-theme="dark"] .wb { background: #f4f0fa; }
  html[data-theme="dark"] .game .b-out { background: #ffd23f; color: #3b2c00; }
  html[data-theme="dark"] .game .b-in { background: rgba(255,255,255,.1); color: #fff; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var SCALE = [1, .5, .25, .1, .03], PCT = ['100', '40', '8', '0.5', '0.001'];
  var me = g.querySelector('.me'), pct = g.querySelector('.pct'), bi = g.querySelector('.b-in'), bo = g.querySelector('.b-out');
  var dots = [].slice.call(g.querySelectorAll('.steps i')), z = 0, popped = false;
  function draw() {
    g.setAttribute('data-z', z);
    me.style.setProperty('--s', SCALE[z]);
    pct.textContent = PCT[z];
    dots.forEach(function (d, i) { d.classList.toggle('on', i <= z); });
    bi.disabled = z === 0; bo.disabled = z === SCALE.length - 1;
    if (z === SCALE.length - 1 && !popped && window.pengessoPop) {
      popped = true;
      var r = g.querySelector('.space').getBoundingClientRect();
      setTimeout(function () { window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['✨', '🌌', '⭐', '🐧', '🪐'], 20); }, 500);
    }
    if (z < SCALE.length - 1) popped = false;
  }
  bo.addEventListener('click', function () { if (z < SCALE.length - 1) { z++; draw(); } });
  bi.addEventListener('click', function () { if (z > 0) { z--; draw(); } });
  draw();
})();
""",
    ja={
        "Zoom out from your worry": "悩みから、ズームアウトしてみよう",
        "😣 I sent a message with a typo!": "😣 誤字のまま、メッセージを送っちゃった！",
        "📍 You are here": "📍 あなたはここ",
        "❄️ A snowy garden": "❄️ 雪の庭",
        "🏙️ The city": "🏙️ 街",
        "🗾 The country": "🗾 国",
        "🌍 The Earth": "🌍 地球",
        "🌌 The universe": "🌌 宇宙",
        "😣 Size of my worry:": "😣 悩みの大きさ：",
        "🔍 Zoom in": "🔍 ズームイン",
        "🔭 Zoom out": "🔭 ズームアウト",
        "Tap 🔭 to zoom out.": "🔭 を押して、ズームアウトしてね。",
        "The world gets bigger. The worry stays the same size.": "世界は大きくなる。悩みの大きさは、そのまま。",
        "Oh. It's fine. 🌌 (Cosmic insignificance therapy™… not really trademarked.)": "あ、大丈夫じゃん 🌌（宇宙的ちっぽけさセラピー™…本当は商標登録してません）",
    },
)

if __name__ == "__main__":
    build(d)
