from gen import build

d = dict(
    slug="too-many-big-rocks", seq=585, url="https://www.oliverburkeman.com/river",
    title=("There are too many big rocks, so choose a few and let the rest go",
           "大きな石は多すぎる。選んで、ほかは放っておく"),
    label=("Big Rocks", "大きな石"),
    h1_emoji="🪨",
    alt="A chubby matte plastic model kit penguin holding one big smooth stone over a real terracotta clay pot that already has three stones in it",
    section="⑯「積ん読は『バケツ』じゃなくて『川』」（大きな石の話）",
    message="大事なものは多すぎて全部は入らない。一番大事なものを選んで、ほかの大事なものは放っておく覚悟をする。",
    tone="素材の重さ：ちょっと真面目（優先順位の考え方）\n→ 見せ方：ポップに（緑とオレンジ。びんに大きな石を入れて遊べる）",
    game_ja="🫙 びんに石を入れる：「勉強」「健康」「友だち」「旅行」「家族」「趣味」の6つの大きな石をタップすると、びんに入る。でもびんには3つしか入らない。4つ目を入れようとすると、びんがゆれて「入らない！不可能なことは不可能（ヒント：名前に書いてある）」。入れた石をタップすると出せる。3つ選んで「🔒 ふたをする」を押すと、ほかの石はそっと横に転がって「今日は選ばなかっただけ」。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made as a matte plastic model kit with "
            "soft rounded parts, holding one big smooth gray river stone in its flippers above a realistic terracotta clay pot that already "
            "holds three big smooth stones. Bright simple fresh green and warm orange background with soft depth. Realistic 3D render, "
            "studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering."),
    combo="ペンギン × マットなプラモデル × 素焼きの鉢と大きな石",
    mood=["think", "laugh"], tags=["books", "productivity", "mindset"],
    pal=dict(bg="#f6faf5", muted="#64806f", acc="#2a8a63", acc2="#f2a541", shadow="rgba(40,110,80,.16)",
             r1="rgba(242,165,65,.24)", r2="rgba(79,178,134,.22)", r3="rgba(120,160,255,.12)",
             h1="#173a2a", photo="#e2f3e8", big="#227a55", bigdark="#93e2bd",
             game="linear-gradient(155deg, #4fb286 0%, #2a8a63 50%, #f2a541 100%)"),
    cards=[
        dict(emoji="🫙", label=("The Jar Story", "びんの話"),
             s=[("There is a famous story: \"Put the big rocks in the jar first.\"", "「大きな石から先にびんに入れなさい」という有名な話があります。"),
                ("It means, \"Do the important things first.\"", "大事なことから先にやろう、という意味です。")]),
        dict(emoji="🪨", label=("Too Many Rocks", "石が多すぎ"),
             s=[("But really, there are too many big rocks to fit.", "でも実際は、大きな石が多すぎて、入りきりません。")]),
        dict(emoji="✂️", label=("Choose Some", "選ぶ"),
             s=[("So choose the most important ones, and be ready to leave the other important ones.",
                 "だから一番大事なものを選んで、ほかの大事なものは放っておく覚悟をします。")]),
        dict(emoji="😂", label=("Best Trick", "最強のワザ"), big=True,
             s=[("Burkeman calls this his best trick: \"Impossible things cannot actually be done. (Hint: it is in the name.)\"",
                 "バークマンさんは「不可能なことは、実際にはできない（ヒント：名前に書いてある）」を最強のテクニックとして紹介しています。")]),
    ],
    game_after=2,
    game_note="びんに石を入れる（3つしか入らない）",
    game_html="""  <section class="game" data-s="pick" data-k="0" data-o="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Fill your jar</div>
    <div class="game-hint">All 6 rocks are important. Tap them to put them in the jar.</div>
    <div class="jar-wrap">
      <div class="lid" aria-hidden="true"></div>
      <div class="jar">
        <span class="slot"></span><span class="slot"></span><span class="slot"></span>
      </div>
      <div class="jar-n"><b class="kn">0</b><span class="of">/3</span></div>
    </div>
    <div class="rocks">
      <button class="rock" type="button" data-e="📚"><span class="re">📚</span><span class="rt">Study</span></button>
      <button class="rock" type="button" data-e="👟"><span class="re">👟</span><span class="rt">Health</span></button>
      <button class="rock" type="button" data-e="🧡"><span class="re">🧡</span><span class="rt">Friends</span></button>
      <button class="rock" type="button" data-e="✈️"><span class="re">✈️</span><span class="rt">Travel</span></button>
      <button class="rock" type="button" data-e="🏠"><span class="re">🏠</span><span class="rt">Family</span></button>
      <button class="rock" type="button" data-e="🎨"><span class="re">🎨</span><span class="rt">Hobby</span></button>
    </div>
    <div class="msg">
      <div class="m m0">Tap the big rocks to put them in the jar.</div>
      <div class="m m1">Good. Is there room for more?</div>
      <div class="m m3">The jar is full. Close the lid?</div>
      <div class="m mo">🫙💦 It does not fit! Impossible things are impossible. (Hint: it is in the name.)</div>
      <div class="m mc">You chose 3. The others are still important… just not today. That is the rule. 🐧</div>
    </div>
    <div class="btns">
      <button class="btn b-lid" type="button">🔒 Close the lid</button>
      <button class="btn ghost b-again" type="button">↺ Try again</button>
    </div>
  </section>""",
    css=r"""
  /* 🫙 びんに石を入れる */
  .jar-wrap { position: relative; width: 170px; margin: 18px auto 0; padding-top: 18px; }
  .lid { position: absolute; left: 22px; right: 22px; top: -40px; height: 22px; border-radius: 10px; background: #ffe066; box-shadow: 0 5px 0 #d4a900;
    opacity: 0; transition: top .45s cubic-bezier(.3,1.4,.5,1), opacity .2s ease; }
  .game[data-s="closed"] .lid { top: 4px; opacity: 1; }
  .jar { display: flex; flex-direction: column-reverse; align-items: center; justify-content: flex-start; gap: 4px; height: 196px; padding: 12px 8px;
    border-radius: 26px 26px 34px 34px; background: rgba(255,255,255,.28); box-shadow: inset 0 0 0 5px rgba(255,255,255,.9), 0 10px 22px rgba(0,0,0,.12); }
  .game[data-o="1"] .jar { animation: shake .45s ease 2; box-shadow: inset 0 0 0 5px #ffe066, 0 10px 22px rgba(0,0,0,.12); }
  .slot { display: grid; place-items: center; width: 108px; height: 52px; border-radius: 26px; font-size: 30px; line-height: 1;
    background: transparent; transform: scale(.4); opacity: 0; transition: transform .35s cubic-bezier(.2,1.5,.4,1), opacity .2s ease; }
  .slot.on { background: linear-gradient(160deg, #e9e4dc, #b8afa3); box-shadow: inset 0 -6px 0 rgba(0,0,0,.12); transform: none; opacity: 1; }
  .jar-n { margin-top: 8px; font-size: 18px; font-weight: 900; }
  .rocks { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; max-width: 400px; margin: 16px auto 0; }
  .rock { min-height: 72px; padding: 8px 4px; border: 0; border-radius: 40% 46% 38% 44% / 50% 44% 52% 46%; cursor: pointer; font: inherit; color: #3b3328;
    background: linear-gradient(160deg, #f1ece4, #c9c0b3); box-shadow: 0 6px 0 rgba(0,0,0,.18); display: flex; flex-direction: column; align-items: center; gap: 2px;
    transition: transform .3s ease, opacity .4s ease, box-shadow .2s ease; touch-action: manipulation; -webkit-tap-highlight-color: transparent; }
  .rock:active { transform: translateY(4px); box-shadow: 0 2px 0 rgba(0,0,0,.18); }
  .re { font-size: 26px; line-height: 1; }
  .rt { font-size: 14px; font-weight: 900; }
  .rock.sel { background: linear-gradient(160deg, #fff6c9, #ffd65a); box-shadow: 0 0 0 4px #fff, 0 6px 0 rgba(0,0,0,.18); }
  .game[data-s="closed"] .rock:not(.sel) { opacity: .45; transform: translateY(6px) rotate(-8deg); }
  .msg { margin-top: 14px; min-height: 52px; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .msg .m { display: none; }
  .game[data-o="0"][data-s="pick"][data-k="0"] .m0, .game[data-o="0"][data-s="pick"]:not([data-k="0"]) .m1,
  .game[data-o="0"][data-s="full"] .m3, .game[data-o="1"] .mo, .game[data-s="closed"] .mc { display: block; }
  .btns { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-top: 12px; }
  .game .b-lid, .game .b-again { display: none; }
  .game[data-s="full"] .b-lid { display: inline-flex; background: #ffe066; color: #4a3500; }
  .game[data-s="closed"] .b-again { display: inline-flex; }
""",
    dark="""  html[data-theme="dark"] .game .b-lid { background: #ffe066; color: #4a3500; }
  html[data-theme="dark"] .rock { color: #3b3328; }""",
    js=r"""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var slots = [].slice.call(g.querySelectorAll('.slot')), rocks = [].slice.call(g.querySelectorAll('.rock')), kn = g.querySelector('.kn');
  var chosen = [], ot = 0;
  function draw() {
    slots.forEach(function (s, i) { s.textContent = chosen[i] ? chosen[i].getAttribute('data-e') : ''; s.classList.toggle('on', !!chosen[i]); });
    rocks.forEach(function (r) { r.classList.toggle('sel', chosen.indexOf(r) >= 0); });
    kn.textContent = chosen.length;
    g.setAttribute('data-k', String(chosen.length));
    if (g.getAttribute('data-s') !== 'closed') g.setAttribute('data-s', chosen.length >= 3 ? 'full' : 'pick');
  }
  rocks.forEach(function (r) {
    r.addEventListener('click', function () {
      if (g.getAttribute('data-s') === 'closed') return;
      var i = chosen.indexOf(r);
      if (i >= 0) { chosen.splice(i, 1); g.setAttribute('data-o', '0'); draw(); return; }
      if (chosen.length >= 3) {
        g.setAttribute('data-o', '1'); clearTimeout(ot);
        ot = setTimeout(function () { g.setAttribute('data-o', '0'); }, 3200);
        if (navigator.vibrate) { try { navigator.vibrate([20, 40, 20]); } catch (e) {} }
        return;
      }
      chosen.push(r); g.setAttribute('data-o', '0'); draw();
    });
  });
  g.querySelector('.b-lid').addEventListener('click', function () {
    clearTimeout(ot); g.setAttribute('data-o', '0'); g.setAttribute('data-s', 'closed');
    var j = g.querySelector('.jar').getBoundingClientRect();
    if (window.pengessoPop) window.pengessoPop(j.left + j.width / 2, j.top + 20, ['🪨', '✨', '🐧'], 16);
  });
  g.querySelector('.b-again').addEventListener('click', function () {
    chosen = []; g.setAttribute('data-s', 'pick'); g.setAttribute('data-o', '0'); draw();
  });
})();
""",
    ja={
        "Fill your jar": "びんに入れてみよう",
        "All 6 rocks are important. Tap them to put them in the jar.": "6つの石は、どれも大事。タップしてびんに入れてね。",
        "Study": "勉強", "Health": "健康", "Friends": "友だち", "Travel": "旅行", "Family": "家族", "Hobby": "趣味",
        "Tap the big rocks to put them in the jar.": "大きな石をタップして、びんに入れよう。",
        "Good. Is there room for more?": "いいね。まだ入るかな？",
        "The jar is full. Close the lid?": "びんがいっぱい。ふたをする？",
        "🫙💦 It does not fit! Impossible things are impossible. (Hint: it is in the name.)": "🫙💦 入らない！不可能なことは不可能です。（ヒント：名前に書いてある）",
        "You chose 3. The others are still important… just not today. That is the rule. 🐧": "3つ選びました。ほかの石も大事なまま…ただ、今日じゃないだけ。それがルールです 🐧",
        "🔒 Close the lid": "🔒 ふたをする",
        "↺ Try again": "↺ もう一回",
    },
)

if __name__ == "__main__":
    build(d)
