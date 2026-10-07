from gen import build

MOT = [
    ("💰", "Start each day at zero, not in debt.", "毎日、借金ゼロからスタート。"),
    ("🔢", "You can only do one thing at a time.", "人間は、1つのことしかできない。"),
    ("🚢", "Fix the ship at sea, one plank at a time.", "航海中の船は、海の上で板を1枚ずつ直す。"),
    ("😬", "A little awkward means it is working.", "ちょっと気まずいのは、うまくいっているサイン。"),
    ("⏹️", "Have the courage to stop.", "止める勇気を持つ。"),
    ("🌊", "Treat it like a river. Scoop, do not empty.", "川として扱う。空にしないで、すくうだけ。"),
    ("🌌", "Tiny in the universe, so you are free.", "宇宙から見ればちっぽけ。だから自由。"),
    ("👣", "Moving is easier than thinking.", "考えるより、動くほうがラク。"),
]
ONE = [
    ("📩", "Reply to 1 message", "メッセージを1つ返す"),
    ("🧺", "Do the laundry", "洗濯をする"),
    ("📖", "Read 5 pages", "5ページ読む"),
    ("👟", "Walk for 10 minutes", "10分歩く"),
    ("🧹", "Clean 1 shelf", "棚を1段だけ片付ける"),
    ("😴", "Take a nap", "昼寝する"),
]

cards_html = "\n".join(
    f'      <button class="mc" type="button"><span class="front"><span class="mf-e">{e}</span><span class="mf-n">#{i + 1}</span></span><span class="back">{e} {en}</span></button>'
    for i, (e, en, ja) in enumerate(MOT))
chips_html = "\n".join(
    f'      <button class="chip" type="button" data-p="{i}">{e} {en}</button>' for i, (e, en, ja) in enumerate(ONE))
big_html = "\n".join(f'        <span class="bo bo{i}">{e} {en}</span>' for i, (e, en, ja) in enumerate(ONE))
sel_css = ", ".join(f'.game[data-p="{i}"] .bo{i}' for i in range(len(ONE)))

ja = {
    "Your 8 mottos": "8つの合言葉",
    "Tap each card to open it.": "カードをタップして、1枚ずつ開いてね。",
    "📖 Mottos opened:": "📖 開いた合言葉：",
    "✏️ Today's one thing": "✏️ 今日の1つ",
    "You cannot do all of it. So pick just one for today.": "全部は無理。だから今日は、1つだけ選ぼう。",
    "✏️ Today, I will just do this:": "✏️ 今日は、これだけやる：",
    "✅ Done!": "✅ できた！",
    "🎉 That is enough for today. Well done! 🐧": "🎉 今日はそれで十分。おつかれさま！🐧",
    "↺ Choose again": "↺ 選びなおす",
    "↺ Start over": "↺ 最初から",
}
for e, en, j in MOT:
    ja[f"{e} {en}"] = f"{e} {j}"
for e, en, j in ONE:
    ja[f"{e} {en}"] = f"{e} {j}"

