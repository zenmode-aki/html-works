/* 🌐 言語の切り替え（python3 tools/i18n.py が各ページに埋め込みます。ここを直したら i18n.py を流し直す）
   ・英語の本文はそのまま。日本語などは「英文 → 訳」の対応表で、文章のかたまりごとに差し替える
   ・対応表にない文は英語のまま残る（壊れるより、英語が残るほうがまし）
   ・選んだ言語は localStorage に覚える。?lang=ja でも指定できる */
(function () {
  var holder = document.getElementById('i18n-data');
  if (!holder) return;
  var DATA;
  try { DATA = JSON.parse(holder.textContent); } catch (e) { return; }
  var LANGS = DATA.langs || {};
  var KEY = 'pengesso-lang';
  var avail = ['en'].concat(Object.keys(LANGS));
  var NAMES = { en: 'English' };
  Object.keys(LANGS).forEach(function (k) { NAMES[k] = LANGS[k].name || k; });

  function pick() {
    var q = (location.search.match(/[?&]lang=([a-zA-Z-]+)/) || [])[1];
    if (q && avail.indexOf(q) >= 0) { save(q); return q; }
    try { var s = localStorage.getItem(KEY); if (s && avail.indexOf(s) >= 0) return s; } catch (e) {}
    var nl = navigator.languages || [navigator.language || 'en'];
    for (var i = 0; i < nl.length; i++) {
      /* 台湾・香港の端末は繁體字へ（2026-09-24 中国語を足した） */
      if (/^zh-(tw|hk|mo|hant)/i.test(String(nl[i] || '')) && avail.indexOf('zh-Hant') >= 0) return 'zh-Hant';
      var c = String(nl[i] || '').toLowerCase().split('-')[0];
      if (avail.indexOf(c) >= 0) return c;
    }
    return 'en';
  }
  function save(l) { try { localStorage.setItem(KEY, l); } catch (e) {} }

  var lang = pick();
  /* トップページが「日本語のときだけ出す記事」を決めるのに使う。<head> で先に決めておく */
  window.PENGESSO_LANG = lang;
  if (lang !== 'en') document.documentElement.setAttribute('lang', lang);

  /* ── 細い文字は使わない（2026-09-24 本人の好み：「細い文字が全部嫌い。全部太字でいいぐらい」）──
     本文など太さを決めていない文字を、どの言語でも太字にする。
     :where() で詳しさを0にしてあるので、見出しなど元から太い指定（.big / h1 / ラベル）はそのまま */
  var bold = document.createElement('style');
  bold.textContent = 'html body :where(p, li, a, span, div, figcaption, td, th, button, small, label, blockquote) { font-weight: 700; }';
  (document.head || document.getElementsByTagName('head')[0]).appendChild(bold);

  /* ── 🌙 ダークモード（2026-09-24 本人の希望：「まぶしい」）──────────────
     全ページ共通。初めての人はいつもライト（2026-09-25 本人の要望：明るい方がパッと見が好き）。
     ボタンで切り替えたら localStorage に覚えて、次からはその設定で開く。
     <head> で先に決めるので、白く光ってから暗くなる「ちらつき」が出ない */
  var THEME_KEY = 'pengesso-theme';
  function pickTheme() {
    var qt = (location.search.match(/[?&]theme=(dark|light)/) || [])[1];
    if (qt) return qt;
    try { var t = localStorage.getItem(THEME_KEY); if (t === 'dark' || t === 'light') return t; } catch (e) {}
    return 'light';
  }
  var theme = pickTheme();
  document.documentElement.setAttribute('data-theme', theme);
  var D = 'html[data-theme="dark"] ';
  var darkCss = document.createElement('style');
  darkCss.textContent =
    D + '{color-scheme:dark}' +
    D + 'body{--bg:#15161d;--card:rgba(34,36,48,.96);--text:#ece8f3;--muted:#b3aac4;--line:rgba(255,255,255,.12);' +
      '--shadow:0 18px 50px rgba(0,0,0,.45);--cream:#14161f;--paper:#1f2230;--ink:#eef0f8;' +
      'background:radial-gradient(circle at 8% 0%,rgba(139,109,232,.18),transparent 30%),' +
      'radial-gradient(circle at 96% 14%,rgba(255,111,174,.10),transparent 30%),#15161d !important;color:#ece8f3 !important}' +
    /* 白い箱を、暗い箱に */
    D + ':is(.card,.panel,.post,.goal,.about,.map-card,.mem,.youtube-card,.timeline-item,.home,.wc-badge,.i18n-switch,.i18n-menu,' +
      '.room,.job,.place,.chip,.pagination button,.now > *,.series,.part-nav a,.credit,.era,.lead,.dek,.shift-summary,.codeblock){' +
      'background:#22242f !important;border-color:rgba(255,255,255,.08) !important;box-shadow:0 10px 28px rgba(0,0,0,.35) !important}' +
    D + '.chip[aria-pressed="true"],' + D + '.i18n-opt.on{background:#8b6de8 !important;color:#fff !important}' +
    /* 文字を明るく */
    D + ':is(h1,h2,h3,.brand-name,.about-name,.post-title,.next-title,.moment-title,.era-title){color:#f4f0fa !important;text-shadow:none !important}' +
    D + '.card :is(p,li,figcaption):not(.bubble):not(.big):not(.closing-line),' + D + '.mem figcaption p,' + D + '.panel :is(p,span,label),' +
      D + ':is(.post,.room,.job,.place,.chip,.home,.wc-badge,.i18n-opt,.lead,.dek,.shift-summary,.part-nav a,.credit,.hint,.map-hint){color:#e6e1ee !important}' +
    D + ':is(.big,.closing-line){color:#f6c8e6 !important}' +
    D + '.timeline-item{background:#2a2c39 !important}' + D + '.timeline-item *{color:#ece8f3 !important}' +
    D + '.card :is(b,strong,.device,.stage:not(.stage-public)){color:#f4f0fa !important}' +
    D + '.card p.aside,' + D + '.ba-col.before{background:rgba(255,255,255,.06) !important}' +
    D + '.photo{background:#22242f !important;border-color:rgba(255,255,255,.10) !important}' +
    D + 'img{filter:brightness(.93)}' +
    D + '.stage-public{background:#23c98a !important;color:#04331d !important}' +
    /* 切り替えボタン */
    '.theme-btn{display:inline-grid;place-items:center;width:40px;height:40px;margin-right:8px;border:2px solid rgba(255,255,255,.9);' +
      'border-radius:50%;background:#fff;font-size:18px;cursor:pointer;box-shadow:0 6px 16px rgba(115,70,111,.10);transition:transform .3s}' +
    '.theme-btn:hover{transform:rotate(-20deg) scale(1.06)}' + D + '.theme-btn{background:#22242f;border-color:rgba(255,255,255,.1)}' +
    '@media (prefers-reduced-motion: reduce){.theme-btn{transition:none}}' +
    /* 読みやすさ（2026-09-25）：章のラベルは淡い色なので少し濃く／PUBLIC は緑の上の濃い字に統一 */
    '.chap .card-label{color:color-mix(in srgb,var(--c) 66%,#000) !important}' +
    D + '.chap .card-label{color:color-mix(in srgb,var(--c) 55%,#fff) !important}' +
    '.stage-public{color:#04331d !important}' +
    D + ':is(.card-label,.label,.series,.next-kicker){filter:none}';
  (document.head || document.getElementsByTagName('head')[0]).appendChild(darkCss);
  function themeButton() {
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'theme-btn'; b.setAttribute('translate', 'no');
    function paint() {
      b.textContent = theme === 'dark' ? '☀️' : '🌙';
      b.setAttribute('aria-label', theme === 'dark' ? 'Light mode' : 'Dark mode');
      b.title = b.getAttribute('aria-label');
    }
    paint();
    b.addEventListener('click', function () {
      theme = theme === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', theme);
      try { localStorage.setItem(THEME_KEY, theme); } catch (e) {}
      paint();
      guard();
    });
    return b;
  }


  /* ── 👀 読みにくい文字の見張り番（2026-09-25 本人の要望：モードを切り替えると読みづらい記事がある）──
     （ダークは全部の文字、ライトは小さなラベル類だけ）文字の色と「実際に後ろにある背景の色」を比べる。
     差が小さすぎる文字だけ、色味は残したまま明るく（背景が明るければ暗く）する。ライトに戻したら元に戻す。
     記事ごとに手で直さなくても、これから作る記事にも効く */
  var fixed = [];
  function rgba(v) { var m = /rgba?\(([^)]+)\)/.exec(v || ''); if (!m) return null;
    var p = m[1].split(/[\s,\/]+/).filter(Boolean).map(parseFloat); return [p[0], p[1], p[2], p.length > 3 ? p[3] : 1]; }
  function lum(c) { var a = [0, 1, 2].map(function (i) { var v = c[i] / 255; return v <= .03928 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); });
    return .2126 * a[0] + .7152 * a[1] + .0722 * a[2]; }
  function over(t, b) { var a = t[3]; return [t[0] * a + b[0] * (1 - a), t[1] * a + b[1] * (1 - a), t[2] * a + b[2] * (1 - a), 1]; }
  function ratio(a, b) { var x = lum(a), y = lum(b); return (Math.max(x, y) + .05) / (Math.min(x, y) + .05); }
  function backOf(el) {
    var layers = [], guess = false;
    for (var e = el; e && e.nodeType === 1; e = e.parentElement) {
      var cs = getComputedStyle(e), img = cs.backgroundImage;
      if (img && img !== 'none' && e !== document.body && e !== document.documentElement) {
        if (!/gradient/.test(img)) return null;               /* 写真の上の文字はさわらない */
        var g = (img.match(/rgba?\([^)]+\)/g) || []).map(rgba).filter(function (c) { return c && c[3] > .5; });
        if (g.length) { layers.push(g[0]); guess = true; break; }
      }
      var c = rgba(cs.backgroundColor);
      if (c && c[3] > 0) { layers.push(c); if (c[3] >= .99) break; }
    }
    var b = rgba(getComputedStyle(document.body).backgroundColor);
    if (!b || b[3] < 1) b = [21, 22, 29, 1];
    for (var i = layers.length - 1; i >= 0; i--) b = over(layers[i], b);
    return { c: b, guess: guess };
  }
  var LIGHT_ONLY = '.card-label,.label,.prev,.next-kicker,.moment-kicker,.series,rt,.value,.chap-title,.bubble,.key,.stage,.i18n-tip';
  var TEXTY = /[A-Za-z0-9぀-ヿ㐀-鿿가-힯]/;
  function guard() {
    fixed.forEach(function (f) { f.el.style.removeProperty('color'); if (f.old) f.el.style.setProperty('color', f.old[0], f.old[1]); });
    fixed = [];
    if (!document.body) return;
    var light = theme !== 'dark';
    var w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT), seen = new Set();
    while (w.nextNode()) {
      var el = w.currentNode.parentElement;
      if (!el || seen.has(el) || !TEXTY.test(w.currentNode.nodeValue)) continue;
      seen.add(el);
      if (el.closest('script,style,svg,.i18n-menu')) continue;
      if (light && !el.closest(LIGHT_ONLY)) continue;   /* ライトでは小さなラベル類だけ（写真の上の見出しを誤って直さない） */
      var cs = getComputedStyle(el), fg = rgba(cs.color); if (!fg) continue;
      var B = backOf(el); if (!B) continue;
      var f = over(fg, B.c), r = ratio(f, B.c);
      if (r >= (B.guess ? 2 : (light ? 3 : 3.2))) continue;
      var to = lum(B.c) > .35 ? [24, 22, 32] : [248, 246, 252], best = null;
      for (var t = .15; t <= 1.001; t += .1) {
        var m = [0, 1, 2].map(function (i) { return Math.round(f[i] + (to[i] - f[i]) * t); }).concat(1);
        if (ratio(m, B.c) >= 4.5) { best = m; break; }
      }
      if (!best) best = to.concat(1);
      var old = el.style.getPropertyValue('color') ? [el.style.getPropertyValue('color'), el.style.getPropertyPriority('color')] : null;
      el.style.setProperty('color', 'rgb(' + best.slice(0, 3).join(',') + ')', 'important');
      fixed.push({ el: el, old: old });
    }
  }
  var gTimer;
  function guardSoon() { clearTimeout(gTimer); gTimer = setTimeout(guard, 120); }
  window.addEventListener('load', guardSoon);
  document.addEventListener('DOMContentLoaded', function () {
    guardSoon();
    if ('MutationObserver' in window) new MutationObserver(function (ms) {
      for (var i = 0; i < ms.length; i++) if (ms[i].type === 'childList') { guardSoon(); return; }
    }).observe(document.body, { childList: true, subtree: true });
  });

  /* ── 📏 読んでいる位置のバー（2026-09-24）。記事ページだけ、いちばん上に細い虹色の線が伸びる ── */
  document.addEventListener('DOMContentLoaded', function () {
    if (!document.querySelector('main .card')) return;
    var bar = document.createElement('div');
    bar.setAttribute('aria-hidden', 'true');
    bar.style.cssText = 'position:fixed;left:0;top:0;height:4px;width:0;z-index:80;border-radius:0 4px 4px 0;' +
      'background:linear-gradient(90deg,#ff8a70,#ffc42e,#34b27d,#4d9de0,#b07ce8);pointer-events:none';
    document.body.appendChild(bar);
    var tick = false;
    function draw() {
      tick = false;
      var h = document.documentElement.scrollHeight - innerHeight;
      bar.style.width = (h > 0 ? Math.min(100, (scrollY / h) * 100) : 0) + '%';
    }
    addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(draw); } }, { passive: true });
    draw();
  });

  /* ── やわらかい丸ゴシック（2026-09-24 本人の希望）────────────────
     端末ごとに入っているフォントが違うので、日本語・韓国語のときだけ Google Fonts から読み込む。
     英字は今までのフォント（Arial Rounded など）を先に並べてそのまま使い、
     日本語・韓国語の文字だけが丸ゴシックに落ちる。英語表示のときは何も読み込まない */
  var SOFT = {
    ja: { css: 'Zen+Maru+Gothic:wght@700;900', name: '"Zen Maru Gothic"' },
    ko: { css: 'Jua', name: '"Jua"' },
    /* 中国語は丸ゴシックの太いものが少ないので、太さのある Noto Sans（簡体・繁体）を使う */
    zh: { css: 'Noto+Sans+SC:wght@700;900', name: '"Noto Sans SC"' },
    'zh-Hant': { css: 'Noto+Sans+TC:wght@700;900', name: '"Noto Sans TC"' }  /* 最初から太くて丸い。Gowun Dodum は細い1種類しかなく、太字にするとにじむので変えた */
  };
  if (SOFT[lang]) {
    var head = document.head || document.getElementsByTagName('head')[0];
    ['https://fonts.googleapis.com', 'https://fonts.gstatic.com'].forEach(function (h, i) {
      var pc = document.createElement('link');
      pc.rel = 'preconnect'; pc.href = h;
      if (i) pc.crossOrigin = 'anonymous';
      head.appendChild(pc);
    });
    var fl = document.createElement('link');
    fl.rel = 'stylesheet';
    fl.href = 'https://fonts.googleapis.com/css2?family=' + SOFT[lang].css + '&display=swap';
    head.appendChild(fl);
    var fs = document.createElement('style');
    fs.textContent = 'html:lang(' + lang + ') body, html:lang(' + lang + ') body *:not(code):not(pre) {' +
      'font-family: "Arial Rounded MT Bold", "Avenir Next Rounded", "Trebuchet MS", ' + SOFT[lang].name + ', sans-serif !important; }';
    head.appendChild(fs);
  }

  /* ── 切り替えボタン ─────────────────────────────── */
  /* 言語が3つまでは [🇺🇸 English | 🇯🇵 日本語] の横並び。4つ以上になったら国旗つきのメニューにする */
  var FLAGS = { en: '🇺🇸' };
  Object.keys(LANGS).forEach(function (k) { FLAGS[k] = LANGS[k].flag || '🌐'; });

  function go(l) {
    if (l === lang) return;
    save(l);
    var u = location.href.replace(/([?&])lang=[^&#]*&?/, '$1').replace(/[?&](#|$)/, '$1');
    if (u === location.href) location.reload(); else location.replace(u);
  }

  var EN_NAMES = { en: 'English', ja: 'Japanese', ko: 'Korean', zh: 'Chinese (Simplified)', 'zh-Hant': 'Chinese (Traditional)' };
  Object.keys(LANGS).forEach(function (k) { if (LANGS[k].englishName) EN_NAMES[k] = LANGS[k].englishName; });
  function option(l) {
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'i18n-opt' + (l === lang ? ' on' : '');
    b.setAttribute('aria-pressed', String(l === lang));
    b.setAttribute('lang', l);
    /* 国旗は使わない（国の印で、言語の印ではない。TASK_多言語化.md §3-2）。その言語の名前＋英語名 */
    b.innerHTML = '<span class="i18n-name">' + NAMES[l] + '</span>' +
                  (EN_NAMES[l] && EN_NAMES[l] !== NAMES[l] ? '<span class="i18n-en">' + EN_NAMES[l] + '</span>' : '');
    b.addEventListener('click', function () { go(l); });
    return b;
  }

  function drawSwitch() {
    if (avail.length < 2) return;
    var st = document.createElement('style');
    st.textContent =
      '.i18n-row{display:flex;justify-content:flex-end;align-items:center;margin:-6px 0 16px}' +
      '.i18n-switch{position:relative;display:inline-flex;gap:3px;padding:4px;background:#fff;' +
      'border:2px solid rgba(255,255,255,.9);border-radius:999px;box-shadow:0 6px 16px rgba(115,70,111,.10)}' +
      '.i18n-opt{display:inline-flex;align-items:center;gap:6px;border:0;background:transparent;color:#7a6a88;' +
      'font:inherit;font-size:13px;font-weight:700;line-height:1;padding:8px 13px;border-radius:999px;cursor:pointer;' +
      'white-space:nowrap;transition:background .2s,color .2s,transform .15s}' +
      '.i18n-opt:hover{background:rgba(139,109,232,.10)}' +
      '.i18n-opt.on{background:#8b6de8;color:#fff;box-shadow:0 4px 10px rgba(139,109,232,.35)}' +
      '.i18n-opt:active{transform:scale(.96)}' +
      '.i18n-opt:focus-visible{outline:3px solid rgba(139,109,232,.45);outline-offset:2px}' +
      '.i18n-flag{font-size:17px;line-height:1}' +
      '.i18n-menu{position:absolute;right:0;top:calc(100% + 6px);z-index:60;display:grid;gap:2px;min-width:230px;max-height:min(70vh,420px);overflow-y:auto;' +
      'padding:6px;background:#fff;border-radius:18px;box-shadow:0 14px 34px rgba(115,70,111,.22)}' +
      '.i18n-menu[hidden]{display:none}.i18n-menu .i18n-opt{justify-content:flex-start;width:100%}' +
      '.i18n-float{position:fixed;top:10px;right:10px;z-index:50}' +
      '.i18n-cur{gap:7px;padding:8px 12px 8px 10px;background:#8b6de8;color:#fff;box-shadow:0 4px 12px rgba(139,109,232,.35)}' +
      '.i18n-cur:hover{background:#7a5bdc}' +
      '.i18n-globe{font-size:17px;line-height:1}' +
      '.i18n-stack{display:inline-flex;margin-left:2px}.i18n-stack i{font-style:normal;font-size:13px;line-height:1;' +
      'margin-left:-5px;padding:2px;border-radius:50%;background:rgba(255,255,255,.92);box-shadow:0 0 0 1.5px #8b6de8}' +
      '.i18n-stack i:first-child{margin-left:0}.i18n-caret{font-size:11px;opacity:.9}' +
      '.i18n-head{padding:8px 10px 6px;font-size:11.5px;font-weight:900;letter-spacing:.04em;color:#8a7d99;border-bottom:1.5px solid rgba(0,0,0,.07);margin-bottom:3px}' +
      '.i18n-en{margin-left:auto;padding-left:12px;font-size:11px;font-weight:700;opacity:.6}' +
      '.i18n-menu .i18n-opt.on .i18n-en{opacity:.85}' +
      '.i18n-menu .i18n-opt.on::after{content:"✓";margin-left:8px;font-weight:900}' +
      '.i18n-nudge .i18n-cur{animation:i18n-pulse 1.6s ease-in-out 3}' +
      '@keyframes i18n-pulse{0%,100%{box-shadow:0 4px 12px rgba(139,109,232,.35)}50%{box-shadow:0 0 0 7px rgba(139,109,232,.22),0 4px 12px rgba(139,109,232,.35)}}' +
      '.i18n-tip{position:absolute;right:0;top:calc(100% + 10px);z-index:55;display:flex;align-items:center;gap:6px;white-space:nowrap;' +
      'padding:8px 8px 8px 13px;border-radius:14px;background:#2b2440;color:#fff;font-size:13px;font-weight:800;cursor:pointer;' +
      'box-shadow:0 10px 26px rgba(0,0,0,.2);animation:i18n-tip-in .35s cubic-bezier(.2,1.4,.4,1) both}' +
      '.i18n-tip::before{content:"";position:absolute;right:26px;top:-6px;width:12px;height:12px;background:#2b2440;transform:rotate(45deg)}' +
      '.i18n-tip button{border:0;background:rgba(255,255,255,.14);color:#fff;width:24px;height:24px;border-radius:50%;font-size:15px;line-height:1;cursor:pointer}' +
      '.i18n-tip .i18n-tip-text{color:#fff !important;font-weight:800}' +
      '.i18n-tip-text.in{animation:i18n-tip-in .3s ease-out both}.i18n-tip.bye{opacity:0;transition:opacity .35s}' +
      '@keyframes i18n-tip-in{from{opacity:0;transform:translateY(-4px)}to{opacity:1;transform:none}}' +
      'html[data-theme="dark"] .i18n-tip,html[data-theme="dark"] .i18n-tip::before{background:#f1ecfb;color:#2b2440}' +
      'html[data-theme="dark"] .i18n-tip .i18n-tip-text{color:#2b2440 !important}' +
      'html[data-theme="dark"] .i18n-tip button{background:rgba(0,0,0,.08);color:#2b2440}' +
      'html[data-theme="dark"] .i18n-head{color:#b3aac4;border-color:rgba(255,255,255,.1)}' +
      'html[data-theme="dark"] .i18n-stack i{background:#3a3450}' +
      '@media (prefers-reduced-motion: reduce){.i18n-nudge .i18n-cur,.i18n-tip,.i18n-tip-text.in{animation:none}}' +
      /* 読む人には関係ない「PUBLIC」は見せない（HTMLには残す。check.py が確かめるため） */
      '.stage-public{display:none !important}' +
      '@media (prefers-reduced-motion: reduce){.i18n-opt{transition:none}}';
    document.head.appendChild(st);

    var wrap = document.createElement('div');
    wrap.className = 'i18n-switch';
    wrap.setAttribute('translate', 'no');
    wrap.setAttribute('role', 'group');
    wrap.setAttribute('aria-label', 'Language');

    if (avail.length <= 2) {
      avail.forEach(function (l) { wrap.appendChild(option(l)); });
    } else {
      /* 🌐 2026-09-25 本人の要望：「言語を切り替えられる」とパッと分かるように。
         地球マーク＋いまの言語名（国旗は使わない）。初めての人には吹き出しで知らせる */
      var cur = document.createElement('button');
      cur.type = 'button';
      cur.className = 'i18n-opt i18n-cur';
      cur.setAttribute('aria-haspopup', 'true');
      cur.setAttribute('aria-expanded', 'false');
      cur.setAttribute('aria-label', 'Language: ' + NAMES[lang]);
      cur.innerHTML = '<span class="i18n-globe" aria-hidden="true">🌐</span>' +
        '<span class="i18n-name">' + NAMES[lang] + '</span>' +
        '<span class="i18n-caret" aria-hidden="true">▾</span>';
      var menu = document.createElement('div');
      menu.className = 'i18n-menu';
      menu.hidden = true;
      var head = document.createElement('div');
      head.className = 'i18n-head';
      head.textContent = '🌐 Language · 言語 · 언어 · 语言';
      menu.appendChild(head);
      avail.forEach(function (l) { menu.appendChild(option(l)); });
      var tip = null;
      function seenTip() { try { localStorage.setItem(TIP_KEY, '1'); } catch (e) {} if (tip) { tip.remove(); tip = null; } wrap.classList.remove('i18n-nudge'); }
      cur.addEventListener('click', function (e) {
        e.stopPropagation();
        seenTip();
        menu.hidden = !menu.hidden;
        cur.setAttribute('aria-expanded', String(!menu.hidden));
      });
      document.addEventListener('click', function () { menu.hidden = true; cur.setAttribute('aria-expanded', 'false'); });
      document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { menu.hidden = true; cur.setAttribute('aria-expanded', 'false'); } });
      wrap.appendChild(cur);
      wrap.appendChild(menu);

      var TIP_KEY = 'pengesso-lang-tip-seen', seen = false;
      try { seen = localStorage.getItem(TIP_KEY) === '1'; } catch (e) {}
      if (!seen) {
        var SAY = { en: 'Read in English', ja: '日本語で読めます', ko: '한국어로도 읽을 수 있어요', zh: '也可以用中文阅读', 'zh-Hant': '也可以用中文閱讀' };
        var lines = avail.filter(function (l) { return l !== lang && SAY[l]; }).map(function (l) { return SAY[l]; });
        if (lines.length) {
          tip = document.createElement('div');
          tip.className = 'i18n-tip';
          tip.setAttribute('role', 'status');
          tip.innerHTML = '<span class="i18n-tip-text"></span><button type="button" aria-label="Close">×</button>';
          var txt = tip.querySelector('.i18n-tip-text'), n = 0;
          txt.textContent = lines[0];
          tip.addEventListener('click', function (e) { e.stopPropagation(); if (e.target.tagName === 'BUTTON') seenTip(); else cur.click(); });
          wrap.appendChild(tip);
          wrap.classList.add('i18n-nudge');
          var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
          var iv = reduce ? null : setInterval(function () {
            if (!tip) return clearInterval(iv);
            n = (n + 1) % lines.length;
            txt.classList.remove('in'); void txt.offsetWidth; txt.textContent = lines[n]; txt.classList.add('in');
          }, 1900);
          setTimeout(function () { if (tip) { tip.classList.add('bye'); setTimeout(function () { if (tip) { tip.remove(); tip = null; } wrap.classList.remove('i18n-nudge'); clearInterval(iv); }, 400); } }, 11000);
        }
      }
    }

    /* 上のバーはスマホだと満員なので、そのすぐ下に1行つくって右に置く */
    var spot = document.querySelector('[data-i18n-switch]');
    var bar = document.querySelector('.topbar') || document.querySelector('body > header, main > header, header');
    var tb = themeButton();
    if (spot) { spot.appendChild(tb); spot.appendChild(wrap); switchMount = spot; }
    else if (bar) {
      var row = document.createElement('div');
      row.className = 'i18n-row';
      row.appendChild(tb);
      row.appendChild(wrap);
      bar.parentNode.insertBefore(row, bar.nextSibling);
      switchMount = row;
    } else { wrap.className += ' i18n-float'; wrap.insertBefore(tb, wrap.firstChild); document.body.appendChild(wrap); switchMount = wrap; }
  }

  /* ── 未確認の翻訳（AIが訳したが、本人が読めない言語）についての注意書き ──────
     i18n/ui.<lang>.json に "unverified": true と "notice" を書いた言語だけに出る。
     一度閉じたら、その言語ではもう出さない（localStorage に言語ごとに覚える） */
  var NOTICE_KEY_PREFIX = 'pengesso-notice-dismissed-';
  function drawNotice(l, L) {
    if (!L.unverified || !L.notice) return;
    try { if (localStorage.getItem(NOTICE_KEY_PREFIX + l) === '1') return; } catch (e) {}

    var st = document.createElement('style');
    st.textContent =
      '.i18n-notice{display:flex;align-items:flex-start;gap:10px;margin:8px 0 16px;padding:12px 14px;' +
      'background:#fff8e8;border:2px solid #f3ddaa;border-radius:16px;' +
      'box-shadow:0 6px 16px rgba(115,70,111,.08)}' +
      '.i18n-notice p{margin:0;flex:1;font-size:13px;line-height:1.55;color:#6b5a3a}' +
      '.i18n-notice button{flex:none;border:0;background:transparent;color:#9a8a5a;font-size:15px;' +
      'line-height:1;cursor:pointer;padding:4px;border-radius:8px}' +
      '.i18n-notice button:hover{background:rgba(154,138,90,.14)}' +
      '.i18n-notice button:focus-visible{outline:3px solid rgba(154,138,90,.45);outline-offset:1px}';
    document.head.appendChild(st);

    var box = document.createElement('div');
    box.className = 'i18n-notice';
    box.setAttribute('role', 'note');
    var p = document.createElement('p');
    p.innerHTML = L.notice;
    var b = document.createElement('button');
    b.type = 'button';
    b.setAttribute('aria-label', L.noticeDismiss || 'Close');
    b.textContent = '✕';
    b.addEventListener('click', function () {
      box.remove();
      try { localStorage.setItem(NOTICE_KEY_PREFIX + l, '1'); } catch (e) {}
    });
    box.appendChild(p);
    box.appendChild(b);

    if (switchMount && switchMount.parentNode) switchMount.parentNode.insertBefore(box, switchMount.nextSibling);
    else document.body.insertBefore(box, document.body.firstChild);
  }

  var switchMount = null;

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();

  function start() {
  drawSwitch();
  if (lang === 'en') return;
  drawNotice(lang, LANGS[lang] || {});

  /* ── 差し替え ───────────────────────────────────── */
  var L = LANGS[lang];
  var DICT = L.dict || {};
  var PATTERNS = (L.patterns || []).map(function (p) { return [new RegExp(p[0]), p[1]]; });
  var INLINE = { A:1, ABBR:1, B:1, BR:1, CODE:1, EM:1, I:1, MARK:1, Q:1, S:1, SMALL:1,
                 STRONG:1, SUB:1, SUP:1, U:1, TIME:1, WBR:1 };
  var SKIP = { SCRIPT:1, STYLE:1, NOSCRIPT:1, TEXTAREA:1, SELECT:1, OPTION:1, TEMPLATE:1 };
  var ATTRS = ['placeholder', 'title', 'aria-label'];
  var LETTER = /[A-Za-z]/;

  function norm(s) { return String(s).replace(/\s+/g, ' ').trim(); }
  /* 文の一部として一緒に訳してよいのは、飾りのない太字・リンクなどだけ。
     id や class が付いた要素は、JavaScript が後から中身を書き換える部品（件数やゲージ）
     かもしれないので、絶対に巻き込まない */
  function isInline(n) {
    return n.nodeType === 1 && n.namespaceURI === 'http://www.w3.org/1999/xhtml' &&
      !n.hasAttribute('class') && !n.hasAttribute('id') &&
      (INLINE[n.tagName] || n.tagName === 'SPAN');
  }

  /* 鍵は英文そのものではなく、英文の短い指紋（FNV-1a）。tools/i18n.py の fp() と同じ計算 */
  function fp(s) {
    var h = 0x811c9dc5;
    for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619) >>> 0; }
    return h.toString(36);
  }
  function lookup(k) {
    if (!k || !LETTER.test(k)) return null;
    var f = fp(k);
    if (Object.prototype.hasOwnProperty.call(DICT, f)) return DICT[f];
    for (var i = 0; i < PATTERNS.length; i++) {
      if (PATTERNS[i][0].test(k)) return k.replace(PATTERNS[i][0], PATTERNS[i][1]);
    }
    var num = k.match(/^(.*\D)\s+(\d+)$/);           /* 地図の「Japan 86」のような、名前＋件数 */
    if (num && LETTER.test(num[1])) {
      var t0 = lookup(num[1]);
      if (t0 !== null) return t0 + ' ' + num[2];
    }
    if (k.indexOf(' · ') > 0) {                     /* 「Notes, self-talk · 12」のような組み合わせ */
      var parts = k.split(' · '), out = [];
      for (var j = 0; j < parts.length; j++) {
        var p = parts[j];
        if (!LETTER.test(p)) { out.push(p); continue; }
        var t = lookup(p);
        if (t === null) return null;
        out.push(t);
      }
      return out.join(' · ');
    }
    return null;
  }

  /* その要素が「直接」持っている文（地の文＋太字などのインライン）をひとかたまりとして見る */
  function unitOf(el) {
    var parts = [], nodes = [], direct = false;
    for (var c = el.firstChild; c; c = c.nextSibling) {
      if (c.nodeType === 3) {
        parts.push(c.nodeValue); nodes.push(c);
        if (/\S/.test(c.nodeValue)) direct = true;
      } else if (isInline(c)) {
        parts.push(c.textContent); nodes.push(c);
      }
    }
    return direct ? { key: norm(parts.join('')), nodes: nodes } : null;
  }

  function place(el, nodes, html) {
    var first = null;
    for (var i = 0; i < nodes.length; i++) {             /* 先頭の空白は飛ばして、文の頭に置く */
      if (nodes[i].nodeType !== 3 || /\S/.test(nodes[i].nodeValue)) { first = nodes[i]; break; }
    }
    if (!first) return;
    /* 元の文の前後に空白があったら（🐧 などの飾りとのすき間）、それは残す */
    var raw = nodes.map(function (n) { return n.nodeType === 3 ? n.nodeValue : n.textContent; }).join('');
    if (/\s$/.test(raw) && nodes[nodes.length - 1].nextSibling) html = html + ' ';
    if (/^\s/.test(raw) && nodes[0].previousSibling) html = ' ' + html;
    if (el.namespaceURI !== 'http://www.w3.org/1999/xhtml') {
      el.insertBefore(document.createTextNode(html.replace(/<[^>]+>/g, '')), first);
    } else {
      var t = document.createElement('template');
      t.innerHTML = html;
      el.insertBefore(t.content, first);
    }
    nodes.forEach(function (n) { if (n.parentNode === el) el.removeChild(n); });
  }

  function attrs(el) {
    for (var i = 0; i < ATTRS.length; i++) {
      var v = el.getAttribute && el.getAttribute(ATTRS[i]);
      if (v) { var t = lookup(norm(v)); if (t !== null) el.setAttribute(ATTRS[i], t.replace(/<[^>]+>/g, '')); }
    }
  }

  function walk(el) {
    if (!el || el.nodeType !== 1 || SKIP[el.tagName] || el.hasAttribute('translate') && el.getAttribute('translate') === 'no') return;
    attrs(el);
    var u = unitOf(el);
    /* 一度訳した文には印をつけて、二度と触らない。
       「AI」→「AI」のように訳が英語と同じだと、差し替え → 変化を検知 → また差し替え…
       と無限に回ってしまうため */
    if (u && el.__i18n !== u.key) {
      var tr = lookup(u.key);
      if (tr !== null) {
        place(el, u.nodes, tr);
        var nu = unitOf(el);
        el.__i18n = nu ? nu.key : '';
      }
    }
    var kids = [];
    for (var c = el.firstChild; c; c = c.nextSibling) if (c.nodeType === 1) kids.push(c);
    for (var i = 0; i < kids.length; i++) {
      /* 文のかたまりに含まれるインライン（太字など）は、かたまりごと扱ったので潜らない */
      if (u && u.nodes.indexOf(kids[i]) >= 0) continue;
      walk(kids[i]);
    }
  }

  document.documentElement.setAttribute('lang', lang);
  var t0 = lookup(norm(document.title));
  if (t0 !== null) document.title = t0.replace(/<[^>]+>/g, '');
  walk(document.body);

  /* ── あとから JavaScript で描かれる部分（トップの一覧など）も訳す ── */
  if ('MutationObserver' in window) {
    new MutationObserver(function (list) {
      list.forEach(function (m) {
        if (m.type === 'childList') {
          m.addedNodes.forEach(function (n) {
            if (n.nodeType === 1) walk(n);
            else if (n.nodeType === 3 && m.target.nodeType === 1) walk(m.target);
          });
        }
      });
    }).observe(document.body, { childList: true, subtree: true });
  }
  }
})();
