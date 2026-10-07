from gen import build

d = dict(
    slug="no-magic-technique", seq=587, url="https://www.oliverburkeman.com/dailyish",
    title=("There is no magic technique, so look at what you made",
           "魔法のテクニックはない。見るのは「何が生まれたか」"),
    label=("No Magic", "魔法はない"),
    h1_emoji="🎩",
    alt="A chubby hand-embroidered felt penguin peeking into a real black magician's top hat with a curious face",
    section="⑰「習慣は『だいたい毎日』」（魔法のテクニックの話）",
    message="成果を自動で生む魔法のテクニックはない。欲しくなるときは裏に理由がある。大事なのは記録より、何が生まれたか。",
    tone="素材の重さ：ちょっと真面目（完璧主義と記録）\n→ 見せ方：ポップに（紫と金色のマジックショー。シルクハットから理由が出てくる）",
    game_ja="🎩 魔法のシルクハット：ハットをタップすると、ウサギではなく「魔法が欲しくなる本当の理由」のカードが出てくる（やり方がわからない／実はやりたくない／完璧な記録で自分の価値を証明したい）。3つ全部出すと、「📅 記録」と「🎁 生まれたもの」を切り替えられる。記録で見ると「鎖が2回切れた…」、生まれたもので見ると「12ページ書けた！」。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of hand-embroidered felt with neat "
            "visible stitches, peeking curiously into a realistic black magician's top hat that stands on a small round table. Bright simple "
            "lavender and warm gold background with soft depth. Realistic 3D render, studio lighting, shallow depth of field, physically based "
            "materials, photographic. Centered composition. No humans, no text, no lettering."),
    combo="ペンギン × 手刺しゅうのフェルト × 黒いシルクハット",
    mood=["think"], tags=["books", "productivity", "mindset"],
    pal=dict(bg="#f8f4ff", muted="#77698f", acc="#7b3fe4", acc2="#e05bb8", shadow="rgba(90,50,160,.18)",
             r1="rgba(255,183,3,.22)", r2="rgba(123,63,228,.18)", r3="rgba(224,91,184,.14)",
             h1="#2a1550", photo="#efe6ff", big="#6a2fd6", bigdark="#cbb2ff",
             game="linear-gradient(155deg, #3b1f7a 0%, #7b3fe4 55%, #e05bb8 100%)"),
    cards=[
        dict(emoji="❌", label=("The Famous Chain", "有名な鎖"),
             s=[("A famous trick says: \"Never break the chain of X marks on your calendar.\"",
                 "「カレンダーに✖をつけて、鎖を切らすな」という有名なテクニックがあります。"),
                ("But Burkeman says even the comedian behind it did not think much of it.",
                 "でもバークマンさんによると、名前のもとになったコメディアン本人は、そんなに大した話だと思っていなかったらしいです。")]),
        dict(emoji="🪄", label=("No Magic", "魔法はない"),
             s=[("There is no magic technique that makes results.", "成果を自動で生む魔法のテクニックはありません。"),
                ("If you still want one, there is a hidden reason.", "それでも欲しくなるときは、裏に理由があります。")]),
        dict(emoji="🎁", label=("What You Made", "生まれたもの"), big=True,
             s=[("What matters is not a perfect record, but what you made.", "大事なのは、記録が完璧かどうかではなく、何が生まれたかです。")]),
        dict(emoji="📌", label=("It Hit Me", "刺さった"),
             s=[("As a perfectionist, this really hit me.", "完璧主義の私には、これが刺さりました。")]),
    ],
    game_after=2,
    game_note="魔法のシルクハット（出てくるのはウサギじゃなくて理由）",
    game_html="""  <section class="game" data-s="hat" data-c="-1" data-v="rec" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">The magic hat</div>
    <div class="game-hint">Tap the hat. A magic technique comes out… maybe?</div>
    <div class="show">
      <button class="hat-btn" type="button" aria-label="Tap the hat"><span class="hat">🎩</span><span class="spark">✨</span></button>
      <div class="reason">
        <div class="rz rz-none">No rabbit. No magic. Tap again…</div>
        <div class="rz rz0"><span class="rz-e">🧭</span> Maybe I do not know how to start.</div>
        <div class="rz rz1"><span class="rz-e">🙈</span> Maybe I do not really want to do it.</div>
        <div class="rz rz2"><span class="rz-e">🏅</span> Maybe I want to prove my worth with a perfect record.</div>
      </div>
      <div class="found"><span class="fl">🔍 Hidden reasons found:</span> <b class="fn">0</b><span class="of">/3</span></div>
    </div>
    <div class="view">
      <div class="tabs">
        <button class="tab t-rec" type="button">📅 The record</button>
        <button class="tab t-made" type="button">🎁 What you made</button>
      </div>
      <div class="panel p-rec">
        <div class="chain" aria-hidden="true"><i class="ok"></i><i class="ok"></i><i class="ok"></i><i class="ok"></i><i class="no"></i><i class="ok"></i><i class="ok"></i><i class="ok"></i><i class="ok"></i><i class="ok"></i><i class="no"></i><i class="ok"></i><i class="ok"></i><i class="ok"></i></div>
        <div class="cap">💔 The chain broke 2 times. Failure…?</div>
      </div>
      <div class="panel p-made">
        <div class="pages" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i><span class="pg-pen">🐧</span></div>
        <div class="cap">📄 12 pages written in 14 days! This is what matters.</div>
      </div>
    </div>
    <div class="btns">
      <button class="btn ghost b-again" type="button">↺ Try again</button>
    </div>
  </section>""",
    css=r"""
  /* 🎩 魔法のシルクハット */
  .show { margin: 14px auto 0; max-width: 420px; }
  .hat-btn { position: relative; width: 130px; height: 120px; border: 0; border-radius: 30px; background: rgba(255,255,255,.14); cursor: pointer; padding: 0;
    box-shadow: inset 0 0 0 3px rgba(255,255,255,.4); touch-action: manipulation; -webkit-tap-highlight-color: transparent; }
  .hat { display: inline-block; font-size: 78px; line-height: 1; }
  .hat-btn.shake .hat { animation: shake .45s ease; }
  .spark { position: absolute; right: 12px; top: 8px; font-size: 26px; animation: float 1.6s ease-in-out infinite alternate; }
  .reason { margin-top: 12px; min-height: 76px; display: flex; align-items: center; justify-content: center; }
  .game .rz { display: none; padding: 12px 14px; border-radius: 18px; background: #fff; color: #3b1f7a; font-size: 16px; font-weight: 900; line-height: 1.4; }
  .game[data-c="-1"] .rz-none, .game[data-c="0"] .rz0, .game[data-c="1"] .rz1, .game[data-c="2"] .rz2 { display: block; animation: boing .45s ease; }
  .game[data-c="-1"] .rz-none { background: rgba(255,255,255,.2); color: #fff; }
  .game[data-s="hat"][data-c="-1"]:not(.started) .rz-none { visibility: hidden; }
  .found { margin-top: 10px; font-size: 15px; font-weight: 900; }
  .found b { display: inline-block; min-width: 1.4em; padding: 1px 7px; border-radius: 999px; background: #ffd166; color: #3b1f7a; }
  .game .view { display: none; }
  .game[data-s="view"] .view { display: block; }
  .view { margin: 16px auto 0; max-width: 420px; }
  .tabs { display: flex; justify-content: center; gap: 8px; flex-wrap: wrap; }
  .tab { min-height: 48px; padding: 8px 16px; border: 0; border-radius: 999px; font: inherit; font-size: 15px; font-weight: 900; cursor: pointer;
    background: rgba(255,255,255,.2); color: #fff; box-shadow: inset 0 0 0 2px rgba(255,255,255,.6); touch-action: manipulation; -webkit-tap-highlight-color: transparent; }
  .game[data-v="rec"] .t-rec, .game[data-v="made"] .t-made { background: #fff; color: #5a2bb8; box-shadow: 0 5px 0 rgba(0,0,0,.18); }
  .game .panel { display: none; margin-top: 12px; padding: 14px 10px; border-radius: 20px; background: rgba(255,255,255,.16); }
  .game[data-v="rec"] .p-rec, .game[data-v="made"] .p-made { display: block; animation: boing .4s ease; }
  .chain { display: grid; grid-template-columns: repeat(7, 1fr); gap: 4px; max-width: 280px; margin: 0 auto; }
  .chain i { aspect-ratio: 1; border-radius: 8px; position: relative; }
  .chain i::after { position: absolute; inset: 0; display: grid; place-items: center; font-style: normal; font-weight: 900; font-size: 16px; }
  .chain i.ok { background: rgba(255,255,255,.85); } .chain i.ok::after { content: "✕"; color: #7b3fe4; }
  .chain i.no { background: #ff6b6b; } .chain i.no::after { content: "!"; color: #fff; }
  .pages { position: relative; width: 150px; height: 120px; margin: 0 auto; }
  .pages i { position: absolute; left: 20px; width: 100px; height: 110px; border-radius: 6px; background: #fff; box-shadow: 0 2px 6px rgba(0,0,0,.18);
    background-image: repeating-linear-gradient(180deg, transparent 0 14px, rgba(123,63,228,.18) 14px 16px); }
  .pages i:nth-child(1) { transform: rotate(-9deg); } .pages i:nth-child(2) { transform: rotate(-5deg); } .pages i:nth-child(3) { transform: rotate(-2deg); }
  .pages i:nth-child(4) { transform: rotate(2deg); } .pages i:nth-child(5) { transform: rotate(5deg); } .pages i:nth-child(6) { transform: rotate(0); }
  .pg-pen { position: absolute; right: -4px; bottom: -6px; font-size: 40px; }
  .cap { margin-top: 12px; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .btns { display: flex; justify-content: center; margin-top: 12px; }
  .game .b-again { display: none; }
  .game[data-s="view"] .b-again { display: inline-flex; }
""",
    dark="""  html[data-theme="dark"] .game .rz:not(.rz-none) { background: #f4f0fa; color: #3b1f7a; }""",
    js=r"""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var hb = g.querySelector('.hat-btn'), fn = g.querySelector('.fn');
  var seen = [], order = [0, 1, 2], tries = 0, vt = 0;
  function shuffle(a) { for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  shuffle(order);
  hb.addEventListener('click', function () {
    if (g.getAttribute('data-s') !== 'hat') return;
    g.classList.add('started');
    hb.classList.remove('shake'); void hb.offsetWidth; hb.classList.add('shake');
    tries++;
    /* 1回目はウサギも魔法も出ない。そのあと理由が1つずつ出てくる */
    if (tries === 1) { g.setAttribute('data-c', '-1'); return; }
    var c = order[seen.length];
    seen.push(c); fn.textContent = seen.length;
    g.setAttribute('data-c', String(c));
    var r = hb.getBoundingClientRect();
    if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + 20, ['✨', '🃏', '🪄'], 8);
    if (seen.length >= 3) {
      vt = setTimeout(function () {
        g.setAttribute('data-s', 'view'); g.setAttribute('data-v', 'rec');
      }, 1300);
    }
  });
  g.querySelector('.t-rec').addEventListener('click', function () { g.setAttribute('data-v', 'rec'); });
  g.querySelector('.t-made').addEventListener('click', function (e) {
    g.setAttribute('data-v', 'made');
    var r = e.currentTarget.getBoundingClientRect();
    if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height + 60, ['📄', '🎁', '🐧', '✨'], 16);
  });
  g.querySelector('.b-again').addEventListener('click', function () {
    clearTimeout(vt); seen = []; tries = 0; shuffle(order); fn.textContent = '0';
    g.classList.remove('started'); g.setAttribute('data-c', '-1'); g.setAttribute('data-s', 'hat'); g.setAttribute('data-v', 'rec');
  });
})();
""",
    ja={
        "The magic hat": "魔法のシルクハット",
        "Tap the hat. A magic technique comes out… maybe?": "ハットをタップしてね。魔法のテクニックが出てくる…かも？",
        "Tap the hat": "ハットをタップ",
        "No rabbit. No magic. Tap again…": "ウサギも魔法も出てこない。もう一回タップ…",
        "Maybe I do not know how to start.": "もしかして、やり方がわからない。",
        "Maybe I do not really want to do it.": "もしかして、実はやりたくない。",
        "Maybe I want to prove my worth with a perfect record.": "もしかして、完璧な記録で、自分の価値を証明したい。",
        "🔍 Hidden reasons found:": "🔍 見つけた本当の理由：",
        "📅 The record": "📅 記録",
        "🎁 What you made": "🎁 生まれたもの",
        "💔 The chain broke 2 times. Failure…?": "💔 鎖が2回切れた。失敗…？",
        "📄 12 pages written in 14 days! This is what matters.": "📄 14日で12ページ書けた！大事なのはこっち。",
        "↺ Try again": "↺ もう一回",
    },
)

if __name__ == "__main__":
    build(d)
