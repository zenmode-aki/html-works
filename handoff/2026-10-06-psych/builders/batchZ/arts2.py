from arts1 import POP
ARTS = []

# ─────────────────────────────── 547 the-immunity-map
ARTS.append(dict(
  slug='the-immunity-map', seq=547,
  title_en='You cannot change because not changing protects a hidden goal',
  title_ja='変われないのは、変わらないことで守っている「裏の目標」があるから',
  label_en='Immunity Map', label_ja='免疫マップ',
  h1e='🛡️', mood=['lift', 'think'], tags=['psychology', 'mindset', 'feelings'],
  alt='A chubby low-poly wood and paper penguin holding a real magnifying glass over a blank folded paper map',
  pal=dict(bg='#f4f6ff', c1='#3f51d8', c2='#20c997', sun='#ffe066', c1d='#2f3fbf', c1l='#a9b4ff',
           game='linear-gradient(155deg, #3f51d8 0%, #4f6ae0 45%, #20c997 100%)',
           glow1='rgba(63,81,216,.16)', glow2='rgba(32,201,151,.18)', glow3='rgba(255,224,102,.22)', photobg='#e8ebff'),
  S=[('ハーバード教育大学院の研究に、「免疫マップ」という考え方があります。', 'Research at the Harvard Graduate School of Education has an idea called the "immunity map."'),
     ('変わりたいのに変われないのは、変わらないことで守っている「裏の目標」があるからです。', 'When you want to change but cannot, it is because you protect a "hidden goal" by not changing.'),
     ('たとえば、人に頼りたいのに、何でも1人でやってしまう人がいます。', 'For example, some people want to ask others for help, but they do everything alone.'),
     ('その裏の目標は、「役に立つ自分を見せたい」かもしれません。', 'Their hidden goal may be "I want to show that I am useful."')],
  layout=[('🗺️', 'Immunity Map', '免疫マップ', ['1'], None),
          ('🛡️', 'Hidden Goal', '裏の目標', ['!2'], None),
          ('🤝', 'For Example', 'たとえば', ['3'], None),
          'GAME',
          ('🔦', 'The Reason', '本当の理由', ['4'], None)],
  game_name='見えない盾を見つけるマップ',
  game_html=r'''  <section class="game" data-n="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">{{Find the invisible shield|見えない盾を見つけよう}}</div>
    <div class="arena" aria-hidden="true">
      <span class="ring"></span>
      <span class="core">🐧</span>
      <span class="arw"><span class="ae">➡️</span><span class="al">{{change|変化}}</span></span>
    </div>
    <div class="msg">
      <div class="m0">{{Why does "change" bounce back? Tap card 1.|どうして「変化」がはね返されるの？1のカードを押してね。}}</div>
      <div class="m1">{{🔍 Something is blocking the change…|🔍 何かが変化をはね返している…}}</div>
      <div class="m4">{{🔍 Found it! The hidden goal was the invisible shield.|🔍 見つけた！裏の目標が、見えない盾だった。}}</div>
    </div>
    <div class="map">
      <button type="button" class="mc c1"><span class="num">1</span><span class="mh">{{🎯 What I want|🎯 変えたいこと}}</span><span class="mt">{{I want to ask others for help.|人に頼りたい。}}</span></button>
      <button type="button" class="mc c2"><span class="num">2</span><span class="mh">{{🏃 What I do|🏃 実際にしていること}}</span><span class="mt">{{But I do everything alone.|でも、何でも1人でやってしまう。}}</span></button>
      <button type="button" class="mc c3"><span class="num">3</span><span class="mh">{{🔦 Hidden goal|🔦 裏の目標}}</span><span class="mt">{{I want to show that I am useful.|役に立つ自分を見せたい。}}</span></button>
      <button type="button" class="mc c4"><span class="num">4</span><span class="mh">{{🧊 Big belief|🧊 強い思い込み}}</span><span class="mt">{{I am only worth something when I am useful.|役に立つときだけ、私には価値がある。}}</span></button>
    </div>
    <button type="button" class="gbtn ghost again">{{↺ Close the cards|↺ カードを閉じる}}</button>
  </section>''',
  game_css=r'''
  .arena { position: relative; height: 130px; margin: 14px auto 0; max-width: 360px; }
  .ring { position: absolute; left: 50%; top: 50%; width: 104px; height: 104px; margin: -52px 0 0 -52px; border-radius: 50%;
    border: 6px solid #fff; box-shadow: 0 0 22px rgba(255,255,255,.9), inset 0 0 18px rgba(255,255,255,.6); opacity: .06; transition: opacity .5s, transform .5s; }
  .game[data-n="4"] .ring { border-color: var(--sun); box-shadow: 0 0 26px var(--sun), inset 0 0 18px rgba(255,230,102,.7); transform: scale(1.06); }
  .core { position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); font-size: 46px; line-height: 1; }
  .arw { position: absolute; left: 0; top: 50%; margin-top: -16px; display: flex; align-items: center; gap: 4px; font-weight: 900; font-size: 13px;
    animation: throw 2s ease-in-out infinite; }
  .ae { font-size: 26px; line-height: 1; }
  @keyframes throw { 0% { transform: translateX(0); } 45% { transform: translateX(60px); } 52% { transform: translateX(46px) rotate(-12deg); } 70% { transform: translateX(10px); } 100% { transform: translateX(0); } }
  .map { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; margin-top: 12px; }
  .mc { min-height: 128px; border: 0; border-radius: 20px; background: rgba(255,255,255,.18); color: #fff; font: inherit; padding: 12px 12px;
    cursor: pointer; text-align: left; display: flex; flex-direction: column; align-items: flex-start; gap: 6px;
    -webkit-tap-highlight-color: transparent; touch-action: manipulation; transition: transform .16s ease, background .2s; }
  .mc .num { font-size: 22px; font-weight: 900; line-height: 1; }
  .mc .mh { font-size: 14px; font-weight: 900; line-height: 1.3; }
  .mc .mt { display: none; font-size: 15.5px; font-weight: 900; line-height: 1.42; }
  .mc.next { background: rgba(255,255,255,.32); box-shadow: inset 0 0 0 3px var(--sun); animation: nudge 1.4s ease-in-out infinite; }
  @keyframes nudge { 50% { box-shadow: inset 0 0 0 3px var(--sun), 0 0 18px rgba(255,224,102,.8); } }
  .mc[disabled] { cursor: default; }
  .mc.squash { transform: scaleX(0); animation: none; }
  .mc.open { background: #fff; color: var(--text); }
  .game .mc.open .mt { display: block; }
  .mc.open .num { color: var(--c1d); }
  .mc.c3.open { background: #fff6c2; }
  .game[data-n="0"] .m0, .game[data-n="1"] .m1, .game[data-n="2"] .m1, .game[data-n="3"] .m1, .game[data-n="4"] .m4 { display: block; }
  .game .again { display: none; margin-top: 14px; }
  .game[data-n="4"] .again { display: inline-flex; }
''',
  dark_css=r'''  html[data-theme="dark"] .game .mc.open { background: #22242f; color: #f4f0fa; }
  html[data-theme="dark"] .game .mc.c3.open { background: #3b3820; }
  html[data-theme="dark"] .game .mc.open .num { color: #a9b4ff; }''',
  game_js=r'''/* 🛡️ 見えない盾：カードを1→4の順に開くと、変化をはね返していた盾が見えてくる */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var cards = [].slice.call(g.querySelectorAll('.mc')), ring = g.querySelector('.ring'), n = 0;
  POPFN
  function mark() {
    cards.forEach(function (c, i) { c.classList.toggle('next', i === n); c.disabled = i !== n; });
    ring.style.opacity = String(0.06 + n * 0.235);
    g.setAttribute('data-n', String(n));
  }
  cards.forEach(function (c, i) {
    c.addEventListener('click', function () {
      if (i !== n) return;
      n += 1; mark();
      c.classList.add('squash');
      setTimeout(function () { c.classList.add('open'); c.classList.remove('squash'); }, 170);
      if (n === 4) setTimeout(function () { pop(ring, ['🛡️', '🔍', '✨', '🐧'], 18); }, 300);
    });
  });
  g.querySelector('.again').addEventListener('click', function () {
    n = 0; cards.forEach(function (c) { c.classList.remove('open', 'squash'); }); mark();
  });
  mark();
})();'''.replace('POPFN', POP),
  sec='自分を変える・挑戦する', exkind='人に頼れない、という一般的な例',
  core='変われないのは、変わらないことで守っている「裏の目標」があるから（免疫マップ）。',
  weight='心のしくみ', look='あい色とミント。見えない盾を見つける',
  gamedesc='🛡️ 見えない盾を見つけよう：ペンギンに「➡️ 変化」が何度も飛んでくるが、はね返される。免疫マップの4枚のカード（🎯変えたいこと：人に頼りたい → 🏃実際にしていること：何でも1人でやる → 🔦裏の目標：役に立つ自分を見せたい → 🧊強い思い込み：役に立つときだけ価値がある）を順番に開くたびに、見えなかった盾（光る輪）が少しずつ見えてくる。4枚開くと盾が金色に光って「見つけた！」。',
  prompt='An extremely cute, chubby round penguin with a gentle face and a plain white belly, made in low-poly 3D style from wood and folded paper, holding a realistic brass magnifying glass and looking curiously at a blank folded paper map spread on the floor. Bright simple indigo blue and mint green background with soft depth. Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering.',
  combo='ペンギン × ローポリの木と紙 × 虫めがね',
))

