ARTS = []

POP = r'''function pop(el, list) {
    if (!window.pengessoPop || !el) return;
    var r = el.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, 16);
  }'''

# ─────────────────────────────── 542 speed-is-fewer-redos
ARTS.append(dict(
  slug='speed-is-fewer-redos', seq=542,
  title_en='Speed comes from fewer redos, not from fast hands',
  title_ja='速さは、手の速さより「やり直しの少なさ」で決まる',
  label_en='Fewer Redos', label_ja='やり直しを減らす',
  h1e='🏁', mood=['lift', 'learn'], tags=['psychology', 'productivity', 'tips'],
  alt='A chubby felted wool penguin writing a real handmade birthday card with a pen on a small desk',
  pal=dict(bg='#fff8ef', c1='#ff7a1a', c2='#12b5a5', sun='#ffd23f', c1d='#c2510a', c1l='#ffb27a',
           game='linear-gradient(150deg, #ff7a1a 0%, #ff9f1a 45%, #12b5a5 100%)',
           glow1='rgba(255,122,26,.22)', glow2='rgba(18,181,165,.18)', glow3='rgba(255,210,63,.22)', photobg='#ffeedd'),
  S=[('早く終わらせたいとき、私はつい手を速く動かそうとします。', 'When I want to finish fast, I try to move my hands fast.'),
     ('でも、速さを決めるのは「やり直しの少なさ」らしいです。', 'But it seems that speed is decided by "fewer redos."'),
     ('手の速さが効くのは、1割くらいだそうです。', 'They say fast hands help only about 10%.'),
     ('遅くなるのは、作り直し・確認・ミスの直しが積み重なるからです。', 'It gets slow because remaking, checking, and fixing mistakes pile up.'),
     ('誕生日カードも、書くことを先に決めておけば、1回で書き終わります。', 'With a birthday card too, if you decide what to write first, you can finish it in 1 try.')],
  layout=[('🏃', 'The Habit', 'ついやること', ['1'], None),
          ('🔑', 'The Real Key', '本当のカギ', ['!2', '3'], '''    <div class="bars" aria-hidden="true">
      <div class="bar-row"><span class="bar-name">{{✋ Fast hands|✋ 手の速さ}}</span><span class="bar"><i class="b-hand"></i></span><span class="bar-n">10%</span></div>
      <div class="bar-row"><span class="bar-name">{{↺ Fewer redos|↺ やり直しの少なさ}}</span><span class="bar"><i class="b-redo"></i></span><span class="bar-n">90%</span></div>
    </div>'''),
          ('🐌', 'Why So Slow', '遅くなる理由', ['4'], None),
          'GAME',
          ('🎂', 'Card Example', 'カードの例', ['5'], None)],
  game_name='誕生日カード・レース',
  game_html=r'''  <section class="game" data-s="pick" data-pick="" data-oops="0" data-r="" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">{{The birthday card race|誕生日カード・レース}}</div>
    <div class="game-hint">{{Who finishes the card first? Pick one, then tap fast!|先にカードを書き終わるのはどっち？選んでから、連打しよう！}}</div>
    <div class="lanes">
      <div class="lane lane-a">
        <div class="lane-top"><span class="lane-name">{{💨 Fast Hands|💨 手が速い}}</span><span class="lane-note"><span class="rl">{{↺ Redos:|↺ やり直し：}}</span> <span class="rn">0</span></span></div>
        <div class="track"><span class="goalflag" aria-hidden="true">🎂</span><span class="runner ra" aria-hidden="true">🐧</span></div>
      </div>
      <div class="lane lane-b">
        <div class="lane-top"><span class="lane-name">{{📝 Plan First|📝 先に決める}}</span><span class="lane-note"><span class="rl">{{↺ Redos:|↺ やり直し：}}</span> <span class="rn2">0</span></span></div>
        <div class="track"><span class="goalflag" aria-hidden="true">🎂</span><span class="runner rb" aria-hidden="true">🐧</span></div>
      </div>
    </div>
    <div class="oops">
      <span class="o1">{{✏️ Wrong name! Start again!|✏️ 名前をまちがえた！書き直し！}}</span>
      <span class="o2">{{📏 No space left! Start again!|📏 スペースが足りない！書き直し！}}</span>
      <span class="o3">{{💧 The ink got smudged! Start again!|💧 インクがにじんだ！書き直し！}}</span>
    </div>
    <div class="g-row picks">
      <button type="button" class="gbtn pa">{{💨 Fast Hands|💨 手が速い}}</button>
      <button type="button" class="gbtn pb">{{📝 Plan First|📝 先に決める}}</button>
    </div>
    <button type="button" class="gbtn wide go">{{✏️ Tap to write!|✏️ 押して書く！}}</button>
    <div class="msg">
      <div class="m-win">{{🎉 You win! "Plan First" wrote it in 1 try.|🎉 勝ち！「先に決める」は1回で書き終わった。}}</div>
      <div class="m-lose">{{😅 "Fast Hands" had 3 redos. "Plan First" won!|😅「手が速い」は3回やり直し。「先に決める」の勝ち！}}</div>
    </div>
    <button type="button" class="gbtn ghost again">{{↺ Race again|↺ もう一回レース}}</button>
  </section>''',
  game_css=r'''
  .bars { display: grid; gap: 8px; margin-top: 14px; }
  .bar-row { display: grid; grid-template-columns: minmax(0, 8.5em) 1fr 3em; align-items: center; gap: 8px; font-weight: 900; font-size: 14px; }
  .bar { height: 16px; border-radius: 999px; background: #fdebd9; overflow: hidden; }
  .bar i { display: block; height: 100%; border-radius: 999px; }
  .b-hand { width: 10%; background: #ffb27a; }
  .b-redo { width: 90%; background: linear-gradient(90deg, #12b5a5, #2fd3a7); }
  .bar-n { text-align: right; color: var(--c1d); }

  .lanes { display: grid; gap: 10px; margin: 16px 0 4px; }
  .lane { background: rgba(255,255,255,.96); color: var(--text); border-radius: 20px; padding: 10px 12px; text-align: left; transition: box-shadow .2s; }
  .lane-top { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 4px 8px; font-weight: 900; font-size: 15px; }
  .lane-note { font-size: 13px; color: var(--muted); }
  .lane-note .rn, .lane-note .rn2 { color: var(--c1d); font-size: 16px; }
  .track { position: relative; height: 46px; margin-top: 6px; border-radius: 999px;
    background: repeating-linear-gradient(90deg, #ffe7d1 0 22px, #fff3e6 22px 44px); }
  .runner { position: absolute; top: 4px; left: 0; width: 38px; text-align: center; font-size: 30px; line-height: 38px; transition: left .22s ease-out; }
  .goalflag { position: absolute; right: 6px; top: 4px; font-size: 28px; line-height: 38px; }
  .game[data-pick="a"] .lane-a, .game[data-pick="b"] .lane-b { box-shadow: 0 0 0 4px var(--sun); }
  .lane.shake .runner { animation: shake .45s ease; }
  .oops { min-height: 30px; margin-top: 8px; font-weight: 900; font-size: 16px; }
  .oops span { display: none; }
  .game[data-oops="1"] .oops .o1, .game[data-oops="2"] .oops .o2, .game[data-oops="3"] .oops .o3 { display: inline-block; animation: popin .3s both; }
  .game .go, .game .again, .game .picks { display: none; }
  .game[data-s="pick"] .picks { display: flex; }
  .game[data-s="race"] .go { display: inline-flex; min-height: 84px; font-size: 24px; margin-top: 10px; }
  .game[data-s="done"] .again { display: inline-flex; margin-top: 12px; }
  .game[data-s="done"][data-r="win"] .m-win, .game[data-s="done"][data-r="lose"] .m-lose { display: block; }
''',
  dark_css=r'''  html[data-theme="dark"] .game .lane { background: #22242f; color: #f4f0fa; }
  html[data-theme="dark"] .game .track { background: repeating-linear-gradient(90deg, #3a3240 0 22px, #2e2a36 22px 44px); }
  html[data-theme="dark"] .bar { background: #3a3240; }
  html[data-theme="dark"] .bar-n, html[data-theme="dark"] .lane-note .rn, html[data-theme="dark"] .lane-note .rn2 { color: #ffb27a; }''',
  game_js=r'''/* 🏁 誕生日カード・レース：「手が速い」は2マス進むが3回やり直し、「先に決める」は1マスずつで1回 */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var ra = g.querySelector('.ra'), rb = g.querySelector('.rb'), la = g.querySelector('.lane-a');
  var rn = g.querySelector('.rn'), go = g.querySelector('.go');
  var LEN = 10, A = 0, B = 0, red = 0;
  POPFN
  function place(el, p) { var f = Math.min(p, LEN) / LEN; el.style.left = 'calc(' + (f * 100) + '% - ' + (f * 44) + 'px)'; }
  function reset() { A = 0; B = 0; red = 0; place(ra, 0); place(rb, 0); rn.textContent = '0';
    g.setAttribute('data-oops', '0'); g.setAttribute('data-r', ''); g.setAttribute('data-pick', ''); g.setAttribute('data-s', 'pick'); }
  function pick(w) { g.setAttribute('data-pick', w); g.setAttribute('data-s', 'race'); }
  g.querySelector('.pa').addEventListener('click', function () { pick('a'); });
  g.querySelector('.pb').addEventListener('click', function () { pick('b'); });
  go.addEventListener('click', function () {
    if (g.getAttribute('data-s') !== 'race') return;
    B += 1; A += 2;
    if (A >= 6 && red < 3) {
      red += 1; A = 0; rn.textContent = String(red);
      g.setAttribute('data-oops', String(red));
      la.classList.remove('shake'); void la.offsetWidth; la.classList.add('shake');
    }
    place(ra, A); place(rb, B);
    if (B >= LEN) {
      var win = g.getAttribute('data-pick') === 'b';
      g.setAttribute('data-r', win ? 'win' : 'lose');
      g.setAttribute('data-s', 'done');
      pop(rb, ['🎂', '🐧', '✨', '📝'], 16);
    }
  });
  g.querySelector('.again').addEventListener('click', reset);
  reset();
})();'''.replace('POPFN', POP),
  sec='速く、うまくなる技術', exkind='誕生日カード',
  core='速さは、手の速さより「やり直しの少なさ」で決まる。',
  weight='段取りのコツ', look='オレンジとエメラルド。誕生日カードのレースで遊べる',
  gamedesc='🏁 誕生日カード・レース：「💨 手が速い」と「📝 先に決める」のどちらが先に書き終わるか選んで、「✏️ 押して書く！」を連打する。手が速いペンギンは1回で2マス進むが、名前のまちがい・スペース不足・インクのにじみで3回スタートに戻る。先に決めたペンギンは1マスずつだが、やり直しなしで先にゴール（10回）。選んだほうで「勝ち／負け」のメッセージ。',
  prompt='An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of soft felted wool, sitting at a small wooden desk and calmly writing on a realistic folded handmade birthday card with a real ballpoint pen, a tiny sticky note with a plan lying next to it. Bright simple warm orange and mint background with soft depth. Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering.',
  combo='ペンギン × フェルト羊毛 × 手作りの誕生日カード',
))

