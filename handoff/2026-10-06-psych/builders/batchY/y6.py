from gen import build

d = dict(
    slug="three-ways-to-see-what-you-do", seq=537,
    title=("There are 3 ways to see the things you do every day",
           "毎日やっていることの見方は、3つある"),
    label=("Three Glasses", "3つのメガネ"),
    h1_emoji="👓",
    alt="A chubby low-poly wood and paper penguin wearing real round tortoiseshell glasses next to a real wooden bento box",
    section="仕事との向き合い方（一般論）",
    message="同じことをしていても、見方は3つ（ジョブ・キャリア・コーリング）。それ自体に意味を感じる見方が、いちばん幸せで集中できる。",
    tone="素材の重さ：ふつう（とらえ方の話。本人の仕事の話にはしない。例はお弁当づくり）\n→ 見せ方：ポップに（トマト色とバジルの緑。3つのメガネをかけかえて、同じお弁当づくりを見る）",
    game_ja="👓 メガネをかけかえる：ペンギンがお弁当をつくっている。「💴 ジョブ」「🪜 キャリア」「💛 コーリング」の3つのメガネを押してかけかえると、ペンギンの頭の中の声（節約になるから…／料理の練習になる／お昼に、誰かがにっこりする！）と、「楽しさ」「集中」のメーターが変わる。3つともためすと「同じお弁当。でも、心がちがう」。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of low-poly 3D wood and paper, "
            "wearing realistic round tortoiseshell eyeglasses and proudly presenting a realistic wooden bento box with colorful rice and vegetables. "
            "Bright simple tomato red and fresh basil green background with soft depth and cheerful kitchen light. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × ローポリの木と紙 × べっこうのメガネとお弁当箱",
    mood=["lift", "think"], tags=["psychology", "mindset", "happiness"],
    pal=dict(bg="#fff8f4", muted="#7e6a60", acc="#e5482f", acc2="#2f9e5a", shadow="rgba(200,80,50,.15)",
             r1="rgba(255,120,90,.24)", r2="rgba(47,158,90,.16)", r3="rgba(255,206,84,.2)",
             h1="#4a1a10", photo="#ffe4da", big="#c23a22", bigdark="#ffb3a0",
             game="linear-gradient(160deg, #ff7a52 0%, #f0a33c 45%, #3fae6a 100%)"),
    cards=[
        dict(emoji="👓", label=("Three Views", "3つの見方"),
             s=[("It is said there are 3 ways to see the things you do every day.",
                 "毎日やっていることには、3つの見方があるそうです。")]),
        dict(emoji="🏷️", label=("Their Names", "名前"),
             s=[("\"Job\" is for money, \"career\" is for the next step, and \"calling\" is because it has meaning in itself.",
                 "「ジョブ」はお金のため、「キャリア」は次のステップのため、「コーリング」はそれ自体に意味を感じるからです。")],
             extra='<div class="lens3" aria-hidden="true"><span class="l3 l3a"><b class="e">💴</b>Job</span><span class="l3 l3b"><b class="e">🪜</b>Career</span><span class="l3 l3c"><b class="e">💛</b>Calling</span></div>'),
        dict(emoji="🎯", label=("Most Happy", "いちばん幸せ"),
             s=[("Even with the same thing, \"calling\" makes you the happiest and the most focused, it is said.",
                 "同じことをしていても、いちばん幸せで、集中できるのは「コーリング」だそうです。")]),
        dict(emoji="🍱", label=("Change Glasses", "かけかえる"), big=True,
             s=[("Just by changing your glasses, the same bento making looks a little different.",
                 "メガネをかけかえるだけで、同じお弁当づくりも、少しちがって見えます。")]),
    ],
    game_after=3,
    game_note="メガネをかけかえる（同じお弁当づくりが、3つの見方でちがって見える）",
    game_html="""  <section class="game" data-l="0" data-all="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Change your glasses</div>
    <div class="game-hint">The penguin is making a bento. Try on each pair of glasses.</div>
    <div class="kitchen">
      <div class="think">
        <span class="th0">👓 Which glasses will I wear today?</span>
        <span class="th1">"It saves money. I have to do this again tomorrow…" 💤</span>
        <span class="th2">"Good practice. I will be a better cook someday." 📈</span>
        <span class="th3">"Someone will open this at lunch and smile!" ✨</span>
      </div>
      <div class="cook"><span class="ck-p">🐧</span><span class="ck-g"><span class="g1">💴</span><span class="g2">🪜</span><span class="g3">💛</span></span><span class="ck-b">🍱</span></div>
    </div>
    <div class="lenses">
      <button type="button" class="btn ln" data-v="1" data-seen="0">💴 Job</button>
      <button type="button" class="btn ln" data-v="2" data-seen="0">🪜 Career</button>
      <button type="button" class="btn ln" data-v="3" data-seen="0">💛 Calling</button>
    </div>
    <div class="meters">
      <div class="mt"><span class="mt-l">😊 Joy</span><span class="mt-bar" aria-hidden="true"><i class="mj"></i></span></div>
      <div class="mt"><span class="mt-l">🎯 Focus</span><span class="mt-bar" aria-hidden="true"><i class="mf"></i></span></div>
    </div>
    <div class="end">🐧 The same bento. But a different heart.</div>
  </section>""",
    css="""
  /* 名前の小さな並び */
  .lens3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin-top: 14px; }
  .lens3 .l3 { display: block; padding: 10px 6px; border-radius: 18px; text-align: center; font-weight: 900; font-size: 15px; }
  .lens3 .l3 b { display: block; font-size: 26px; margin-bottom: 2px; }
  .lens3 .l3a { background: #f1eee9; color: #6b5f55; }
  .lens3 .l3b { background: #e3f1ff; color: #23508a; }
  .lens3 .l3c { background: #ffe8c2; color: #8a4a00; }

  /* 👓 メガネをかけかえる */
  .kitchen { max-width: 440px; margin: 14px auto 0; padding: 14px 12px 10px; border-radius: 24px; background: rgba(255,255,255,.2); transition: background .4s ease; }
  .game[data-l="1"] .kitchen { background: rgba(90,80,70,.28); }
  .game[data-l="3"] .kitchen { background: rgba(255,240,180,.4); }
  .think { position: relative; min-height: 64px; padding: 12px 14px; border-radius: 20px; background: #fff; color: #3a2a20; font-size: 16px; font-weight: 900; line-height: 1.45;
    display: flex; align-items: center; justify-content: center; }
  .think::after { content: ""; position: absolute; left: 50%; bottom: -10px; margin-left: -10px; border: 10px solid transparent; border-bottom: 0; border-top-color: #fff; }
  .think > span { display: none; }
  .game[data-l="0"] .th0, .game[data-l="1"] .th1, .game[data-l="2"] .th2, .game[data-l="3"] .th3 { display: inline; animation: boing .4s ease; }
  .game[data-l="1"] .think { color: #6b5f55; }
  .cook { position: relative; display: flex; align-items: flex-end; justify-content: center; gap: 4px; margin-top: 16px; height: 78px; }
  .game .ck-p { font-size: 60px; line-height: 1; transition: transform .4s ease; }
  .game .ck-b { font-size: 40px; line-height: 1; }
  .ck-g { position: absolute; left: 50%; top: 0; margin-left: -46px; width: 40px; text-align: center; }
  .ck-g > span { position: absolute; left: 0; top: 0; width: 40px; font-size: 22px; opacity: 0; transition: opacity .3s ease, transform .3s ease; transform: translateY(-10px); }
  .game[data-l="1"] .g1, .game[data-l="2"] .g2, .game[data-l="3"] .g3 { opacity: 1; transform: none; }
  .game[data-l="1"] .ck-p { transform: rotate(-8deg) translateY(4px); }
  .game[data-l="3"] .ck-p { animation: hop2 .5s ease-in-out infinite alternate; }
  @keyframes hop2 { from { transform: translateY(0); } to { transform: translateY(-10px) rotate(4deg); } }
  .lenses { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; max-width: 440px; margin: 14px auto 0; }
  .ln { padding: 8px 6px; font-size: 15px; }
  .game[data-l="1"] .ln[data-v="1"], .game[data-l="2"] .ln[data-v="2"], .game[data-l="3"] .ln[data-v="3"] { background: #3a2a20; color: #fff; box-shadow: 0 0 0 3px #fff; }
  .meters { display: grid; gap: 8px; max-width: 440px; margin: 14px auto 0; padding: 12px 14px; border-radius: 18px; background: rgba(255,255,255,.18); }
  .mt { display: grid; grid-template-columns: 7.5em 1fr; align-items: center; gap: 10px; text-align: left; }
  .mt-l { font-size: 15px; font-weight: 900; }
  .mt-bar { position: relative; display: block; height: 14px; border-radius: 999px; background: rgba(255,255,255,.3); overflow: hidden; }
  .mt-bar i { position: absolute; inset: 0 auto 0 0; width: 0; border-radius: 999px; transition: width .6s cubic-bezier(.2,1.3,.4,1); }
  .mj { background: #ffe066; }
  .mf { background: #fff; }
  .end { display: none; max-width: 440px; margin: 12px auto 0; padding: 12px 14px; border-radius: 18px; background: #fff; color: #c23a22;
    font-size: 16.5px; font-weight: 900; line-height: 1.45; }
  .game[data-all="1"] .end { display: block; animation: boing .5s ease; }
""",
    dark="""  html[data-theme="dark"] .lens3 .l3a { background: #2c2e3b; color: #d6cfc8; }
  html[data-theme="dark"] .lens3 .l3b { background: #1f2f45; color: #b9d8ff; }
  html[data-theme="dark"] .lens3 .l3c { background: #4a3a12; color: #ffd99a; }
  html[data-theme="dark"] .think { background: #2b2d3a; color: #f4ece4; }
  html[data-theme="dark"] .think::after { border-top-color: #2b2d3a; }
  html[data-theme="dark"] .game[data-l="1"] .think { color: #c9c0b8; }
  html[data-theme="dark"] .end { background: #2b2d3a; color: #ffb3a0; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var JOY = [0, 30, 60, 100], FOC = [0, 35, 60, 100], mj = g.querySelector('.mj'), mf = g.querySelector('.mf');
  var btns = [].slice.call(g.querySelectorAll('.ln'));
  btns.forEach(function (b) {
    b.addEventListener('click', function () {
      var v = +b.getAttribute('data-v');
      g.setAttribute('data-l', String(v));
      mj.style.width = JOY[v] + '%'; mf.style.width = FOC[v] + '%';
      b.setAttribute('data-seen', '1');
      if (btns.every(function (x) { return x.getAttribute('data-seen') === '1'; })) g.setAttribute('data-all', '1');
      if (v === 3 && window.pengessoPop) {
        var r = g.querySelector('.cook').getBoundingClientRect();
        window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🍱', '💛', '🐧', '✨'], 16);
      }
    });
  });
})();
""",
    ja={
        "Job": "ジョブ", "Career": "キャリア", "Calling": "コーリング",
        "Change your glasses": "メガネをかけかえよう",
        "The penguin is making a bento. Try on each pair of glasses.": "ペンギンがお弁当をつくっています。メガネを1つずつかけてみてね。",
        "👓 Which glasses will I wear today?": "👓 今日は、どのメガネをかけようかな？",
        "\"It saves money. I have to do this again tomorrow…\" 💤": "「節約になるから…。明日もまた、つくらなきゃ…」💤",
        "\"Good practice. I will be a better cook someday.\" 📈": "「いい練習になる。いつか、もっと料理がうまくなるぞ」📈",
        "\"Someone will open this at lunch and smile!\" ✨": "「お昼にこれを開けて、誰かがにっこりする！」✨",
        "💴 Job": "💴 ジョブ",
        "🪜 Career": "🪜 キャリア",
        "💛 Calling": "💛 コーリング",
        "😊 Joy": "😊 楽しさ",
        "🎯 Focus": "🎯 集中",
        "🐧 The same bento. But a different heart.": "🐧 同じお弁当。でも、心がちがう。",
    },
)
build(d)
