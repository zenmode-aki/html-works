from gen import build

d = dict(
    slug="be-kind-right-now", seq=569, path="justdo",
    title=("When you want to be kind, do it right away, and keep it short",
           "優しくしたいと思ったら、その場でやる。短くていい"),
    label=("Kind Now", "今すぐ優しく"),
    h1_emoji="💌",
    alt="A chubby hand-embroidered felt penguin holding out a realistic small envelope with a heart sticker",
    section="⑨「考える前に、やっちゃう」",
    message="優しくしたいと思ったら、その場でやる。ハードルを上げすぎない。短くていい。自分にも同じ。",
    tone="素材の重さ：ふつう（人間関係・やさしさ）\n→ 見せ方：ポップに（ピンクとミント。手紙を飛ばして遊べる）",
    game_ja="💌 ありがとうの手紙：左のペンギンが手紙を持ち、右に友だちのペンギン。「📝 あとで、ちゃんと長く」を押すたびに1日たって、真ん中のハードル（壁）がどんどん高くなる。手紙は壁にぶつかって戻ってくる（1日目「あとでちゃんと書こう」→「完璧じゃないと…」→「今さら送りにくい…」）。「⚡ 今、短く」を押すと、壁が低くなって、手紙がふわっと飛んで届き、友だちのペンギンにハートと「ありがとう！🙂」。何日たっていても、短くなら送れる。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of hand-embroidered felt with visible stitches, "
            "holding out a realistic small cream paper envelope with a red heart sticker, smiling kindly. "
            "Bright simple soft pink and mint background with gentle depth. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × 手刺しゅうのフェルト × 封筒",
    mood=["lift"], tags=["books", "feelings", "tips"],
    pal=dict(bg="#fff5f8", muted="#8a6676", acc="#e0457b", acc2="#2bbf9a", shadow="rgba(160,50,90,.16)",
             r1="rgba(255,120,170,.26)", r2="rgba(43,191,154,.18)", r3="rgba(255,200,80,.16)",
             h1="#4a1328", photo="#ffe3ec", big="#c9366a", bigdark="#ffaecb",
             game="linear-gradient(150deg, #ff7aa2 0%, #e0457b 50%, #2bbf9a 100%)"),
    cards=[
        dict(emoji="🧘", label=("His Rule", "先生のルール"),
             s=[("Oliver Burkeman says the meditation teacher Joseph Goldstein acts right away when he wants to be kind.",
                 "オリバー・バークマンさんによると、瞑想の先生ジョセフ・ゴールドスタインさんは、優しくしたいと思ったら、その場でやるそうです。")]),
        dict(emoji="💭", label=("Not Small", "心は狭くない"),
             s=[("We are not unkind because our hearts are small.",
                 "優しくできないのは、心が狭いからではありません。")]),
        dict(emoji="📏", label=("Bar Too High", "ハードル"),
             s=[("It is because we raise the bar too high: \"I will send a proper long one later.\"",
                 "「あとで、ちゃんとした長いのを送ろう」と、ハードルを上げすぎてしまうからです。")]),
        dict(emoji="💌", label=("Short Is Fine", "短くていい"), big=True,
             s=[("Short is fine, so send it the moment you think of it.",
                 "短くていいので、思った瞬間に送りましょう。")]),
        dict(emoji="💛", label=("You Too", "自分にも"),
             s=[("Being kind to yourself works the same way.", "自分への優しさも、同じです。")]),
    ],
    game_after=3,
    game_note="ありがとうの手紙（あとで長く／今、短く）",
    game_html="""  <section class="game" data-s="idle" data-m="hint" style="--h:34px" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Send a thank-you message</div>
    <div class="lane">
      <div class="day"><span class="dy-l">📅 Day</span> <span class="dn">0</span></div>
      <div class="me-p" aria-hidden="true"><span class="pe">🐧</span></div>
      <div class="letter"><span class="lt-e" aria-hidden="true">💌</span></div>
      <div class="wall"><span class="wl-t">Hurdle</span></div>
      <div class="fr" aria-hidden="true"><span class="pe">🐧</span><span class="hrt">💖</span></div>
      <div class="note">"Thank you! 🙂"</div>
      <div class="ground" aria-hidden="true"></div>
    </div>
    <div class="msgs">
      <div class="m-hint">You want to say thank you to a friend. When will you send it?</div>
      <div class="m-d1">Day 1: "I will write a proper one later."</div>
      <div class="m-d2">"Now it has to be perfect…" 😓 The hurdle grows.</div>
      <div class="m-d3">"It has been too long. It feels strange to send now." 😶</div>
      <div class="m-fast">Sent in 5 seconds! Your friend smiles. 💖</div>
      <div class="m-late">Even after a few days, a short one gets there! 💖</div>
    </div>
    <div class="ctrl">
      <button type="button" class="btn b-later">📝 Later, a long one</button>
      <button type="button" class="btn b-send">⚡ Now, a short one</button>
    </div>
    <div class="ctrl2"><button type="button" class="btn ghost b-reset">↺ Again</button></div>
  </section>""",
    css="""
  /* 💌 ありがとうの手紙 */
  .lane { position: relative; height: 210px; max-width: 440px; margin: 16px auto 0; border-radius: 24px; overflow: hidden;
    background: linear-gradient(180deg, #fff0f6 0%, #ffffff 72%, #d9f6ec 72%, #c4efdf 100%); color: #4a1328; }
  .ground { position: absolute; left: 0; right: 0; bottom: 0; height: 28%; }
  .day { position: absolute; left: 12px; top: 10px; padding: 4px 10px; border-radius: 999px; background: #fff; font-size: 14px; font-weight: 900; box-shadow: 0 3px 0 rgba(0,0,0,.08); }
  .dn { display: inline-block; min-width: 1.2em; }
  .me-p { position: absolute; left: 12px; bottom: 50px; font-size: 44px; line-height: 1; }
  .fr { position: absolute; right: 12px; bottom: 50px; font-size: 44px; line-height: 1; }
  .pe { display: inline-block; }
  .fr .pe { transform: scaleX(-1); }
  .hrt { position: absolute; left: 50%; top: -26px; font-size: 26px; opacity: 0; transform: translateX(-50%) scale(.3); transition: opacity .3s ease, transform .5s cubic-bezier(.3,1.7,.5,1); }
  .game[data-s="sent"] .hrt { opacity: 1; transform: translateX(-50%) scale(1); transition-delay: 1s; }
  .note { position: absolute; right: 8px; top: 12px; max-width: 46%; padding: 6px 10px; border-radius: 14px 14px 4px 14px; background: #fff; color: #4a1328;
    font-size: 14px; font-weight: 900; line-height: 1.3; opacity: 0; transform: translateY(6px); transition: opacity .3s ease, transform .3s ease; }
  .game[data-s="sent"] .note { opacity: 1; transform: none; transition-delay: 1.1s; }
  .wall { position: absolute; left: 50%; bottom: 50px; width: 44px; margin-left: -22px; height: var(--h); display: flex; align-items: flex-start; justify-content: center;
    border-radius: 10px 10px 0 0; background: repeating-linear-gradient(0deg, #ff9fb8 0 14px, #ff86a6 14px 16px); box-shadow: 0 -3px 0 #e0457b inset;
    transition: height .5s cubic-bezier(.3,1.4,.5,1); overflow: hidden; }
  .wl-t { margin-top: 4px; font-size: 10.5px; font-weight: 900; color: #6a0f33; line-height: 1.1; writing-mode: vertical-rl; }
  .letter { position: absolute; left: 58px; bottom: 62px; font-size: 30px; line-height: 1; transition: left 1s ease-in-out; }
  .lt-e { display: inline-block; }
  .letter.bonk { animation: bonk .6s ease; }
  @keyframes bonk { 0% { transform: none; } 45% { transform: translateX(calc(min(440px, 100vw) * .5 - 110px)) rotate(10deg); } 60% { transform: translateX(calc(min(440px, 100vw) * .5 - 125px)) rotate(-15deg); } 100% { transform: none; } }
  .game[data-s="sent"] .letter { left: calc(100% - 64px); }
  .game[data-s="sent"] .lt-e { animation: arc 1s ease-in-out; }
  @keyframes arc { 0% { transform: translateY(0); } 50% { transform: translateY(-90px) rotate(-12deg); } 100% { transform: translateY(0); } }
  .msgs { min-height: 76px; margin-top: 10px; }
  .msgs > div { display: none; font-size: 16px; font-weight: 900; line-height: 1.45; padding: 4px; }
  .game[data-m="hint"] .m-hint, .game[data-m="d1"] .m-d1, .game[data-m="d2"] .m-d2, .game[data-m="d3"] .m-d3, .game[data-m="fast"] .m-fast, .game[data-m="late"] .m-late { display: block; animation: boing .45s ease; }
  .ctrl { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; }
  .ctrl .btn { flex: 1 1 150px; max-width: 220px; min-height: 58px; }
  .b-later { background: rgba(255,255,255,.2); color: #fff; box-shadow: inset 0 0 0 2px rgba(255,255,255,.7); }
  .b-send { background: #fff; color: #c9366a; }
  .game[data-s="sent"] .ctrl { display: none; }
  .ctrl2 { margin-top: 10px; min-height: 48px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
  .game[data-s="idle"] .b-reset { visibility: hidden; }
""",
    dark="""  html[data-theme="dark"] .lane { background: linear-gradient(180deg, #3a2532 0%, #2d2430 72%, #1e3d33 72%, #1a352c 100%); color: #ffe3ec; }
  html[data-theme="dark"] .day, html[data-theme="dark"] .note { background: #22242f; color: #ffe3ec; }
  html[data-theme="dark"] .game .b-send { background: #22242f; color: #ffaecb; }
  html[data-theme="dark"] .game .b-later { background: rgba(255,255,255,.1); color: #fff; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var letter = g.querySelector('.letter'), dn = g.querySelector('.dn'), day = 0;
  function msg(m) { g.setAttribute('data-m', ''); void g.offsetWidth; g.setAttribute('data-m', m); }
  function reset() {
    day = 0; dn.textContent = '0'; letter.classList.remove('bonk');
    g.style.setProperty('--h', '34px'); g.setAttribute('data-s', 'idle'); msg('hint');
  }
  g.querySelector('.b-later').addEventListener('click', function () {
    if (g.getAttribute('data-s') === 'sent') return;
    day++; dn.textContent = day;
    g.setAttribute('data-s', 'later');
    g.style.setProperty('--h', Math.min(34 + day * 24, 150) + 'px');
    letter.classList.remove('bonk'); void letter.offsetWidth; letter.classList.add('bonk');
    msg(day === 1 ? 'd1' : day <= 3 ? 'd2' : 'd3');
    if (navigator.vibrate) { try { navigator.vibrate(20); } catch (e) {} }
  });
  g.querySelector('.b-send').addEventListener('click', function () {
    letter.classList.remove('bonk');
    g.style.setProperty('--h', '16px');
    g.setAttribute('data-s', 'sent'); msg(day ? 'late' : 'fast');
    setTimeout(function () {
      if (g.getAttribute('data-s') !== 'sent' || !window.pengessoPop) return;
      var r = g.querySelector('.fr').getBoundingClientRect();
      window.pengessoPop(r.left + r.width / 2, r.top, ['💖', '💌', '🐧', '✨'], 16);
    }, 1050);
  });
  g.querySelector('.b-reset').addEventListener('click', reset);
  reset();
})();
""",
    ja={
        "Send a thank-you message": "ありがとうを送ろう",
        "📅 Day": "📅 日数：",
        "Hurdle": "ハードル",
        "\"Thank you! 🙂\"": "「ありがとう！🙂」",
        "You want to say thank you to a friend. When will you send it?": "友だちに「ありがとう」を言いたい。いつ送る？",
        "Day 1: \"I will write a proper one later.\"": "1日目：「あとで、ちゃんとしたのを書こう」",
        "\"Now it has to be perfect…\" 😓 The hurdle grows.": "「こうなったら完璧にしないと…」😓 ハードルが高くなる。",
        "\"It has been too long. It feels strange to send now.\" 😶": "「時間がたちすぎて、今さら送りにくい…」😶",
        "Sent in 5 seconds! Your friend smiles. 💖": "5秒で送れた！友だちがにっこり 💖",
        "Even after a few days, a short one gets there! 💖": "何日たっていても、短くなら届く！ 💖",
        "📝 Later, a long one": "📝 あとで、ちゃんと長く",
        "⚡ Now, a short one": "⚡ 今、短く",
        "↺ Again": "↺ もう一回",
    },
)

if __name__ == "__main__":
    build(d)
