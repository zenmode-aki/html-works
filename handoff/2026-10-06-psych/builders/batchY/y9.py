from gen import build

d = dict(
    slug="five-regrets-at-the-end", seq=540,
    title=("5 regrets people often have, and what I can do today",
           "人生をふり返ったときに多い5つの後悔と、今日できること"),
    label=("5 Regrets", "5つの後悔"),
    h1_emoji="🌻",
    alt="A chubby alpaca wool penguin gently holding a real sunflower in warm morning light",
    section="仕事との向き合い方（一般論）の「人生の最期に多い後悔」",
    message="人生の最後に多い5つの後悔は、どれも毎日の小さな選び方の話。今日できることを、ひとつだけ選んでみる。",
    tone="素材の重さ：重め（人生の最後の話）\n→ 見せ方：やさしく、あたたかく（ひまわりの黄色・ピーチ・ミント。暗い色や、死を思わせる絵は使わない。勝ち負けのゲームにしない）",
    game_ja="🌻 5まいのカード：ひまわりのカードを1まいずつ押すと、くるっと回って後悔が1つと「🌱 今日できること」（自分だけのゆっくりした夜／小さなことを1つ自分の好きなほうで選ぶ／誰かに声に出して「ありがとう」／昔の友達に短いメッセージ／好きなおやつを、気にせず楽しむ）が出る。5まい開いたら、開いたカードを押して「今日のひとつ」を選ぶ（💛が付く）。点数やタイマーはなし。",
    prompt=("An extremely cute, chubby round penguin with a gentle face and a plain white belly, made of soft alpaca wool, "
            "gently hugging a single realistic fresh sunflower with a calm, happy smile. "
            "Bright simple warm peach and soft sunflower yellow background with a hint of mint, soft depth and warm morning light. "
            "Realistic 3D render, studio lighting, shallow depth of field, physically based materials, photographic. Centered composition. "
            "No humans, no text, no lettering."),
    combo="ペンギン × アルパカウール × ひまわり",
    mood=["lift", "think"], tags=["psychology", "happiness", "friends"],
    pal=dict(bg="#fffaf2", muted="#857260", acc="#e07a2e", acc2="#3fb58a", shadow="rgba(200,130,60,.15)",
             r1="rgba(255,214,90,.34)", r2="rgba(255,170,140,.2)", r3="rgba(120,220,180,.18)",
             h1="#4a2a10", photo="#ffeccf", big="#c4621c", bigdark="#ffcf9e",
             game="linear-gradient(165deg, #ffe39a 0%, #ffc3a8 55%, #bff0dc 100%)"),
    cards=[
        dict(emoji="🌻", label=("Five Regrets", "5つの後悔"),
             s=[("It is said a nurse who stayed with people in the last part of their lives often heard 5 regrets.",
                 "人生の最後の時間をすごす人たちのそばにいた看護師さんが、よく聞いた後悔が5つあるそうです。")]),
        dict(emoji="🌱", label=("Small Choices", "小さな選び方"),
             s=[("They are all about small choices we make every day.",
                 "どれも、毎日の小さな選び方の話です。"),
                ("All of them are things you can change a little, starting today.",
                 "どれも、今日から少しずつ変えられることです。")]),
        dict(emoji="💛", label=("Just One", "ひとつだけ"), big=True,
             s=[("Why not pick just 1 thing you can do today?",
                 "今日できることを、ひとつだけ選んでみませんか。")]),
    ],
    game_after=1,
    game_note="5まいのカード（後悔と、今日できること。最後に「今日のひとつ」を選ぶ）",
    game_html="""  <section class="game" data-open="0" data-pick="0" aria-live="polite">
    <div class="game-kicker">⚡ TRY IT</div>
    <div class="game-title">5 gentle cards</div>
    <div class="game-hint">Tap each sunflower card to open it. Each one has a small thing you can do today.</div>
    <div class="deck">
      <button type="button" class="rc" data-o="0" data-i="1">
        <span class="fr"><span class="fr-n">1</span><span class="fr-e">🌻</span><span class="fr-t">Tap to open</span></span>
        <span class="bk"><span class="rg">"I wish I had not worked so hard."</span><span class="td">🌱 Today: one slow evening just for me.</span><span class="pk">💛 Today's one</span></span>
      </button>
      <button type="button" class="rc" data-o="0" data-i="2">
        <span class="fr"><span class="fr-n">2</span><span class="fr-e">🌼</span><span class="fr-t">Tap to open</span></span>
        <span class="bk"><span class="rg">"I wish I had lived true to myself, not to what others expected."</span><span class="td">🌱 Today: choose 1 small thing the way I like.</span><span class="pk">💛 Today's one</span></span>
      </button>
      <button type="button" class="rc" data-o="0" data-i="3">
        <span class="fr"><span class="fr-n">3</span><span class="fr-e">🌷</span><span class="fr-t">Tap to open</span></span>
        <span class="bk"><span class="rg">"I wish I had said how I really felt."</span><span class="td">🌱 Today: say "thank you" out loud to someone.</span><span class="pk">💛 Today's one</span></span>
      </button>
      <button type="button" class="rc" data-o="0" data-i="4">
        <span class="fr"><span class="fr-n">4</span><span class="fr-e">🌸</span><span class="fr-t">Tap to open</span></span>
        <span class="bk"><span class="rg">"I wish I had stayed in touch with my friends."</span><span class="td">🌱 Today: send a short message to an old friend.</span><span class="pk">💛 Today's one</span></span>
      </button>
      <button type="button" class="rc" data-o="0" data-i="5">
        <span class="fr"><span class="fr-n">5</span><span class="fr-e">🌞</span><span class="fr-t">Tap to open</span></span>
        <span class="bk"><span class="rg">"I wish I had let myself be happier."</span><span class="td">🌱 Today: enjoy my favorite sweet, with no guilt.</span><span class="pk">💛 Today's one</span></span>
      </button>
    </div>
    <div class="prog"><span class="pg-l">🌻 Opened:</span> <span class="pg-n">0</span><span class="pg-of">/ 5</span></div>
    <div class="msg">
      <div class="m-all">💛 All open. Now tap 1 card to choose "today's one."</div>
      <div class="m-pick">🌻 Nice. Just this one, today. That is enough.</div>
    </div>
  </section>""",
    css="""
  /* 🌻 5まいのカード（やさしい色だけ。勝ち負けなし） */
  .game { color: #5a3a20; }
  .game .btn.ghost { color: #5a3a20; box-shadow: inset 0 0 0 2px rgba(90,58,32,.4); }
  .deck { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 440px; margin: 14px auto 0; }
  .rc { position: relative; display: block; min-height: 150px; padding: 0; border: 0; border-radius: 22px; background: transparent; font: inherit; color: inherit;
    cursor: pointer; -webkit-tap-highlight-color: transparent; touch-action: manipulation; transition: transform .18s ease-in; }
  .rc:last-child { grid-column: 1 / -1; min-height: 120px; }
  .rc:focus-visible { outline: 3px solid #e07a2e; outline-offset: 3px; }
  .rc.turn { transform: scaleX(0); }
  .fr, .bk { display: grid; align-content: center; justify-items: center; gap: 6px; min-height: inherit; padding: 12px 10px; border-radius: 22px; }
  .fr { background: rgba(255,255,255,.55); box-shadow: 0 5px 0 rgba(200,130,60,.2); }
  .fr-n { font-size: 14px; font-weight: 900; opacity: .7; }
  .game .fr-e { display: inline-block; font-size: 40px; line-height: 1; animation: sway 3s ease-in-out infinite alternate; }
  @keyframes sway { from { transform: rotate(-6deg); } to { transform: rotate(6deg); } }
  .fr-t { font-size: 13.5px; font-weight: 900; }
  .bk { display: none; background: #fff; box-shadow: 0 5px 0 rgba(200,130,60,.22); text-align: left; justify-items: start; }
  .rc[data-o="1"] .fr { display: none; }
  .rc[data-o="1"] .bk { display: grid; }
  .rg { font-size: 14.5px; font-weight: 900; line-height: 1.4; color: #6a4428; }
  .td { padding: 6px 10px; border-radius: 14px; background: #e6f8ef; color: #1f6a4c; font-size: 13.5px; font-weight: 900; line-height: 1.35; }
  .pk { display: none; padding: 3px 10px; border-radius: 999px; background: #ffd23f; color: #5a3a00; font-size: 13px; font-weight: 900; }
  .rc[data-p="1"] .bk { box-shadow: 0 0 0 4px #ffd23f, 0 5px 0 rgba(200,130,60,.22); }
  .rc[data-p="1"] .pk { display: inline-block; animation: boing .45s ease; }
  .prog { display: inline-block; margin-top: 12px; padding: 6px 14px; border-radius: 999px; background: rgba(255,255,255,.5); font-size: 15px; font-weight: 900; }
  .pg-of { margin-left: 4px; opacity: .8; }
  .msg { max-width: 440px; margin: 10px auto 0; min-height: 26px; font-size: 16px; font-weight: 900; line-height: 1.45; }
  .msg > div { display: none; }
  .game[data-open="5"][data-pick="0"] .m-all { display: block; }
  .game[data-pick="1"] .m-pick { display: block; padding: 12px 14px; border-radius: 18px; background: #fff; animation: boing .5s ease; }
""",
    dark="""  html[data-theme="dark"] .game { color: #4a2e18; }
  html[data-theme="dark"] .bk, html[data-theme="dark"] .game[data-pick="1"] .m-pick { background: #fffaf2; }""",
    js="""
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var cards = [].slice.call(g.querySelectorAll('.rc')), num = g.querySelector('.pg-n');
  function opened() { return cards.filter(function (c) { return c.getAttribute('data-o') === '1'; }).length; }
  cards.forEach(function (c) {
    c.addEventListener('click', function () {
      if (c.getAttribute('data-o') !== '1') {
        /* rotateY は iPhone で裏の字が鏡うつしに透けるので、横にしぼんで → 中身を入れかえ → ひらく */
        c.classList.add('turn');
        setTimeout(function () {
          c.setAttribute('data-o', '1'); c.classList.remove('turn');
          var n = opened(); num.textContent = String(n); g.setAttribute('data-open', String(n));
        }, 180);
        return;
      }
      if (opened() < 5) return;
      cards.forEach(function (x) { x.setAttribute('data-p', x === c ? '1' : '0'); });
      g.setAttribute('data-pick', '1');
      if (window.pengessoPop) {
        var r = c.getBoundingClientRect();
        window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🌻', '💛', '🐧', '🌱'], 14);
      }
    });
  });
})();
""",
    ja={
        "5 gentle cards": "やさしい5まいのカード",
        "Tap each sunflower card to open it. Each one has a small thing you can do today.": "ひまわりのカードを1まいずつ押して、開いてみてね。どのカードにも、今日できる小さなことが入っています。",
        "Tap to open": "押して開く",
        "\"I wish I had not worked so hard.\"": "「あんなに働きすぎなければよかった」",
        "🌱 Today: one slow evening just for me.": "🌱 今日：自分のためだけの、ゆっくりした夜をひとつ。",
        "\"I wish I had lived true to myself, not to what others expected.\"": "「人の期待じゃなく、自分に正直に生きればよかった」",
        "🌱 Today: choose 1 small thing the way I like.": "🌱 今日：小さなことを1つ、自分の好きなほうで選ぶ。",
        "\"I wish I had said how I really felt.\"": "「勇気を出して、気持ちを伝えればよかった」",
        "🌱 Today: say \"thank you\" out loud to someone.": "🌱 今日：誰かに、声に出して「ありがとう」と言う。",
        "\"I wish I had stayed in touch with my friends.\"": "「友達と、連絡をとり続ければよかった」",
        "🌱 Today: send a short message to an old friend.": "🌱 今日：昔の友達に、短いメッセージを送る。",
        "\"I wish I had let myself be happier.\"": "「自分が幸せになるのを、許してあげればよかった」",
        "🌱 Today: enjoy my favorite sweet, with no guilt.": "🌱 今日：好きなおやつを、気にせず楽しむ。",
        "💛 Today's one": "💛 今日のひとつ",
        "🌻 Opened:": "🌻 開いたカード：",
        "/ 5": "/ 5",
        "💛 All open. Now tap 1 card to choose \"today's one.\"": "💛 ぜんぶ開きました。カードを1まい押して「今日のひとつ」を選んでね。",
        "🌻 Nice. Just this one, today. That is enough.": "🌻 いいですね。今日は、これひとつだけ。それで十分です。",
    },
)
build(d)
