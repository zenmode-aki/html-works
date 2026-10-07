EV = [
    ("It starts to rain on your day off. ☔", "休みの日に、雨が降ってきた。☔",
     '🌸 "A good day for a book and tea!"', "🌸「本とお茶の日にしよう！」",
     '😤 "Rain again?! Worst day ever."', "😤「また雨！？最悪の日だ」"),
    ("The train is 5 minutes late. 🚃", "電車が5分おくれている。🚃",
     '🌸 "5 more minutes to read my book."', "🌸「本を5分よけいに読める」",
     '😤 "Why does this always happen to me?!"', "😤「なんでいつも私ばっかり！？」"),
    ("You drop your ice cream. 🍦", "アイスを落とした。🍦",
     '🌸 "Well, the ants get a party today."', "🌸「まあ、今日はアリさんのパーティーだ」",
     '😤 "Nothing goes right for me!"', "😤「何もうまくいかない！」"),
    ("Your favorite cafe is full. ☕", "お気に入りのカフェが満席。☕",
     "🌸 \"Let's find a new cafe!\"", "🌸「新しいカフェを探そう！」",
     '😤 "Ugh, everything is against me."', "😤「もう、全部が私の邪魔をする」"),
    ("Your hair is sticking up this morning. 🌀", "朝、寝ぐせがすごい。🌀",
     '🌸 "A new hairstyle! Not bad."', "🌸「新しい髪型だ！悪くない」",
     '😤 "My whole day is ruined."', "😤「今日はもう全部ダメだ」"),
    ("You wake up late on Sunday. ⏰", "日曜日に寝坊した。⏰",
     '🌸 "Wow, I really slept well!"', "🌸「わあ、よく寝た！」",
     '😤 "I wasted my Sunday."', "😤「日曜日を無駄にした」"),
]
import html as _h
_ev = "\n".join(f'      <span class="e{i+1}">{_h.escape(e[0], quote=False)}</span>' for i, e in enumerate(EV))
_k = "".join(f'<span class="k{i+1}">{_h.escape(e[2], quote=False)}</span>' for i, e in enumerate(EV))
_g = "".join(f'<span class="g{i+1}">{_h.escape(e[4], quote=False)}</span>' for i, e in enumerate(EV))
_ja = {}
for e in EV:
    _ja[e[0]] = e[1]; _ja[e[2]] = e[3]; _ja[e[4]] = e[5]
_css_ev = ",\n  ".join(f'.game[data-e="{i}"] .e{i}, .game[data-e="{i}"] .k{i}, .game[data-e="{i}"] .g{i}' for i in range(1, 7))
_lv = '<span class="lv1">🌱 Tiny trail</span><span class="lv2">👣 Path</span><span class="lv3">🛣️ Road</span><span class="lv4">🚀 Highway</span>'