# ─────────────────────────────── 548 dig-one-more-level
ARTS.append(dict(
  slug='dig-one-more-level', seq=548,
  title_en='"Because I am anxious" is still the surface, so dig one more level',
  title_ja='「不安だから」「癖だから」はまだ表面。もう一段掘る',
  label_en='Dig Deeper', label_ja='もう一段',
  h1e='⛏️', mood=['lift', 'think'], tags=['psychology', 'mindset', 'feelings'],
  alt='A chubby brushed mohair penguin holding a real small garden shovel next to a glowing purple gemstone in soft soil',
  pal=dict(bg='#fff9f0', c1='#f08c00', c2='#9b40ff', sun='#ffe066', c1d='#b85f00', c1l='#ffc266',
           game='linear-gradient(160deg, #f08c00 0%, #d9650f 45%, #9b40ff 100%)',
           glow1='rgba(240,140,0,.18)', glow2='rgba(155,64,255,.16)', glow3='rgba(255,224,102,.24)', photobg='#fff0dc'),
  S=[('変われない理由を考えると、「癖だから」「不安だから」が出てきます。', 'When you think about why you cannot change, you find "it is a habit" or "I am anxious."'),
     ('でも、それはまだ表面です。', 'But that is still the surface.'),
     ('もう一段掘ると、「変わらないことで得ている目的」が出てきます。', 'If you dig one more level, you find "the goal you get by not changing."'),
     ('認めたくなくても、それを手放さない限り、変わりません。', 'Even if you do not want to admit it, you will not change until you let it go.')],
  layout=[('🤔', 'First Answers', '最初の答え', ['1'], None),
          ('🏝️', 'Only Surface', 'まだ表面', ['2'], None),
          'GAME',
          ('⛏️', 'One More Level', 'もう一段', ['!3'], None),
          ('🎈', 'Let It Go', '手放す', ['4'], None)],
  game_name='もう一段の穴掘り',
  game_html=r'''  <section class="game" data-d="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">{{Dig one more level|もう一段掘ろう}}</div>
    <div class="problem">{{😩 "I say yes to every invite, even when I am tired."|😩「疲れていても、誘いに全部『行く』と言ってしまう」}}</div>
    <div class="pit">
      <div class="ly l1" data-h="0"><span class="lk">{{Surface|表面}}</span><span class="lt">{{🪨 "It is just a habit."|🪨「ただの癖だから」}}</span><span class="dirt"></span></div>
      <div class="ly l2" data-h="0"><span class="lk">{{Still shallow|まだ浅い}}</span><span class="lt">{{🌀 "I am anxious."|🌀「不安だから」}}</span><span class="dirt"></span></div>
      <div class="ly l3" data-h="0"><span class="lk">{{The real reason|本当の理由}}</span><span class="lt">{{💎 "I want everyone to like me."|💎「みんなに好かれていたい」}}</span><span class="dirt"></span></div>
      <span class="digger" aria-hidden="true">🐧</span>
    </div>
    <div class="depth"><span class="dl">{{📏 Depth:|📏 深さ：}}</span> <span class="m">0</span> <span class="mu">{{m|メートル}}</span></div>
    <div class="msg">
      <div class="m0">{{Tap the shovel and dig!|シャベルを押して掘ろう！}}</div>
      <div class="m1">{{That is only the surface. Dig more!|それはまだ表面。もっと掘ろう！}}</div>
      <div class="m2">{{Still not the bottom… One more level!|まだ底じゃない…もう一段！}}</div>
      <div class="m3">{{💎 Found it! Now you know what to let go of.|💎 見つけた！手放すものが分かった。}}</div>
    </div>
    <div class="g-row">
      <button type="button" class="gbtn wide dig">{{⛏️ Dig!|⛏️ 掘る！}}</button>
      <button type="button" class="gbtn ghost again">{{↺ Fill the hole|↺ 穴を埋めなおす}}</button>
    </div>
  </section>''',
  game_css=r'''
  .problem { margin: 12px auto 0; max-width: 440px; padding: 10px 14px; border-radius: 18px; background: #fff; color: var(--text); font-weight: 900; font-size: 15.5px; line-height: 1.45; }
  .pit { position: relative; margin-top: 14px; border-radius: 22px; overflow: hidden; text-align: left; border-top: 10px solid #7cc94f; }
  .ly { position: relative; min-height: 70px; padding: 12px 64px 12px 14px; display: flex; flex-direction: column; justify-content: center; gap: 2px; font-weight: 900; }
  .l1 { background: #d9b48c; color: #3a2614; }
  .l2 { background: #a8754c; color: #fff; }
  .l3 { background: #5b3a29; color: #fff; }
  .lk { font-size: 11.5px; letter-spacing: .12em; text-transform: uppercase; opacity: .8; }
  .lt { font-size: 16px; line-height: 1.4; }
  .dirt { position: absolute; inset: 0; background: linear-gradient(170deg, #8a5a36, #6b4329); transition: opacity .35s; }
  .l2 .dirt { background: linear-gradient(170deg, #6b4329, #553422); }
  .l3 .dirt { background: linear-gradient(170deg, #4a2e1f, #3b2418); }
  .ly[data-h="1"] .dirt { opacity: .55; }
  .ly[data-h="2"] .dirt { opacity: 0; }
  .l3[data-h="2"] { background: radial-gradient(circle at 30% 50%, #9b40ff 0%, #5b3a29 70%); animation: glow 1.6s ease-in-out infinite alternate; }
  @keyframes glow { to { box-shadow: inset 0 0 34px rgba(214,170,255,.85); } }
  .digger { position: absolute; right: 14px; top: 16px; font-size: 34px; line-height: 1; transition: top .35s cubic-bezier(.2,1.4,.4,1); }
  .digger.hit { animation: shake .3s ease; }
  .depth { margin-top: 10px; font-size: 14px; font-weight: 900; }
  .depth .m { font-size: 20px; }
  .game[data-d="0"] .m0, .game[data-d="1"] .m1, .game[data-d="2"] .m2, .game[data-d="3"] .m3 { display: block; }
  .game .again { display: none; }
  .game[data-d="3"] .again { display: inline-flex; }
  .game[data-d="3"] .dig { display: none; }
''',
  dark_css=r'''  html[data-theme="dark"] .game .problem { background: #22242f; color: #f4f0fa; }''',
  game_js=r'''/* ⛏️ もう一段の穴掘り：1つの層を2回ずつ掘る。いちばん下に、本当の理由が光っている */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var lys = [].slice.call(g.querySelectorAll('.ly')), digger = g.querySelector('.digger'), mEl = g.querySelector('.m');
  var taps = 0;
  POPFN
  function draw() {
    var open = 0;
    lys.forEach(function (l, i) { var h = Math.max(0, Math.min(2, taps - i * 2)); l.setAttribute('data-h', String(h)); if (h === 2) open++; });
    g.setAttribute('data-d', String(open));
    mEl.textContent = (taps * 0.5).toFixed(1);
    var cur = lys[Math.min(2, Math.floor(Math.max(0, taps - 1) / 2))];
    digger.style.top = (taps === 0 ? 16 : cur.offsetTop + 18) + 'px';
  }
  g.querySelector('.dig').addEventListener('click', function () {
    if (taps >= 6) return;
    taps += 1; draw();
    digger.classList.remove('hit'); void digger.offsetWidth; digger.classList.add('hit');
    if (taps === 6) pop(lys[2], ['💎', '✨', '🐧', '⛏️'], 18);
  });
  g.querySelector('.again').addEventListener('click', function () { taps = 0; draw(); });
  draw();
})();'''.replace('POPFN', POP),
  sec='自分を変える・挑戦する', exkind='誘いを断れない、という一般的な例',
  core='「不安だから」「癖だから」はまだ表面。もう一段掘ると、変わらないことで得ている目的が出てくる。',
  weight='心のしくみ', look='オレンジとむらさき。穴を掘って宝石を見つける',
  gamedesc='⛏️ もう一段の穴掘り：「疲れていても、誘いに全部『行く』と言ってしまう」という悩み。「⛏️ 掘る！」を押すと、土が2回ずつ薄くなって層が出てくる（表面：🪨ただの癖だから → まだ浅い：🌀不安だから → 本当の理由：💎みんなに好かれていたい）。深さメーターが0.5mずつ増え、いちばん下の層がむらさきに光って紙吹雪。',
  prompt='An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of soft brushed mohair, holding a realistic small metal garden shovel and smiling at a single glowing purple gemstone half buried in smooth brown soil. Bright simple warm orange and violet background with soft depth. Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering.',
  combo='ペンギン × モヘア × 園芸用のシャベル',
))

