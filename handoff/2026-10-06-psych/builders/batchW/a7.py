from gen import build

d = dict(
    slug="two-keys-to-happiness", seq=518,
    title=("2 keys to a happy life: hope and good people around you",
           "幸せの2つの鍵は「希望」と「いい人間関係」"),
    label=("2 Keys", "2つの鍵"),
    h1_emoji="🗝️",
    alt="A chubby low-poly wood and paper penguin hugging a real old wooden treasure chest with two brass padlocks",
    section="幸せに大切な2つ",
    message="幸せに大切なのは2つ。希望（どんなときも自分で切り開けると思えること）と、いい人間関係。",
    tone="素材の重さ：真面目（幸せの土台）\n→ 見せ方：ポップに（青緑と金色。2つの錠前の宝箱）",
    game_ja="🗝️ 2つの錠前の宝箱：小さな場面（「失敗したけど、またやれる」／話を聞いてくれる友達とコーヒー など6つ）が1つずつ出てくる。「希望の錠前」か「人の錠前」かを選んで押す。合っていると鍵がカチッと進み、ちがうと錠前がぶるぶる。両方の錠前が3/3になると、宝箱のふたが開いてキラキラ。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made in low-poly 3D wood and paper style, "
            "happily hugging a realistic old wooden treasure chest that has two small brass padlocks on the front, one padlock already open. "
            "Bright simple teal and warm gold background with soft depth, a clean soft floor. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × ローポリの木と紙 × 錠前が2つの宝箱",
    mood=["lift", "think"], tags=["psychology", "happiness", "friends"],
    pal=dict(bg="#f2fffc", muted="#5c8079", acc="#0d8a7a", acc2="#ffb000", shadow="rgba(20,110,100,.16)",
             r1="rgba(255,190,40,.30)", r2="rgba(13,138,122,.18)", r3="rgba(90,108,255,.14)",
             h1="#0f3a34", photo="#dcf7f1", big="#0a7566", bigdark="#86ecdc",
             game="linear-gradient(155deg, #12b5a0 0%, #5a6cff 55%, #ffb000 100%)"),
    cards=[
        dict(emoji="🗝️", label=("2 Things", "2つのもの"),
             s=[("It is said that there are 2 important things for a happy life.",
                 "幸せに生きるために大切なものは、2つあるそうです。")]),
        dict(emoji="🌅", label=("Key 1: Hope", "鍵1：希望"),
             s=[("The 1st is hope: feeling \"I can open up my own life, at any time.\"",
                 "1つ目は希望、つまり「どんなときでも、自分の人生は自分で切り開ける」と思えることです。")]),
        dict(emoji="🤝", label=("Key 2: People", "鍵2：人"), big=True,
             s=[("The 2nd is good relationships with people.",
                 "2つ目は、いい人間関係です。")]),
        dict(emoji="📖", label=("Both Together", "両方そろうと"),
             s=[("For example, if you think \"I can do it somehow\" about hard English, and you have a friend to laugh with, you feel much stronger.",
                 "たとえば、苦手な英語でも「やれば何とかなる」と思えて、一緒に笑える友達がいたら、だいぶ心強いです。")]),
    ],
    game_after=3,
    game_note="2つの錠前の宝箱（希望と人に仕分ける）",
    game_html="""  <section class="game" data-i="0" data-h="0" data-p="0" data-fb="" data-open="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Open the chest with 2 keys</div>
    <div class="game-hint">Which lock does this little moment fit? Tap one.</div>
    <div class="chest">
      <div class="lid"></div>
      <div class="gem"><span class="gem-e">💎</span></div>
      <div class="box">
        <div class="lock lk-h"><span class="lk-e">🔒</span><span class="lk-n"><span class="nh">0</span>/3</span></div>
        <div class="lock lk-p"><span class="lk-e">🔒</span><span class="lk-n"><span class="np">0</span>/3</span></div>
      </div>
    </div>
    <div class="scene">
      <span class="q q0" data-k="h">📝 "I failed, but I can try again."</span>
      <span class="q q1" data-k="p">☕ Coffee with a friend who listens</span>
      <span class="q q2" data-k="p">📱 A "How are you?" message</span>
      <span class="q q3" data-k="h">🗺️ "If this road is closed, I can find another."</span>
      <span class="q q4" data-k="h">🐢 "I can learn this slowly."</span>
      <span class="q q5" data-k="p">🍲 Eating dinner together and laughing</span>
      <span class="q q6">🎉 All 6 moments are in!</span>
    </div>
    <div class="fb"><span class="fb-ok">✅ Click! It fits.</span><span class="fb-ng">🤔 Hmm… it fits the other lock.</span></div>
    <div class="locks">
      <button type="button" class="btn pick pk-h" data-k="h">🌅 Hope lock</button>
      <button type="button" class="btn pick pk-p" data-k="p">🤝 People lock</button>
    </div>
    <div class="end">🎉 Both keys! Hope and good people open the chest together.</div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Start over</button></div>
  </section>""",
    css="""
  /* 🗝️ 2つの錠前の宝箱 */
  .chest { position: relative; width: 230px; height: 170px; margin: 44px auto 0; }
  .box { position: absolute; left: 0; right: 0; bottom: 0; height: 104px; border-radius: 10px 10px 18px 18px; background: #b8742e;
    border: 5px solid #8a521a; display: flex; justify-content: space-around; align-items: center; box-shadow: 0 8px 0 rgba(0,0,0,.18); z-index: 2; }
  .lid { position: absolute; left: -4px; right: -4px; top: 18px; height: 54px; border-radius: 60px 60px 8px 8px; background: #c98535; border: 5px solid #8a521a;
    transform-origin: 50% 100%; transition: transform .7s cubic-bezier(.3,1.5,.5,1); z-index: 3; }
  .game[data-open="1"] .lid { transform: translateY(-10px) rotate(-16deg); }
  .gem { position: absolute; left: 50%; top: 52px; transform: translate(-50%, 30px) scale(.4); opacity: 0; z-index: 1;
    transition: transform .7s .25s cubic-bezier(.3,1.6,.5,1), opacity .4s .25s; }
  .gem-e { font-size: 48px; line-height: 1; }
  .game[data-open="1"] .gem { transform: translate(-50%, -34px) scale(1); opacity: 1; z-index: 4; }
  .lock { display: grid; justify-items: center; gap: 2px; width: 74px; padding: 6px 4px; border-radius: 14px; background: #ffe7a8; color: #5a3a00; }
  .lk-e { font-size: 28px; line-height: 1; }
  .lk-n { font-size: 14px; font-weight: 900; }
  .lock.bump { animation: boing .4s ease; }
  .lock.no { animation: shake .4s ease; }
  .game[data-h="3"] .lk-h, .game[data-p="3"] .lk-p { background: #c6ffb0; color: #1d5a00; }
  .scene { margin: 16px auto 0; max-width: 420px; min-height: 70px; display: grid; place-items: center; padding: 12px 16px; border-radius: 20px;
    background: #fff; color: #23314d; font-size: 17px; font-weight: 900; line-height: 1.4; }
  .q { display: none; }
  .game[data-i="0"] .q0, .game[data-i="1"] .q1, .game[data-i="2"] .q2, .game[data-i="3"] .q3, .game[data-i="4"] .q4,
  .game[data-i="5"] .q5, .game[data-i="6"] .q6 { display: block; animation: boing .4s ease; }
  .fb { min-height: 30px; margin-top: 8px; font-size: 15px; font-weight: 900; }
  .fb span { display: none; }
  .game[data-fb="ok"] .fb-ok, .game[data-fb="ng"] .fb-ng { display: inline; }
  .locks { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 420px; margin: 6px auto 0; }
  .pick { min-height: 62px; border-radius: 18px; font-size: 15.5px; padding: 8px 10px; }
  .pk-h { background: #fff1b8; color: #5a3d00; }
  .pk-p { background: #e2e6ff; color: #2c3577; }
  .game[data-i="6"] .locks { opacity: .4; pointer-events: none; }
  .end { display: none; margin: 14px auto 0; max-width: 420px; padding: 12px 14px; border-radius: 18px; background: #fff; color: #0f4f46; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .game[data-open="1"] .end { display: block; animation: boing .5s ease; }
  .ctrl { margin-top: 12px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
""",
    dark="""  html[data-theme="dark"] .lock { background: #4a3c12; color: #ffe39a; }
  html[data-theme="dark"] .game[data-h="3"] .lk-h, html[data-theme="dark"] .game[data-p="3"] .lk-p { background: #2f4f1a; color: #d4ffb8; }
  html[data-theme="dark"] .scene { background: #2b2d3a; color: #f4f0fa; }
  html[data-theme="dark"] .pk-h { background: #4a3c12; color: #ffe39a; }
  html[data-theme="dark"] .pk-p { background: #2a3050; color: #d6dcff; }
  html[data-theme="dark"] .end { background: #2b2d3a; color: #a8f0e2; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var i = 0, h = 0, p = 0, busy = false, t = 0;
  var ans = [].map.call(g.querySelectorAll('.q[data-k]'), function (q) { return q.getAttribute('data-k'); });
  function again(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function paint() {
    g.querySelector('.nh').textContent = h; g.querySelector('.np').textContent = p;
    g.setAttribute('data-h', String(h)); g.setAttribute('data-p', String(p)); g.setAttribute('data-i', String(i));
  }
  [].forEach.call(g.querySelectorAll('.pick'), function (b) {
    b.addEventListener('click', function () {
      if (busy || i >= ans.length) return;
      var k = b.getAttribute('data-k'), lock = g.querySelector('.lk-' + k);
      g.setAttribute('data-fb', '');
      if (k === ans[i]) {
        busy = true;
        if (k === 'h') h++; else p++;
        g.setAttribute('data-fb', 'ok');
        again(lock, 'bump');
        if (window.pengessoPop) { var r = lock.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top, ['🔑', '✨'], 6); }
        clearTimeout(t);
        t = setTimeout(function () {
          i++; paint(); busy = false;
          if (h === 3 && p === 3) {
            g.setAttribute('data-open', '1');
            [].forEach.call(g.querySelectorAll('.lk-e'), function (e) { e.textContent = '🔓'; });
            if (window.pengessoPop) { var c = g.querySelector('.chest').getBoundingClientRect(); window.pengessoPop(c.left + c.width / 2, c.top + 40, ['💎', '✨', '🗝️', '🐧', '🌅', '🤝'], 22); }
          }
        }, 600);
        g.querySelector('.nh').textContent = h; g.querySelector('.np').textContent = p;
        g.setAttribute('data-h', String(h)); g.setAttribute('data-p', String(p));
      } else {
        g.setAttribute('data-fb', 'ng');
        again(lock, 'no');
        if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
      }
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    clearTimeout(t); busy = false; i = 0; h = 0; p = 0;
    [].forEach.call(g.querySelectorAll('.lk-e'), function (e) { e.textContent = '🔒'; });
    g.setAttribute('data-fb', ''); g.setAttribute('data-open', '0'); paint();
  });
})();
""",
    ja={
        "Open the chest with 2 keys": "2つの鍵で、宝箱を開けよう",
        "Which lock does this little moment fit? Tap one.": "この小さな場面は、どっちの錠前に合う？押してみてね。",
        "📝 \"I failed, but I can try again.\"": "📝「失敗したけど、またやれる」",
        "☕ Coffee with a friend who listens": "☕ 話を聞いてくれる友達とコーヒー",
        "📱 A \"How are you?\" message": "📱「元気？」のメッセージ",
        "🗺️ \"If this road is closed, I can find another.\"": "🗺️「この道がだめでも、別の道を探せる」",
        "🐢 \"I can learn this slowly.\"": "🐢「ゆっくりなら、できるようになる」",
        "🍲 Eating dinner together and laughing": "🍲 一緒に晩ごはんを食べて笑う",
        "🎉 All 6 moments are in!": "🎉 6つの場面、ぜんぶ入った！",
        "✅ Click! It fits.": "✅ カチッ！ぴったり。",
        "🤔 Hmm… it fits the other lock.": "🤔 うーん…それはもう1つの錠前かも。",
        "🌅 Hope lock": "🌅 希望の錠前",
        "🤝 People lock": "🤝 人の錠前",
        "🎉 Both keys! Hope and good people open the chest together.": "🎉 鍵が2つそろった！希望といい人間関係で、宝箱が開きました。",
        "↺ Start over": "↺ 最初から",
    },
)
build(d)