# ─────────────────────────────── 543 outline-before-you-start
ARTS.append(dict(
  slug='outline-before-you-start', seq=543,
  title_en='Before you start, decide 3 things: the goal, the wall, and the fix',
  title_ja='始める前に、ゴール・壁・解決策の3つを決める',
  label_en='3-Line Plan', label_ja='3行の計画',
  h1e='🧺', mood=['lift', 'learn'], tags=['psychology', 'productivity', 'tips'],
  alt='A chubby corduroy and felt plush penguin standing next to a real wicker picnic basket on green grass',
  pal=dict(bg='#f3fbff', c1='#1e88e5', c2='#7cc72b', sun='#ffd43b', c1d='#1565c0', c1l='#8cc4ff',
           game='linear-gradient(155deg, #1e88e5 0%, #34a6e8 50%, #7cc72b 100%)',
           glow1='rgba(30,136,229,.18)', glow2='rgba(124,199,43,.20)', glow3='rgba(255,212,59,.22)', photobg='#e6f3ff'),
  S=[('手を動かす前に、3つのことを決めておくといいそうです。', 'It is said that it is good to decide 3 things before you move your hands.'),
     ('1つ目は、ゴール。手に入れたい結果です。', 'The 1st is the goal. It is the result you want to get.'),
     ('2つ目は、壁。ゴールとの間にある問題です。', 'The 2nd is the wall. It is the problem between you and the goal.'),
     ('3つ目は、解決策。その壁を壊す方法です。', 'The 3rd is the fix. It is the way to break that wall.'),
     ('中でも、ゴールで9割が決まるそうです。', 'Of the 3, the goal decides 90%, they say.')],
  layout=[('✋', 'Before You Start', '始める前に', ['1'], None),
          ('🎯', '1 The Goal', '1 ゴール', ['2'], None),
          ('🧱', '2 The Wall', '2 壁', ['3'], None),
          ('🔧', '3 The Fix', '3 解決策', ['4'], None),
          'GAME',
          ('💯', 'The Big One', 'いちばん大事', ['!5'], None)],
  game_name='ピクニックの3行計画',
  game_html=r'''  <section class="game" data-s="plan" data-n="0" data-r="" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">{{Plan a picnic in 3 lines|3行でピクニックを計画しよう}}</div>
    <div class="game-hint">{{Open the blocks in order. You can go any time!|ブロックを順番に開こう。いつ出発してもいいよ！}}</div>
    <div class="blocks">
      <button type="button" class="blk b1" data-i="1"><span class="bh">{{🎯 Goal|🎯 ゴール}}</span><span class="bq" aria-hidden="true">❓</span><span class="ba">{{Everyone laughs together.|みんなで笑う。}}</span></button>
      <button type="button" class="blk b2" data-i="2" disabled><span class="bh">{{🧱 Wall|🧱 壁}}</span><span class="bq" aria-hidden="true">❓</span><span class="ba">{{It may rain.|雨が降るかも。}}</span></button>
      <button type="button" class="blk b3" data-i="3" disabled><span class="bh">{{🔧 Fix|🔧 解決策}}</span><span class="bq" aria-hidden="true">❓</span><span class="ba">{{Pick a park with a roof.|屋根のある公園にする。}}</span></button>
    </div>
    <div class="scene" aria-hidden="true">
      <span class="sky">☁️</span>
      <span class="drop d1">💧</span><span class="drop d2">💧</span><span class="drop d3">💧</span>
      <span class="shelter"><span class="roof"></span><span class="post p1"></span><span class="post p2"></span></span>
      <span class="crowd">🐧🐧🐧🧺</span>
    </div>
    <div class="msg">
      <div class="m-0">{{🌀 Where are we going? Nobody knows… We got lost.|🌀 どこに行くの？誰も知らない…迷子になった。}}</div>
      <div class="m-1">{{🌧️ Rain! We had a goal, but forgot the wall.|🌧️ 雨！ゴールはあったのに、壁を忘れてた。}}</div>
      <div class="m-2">{{☔ We knew it may rain, but had no fix. Soaking wet!|☔ 雨かもとは分かっていたのに、解決策がなかった。びしょぬれ！}}</div>
      <div class="m-3">{{☀️ It rained, but we laughed together under the roof!|☀️ 雨が降ったけど、屋根の下でみんなで笑った！}}</div>
    </div>
    <div class="g-row">
      <button type="button" class="gbtn wide go">{{🧺 Go on the picnic!|🧺 ピクニックに出発！}}</button>
      <button type="button" class="gbtn ghost again">{{↺ Plan again|↺ 計画しなおす}}</button>
    </div>
  </section>''',
  game_css=r'''
  .blocks { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px; margin-top: 14px; }
  .blk { min-height: 116px; border: 0; border-radius: 18px; background: rgba(255,255,255,.96); color: var(--text); font: inherit; font-weight: 900;
    padding: 10px 6px; cursor: pointer; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px;
    box-shadow: 0 5px 0 rgba(0,0,0,.16); -webkit-tap-highlight-color: transparent; touch-action: manipulation; transition: transform .16s ease, opacity .2s; }
  .blk .bh { font-size: 14px; }
  .blk .bq { font-size: 28px; line-height: 1; }
  .blk .ba { display: none; font-size: 14px; line-height: 1.35; overflow-wrap: anywhere; }
  .game .blk.open .bq { display: none; }
  .game .blk.open .ba { display: block; }
  .blk.open { background: #fff6c2; }
  .blk[disabled] { opacity: .5; cursor: default; }
  .blk.next { box-shadow: 0 0 0 4px var(--sun), 0 5px 0 rgba(0,0,0,.16); }
  .blk.squash { transform: scaleX(0); }

  .scene { position: relative; height: 150px; margin-top: 14px; border-radius: 22px; overflow: hidden;
    background: linear-gradient(#bfe6ff 0%, #e9f8ff 64%, #8fd46a 64%, #79c257 100%); }
  .sky { position: absolute; top: 8px; left: 50%; transform: translateX(-50%); font-size: 44px; line-height: 1; transition: transform .3s; }
  .drop { position: absolute; top: 40px; font-size: 20px; opacity: 0; }
  .d1 { left: 30%; } .d2 { left: 52%; } .d3 { left: 70%; }
  .scene.rain .drop { animation: fall .9s linear infinite; }
  .scene.rain .d2 { animation-delay: .3s; } .scene.rain .d3 { animation-delay: .6s; }
  @keyframes fall { 0% { opacity: 0; transform: translateY(0); } 20% { opacity: 1; } 100% { opacity: 0; transform: translateY(70px); } }
  .shelter { position: absolute; left: 50%; bottom: 14px; width: 170px; height: 92px; transform: translateX(-50%) scale(0); transform-origin: 50% 100%;
    transition: transform .45s cubic-bezier(.2,1.4,.4,1); }
  .scene.roofed .shelter { transform: translateX(-50%) scale(1); }
  .roof { position: absolute; left: 0; right: 0; top: 0; height: 40px; background: #ff7043; clip-path: polygon(50% 0, 100% 100%, 0 100%); }
  .post { position: absolute; top: 40px; bottom: 0; width: 8px; background: #8d5a3b; border-radius: 4px; }
  .p1 { left: 22px; } .p2 { right: 22px; }
  .crowd { position: absolute; bottom: 10px; left: 50%; font-size: 28px; line-height: 1; white-space: nowrap; transform: translateX(-260%);
    transition: transform .9s ease-out; }
  .scene.walk .crowd { transform: translateX(-50%); }
  .scene.wet .crowd { animation: shiver .25s linear 6; }
  .scene.lost .crowd { animation: wander 1.2s ease-in-out 2; }
  @keyframes shiver { 50% { margin-left: 3px; } }
  @keyframes wander { 25% { margin-left: -60px; } 75% { margin-left: 60px; } }

  .game .go, .game .again { display: none; }
  .game[data-s="plan"] .go { display: inline-flex; }
  .game[data-s="done"] .again { display: inline-flex; }
  .game[data-s="done"][data-r="0"] .m-0, .game[data-s="done"][data-r="1"] .m-1,
  .game[data-s="done"][data-r="2"] .m-2, .game[data-s="done"][data-r="3"] .m-3 { display: block; }
''',
  dark_css=r'''  html[data-theme="dark"] .game .blk { background: #22242f; color: #f4f0fa; }
  html[data-theme="dark"] .game .blk.open { background: #3b3820; }''',
  game_js=r'''/* 🧺 ピクニックの3行計画：開いたブロックの数で、ピクニックの結末が変わる */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var blks = [].slice.call(g.querySelectorAll('.blk')), scene = g.querySelector('.scene'), sky = g.querySelector('.sky');
  var go = g.querySelector('.go'), n = 0, busy = false, timers = [];
  POPFN
  function mark() { blks.forEach(function (b, i) { b.disabled = (i !== n) || busy; b.classList.toggle('next', i === n && !busy); }); }
  blks.forEach(function (b, i) {
    b.addEventListener('click', function () {
      if (i !== n || busy) return;
      b.classList.add('squash');
      setTimeout(function () { b.classList.add('open'); b.classList.remove('squash'); }, 160);
      n += 1; g.setAttribute('data-n', String(n)); mark();
      if (n === 3) pop(b, ['🧺', '✨', '🐧'], 10);
    });
  });
  function later(f, ms) { timers.push(setTimeout(f, ms)); }
  go.addEventListener('click', function () {
    if (busy || g.getAttribute('data-s') !== 'plan') return;
    busy = true; go.disabled = true; mark();
    scene.className = 'scene walk';
    later(function () {
      if (n === 0) { scene.classList.add('lost'); }
      else { sky.textContent = '🌧️'; scene.classList.add('rain'); if (n === 3) scene.classList.add('roofed'); else scene.classList.add('wet'); }
    }, 950);
    later(function () {
      g.setAttribute('data-r', String(n)); g.setAttribute('data-s', 'done');
      if (n === 3) pop(scene, ['☀️', '🐧', '🧺', '🎉'], 18);
    }, 2100);
  });
  g.querySelector('.again').addEventListener('click', function () {
    timers.forEach(clearTimeout); timers = [];
    n = 0; busy = false; go.disabled = false; sky.textContent = '☁️'; scene.className = 'scene';
    blks.forEach(function (b) { b.classList.remove('open', 'squash'); });
    g.setAttribute('data-n', '0'); g.setAttribute('data-r', ''); g.setAttribute('data-s', 'plan'); mark();
  });
  mark();
})();'''.replace('POPFN', POP),
  sec='速く、うまくなる技術', exkind='ピクニックの計画',
  core='始める前に、ゴール・壁・解決策の3つを決める。',
  weight='段取りのコツ', look='空色と黄緑。ピクニックの計画で遊べる',
  gamedesc='🧺 ピクニックの3行計画：🎯ゴール（みんなで笑う）→🧱壁（雨が降るかも）→🔧解決策（屋根のある公園）のブロックを順番に開ける。いつでも「ピクニックに出発！」を押せて、開いた数で結末が変わる（0個＝迷子／1個＝雨でびっくり／2個＝雨と分かっていたのにびしょぬれ／3個＝屋根の下でみんなで笑う＋紙吹雪）。',
  prompt='An extremely cute, chubby round penguin with a gentle face and a plain white belly, made as a plush toy of corduroy and felt, standing happily on soft green grass next to a realistic wicker picnic basket with a folded checkered cloth, a small wooden gazebo roof softly blurred behind. Bright simple sky-blue and fresh green background with soft depth. Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering.',
  combo='ペンギン × コーデュロイとフェルトのぬいぐるみ × ピクニックバスケット',
))