# ─────────────────────────────── 549 change-like-braces
ARTS.append(dict(
  slug='change-like-braces', seq=549,
  title_en='Change yourself like braces: a small push for a long time',
  title_ja='自分を変えるのは歯の矯正と同じ。弱い力を長くかける',
  label_en='Small Push', label_ja='弱い力で長く',
  h1e='🦷', mood=['lift', 'energy'], tags=['psychology', 'mindset', 'tips'],
  alt='A chubby chenille yarn penguin gently watering a real small potted sapling tied to a straight bamboo stick',
  pal=dict(bg='#f2fffa', c1='#00a37a', c2='#ff6fb5', sun='#ffe14d', c1d='#007a5c', c1l='#7ee6c6',
           game='linear-gradient(150deg, #00a37a 0%, #2bbf95 45%, #ff6fb5 100%)',
           glow1='rgba(0,163,122,.16)', glow2='rgba(255,111,181,.16)', glow3='rgba(255,225,77,.22)', photobg='#e0f8ef'),
  S=[('自分を変えるのは、歯の矯正に似ているそうです。', 'It is said that changing yourself is like braces on your teeth.'),
     ('強い力で一気に動かそうとしても、すぐ元に戻ります。', 'If you try to move it at once with a strong push, it goes back soon.'),
     ('弱い力を、何か月も長くかけ続けます。', 'You keep a weak push on for many months.'),
     ('毎日、思い込みと逆のことを1つして、毎週「できた／できなかった」を振り返ります。', 'Every day, do 1 thing that is opposite to your belief, and every week, look back: "did it" or "did not."')],
  layout=[('🦷', 'Like Braces', '矯正と同じ', ['1'], None),
          ('💥', 'Strong Push', '強い力', ['2'], None),
          ('🐌', 'Weak and Long', '弱く長く', ['!3'], None),
          'GAME',
          ('📅', 'Every Week', '毎週', ['4'], None)],
  game_name='12週間の矯正カレンダー',
  game_html=r'''  <section class="game" data-s="idle" data-end="" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">{{Make the tooth straight|歯をまっすぐにしよう}}</div>
    <div class="mouth" aria-hidden="true"><span class="guide"></span><span class="tooth">🦷</span></div>
    <div class="tilt"><span class="tl">{{📐 Tilt:|📐 かたむき：}}</span> <span class="ag">30</span><span class="agu">°</span> · <span class="wl">{{📅 Week|📅 週}}</span> <span class="wkn">0</span><span class="wkt">/12</span></div>
    <div class="msg">
      <div class="m-idle">{{Try the big push, or stamp 1 week at a time.|強い力を試すか、1週間ずつスタンプを押してね。}}</div>
      <div class="m-big">{{💥 Boing! It went right back.|💥 ボヨン！すぐ元に戻った。}}</div>
      <div class="m-week">{{🐌 Small push. Slowly, slowly…|🐌 弱い力で、ゆっくり、ゆっくり…}}</div>
      <div class="m-good">{{🦷✨ Straight! It is OK to have some ❌ weeks.|🦷✨ まっすぐ！❌の週があっても大丈夫。}}</div>
      <div class="m-ok">{{🙂 Much straighter! Keep going a little longer.|🙂 かなりまっすぐ！もう少し続けよう。}}</div>
    </div>
    <div class="cal" aria-hidden="true"></div>
    <div class="g-row">
      <button type="button" class="gbtn b-ok">{{✅ Did it this week|✅ 今週はできた}}</button>
      <button type="button" class="gbtn b-ng">{{❌ Not this week|❌ 今週はできなかった}}</button>
      <button type="button" class="gbtn ghost b-big">{{💥 Big push|💥 強い力で一気に}}</button>
      <button type="button" class="gbtn ghost again">{{↺ Start over|↺ 最初から}}</button>
    </div>
  </section>''',
  game_css=r'''
  .mouth { position: relative; height: 150px; margin: 14px auto 0; max-width: 360px; border-radius: 24px; background: rgba(255,255,255,.96); }
  .guide { position: absolute; left: 50%; top: 14px; bottom: 14px; border-left: 4px dashed #9fe3cd; }
  .tooth { position: absolute; left: 50%; top: 50%; font-size: 76px; line-height: 1; --a: 30deg;
    transform: translate(-50%, -50%) rotate(var(--a)); transition: transform .6s cubic-bezier(.2,1.3,.4,1); }
  .tooth.boing { animation: boing 1.1s ease both; }
  @keyframes boing { 0% { transform: translate(-50%, -50%) rotate(var(--a)); } 22% { transform: translate(-50%, -50%) rotate(0deg) scale(1.08); }
    40% { transform: translate(-50%, -50%) rotate(-4deg); } 70% { transform: translate(-50%, -50%) rotate(calc(var(--a) + 6deg)); } 100% { transform: translate(-50%, -50%) rotate(var(--a)); } }
  .tilt { margin-top: 10px; font-size: 14px; font-weight: 900; }
  .tilt .ag, .tilt .wkn { font-size: 20px; }
  .cal { display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 6px; max-width: 380px; margin: 4px auto 0; }
  .wk { height: 44px; border-radius: 12px; background: rgba(255,255,255,.2); display: grid; place-items: center; font-weight: 900; font-size: 13px; }
  .wk.ok { background: #fff; }
  .wk.ng { background: rgba(255,255,255,.55); }
  .wk.cur { box-shadow: inset 0 0 0 3px var(--sun); }
  .wk .st { font-size: 22px; line-height: 1; }
  .wk .st.in { animation: popin .35s cubic-bezier(.2,1.8,.4,1) both; }
  .game .gbtn { display: none; }
  .game[data-s="idle"] .b-ok, .game[data-s="idle"] .b-ng, .game[data-s="idle"] .b-big, .game[data-s="big"] .b-ok, .game[data-s="big"] .b-ng, .game[data-s="big"] .b-big,
  .game[data-s="week"] .b-ok, .game[data-s="week"] .b-ng, .game[data-s="end"] .again, .game[data-s="big"] .again { display: inline-flex; }
  .game[data-s="idle"] .m-idle, .game[data-s="big"] .m-big, .game[data-s="week"] .m-week,
  .game[data-s="end"][data-end="good"] .m-good, .game[data-s="end"][data-end="ok"] .m-ok { display: block; }
''',
  dark_css=r'''  html[data-theme="dark"] .game .mouth, html[data-theme="dark"] .game .wk.ok { background: #22242f; }
  html[data-theme="dark"] .game .guide { border-left-color: #2e6b58; }''',
  game_js=r'''/* 🦷 12週間の矯正カレンダー：強い力はボヨンと戻る。弱い力（毎週のスタンプ）で少しずつまっすぐに */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var tooth = g.querySelector('.tooth'), agEl = g.querySelector('.ag'), wkEl = g.querySelector('.wkn'), cal = g.querySelector('.cal');
  var ang = 30, week = 0, cells = [];
  POPFN
  for (var i = 0; i < 12; i++) {
    var c = document.createElement('span'); c.className = 'wk';
    var s = document.createElement('span'); s.className = 'st'; s.textContent = String(i + 1);
    c.appendChild(s); cal.appendChild(c); cells.push(c);
  }
  function draw() {
    tooth.style.setProperty('--a', ang + 'deg');
    agEl.textContent = String(Math.round(ang)); wkEl.textContent = String(week);
    cells.forEach(function (c, i) { c.classList.toggle('cur', i === week); });
  }
  function stamp(ok) {
    if (week >= 12) return;
    var c = cells[week], s = c.firstChild;
    c.classList.add(ok ? 'ok' : 'ng'); s.textContent = ok ? '✅' : '❌'; s.classList.add('in');
    if (ok) ang = Math.max(0, ang - 3.5);
    week += 1; tooth.classList.remove('boing');
    g.setAttribute('data-s', week >= 12 ? 'end' : 'week');
    if (week >= 12) {
      var good = ang <= 6; g.setAttribute('data-end', good ? 'good' : 'ok');
      if (good) pop(tooth, ['🦷', '✨', '🐧', '🌱'], 18);
    }
    draw();
  }
  g.querySelector('.b-ok').addEventListener('click', function () { stamp(true); });
  g.querySelector('.b-ng').addEventListener('click', function () { stamp(false); });
  g.querySelector('.b-big').addEventListener('click', function () {
    tooth.classList.remove('boing'); void tooth.offsetWidth; tooth.classList.add('boing');
    g.setAttribute('data-s', 'big');
  });
  g.querySelector('.again').addEventListener('click', function () {
    ang = 30; week = 0; tooth.classList.remove('boing');
    cells.forEach(function (c, i) { c.className = 'wk'; c.firstChild.className = 'st'; c.firstChild.textContent = String(i + 1); });
    g.setAttribute('data-s', 'idle'); g.setAttribute('data-end', ''); draw();
  });
  draw();
})();'''.replace('POPFN', POP),
  sec='自分を変える・挑戦する', exkind='歯の矯正のたとえ',
  core='自分を変えるのは歯の矯正と同じ。弱い力を長くかけ続ける。',
  weight='心のしくみ', look='ミントとピンク。歯の矯正カレンダーで遊べる',
  gamedesc='🦷 12週間の矯正カレンダー：30°かたむいた歯。「💥 強い力で一気に」を押すと、一瞬まっすぐになってボヨンと元に戻る。「✅ 今週はできた」「❌ 今週はできなかった」で12週ぶんのカレンダーにスタンプを押すと、✅のたびに3.5°ずつまっすぐになる。12週後、6°以下なら「まっすぐ！❌の週があっても大丈夫」＋紙吹雪、そうでなければ「かなりまっすぐ！もう少し続けよう」。',
  prompt='An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of soft chenille yarn, gently watering a realistic small potted sapling that is softly tied with twine to a straight bamboo stick so it grows upright, using a small real watering can. Bright simple mint green and soft pink background with soft depth. Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering.',
  combo='ペンギン × シェニール糸 × 支柱をそえた苗木',
))

