from gen import build

d = dict(
    slug="print-it-and-hold-it", seq=589, url="https://www.oliverburkeman.com/physical",
    title=("Ideas only in your head float away, so print them and hold them",
           "頭の中だけだとふわふわ。印刷して、手で持てる形にする"),
    label=("Print It", "印刷する"),
    h1_emoji="📄",
    alt="A chubby alpaca wool penguin standing on green grass and holding one real sheet of printed paper with both flippers",
    section="⑱「『次に手を動かすこと』を書く」（頭の中は無限・印刷して持つ話）",
    message="頭の中とネットだけだと神様気分でふわふわ浮いて、ちょっと落ち込む。印刷して手で持てる形にすると、足が地面につく。",
    tone="素材の重さ：ふつう（考えすぎの話）\n→ 見せ方：ポップに（空色と紫と草の緑。雲に乗ったペンギンを、印刷して地面におろす）",
    game_ja="☁️ 雲の上のペンギン：頭の中のアイデアが多いほど、ペンギンが雲に乗って高く浮き、「現実っぽさ」メーターが下がる。「💭 もっと考える」でさらに上へ。「🖨️ 印刷する」を押すと、プリンターから紙が1枚飛んできてヒレに収まり、ペンギンが少し下りる。アイデアを全部紙にすると、足が地面について「🌱 これで本当に始められる」。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of fluffy alpaca wool with long soft fibers, "
            "standing on fresh green grass and proudly holding one realistic sheet of white printer paper with both flippers, a small soft white "
            "cloud floating behind it. Bright simple sky blue and lilac background with soft depth. Realistic 3D render, studio lighting, shallow "
            "depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering."),
    combo="ペンギン × アルパカウール × 印刷した1枚の紙",
    mood=["lift"], tags=["books", "productivity", "feelings"],
    pal=dict(bg="#f3f7ff", muted="#66718f", acc="#3d6fe0", acc2="#4fbf73", shadow="rgba(60,90,170,.16)",
             r1="rgba(142,197,255,.30)", r2="rgba(185,168,255,.22)", r3="rgba(127,209,138,.20)",
             h1="#17264d", photo="#e3ecff", big="#2f5fd0", bigdark="#a9c2ff",
             game="linear-gradient(180deg, #7fb8ff 0%, #a99bff 58%, #78cf8a 100%)"),
    cards=[
        dict(emoji="☁️", label=("God Mode", "神様気分"),
             s=[("Your head and the internet have no limits, so you feel like a god.", "頭の中とネットには限界がないので、神様みたいな気分になれます。")]),
        dict(emoji="📉", label=("A Little Down", "ちょっと落ちこむ"),
             s=[("But you lose the feeling of changing real life, and feel a little down.", "でも、現実を動かしている感じがなくなって、ちょっと落ち込みます。")]),
        dict(emoji="🖨️", label=("Hold It", "手で持つ"),
             s=[("So write your decision on 1 page and print it.", "だから、決めたことを1ページのメモにして印刷します。"),
                ("Holding it puts your feet on the ground.", "手で持つと、足が地面につきます。")]),
        dict(emoji="😂", label=("The Philosophy", "哲学の話"),
             s=[("Burkeman skips the big philosophy behind this.", "バークマンさんは、この話の大きな哲学は飛ばしています。"),
                ("One reason is that he does not understand it himself.", "理由の1つは、自分でも理解していないからだそうです。")]),
    ],
    game_after=2,
    game_note="雲の上のペンギン（印刷するたびに地面に近づく）",
    game_html="""  <section class="game" data-s="float" data-a="3" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Back to the ground</div>
    <div class="game-hint">The penguin is floating on its ideas. Help it land!</div>
    <div class="sky">
      <span class="printer" aria-hidden="true">🖨️</span>
      <i class="sheet" aria-hidden="true"></i>
      <div class="rider"><span class="rp">🐧</span><span class="hold">📄</span><i class="cl"></i></div>
      <div class="ground" aria-hidden="true"></div>
    </div>
    <div class="meter-row"><span class="ml">🌍 Feels real</span><div class="meter"><i></i></div></div>
    <div class="stats">
      <div class="st"><span class="sl">💡 Ideas in your head:</span> <b class="in">3</b></div>
      <div class="st"><span class="sl">📄 Papers in your flippers:</span> <b class="pn">0</b></div>
    </div>
    <div class="msg">
      <div class="m m-float">Your head is full of ideas. You feel like a god… but you are floating.</div>
      <div class="m m-think">More ideas! Higher and higher… but it feels less real. ☁️</div>
      <div class="m m-print">Clunk! A real paper in your flippers. 📄</div>
      <div class="m m-ground">🌱 Feet on the ground! Now you can really start. 🐧</div>
    </div>
    <div class="btns">
      <button class="btn b-think" type="button">💭 Think more</button>
      <button class="btn b-print" type="button">🖨️ Print it</button>
      <button class="btn ghost b-again" type="button">↺ Try again</button>
    </div>
  </section>""",
    css=r"""
  /* ☁️ 雲の上のペンギン */
  .sky { position: relative; height: 250px; max-width: 420px; margin: 14px auto 0; border-radius: 24px; overflow: hidden;
    background: linear-gradient(180deg, rgba(255,255,255,.28), rgba(255,255,255,.08)); }
  .ground { position: absolute; left: 0; right: 0; bottom: 0; height: 30px; background: linear-gradient(180deg, #6fd27f, #3fae5c); border-radius: 50% 50% 0 0 / 24px 24px 0 0; }
  .printer { position: absolute; left: 12px; bottom: 34px; font-size: 40px; line-height: 1; z-index: 2; }
  .sheet { position: absolute; left: 22px; bottom: 60px; width: 26px; height: 32px; border-radius: 3px; background: #fff; box-shadow: 0 2px 6px rgba(0,0,0,.2); opacity: 0; z-index: 3; }
  .sheet.fly { animation: fly .6s ease-out; }
  @keyframes fly { 0% { opacity: 1; transform: translate(0, 0) rotate(0); } 70% { opacity: 1; } 100% { opacity: 0; transform: translate(var(--dx, 150px), var(--dy, -60px)) rotate(200deg); } }
  .rider { position: absolute; left: 50%; bottom: 30px; width: 120px; margin-left: -40px; height: 90px; transition: transform .6s cubic-bezier(.3,1.3,.5,1); }
  .game[data-a="1"] .rider { transform: translateY(-30px); } .game[data-a="2"] .rider { transform: translateY(-62px); }
  .game[data-a="3"] .rider { transform: translateY(-94px); } .game[data-a="4"] .rider { transform: translateY(-120px); }
  .game[data-a="5"] .rider { transform: translateY(-146px); }
  .game:not([data-a="0"]) .rp { animation: float 2.4s ease-in-out infinite alternate; }
  .rp { position: absolute; left: 22px; bottom: 18px; display: inline-block; font-size: 50px; line-height: 1; z-index: 2; }
  .hold { position: absolute; left: 66px; bottom: 22px; display: inline-block; font-size: 26px; line-height: 1; z-index: 3; transform: scale(0); transition: transform .35s cubic-bezier(.2,1.6,.4,1); }
  .game.has .hold { transform: scale(1); }
  .cl { position: absolute; left: 0; right: 10px; bottom: 0; height: 34px; border-radius: 30px; background: #fff; box-shadow: 18px -12px 0 -2px #fff, 50px -6px 0 2px #fff;
    transition: opacity .5s ease, transform .5s ease; }
  .game[data-a="0"] .cl { opacity: 0; transform: scale(.4); }
  .meter-row { display: flex; align-items: center; gap: 10px; max-width: 400px; margin: 12px auto 0; font-size: 14px; font-weight: 900; }
  .meter { position: relative; flex: 1; height: 16px; border-radius: 999px; background: rgba(255,255,255,.28); overflow: hidden; }
  .meter i { position: absolute; inset: 0 auto 0 0; width: 46%; border-radius: 999px; background: #ffe066; transition: width .45s cubic-bezier(.2,1.2,.4,1); }
  .stats { display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; margin-top: 10px; }
  .st { padding: 6px 12px; border-radius: 999px; background: rgba(255,255,255,.2); font-size: 14px; font-weight: 900; }
  .st b { font-size: 18px; }
  .msg { margin-top: 12px; min-height: 52px; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .msg .m { display: none; }
  .game[data-s="float"] .m-float, .game[data-s="think"] .m-think, .game[data-s="print"] .m-print, .game[data-s="ground"] .m-ground { display: block; }
  .btns { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-top: 12px; }
  .game .b-again { display: none; }
  .game[data-s="ground"] .b-think, .game[data-s="ground"] .b-print { display: none; }
  .game[data-s="ground"] .b-again { display: inline-flex; }
  .b-print { background: #ffe066; color: #4a3500; min-width: 160px; }
""",
    dark="""  html[data-theme="dark"] .game .b-print { background: #ffe066; color: #4a3500; }
  html[data-theme="dark"] .cl { background: #f4f6ff; }""",
    js=r"""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var inEl = g.querySelector('.in'), pnEl = g.querySelector('.pn'), bar = g.querySelector('.meter i'), sheet = g.querySelector('.sheet');
  var rider = g.querySelector('.rp'), printer = g.querySelector('.printer');
  var ideas = 3, papers = 0;
  function draw(s) {
    inEl.textContent = ideas; pnEl.textContent = papers;
    g.setAttribute('data-a', String(Math.min(5, ideas)));
    bar.style.width = Math.max(8, 100 - ideas * 18) + '%';
    g.classList.toggle('has', papers > 0);
    g.setAttribute('data-s', ideas === 0 ? 'ground' : s);
  }
  g.querySelector('.b-think').addEventListener('click', function () {
    if (ideas >= 7) return;
    ideas++; draw('think');
    var r = rider.getBoundingClientRect();
    if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top, ['💡', '💭'], 5);
  });
  g.querySelector('.b-print').addEventListener('click', function () {
    if (ideas <= 0) return;
    var a = printer.getBoundingClientRect(), b = rider.getBoundingClientRect();
    sheet.style.setProperty('--dx', Math.round(b.left - a.left + 20) + 'px');
    sheet.style.setProperty('--dy', Math.round(b.top - a.top + 10) + 'px');
    sheet.classList.remove('fly'); void sheet.offsetWidth; sheet.classList.add('fly');
    ideas--; papers++; draw('print');
    if (ideas === 0) {
      setTimeout(function () {
        var r = rider.getBoundingClientRect();
        if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🌱', '📄', '🐧', '✨'], 18);
      }, 450);
      if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
    }
  });
  g.querySelector('.b-again').addEventListener('click', function () { ideas = 3; papers = 0; draw('float'); });
  draw('float');
})();
""",
    ja={
        "Back to the ground": "地面にもどろう",
        "The penguin is floating on its ideas. Help it land!": "ペンギンが、アイデアに乗ってふわふわ浮いています。おろしてあげて！",
        "🌍 Feels real": "🌍 現実っぽさ",
        "💡 Ideas in your head:": "💡 頭の中のアイデア：",
        "📄 Papers in your flippers:": "📄 ヒレの中の紙：",
        "Your head is full of ideas. You feel like a god… but you are floating.": "頭の中はアイデアでいっぱい。神様気分…でも、ふわふわ浮いています。",
        "More ideas! Higher and higher… but it feels less real. ☁️": "もっとアイデア！どんどん高く…でも、現実っぽさは減っていく ☁️",
        "Clunk! A real paper in your flippers. 📄": "ガシャン！本物の紙が、ヒレの中に 📄",
        "🌱 Feet on the ground! Now you can really start. 🐧": "🌱 足が地面につきました！これで本当に始められます 🐧",
        "💭 Think more": "💭 もっと考える",
        "🖨️ Print it": "🖨️ 印刷する",
        "↺ Try again": "↺ もう一回",
    },
)

if __name__ == "__main__":
    build(d)