# ─────────────────────────────── 544 one-step-above-the-request
ARTS.append(dict(
  slug='one-step-above-the-request', seq=544,
  title_en='Make your goal one step above what you were asked to do',
  title_ja='頼まれた作業ではなく、その一段上の「本当に欲しいもの」をゴールにする',
  label_en='One Step Up', label_ja='一段上',
  h1e='🪜', mood=['lift', 'think'], tags=['psychology', 'productivity', 'friends'],
  alt='A chubby crocheted amigurumi penguin standing on a small real wooden step ladder holding a loaf of bread',
  pal=dict(bg='#fffaf0', c1='#ff5a5f', c2='#ffb400', sun='#ffe14d', c1d='#d63a40', c1l='#ff9da0',
           game='linear-gradient(160deg, #ff5a5f 0%, #ff7f50 50%, #ffb400 100%)',
           glow1='rgba(255,90,95,.18)', glow2='rgba(255,180,0,.22)', glow3='rgba(255,225,77,.25)', photobg='#ffefe6'),
  S=[('ゴールは、頼まれた作業そのものではありません。', 'The goal is not the task you were asked to do.'),
     ('その一段上にある「頼んだ人が本当に欲しいもの」です。', 'It is one step above it: "what the person really wants."'),
     ('たとえば、友達に「パンを買ってきて」と頼まれたとします。', 'For example, a friend asks you, "Please buy bread."'),
     ('本当に欲しいのは、パンではなく「ゆっくりできる日曜の朝ごはん」かもしれません。', 'What they really want may not be bread but "a slow Sunday breakfast."'),
     ('そう分かると、ジャムも買っていこうと思えます。', 'When you know that, you can think, "I will buy jam too."')],
  layout=[('📋', 'Not the Task', '作業ではない', ['1'], None),
          ('🪜', 'One Step Up', '一段上', ['!2'], None),
          ('🍞', 'For Example', 'たとえば', ['3'], None),
          'GAME',
          ('☀️', 'The Real Wish', '本当の願い', ['4'], None),
          ('🍓', 'Better Choices', 'いい選択', ['5'], None)],
  game_name='一段上のはしご',
  game_html=r'''  <section class="game" data-lv="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">{{Climb one step up|一段上にのぼろう}}</div>
    <div class="req">{{💬 Your friend: "Please buy bread!"|💬 友達：「パン買ってきて！」}}</div>
    <div class="climb">
      <div class="ladder">
        <div class="rung r0"><span class="rt">{{👣 Ground|👣 地面}}</span><span class="me" aria-hidden="true">🐧</span></div>
        <div class="rung r1"><span class="rt">{{🍞 Bread|🍞 パン}}</span><span class="me" aria-hidden="true">🐧</span></div>
        <div class="rung r2"><span class="rt">{{🍳 Breakfast|🍳 朝ごはん}}</span><span class="me" aria-hidden="true">🐧</span></div>
        <div class="rung r3"><span class="rt">{{☀️ A slow Sunday morning|☀️ ゆっくりした日曜の朝}}</span><span class="me" aria-hidden="true">🐧</span></div>
        <div class="rung r4"><span class="rt">{{🌍 World peace|🌍 世界平和}}</span><span class="me" aria-hidden="true">🐧</span></div>
      </div>
      <div class="side">
        <span class="face" aria-hidden="true">😐</span>
        <div class="side-t">{{🧺 Your basket|🧺 かご}}</div>
        <div class="items" aria-hidden="true"><span class="it it1">🍞</span><span class="it it2">🧈</span><span class="it it3">🍓</span><span class="it it4">☕</span><span class="it it5">🌼</span></div>
      </div>
    </div>
    <div class="msg">
      <div class="m0">{{Your friend asked for bread. Climb up and see!|頼まれたのはパン。のぼって見てみよう！}}</div>
      <div class="m1">{{🍞 Just bread. OK, but…|🍞 パンだけ。OK、でも…}}</div>
      <div class="m2">{{🍳 Oh, it is for breakfast! Butter too?|🍳 そうか、朝ごはん用だ！バターもいるかな？}}</div>
      <div class="m3">{{☀️ A slow Sunday morning! Jam, coffee, and a little flower. 🎉|☀️ ゆっくりした日曜の朝！ジャムとコーヒーと、小さな花も 🎉}}</div>
      <div class="m4">{{🌍 World peace? Too high! 1 step up is enough. 😂|🌍 世界平和？高すぎ！一段上で十分 😂}}</div>
    </div>
    <div class="g-row">
      <button type="button" class="gbtn wide up"><span class="u-up">{{⬆ One step up|⬆ 一段のぼる}}</span><span class="u-more">{{⬆ Even higher?|⬆ もっと上？}}</span><span class="u-down">{{⬇ Back down 1 step|⬇ 一段おりる}}</span></button>
      <button type="button" class="gbtn ghost again">{{↺ Start again|↺ 最初から}}</button>
    </div>
  </section>''',
  game_css=r'''
  .req { display: inline-block; margin-top: 12px; padding: 10px 16px; border-radius: 18px 18px 18px 6px; background: #fff; color: var(--text);
    font-weight: 900; font-size: 16px; line-height: 1.4; }
  .climb { display: grid; grid-template-columns: minmax(0, 1fr) 112px; gap: 10px; margin-top: 14px; align-items: stretch; }
  .ladder { display: flex; flex-direction: column-reverse; gap: 8px; padding: 0 10px; position: relative;
    border-left: 6px solid rgba(255,255,255,.7); border-right: 6px solid rgba(255,255,255,.7); border-radius: 6px; }
  .rung { display: flex; align-items: center; justify-content: space-between; gap: 6px; min-height: 46px; padding: 8px 10px; border-radius: 14px;
    background: rgba(255,255,255,.22); font-weight: 900; font-size: 15px; text-align: left; line-height: 1.3; transition: background .25s, color .25s, transform .25s; }
  .rung.r4 { background: transparent; border: 2px dashed rgba(255,255,255,.65); }
  .rung.on { background: #fff; color: var(--text); }
  .rung.r4.on { background: #e8e4ff; }
  .rung.cur { transform: scale(1.04); box-shadow: 0 0 0 4px var(--sun); }
  .rung .me { font-size: 26px; line-height: 1; opacity: 0; transform: translateY(8px); transition: opacity .2s, transform .25s cubic-bezier(.2,1.6,.4,1); }
  .rung.cur .me { opacity: 1; transform: none; }
  .side { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; padding: 10px 6px; border-radius: 18px;
    background: rgba(255,255,255,.96); color: var(--text); }
  .face { font-size: 40px; line-height: 1; transition: transform .25s; }
  .face.bump { animation: popin .4s cubic-bezier(.2,1.6,.4,1); }
  .side-t { font-size: 13px; font-weight: 900; }
  .items { display: grid; grid-template-columns: repeat(3, 1fr); gap: 4px; font-size: 24px; }
  .it { opacity: .14; filter: grayscale(1); transform: scale(.8); transition: opacity .3s, filter .3s, transform .35s cubic-bezier(.2,1.6,.4,1); }
  .it.got { opacity: 1; filter: none; transform: none; }
  .up span { display: none; }
  .game[data-lv="0"] .u-up, .game[data-lv="1"] .u-up, .game[data-lv="2"] .u-up, .game[data-lv="3"] .u-more, .game[data-lv="4"] .u-down { display: inline; }
  .game .again { display: none; }
  .game[data-lv="3"] .again, .game[data-lv="4"] .again { display: inline-flex; }
  .game[data-lv="0"] .m0, .game[data-lv="1"] .m1, .game[data-lv="2"] .m2, .game[data-lv="3"] .m3, .game[data-lv="4"] .m4 { display: block; }
''',
  dark_css=r'''  html[data-theme="dark"] .req, html[data-theme="dark"] .game .side, html[data-theme="dark"] .game .rung.on { background: #22242f; color: #f4f0fa; }
  html[data-theme="dark"] .game .rung.r4.on { background: #2f2a48; }''',
  game_js=r'''/* 🪜 一段上のはしご：パン → 朝ごはん → ゆっくりした日曜の朝。のぼりすぎると「世界平和」 */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var rungs = [].slice.call(g.querySelectorAll('.rung')), its = [].slice.call(g.querySelectorAll('.it')), face = g.querySelector('.face');
  var FACES = ['😐', '🙂', '😊', '😄', '😵'], GOT = [0, 1, 2, 5, 5], lv = 0, best = 0;
  POPFN
  function draw() {
    g.setAttribute('data-lv', String(lv));
    rungs.forEach(function (r, i) { r.classList.toggle('on', i <= lv); r.classList.toggle('cur', i === lv); });
    its.forEach(function (it, i) { it.classList.toggle('got', i < GOT[lv]); });
    face.textContent = FACES[lv];
    face.classList.remove('bump'); void face.offsetWidth; face.classList.add('bump');
  }
  g.querySelector('.up').addEventListener('click', function () {
    lv = lv === 4 ? 3 : lv + 1;
    draw();
    if (lv === 3 && best < 3) { best = 3; pop(face, ['🍓', '☕', '🌼', '🍞', '✨'], 16); }
  });
  g.querySelector('.again').addEventListener('click', function () { lv = 0; best = 0; draw(); });
  draw();
})();'''.replace('POPFN', POP),
  sec='速く、うまくなる技術', exkind='友達のおつかい',
  core='言われた作業ではなく、その一段上の「頼んだ人が本当に欲しいもの」をゴールにする。',
  weight='段取りのコツ', look='コーラルと山吹色。はしごをのぼって遊べる',
  gamedesc='🪜 一段上のはしご：友達に「パン買ってきて！」と頼まれる。「⬆ 一段のぼる」を押すと、🍞パン → 🍳朝ごはん → ☀️ゆっくりした日曜の朝 とのぼり、かごの中身（パン→バター→ジャム・コーヒー・花）と友達の顔（😐→😄）が変わる。さらに「もっと上？」を押すと「🌍 世界平和？高すぎ！一段上で十分 😂」というオチ。',
  prompt='An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of crocheted amigurumi yarn, standing on the second step of a small realistic wooden step ladder and proudly holding a real fresh loaf of bread, a small jar of strawberry jam on the floor beside the ladder. Bright simple coral and sunny yellow background with soft depth. Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering.',
  combo='ペンギン × あみぐるみ × 木の踏み台',
))