# ─────────────────────────────── 550 show-it-early
ARTS.append(dict(
  slug='show-it-early', seq=550,
  title_en='The more sure you feel, the earlier you should show it',
  title_ja='「絶対いける」と思ったものほど、早めに相手の反応を見る',
  label_en='Show It Early', label_ja='早めに見せる',
  h1e='🥄', mood=['lift', 'laugh'], tags=['psychology', 'productivity', 'friends'],
  alt='A chubby boucle wool penguin holding out a real wooden spoon with a small taste of curry next to a cooking pot',
  pal=dict(bg='#fff8f2', c1='#ef3b2d', c2='#2fb344', sun='#ffd43b', c1d='#c4281b', c1l='#ff9a90',
           game='linear-gradient(155deg, #ef3b2d 0%, #f76b1c 50%, #2fb344 100%)',
           glow1='rgba(239,59,45,.14)', glow2='rgba(47,179,68,.16)', glow3='rgba(255,212,59,.24)', photobg='#ffeee6'),
  S=[('自分が「絶対いける」と思ったものほど、相手には響かないことがあります。', 'The more you think "This will surely work," the more it may not reach the other person.'),
     ('だから、思い込みのまま1人で長く作り込まないようにします。', 'So I try not to spend a long time making it alone, with only my belief.'),
     ('料理なら、10時間かけたごちそうより、まず一口の味見です。', 'In cooking, a small taste first is better than a big dish that took 10 hours.'),
     ('早めに反応を見れば、直すのも簡単です。', 'If you see the reaction early, it is easy to fix.')],
  layout=[('🤩', 'Sure Things', '自信作', ['1'], None),
          ('⏳', 'Not Too Long', '作り込みすぎない', ['2'], None),
          ('🍛', 'Cooking Example', '料理の例', ['3'], None),
          'GAME',
          ('🥄', 'Easy Fix', '直すのも簡単', ['!4'], None)],
  game_name='いつ味見する？カレー計算機',
  game_html=r'''  <section class="game" data-s="set" data-r="" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">{{When do you give a taste?|いつ味見してもらう？}}</div>
    <div class="story">{{🍛 The curry takes 10 hours. Your friend cannot eat spicy food, but you do not know that yet.|🍛 カレーは10時間かかる。友達は辛いのが苦手。でも、私はまだそれを知らない。}}</div>
    <div class="stepper">
      <button type="button" class="gbtn sb minus" aria-label="−1">−</button>
      <div class="sval"><span class="tl">{{🥄 Give a taste after|🥄 味見は}}</span> <span class="th">1</span> <span class="tu">{{hours|時間後}}</span></div>
      <button type="button" class="gbtn sb plus" aria-label="+1">+</button>
    </div>
    <div class="track2" aria-hidden="true"><i class="fill"></i><span class="spoon">🥄</span><span class="potend">🍛</span></div>
    <div class="friend" aria-hidden="true"><span class="ff">🐧</span></div>
    <div class="msg">
      <div class="m-set">{{Choose the hour, then start cooking!|時間を選んで、作り始めよう！}}</div>
      <div class="m-cook">{{🔥 Cooking…|🔥 作っています…}}</div>
      <div class="m-taste">{{🥵 Friend: "Too spicy for me!"|🥵 友達：「私には辛すぎる！」}}</div>
      <div class="m-early">{{🎉 Early taste, easy fix! Less spice, and done.|🎉 早めの味見で、直すのも簡単！辛さを控えて完成。}}</div>
      <div class="m-mid">{{😅 OK, but you had to make many hours again.|😅 間に合ったけど、何時間ぶんも作り直し。}}</div>
      <div class="m-late">{{😭 A big pot of spicy curry… nobody can eat it. Start over!|😭 大鍋の辛いカレー…誰も食べられない。最初から！}}</div>
    </div>
    <div class="total"><span class="tt-l">{{⏱️ Total:|⏱️ 合計：}}</span> <span class="tt">0</span> <span class="tt-u">{{hours|時間}}</span><span class="tbar"><i></i></span></div>
    <div class="g-row">
      <button type="button" class="gbtn wide cook">{{🍛 Start cooking!|🍛 作り始める！}}</button>
      <button type="button" class="gbtn ghost again">{{↺ Try another hour|↺ ちがう時間で}}</button>
    </div>
  </section>''',
  game_css=r'''
  .story { margin: 12px auto 0; max-width: 440px; padding: 10px 14px; border-radius: 18px; background: rgba(255,255,255,.96); color: var(--text);
    font-weight: 900; font-size: 15px; line-height: 1.5; }
  .stepper { display: flex; align-items: center; justify-content: center; gap: 10px; margin-top: 14px; }
  .sb { width: 58px; min-width: 58px; padding: 0; font-size: 30px; }
  .sval { min-width: 0; padding: 8px 12px; border-radius: 16px; background: rgba(255,255,255,.2); font-weight: 900; font-size: 15px; line-height: 1.35; }
  .sval .th { font-size: 28px; }
  .track2 { position: relative; height: 30px; margin: 16px 34px 0 8px; border-radius: 999px; background: rgba(255,255,255,.28); }
  .fill { position: absolute; left: 0; top: 0; bottom: 0; width: 0; border-radius: 999px; background: #ffd43b; }
  .game.cooking .fill { transition: width 1.2s linear; }
  .spoon { position: absolute; top: -6px; font-size: 28px; line-height: 1; margin-left: -14px; transition: left .25s ease; }
  .potend { position: absolute; right: -32px; top: -4px; font-size: 28px; line-height: 1; }
  .friend { margin-top: 10px; font-size: 40px; line-height: 1; }
  .friend .ff { display: inline-block; transition: transform .3s; }
  .game[data-s="taste"] .friend .ff { animation: shake .45s ease; }
  .total { display: flex; align-items: center; justify-content: center; flex-wrap: wrap; gap: 6px 8px; font-size: 14px; font-weight: 900; }
  .total .tt { font-size: 22px; }
  .tbar { flex: 0 0 120px; height: 12px; border-radius: 999px; background: rgba(255,255,255,.28); overflow: hidden; }
  .tbar i { display: block; width: 0; height: 100%; background: #fff; border-radius: 999px; transition: width .5s; }
  .game .total { visibility: hidden; }
  .game[data-s="done"] .total { visibility: visible; }
  .game .cook, .game .again { display: none; }
  .game[data-s="set"] .cook { display: inline-flex; }
  .game[data-s="done"] .again { display: inline-flex; }
  .game[data-s="set"] .m-set, .game[data-s="cook"] .m-cook, .game[data-s="taste"] .m-taste,
  .game[data-s="done"][data-r="early"] .m-early, .game[data-s="done"][data-r="mid"] .m-mid, .game[data-s="done"][data-r="late"] .m-late { display: block; }
''',
  dark_css=r'''  html[data-theme="dark"] .game .story { background: #22242f; color: #f4f0fa; }''',
  game_js=r'''/* 🥄 いつ味見する？：味見が遅いほど、作り直す時間が増える（合計＝10時間＋味見までの時間） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var th = g.querySelector('.th'), spoon = g.querySelector('.spoon'), fill = g.querySelector('.fill'), ff = g.querySelector('.ff');
  var tt = g.querySelector('.tt'), tbar = g.querySelector('.tbar i'), minus = g.querySelector('.minus'), plus = g.querySelector('.plus');
  var h = 1, timers = [];
  POPFN
  function draw() {
    th.textContent = String(h); spoon.style.left = (h * 10) + '%';
    var free = g.getAttribute('data-s') === 'set';
    minus.disabled = !free || h <= 1; plus.disabled = !free || h >= 10;
  }
  minus.addEventListener('click', function () { if (h > 1) { h--; draw(); } });
  plus.addEventListener('click', function () { if (h < 10) { h++; draw(); } });
  function later(f, ms) { timers.push(setTimeout(f, ms)); }
  g.querySelector('.cook').addEventListener('click', function () {
    g.setAttribute('data-s', 'cook'); g.classList.add('cooking'); draw();
    fill.style.width = (h * 10) + '%';
    later(function () { g.setAttribute('data-s', 'taste'); ff.textContent = '🥵'; }, 1300);
    later(function () {
      var r = h <= 2 ? 'early' : h <= 7 ? 'mid' : 'late', total = 10 + h;
      ff.textContent = r === 'early' ? '😋' : r === 'mid' ? '😅' : '😭';
      tt.textContent = String(total); tbar.style.width = (total / 20 * 100) + '%';
      g.setAttribute('data-r', r); g.setAttribute('data-s', 'done');
      if (r === 'early') pop(ff, ['🍛', '🥄', '😋', '✨'], 16);
    }, 2500);
  });
  g.querySelector('.again').addEventListener('click', function () {
    timers.forEach(clearTimeout); timers = [];
    g.classList.remove('cooking'); fill.style.width = '0'; ff.textContent = '🐧'; tbar.style.width = '0';
    g.setAttribute('data-r', ''); g.setAttribute('data-s', 'set'); draw();
  });
  draw();
})();'''.replace('POPFN', POP),
  sec='自分を変える・挑戦する', exkind='友達のためのカレー',
  core='「絶対いける」と思ったものほど、思い込みで作り込まず、早めに相手の反応を見る。',
  weight='段取りのコツ', look='トマトの赤と緑。味見のタイミング計算機',
  gamedesc='🥄 いつ味見する？カレー計算機：カレーは10時間かかる。友達は辛いのが苦手（でもまだ知らない）。「−」「＋」で味見のタイミング（1〜10時間後）を選んで「作り始める！」。その時間で友達が「私には辛すぎる！」→ 作り直しの時間がのって合計（10＋味見の時間）が出る。1〜2時間なら「早めの味見で直すのも簡単！」＋紙吹雪、3〜7時間は「何時間ぶんも作り直し」、8〜10時間は「大鍋の辛いカレー…最初から！」。',
  prompt='An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of soft boucle wool, holding out a realistic wooden spoon with a tiny taste of golden curry toward the viewer, a real small enamel cooking pot on a stove top beside it. Bright simple tomato red and fresh green background with soft depth. Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering.',
  combo='ペンギン × ブークレ羊毛 × 木のスプーンと鍋',
))

