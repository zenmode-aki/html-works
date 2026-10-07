from gen import build

d = dict(
    slug="love-the-cat-in-front-of-you", seq=582, url="https://www.oliverburkeman.com/never",
    title=("Love the cat in front of you, not its kittens' kittens",
           "子猫の子猫じゃなくて、目の前の猫を愛そう"),
    label=("This Cat", "目の前の猫"),
    h1_emoji="🐈",
    alt="A chubby plush corduroy and felt penguin sitting on a cozy sofa and gently petting a real sleeping orange cat",
    section="⑮「人生は一生『整わない』。それでOK」（ケインズの猫の話）",
    message="「いつか」ばかり見ていると、目の前の猫を一生愛せない。今日は目の前の猫をなでよう。",
    tone="素材の重さ：ちょっと真面目（生き方の考え方）\n→ 見せ方：ポップに（ミントとピンク。ソファの猫をなでて遊べる）",
    game_ja="🐈 どの猫を愛する？：ソファに猫が1匹。「🔭 未来の猫を愛する」を押すと、雲の中に子猫 → 子猫の子猫 → ずっと先の猫…が増えていき、ソファの猫はすねて顔が 😾 → 😿 に。機嫌メーターも下がる。「💛 この猫をなでる」（または猫を直接タップ）で雲が消えて、ハートが飛び、ゴロゴロ。機嫌が100になると 😻「目の前の猫を愛せました」。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made as a plush toy of soft corduroy and felt "
            "with visible stitching, sitting on a cozy mint green sofa and gently petting a realistic sleeping orange tabby cat curled up "
            "beside it. Bright simple soft pink background with gentle depth. Realistic 3D render, studio lighting, shallow depth of field, "
            "physically based materials, photographic. Centered composition. No humans, no text, no lettering."),
    combo="ペンギン × コーデュロイとフェルトのぬいぐるみ × 本物の猫",
    mood=["think"], tags=["books", "happiness", "mindset"],
    pal=dict(bg="#f2fbf9", muted="#5f7f7a", acc="#0e9f8f", acc2="#ff6f91", shadow="rgba(20,110,100,.16)",
             r1="rgba(255,111,145,.22)", r2="rgba(46,196,182,.22)", r3="rgba(58,134,255,.14)",
             h1="#123c38", photo="#dff5f1", big="#0b8577", bigdark="#8fe8dc",
             game="linear-gradient(150deg, #2ec4b6 0%, #3a86ff 60%, #ff6f91 100%)"),
    cards=[
        dict(emoji="📜", label=("Keynes Wrote", "ケインズの話"),
             s=[("The economist Keynes wrote about a certain kind of person.", "経済学者のケインズは、こんな人のことを書いています。"),
                ("That person does not love their cat, but its kittens.", "その人は、自分の猫ではなく、その子猫を愛します。")]),
        dict(emoji="🐾", label=("Kittens' Kittens", "子猫の子猫"),
             s=[("No, really, they love the kittens of the kittens.", "いや、本当はその子猫の、さらに子猫を愛しているのです。")]),
        dict(emoji="🔭", label=("Always Someday", "いつも「いつか」"),
             s=[("They always look at \"someday,\" so they never love the cat in front of them.",
                 "いつも「いつか」ばかり見ていて、目の前の猫は一生愛さないのです。")]),
        dict(emoji="📘", label=("Habit Books", "習慣の本"),
             s=[("Habit books that promise \"easy forever\" may be the same trap.",
                 "「一度身につけば一生ラク」と約束する習慣の本も、同じわなかもしれません。")]),
        dict(emoji="💛", label=("This Cat", "この猫"), big=True,
             s=[("Today, why not pet the cat in front of you?", "今日は、目の前の猫をなでてみませんか。")]),
    ],
    game_after=3,
    game_note="どの猫を愛する？（未来の猫 vs ソファの猫）",
    game_html="""  <section class="game" data-m="idle" data-f="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Which cat do you love?</div>
    <div class="game-hint">A cat is on your sofa. Tap a button and watch its face.</div>
    <div class="scene">
      <div class="room-l">
        <button class="cat-btn" type="button" aria-label="Pet this cat"><span class="face">😺</span></button>
        <div class="purr">purr…</div>
        <div class="sofa" aria-hidden="true"><i class="arm a1"></i><i class="seat"></i><i class="arm a2"></i></div>
      </div>
      <div class="arrow" aria-hidden="true"><span class="arr">➡️</span></div>
      <div class="cloud">
        <div class="cloud-t">Someday…</div>
        <div class="kits"><span class="k k1">🐱</span><span class="k k1">🐱</span><span class="k k2">🐱</span><span class="k k2">🐱</span><span class="k k3">🐱</span><span class="k k3">🐱</span></div>
      </div>
    </div>
    <div class="meter-row"><span class="ml">The cat's mood</span><div class="meter"><i></i></div></div>
    <div class="msg">
      <div class="m m-idle">This is your cat. It is here, right now.</div>
      <div class="m m-f1">You dream about its kittens…</div>
      <div class="m m-f2">Now its kittens' kittens… The cat on the sofa is sulking.</div>
      <div class="m m-f3">Kittens forever… The real cat waits alone. 😿</div>
      <div class="m m-pet">Purr… The cat is happy you are here. 💗</div>
      <div class="m m-love">😻 Purr purr! You loved the cat in front of you.</div>
    </div>
    <div class="btns">
      <button class="btn b-fut" type="button">🔭 Love the future cats</button>
      <button class="btn b-pet" type="button">💛 Pet this cat</button>
      <button class="btn ghost b-again" type="button">↺ Try again</button>
    </div>
  </section>""",
    css=r"""
  /* 🐈 どの猫を愛する？ */
  .scene { display: grid; grid-template-columns: 1.15fr auto 1fr; align-items: end; gap: 6px; margin: 16px auto 0; max-width: 430px;
    padding: 14px 10px 12px; border-radius: 24px; background: rgba(255,255,255,.16); }
  .room-l { position: relative; display: flex; flex-direction: column; align-items: center; }
  .cat-btn { position: relative; z-index: 2; width: 92px; height: 84px; margin-bottom: -18px; border: 0; background: none; cursor: pointer; padding: 0;
    -webkit-tap-highlight-color: transparent; touch-action: manipulation; }
  .face { display: inline-block; font-size: 64px; line-height: 1; transition: transform .3s cubic-bezier(.2,1.5,.4,1); }
  .game[data-m="pet"] .face, .game[data-m="love"] .face { transform: scale(1.12) rotate(-6deg); }
  .game[data-f="2"] .face, .game[data-f="3"] .face { transform: rotate(14deg) translateX(4px); }
  .sofa { position: relative; width: 132px; height: 52px; }
  .sofa .seat { position: absolute; left: 14px; right: 14px; bottom: 0; height: 40px; border-radius: 14px; background: #ffd1dc; box-shadow: inset 0 -8px 0 rgba(0,0,0,.08); }
  .sofa .arm { position: absolute; bottom: 0; width: 24px; height: 52px; border-radius: 12px; background: #ff9db5; }
  .sofa .a1 { left: 0; } .sofa .a2 { right: 0; }
  .purr { position: absolute; top: -6px; right: -6px; padding: 4px 9px; border-radius: 999px; background: #fff; color: #d6336c; font-size: 13px; font-weight: 900;
    opacity: 0; transform: translateY(6px); transition: opacity .25s ease, transform .25s ease; }
  .game.purring .purr { opacity: 1; transform: none; }
  .arrow { align-self: center; font-size: 22px; opacity: 0; transition: opacity .3s ease; }
  .game:not([data-f="0"]) .arrow { opacity: 1; }
  .cloud { align-self: center; min-height: 92px; padding: 8px 6px; border-radius: 28px; background: rgba(255,255,255,.88); color: #36507a;
    opacity: .35; transition: opacity .3s ease, transform .3s ease; }
  .game:not([data-f="0"]) .cloud { opacity: 1; }
  .cloud.wob { animation: shake .4s ease; }
  .cloud-t { font-size: 13px; font-weight: 900; }
  .kits { display: flex; flex-wrap: wrap; justify-content: center; gap: 2px; margin-top: 4px; }
  .game .k { display: inline-block; line-height: 1; transform: scale(0); transition: transform .35s cubic-bezier(.2,1.5,.4,1); }
  .k1 { font-size: 28px; } .k2 { font-size: 21px; } .k3 { font-size: 15px; }
  .game[data-f="1"] .k1, .game[data-f="2"] .k1, .game[data-f="2"] .k2, .game[data-f="3"] .k { transform: scale(1); }
  .meter-row { display: flex; align-items: center; gap: 10px; max-width: 400px; margin: 14px auto 0; font-size: 14px; font-weight: 900; }
  .meter { position: relative; flex: 1; height: 16px; border-radius: 999px; background: rgba(255,255,255,.28); overflow: hidden; }
  .meter i { position: absolute; inset: 0 auto 0 0; width: 50%; border-radius: 999px; background: #ffe066; transition: width .45s cubic-bezier(.2,1.2,.4,1); }
  .msg { margin-top: 12px; min-height: 52px; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .msg .m { display: none; }
  .game[data-m="idle"] .m-idle, .game[data-m="f1"] .m-f1, .game[data-m="f2"] .m-f2, .game[data-m="f3"] .m-f3,
  .game[data-m="pet"] .m-pet, .game[data-m="love"] .m-love { display: block; }
  .btns { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-top: 12px; }
  .game .b-again { display: none; }
  .game[data-m="love"] .b-fut, .game[data-m="love"] .b-pet { display: none; }
  .game[data-m="love"] .b-again { display: inline-flex; }
  .b-pet { background: #ffe066; color: #4a3500; }
  @media (max-width: 380px) { .scene { grid-template-columns: 1fr; justify-items: center; } .arrow { transform: rotate(90deg); } .cloud { width: 80%; } }
""",
    dark="""  html[data-theme="dark"] .game .b-pet { background: #ffe066; color: #4a3500; }
  html[data-theme="dark"] .cloud { background: rgba(240,244,255,.9); }""",
    js=r"""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var face = g.querySelector('.face'), bar = g.querySelector('.meter i'), cloud = g.querySelector('.cloud'), cat = g.querySelector('.cat-btn');
  var mood = 50, fut = 0, pt = 0;
  function draw() {
    bar.style.width = mood + '%';
    face.textContent = mood >= 100 ? '😻' : mood >= 70 ? '😸' : mood >= 40 ? '😺' : mood >= 20 ? '😾' : '😿';
    g.setAttribute('data-f', String(fut));
  }
  function future() {
    if (g.getAttribute('data-m') === 'love') return;
    fut = Math.min(3, fut + 1); mood = Math.max(0, mood - 20);
    g.setAttribute('data-m', 'f' + fut); g.classList.remove('purring');
    cloud.classList.remove('wob'); void cloud.offsetWidth; cloud.classList.add('wob');
    draw();
  }
  function pet() {
    if (g.getAttribute('data-m') === 'love') return;
    fut = 0; mood = Math.min(100, mood + 17);
    g.classList.add('purring'); clearTimeout(pt); pt = setTimeout(function () { g.classList.remove('purring'); }, 1100);
    var r = cat.getBoundingClientRect();
    if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 3, ['💗', '💛', '🐾'], mood >= 100 ? 20 : 7);
    g.setAttribute('data-m', mood >= 100 ? 'love' : 'pet');
    if (mood >= 100 && navigator.vibrate) { try { navigator.vibrate(25); } catch (e) {} }
    draw();
  }
  g.querySelector('.b-fut').addEventListener('click', future);
  g.querySelector('.b-pet').addEventListener('click', pet);
  cat.addEventListener('click', pet);
  g.querySelector('.b-again').addEventListener('click', function () {
    mood = 50; fut = 0; g.classList.remove('purring'); g.setAttribute('data-m', 'idle'); draw();
  });
})();
""",
    ja={
        "Which cat do you love?": "どの猫を愛する？",
        "A cat is on your sofa. Tap a button and watch its face.": "ソファに猫がいます。ボタンを押して、猫の顔を見てね。",
        "Pet this cat": "この猫をなでる",
        "purr…": "ゴロゴロ…",
        "Someday…": "いつか…",
        "The cat's mood": "猫の機嫌",
        "This is your cat. It is here, right now.": "これがあなたの猫。今ここにいます。",
        "You dream about its kittens…": "その子猫のことを夢見ています…",
        "Now its kittens' kittens… The cat on the sofa is sulking.": "今度は子猫の子猫… ソファの猫がすねています。",
        "Kittens forever… The real cat waits alone. 😿": "ずっと先の猫ばかり… 本物の猫はひとりで待っています 😿",
        "Purr… The cat is happy you are here. 💗": "ゴロゴロ… あなたがここにいて、猫はうれしそう 💗",
        "😻 Purr purr! You loved the cat in front of you.": "😻 ゴロゴロゴロ！目の前の猫を愛せました。",
        "🔭 Love the future cats": "🔭 未来の猫を愛する",
        "💛 Pet this cat": "💛 この猫をなでる",
        "↺ Try again": "↺ もう一回",
    },
)

if __name__ == "__main__":
    build(d)