# ─────────────────────────────── 545 split-the-goal-into-clear-words
ARTS.append(dict(
  slug='split-the-goal-into-clear-words', seq=545,
  title_en='Split a vague goal into words that everyone reads the same way',
  title_ja='ゴールはあいまいな言葉のままにしない。誰が読んでもズレない言葉に分ける',
  label_en='Clear Words', label_ja='ズレない言葉',
  h1e='✂️', mood=['lift', 'learn'], tags=['psychology', 'productivity', 'tips'],
  alt='A chubby layered cut paper penguin sitting on a real small travel suitcase in a paper diorama',
  pal=dict(bg='#f8f5ff', c1='#7b4dff', c2='#00c2d1', sun='#ffe066', c1d='#5b2fe0', c1l='#c2adff',
           game='linear-gradient(150deg, #7b4dff 0%, #5b6dff 45%, #00c2d1 100%)',
           glow1='rgba(123,77,255,.18)', glow2='rgba(0,194,209,.20)', glow3='rgba(255,224,102,.22)', photobg='#efe9ff'),
  S=[('一番多いミスは、ゴールをあいまいな言葉で決めることだそうです。', 'It is said that the most common mistake is to set a goal with vague words.'),
     ('「楽しい旅行」と言っても、海を思う人も、街を思う人も、山を思う人もいます。', 'When you say "a fun trip," some people think of the sea, some think of a city, and some think of mountains.'),
     ('だから、誰が読んでもズレないところまで、言葉を分けます。', 'So split the words until nobody reads them in a different way.'),
     ('「暖かい・海の近く・2日間」なら、みんな同じ旅を思い浮かべます。', 'With "warm, near the sea, 2 days," everyone pictures the same trip.')],
  layout=[('🌀', 'Common Mistake', 'よくあるミス', ['1'], None),
          ('🧳', 'A Fun Trip', '楽しい旅行', ['2'], None),
          'GAME',
          ('✂️', 'Split It', '分ける', ['3'], None),
          ('🏖️', 'Same Picture', '同じ絵', ['!4'], None)],
  game_name='旅の言葉ハサミ',
  game_html=r'''  <section class="game" data-k="0" data-w1="0" data-w2="0" data-w3="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">{{Make the trip words clear|旅の言葉をはっきりさせよう}}</div>
    <div class="goalbox"><span class="gb-t">{{🧳 Goal: a fun trip|🧳 ゴール：楽しい旅行}}</span> <span class="w w1">{{☀️ warm|☀️ 暖かい}}</span> <span class="w w2">{{🌊 near the sea|🌊 海の近く}}</span> <span class="w w3">{{🗓️ 2 days|🗓️ 2日間}}</span></div>
    <div class="friends">
      <div class="fr"><span class="who" aria-hidden="true">🐧</span><div class="think"><span class="pic pa">🏖️</span><span class="days"><span class="d da">1</span> <span class="du">{{day(s)|日}}</span></span></div></div>
      <div class="fr"><span class="who" aria-hidden="true">🐻‍❄️</span><div class="think"><span class="pic pb">🏙️</span><span class="days"><span class="d db">7</span> <span class="du">{{day(s)|日}}</span></span></div></div>
      <div class="fr"><span class="who" aria-hidden="true">🦭</span><div class="think"><span class="pic pc">🏔️</span><span class="days"><span class="d dc">3</span> <span class="du">{{day(s)|日}}</span></span></div></div>
    </div>
    <div class="same"><span class="same-t">{{👀 Same picture|👀 同じ絵}}</span><span class="sbar"><i></i></span></div>
    <div class="g-hint2">{{✂️ Tap a word to add it to the goal.|✂️ 言葉を押して、ゴールに足そう。}}</div>
    <div class="g-row chips">
      <button type="button" class="gbtn chip c1" data-w="1">{{☀️ warm|☀️ 暖かい}}</button>
      <button type="button" class="gbtn chip c2" data-w="2">{{🌊 near the sea|🌊 海の近く}}</button>
      <button type="button" class="gbtn chip c3" data-w="3">{{🗓️ 2 days|🗓️ 2日間}}</button>
    </div>
    <div class="msg">
      <div class="m0">{{😵 3 friends, 3 different trips!|😵 3人いたら、3つの別の旅！}}</div>
      <div class="m1">{{🤔 A little closer…|🤔 ちょっと近づいた…}}</div>
      <div class="m2">{{🙂 Almost the same!|🙂 ほとんど同じ！}}</div>
      <div class="m3">{{🎉 Everyone pictures the same trip!|🎉 みんな同じ旅を思い浮かべた！}}</div>
    </div>
    <button type="button" class="gbtn ghost again">{{↺ Back to "a fun trip"|↺「楽しい旅行」に戻す}}</button>
  </section>''',
  game_css=r'''
  .goalbox { margin-top: 14px; padding: 12px 14px; border-radius: 20px; background: #fff; color: var(--text); font-weight: 900; font-size: 18px; line-height: 1.6; }
  .goalbox .w { display: none; margin: 2px 2px; padding: 2px 10px; border-radius: 999px; background: var(--sun); color: #3b2c00; font-size: 15px; }
  .game[data-w1="1"] .goalbox .w1, .game[data-w2="1"] .goalbox .w2, .game[data-w3="1"] .goalbox .w3 { display: inline-block; animation: popin .35s cubic-bezier(.2,1.5,.4,1) both; }
  .friends { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px; margin-top: 14px; }
  .fr { padding: 8px 4px 10px; border-radius: 18px; background: rgba(255,255,255,.18); }
  .who { font-size: 30px; line-height: 1.2; }
  .think { position: relative; margin-top: 6px; padding: 8px 4px; border-radius: 16px; background: #fff; color: var(--text); font-weight: 900; }
  .think::before { content: ""; position: absolute; top: -7px; left: 50%; width: 12px; height: 12px; margin-left: -6px; border-radius: 50%; background: #fff; }
  .pic { display: block; font-size: 38px; line-height: 1.15; }
  .pic.chg { animation: popin .4s cubic-bezier(.2,1.6,.4,1); }
  .days { display: block; font-size: 14px; }
  .d { font-size: 18px; color: var(--c1d); }
  .same { display: flex; align-items: center; gap: 10px; margin: 14px auto 0; max-width: 380px; font-weight: 900; font-size: 14px; }
  .sbar { flex: 1; height: 14px; border-radius: 999px; background: rgba(255,255,255,.28); overflow: hidden; }
  .sbar i { display: block; width: 0; height: 100%; border-radius: 999px; background: var(--sun); transition: width .5s cubic-bezier(.2,1.2,.4,1); }
  .g-hint2 { margin-top: 12px; font-size: 14px; font-weight: 800; opacity: .95; }
  .chips { margin-top: 8px; }
  .chip { font-size: 16px; min-height: 52px; padding: 10px 16px; }
  .game .again { display: none; margin-top: 12px; }
  .game:not([data-k="0"]) .again { display: inline-flex; }
  .game[data-k="0"] .m0, .game[data-k="1"] .m1, .game[data-k="2"] .m2, .game[data-k="3"] .m3 { display: block; }
''',
  dark_css=r'''  html[data-theme="dark"] .goalbox, html[data-theme="dark"] .game .think { background: #22242f; color: #f4f0fa; }
  html[data-theme="dark"] .game .think::before { background: #22242f; }
  html[data-theme="dark"] .game .d { color: #c2adff; }''',
  game_js=r'''/* ✂️ 旅の言葉ハサミ：言葉を足すほど、3人の頭の中の旅がそろっていく */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var pics = [g.querySelector('.pa'), g.querySelector('.pb'), g.querySelector('.pc')];
  var ds = [g.querySelector('.da'), g.querySelector('.db'), g.querySelector('.dc')];
  var chips = [].slice.call(g.querySelectorAll('.chip')), bar = g.querySelector('.sbar i');
  var w = { 1: 0, 2: 0, 3: 0 };
  POPFN
  function picOf(i) {
    var warm = w[1], sea = w[2];
    if (i === 0) return '🏖️';
    if (i === 1) return warm && sea ? '🏖️' : warm ? '🏖️' : sea ? '🚢' : '🏙️';
    return warm && sea ? '🏖️' : warm ? '🏜️' : sea ? '🧊' : '🏔️';
  }
  function dayOf(i) { return w[3] ? 2 : [1, 7, 3][i]; }
  function draw(changed) {
    var k = w[1] + w[2] + w[3], p = [], d = [];
    for (var i = 0; i < 3; i++) {
      var np = picOf(i), nd = dayOf(i);
      if (pics[i].textContent !== np || ds[i].textContent !== String(nd)) {
        pics[i].textContent = np; ds[i].textContent = String(nd);
        if (changed) { pics[i].classList.remove('chg'); void pics[i].offsetWidth; pics[i].classList.add('chg'); }
      }
      p.push(np); d.push(nd);
    }
    var pairs = 0;
    [[0, 1], [0, 2], [1, 2]].forEach(function (q) { if (p[q[0]] === p[q[1]]) pairs++; if (d[q[0]] === d[q[1]]) pairs++; });
    bar.style.width = Math.max(4, pairs / 6 * 100) + '%';
    g.setAttribute('data-k', String(k));
    for (var j = 1; j <= 3; j++) g.setAttribute('data-w' + j, String(w[j]));
    chips.forEach(function (c) { c.disabled = !!w[c.getAttribute('data-w')]; });
    if (k === 3 && changed) pop(g.querySelector('.friends'), ['🏖️', '🐧', '✨', '🧳'], 18);
  }
  chips.forEach(function (c) {
    c.addEventListener('click', function () { var j = c.getAttribute('data-w'); if (w[j]) return; w[j] = 1; draw(true); });
  });
  g.querySelector('.again').addEventListener('click', function () { w = { 1: 0, 2: 0, 3: 0 }; draw(true); });
  draw(false);
})();'''.replace('POPFN', POP),
  sec='速く、うまくなる技術', exkind='友達との旅行の計画',
  core='ゴールはあいまいな言葉のままにしない。誰が読んでもズレない言葉に分ける。',
  weight='段取りのコツ', look='むらさきと水色。旅の言葉を足していく',
  gamedesc='✂️ 旅の言葉ハサミ：ゴールは「楽しい旅行」だけ。3匹（ペンギン・シロクマ・アザラシ）の頭の中は 🏖️1日／🏙️7日／🏔️3日 とバラバラ。「☀️暖かい」「🌊海の近く」「🗓️2日間」を押してゴールに足すと、頭の中の絵と日数が少しずつそろっていく（海だけ足すとアザラシは🧊を思い浮かべる、というオチつき）。3つそろうと全員 🏖️2日で「同じ絵」メーターが満タン＋紙吹雪。',
  prompt='An extremely cute, chubby round penguin with a gentle face and a plain white belly, made as a layered cut paper diorama, sitting on top of a small realistic vintage travel suitcase with leather straps, a soft paper sea and paper hills layered behind. Bright simple violet and aqua background with soft depth. Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering.',
  combo='ペンギン × 切り絵のジオラマ × 旅行かばん',
))

