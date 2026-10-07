from gen import build

d = dict(
    slug="your-reading-pile-is-a-river", seq=584, url="https://www.oliverburkeman.com/river",
    title=("Your reading pile is not a bucket to empty, it is a river",
           "積ん読は「空にするバケツ」じゃなくて「流れる川」"),
    label=("Reading River", "積ん読の川"),
    h1_emoji="🌊",
    alt="A chubby chenille yarn penguin sitting on a grassy riverbank and lifting one real hardcover book out of a calm stream",
    section="⑯「積ん読は『バケツ』じゃなくて『川』」",
    message="積ん読は空にするバケツではなく流れる川。気になったものをときどきすくえば十分。",
    tone="素材の重さ：ふつう（情報との付き合い方）\n→ 見せ方：ポップに（川の青とミント。バケツと川を切り替えて遊べる）",
    game_ja="🌊 バケツ or 川：「🪣 バケツ」モードでは、本がどんどん降ってきてバケツにたまる。「📖 1冊読む」を押しても読むのに時間がかかるので、いつか必ずあふれて 😵「空にはできない」。「🌊 川」モードでは、本が川をぷかぷか流れていく。気になった本をタップしてすくうだけ（ほかは流れていってOK）。3冊すくえば「それで十分！」",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of soft chenille yarn with a velvety "
            "texture, sitting on a grassy riverbank and happily lifting one realistic hardcover book with a blue cloth cover out of a calm, "
            "clear shallow stream. Bright simple sky blue and fresh green background with soft depth. Realistic 3D render, studio lighting, "
            "shallow depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering."),
    combo="ペンギン × シェニール糸 × 川から拾い上げる本",
    mood=["lift"], tags=["books", "study", "tips"],
    pal=dict(bg="#f1f8ff", muted="#5d7590", acc="#1677d2", acc2="#ff8a3d", shadow="rgba(20,90,160,.16)",
             r1="rgba(43,156,240,.22)", r2="rgba(255,138,61,.18)", r3="rgba(143,214,148,.22)",
             h1="#0f2d4d", photo="#e0f0ff", big="#1167b8", bigdark="#9fd0ff",
             game="linear-gradient(160deg, #2b8ff0 0%, #22b8c3 60%, #7fd18a 100%)"),
    cards=[
        dict(emoji="📚", label=("Too Many Good", "いいものが多すぎ"),
             s=[("Your reading pile grows not because of too much useless information.", "読みたいものがたまるのは、いらない情報が多いからではありません。"),
                ("It grows because there are too many things you want to read.", "読みたいものが、多すぎるからです。")]),
        dict(emoji="🪣", label=("Not A Bucket", "バケツじゃない"),
             s=[("So think of the pile as a river, not a bucket to empty.", "だから積ん読は、空にするバケツではなく、流れていく川だと考えます。")]),
        dict(emoji="🎣", label=("Just Scoop", "すくうだけ"),
             s=[("It is enough to scoop up the one you like sometimes.", "気になったものを、ときどきすくうだけで十分です。")]),
        dict(emoji="🏛️", label=("Library Calm", "図書館では平気"), big=True,
             s=[("We do not panic at a library's unread books, because reading them all is not our job.",
                 "図書館の読んでいない本に焦らないのは、全部読むのが自分の仕事だと思っていないからです。")]),
    ],
    game_after=2,
    game_note="バケツ or 川（あふれるバケツ vs すくうだけの川）",
    game_html="""  <section class="game" data-m="bucket" data-s="idle" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Bucket or river?</div>
    <div class="tabs">
      <button class="tab t-bucket" type="button">🪣 Bucket</button>
      <button class="tab t-river" type="button">🌊 River</button>
    </div>
    <div class="field">
      <div class="bucket-area">
        <span class="drop">📕</span>
        <div class="bucket"><div class="fill"></div></div>
        <div class="cnt"><span class="cl">📚 In the bucket:</span> <b class="bn">0</b><span class="of">/10</span></div>
      </div>
      <div class="river-area">
        <div class="river"></div>
        <div class="shelf"><span class="cl">🎣 Scooped:</span> <b class="sn">0</b><span class="of">/3</span> <span class="picks"></span></div>
      </div>
      <div class="pg" aria-hidden="true"><span class="pface">🐧</span></div>
    </div>
    <div class="msg">
      <div class="m m-b-idle">New books keep coming. Try to empty the bucket!</div>
      <div class="m m-b-run">Read, read, read…! 😰</div>
      <div class="m m-b-over">😵 It overflows! You can never empty it.</div>
      <div class="m m-r-idle">Books float down the river. Tap the ones you like.</div>
      <div class="m m-r-run">😌 The rest just flows by. That is fine.</div>
      <div class="m m-r-done">🎣 You scooped 3 good ones. That is enough! 🎉</div>
    </div>
    <div class="btns">
      <button class="btn b-start" type="button">▶ Start</button>
      <button class="btn b-read" type="button"><span class="rd-a">📖 Read one</span><span class="rd-b">⏳ Reading…</span></button>
      <button class="btn ghost b-again" type="button">↺ Try again</button>
    </div>
  </section>""",
    css=r"""
  /* 🌊 バケツ or 川 */
  .tabs { display: flex; justify-content: center; gap: 8px; margin-top: 14px; }
  .tab { min-height: 48px; padding: 8px 18px; border: 0; border-radius: 999px; font: inherit; font-size: 16px; font-weight: 900; cursor: pointer;
    background: rgba(255,255,255,.2); color: #fff; box-shadow: inset 0 0 0 2px rgba(255,255,255,.6); touch-action: manipulation; -webkit-tap-highlight-color: transparent; }
  .game[data-m="bucket"] .t-bucket, .game[data-m="river"] .t-river { background: #fff; color: #135ea8; box-shadow: 0 5px 0 rgba(0,0,0,.16); }
  .field { position: relative; height: 230px; max-width: 420px; margin: 12px auto 0; border-radius: 24px; background: rgba(255,255,255,.14); overflow: hidden; }
  .game .bucket-area, .game .river-area { display: none; }
  .game[data-m="bucket"] .bucket-area, .game[data-m="river"] .river-area { display: block; }
  .bucket-area { position: absolute; inset: 0; }
  .bucket { position: absolute; left: 50%; bottom: 44px; width: 130px; height: 120px; margin-left: -65px; overflow: hidden;
    border-radius: 6px 6px 30px 30px; background: rgba(255,255,255,.35); box-shadow: inset 0 0 0 5px #fff; }
  .fill { position: absolute; left: 0; right: 0; bottom: 0; height: 0; background: repeating-linear-gradient(0deg, #ff7a59 0 12px, #ffd166 12px 24px, #6c9cff 24px 36px, #7bd88f 36px 48px);
    transition: height .25s ease; }
  .game[data-s="over"] .bucket { animation: shake .45s ease 2; box-shadow: inset 0 0 0 5px #ffe066; }
  .drop { position: absolute; left: 50%; top: -40px; margin-left: -16px; font-size: 32px; line-height: 1; display: inline-block; }
  .drop.go { animation: fall .45s ease-in; }
  @keyframes fall { from { transform: translateY(0); } to { transform: translateY(120px); } }
  .cnt, .shelf { position: absolute; left: 0; right: 0; bottom: 10px; font-size: 15px; font-weight: 900; }
  .cnt b, .shelf b { display: inline-block; min-width: 1.4em; padding: 1px 7px; border-radius: 999px; background: #fff; color: #135ea8; }
  .river-area { position: absolute; inset: 0; }
  .river { position: absolute; left: 0; right: 0; top: 54px; height: 112px;
    background: linear-gradient(180deg, rgba(255,255,255,.1), rgba(150,220,255,.5) 30%, rgba(80,170,255,.6) 70%, rgba(255,255,255,.1)); }
  .bk { position: absolute; top: 0; left: 0; width: 54px; height: 54px; padding: 0; border: 0; border-radius: 16px; background: rgba(255,255,255,.85);
    font-size: 30px; line-height: 1; cursor: pointer; box-shadow: 0 4px 0 rgba(0,0,0,.12); touch-action: manipulation; -webkit-tap-highlight-color: transparent; }
  .bk.got { background: #ffe066; transition: opacity .35s ease; opacity: 0; }
  .picks { font-size: 20px; }
  .pg { position: absolute; right: 12px; top: 10px; font-size: 34px; }
  .pface { display: inline-block; }
  .msg { margin-top: 12px; min-height: 50px; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .msg .m { display: none; }
  .game[data-m="bucket"][data-s="idle"] .m-b-idle, .game[data-m="bucket"][data-s="run"] .m-b-run, .game[data-m="bucket"][data-s="over"] .m-b-over,
  .game[data-m="river"][data-s="idle"] .m-r-idle, .game[data-m="river"][data-s="run"] .m-r-run, .game[data-m="river"][data-s="done"] .m-r-done { display: block; }
  .btns { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-top: 12px; }
  .game .b-read, .game .b-again { display: none; }
  .game:not([data-s="idle"]) .b-start { display: none; }
  .game[data-m="bucket"][data-s="run"] .b-read { display: inline-flex; min-width: 200px; background: #ffe066; color: #4a3500; }
  .game[data-s="over"] .b-again, .game[data-s="done"] .b-again { display: inline-flex; }
  .b-read .rd-b { display: none; }
  .b-read.busy .rd-a { display: none; }
  .b-read.busy .rd-b { display: inline; }
""",
    dark="""  html[data-theme="dark"] .game .b-read { background: #ffe066; color: #4a3500; }
  html[data-theme="dark"] .bk { background: rgba(240,248,255,.9); }""",
    js=r"""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var fill = g.querySelector('.fill'), bn = g.querySelector('.bn'), sn = g.querySelector('.sn'), drop = g.querySelector('.drop');
  var river = g.querySelector('.river'), picks = g.querySelector('.picks'), face = g.querySelector('.pface'), read = g.querySelector('.b-read');
  var BOOKS = ['📕', '📗', '📘', '📙'];
  var n = 0, got = 0, tm = 0, raf = 0, spawnT = 0, floats = [];
  function st(s) { g.setAttribute('data-s', s); }
  function stopAll() {
    clearInterval(tm); clearTimeout(spawnT); cancelAnimationFrame(raf);
    floats.forEach(function (f) { if (f.el.parentNode) f.el.parentNode.removeChild(f.el); }); floats = [];
  }
  function reset(mode) {
    stopAll(); n = 0; got = 0; bn.textContent = '0'; sn.textContent = '0'; picks.textContent = '';
    fill.style.height = '0'; face.textContent = '🐧'; read.classList.remove('busy');
    if (mode) g.setAttribute('data-m', mode); st('idle');
  }
  /* 🪣 バケツ：本は読むより速くたまる */
  function addBook() {
    n++; bn.textContent = Math.min(n, 10); fill.style.height = Math.min(100, n * 10) + '%';
    drop.textContent = BOOKS[n % 4]; drop.classList.remove('go'); void drop.offsetWidth; drop.classList.add('go');
    face.textContent = n >= 7 ? '😰' : '🐧';
    if (n >= 10) { clearInterval(tm); st('over'); face.textContent = '😵'; }
  }
  function startBucket() { st('run'); addBook(); tm = setInterval(addBook, 650); }
  read.addEventListener('click', function () {
    if (g.getAttribute('data-s') !== 'run' || read.classList.contains('busy')) return;
    read.classList.add('busy');
    setTimeout(function () {
      read.classList.remove('busy');
      if (g.getAttribute('data-s') !== 'run') return;
      n = Math.max(0, n - 1); bn.textContent = n; fill.style.height = n * 10 + '%';
    }, 1100);
  });
  /* 🌊 川：すくうだけ */
  function spawn() {
    if (g.getAttribute('data-s') !== 'run') return;
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'bk'; b.textContent = BOOKS[Math.floor(Math.random() * 4)];
    var f = { el: b, x: -60, y: 8 + Math.random() * 50, v: 55 + Math.random() * 25 };
    b.style.transform = 'translate(' + f.x + 'px,' + f.y + 'px)';
    b.addEventListener('click', function () {
      if (b.classList.contains('got') || g.getAttribute('data-s') !== 'run') return;
      b.classList.add('got'); f.dead = true; setTimeout(function () { f.gone = true; if (b.parentNode) b.parentNode.removeChild(b); }, 400); got++; sn.textContent = got; picks.textContent += b.textContent;
      var r = b.getBoundingClientRect();
      if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, [b.textContent, '✨', '💧'], 8);
      face.textContent = '😌';
      if (got >= 3) {
        st('done'); clearTimeout(spawnT);
        var q = g.getBoundingClientRect();
        if (window.pengessoPop) window.pengessoPop(q.left + q.width / 2, Math.max(80, q.top + 150), ['🎣', '📚', '🐧', '✨'], 18);
      }
    });
    river.appendChild(b); floats.push(f);
    spawnT = setTimeout(spawn, 900 + Math.random() * 500);
  }
  var last = 0;
  function frame(t) {
    var dt = last ? Math.min(60, t - last) / 1000 : 0; last = t;
    var w = river.clientWidth + 60;
    floats = floats.filter(function (f) {
      if (!f.dead) f.x += f.v * dt;
      f.el.style.transform = 'translate(' + f.x.toFixed(1) + 'px,' + f.y.toFixed(1) + 'px)';
      if (f.gone) return false;
      if (f.x > w) { if (f.el.parentNode) f.el.parentNode.removeChild(f.el); return false; }
      return true;
    });
    if (g.getAttribute('data-m') === 'river' && g.getAttribute('data-s') !== 'idle') raf = requestAnimationFrame(frame);
  }
  function startRiver() { st('run'); last = 0; spawn(); raf = requestAnimationFrame(frame); }
  g.querySelector('.b-start').addEventListener('click', function () {
    if (g.getAttribute('data-m') === 'bucket') startBucket(); else startRiver();
  });
  g.querySelector('.b-again').addEventListener('click', function () { reset(); });
  g.querySelector('.t-bucket').addEventListener('click', function () { reset('bucket'); });
  g.querySelector('.t-river').addEventListener('click', function () { reset('river'); });
})();
""",
    ja={
        "Bucket or river?": "バケツ？それとも川？",
        "🪣 Bucket": "🪣 バケツ",
        "🌊 River": "🌊 川",
        "📚 In the bucket:": "📚 バケツの中：",
        "🎣 Scooped:": "🎣 すくった本：",
        "New books keep coming. Try to empty the bucket!": "新しい本がどんどん来ます。バケツを空にしてみて！",
        "Read, read, read…! 😰": "読んで、読んで、読んで…！😰",
        "😵 It overflows! You can never empty it.": "😵 あふれた！バケツは絶対に空になりません。",
        "Books float down the river. Tap the ones you like.": "本が川を流れていきます。気になった本をタップしてね。",
        "😌 The rest just flows by. That is fine.": "😌 ほかの本は流れていくだけ。それでいいんです。",
        "🎣 You scooped 3 good ones. That is enough! 🎉": "🎣 いい本を3冊すくえました。それで十分！🎉",
        "▶ Start": "▶ スタート",
        "📖 Read one": "📖 1冊読む",
        "⏳ Reading…": "⏳ 読んでいます…",
        "↺ Try again": "↺ もう一回",
    },
)

if __name__ == "__main__":
    build(d)