# ─────────────────────────────── 551 failure-is-proof-you-tried
ARTS.append(dict(
  slug='failure-is-proof-you-tried', seq=551,
  title_en='A failure is proof that you tried without running away',
  title_ja='失敗は、逃げずに挑戦した証',
  label_en='Proof of Trying', label_ja='挑戦の証',
  h1e='⛸️', mood=['lift', 'energy'], tags=['psychology', 'mistakes', 'mindset'],
  alt='A chubby alpaca wool penguin wearing real small ice skates and smiling after a little fall on a smooth ice rink',
  pal=dict(bg='#f2f9ff', c1='#1a8fd6', c2='#ffb703', sun='#ffd23f', c1d='#0f6aa8', c1l='#8fd0ff',
           game='linear-gradient(155deg, #1a8fd6 0%, #43b0f0 50%, #ffb703 100%)',
           glow1='rgba(26,143,214,.16)', glow2='rgba(255,183,3,.20)', glow3='rgba(143,208,255,.30)', photobg='#e3f3ff'),
  S=[('失敗は、逃げずに挑戦した証です。', 'A failure is proof that you tried without running away.'),
     ('だから、ちょっと誇っていいと思います。', 'So I think you can be a little proud of it.'),
     ('本気でやった失敗は、あとで笑い話になって、後悔も残りません。', 'A failure from real effort becomes a funny story later, and it leaves no regret.'),
     ('転ぶたびに、転ばない方法を少しずつ覚えます。', 'Each time you fall, you learn a little about how not to fall.')],
  layout=[('🏅', 'The Proof', '証', ['!1'], None),
          ('😊', 'Be Proud', '誇っていい', ['2'], None),
          ('😂', 'No Regret', '後悔なし', ['3'], None),
          'GAME',
          ('⛸️', 'Fall and Learn', '転んで覚える', ['4'], None)],
  game_name='スケート練習',
  game_html=r'''  <section class="game" data-t="0" data-skip="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">{{Learn to skate|スケートを覚えよう}}</div>
    <div class="rink" aria-hidden="true">
      <span class="flag">🏁</span>
      <span class="sk"><span class="bang">💥</span><span class="pg">🐧</span></span>
    </div>
    <div class="medals" aria-hidden="true"><span class="md md1">🏅</span><span class="md md2">🏅</span><span class="md md3">🏅</span><span class="md md4">🏅</span><span class="md trophy">🏆</span></div>
    <div class="bal"><span class="bl">{{⚖️ Balance|⚖️ バランス}}</span><span class="bbar"><i></i></span></div>
    <div class="msg">
      <div class="m0">{{Tap "Try!" It is OK to fall.|「やってみる！」を押してね。転んでも大丈夫。}}</div>
      <div class="m1">{{💥 You fell! 🏅 +1 "I tried" medal.|💥 転んだ！🏅「挑戦した」メダル +1}}</div>
      <div class="m2">{{💥 Fell again, but a little farther! Learned: bend your knees.|💥 また転んだ。でも少し遠くまで！覚えた：ひざを曲げる。}}</div>
      <div class="m3">{{💥 Learned: look ahead, not down.|💥 覚えた：下じゃなくて前を見る。}}</div>
      <div class="m4">{{💥 Learned: arms out for balance.|💥 覚えた：腕を広げてバランスをとる。}}</div>
      <div class="m5">{{🏆 You glide! Every fall taught you something.|🏆 すいすい滑れた！転ぶたびに、何かを覚えていた。}}</div>
      <div class="m-skip">{{🙈 No falls. But no medals, and nothing learned.|🙈 転ばなかった。でもメダルもないし、何も覚えなかった。}}</div>
    </div>
    <div class="g-row">
      <button type="button" class="gbtn wide try">{{⛸️ Try!|⛸️ やってみる！}}</button>
      <button type="button" class="gbtn ghost skip">{{🙈 Do not try|🙈 やらない}}</button>
      <button type="button" class="gbtn ghost again">{{↺ Skate again|↺ もう一回すべる}}</button>
    </div>
  </section>''',
  game_css=r'''
  .rink { position: relative; height: 112px; margin-top: 14px; border-radius: 24px; overflow: hidden;
    background: linear-gradient(180deg, #f4fbff 0%, #d7f0ff 60%, #bfe6ff 100%); box-shadow: inset 0 -8px 0 rgba(26,143,214,.18); }
  .flag { position: absolute; right: 12px; top: 22px; font-size: 34px; line-height: 1; }
  .sk { position: absolute; left: 10px; bottom: 18px; width: 50px; height: 56px; }
  .sk.go { transition: left .9s cubic-bezier(.3,.6,.4,1); }
  .pg { position: absolute; left: 0; bottom: 0; width: 50px; text-align: center; font-size: 42px; line-height: 1; transform-origin: 50% 90%; transition: transform .25s ease; }
  .sk.fell .pg { transform: rotate(84deg) translateX(6px); }
  .sk.spin .pg { animation: spin .9s ease; }
  @keyframes spin { to { transform: rotate(360deg); } }
  .bang { position: absolute; left: 30px; top: -16px; font-size: 26px; line-height: 1; opacity: 0; transform: scale(.4); transition: opacity .2s, transform .25s cubic-bezier(.2,1.8,.4,1); }
  .sk.fell .bang { opacity: 1; transform: scale(1); }
  .medals { display: flex; justify-content: center; gap: 8px; margin-top: 12px; font-size: 30px; line-height: 1; }
  .md { opacity: .22; filter: grayscale(1); transform: scale(.8); transition: opacity .3s, filter .3s, transform .4s cubic-bezier(.2,1.8,.4,1); }
  .md.got { opacity: 1; filter: none; transform: none; }
  .bal { display: flex; align-items: center; gap: 10px; max-width: 360px; margin: 12px auto 0; font-weight: 900; font-size: 14px; }
  .bbar { flex: 1; height: 14px; border-radius: 999px; background: rgba(255,255,255,.3); overflow: hidden; }
  .bbar i { display: block; width: 10%; height: 100%; border-radius: 999px; background: #fff; transition: width .5s cubic-bezier(.2,1.2,.4,1); }
  .game .again { display: none; }
  .game[data-t="5"] .try, .game[data-t="5"] .skip, .game[data-skip="1"] .skip { display: none; }
  .game[data-t="5"] .again, .game[data-skip="1"] .again { display: inline-flex; }
  .game[data-skip="0"][data-t="0"] .m0, .game[data-t="1"] .m1, .game[data-t="2"] .m2, .game[data-t="3"] .m3, .game[data-t="4"] .m4, .game[data-t="5"] .m5,
  .game[data-skip="1"][data-t="0"] .m-skip { display: block; }
''',
  dark_css=r'''  html[data-theme="dark"] .game .rink { background: linear-gradient(180deg, #2a3442 0%, #24384a 60%, #1f3a52 100%); }''',
  game_js=r'''/* ⛸️ スケート練習：4回転ぶたびにメダルとコツが1つ増えて、5回目ですいすい滑れる */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var rink = g.querySelector('.rink'), sk = g.querySelector('.sk'), tryB = g.querySelector('.try'), skipB = g.querySelector('.skip');
  var mds = [].slice.call(g.querySelectorAll('.md')), bal = g.querySelector('.bbar i');
  var FALL = [0.28, 0.46, 0.64, 0.8], BAL = [10, 30, 50, 70, 88, 100], t = 0, busy = false, timers = [];
  POPFN
  function later(f, ms) { timers.push(setTimeout(f, ms)); }
  function toStart() { sk.classList.remove('go', 'fell', 'spin'); sk.style.left = '10px'; void sk.offsetWidth; }
  tryB.addEventListener('click', function () {
    if (busy || t >= 5) return;
    busy = true; tryB.disabled = true; skipB.disabled = true;
    g.setAttribute('data-skip', '0');
    toStart();
    var room = rink.clientWidth - 70, frac = t < 4 ? FALL[t] : 1;
    sk.classList.add('go'); sk.style.left = (10 + room * frac * (t < 4 ? 1 : 0.86)) + 'px';
    later(function () {
      if (t < 4) {
        sk.classList.add('fell');
        mds[t].classList.add('got');
        t += 1;
      } else {
        sk.classList.add('spin'); mds[4].classList.add('got'); t = 5;
        pop(sk, ['🏆', '⛸️', '🐧', '✨', '🏅'], 20);
      }
      g.setAttribute('data-t', String(t)); bal.style.width = BAL[t] + '%';
      busy = false; tryB.disabled = false; skipB.disabled = false;
    }, 950);
  });
  skipB.addEventListener('click', function () {
    if (busy) return;
    timers.forEach(clearTimeout); timers = [];
    t = 0; toStart(); mds.forEach(function (m) { m.classList.remove('got'); }); bal.style.width = '10%';
    g.setAttribute('data-t', '0'); g.setAttribute('data-skip', '1');
  });
  g.querySelector('.again').addEventListener('click', function () {
    timers.forEach(clearTimeout); timers = []; busy = false; tryB.disabled = false; skipB.disabled = false;
    t = 0; toStart(); mds.forEach(function (m) { m.classList.remove('got'); }); bal.style.width = '10%';
    g.setAttribute('data-t', '0'); g.setAttribute('data-skip', '0');
  });
})();'''.replace('POPFN', POP),
  sec='自分を変える・挑戦する', exkind='スケートの練習',
  core='失敗は逃げずに挑戦した証。転ぶたびに、転ばない方法を覚える。',
  weight='心の持ち方', look='氷の青と金色。スケートの練習で遊べる',
  gamedesc='⛸️ スケート練習：「⛸️ やってみる！」を押すと、ペンギンがすべり出して転ぶ（💥）。転ぶたびに「挑戦した」メダル🏅が1つ増え、少しずつ遠くまで行けて、コツ（ひざを曲げる・前を見る・腕を広げる）を1つずつ覚える。バランスメーターも増える。5回目はゴールまですいすい滑って回り、🏆＋紙吹雪。「🙈 やらない」を押すと「転ばなかった。でもメダルもないし、何も覚えなかった」。',
  prompt='An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of fluffy alpaca wool, wearing a pair of realistic small white leather ice skates with silver blades, sitting happily on smooth ice after a little fall and smiling, a small gold medal ribbon beside it. Bright simple icy blue and warm golden background with soft depth. Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering.',
  combo='ペンギン × アルパカ毛 × アイススケート靴',
))
