from gen import build

d = dict(
    slug="three-minutes-of-morning-thanks", seq=521,
    title=("Spend 3 minutes every morning writing your thanks in detail",
           "毎朝3分、感謝したことを具体的に書く"),
    label=("Morning Thanks", "朝の感謝"),
    h1_emoji="🌅",
    alt="A chubby boucle wool penguin writing in a real open notebook with a pencil beside a warm cup of tea at sunrise",
    section="感謝を習慣に",
    message="感謝は、毎朝決まった時間に3分、具体的に書く。具体的なほど、良かったことがはっきり見える。",
    tone="素材の重さ：ふつう（習慣のコツ）\n→ 見せ方：ポップに（朝焼けのオレンジと青。ぼんやりした感謝を、具体的に書きかえると日がのぼる）",
    game_ja="🌅 朝の3分ノート：ノートに、ぼんやりした感謝が3行（家族に感謝／ごはんに感謝／友達に感謝）。1行ずつ「🔍 具体的にする」を押すと、「寒い朝に、お茶をいれてもらった 🍵」のように書きかわって、しあわせメーターがぐんと上がる（ぼんやりは+1、具体的は+3）。1行ごとに時計が1分進み、朝日が少しずつのぼる。3分で「おはよう！」。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of cozy boucle wool, "
            "sitting at a small table and writing in a realistic open paper notebook with a yellow pencil, a steaming cup of tea beside it. "
            "Bright simple sunrise peach and soft morning blue background with soft depth and a gentle warm window light. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × ブークレウール × ノートとお茶",
    mood=["lift", "learn"], tags=["psychology", "happiness", "tips"],
    pal=dict(bg="#fff8f1", muted="#8a7466", acc="#ec5a2c", acc2="#3a6bdc", shadow="rgba(170,90,50,.16)",
             r1="rgba(255,194,61,.32)", r2="rgba(236,90,44,.16)", r3="rgba(58,107,220,.14)",
             h1="#4a2210", photo="#ffe8d9", big="#d24a1c", bigdark="#ffb899",
             game="linear-gradient(170deg, #3a4bbf 0%, #9c5bd6 35%, #ff7a59 70%, #ffc94d 100%)"),
    cards=[
        dict(emoji="⏰", label=("3 Minutes", "3分"),
             s=[("It is said the trick to keep a thanks habit is to write for just 3 minutes at the same time every morning.",
                 "感謝の習慣を続けるコツは、毎朝決まった時間に、3分だけ書くことだそうです。")]),
        dict(emoji="🔍", label=("In Detail", "具体的に"),
             s=[("The point is to write in detail.",
                 "ポイントは、具体的に書くことです。")]),
        dict(emoji="🍵", label=("Much Clearer", "はっきり見える"),
             s=[("\"Someone made me tea on a cold morning\" shows the good thing more clearly than \"thanks to my family.\"",
                 "「寒い朝に、お茶をいれてもらった」のほうが、「家族に感謝」より、良かったことがはっきり見えます。")]),
        dict(emoji="🌅", label=("Lucky Start", "いい1日の始まり"), big=True,
             s=[("If you write in the morning, you can start the day feeling lucky.",
                 "朝に書くと、その日を「恵まれているな」という気持ちで始められます。")]),
    ],
    game_after=3,
    game_note="朝の3分ノート（ぼんやりした感謝を具体的にすると、日がのぼる）",
    game_html="""  <section class="game" data-m="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">The 3-minute morning notebook</div>
    <div class="game-hint">Tap each line to make it specific. Watch the sun.</div>
    <div class="dawn">
      <div class="sun" aria-hidden="true"></div>
      <div class="hills" aria-hidden="true"></div>
      <div class="clock"><span class="ck-e">⏰</span> <span class="mm">0</span><span class="ss">:00</span> <span class="ck-of">/ 3:00</span></div>
    </div>
    <div class="note">
      <button type="button" class="ln" data-v="0">
        <span class="lv">Thanks to my family.</span>
        <span class="ls">Someone made me tea on a cold morning. 🍵</span>
        <span class="lb">🔍 Make it specific</span>
      </button>
      <button type="button" class="ln" data-v="0">
        <span class="lv">Thanks for the food.</span>
        <span class="ls">My rice ball had a big piece of salmon inside. 🍙</span>
        <span class="lb">🔍 Make it specific</span>
      </button>
      <button type="button" class="ln" data-v="0">
        <span class="lv">Thanks to my friend.</span>
        <span class="ls">My friend sent me a funny cat video last night. 🐈</span>
        <span class="lb">🔍 Make it specific</span>
      </button>
    </div>
    <div class="happy">
      <div class="hp-head"><span class="hp-l">😊 Happy meter</span> <span class="hp-n">3</span></div>
      <div class="hp-bar" aria-hidden="true"><i></i></div>
      <div class="hp-k"><span class="hk-v">Vague: +1</span> <span class="hk-s">Specific: +3</span></div>
    </div>
    <div class="end">☀️ 3 minutes. Good morning! The day starts feeling lucky.</div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Start over</button></div>
  </section>""",
    css="""
  /* 🌅 朝の3分ノート */
  .dawn { position: relative; height: 130px; max-width: 420px; margin: 16px auto 0; border-radius: 22px; overflow: hidden;
    background: linear-gradient(#5a6fd6, #c28bd8 60%, #ffb38a); transition: background .6s ease; }
  .game[data-m="2"] .dawn, .game[data-m="3"] .dawn { background: linear-gradient(#7fc4ff, #ffd1a8 60%, #ffe39a); }
  .sun { position: absolute; left: 50%; width: 74px; height: 74px; margin-left: -37px; border-radius: 50%; background: #ffd23f;
    box-shadow: 0 0 30px 10px rgba(255,210,63,.6); bottom: -60px; transition: bottom .9s cubic-bezier(.3,1.3,.5,1); }
  .game[data-m="1"] .sun { bottom: -26px; } .game[data-m="2"] .sun { bottom: 10px; } .game[data-m="3"] .sun { bottom: 42px; }
  .hills { position: absolute; left: -10%; right: -10%; bottom: -40px; height: 80px; border-radius: 50% 50% 0 0; background: #3f8f5a; }
  .clock { position: absolute; left: 10px; top: 10px; padding: 4px 10px; border-radius: 999px; background: rgba(255,255,255,.9); color: #3a2a1a;
    font-size: 15px; font-weight: 900; }
  .ck-of { opacity: .6; font-size: 12.5px; }
  .note { max-width: 420px; margin: 12px auto 0; padding: 10px; border-radius: 20px; background: #fffdf4; display: grid; gap: 8px;
    box-shadow: 0 8px 0 rgba(0,0,0,.14); }
  .ln { display: grid; gap: 4px; justify-items: start; text-align: left; width: 100%; min-height: 64px; padding: 10px 12px; border: 0; border-radius: 14px;
    border-bottom: 2px solid #f0dcc0; background: transparent; color: #3a2a1a; font: inherit; cursor: pointer;
    -webkit-tap-highlight-color: transparent; touch-action: manipulation; }
  .ln:focus-visible { outline: 3px solid #ec5a2c; outline-offset: 2px; }
  .lv { font-size: 16.5px; font-weight: 900; color: #9a8a7a; }
  .ls { display: none; font-size: 16.5px; font-weight: 900; color: #3a2a1a; }
  .lb { display: inline-block; padding: 5px 12px; border-radius: 999px; background: #ffe7d6; color: #a03a12; font-size: 13.5px; font-weight: 900; }
  .ln[data-v="1"] { background: #fff1c2; cursor: default; animation: boing .45s ease; }
  .ln[data-v="1"] .lv, .ln[data-v="1"] .lb { display: none; }
  .ln[data-v="1"] .ls { display: block; }
  .happy { max-width: 420px; margin: 14px auto 0; padding: 12px 14px; border-radius: 20px; background: rgba(255,255,255,.18); }
  .hp-head { display: flex; justify-content: space-between; align-items: center; font-size: 15px; font-weight: 900; }
  .hp-n { display: inline-block; min-width: 2em; padding: 1px 8px; border-radius: 999px; background: rgba(255,255,255,.3); }
  .hp-bar { position: relative; height: 16px; margin-top: 8px; border-radius: 999px; background: rgba(255,255,255,.3); overflow: hidden; }
  .hp-bar i { position: absolute; inset: 0 auto 0 0; width: 33%; border-radius: 999px; background: #ffe066; transition: width .5s cubic-bezier(.2,1.3,.4,1); }
  .hp-k { display: flex; justify-content: space-between; gap: 10px; margin-top: 5px; font-size: 12.5px; font-weight: 900; opacity: .9; }
  .end { display: none; margin: 14px auto 0; max-width: 420px; padding: 12px 14px; border-radius: 18px; background: #fff; color: #9a3410; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .game[data-m="3"] .end { display: block; animation: boing .5s ease; }
  .ctrl { margin-top: 12px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
""",
    dark="""  html[data-theme="dark"] .clock { background: rgba(30,32,44,.9); color: #ffe3c8; }
  html[data-theme="dark"] .note { background: #2b2a30; }
  html[data-theme="dark"] .ln { color: #f4ece4; border-bottom-color: #4a3d30; }
  html[data-theme="dark"] .lv { color: #b8a898; }
  html[data-theme="dark"] .ls { color: #fff2e0; }
  html[data-theme="dark"] .lb { background: #4a2418; color: #ffd0be; }
  html[data-theme="dark"] .ln[data-v="1"] { background: #4a3c12; }
  html[data-theme="dark"] .end { background: #2b2d3a; color: #ffc9a8; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var m = 0, happy = 3, bar = g.querySelector('.hp-bar i');
  function paint() {
    g.setAttribute('data-m', String(m));
    g.querySelector('.mm').textContent = m;
    g.querySelector('.hp-n').textContent = happy;
    bar.style.width = Math.round(happy / 9 * 100) + '%';
  }
  [].forEach.call(g.querySelectorAll('.ln'), function (b) {
    b.addEventListener('click', function () {
      if (b.getAttribute('data-v') === '1') return;
      b.setAttribute('data-v', '1');
      m++; happy += 2; paint();   /* ぼんやり +1 → 具体的 +3 なので、1行につき +2 */
      if (window.pengessoPop) {
        var r = b.getBoundingClientRect();
        window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, m === 3 ? ['☀️', '🌅', '🐧', '✨', '🍵'] : ['✨', '😊'], m === 3 ? 20 : 8);
      }
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    m = 0; happy = 3;
    [].forEach.call(g.querySelectorAll('.ln'), function (b) { b.setAttribute('data-v', '0'); });
    paint();
  });
})();
""",
    ja={
        "The 3-minute morning notebook": "朝の3分ノート",
        "Tap each line to make it specific. Watch the sun.": "1行ずつ押して、具体的にしてみてね。お日さまを見ていて。",
        ":00": ":00",
        "/ 3:00": "/ 3:00",
        "Thanks to my family.": "家族に感謝。",
        "Someone made me tea on a cold morning. 🍵": "寒い朝に、お茶をいれてもらった。🍵",
        "Thanks for the food.": "ごはんに感謝。",
        "My rice ball had a big piece of salmon inside. 🍙": "おにぎりに、鮭が大きく入っていた。🍙",
        "Thanks to my friend.": "友達に感謝。",
        "My friend sent me a funny cat video last night. 🐈": "ゆうべ、友達がおもしろいネコの動画を送ってくれた。🐈",
        "🔍 Make it specific": "🔍 具体的にする",
        "😊 Happy meter": "😊 しあわせメーター",
        "Vague: +1": "ぼんやり：+1",
        "Specific: +3": "具体的：+3",
        "☀️ 3 minutes. Good morning! The day starts feeling lucky.": "☀️ 3分たちました。おはよう！「恵まれているな」で1日が始まります。",
        "↺ Start over": "↺ 最初から",
    },
)
build(d)
