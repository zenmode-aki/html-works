from gen import build

d = dict(
    slug="growth-is-a-tool", seq=539,
    title=("Growth is not the goal, it is a tool for what you want",
           "成長は目的じゃなく、やりたいことのための道具"),
    label=("Just a Tool", "成長は道具"),
    h1_emoji="⚙️",
    alt="A chubby hand-embroidered felt penguin turning a crank on a real small brass gear machine with three big gears",
    section="仕事との向き合い方（一般論）",
    message="成長は目的ではなく手段。「やりたいこと → 結果 → 成長」の順番で考える。",
    tone="素材の重さ：ふつう（考え方の順番）\n→ 見せ方：ポップに（ぶどう色とレモン色。3つのブロックを正しい順に入れると、機械が動き出す）",
    game_ja="⚙️ 順番マシン：「📈 成長」「💛 やりたいこと」「🎯 結果」のブロックを押して、機械の1→2→3の穴に入れる。「やりたいこと → 結果 → 成長」の順なら歯車が回りだして、タイ旅行の例（タイを旅したい → 自分でごはんを注文したい → だから少しタイ語を覚える）が流れて紙ふぶき。ちがう順だと、歯車がガタガタ止まって「なんのための成長？」。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of hand-embroidered felt, "
            "happily turning the crank of a realistic small vintage brass machine with three large smooth brass gears. "
            "Bright simple grape purple and lemon yellow background with soft depth and cheerful light. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × 刺しゅうフェルト × 真ちゅうの歯車の機械",
    mood=["lift", "learn"], tags=["psychology", "mindset", "study"],
    pal=dict(bg="#faf6ff", muted="#706487", acc="#7a3fe0", acc2="#f0a500", shadow="rgba(110,60,200,.16)",
             r1="rgba(255,214,60,.3)", r2="rgba(122,63,224,.16)", r3="rgba(80,200,170,.14)",
             h1="#2a1650", photo="#efe4ff", big="#6a31cc", bigdark="#cdb4ff",
             game="linear-gradient(160deg, #7a3fe0 0%, #b04fd8 50%, #f0a500 115%)"),
    cards=[
        dict(emoji="🧰", label=("A Tool", "道具"),
             s=[("It is said growth is not a goal but a tool.",
                 "成長は、目的ではなく手段だそうです。")]),
        dict(emoji="🔢", label=("The Order", "順番"),
             s=[("The order is \"what I want → a result → growth.\"",
                 "順番は「やりたいこと → 結果 → 成長」です。"),
                ("For example, \"I want to watch baseball in Korea\" → \"I want to cheer in Korean\" → \"So I study Korean.\"",
                 "たとえば「韓国で野球を見たい」→「韓国語で応援したい」→「だから韓国語を勉強する」。")]),
        dict(emoji="🌱", label=("Grows Naturally", "自然に伸びる"), big=True,
             s=[("It is said your skills grow naturally when it is something you love.",
                 "夢中になれることなら、スキルは自然に伸びるそうです。")]),
    ],
    game_after=2,
    game_note="順番マシン（やりたいこと→結果→成長の順に入れると、歯車が回る）",
    game_html="""  <section class="game" data-n="0" data-ok="" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">The order machine</div>
    <div class="game-hint">Tap the 3 blocks to put them into the machine. Which order makes it run?</div>
    <div class="tray">
      <button type="button" class="btn blk" data-k="g" data-used="0">📈 Growth</button>
      <button type="button" class="btn blk" data-k="w" data-used="0">💛 What I want</button>
      <button type="button" class="btn blk" data-k="r" data-used="0">🎯 A result</button>
    </div>
    <div class="mach">
      <div class="gears" aria-hidden="true"><span class="gr gr1">⚙️</span><span class="gr gr2">⚙️</span></div>
      <div class="slots">
        <div class="slot" data-v=""><span class="sn">1</span><span class="cv cw">💛 What I want</span><span class="cv cr">🎯 A result</span><span class="cv cg">📈 Growth</span></div>
        <div class="arw" aria-hidden="true">↓</div>
        <div class="slot" data-v=""><span class="sn">2</span><span class="cv cw">💛 What I want</span><span class="cv cr">🎯 A result</span><span class="cv cg">📈 Growth</span></div>
        <div class="arw" aria-hidden="true">↓</div>
        <div class="slot" data-v=""><span class="sn">3</span><span class="cv cw">💛 What I want</span><span class="cv cr">🎯 A result</span><span class="cv cg">📈 Growth</span></div>
      </div>
    </div>
    <div class="res">
      <div class="rs0">Put all 3 blocks in.</div>
      <div class="rs-ok">
        <div class="okh">✨ It runs! For example:</div>
        <div class="chain"><span class="ch1">🏝️ I want to travel in Thailand.</span><span class="ch2">🍜 I want to order food by myself.</span><span class="ch3">📈 So I learn a little Thai.</span></div>
      </div>
      <div class="rs-ng">⚙️ Clunk! The gears stop. "Growth… but for what?"</div>
    </div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Take the blocks out</button></div>
  </section>""",
    css="""
  /* ⚙️ 順番マシン */
  .tray { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; max-width: 440px; margin: 14px auto 0; }
  .blk { padding: 8px 6px; font-size: 15px; min-height: 58px; }
  .blk[data-used="1"] { opacity: .3; transform: scale(.92); pointer-events: none; }
  .mach { position: relative; max-width: 440px; margin: 14px auto 0; padding: 14px 14px 14px 62px; border-radius: 24px; background: rgba(255,255,255,.18);
    border: 3px dashed rgba(255,255,255,.55); }
  .gears { position: absolute; left: 10px; top: 50%; margin-top: -48px; display: grid; gap: 8px; }
  .game .gr { display: inline-block; font-size: 36px; line-height: 1; }
  .game[data-ok="1"] .gr1 { animation: spin 1.6s linear infinite; }
  .game[data-ok="1"] .gr2 { animation: spin 1.6s linear infinite reverse; }
  .game[data-ok="0"] .gr { animation: shake .4s ease 2; }
  @keyframes spin { to { transform: rotate(360deg); } }
  .slots { display: grid; gap: 4px; }
  .slot { display: flex; align-items: center; gap: 10px; min-height: 52px; padding: 8px 12px; border-radius: 16px; background: rgba(0,0,0,.14); text-align: left;
    transition: background .3s ease; }
  .sn { display: grid; place-items: center; flex: 0 0 30px; height: 30px; border-radius: 50%; background: rgba(255,255,255,.3); font-size: 15px; font-weight: 900; }
  .cv { display: none; font-size: 16px; font-weight: 900; }
  .slot[data-v="w"] .cw, .slot[data-v="r"] .cr, .slot[data-v="g"] .cg { display: inline; animation: boing .35s ease; }
  .slot:not([data-v=""]) { background: #fff; color: #2a1650; }
  .slot:not([data-v=""]) .sn { background: #efe4ff; }
  .game[data-ok="0"] .slot:not([data-v=""]) { background: #ffd6d6; }
  .game[data-ok="1"] .slot:not([data-v=""]) { background: #fff5c2; }
  .arw { font-size: 16px; font-weight: 900; line-height: 1; opacity: .8; }
  .res { max-width: 440px; margin: 12px auto 0; min-height: 50px; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .res > div { display: none; }
  .game[data-ok=""] .rs0, .game[data-ok="0"] .rs-ng { display: block; }
  .game[data-ok="0"] .rs-ng { animation: shake .45s ease; }
  .game[data-ok="1"] .rs-ok { display: block; animation: boing .5s ease; }
  .chain { display: grid; gap: 6px; margin-top: 8px; }
  .chain > span { display: block; padding: 8px 12px; border-radius: 14px; background: #fff; color: #4a2a90; font-size: 15px; }
  .ctrl { margin-top: 12px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
""",
    dark="""  html[data-theme="dark"] .slot:not([data-v=""]) { background: #2b2d3a; color: #efe4ff; }
  html[data-theme="dark"] .slot:not([data-v=""]) .sn { background: #3f3460; }
  html[data-theme="dark"] .game[data-ok="0"] .slot:not([data-v=""]) { background: #4a2626; }
  html[data-theme="dark"] .game[data-ok="1"] .slot:not([data-v=""]) { background: #4a3c12; }
  html[data-theme="dark"] .chain > span { background: #2b2d3a; color: #d9c8ff; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var slots = [].slice.call(g.querySelectorAll('.slot')), blks = [].slice.call(g.querySelectorAll('.blk')), n = 0;
  blks.forEach(function (b) {
    b.addEventListener('click', function () {
      if (n >= 3 || b.getAttribute('data-used') === '1') return;
      slots[n].setAttribute('data-v', b.getAttribute('data-k'));
      b.setAttribute('data-used', '1'); n++;
      g.setAttribute('data-n', String(n));
      if (n === 3) {
        var order = slots.map(function (s) { return s.getAttribute('data-v'); }).join('');
        var ok = order === 'wrg';
        g.setAttribute('data-ok', ok ? '1' : '0');
        if (ok && window.pengessoPop) {
          var r = g.querySelector('.mach').getBoundingClientRect();
          window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['⚙️', '✨', '🐧', '🎉', '💛'], 22);
        }
      }
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    n = 0; g.setAttribute('data-n', '0'); g.setAttribute('data-ok', '');
    slots.forEach(function (s) { s.setAttribute('data-v', ''); });
    blks.forEach(function (b) { b.setAttribute('data-used', '0'); });
  });
})();
""",
    ja={
        "The order machine": "順番マシン",
        "Tap the 3 blocks to put them into the machine. Which order makes it run?": "3つのブロックを押して、機械に入れてね。どの順番なら動くかな？",
        "📈 Growth": "📈 成長",
        "💛 What I want": "💛 やりたいこと",
        "🎯 A result": "🎯 結果",
        "Put all 3 blocks in.": "3つとも入れてね。",
        "✨ It runs! For example:": "✨ 動いた！たとえば：",
        "🏝️ I want to travel in Thailand.": "🏝️ タイを旅したい。",
        "🍜 I want to order food by myself.": "🍜 自分でごはんを注文したい。",
        "📈 So I learn a little Thai.": "📈 だから、少しタイ語を覚える。",
        "⚙️ Clunk! The gears stop. \"Growth… but for what?\"": "⚙️ ガタン！歯車が止まりました。「成長…って、なんのため？」",
        "↺ Take the blocks out": "↺ ブロックを出す",
    },
)
build(d)