A = dict(
    slug="personality-can-change", seq=414,
    title="Your personality can change, because the thoughts you use become wide roads",
    title_ja="性格は変えられる。よく使う考え方ほど、脳の道が太くなる",
    label="Brain Roads", label_ja="脳の道",
    float="🛣️",
    alt="A chubby low-poly wood and paper penguin standing at a real wooden signpost with two blank arrows",
    mood=["lift", "learn"], tags=["psychology", "mindset", "feelings"],
    src_no="16", src_title="性格は変えられる",
    center="性格は変えられる。よく使う考え方ほど脳の道が太くなるので、何歳からでも変わる。",
    tone="素材の重さ：真面目（性格・遺伝・脳）\n→ 見せ方：ポップに（緑と紫。脳の道を自分で太くするゲームで遊べる）",
    tone_css="真面目な話 → ポップに。緑と紫",
    game_name="脳の道づくり",
    play="🛣️ 脳の道づくり：脳の地図に「😤 プンプンの道」（最初は太い）と「🌸 やさしい道」（最初は細いけもの道）。出来事が1つずつ出る（休みの日の雨／電車が5分おくれ／アイスを落とした／カフェが満席／寝ぐせ／日曜に寝坊）。🌸 と 😤 の考え方から1つ選ぶと、ペンギンがその道を歩いて、使った道が太くなる（使わない道は細く・うすくなる）。今の太いほうに「🤖 自動運転」の黄色い輪が付く＝脳が勝手に選ぶクセ。🌸 を3回選ぶと道の太さが逆転して「🎉 クセが入れかわった！」。道の太さは けもの道 → 小道 → 道路 → 高速道路。「↺ 最初から」。",
    prompt="An extremely cute, chubby round penguin with a gentle face and a plain white belly (no rings or patterns on the belly), made in a low-poly 3D wood and paper style with crisp faceted planes and warm natural wood tones, standing at a fork in a soft green path next to one realistic old wooden signpost with two blank wooden arrows pointing different ways, looking up at the brighter path with a hopeful smile. Bright fresh green and soft lavender background with gentle depth, simple and uncluttered. Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. No humans, no text, no lettering.",
    combo="ペンギン × ローポリの木と紙 × 木の道しるべ",
    pal=dict(bg="#f2fbf5", text="#1f3329", muted="#5e7568", a="#0b8f50", b="#7c4dff", c="#ffd43b", d="#ff7a59",
             big="#0b8a4b", bigdark="#9be7bf", h1="#12341f", ink="#1f3329", shadowc="rgba(30,120,80,.16)",
             bg1="rgba(124,77,255,.16)", bg2="rgba(255,212,59,.28)", bg3="rgba(15,157,88,.14)", photo="#dff5e8",
             game="linear-gradient(150deg, #12a565 0%, #0f8f8a 50%, #5b5bd6 100%)"),
    cards=[
        dict(e="🧬", l="Born This Way?", lj="生まれつき？", s=[(
            "We often think personality comes from birth, but it is said genes are about 40% of it.",
            "性格は生まれつきだと思いがちですが、遺伝の影響は4割くらいだと言われています。", False)]),
        dict(e="🔓", l="The Other 60%", lj="残りの6割", s=[(
            "This means you can change the rest from now.",
            "つまり残りは、これから変えられるということです。", False)]),
        dict(e="🛣️", l="Brain Roads", lj="脳の道", s=[(
            "It seems the ways of thinking you use often become wider roads in your brain.",
            "よく使う考え方ほど、脳の中の道が太くなっていくそうです。", False)]),
        "GAME",
        dict(e="🎂", l="Any Age", lj="何歳からでも", s=[(
            "Your personality can change at any age.",
            "性格は、何歳からでも変わります。", True)]),
        dict(e="🎬", l="Play The Hero", lj="主人公になりきる", s=[(
            "For example, it seems good to act like your favorite anime hero.",
            "たとえば、好きなアニメの主人公になりきってみるのもいいそうです。", False)]),
    ],
    game_html=r'''
  <!-- ⚡ 触って遊べる部品：脳の道づくり（選んだ考え方の道が太くなる。太いほうを脳が自動で選ぶ） -->
  <section class="game" data-e="1" data-auto="g" data-sw="0" data-flip="0" data-busy="0" data-lg="4" data-lk="1" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">Build a new road in your brain</div>
    <div class="game-hint">Something happens. Pick a thought. The road you use gets wider.</div>
    <div class="map">
      <div class="rd rd-g">
        <div class="rd-head"><span class="rd-l">😤 Grumpy road</span><span class="lv">LVS</span></div>
        <div class="rd-track" aria-hidden="true"><i class="rd-w"></i><span class="walker">🐧</span></div>
      </div>
      <div class="rd rd-k">
        <div class="rd-head"><span class="rd-l">🌸 Kind road</span><span class="lv">LVS</span></div>
        <div class="rd-track" aria-hidden="true"><i class="rd-w"></i><span class="walker">🐧</span></div>
      </div>
    </div>
    <div class="auto"><span class="a-g">🤖 Autopilot: your brain takes the 😤 road.</span><span class="a-k">🤖 Autopilot: your brain takes the 🌸 road now!</span></div>
    <div class="ev">
EVS
    </div>
    <div class="picks">
      <button type="button" class="btn pk pk-g" data-w="g">GS</button>
      <button type="button" class="btn pk pk-k" data-w="k">KS</button>
    </div>
    <div class="tally"><span class="tl">🌸 Kind thoughts:</span> <span class="kn">0</span></div>
    <div class="msg m-switch">🎉 Habit switch! The kind road is the wide one now.</div>
    <div class="ctrl"><button type="button" class="btn ghost b-reset">↺ Start over</button></div>
  </section>
'''.replace("LVS", _lv).replace("EVS", _ev).replace("GS", _g).replace("KS", _k),
    game_ja=dict({
        "Build a new road in your brain": "脳に新しい道をつくろう",
        "Something happens. Pick a thought. The road you use gets wider.": "何かが起きます。考え方を選んでね。使った道が太くなります。",
        "😤 Grumpy road": "😤 プンプンの道",
        "🌸 Kind road": "🌸 やさしい道",
        "🌱 Tiny trail": "🌱 けもの道",
        "👣 Path": "👣 小道",
        "🛣️ Road": "🛣️ 道路",
        "🚀 Highway": "🚀 高速道路",
        "🤖 Autopilot: your brain takes the 😤 road.": "🤖 自動運転：脳は 😤 の道を選びます。",
        "🤖 Autopilot: your brain takes the 🌸 road now!": "🤖 自動運転：脳が 🌸 の道を選ぶようになった！",
        "🌸 Kind thoughts:": "🌸 やさしい考え：",
        "🎉 Habit switch! The kind road is the wide one now.": "🎉 クセが入れかわった！やさしい道のほうが太くなりました。",
        "↺ Start over": "↺ 最初から",
    }, **_ja),
    css=r'''
  /* 🛣️ 脳の道づくり */
  .map { display: grid; gap: 10px; max-width: 420px; margin: 14px auto 0; padding: 12px; border-radius: 22px; background: #fff; color: var(--ink); text-align: left; }
  .rd-head { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 2px 8px; font-size: 15px; font-weight: 900; }
  .rd-g .rd-l { color: #5b4a86; }
  .rd-k .rd-l { color: #0b7a43; }
  .lv { font-size: 12.5px; font-weight: 900; padding: 3px 9px; border-radius: 999px; background: #eef1ec; color: #4c5a50; }
  .lv span { display: none; }
  .game[data-lg="1"] .rd-g .lv1, .game[data-lg="2"] .rd-g .lv2, .game[data-lg="3"] .rd-g .lv3, .game[data-lg="4"] .rd-g .lv4,
  .game[data-lk="1"] .rd-k .lv1, .game[data-lk="2"] .rd-k .lv2, .game[data-lk="3"] .rd-k .lv3, .game[data-lk="4"] .rd-k .lv4 { display: inline; }
  .rd-track { position: relative; display: flex; align-items: center; height: 50px; margin-top: 6px; padding: 0 4px; border-radius: 14px; background: #e3f3df; overflow: hidden; }
  .rd-w { position: relative; display: block; width: 100%; height: 6px; border-radius: 999px; transition: height .55s cubic-bezier(.2,1.3,.4,1), opacity .55s ease; }
  .rd-g .rd-w { background: #6b5b95; }
  .rd-k .rd-w { background: #ffb703; }
  .rd-w.wide::after { content: ""; position: absolute; left: 8px; right: 8px; top: 50%; height: 3px; transform: translateY(-50%);
    background: repeating-linear-gradient(90deg, rgba(255,255,255,.95) 0 16px, transparent 16px 30px); }
  .walker { position: absolute; top: 50%; left: -40px; font-size: 26px; line-height: 1; transform: translateY(-60%); }
  @keyframes walk { from { left: 0; } to { left: calc(100% - 32px); } }
  .walker.go { animation: walk 1s ease-in-out both; }
  .auto { max-width: 420px; margin: 10px auto 0; font-size: 14.5px; font-weight: 900; line-height: 1.4; }
  .auto span { display: none; }
  .game[data-auto="g"] .a-g, .game[data-auto="k"] .a-k { display: inline; }
  .ev { display: flex; align-items: center; justify-content: center; max-width: 420px; min-height: 58px; margin: 12px auto 0; padding: 10px 14px;
    border-radius: 18px; background: rgba(255,255,255,.2); font-size: 17px; font-weight: 900; line-height: 1.4; }
  .ev span, .pk span { display: none; }
  ''' + _css_ev + r''' { display: inline; }
  .game[data-e] .ev span { animation: g-in .35s ease-out; }
  .picks { display: flex; flex-direction: column; gap: 12px; max-width: 380px; margin: 14px auto 0; }
  .pk { width: 100%; position: relative; }
  .pk-g { color: #5b4a86; }
  .pk-k { color: #0b7a43; }
  .game[data-flip="1"] .pk-k { order: -1; }
  .game[data-auto="g"] .pk-g, .game[data-auto="k"] .pk-k { box-shadow: 0 0 0 4px #ffe066, 0 6px 0 rgba(0,0,0,.16), 0 12px 22px rgba(0,0,0,.12); }
  .game[data-auto="g"] .pk-g::after, .game[data-auto="k"] .pk-k::after { content: "🤖"; position: absolute; top: -12px; right: -6px; font-size: 22px; }
  .game[data-busy="1"] .picks { pointer-events: none; opacity: .7; }
  .tally { margin-top: 14px; font-size: 15.5px; font-weight: 900; }
  .kn { font-variant-numeric: tabular-nums; display: inline-block; }
  .m-switch { display: none; }
  .game[data-sw="1"] .m-switch { display: block; animation: g-pop .45s cubic-bezier(.2,1.4,.4,1); }
''',
    dark=r'''
  html[data-theme="dark"] .map { background: #f1edf8; }
''',
    js=r'''
/* 🛣️ 脳の道づくり：JS は data-*・class・style（道の太さ）・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var wG = g.querySelector('.rd-g .rd-w'), wK = g.querySelector('.rd-k .rd-w'),
      walkG = g.querySelector('.rd-g .walker'), walkK = g.querySelector('.rd-k .walker'), kn = g.querySelector('.kn');
  var G = 34, K = 6, e = 1, kind = 0, timer = 0;
  function lvl(w) { return w < 12 ? 1 : w < 22 ? 2 : w < 32 ? 3 : 4; }
  function paint() {
    wG.style.height = G + 'px'; wK.style.height = K + 'px';
    wG.style.opacity = String(0.35 + 0.65 * (G - 4) / 36);
    wK.style.opacity = String(0.55 + 0.45 * (K - 4) / 36);
    wG.classList.toggle('wide', G >= 20); wK.classList.toggle('wide', K >= 20);
    g.setAttribute('data-lg', String(lvl(G))); g.setAttribute('data-lk', String(lvl(K)));
    g.setAttribute('data-auto', K > G ? 'k' : 'g');
    g.setAttribute('data-e', String(e)); g.setAttribute('data-flip', e % 2 ? '0' : '1');
    kn.textContent = String(kind);
  }
  function walk(el) { el.classList.remove('go'); void el.offsetWidth; el.classList.add('go'); }
  [].forEach.call(g.querySelectorAll('.pk'), function (b) {
    b.addEventListener('click', function () {
      if (g.getAttribute('data-busy') === '1') return;
      var before = g.getAttribute('data-auto');
      if (b.getAttribute('data-w') === 'k') { K = Math.min(40, K + 7); G = Math.max(4, G - 5); kind++; walk(walkK); }
      else { G = Math.min(40, G + 4); K = Math.max(4, K - 2); walk(walkG); }
      g.setAttribute('data-busy', '1');
      paint();
      var after = g.getAttribute('data-auto');
      if (before === 'g' && after === 'k') {
        g.setAttribute('data-sw', '1');
        if (window.pengessoPop) { var r = wK.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🌸', '🛣️', '🐧', '✨', '🧠'], 20); }
        if (navigator.vibrate) { try { navigator.vibrate(30); } catch (err) {} }
      } else if (after === 'g') { g.setAttribute('data-sw', '0'); }
      clearTimeout(timer);
      timer = setTimeout(function () { e = e % 6 + 1; g.setAttribute('data-busy', '0'); paint(); }, 950);
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    clearTimeout(timer); G = 34; K = 6; e = 1; kind = 0;
    g.setAttribute('data-sw', '0'); g.setAttribute('data-busy', '0');
    walkG.classList.remove('go'); walkK.classList.remove('go'); paint();
  });
  paint();
})();
''',
)
