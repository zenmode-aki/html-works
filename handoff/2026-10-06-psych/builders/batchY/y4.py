from gen import build

d = dict(
    slug="thanks-shows-you-what-you-have", seq=535,
    title=("Saying thank you shows you how much you already have",
           "「ありがとう」を言うと、もう持っているものが見えてくる"),
    label=("Already Here", "もうここにある"),
    h1_emoji="💡",
    alt="A chubby layered cut paper penguin switching on a real brass table lamp in a cozy room that fills with warm light",
    section="感謝を習慣に",
    message="感謝を伝えるいちばんの効果は、自分が「良かったこと」にあらためて気づけること。慣れて見えなくなったものを照らしてくれる。",
    tone="素材の重さ：ふつう（感謝の効果）\n→ 見せ方：ポップに（夜の紺色と、あたたかいランプの黄色。「ありがとう」を言うたびに、暗い部屋のものが1つずつ光る）",
    game_ja="💡 ありがとうライト：暗い部屋に、影になったものが6つ。押して「ありがとう」を言うと、そのものがパッと明るくなって名前が出る（読書できる明かり／あたたかいごはん／ふかふかのベッド／きれいな水／友達からのメッセージ／足に合うくつ）。1つ光るごとに部屋が明るくなり、6つで「ぜんぶ、最初からここにあった」。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of layered cut paper diorama style, "
            "reaching up to switch on a realistic small brass table lamp with a warm cream fabric shade, the lamp glowing softly in a cozy simple room. "
            "Bright simple warm honey yellow and soft navy background with soft depth and a gentle glow. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × 切り絵のジオラマ × 真ちゅうのテーブルランプ",
    mood=["lift"], tags=["psychology", "happiness", "feelings"],
    pal=dict(bg="#fffaf0", muted="#7c705c", acc="#d98a00", acc2="#3b4bb5", shadow="rgba(150,110,30,.16)",
             r1="rgba(255,206,84,.36)", r2="rgba(59,75,181,.14)", r3="rgba(255,170,90,.16)",
             h1="#3a2a08", photo="#fff1cc", big="#b06c00", bigdark="#ffd27a",
             game="linear-gradient(165deg, #2a2f6b 0%, #4a3f8f 55%, #c9873a 100%)"),
    cards=[
        dict(emoji="✨", label=("Best Effect", "いちばんの効果"),
             s=[("It is said the biggest effect of saying thanks is that you notice the good things again.",
                 "感謝を伝えるいちばんの効果は、自分が「良かったこと」に、あらためて気づけることだそうです。")]),
        dict(emoji="🌱", label=("Lucky Feeling", "恵まれている"),
             s=[("When you feel \"I am lucky,\" you feel happier, and you also get more energy.",
                 "「恵まれているな」と感じると、幸せな気持ちが増えて、やる気も出てきます。")]),
        dict(emoji="😶", label=("We Get Used", "慣れてしまう"),
             s=[("People get used to anything very quickly.",
                 "人は、どんなことにもすぐ慣れてしまいます。")]),
        dict(emoji="💡", label=("A Small Light", "小さなライト"), big=True,
             s=[("So \"thank you\" is like a light that shows the things you stopped seeing.",
                 "だから「ありがとう」は、慣れて見えなくなったものを照らすライトみたいなものです。")]),
    ],
    game_after=3,
    game_note="ありがとうライト（「ありがとう」を言うたびに、暗い部屋のものが光る）",
    game_html="""  <section class="game" data-n="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">The thank-you light</div>
    <div class="game-hint">The room is dark. Tap each shadow and say "thank you."</div>
    <div class="roomx">
      <button type="button" class="it" data-on="0"><span class="ie">💡</span><span class="iq">💛 Thank you</span><span class="il">A light to read by</span></button>
      <button type="button" class="it" data-on="0"><span class="ie">🍚</span><span class="iq">💛 Thank you</span><span class="il">Warm rice</span></button>
      <button type="button" class="it" data-on="0"><span class="ie">🛏️</span><span class="iq">💛 Thank you</span><span class="il">A soft bed</span></button>
      <button type="button" class="it" data-on="0"><span class="ie">🚰</span><span class="iq">💛 Thank you</span><span class="il">Clean water</span></button>
      <button type="button" class="it" data-on="0"><span class="ie">📱</span><span class="iq">💛 Thank you</span><span class="il">A message from a friend</span></button>
      <button type="button" class="it" data-on="0"><span class="ie">👟</span><span class="iq">💛 Thank you</span><span class="il">Shoes that fit</span></button>
    </div>
    <div class="glow">
      <div class="gw-head"><span class="gw-l">🔆 Room light</span> <span class="gw-n">0</span><span class="gw-of">/ 6</span></div>
      <div class="gw-bar" aria-hidden="true"><i></i></div>
    </div>
    <div class="end">✨ It was all here from the start. I just stopped seeing it.</div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">🌙 Turn the room dark again</button></div>
  </section>""",
    css="""
  /* 💡 ありがとうライト */
  .roomx { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; max-width: 440px; margin: 14px auto 0; padding: 10px;
    border-radius: 24px; background: rgba(10,12,40,.55); transition: background .6s ease; }
  .game[data-n="2"] .roomx, .game[data-n="3"] .roomx { background: rgba(60,50,90,.5); }
  .game[data-n="4"] .roomx, .game[data-n="5"] .roomx { background: rgba(140,100,60,.45); }
  .game[data-n="6"] .roomx { background: rgba(255,214,120,.5); }
  .it { display: grid; justify-items: center; align-content: start; gap: 4px; min-height: 104px; padding: 10px 4px; border: 0; border-radius: 18px;
    background: rgba(255,255,255,.06); color: #fff; font: inherit; cursor: pointer; -webkit-tap-highlight-color: transparent; touch-action: manipulation;
    transition: background .4s ease, box-shadow .4s ease; }
  .it:focus-visible { outline: 3px solid #ffd27a; outline-offset: 2px; }
  .game .ie { font-size: 36px; line-height: 1.1; filter: brightness(0) opacity(.55); transition: filter .5s ease; }
  .iq { padding: 3px 8px; border-radius: 999px; background: rgba(255,255,255,.16); font-size: 12.5px; font-weight: 900; line-height: 1.3; }
  .il { display: none; font-size: 13px; font-weight: 900; line-height: 1.3; color: #5a3a00; }
  .it[data-on="1"] { background: #fff6d6; box-shadow: 0 0 22px 6px rgba(255,210,100,.55); cursor: default; animation: boing .45s ease; }
  .it[data-on="1"] .ie { filter: none; }
  .it[data-on="1"] .iq { display: none; }
  .it[data-on="1"] .il { display: block; }
  .glow { max-width: 440px; margin: 12px auto 0; padding: 10px 14px; border-radius: 18px; background: rgba(255,255,255,.16); }
  .gw-head { display: flex; justify-content: space-between; align-items: center; gap: 6px; font-size: 15px; font-weight: 900; }
  .gw-l { margin-right: auto; text-align: left; }
  .gw-of { opacity: .8; }
  .gw-bar { position: relative; height: 14px; margin-top: 6px; border-radius: 999px; background: rgba(255,255,255,.22); overflow: hidden; }
  .gw-bar i { position: absolute; inset: 0 auto 0 0; width: 0; border-radius: 999px; background: #ffd23f; transition: width .5s cubic-bezier(.2,1.3,.4,1); }
  .end { display: none; max-width: 440px; margin: 12px auto 0; padding: 12px 14px; border-radius: 18px; background: #fff6d6; color: #8a5200;
    font-size: 16.5px; font-weight: 900; line-height: 1.45; }
  .game[data-n="6"] .end { display: block; animation: boing .5s ease; }
  .ctrl { margin-top: 12px; }
  .b-reset { min-height: 48px; font-size: 14.5px; }
""",
    dark="""  html[data-theme="dark"] .it[data-on="1"] { background: #4a3c12; }
  html[data-theme="dark"] .il { color: #ffe39a; }
  html[data-theme="dark"] .end { background: #4a3c12; color: #ffe39a; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var its = [].slice.call(g.querySelectorAll('.it')), bar = g.querySelector('.gw-bar i'), num = g.querySelector('.gw-n');
  function count() { return its.filter(function (b) { return b.getAttribute('data-on') === '1'; }).length; }
  function paint() { var n = count(); g.setAttribute('data-n', String(n)); num.textContent = String(n); bar.style.width = Math.round(n / 6 * 100) + '%'; return n; }
  its.forEach(function (b) {
    b.addEventListener('click', function () {
      if (b.getAttribute('data-on') === '1') return;
      b.setAttribute('data-on', '1');
      var n = paint();
      if (window.pengessoPop) {
        var r = b.getBoundingClientRect();
        window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, n === 6 ? ['✨', '💡', '🐧', '💛', '🌟'] : ['✨', '💛'], n === 6 ? 22 : 8);
      }
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    its.forEach(function (b) { b.setAttribute('data-on', '0'); }); paint();
  });
})();
""",
    ja={
        "The thank-you light": "ありがとうライト",
        "The room is dark. Tap each shadow and say \"thank you.\"": "部屋がまっくら。影を1つずつ押して「ありがとう」を言ってみてね。",
        "💛 Thank you": "💛 ありがとう",
        "A light to read by": "本が読める明かり",
        "Warm rice": "あたたかいごはん",
        "A soft bed": "ふかふかのベッド",
        "Clean water": "きれいな水",
        "A message from a friend": "友達からのメッセージ",
        "Shoes that fit": "足に合うくつ",
        "🔆 Room light": "🔆 部屋の明るさ",
        "/ 6": "/ 6",
        "✨ It was all here from the start. I just stopped seeing it.": "✨ ぜんぶ、最初からここにありました。見えなくなっていただけでした。",
        "🌙 Turn the room dark again": "🌙 もう一度、部屋を暗くする",
    },
)
build(d)
