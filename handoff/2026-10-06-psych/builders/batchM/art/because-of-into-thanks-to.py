FL = [
    ("😣 Because I failed the test…", "😣 試験に落ちたせいで…",
     "☀️ Thanks to that, I understand others who failed.", "☀️ そのおかげで、落ちた人の気持ちがわかる。"),
    ("😩 Because I missed the train…", "😩 電車に乗りおくれたせいで…",
     "☕ Thanks to that, I found a nice cafe by the station.", "☕ そのおかげで、駅の近くのすてきなカフェを見つけた。"),
    ("😭 Because we lost the match…", "😭 試合に負けたせいで…",
     "🔥 Thanks to that, we started to practice harder.", "🔥 そのおかげで、もっと練習するようになった。"),
]
_fl = "\n".join(
    f'      <button type="button" class="flip"><span class="f-in"><span class="f-front">{a}<span class="f-tap" aria-hidden="true">🔄</span></span><span class="f-back">{c}</span></span></button>'
    for a, b, c, d in FL)
_ja = {}
for a, b, c, d in FL:
    _ja[a] = b; _ja[c] = d

A = dict(
    slug="because-of-into-thanks-to", seq=418,
    title='You cannot erase the past, but you can change "because of" into "thanks to"',
    title_ja="過去は消せない。でも「〜のせいで」は「〜のおかげで」に変えられる",
    label="Thanks To", label_ja="おかげで",
    float="🐻‍❄️",
    alt="A chubby cut paper penguin watering a small sprout growing from a real old rain boot",
    mood=["lift", "think"], tags=["psychology", "mistakes", "mindset"],
    src_no="19", src_title="「せいで」を「おかげで」に",
    center="過去は消せないし、忘れようとするほど思い出す。でも「〜のせいで」を「〜のおかげで」に言いかえれば、見方は変えられる。",
    tone="素材の重さ：真面目（イヤな過去）\n→ 見せ方：ポップに（青とオレンジ。シロクマ実験の小ネタと、言葉をひっくり返すカード）",
    tone_css="真面目な話 → ポップに。青とオレンジ",
    game_name="シロクマ実験と、ひっくり返しカード",
    play="🐻‍❄️ ① シロクマ実験：「🙈 シロクマを忘れる！」を押すたびに、頭の中のシロクマが1頭ずつ増える（最大6頭）。3頭をこえると「😅 忘れようとするほど増える」。② 言葉のひっくり返しカード：3枚（試験に落ちた／電車に乗りおくれた／試合に負けた）を押すと、くるっと回って「〜のせいで」が「そのおかげで〜」に変わる。1枚めくるごとに、頭の中のシロクマが2頭ずつ 💤 おやすみ。3枚全部めくると「過去は同じ。変わったのは言葉だけ」🎉。「↺ もう一回」。",
    prompt="An extremely cute, chubby round penguin with a gentle face and a plain white belly (no rings or patterns on the belly), made as a layered cut paper diorama with soft paper edges and gentle shadows between the layers, holding a small watering can over one realistic old yellow rubber rain boot that has become a flower pot, with one fresh green sprout growing out of it. Bright background in clear sky blue and warm sunny orange with gentle depth, simple and uncluttered. Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering.",
    combo="ペンギン × 切り絵のジオラマ × 古い長ぐつの植木鉢",
    pal=dict(bg="#f3f6ff", text="#1f2746", muted="#636b8a", a="#3d5af1", b="#ff9f1c", c="#2ec4b6", d="#ff5d8f",
             big="#3550e0", bigdark="#b8c4ff", h1="#1a2250", ink="#1f2746", shadowc="rgba(61,90,241,.16)",
             bg1="rgba(255,159,28,.24)", bg2="rgba(46,196,182,.16)", bg3="rgba(61,90,241,.12)", photo="#e4e9ff",
             game="linear-gradient(155deg, #5b7cff 0%, #3d5af1 45%, #16a99b 100%)"),
    cards=[
        dict(e="🐻‍❄️", l="White Bear", lj="シロクマ", s=[(
            'It seems that if you hear "Do not think about a white bear," you think about it more.',
            "「シロクマのことは考えないで」と言われると、逆にもっと考えてしまうそうです。", False)]),
        dict(e="🌀", l="Trying To Forget", lj="忘れようとすると", s=[(
            "Bad memories too: the more you try to forget, the more you remember.",
            "イヤな思い出も、忘れようとするほど思い出してしまいます。", False)]),
        dict(e="👓", l="New View", lj="見方", s=[(
            "You cannot erase the past, but you can change how you see it.",
            "過去は消せませんが、見方は変えられます。", False)]),
        dict(e="🔄", l="The Trick", lj="コツ", s=[(
            'The trick is to change "because of" into "thanks to."',
            "コツは、「〜のせいで」を「〜のおかげで」に言いかえることです。", True)],
             extra='''    <div class="vs" aria-hidden="true">
      <div class="vs-a"><b class="e">😣</b>Because of…</div>
      <div class="vs-b"><b class="e">☀️</b>Thanks to…</div>
    </div>''', extra_ja={"Because of…": "〜のせいで…", "Thanks to…": "〜のおかげで…"}),
        "GAME",
    ],
    game_html=r'''
  <!-- ⚡ 触って遊べる部品：シロクマ実験（忘れようとすると増える）＋ 言葉のひっくり返しカード（めくるとシロクマがおやすみ） -->
  <section class="game" data-n="1" data-b3="0" data-all="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Try to forget the white bear</div>
    <div class="head-box">
      <div class="head" aria-hidden="true">
        <span class="bear on">🐻‍❄️</span><span class="bear">🐻‍❄️</span><span class="bear">🐻‍❄️</span><span class="bear">🐻‍❄️</span><span class="bear">🐻‍❄️</span><span class="bear">🐻‍❄️</span>
      </div>
      <div class="bear-cnt"><span class="bc-l">Bears in your head:</span> <span class="bc-n">1</span></div>
    </div>
    <div class="ctrl"><button type="button" class="btn b-forget">🙈 Forget the bear!</button></div>
    <div class="msg m-b3">😅 See? The harder you try to forget, the more bears come.</div>
    <div class="part2">🔄 Now flip the words. Tap a card!</div>
    <div class="flips">
FLIPS
    </div>
    <div class="msg m-all">☀️ The past did not change. Only the words did. The bears are sleeping now.</div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Again</button></div>
  </section>
'''.replace("FLIPS", _fl),
    game_ja=dict({
        "Try to forget the white bear": "シロクマを忘れてみよう",
        "Bears in your head:": "頭の中のシロクマ：",
        "🙈 Forget the bear!": "🙈 シロクマを忘れる！",
        "😅 See? The harder you try to forget, the more bears come.": "😅 ね？忘れようとするほど、シロクマが増えます。",
        "🔄 Now flip the words. Tap a card!": "🔄 今度は言葉をひっくり返そう。カードをタップ！",
        "☀️ The past did not change. Only the words did. The bears are sleeping now.": "☀️ 過去は変わっていません。変わったのは言葉だけ。シロクマたちも、おやすみ中。",
        "↺ Again": "↺ もう一回",
    }, **_ja),
    css=r'''
  /* 「せいで」と「おかげで」を並べる */
  .vs { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 14px; }
  .vs > div { padding: 12px 10px; border-radius: 20px; text-align: center; font-weight: 900; }
  .vs .vs-a { background: #eceef6; color: #6d7290; }
  .vs .vs-b { background: #fff1d6; color: #8a4b00; }
  .vs b { display: block; font-size: 28px; margin-bottom: 4px; }

  /* 🐻‍❄️ シロクマ実験 */
  .head-box { max-width: 420px; margin: 14px auto 0; padding: 12px; border-radius: 22px; background: rgba(255,255,255,.18); }
  .head { display: flex; flex-wrap: wrap; justify-content: center; gap: 4px 8px; min-height: 96px; padding: 10px; border-radius: 48px 48px 26px 26px;
    background: #fff; align-items: center; }
  .bear { position: relative; display: none; font-size: 36px; line-height: 1; }
  .bear.on { display: inline-block; animation: g-pop .4s cubic-bezier(.2,1.4,.4,1); }
  .bear.zz { opacity: .45; transform: rotate(-12deg) translateY(4px); transition: opacity .4s ease, transform .4s ease; }
  .bear.zz::after { content: "💤"; position: absolute; right: -10px; top: -10px; font-size: 16px; }
  .bear-cnt { margin-top: 8px; font-size: 15.5px; font-weight: 900; }
  .bc-n { font-variant-numeric: tabular-nums; display: inline-block; }
  .m-b3, .m-all { display: none; }
  .game[data-b3="1"] .m-b3 { display: block; animation: g-in .35s ease-out; }
  .game[data-all="1"] .m-all { display: block; animation: g-pop .45s cubic-bezier(.2,1.4,.4,1); }
  .part2 { margin: 20px auto 0; max-width: 420px; padding-top: 14px; border-top: 2px dashed rgba(255,255,255,.45); font-size: 16.5px; font-weight: 900; }

  /* 🔄 ひっくり返しカード */
  .flips { display: grid; gap: 12px; max-width: 400px; margin: 12px auto 0; perspective: 900px; }
  .flip { display: block; width: 100%; padding: 0; border: 0; background: none; font: inherit; cursor: pointer; text-align: left;
    -webkit-tap-highlight-color: transparent; touch-action: manipulation; }
  .flip:focus-visible { outline: 4px solid #fff; outline-offset: 3px; border-radius: 20px; }
  .f-in { display: grid; transition: transform .6s cubic-bezier(.3,1.3,.5,1); transform-style: preserve-3d; }
  .f-front, .f-back { grid-area: 1 / 1; display: flex; align-items: center; gap: 8px; min-height: 64px; padding: 12px 16px; border-radius: 20px;
    font-size: 16px; font-weight: 900; line-height: 1.4; -webkit-backface-visibility: hidden; backface-visibility: hidden;
    box-shadow: 0 6px 0 rgba(0,0,0,.14), 0 12px 20px rgba(0,0,0,.10); }
  .f-front { background: #e9ecf5; color: #4d5370; justify-content: space-between; }
  .f-tap { font-size: 20px; flex: 0 0 auto; }
  .f-back { background: #fff3c4; color: #6b4300; transform: rotateY(180deg); }
  .flip.on .f-in { transform: rotateY(180deg); }
''',
    dark=r'''
  html[data-theme="dark"] .vs .vs-a { background: #2c2e3b; color: #c3c6da; }
  html[data-theme="dark"] .vs .vs-b { background: #4a3a14; color: #ffe0a3; }
  html[data-theme="dark"] .head { background: #f1edf8; }
  html[data-theme="dark"] .f-front { background: #dfe2ee; }
''',
    js=r'''
/* 🐻‍❄️ シロクマ実験 ＋ 🔄 ひっくり返しカード：JS は data-*・class・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var bears = [].slice.call(g.querySelectorAll('.bear')), bcn = g.querySelector('.bc-n'), flips = [].slice.call(g.querySelectorAll('.flip'));
  var n = 1;
  function awake() { return bears.filter(function (b) { return b.classList.contains('on') && !b.classList.contains('zz'); }).length; }
  function paint() { bcn.textContent = String(awake()); g.setAttribute('data-n', String(n)); }
  g.querySelector('.b-forget').addEventListener('click', function () {
    if (n < bears.length) { bears[n].classList.add('on'); n++; }
    else { bears.forEach(function (b) { b.classList.remove('zz'); }); var h = g.querySelector('.head'); h.classList.remove('shake'); void h.offsetWidth; h.classList.add('shake'); }
    if (n >= 3) g.setAttribute('data-b3', '1');
    paint();
  });
  flips.forEach(function (f) {
    f.addEventListener('click', function () {
      if (f.classList.contains('on')) return;
      f.classList.add('on');
      var k = 0;
      bears.forEach(function (b) { if (k < 2 && b.classList.contains('on') && !b.classList.contains('zz')) { b.classList.add('zz'); k++; } });
      paint();
      var r = f.getBoundingClientRect();
      if (flips.every(function (x) { return x.classList.contains('on'); })) {
        g.setAttribute('data-all', '1');
        if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['☀️', '🐻‍❄️', '💤', '🐧', '✨'], 22);
        if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
      } else if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['☀️', '✨'], 8);
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    n = 1;
    bears.forEach(function (b, i) { b.classList.remove('zz'); b.classList.toggle('on', i === 0); });
    flips.forEach(function (f) { f.classList.remove('on'); });
    g.setAttribute('data-b3', '0'); g.setAttribute('data-all', '0'); paint();
  });
  paint();
})();
''',
)
