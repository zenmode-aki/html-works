from gen import build

TILES = "\n".join('        <span class="tile" aria-hidden="true">💡</span>' for _ in range(16))

d = dict(
    slug="quality-comes-from-quantity", seq=565, path="morningpages",
    title=("If you stop judging and make a lot, good ideas come out",
           "評価しないで量を出すと、たまにいいのが混ざる"),
    label=("Quantity First", "まず量"),
    h1_emoji="💡",
    alt="A chubby layered cut paper penguin happily holding a realistic glowing light bulb in front of a simple paper landscape",
    section="⑦「毎朝3ページ」",
    message="評価しないで量を出すと、たまにいいのが混ざる。質は量から生まれる。",
    tone="素材の重さ：ふつう（考え方のコツ）\n→ 見せ方：ポップに（ティールと黄色。アイデア製造機で遊べる）",
    game_ja="💡 アイデア製造機：「🙈 評価しない」か「🧐 1つずつ評価する」を選んで、6秒間「💡 アイデアを出す！」を連打。評価しないモードは、押すたびにアイデアが出て、6つに1つくらい⭐（いいアイデア）が混ざる。評価するモードは、1つ出すたびに審査員ペンギンが「うーん…完璧じゃない」と1秒止めて、ほとんどゴミ箱へ。終わると数が出て、2つのモードの⭐の数を並べて比べられる。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made as a layered cut paper diorama, "
            "proudly holding up a realistic warm glowing light bulb with both flippers. "
            "Bright simple teal and sunny yellow background with soft paper layers giving depth. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × 切り絵のジオラマ × 電球",
    mood=["lift", "think"], tags=["books", "productivity", "tips"],
    pal=dict(bg="#effbf8", muted="#5a7a75", acc="#0f9488", acc2="#ffb703", shadow="rgba(20,110,100,.16)",
             r1="rgba(255,200,60,.32)", r2="rgba(15,148,136,.20)", r3="rgba(120,140,255,.14)",
             h1="#0f3a36", photo="#dcf5ef", big="#0b7d72", bigdark="#86ead9",
             game="linear-gradient(150deg, #0fa596 0%, #1d7fd1 58%, #f9a826 100%)"),
    cards=[
        dict(emoji="📏", label=("Only 3 Pages", "3ページだけ"),
             s=[("In morning pages, the only goal is \"3 pages.\"",
                 "モーニングページの決まりは、「3ページ」だけです。")]),
        dict(emoji="🙈", label=("No Judging", "評価しない"),
             s=[("So you stop judging every idea that comes out.",
                 "だから、出てくるアイデアをいちいち評価しなくなります。")]),
        dict(emoji="💎", label=("Some Are Good", "いいのが混ざる"),
             s=[("Oliver Burkeman says that when you make a lot without judging, sometimes a good one comes out.",
                 "オリバー・バークマンさんによると、評価しないで量を出すと、たまにいいのが混ざるそうです。")]),
        dict(emoji="⭐", label=("From Quantity", "量から質"), big=True,
             s=[("Quality comes from quantity.", "質は、量から生まれるんです。")]),
        dict(emoji="🐧", label=("A Bit Painful", "耳が痛い"),
             s=[("As a perfectionist, this is a little painful for me to hear.",
                 "完璧主義の私には、ちょっと耳が痛い話です。")]),
    ],
    game_after=2,
    game_note="アイデア製造機（評価しないと、量から⭐が出る）",
    game_html="""  <section class="game" data-s="ready" data-mode="free" data-j="0" data-r="" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">The idea machine</div>
    <div class="game-hint">Choose a mode. Then tap 💡 as fast as you can for 6 seconds.</div>
    <div class="modes">
      <button type="button" class="btn mode m-free" data-mode="free">🙈 No judging</button>
      <button type="button" class="btn mode m-judge" data-mode="judge">🧐 Judge each one</button>
    </div>
    <div class="panel">
      <div class="top-row">
        <span class="clock"><span class="ck-e" aria-hidden="true">⏱️</span> <span class="tl">6.0</span></span>
        <span class="cnts"><span class="c-i">💡 Ideas:</span> <span class="ni">0</span> <span class="c-g">⭐ Good ones:</span> <span class="ng">0</span></span>
      </div>
      <div class="tray">
""" + TILES + """
      </div>
      <div class="judge"><span class="jd-e" aria-hidden="true">🧐</span> <span class="jd-t">Hmm… not perfect. Into the trash.</span></div>
    </div>
    <button type="button" class="make">
      <span class="k-go">💡 Make an idea!</span>
      <span class="k-wait">🧐 Judging…</span>
      <span class="k-again">↺ Again</span>
    </button>
    <div class="result">
      <div class="r-free">🎉 <span class="rn">0</span> <span class="r1">ideas, and</span> <span class="rg">0</span> <span class="r2">⭐! Make a lot, and good ones come.</span></div>
      <div class="r-judge">😵 <span class="r3">Only</span> <span class="rn">0</span> <span class="r4">ideas… Judging every one stopped your pen.</span></div>
    </div>
    <div class="board">
      <div><span class="b1">🙈 No judging:</span> <span class="bs-free">–</span> <span class="b-st">⭐</span></div>
      <div><span class="b2">🧐 Judging:</span> <span class="bs-judge">–</span> <span class="b-st">⭐</span></div>
    </div>
  </section>""",
    css="""
  /* 💡 アイデア製造機 */
  .modes { display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; margin-top: 14px; }
  .mode { flex: 1 1 140px; max-width: 210px; min-height: 52px; background: rgba(255,255,255,.18); color: #fff; box-shadow: inset 0 0 0 2px rgba(255,255,255,.6); }
  .game[data-mode="free"] .m-free, .game[data-mode="judge"] .m-judge { background: #fff; color: #0b5b53; box-shadow: 0 5px 0 rgba(0,0,0,.2); }
  .game[data-s="run"] .mode { opacity: .5; pointer-events: none; }
  .panel { position: relative; max-width: 420px; margin: 14px auto 0; padding: 12px; border-radius: 22px; background: rgba(255,255,255,.95); color: #23423f; }
  .top-row { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 6px; font-size: 14.5px; font-weight: 900; }
  .tl { display: inline-block; min-width: 2.2em; font-variant-numeric: tabular-nums; }
  .ni, .ng { display: inline-block; min-width: 1.5em; padding: 0 6px; border-radius: 999px; background: #e3f6f2; }
  .tray { display: grid; grid-template-columns: repeat(8, 1fr); gap: 4px; min-height: 84px; margin-top: 10px; }
  .game .tray .tile { display: grid; place-items: center; height: 38px; border-radius: 10px; background: #eef4f3; font-size: 22px; line-height: 1; opacity: 0; transform: scale(.4); }
  .game .tray .tile.on { opacity: 1; transform: none; transition: transform .25s cubic-bezier(.3,1.7,.5,1), opacity .15s ease; }
  .game .tray .tile.gold { background: #ffe58a; box-shadow: 0 0 0 2px #ffb703; }
  .game .tray .tile.trash { background: #e6e6ea; }
  .judge { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; gap: 6px; padding: 12px; border-radius: 22px;
    background: rgba(255,255,255,.94); font-size: 17px; font-weight: 900; opacity: 0; pointer-events: none; transition: opacity .15s ease; }
  .jd-e { font-size: 36px; }
  .game[data-j="1"] .judge { opacity: 1; }
  .game[data-j="1"] .jd-e { animation: shake .5s ease 2; }
  .make { display: block; width: min(320px, 100%); min-height: 96px; margin: 16px auto 0; border: 0; border-radius: 999px; cursor: pointer;
    font: inherit; font-size: clamp(22px, 6vw, 30px); font-weight: 900; color: #3b2c00; background: #ffd23f;
    box-shadow: 0 10px 0 #d99a00, 0 18px 30px rgba(0,0,0,.18); transition: transform .06s ease, box-shadow .06s ease;
    -webkit-tap-highlight-color: transparent; touch-action: manipulation; user-select: none; -webkit-user-select: none; }
  .make:active { transform: translateY(8px); box-shadow: 0 2px 0 #d99a00, 0 6px 14px rgba(0,0,0,.18); }
  .make:focus-visible { outline: 4px solid #fff; outline-offset: 4px; }
  .make span { display: none; }
  .game[data-s="ready"] .k-go, .game[data-s="run"][data-j="0"] .k-go, .game[data-j="1"] .k-wait, .game[data-s="end"] .k-again { display: inline; }
  .game[data-j="1"] .make { background: #e2e6ea; color: #556; box-shadow: 0 10px 0 #b6bcc4, 0 18px 30px rgba(0,0,0,.14); }
  .result { min-height: 58px; margin-top: 14px; }
  .result > div { display: none; font-size: 17px; font-weight: 900; line-height: 1.45; }
  .game[data-s="end"][data-r="free"] .r-free, .game[data-s="end"][data-r="judge"] .r-judge { display: block; animation: boing .5s ease; }
  .rn, .rg { display: inline-block; padding: 0 8px; border-radius: 999px; background: rgba(255,255,255,.28); }
  .board { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; max-width: 420px; margin: 8px auto 0; font-size: 14px; font-weight: 900; }
  .board > div { padding: 8px 6px; border-radius: 14px; background: rgba(255,255,255,.18); }
""",
    dark="""  html[data-theme="dark"] .panel { background: #22242f; color: #e6f5f2; }
  html[data-theme="dark"] .judge { background: rgba(34,36,47,.95); }
  html[data-theme="dark"] .tile { background: #2e3140; }
  html[data-theme="dark"] .tile.gold { background: #5a4a17; }
  html[data-theme="dark"] .tile.trash { background: #33343c; }
  html[data-theme="dark"] .ni, html[data-theme="dark"] .ng { background: #1d4a44; }
  html[data-theme="dark"] .game[data-mode="free"] .m-free, html[data-theme="dark"] .game[data-mode="judge"] .m-judge { background: #e6f5f2; color: #0b5b53; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var tiles = [].slice.call(g.querySelectorAll('.tile')), make = g.querySelector('.make');
  var tl = g.querySelector('.tl'), ni = g.querySelector('.ni'), ng = g.querySelector('.ng');
  var LEN = 6000, t0 = 0, tick = 0, judgeT = 0, ideas = 0, gold = 0, dry = 0, slot = 0;
  var best = { free: '–', judge: '–' };
  try { var sv = JSON.parse(localStorage.getItem('pengesso-quality-comes-from-quantity-board') || 'null'); if (sv) best = sv; } catch (e) {}
  function board() { g.querySelector('.bs-free').textContent = best.free; g.querySelector('.bs-judge').textContent = best.judge; }
  board();
  function clearTray() { tiles.forEach(function (t) { t.className = 'tile'; t.textContent = '💡'; }); slot = 0; }
  function addTile(kind) {
    var t = tiles[slot % tiles.length]; slot++;
    t.className = 'tile'; void t.offsetWidth;
    t.textContent = kind === 'gold' ? '⭐' : kind === 'trash' ? '🗑️' : '💡';
    t.className = 'tile on' + (kind === 'gold' ? ' gold' : kind === 'trash' ? ' trash' : '');
  }
  function count() { ni.textContent = ideas; ng.textContent = gold; }
  function ready() {
    clearInterval(tick); clearTimeout(judgeT); ideas = 0; gold = 0; dry = 0; count(); clearTray(); tl.textContent = '6.0';
    g.setAttribute('data-s', 'ready'); g.setAttribute('data-j', '0'); g.setAttribute('data-r', '');
  }
  function end() {
    clearInterval(tick); clearTimeout(judgeT); tl.textContent = '0.0';
    var m = g.getAttribute('data-mode');
    g.setAttribute('data-j', '0'); g.setAttribute('data-s', 'end'); g.setAttribute('data-r', m);
    [].forEach.call(g.querySelectorAll('.rn'), function (e) { e.textContent = ideas; });
    g.querySelector('.rg').textContent = gold;
    best[m] = String(gold); board();
    try { localStorage.setItem('pengesso-quality-comes-from-quantity-board', JSON.stringify(best)); } catch (e) {}
    if (m === 'free' && gold > 0 && window.pengessoPop) { var r = make.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top, ['⭐', '💡', '🐧', '✨'], 18); }
  }
  function isGold() { var hit = Math.random() < 1 / 6 || dry >= 7; dry = hit ? 0 : dry + 1; return hit; }
  [].forEach.call(g.querySelectorAll('.mode'), function (b) {
    b.addEventListener('click', function () { if (g.getAttribute('data-s') === 'run') return; g.setAttribute('data-mode', b.getAttribute('data-mode')); ready(); });
  });
  make.addEventListener('click', function () {
    var s = g.getAttribute('data-s');
    if (s === 'end') { ready(); return; }
    if (g.getAttribute('data-j') === '1') return;
    if (s === 'ready') {
      g.setAttribute('data-s', 'run'); t0 = Date.now();
      tick = setInterval(function () {
        var left = Math.max(0, LEN - (Date.now() - t0));
        tl.textContent = (left / 1000).toFixed(1);
        if (left <= 0) end();
      }, 100);
    }
    if (g.getAttribute('data-mode') === 'free') {
      var hit = isGold(); ideas++; if (hit) gold++;
      addTile(hit ? 'gold' : 'idea'); count();
    } else {
      g.setAttribute('data-j', '1');
      judgeT = setTimeout(function () {
        if (g.getAttribute('data-s') !== 'run') return;
        var keep = Math.random() < 1 / 12;
        if (keep) { ideas++; gold++; addTile('gold'); } else addTile('trash');
        count(); g.setAttribute('data-j', '0');
      }, 1100);
    }
  });
  ready();
})();
""",
    ja={
        "The idea machine": "アイデア製造機",
        "Choose a mode. Then tap 💡 as fast as you can for 6 seconds.": "モードを選んで、6秒間 💡 をできるだけ速く押してね。",
        "🙈 No judging": "🙈 評価しない",
        "🧐 Judge each one": "🧐 1つずつ評価する",
        "💡 Ideas:": "💡 アイデア：",
        "⭐ Good ones:": "⭐ いいアイデア：",
        "Hmm… not perfect. Into the trash.": "うーん…完璧じゃない。ゴミ箱へ。",
        "💡 Make an idea!": "💡 アイデアを出す！",
        "🧐 Judging…": "🧐 審査中…",
        "↺ Again": "↺ もう一回",
        "ideas, and": "個のアイデアと",
        "⭐! Make a lot, and good ones come.": "個の⭐！たくさん出すと、いいのが混ざる。",
        "Only": "アイデアは",
        "ideas… Judging every one stopped your pen.": "個だけ…1つずつ評価したら、ペンが止まっちゃった。",
        "🙈 No judging:": "🙈 評価しない：",
        "🧐 Judging:": "🧐 評価する：",
    },
)

if __name__ == "__main__":
    build(d)
