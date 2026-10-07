from gen import build

d = dict(
    slug="you-can-only-light-a-spark", seq=517,
    title=("You cannot change someone's heart, you can only light a small spark",
           "人の心は変えられない。できるのは、小さなきっかけを作ることだけ"),
    label=("A Spark", "きっかけ"),
    h1_emoji="✨",
    alt="A chubby hand-embroidered felt penguin happily holding a real lit sparkler with small warm sparks",
    section="自分のコップからあふれた水でしか、人は満たせない",
    message="人の心は変えられない。できるのはきっかけを作ることだけ。だから、まず自分が幸せに生きる。",
    tone="素材の重さ：真面目（人は変えられない）\n→ 見せ方：ポップに（オレンジと黄色。押しても動かないペンギンが、楽しそうな姿を見て自分から来る）",
    game_ja="✨ 押すか、楽しむか：くもり空のペンギン（友だち）がいる。「➡️ 変わってよと押す」を押すと、友だちは押し返されて「押さないで…」と雲が濃くなる。「☀️ 自分の1日を楽しむ」を押すと、自分のペンギンが光って、コーヒー・音楽・本で楽しそうにする。3回楽しむと、友だちの雲が消えて、自分から歩いてきて「私もやっていい？」。押した回数と、楽しんだ回数が出る。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of hand-embroidered felt with visible stitches, "
            "smiling and holding up a realistic lit sparkler that gives off a few soft warm golden sparks, glowing happily. "
            "Bright simple warm orange and sunny yellow background with soft depth and a gentle bokeh glow. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × 刺しゅうのフェルト × 手持ち花火",
    mood=["lift", "think"], tags=["psychology", "friends", "happiness"],
    pal=dict(bg="#fffaf0", muted="#8a7560", acc="#e57a00", acc2="#ff4d6d", shadow="rgba(170,110,30,.16)",
             r1="rgba(255,210,63,.34)", r2="rgba(255,77,109,.16)", r3="rgba(123,140,255,.14)",
             h1="#4a2a00", photo="#fff0d6", big="#cc5f00", bigdark="#ffc98a",
             game="linear-gradient(155deg, #7b8cff 0%, #ff9f43 58%, #ffd23f 100%)"),
    cards=[
        dict(emoji="🚪", label=("From Outside", "外からは無理"),
             s=[("You cannot change another person's heart from the outside.",
                 "人の心を、外から変えることはできません。")]),
        dict(emoji="✨", label=("Only A Spark", "きっかけだけ"),
             s=[("All we can do is make a \"spark\" for them to change.",
                 "私たちにできるのは、変わる「きっかけ」を作ることだけです。")]),
        dict(emoji="☀️", label=("Who Can", "作れる人"),
             s=[("And the people who can make that spark are people who live happily from the heart.",
                 "そして、そのきっかけを作れるのは、自分が心から幸せに生きている人です。")]),
        dict(emoji="🐧", label=("You First", "まず自分"), big=True,
             s=[("So the first thing to do is to make yourself happy.",
                 "だから最初にやることは、自分を幸せにすることです。")]),
        dict(emoji="🦁", label=("Needs Courage", "勇気がいる"),
             s=[("This is not living the easy way; it takes a little courage to follow your heart.",
                 "これは楽に生きることとはちがって、心のままに動くには、ちょっと勇気がいります。")]),
    ],
    game_after=3,
    game_note="押すか、楽しむか（押しても動かない・楽しそうだと自分から来る）",
    game_html="""  <section class="game" data-f="idle" data-glow="0" data-end="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Push, or enjoy?</div>
    <div class="game-hint">Your friend is under a gray cloud. What will you do?</div>
    <div class="yard">
      <div class="me">
        <div class="halo" aria-hidden="true"></div>
        <span class="me-p">🐧</span><span class="me-i"></span>
        <div class="tag t-me">You</div>
      </div>
      <div class="fr">
        <div class="cloud"><span class="cl-e">☁️</span></div>
        <div class="fr-say">
          <span class="f-idle">I am fine like this.</span>
          <span class="f-push">Stop pushing me… 😣</span>
          <span class="f-c1">…? What is that?</span>
          <span class="f-c2">You look happy. What is so fun?</span>
          <span class="f-came">Can I try it too?</span>
        </div>
        <span class="fr-p">🐧</span>
        <div class="tag t-fr">Friend</div>
      </div>
    </div>
    <div class="ctl">
      <button type="button" class="btn b-push">➡️ Push them to change</button>
      <button type="button" class="btn b-joy">☀️ Enjoy my own day</button>
    </div>
    <div class="score"><span class="s-p">➡️ Pushes:</span> <span class="np">0</span> <span class="s-sep">·</span> <span class="s-j">☀️ Happy moments:</span> <span class="nj">0</span></div>
    <div class="nudge">Pushing does not move a heart. Try the other button.</div>
    <div class="end">✨ Not by pushing: your friend came by themselves. That is a spark.</div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Start over</button></div>
  </section>""",
    css="""
  /* ✨ 押すか、楽しむか */
  .yard { position: relative; height: 230px; max-width: 420px; margin: 16px auto 0; border-radius: 24px; overflow: hidden;
    background: linear-gradient(#fff4d6, #ffe3b0 78%, #ffd08a 78%); }
  .me, .fr { position: absolute; bottom: 14px; width: 120px; text-align: center; transition: left .9s cubic-bezier(.3,1.2,.5,1), transform .2s ease; }
  .me { left: 4%; }
  .fr { left: calc(96% - 120px); }
  .game[data-f="came"] .fr { left: calc(4% + 106px); }
  .me-p, .fr-p { position: relative; z-index: 1; font-size: 58px; line-height: 1; }
  .halo { z-index: 0; }
  .me-i { position: absolute; right: 8px; bottom: 54px; font-size: 28px; line-height: 1; }
  .halo { position: absolute; left: 50%; bottom: 30px; width: 40px; height: 40px; margin-left: -20px; border-radius: 50%;
    background: radial-gradient(circle, rgba(255,226,90,.95), rgba(255,226,90,0) 70%); opacity: 0; transition: all .45s ease; }
  .game[data-glow="1"] .halo { opacity: 1; width: 90px; height: 90px; margin-left: -45px; bottom: 6px; }
  .game[data-glow="2"] .halo { opacity: 1; width: 120px; height: 120px; margin-left: -60px; bottom: -8px; }
  .game[data-glow="3"] .halo { opacity: 1; width: 150px; height: 150px; margin-left: -75px; bottom: -22px; }
  .me.joy .me-p { display: inline-block; animation: dance .6s ease; }
  @keyframes dance { 25% { transform: rotate(-12deg) translateY(-8px); } 75% { transform: rotate(12deg) translateY(-8px); } }
  .tag { font-size: 12.5px; font-weight: 900; color: #6a4300; }
  .cloud { height: 34px; transition: opacity .6s ease, filter .3s ease; }
  .cl-e { font-size: 40px; line-height: 1; }
  .game[data-f="push"] .cloud { filter: brightness(.55); }
  .game[data-f="c2"] .cloud, .game[data-f="came"] .cloud { opacity: 0; }
  .fr-say { min-height: 52px; display: flex; align-items: flex-end; justify-content: center; margin-bottom: 4px; }
  .fr-say span { display: none; padding: 5px 9px; border-radius: 12px; background: #fff; color: #3a2a1a; font-size: 13px; font-weight: 900; line-height: 1.3; }
  .game[data-f="idle"] .f-idle, .game[data-f="push"] .f-push, .game[data-f="c1"] .f-c1, .game[data-f="c2"] .f-c2, .game[data-f="came"] .f-came { display: inline-block; animation: boing .4s ease; }
  .fr.pushed { animation: pushed .5s ease; }
  @keyframes pushed { 30% { transform: translateX(14px) rotate(8deg); } 60% { transform: translateX(-6px) rotate(-4deg); } }

  .ctl { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 420px; margin: 16px auto 0; }
  .ctl .btn { min-height: 62px; border-radius: 18px; font-size: 15px; padding: 8px 10px; }
  .b-push { background: #e9ecff; color: #2c3577; }
  .b-joy { background: #ffe066; color: #5a3d00; }
  .score { margin-top: 14px; font-size: 15px; font-weight: 900; }
  .np, .nj { display: inline-block; min-width: 1.4em; padding: 1px 8px; border-radius: 999px; background: rgba(255,255,255,.3); }
  .nudge { display: none; margin-top: 10px; font-size: 15px; font-weight: 900; }
  .game.stuck .nudge { display: block; animation: boing .45s ease; }
  .end { display: none; margin: 14px auto 0; max-width: 420px; padding: 12px 14px; border-radius: 18px; background: #fff; color: #7a3d00; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .game[data-end="1"] .end { display: block; animation: boing .5s ease; }
  .game[data-end="1"] .nudge { display: none; }
  .ctrl { margin-top: 12px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
  @media (max-width: 380px) { .me, .fr { width: 104px; } .fr { left: calc(96% - 104px); } .game[data-f="came"] .fr { left: calc(4% + 84px); } .me-p, .fr-p { font-size: 50px; } }
""",
    dark="""  html[data-theme="dark"] .yard { background: linear-gradient(#3a3020, #4a3a22 78%, #5a4526 78%); }
  html[data-theme="dark"] .tag { color: #ffd9a0; }
  html[data-theme="dark"] .fr-say span { background: #2b2d3a; color: #f4f0fa; }
  html[data-theme="dark"] .b-push { background: #2a3050; color: #d6dcff; }
  html[data-theme="dark"] .b-joy { background: #4a3c12; color: #ffe39a; }
  html[data-theme="dark"] .end { background: #2b2d3a; color: #ffd9a0; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var np = 0, nj = 0, glow = 0, ITEMS = ['☕', '🎵', '📚'];
  var me = g.querySelector('.me'), fr = g.querySelector('.fr'), item = g.querySelector('.me-i');
  function num() { g.querySelector('.np').textContent = np; g.querySelector('.nj').textContent = nj; }
  function again(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  g.querySelector('.b-push').addEventListener('click', function () {
    if (g.getAttribute('data-end') === '1') return;
    np++; num();
    g.setAttribute('data-f', 'push');
    again(fr, 'pushed');
    if (navigator.vibrate) { try { navigator.vibrate(25); } catch (e) {} }
    if (np >= 3) g.classList.add('stuck');
  });
  g.querySelector('.b-joy').addEventListener('click', function () {
    if (g.getAttribute('data-end') === '1') return;
    nj++; num();
    glow = Math.min(3, glow + 1);
    g.setAttribute('data-glow', String(glow));
    item.textContent = ITEMS[(nj - 1) % ITEMS.length];
    again(me, 'joy');
    var r = me.getBoundingClientRect();
    if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + 20, ['✨', item.textContent], 8);
    g.setAttribute('data-f', glow === 1 ? 'c1' : glow === 2 ? 'c2' : 'came');
    if (glow === 3) {
      g.classList.remove('stuck');
      setTimeout(function () {
        g.setAttribute('data-end', '1');
        if (window.pengessoPop) { var q = fr.getBoundingClientRect(); window.pengessoPop(q.left + q.width / 2, q.top + 30, ['✨', '🐧', '☀️', '💛'], 18); }
      }, 900);
    }
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    np = 0; nj = 0; glow = 0; num(); item.textContent = '';
    g.classList.remove('stuck');
    g.setAttribute('data-f', 'idle'); g.setAttribute('data-glow', '0'); g.setAttribute('data-end', '0');
  });
})();
""",
    ja={
        "Push, or enjoy?": "押す？それとも、楽しむ？",
        "Your friend is under a gray cloud. What will you do?": "友だちが、くもり空の下にいます。どうする？",
        "You": "自分",
        "Friend": "友だち",
        "I am fine like this.": "このままでいいよ。",
        "Stop pushing me… 😣": "押さないで… 😣",
        "…? What is that?": "…？ それ、なに？",
        "You look happy. What is so fun?": "楽しそうだね。何がそんなに楽しいの？",
        "Can I try it too?": "私もやってみていい？",
        "➡️ Push them to change": "➡️「変わってよ」と押す",
        "☀️ Enjoy my own day": "☀️ 自分の1日を楽しむ",
        "➡️ Pushes:": "➡️ 押した：",
        "·": "·",
        "☀️ Happy moments:": "☀️ 楽しんだ：",
        "Pushing does not move a heart. Try the other button.": "押しても心は動きません。もう1つのボタンを押してみて。",
        "✨ Not by pushing: your friend came by themselves. That is a spark.": "✨ 押したからではなく、友だちが自分から来ました。これが「きっかけ」です。",
        "↺ Start over": "↺ 最初から",
    },
)
build(d)
