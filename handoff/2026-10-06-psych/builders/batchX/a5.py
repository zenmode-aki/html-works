from gen import build

d = dict(
    slug="because-everyone-is-going", seq=526,
    title=("When you cannot decide, check if you chose because everyone did",
           "迷ったら「みんなが行くから」で選んでいないか確かめる"),
    label=("Whose Choice", "誰の選択？"),
    h1_emoji="🧭",
    alt="A chubby boucle wool penguin holding a real brass compass and looking at it with a happy face",
    section="一番大事なのは「戦わない」こと（①自分の価値観で生きる）",
    message="迷ったら「みんなが行くから行く」で選んでいないか確かめる。「私が行きたいから」なら、それは自分の選択。",
    tone="素材の重さ：真面目（生き方の考え方）\n→ 見せ方：ポップに（すみれ色とレモン色。理由カードの仕分けで遊べる）",
    game_ja="🧺 理由の仕分け：理由のカードが1枚ずつ出てくる（「みんなが新しいカフェに行くから」「そこのレモンケーキが食べてみたいから」など6枚）。「👥 みんなが…だから」か「💛 私が…したいから」の箱に仕分ける。正解ならカードが箱にすいこまれて数が増える、まちがえるとカードがぷるぷる。全部終わると「💛 が3つ：これはあなたの選択」「👥 のときは、もう1回『私もしたい？』と聞いてみよう」。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of cream boucle wool with a "
            "soft loopy texture, holding a realistic antique brass compass in both flippers and looking down at it with a happy, curious "
            "face. Bright simple violet and lemon yellow background with soft depth. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × ブークレ羊毛 × 真ちゅうのコンパス",
    mood=["lift", "think"], tags=["psychology", "mindset", "friends"],
    pal=dict(bg="#f8f5ff", muted="#71688a", acc="#7b52e0", acc2="#ffc93c", shadow="rgba(90,60,160,.16)",
             r1="rgba(255,214,80,.30)", r2="rgba(130,90,240,.20)", r3="rgba(255,140,180,.16)",
             h1="#2b1d55", photo="#ece4ff", big="#6a3fd6", bigdark="#c9b6ff",
             game="linear-gradient(150deg, #8b5cf6 0%, #b05cd6 50%, #ffb93c 100%)"),
    cards=[
        dict(emoji="🤔", label=("Stuck Between", "板ばさみ"),
             s=[("When we cannot decide in life, we are usually stuck between other people's values and our own.",
                 "人生の選択で迷うのは、たいてい、他人の価値観と自分の価値観の板ばさみになっているときです。")]),
        dict(emoji="👥", label=("Check It", "確かめる"),
             s=[("When I cannot decide, I check: \"Am I going because everyone goes?\"",
                 "迷ったら、「みんなが行くから行く」で選んでいないか、確かめてみます。")]),
        dict(emoji="💛", label=("Your Choice", "自分の選択"), big=True,
             s=[("If it is \"I go because I want to go,\" that choice is surely my own.",
                 "「私が行きたいから行く」なら、その選択はきっと自分のものです。")]),
        dict(emoji="✈️", label=("Trip Example", "旅行なら"),
             s=[("For example, a trip is fun when I choose it by \"the view I want to see.\"",
                 "たとえば旅行先も、「私が見たい景色」で選ぶと楽しいです。")]),
    ],
    game_after=2,
    game_note="理由の仕分け（みんなが…だから／私が…したいから）",
    game_html="""  <section class="game" data-i="0" data-done="0" data-bad="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Sort the reasons</div>
    <div class="game-hint">Whose reason is this? Put each card in a box.</div>
    <div class="deck">
      <div class="rc" data-a="e"><span class="rc-e">☕</span><span class="rc-t">Everyone is going to the new cafe.</span></div>
      <div class="rc" data-a="m"><span class="rc-e">🍋</span><span class="rc-t">I want to try their lemon cake.</span></div>
      <div class="rc" data-a="e"><span class="rc-e">📱</span><span class="rc-t">All my friends have this phone.</span></div>
      <div class="rc" data-a="m"><span class="rc-e">📖</span><span class="rc-t">I want to read English books.</span></div>
      <div class="rc" data-a="e"><span class="rc-e">🏆</span><span class="rc-t">It is No. 1 in the ranking.</span></div>
      <div class="rc" data-a="m"><span class="rc-e">🌊</span><span class="rc-t">I want to see the sea in Malaysia.</span></div>
      <div class="rc-end"><span class="rc-e">🧭</span><span class="rc-t">All sorted!</span></div>
    </div>
    <div class="bins">
      <button type="button" class="btn bin be" data-b="e"><span class="bin-t">👥 Because everyone…</span><span class="bin-n ne">0</span></button>
      <button type="button" class="btn bin bm" data-b="m"><span class="bin-t">💛 Because I want…</span><span class="bin-n nm">0</span></button>
    </div>
    <div class="msg">
      <div class="m-play">Read the card, then tap a box.</div>
      <div class="m-bad">Hmm, read it one more time. 👀</div>
      <div class="m-end">💛 3 choices are really yours. For a 👥 one, ask once more: "Do I want it too?"</div>
    </div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Start over</button></div>
  </section>""",
    css="""
  /* 🧺 理由の仕分け */
  .deck { position: relative; max-width: 360px; height: 150px; margin: 16px auto 0; }
  .rc, .rc-end { position: absolute; inset: 0; display: grid; place-items: center; align-content: center; gap: 6px; padding: 14px 18px;
    border-radius: 24px; background: #fff; color: #2b1d55; box-shadow: 0 10px 0 rgba(0,0,0,.14);
    opacity: 0; transform: translateY(20px) scale(.92); pointer-events: none; transition: opacity .3s ease, transform .35s ease; }
  .rc-e { font-size: 40px; line-height: 1; }
  .rc-t { font-size: 18px; font-weight: 900; line-height: 1.35; }
  .rc.cur { opacity: 1; transform: none; }
  .rc.go-e { opacity: 0; transform: translate(-60%, 70px) scale(.3) rotate(-14deg); }
  .rc.go-m { opacity: 0; transform: translate(60%, 70px) scale(.3) rotate(14deg); }
  .game[data-bad="1"] .rc.cur { animation: shake .4s ease; }
  .game[data-done="1"] .rc-end { opacity: 1; transform: none; background: #fff6c9; }
  .bins { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 380px; margin: 16px auto 0; }
  .bin { flex-direction: column; min-height: 96px; border-radius: 22px 22px 30px 30px; padding: 10px 8px; }
  .bin-t { font-size: 15px; line-height: 1.3; }
  .bin-n { display: block; margin-top: 4px; font-size: 28px; line-height: 1; }
  .be { background: #e8e4f2; color: #4a4360; }
  .bm { background: #fff1b3; color: #6b4b00; }
  .bin.got { animation: boing .4s ease; }
  .msg { margin-top: 12px; min-height: 52px; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .msg > div { display: none; }
  .game[data-done="0"][data-bad="0"] .m-play, .game[data-done="0"][data-bad="1"] .m-bad, .game[data-done="1"] .m-end { display: block; }
  .game[data-done="1"] .m-end { animation: boing .5s ease; }
  .ctrl { margin-top: 10px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
""",
    dark="""  html[data-theme="dark"] .rc, html[data-theme="dark"] .rc-end { background: #2b2d3a; color: #ece6ff; }
  html[data-theme="dark"] .game[data-done="1"] .rc-end { background: #4a3c12; color: #ffe39a; }
  html[data-theme="dark"] .game .be { background: #34364a; color: #d8d2ee; }
  html[data-theme="dark"] .game .bm { background: #4a3c12; color: #ffe39a; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var cards = g.querySelectorAll('.rc'), i = 0, n = { e: 0, m: 0 }, busy = false;
  function pop(el, list) {
    if (!window.pengessoPop) return;
    var r = el.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, 16);
  }
  function show() {
    [].forEach.call(cards, function (c, k) { c.classList.remove('cur', 'go-e', 'go-m'); if (k === i) c.classList.add('cur'); });
  }
  show();
  [].forEach.call(g.querySelectorAll('.bin'), function (b) {
    b.addEventListener('click', function () {
      if (busy || i >= cards.length) return;
      var c = cards[i], want = c.getAttribute('data-a'), got = b.getAttribute('data-b');
      if (want !== got) {
        g.setAttribute('data-bad', '0'); void g.offsetWidth; g.setAttribute('data-bad', '1');
        if (navigator.vibrate) { try { navigator.vibrate([15, 30, 15]); } catch (e) {} }
        return;
      }
      g.setAttribute('data-bad', '0');
      busy = true;
      c.classList.remove('cur'); c.classList.add('go-' + got);
      n[got]++; g.querySelector('.n' + got).textContent = n[got];
      b.classList.remove('got'); void b.offsetWidth; b.classList.add('got');
      if (got === 'm') pop(b, ['💛', '✨']);
      setTimeout(function () {
        busy = false; i++;
        if (i >= cards.length) { g.setAttribute('data-done', '1'); pop(g.querySelector('.deck'), ['💛', '🧭', '🐧', '✨']); }
        else show();
      }, 380);
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    i = 0; n = { e: 0, m: 0 }; busy = false;
    g.querySelector('.ne').textContent = '0'; g.querySelector('.nm').textContent = '0';
    g.setAttribute('data-done', '0'); g.setAttribute('data-bad', '0'); show();
  });
})();
""",
    ja={
        "Sort the reasons": "理由の仕分け",
        "Whose reason is this? Put each card in a box.": "これは誰の理由？カードを箱に入れてね。",
        "Everyone is going to the new cafe.": "みんなが新しいカフェに行くから。",
        "I want to try their lemon cake.": "そこのレモンケーキを食べてみたいから。",
        "All my friends have this phone.": "友達がみんなこのスマホを持っているから。",
        "I want to read English books.": "英語の本を読めるようになりたいから。",
        "It is No. 1 in the ranking.": "ランキングで1位だから。",
        "I want to see the sea in Malaysia.": "マレーシアの海を見たいから。",
        "All sorted!": "仕分け完了！",
        "👥 Because everyone…": "👥 みんなが…だから",
        "💛 Because I want…": "💛 私が…したいから",
        "Read the card, then tap a box.": "カードを読んで、箱を押してね。",
        "Hmm, read it one more time. 👀": "うーん、もう1回読んでみて。👀",
        "💛 3 choices are really yours. For a 👥 one, ask once more: \"Do I want it too?\"": "💛 の3つは、本当にあなたの選択。👥 のときは、もう1回「私もしたい？」と聞いてみよう。",
        "↺ Start over": "↺ 最初から",
    },
)
build(d)