# ─────────────────────────────── 546 match-the-picture-first
ARTS.append(dict(
  slug='match-the-picture-first', seq=546,
  title_en='Before you start, write 3 lines and show them to the person who asked',
  title_ja='始める前に3行を書いて、頼んだ人に見せる',
  label_en='Show 3 Lines', label_ja='3行を見せる',
  h1e='🎂', mood=['lift', 'laugh'], tags=['psychology', 'productivity', 'friends'],
  alt='A chubby hand-embroidered felt penguin holding a small note card next to a real strawberry shortcake',
  pal=dict(bg='#fff6f8', c1='#e83e8c', c2='#8a5a44', sun='#ffd6e5', c1d='#c2185b', c1l='#ff9cc8',
           game='linear-gradient(150deg, #e83e8c 0%, #f06292 50%, #a1673f 100%)',
           glow1='rgba(232,62,140,.16)', glow2='rgba(138,90,68,.14)', glow3='rgba(255,214,229,.45)', photobg='#ffe6ef'),
  S=[('頼まれたことは、すぐに始めないほうがいいそうです。', 'It is said that you should not start a request right away.'),
     ('まず、ゴール・壁・解決策の3行を書いて、頼んだ人に見せます。', 'First, write 3 lines (goal, wall, fix) and show them to the person who asked.'),
     ('そこで、お互いの頭の中の絵のズレをなくします。', 'There, you remove the gap between the pictures in your heads.'),
     ('そうすると、あとから「そうじゃない」と言われることが、ほとんどなくなります。', 'Then you almost never hear "That is not it" later.')],
  layout=[('✋', 'Wait First', 'まず待つ', ['1'], None),
          ('📝', '3 Lines', '3行', ['2'], None),
          'GAME',
          ('🖼️', 'No Gap', 'ズレをなくす', ['3'], None),
          ('✅', 'No Redo', 'やり直しなし', ['!4'], None)],
  game_name='ケーキのイメージ合わせ',
  game_html=r'''  <section class="game" data-s="idle" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">{{Bake a birthday cake for a friend|友達の誕生日ケーキを作ろう}}</div>
    <div class="heads">
      <div class="head hf"><div class="who">{{💭 In my friend's head|💭 友達の頭の中}}</div><div class="cake" aria-hidden="true"><span class="fl ff">🍓</span><span class="ck">🎂</span></div></div>
      <div class="head hm"><div class="who">{{💭 In my head|💭 私の頭の中}}</div><div class="cake" aria-hidden="true"><span class="fl mf">🍫</span><span class="ck">🎂</span></div></div>
    </div>
    <div class="oven"><i></i></div>
    <div class="note">
      <div class="nl">{{🎯 Goal: a cake my friend loves|🎯 ゴール：友達が大好きなケーキ}}</div>
      <div class="nl">{{🧱 Wall: I do not know the flavor.|🧱 壁：好きな味を知らない。}}</div>
      <div class="nl">{{🔧 Fix: ask before I bake.|🔧 解決策：焼く前に聞く。}}</div>
      <div class="reply">{{📮 Friend: "🍓 Strawberry, please!"|📮 友達：「🍓 いちごがいいな！」}}</div>
    </div>
    <div class="msg">
      <div class="m-idle">{{The birthday is tomorrow. What do you do first?|誕生日は明日。まず何をする？}}</div>
      <div class="m-bake">{{🔥 Baking…|🔥 焼いています…}}</div>
      <div class="m-wrong">{{😮 Friend: "Oh… that is not it."|😮 友達：「あ…そうじゃないんだけど」}}</div>
      <div class="m-done">{{🎉 Friend: "Yes! This is it!"|🎉 友達：「そう、これこれ！」}}</div>
    </div>
    <div class="score"><span class="sc-l">{{⏱️ Time used:|⏱️ かかった時間：}}</span> <span class="h">0</span> <span class="hu">{{hours|時間}}</span> · <span class="sc-l2">{{↺ Redos:|↺ やり直し：}}</span> <span class="rd">0</span></div>
    <div class="g-row">
      <button type="button" class="gbtn b-now">{{🔨 Start right away|🔨 すぐ作り始める}}</button>
      <button type="button" class="gbtn b-lines">{{📝 Send 3 lines first|📝 先に3行を送る}}</button>
      <button type="button" class="gbtn wide b-bake">{{🎂 Now bake it!|🎂 さあ、焼こう！}}</button>
      <button type="button" class="gbtn ghost again">{{↺ Start over|↺ 最初から}}</button>
    </div>
  </section>''',
  game_css=r'''
  .heads { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; margin-top: 14px; }
  .head { padding: 10px 8px 12px; border-radius: 22px; background: rgba(255,255,255,.96); color: var(--text); }
  .who { font-size: 13.5px; font-weight: 900; line-height: 1.35; }
  .cake { margin-top: 6px; font-size: 40px; line-height: 1.1; white-space: nowrap; }
  .cake .fl { display: inline-block; font-size: 30px; vertical-align: top; transition: transform .3s; }
  .cake .fl.chg { animation: popin .45s cubic-bezier(.2,1.6,.4,1); }
  .hf .cake { filter: blur(7px); transition: filter .5s; }
  .game[data-s="note"] .hf .cake, .game[data-s="bake2"] .hf .cake, .game[data-s="done"] .hf .cake { filter: none; }
  .game[data-s="done"] .head { box-shadow: 0 0 0 4px #7ee0a8; }
  .oven { height: 12px; margin: 14px auto 0; max-width: 360px; border-radius: 999px; background: rgba(255,255,255,.28); overflow: hidden; }
  .oven i { display: block; width: 0; height: 100%; border-radius: 999px; background: #ffd27a; }
  .oven.go i { width: 100%; transition: width 1.1s linear; }
  .note { display: none; margin: 12px auto 0; max-width: 420px; padding: 12px 14px; border-radius: 16px; background: #fffbe6; color: #3a2f20;
    text-align: left; font-weight: 900; font-size: 15px; line-height: 1.55; transform: rotate(-.6deg); }
  .game[data-s="note"] .note, .game[data-s="bake2"] .note, .game[data-s="done"] .note { display: block; animation: popin .4s both; }
  .reply { margin-top: 6px; padding-top: 6px; border-top: 2px dashed #e8d9a8; color: var(--c1d); }
  .score { margin-top: 8px; font-size: 14px; font-weight: 900; opacity: .95; }
  .score .h, .score .rd { font-size: 18px; }
  .game .gbtn { display: none; }
  .game[data-s="idle"] .b-now, .game[data-s="idle"] .b-lines, .game[data-s="wrong"] .b-now, .game[data-s="wrong"] .b-lines,
  .game[data-s="note"] .b-bake, .game[data-s="done"] .again, .game[data-s="wrong"] .again { display: inline-flex; }
  .game[data-s="idle"] .m-idle, .game[data-s="bake1"] .m-bake, .game[data-s="bake2"] .m-bake, .game[data-s="wrong"] .m-wrong, .game[data-s="done"] .m-done { display: block; }
  .game[data-s="wrong"] .hm { animation: shake .45s ease; }
''',
  dark_css=r'''  html[data-theme="dark"] .game .head { background: #22242f; color: #f4f0fa; }
  html[data-theme="dark"] .game .note { background: #3a3320; color: #ffe9a8; }
  html[data-theme="dark"] .game .reply { color: #ff9cc8; border-top-color: rgba(255,233,168,.3); }''',
  game_js=r'''/* 🎂 ケーキのイメージ合わせ：すぐ作るとズレてやり直し。3行を送ると頭の中の絵がそろう */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var oven = g.querySelector('.oven'), mf = g.querySelector('.mf'), hEl = g.querySelector('.h'), rdEl = g.querySelector('.rd');
  var WRONG = ['🍫', '🍋', '🍵'], tries = 0, hours = 0, redo = 0, t = 0;
  POPFN
  function set(s) { g.setAttribute('data-s', s); }
  function bake(next) {
    oven.classList.remove('go'); void oven.offsetWidth; oven.classList.add('go');
    hours += 3; hEl.textContent = String(hours);
    t = setTimeout(next, 1200);
  }
  function flavor(e) { mf.textContent = e; mf.classList.remove('chg'); void mf.offsetWidth; mf.classList.add('chg'); }
  g.querySelector('.b-now').addEventListener('click', function () {
    flavor(WRONG[tries % WRONG.length]); tries++;
    set('bake1');
    bake(function () { redo++; rdEl.textContent = String(redo); set('wrong'); });
  });
  g.querySelector('.b-lines').addEventListener('click', function () { set('note'); setTimeout(function () { flavor('🍓'); }, 500); });
  g.querySelector('.b-bake').addEventListener('click', function () {
    set('bake2');
    bake(function () { set('done'); pop(g.querySelector('.heads'), ['🍓', '🎂', '🐧', '🎉'], 18); });
  });
  g.querySelector('.again').addEventListener('click', function () {
    clearTimeout(t); tries = 0; hours = 0; redo = 0; hEl.textContent = '0'; rdEl.textContent = '0';
    mf.textContent = '🍫'; oven.classList.remove('go'); set('idle');
  });
})();'''.replace('POPFN', POP),
  sec='速く、うまくなる技術', exkind='友達の誕生日ケーキ',
  core='始める前に、ゴール・壁・解決策の3行を書いて頼んだ人に見せ、イメージのズレをなくす。',
  weight='段取りのコツ', look='いちごピンクとチョコ色。ケーキの注文で遊べる',
  gamedesc='🎂 ケーキのイメージ合わせ：友達の頭の中（ぼかしてあって見えない）は🍓、私の頭の中は🍫。「🔨 すぐ作り始める」を押すと焼き上がるたびに「あ…そうじゃないんだけど」で、3時間ずつ時間とやり直しが増える（🍫→🍋→🍵）。「📝 先に3行を送る」を押すとメモ（ゴール・壁・解決策）が出て、友達から「🍓 いちごがいいな！」と返事。頭の中の絵がそろって、焼くと「そう、これこれ！」＋紙吹雪。',
  prompt='An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of hand-embroidered felt with visible stitches, holding a small blank note card in one flipper and standing next to a realistic strawberry shortcake on a white plate. Bright simple strawberry pink and soft chocolate brown background with soft depth. Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering.',
  combo='ペンギン × 手刺しゅうのフェルト × いちごのショートケーキ',
))
