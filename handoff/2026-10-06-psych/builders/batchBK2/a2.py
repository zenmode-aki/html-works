from gen import build

d = dict(
    slug="choosing-means-not-choosing", seq=563, path="reality",
    title=("Choosing one thing means not choosing millions of other things",
           "何かを選ぶことは、ほかの何百万個を選ばないこと"),
    label=("Choosing", "選ぶこと"),
    h1_emoji="🚪",
    alt="A chubby low-poly wood and paper penguin opening one realistic old wooden door and peeking through happily",
    section="⑥「人生の『管制塔』には登れない」",
    message="何かを選ぶ＝ほかの何百万個を選ばないこと。それは失敗ではなくルール。だから選んだ1つを楽しむ。",
    tone="素材の重さ：真面目（生き方の考え方）\n→ 見せ方：ポップに（紫とピンク。6つのドアで遊べる）",
    game_ja="🚪 6つのドア：カフェ・勉強・野球・旅・お絵かき・昼寝のドアから1つを押すと、そのドアがパッと開いて中身が飛び出す。ほかの5つは、やさしく薄くなって閉まる。「選ばなかったドア」の数が 5 → 1,000,000+ まで数え上がる。閉まったドアを押すと、ぷるっとゆれて「1つずつ！それがルール」。最後に「🤔 本当に自分で選んだ？」を押すと、バークマンさんの「本当に選べるならの話だけどね」のオチ。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made in low-poly 3D wood and paper style, "
            "pushing open one realistic old painted wooden door standing alone, warm light coming through the open door. "
            "Bright simple lavender and soft pink background with depth. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × 木と紙のローポリ × 古い木のドア",
    mood=["think", "laugh"], tags=["books", "mindset", "happiness"],
    pal=dict(bg="#f8f4ff", muted="#77699a", acc="#7a4fe0", acc2="#ff7aa8", shadow="rgba(90,60,160,.16)",
             r1="rgba(255,140,180,.28)", r2="rgba(122,79,224,.20)", r3="rgba(80,200,220,.14)",
             h1="#2d2152", photo="#ece5ff", big="#6a3fd0", bigdark="#c6b3ff",
             game="linear-gradient(150deg, #7a4fe0 0%, #b660f0 55%, #ff8fb1 100%)"),
    cards=[
        dict(emoji="🚪", label=("The Rule", "ルール"),
             s=[("Oliver Burkeman says that choosing one thing means not choosing millions of other things.",
                 "オリバー・バークマンさんによると、何かを選ぶということは、ほかの何百万個を選ばないということだそうです。")]),
        dict(emoji="⏳", label=("Limited Time", "限りある時間"),
             s=[("Our time is limited, so we cannot choose everything.",
                 "時間は限られているので、全部は選べません。")]),
        dict(emoji="🙂", label=("Not A Failure", "失敗じゃない"),
             s=[("Not choosing the others is not a failure.", "ほかを選ばないのは、失敗ではありません。"),
                ("It is just the rule.", "ただのルールです。")]),
        dict(emoji="💛", label=("Enjoy It", "楽しめばいい"), big=True,
             s=[("So, just enjoy the one you chose.",
                 "だから、選んだ1つを楽しめばいいんです。")]),
        dict(emoji="😂", label=("His Joke", "オチ"),
             s=[("Burkeman even makes a joke at himself: \"Well, that is, if we can really choose.\"",
                 "バークマンさんは、「まあ、本当に選べるならの話だけどね」と、自分でツッコんでいます。")]),
    ],
    game_after=2,
    game_note="6つのドア（1つ開けると、ほかは閉まる）",
    game_html="""  <section class="game" data-s="idle" data-m="hint" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Which door will you open today?</div>
    <div class="doors">
      <button type="button" class="door" data-i="0"><span class="dr-e" aria-hidden="true">🚪</span><span class="dr-in" aria-hidden="true">☕</span><span class="dr-t">Cafe</span></button>
      <button type="button" class="door" data-i="1"><span class="dr-e" aria-hidden="true">🚪</span><span class="dr-in" aria-hidden="true">📚</span><span class="dr-t">Study</span></button>
      <button type="button" class="door" data-i="2"><span class="dr-e" aria-hidden="true">🚪</span><span class="dr-in" aria-hidden="true">⚾</span><span class="dr-t">Baseball</span></button>
      <button type="button" class="door" data-i="3"><span class="dr-e" aria-hidden="true">🚪</span><span class="dr-in" aria-hidden="true">✈️</span><span class="dr-t">Trip</span></button>
      <button type="button" class="door" data-i="4"><span class="dr-e" aria-hidden="true">🚪</span><span class="dr-in" aria-hidden="true">🎨</span><span class="dr-t">Drawing</span></button>
      <button type="button" class="door" data-i="5"><span class="dr-e" aria-hidden="true">🚪</span><span class="dr-in" aria-hidden="true">😴</span><span class="dr-t">Nap</span></button>
    </div>
    <div class="more"><span class="mo-a">+ 999,994</span> <span class="mo-t">more doors out there</span></div>
    <div class="closed"><span class="cl-l">🚪 Doors you did not open:</span> <span class="cl-n">0</span></div>
    <div class="msgs">
      <div class="m-hint">Pick 1 door you want to open.</div>
      <div class="m-chose">You opened 1 door. The other 5, and millions more, closed. That is the rule, not a mistake. 🙂</div>
      <div class="m-one">One at a time! That is the rule. 🚪</div>
      <div class="m-joke">…That is, if we can really choose at all. 😂</div>
    </div>
    <div class="ctrl">
      <button type="button" class="btn b-joke">🤔 Did I really choose?</button>
      <button type="button" class="btn ghost b-reset">↺ Choose again</button>
    </div>
  </section>""",
    css="""
  /* 🚪 6つのドア */
  .doors { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; max-width: 420px; margin: 16px auto 0; perspective: 600px; }
  .door { position: relative; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; gap: 4px;
    min-height: 112px; padding: 10px 4px 10px; border: 0; border-radius: 18px 18px 10px 10px; cursor: pointer; font: inherit;
    background: linear-gradient(180deg, #fff 0%, #f3ecff 100%); color: #3a2a66; box-shadow: 0 6px 0 rgba(60,30,120,.28);
    transition: opacity .6s ease, transform .35s ease, filter .6s ease, background .4s ease;
    -webkit-tap-highlight-color: transparent; touch-action: manipulation; user-select: none; -webkit-user-select: none; }
  .door:active { transform: translateY(4px); box-shadow: 0 2px 0 rgba(60,30,120,.28); }
  .door:focus-visible { outline: 4px solid #fff; outline-offset: 3px; }
  .dr-e { font-size: 40px; line-height: 1; transition: transform .45s ease, opacity .45s ease; transform-origin: 0 50%; }
  .dr-in { position: absolute; left: 50%; top: 14px; font-size: 44px; line-height: 1; opacity: 0; transform: translateX(-50%) scale(.3);
    transition: opacity .4s .15s ease, transform .5s .15s cubic-bezier(.3,1.6,.5,1); }
  .dr-t { font-size: 14.5px; font-weight: 900; line-height: 1.2; }
  .door.open { background: linear-gradient(180deg, #fff7c2 0%, #ffd86b 100%); transform: scale(1.06); box-shadow: 0 0 0 4px #fff, 0 10px 24px rgba(0,0,0,.2); }
  .door.open .dr-e { transform: rotateY(-75deg); opacity: 0; }
  .door.open .dr-in { opacity: 1; transform: translateX(-50%) scale(1); }
  .door.shut { opacity: .3; filter: grayscale(1); transform: scale(.94); }
  .door.wig { animation: shake .4s ease; }
  .more { margin-top: 12px; font-size: 14px; font-weight: 900; opacity: .9; transition: opacity .6s ease; }
  .game[data-s="chose"] .more { opacity: .25; text-decoration: line-through; }
  .closed { margin-top: 8px; font-size: 15px; font-weight: 900; opacity: 0; transition: opacity .4s ease; }
  .game[data-s="chose"] .closed { opacity: 1; }
  .cl-n { display: inline-block; min-width: 2em; padding: 1px 10px; border-radius: 999px; background: rgba(255,255,255,.25); }
  .msgs { min-height: 76px; margin-top: 8px; }
  .msgs > div { display: none; font-size: 16px; font-weight: 900; line-height: 1.45; padding: 6px 4px; }
  .game[data-m="hint"] .m-hint, .game[data-m="chose"] .m-chose, .game[data-m="one"] .m-one, .game[data-m="joke"] .m-joke { display: block; animation: boing .45s ease; }
  .ctrl { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-top: 6px; }
  .b-joke { background: #ffe066; color: #4a3500; }
  .game[data-s="idle"] .ctrl { visibility: hidden; }
""",
    dark="""  html[data-theme="dark"] .door { background: linear-gradient(180deg, #2f2a45 0%, #262238 100%); color: #ece5ff; }
  html[data-theme="dark"] .door.open { background: linear-gradient(180deg, #5a4a17 0%, #4a3c12 100%); color: #ffe39a; }
  html[data-theme="dark"] .game .b-joke { background: #5a4a17; color: #ffe39a; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var doors = [].slice.call(g.querySelectorAll('.door')), num = g.querySelector('.cl-n'), rollT = 0;
  function msg(m) { g.setAttribute('data-m', ''); void g.offsetWidth; g.setAttribute('data-m', m); }
  function roll() {
    var steps = [5, 50, 500, 5000, 50000, 500000, 1000000], k = 0;
    clearInterval(rollT);
    rollT = setInterval(function () {
      num.textContent = steps[k].toLocaleString('en-US') + (k === steps.length - 1 ? '+' : '');
      k++; if (k >= steps.length) clearInterval(rollT);
    }, 260);
  }
  doors.forEach(function (d) {
    d.addEventListener('click', function () {
      if (g.getAttribute('data-s') === 'chose') {
        if (d.classList.contains('open')) return;
        d.classList.remove('wig'); void d.offsetWidth; d.classList.add('wig');
        msg('one');
        if (navigator.vibrate) { try { navigator.vibrate(20); } catch (e) {} }
        return;
      }
      g.setAttribute('data-s', 'chose');
      doors.forEach(function (o) { o.classList.add(o === d ? 'open' : 'shut'); });
      msg('chose'); roll();
      if (window.pengessoPop) {
        var r = d.getBoundingClientRect(), em = d.querySelector('.dr-in').textContent;
        setTimeout(function () { window.pengessoPop(r.left + r.width / 2, r.top + r.height / 3, [em, '✨', '🐧'], 16); }, 250);
      }
    });
  });
  g.querySelector('.b-joke').addEventListener('click', function () { msg('joke'); });
  g.querySelector('.b-reset').addEventListener('click', function () {
    clearInterval(rollT); num.textContent = '0';
    doors.forEach(function (o) { o.classList.remove('open', 'shut', 'wig'); });
    g.setAttribute('data-s', 'idle'); msg('hint');
  });
})();
""",
    ja={
        "Which door will you open today?": "今日は、どのドアを開ける？",
        "Cafe": "カフェ",
        "Study": "勉強",
        "Baseball": "野球",
        "Trip": "旅",
        "Drawing": "お絵かき",
        "Nap": "昼寝",
        "+ 999,994": "＋ 999,994",
        "more doors out there": "個のドアが、ほかにもある",
        "🚪 Doors you did not open:": "🚪 開けなかったドア：",
        "Pick 1 door you want to open.": "開けたいドアを1つ選んでね。",
        "You opened 1 door. The other 5, and millions more, closed. That is the rule, not a mistake. 🙂": "ドアを1つ開けた。ほかの5つと、何百万個のドアは閉まった。それはミスじゃなくて、ルールです 🙂",
        "One at a time! That is the rule. 🚪": "1つずつ！それがルールです 🚪",
        "…That is, if we can really choose at all. 😂": "…まあ、本当に選べるならの話だけどね 😂",
        "🤔 Did I really choose?": "🤔 本当に自分で選んだ？",
        "↺ Choose again": "↺ 選びなおす",
    },
)

if __name__ == "__main__":
    build(d)
