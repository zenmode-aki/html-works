import html as _h
AG = ("😶 Hmm, that only agrees with the gloomy thought.", "😶 うーん、それは暗い考えに賛成しているだけ。")
RN = ("💨 That is running away, not arguing back.", "💨 それは反論じゃなくて、逃げているだけ。")
OK = ("🎯 Great argument! You talked like a kind friend.", "🎯 いい反論！やさしい友達みたいに言えたね。")
CASES = [
    ("At the station, I bumped into someone's shoulder, and they clicked their tongue.", "駅で肩がぶつかって、舌打ちされた。",
     '"I am always so clumsy. I am no good."', "「私はいつもドンくさい。ダメな人間だ」",
     [("agree", "That's right. You are hopeless.", "そうだよ。もうダメだね。"),
      ("ok", "Always? Bumping shoulders happens to everyone!", "いつも？肩がぶつかるなんて、誰にでもあるよ！"),
      ("run", "Never go to the station again.", "もう二度と駅に行かない。")]),
    ("I made a big mistake when I spoke English.", "英語で話したとき、大きなまちがいをした。",
     '"I am terrible. Everyone thinks I am stupid."', "「私はひどい。みんな私をバカだと思っている」",
     [("ok", "Everyone? You are learning, so mistakes are normal!", "みんな？勉強中なんだから、まちがえるのは普通だよ！"),
      ("agree", "Yes, English is not for you.", "そうだね、英語は向いてないよ。"),
      ("run", "Never speak English again.", "もう英語は話さない。")]),
    ("I forgot my umbrella and got wet.", "傘を忘れて、ぬれてしまった。",
     '"I ruin everything. Today is over."', "「私は全部ダメにする。今日はもう終わりだ」",
     [("run", "Stay home on every cloudy day.", "くもりの日は、ずっと家にいる。"),
      ("agree", "Yes, today is a total loss.", "うん、今日は全部ムダだね。"),
      ("ok", "Everything? You only forgot 1 umbrella.", "全部？傘を1本忘れただけだよ。")]),
]
_ev = "".join(f'<span class="c{i+1}">{_h.escape(c[0], quote=False)}</span>' for i, c in enumerate(CASES))
_th = "".join(f'<span class="c{i+1}">{_h.escape(c[2], quote=False)}</span>' for i, c in enumerate(CASES))
_op = "\n".join(f'        <button type="button" class="btn opt c{i+1}" data-k="{k}">{_h.escape(en, quote=False)}</button>'
                for i, c in enumerate(CASES) for (k, en, ja) in c[4])
_ja = {AG[0]: AG[1], RN[0]: RN[1], OK[0]: OK[1]}
for c in CASES:
    _ja[c[0]] = c[1]; _ja[c[2]] = c[3]
    for k, en, ja in c[4]:
        _ja[en] = ja