d = dict(
    slug="just-one-thing-today", seq=590, url="https://www.oliverburkeman.com/",
    title=("You cannot do everything, so just do one thing today",
           "全部は無理。だから安心して、今日は目の前の1つをやろう"),
    label=("One Thing", "今日の1つ"),
    h1_emoji="✅",
    alt="A chubby soft felted wool penguin holding a real yellow pencil next to one blank index card with a single check mark",
    section="まとめ「全部は無理。だから安心して、目の前の1つをやろう」（シリーズの最後）",
    message="全部は無理。だから安心して、今日は目の前の1つをやろう。",
    tone="素材の重さ：ふつう（シリーズのまとめ）\n→ 見せ方：にぎやかなポップ（オレンジ・ピンク・紫・ミントの虹色。合言葉カードをめくって、最後に今日の1つを選ぶ）",
    game_ja="🃏 8つの合言葉 → 今日の1つ：8枚のカード（💰借金ゼロスタート／🔢1つしかできない／🚢海の上で船を直す／😬気まずいのはサイン／⏹️止める勇気／🌊川として扱う／🌌宇宙から見ればちっぽけ／👣考えるより動く）をタップしてくるっとめくる。8枚全部めくると「✏️ 今日の1つ」が出てきて、「メッセージを1つ返す」「洗濯」「5ページ読む」「10分歩く」「棚を1段片付ける」「昼寝」から1つだけ選ぶ。大きなカードになって、「✅ できた！」で線が引かれて「今日はそれで十分」。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of soft felted wool with a fuzzy matte "
            "texture, holding a realistic yellow wooden pencil next to one blank white index card that has a single green check mark on it. "
            "Bright simple rainbow pastel background of orange, pink and mint with soft depth. Realistic 3D render, studio lighting, shallow "
            "depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering."),
    combo="ペンギン × 羊毛フェルト × 鉛筆と1枚の単語カード",
    mood=["lift"], tags=["books", "mindset", "happiness"],
    pal=dict(bg="#fffaf3", muted="#7a6f86", acc="#6a5cff", acc2="#ff6f91", shadow="rgba(90,70,140,.16)",
             r1="rgba(255,154,61,.26)", r2="rgba(106,92,255,.18)", r3="rgba(46,196,182,.18)",
             h1="#2c2547", photo="#f1ecff", big="#4b3fd1", bigdark="#b9b0ff",
             game="linear-gradient(150deg, #ff9a3d 0%, #ff6f91 35%, #6a5cff 72%, #2ec4b6 100%)"),
    cards=[
        dict(emoji="🎛️", label=("The Root", "しんどさの根っこ"),
             s=[("Most of the hard feelings come from wanting to control life perfectly.", "しんどさの原因は、だいたい「人生を完璧にコントロールしたい」という気持ちです。")]),
        dict(emoji="🪶", label=("Let It Go", "手放す"),
             s=[("When you let it go, strangely, you can start to move.", "それを手放すと、不思議と動けるようになります。")]),
        dict(emoji="🐧", label=("My 8 Mottos", "8つの合言葉"),
             s=[("I put what I learned from Burkeman's blog into 8 mottos.", "バークマンさんのブログから学んだことを、8つの合言葉にまとめました。")]),
        dict(emoji="✅", label=("Just One", "1つだけ"), big=True,
             s=[("You cannot do everything.", "全部は無理です。"),
                ("So relax, and do just one thing in front of you today.", "だから安心して、今日は目の前の1つをやりましょう。")]),
    ],
    game_after=3,
    game_note="8つの合言葉 → 今日の1つ",
    game_html=f"""  <section class="game" data-s="cards" data-p="" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Your 8 mottos</div>
    <div class="game-hint">Tap each card to open it.</div>
    <div class="deck">
{cards_html}
    </div>
    <div class="cnt"><span class="cl">📖 Mottos opened:</span> <b class="mn">0</b><span class="of">/8</span></div>
    <div class="today">
      <div class="td-h">✏️ Today's one thing</div>
      <div class="td-hint">You cannot do all of it. So pick just one for today.</div>
      <div class="chips">
{chips_html}
      </div>
      <div class="one">
        <div class="one-h">✏️ Today, I will just do this:</div>
        <div class="one-t">
{big_html}
        </div>
        <button class="btn b-done" type="button">✅ Done!</button>
        <div class="one-ok">🎉 That is enough for today. Well done! 🐧</div>
      </div>
      <div class="btns">
        <button class="btn ghost b-re" type="button">↺ Choose again</button>
        <button class="btn ghost b-over" type="button">↺ Start over</button>
      </div>
    </div>
  </section>""",
    css=r"""
  /* 🃏 8つの合言葉 → 今日の1つ */
  .deck { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 440px; margin: 16px auto 0; }
  .mc { min-height: 92px; padding: 10px 10px; border: 0; border-radius: 20px; cursor: pointer; font: inherit; color: #2c2547;
    background: rgba(255,255,255,.22); box-shadow: inset 0 0 0 3px rgba(255,255,255,.7), 0 5px 0 rgba(0,0,0,.14);
    display: flex; align-items: center; justify-content: center; touch-action: manipulation; -webkit-tap-highlight-color: transparent; }
  .mc:active { transform: translateY(3px); }
  .mc .front { display: flex; flex-direction: column; align-items: center; gap: 2px; color: #fff; }
  .mf-e { font-size: 34px; line-height: 1; }
  .mf-n { font-size: 13px; font-weight: 900; opacity: .9; }
  .game .mc .back { display: none; font-size: 15px; font-weight: 900; line-height: 1.35; }
  .game .mc.open { background: #fff; box-shadow: 0 5px 0 rgba(0,0,0,.14); }
  .game .mc.open .front { display: none; }
  .game .mc.open .back { display: block; }
  .mc.turn { animation: turn .36s ease-in-out; }
  @keyframes turn { 0% { transform: scaleX(1); } 50% { transform: scaleX(0); } 100% { transform: scaleX(1); } }
  .cnt { margin-top: 12px; font-size: 16px; font-weight: 900; }
  .cnt b { display: inline-block; min-width: 1.4em; padding: 1px 8px; border-radius: 999px; background: #fff; color: #6a5cff; }
  .game .today { display: none; }
  .game:not([data-s="cards"]) .today { display: block; animation: boing .5s ease; }
  .today { margin: 18px auto 0; max-width: 440px; padding: 16px 12px; border-radius: 24px; background: rgba(255,255,255,.18); }
  .td-h { font-size: 21px; font-weight: 900; }
  .td-hint { margin-top: 4px; font-size: 15px; font-weight: 800; line-height: 1.45; }
  .chips { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: 12px; }
  .chip { min-height: 52px; padding: 8px 10px; border: 0; border-radius: 16px; cursor: pointer; font: inherit; font-size: 15px; font-weight: 900; line-height: 1.3;
    color: #2c2547; background: #fff; box-shadow: 0 4px 0 rgba(0,0,0,.14); touch-action: manipulation; -webkit-tap-highlight-color: transparent; }
  .chip:active { transform: translateY(3px); }
  .game[data-s="one"] .chips, .game[data-s="done"] .chips, .game[data-s="one"] .td-hint, .game[data-s="done"] .td-hint { display: none; }
  .game .one { display: none; }
  .game[data-s="one"] .one, .game[data-s="done"] .one { display: block; }
  .one { margin-top: 12px; padding: 18px 14px; border-radius: 22px; background: #fffbe8; color: #2c2547; box-shadow: 0 8px 0 rgba(0,0,0,.12); animation: boing .5s ease; }
  .one-h { font-size: 14px; font-weight: 900; color: #6a5cff; }
  .one-t { margin: 8px 0 12px; font-size: clamp(24px, 6.4vw, 32px); font-weight: 900; line-height: 1.3; }
  .game .bo { display: none; }
  """ + sel_css + r""" { display: inline; }
  .game[data-s="done"] .one-t { text-decoration: line-through; text-decoration-thickness: 4px; text-decoration-color: #ff6f91; }
  .b-done { background: #6a5cff; color: #fff; min-width: 180px; }
  .game[data-s="done"] .b-done { display: none; }
  .one-ok { display: none; font-size: 17px; font-weight: 900; color: #2c7a50; }
  .game[data-s="done"] .one-ok { display: block; }
  .btns { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-top: 12px; }
  .game .b-re { display: none; }
  .game[data-s="one"] .b-re, .game[data-s="done"] .b-re { display: inline-flex; }
""",
    dark="""  html[data-theme="dark"] .game .mc.open { background: #f7f4ff; color: #2c2547; }
  html[data-theme="dark"] .game .chip { background: #f7f4ff; color: #2c2547; }
  html[data-theme="dark"] .one { background: #fffbe8; color: #2c2547; }
  html[data-theme="dark"] .game .b-done { background: #6a5cff; color: #fff; }""",
    js=r"""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var cards = [].slice.call(g.querySelectorAll('.mc')), mn = g.querySelector('.mn'), KEY = 'pengesso-just-one-thing-today-pick';
  function opened() { return g.querySelectorAll('.mc.open').length; }
  cards.forEach(function (c) {
    c.addEventListener('click', function () {
      if (c.classList.contains('turn')) return;
      c.classList.add('turn');
      /* 横向き（幅0）のときに表と裏を入れかえる。backface は使わない（iPhone で裏の字が鏡文字で透けるため） */
      setTimeout(function () {
        c.classList.toggle('open');
        var k = opened(); mn.textContent = k;
        if (k === 8 && g.getAttribute('data-s') === 'cards') {
          g.setAttribute('data-s', 'pick');
          var r = g.getBoundingClientRect();
          if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, Math.max(80, r.top + 120), ['💰', '🔢', '🚢', '😬', '⏹️', '🌊', '🌌', '👣'], 16);
        }
      }, 180);
      setTimeout(function () { c.classList.remove('turn'); }, 380);
    });
  });
  [].slice.call(g.querySelectorAll('.chip')).forEach(function (ch) {
    ch.addEventListener('click', function () {
      var p = ch.getAttribute('data-p');
      g.setAttribute('data-p', p); g.setAttribute('data-s', 'one');
      try { localStorage.setItem(KEY, p); } catch (e) {}
    });
  });
  g.querySelector('.b-done').addEventListener('click', function (e) {
    g.setAttribute('data-s', 'done');
    var r = g.querySelector('.one').getBoundingClientRect();
    if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['✅', '🐧', '🎉', '✨'], 20);
    if (navigator.vibrate) { try { navigator.vibrate(30); } catch (er) {} }
  });
  g.querySelector('.b-re').addEventListener('click', function () { g.setAttribute('data-p', ''); g.setAttribute('data-s', 'pick'); });
  g.querySelector('.b-over').addEventListener('click', function () {
    cards.forEach(function (c) { c.classList.remove('open', 'turn'); }); mn.textContent = '0';
    g.setAttribute('data-p', ''); g.setAttribute('data-s', 'cards');
  });
})();
""",
    ja=ja,
)

if __name__ == "__main__":
    build(d)