A = dict(
    slug="argue-with-your-gloomy-thought", seq=416,
    title="Argue back at your gloomy thought as if you were another person",
    title_ja="暗い考えには、他人になったつもりで反論してみる",
    label="Argue Back", label_ja="反論ノート",
    float="📓",
    alt="A chubby embroidered felt penguin holding a pencil over a real open notebook with blank pages",
    mood=["lift", "think"], tags=["psychology", "feelings", "tips"],
    src_no="17", src_title="悲観を楽観に変えるノート（3ステップ。セリグマン）",
    center="暗い考えは書き出して、他人になったつもりで反論する。反論の練習が前向きになるいちばんの方法。",
    tone="素材の重さ：真面目（悲観と楽観・心理学者の方法）\n→ 見せ方：ポップに（青とミントと黄色。3ステップのノートで遊べる）",
    tone_css="真面目な話 → ポップに。青とミント",
    game_name="3ステップ・ノート",
    play="📓 3ステップ・ノート：ノートのページに ①出来事 と、そのとき浮かんだ暗い考えが書いてある（駅で肩がぶつかって舌打ちされた→「私はいつもドンくさい」／英語で大きなまちがい→「みんなバカだと思っている」／傘を忘れてぬれた→「全部ダメにする」）。②反論を3つから選ぶ：賛成してしまう答え（😶 気分が下がる）・逃げる答え（💨 気分は変わらない）・他人になったつもりの反論（🎯 正解）。③気分メーターが 😞20% → 😊85% に上がる。3ページ終わると「🌤️ 反論がうまくなってきた」🎉。正解の位置はページごとに違う。",
    prompt="An extremely cute, chubby round penguin with a gentle face and a plain white belly (no rings or patterns on the belly), made of hand-embroidered felt with neat visible stitching along the edges, sitting at a small desk and holding a yellow pencil over one realistic open spiral notebook with clean blank cream pages, looking thoughtful and then a little proud. Bright background in clear sky blue and soft mint green with gentle depth, simple and uncluttered. Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering.",
    combo="ペンギン × 刺しゅうフェルト × ノートと鉛筆",
    pal=dict(bg="#f2f6ff", text="#1e2547", muted="#626a8c", a="#3048e0", b="#00b39c", c="#ffd84d", d="#ff6f61",
             big="#2f45d6", bigdark="#b3c0ff", h1="#18204a", ink="#1e2547", shadowc="rgba(48,72,224,.16)",
             bg1="rgba(0,179,156,.18)", bg2="rgba(255,216,77,.30)", bg3="rgba(48,72,224,.12)", photo="#e3e9ff",
             game="linear-gradient(150deg, #3048e0 0%, #4f7cf0 50%, #00a891 100%)"),
    cards=[
        dict(e="📓", l="A Notebook", lj="ノート", s=[(
            "The psychologist Martin Seligman suggests a notebook for arguing back at dark thoughts.",
            "心理学者のセリグマンは、暗い考えに反論するノートをすすめています。", False)]),
        dict(e="1️⃣", l="Step 1", lj="ステップ1", s=[(
            "First, write the event and the thought that came to you.",
            "まず、出来事と、そのとき浮かんだ考えを書きます。", False)]),
        dict(e="2️⃣", l="Step 2", lj="ステップ2", s=[(
            "Next, pretend to be another person, and argue back at the thought with all your power.",
            "次に、他人になったつもりで、その考えに全力で反論します。", False)]),
        dict(e="3️⃣", l="Step 3", lj="ステップ3", s=[(
            "Last, write how your mood changed.",
            "最後に、気分がどう変わったかを書きます。", False)]),
        "GAME",
        dict(e="🌤️", l="Best Practice", lj="いちばんの練習", s=[(
            "It seems that practice in arguing back is the best way to become positive.",
            "反論の練習は、前向きになるいちばんの方法だそうです。", True)]),
    ],
    game_html=r'''
  <!-- ⚡ 触って遊べる部品：3ステップ・ノート（出来事と暗い考え → 他人のつもりで反論を選ぶ → 気分メーター） -->
  <section class="game" data-c="1" data-w="" data-done="0" data-all="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">The 3-step notebook</div>
    <div class="page">
      <div class="steps" aria-hidden="true"><span class="stp s1">① Event</span><span class="stp s2">② Argue back</span><span class="stp s3">③ Mood</span></div>
      <div class="row"><span class="row-l">📅 What happened:</span> <span class="row-t">EVS</span></div>
      <div class="row think"><span class="row-l">💭 Gloomy thought:</span> <span class="row-t">THS</span></div>
      <div class="row-l ask">✍️ Pretend you are another person. Argue back!</div>
      <div class="opts">
OPS
      </div>
      <div class="react"><span class="r-agree">AGS</span><span class="r-run">RNS</span><span class="r-ok">OKS</span></div>
      <div class="mood">
        <span class="row-l">Mood:</span>
        <span class="m-face" aria-hidden="true">😞</span>
        <span class="m-bar" aria-hidden="true"><i></i></span>
        <span class="m-pc">20</span><span class="m-u">%</span>
      </div>
    </div>
    <div class="score"><span class="sc-l">📓 Pages done:</span> <span class="sc-n">0</span>/3</div>
    <div class="msg m-all">🌤️ 3 pages done! Arguing back is getting easier.</div>
    <div class="ctrl">
      <button type="button" class="btn b-next">Next page ➜</button>
      <button type="button" class="btn ghost b-reset">↺ Start over</button>
    </div>
  </section>
'''.replace("EVS", _ev).replace("THS", _th).replace("OPS", _op).replace("AGS", AG[0]).replace("RNS", RN[0]).replace("OKS", OK[0]),
    game_ja=dict({
        "The 3-step notebook": "3ステップ・ノート",
        "① Event": "① 出来事", "② Argue back": "② 反論", "③ Mood": "③ 気分",
        "📅 What happened:": "📅 起きたこと：",
        "💭 Gloomy thought:": "💭 暗い考え：",
        "✍️ Pretend you are another person. Argue back!": "✍️ 他人になったつもりで、反論しよう！",
        "Mood:": "気分：",
        "📓 Pages done:": "📓 書けたページ：",
        "🌤️ 3 pages done! Arguing back is getting easier.": "🌤️ 3ページ書けた！反論がうまくなってきました。",
        "Next page ➜": "次のページ ➜",
        "↺ Start over": "↺ 最初から",
    }, **_ja),
    css=r'''
  /* 📓 3ステップ・ノート */
  .page { max-width: 440px; margin: 14px auto 0; padding: 14px 14px 16px 22px; border-radius: 20px; text-align: left; color: var(--ink);
    background: #fffdf5; box-shadow: inset 6px 0 0 #ff8a80; }
  .steps { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 10px; }
  .stp { padding: 4px 10px; border-radius: 999px; background: #eceff8; color: #6a7193; font-size: 12.5px; font-weight: 900; }
  .s1, .s2 { background: #3048e0; color: #fff; }
  .game[data-w="ok"] .s3 { background: #00a891; color: #fff; animation: g-pop .4s cubic-bezier(.2,1.4,.4,1); }
  .row { margin-top: 6px; font-size: 15.5px; font-weight: 800; line-height: 1.5; }
  .row-l { font-size: 12.5px; font-weight: 900; letter-spacing: .04em; color: #3048e0; }
  .row-t span, .opt, .react span { display: none; }
  .game[data-c="1"] .c1, .game[data-c="2"] .c2, .game[data-c="3"] .c3 { display: inline; }
  .think .row-t { color: #4a4f6e; background: #eef0f7; padding: 2px 6px; border-radius: 6px; }
  .ask { display: block; margin-top: 12px; }
  .opts { display: grid; gap: 10px; margin-top: 8px; }
  .game[data-c="1"] .opt.c1, .game[data-c="2"] .opt.c2, .game[data-c="3"] .opt.c3 { display: flex; }
  .opt { width: 100%; justify-content: flex-start; text-align: left; font-size: 15.5px; padding: 12px 16px; border-radius: 18px;
    color: var(--ink); background: #fff; box-shadow: 0 0 0 2px #d9def0, 0 5px 0 #d9def0; }
  .opt.pick-ok { background: #d3f9ee; box-shadow: 0 0 0 3px #00a891, 0 5px 0 #00a891; }
  .opt.pick-bad { background: #f1f1f4; opacity: .65; }
  .game[data-w="ok"] .opt { pointer-events: none; }
  .react { min-height: 26px; margin-top: 10px; font-size: 15px; font-weight: 900; line-height: 1.45; }
  .game[data-w="agree"] .r-agree, .game[data-w="run"] .r-run, .game[data-w="ok"] .r-ok { display: inline; animation: g-in .3s ease-out; }
  .r-ok { color: #00876f; }
  .r-agree, .r-run { color: #8a5a00; }
  .mood { display: flex; align-items: center; gap: 8px; margin-top: 10px; padding-top: 10px; border-top: 2px dashed #e1e4ef; }
  .m-face { font-size: 26px; line-height: 1; display: inline-block; }
  .m-bar { position: relative; flex: 1; height: 14px; border-radius: 999px; background: #e7eaf3; overflow: hidden; }
  .m-bar i { position: absolute; inset: 0 auto 0 0; width: 20%; border-radius: 999px; background: linear-gradient(90deg, #ffd84d, #00b39c);
    transition: width .6s cubic-bezier(.2,1.2,.4,1); }
  .m-pc, .m-u { font-size: 16px; font-weight: 900; font-variant-numeric: tabular-nums; }
  .score { margin-top: 14px; font-size: 15.5px; font-weight: 900; }
  .sc-n { font-variant-numeric: tabular-nums; display: inline-block; }
  .m-all, .b-next { display: none; }
  .game[data-all="1"] .m-all { display: block; animation: g-pop .45s cubic-bezier(.2,1.4,.4,1); }
  .game[data-w="ok"][data-all="0"] .b-next { display: inline-flex; }
  .b-next { color: #3048e0; }
''',
    dark=r'''
  html[data-theme="dark"] .page { background: #f4f1e6; }
  html[data-theme="dark"] .opt { background: #f1edf8; }
  html[data-theme="dark"] .opt.pick-ok { background: #c6f0e3; }
  html[data-theme="dark"] .opt.pick-bad { background: #dcdce3; }
''',
    js=r'''
/* 📓 3ステップ・ノート：JS は data-*・class・style（メーター）・絵文字・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var bar = g.querySelector('.m-bar i'), pc = g.querySelector('.m-pc'), face = g.querySelector('.m-face'), scn = g.querySelector('.sc-n');
  var c = 1, done = 0;
  function mood(v) {
    bar.style.width = v + '%'; pc.textContent = String(v);
    face.textContent = v <= 15 ? '😣' : v <= 30 ? '😞' : '😊';
    face.classList.remove('pop'); void face.offsetWidth; face.classList.add('pop');
  }
  function page(n) {
    c = n; g.setAttribute('data-c', String(c)); g.setAttribute('data-w', '');
    [].forEach.call(g.querySelectorAll('.opt'), function (o) { o.classList.remove('pick-ok', 'pick-bad', 'shake'); });
    mood(20);
  }
  [].forEach.call(g.querySelectorAll('.opt'), function (o) {
    o.addEventListener('click', function () {
      if (g.getAttribute('data-w') === 'ok') return;
      var k = o.getAttribute('data-k');
      g.setAttribute('data-w', k);
      if (k === 'ok') {
        o.classList.add('pick-ok'); mood(85);
        done++; scn.textContent = String(done);
        scn.classList.remove('pop'); void scn.offsetWidth; scn.classList.add('pop');
        var r = o.getBoundingClientRect();
        if (done >= 3) {
          g.setAttribute('data-all', '1');
          if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🌤️', '📓', '🐧', '✨', '🎯'], 24);
        } else if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🎯', '✨', '📓'], 12);
        if (navigator.vibrate) { try { navigator.vibrate(25); } catch (e) {} }
      } else {
        o.classList.remove('shake'); void o.offsetWidth; o.classList.add('pick-bad', 'shake');
        mood(k === 'agree' ? 10 : 20);
      }
    });
  });
  g.querySelector('.b-next').addEventListener('click', function () { if (c < 3) page(c + 1); });
  g.querySelector('.b-reset').addEventListener('click', function () {
    done = 0; scn.textContent = '0'; g.setAttribute('data-all', '0'); page(1);
  });
  page(1);
})();
''',
)
