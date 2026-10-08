/* 🌐 言語の切り替え（共通メニューと記事訳は必要なJSONだけ読む。ここを直したら i18n.py を流し直す）
   ・英語の本文はそのまま。日本語などは「英文 → 訳」の対応表で、文章のかたまりごとに差し替える
   ・対応表にない文は英語のまま残る（壊れるより、英語が残るほうがまし）
   ・選んだ言語は localStorage に覚える。?lang=ja でも指定できる */

/* ✨ 動きの設定（2026-10-04 本人：「スマホだとアニメーションがなかったりして、非常に残念」）
   原因の候補：端末の「視差効果を減らす」（iPhone）／「アニメーションを削除」（Android）が ON だと、
   記事の動きを全部止める決まりになっていた（prefers-reduced-motion）。本人の端末がそうなっていても気づけない。
   なので、このサイトの「動き」は、読む人が自分で選べるようにした（ページのいちばん下の ✨ ボタン）。
     auto … 端末の設定にしたがう（はじめはこれ。端末が「減らす」なら、止める）
     on   … 端末が「減らす」でも、動かす（本人が選んだとき。端末の設定より本人の選択を優先）
     off  … 端末が「減らさない」でも、止める
   選んだものは localStorage の pengesso-motion に覚え、<html data-motion="on|off"> に出す。CSS（記事ごとの
   @media (prefers-reduced-motion) と、下のランタイムの CSS）が、これを見る。
   記事の JS が (prefers-reduced-motion: reduce) を見るところも、選んだ値を返す（matchMedia を包んだ）。 */
(function () {
  var html = document.documentElement, KEY = 'pengesso-motion';
  function stored() { try { var v = localStorage.getItem(KEY); return v === 'on' || v === 'off' ? v : 'auto'; } catch (e) { return 'auto'; } }
  var m0 = stored();
  if (m0 !== 'auto') html.setAttribute('data-motion', m0);
  var realMM = window.matchMedia;
  var osMQ = realMM ? realMM.call(window, '(prefers-reduced-motion: reduce)') : null;
  if (realMM) {
    window.matchMedia = function (q) {
      var mql = realMM.call(window, q);
      if (typeof q !== 'string' || q.indexOf('prefers-reduced-motion') < 0) return mql;
      var cur = html.getAttribute('data-motion');
      if (cur !== 'on' && cur !== 'off') return mql;
      var asksNoPref = /no-preference/.test(q);
      return { matches: asksNoPref ? cur === 'on' : cur === 'off', media: q, onchange: null,
        addListener: function () {}, removeListener: function () {}, addEventListener: function () {}, removeEventListener: function () {}, dispatchEvent: function () { return false; } };
    };
  }
  window.pengessoMotion = {
    mode: function () { var c = html.getAttribute('data-motion'); return c === 'on' || c === 'off' ? c : 'auto'; },
    os: function () { return !!(osMQ && osMQ.matches); },
    set: function (m) {
      try { if (m === 'on' || m === 'off') localStorage.setItem(KEY, m); else localStorage.removeItem(KEY); } catch (e) {}
      if (m === 'on' || m === 'off') html.setAttribute('data-motion', m); else html.removeAttribute('data-motion');
      try { document.dispatchEvent(new CustomEvent('pengesso:motion', { detail: m })); } catch (e) {}
    }
  };
  /* 「止める」のとき、ランタイムが作る部品（勉強バー・言語メニューなど）の動きも止める */
  var st = document.createElement('style');
  st.textContent = 'html[data-motion="off"] *,html[data-motion="off"] *::before,html[data-motion="off"] *::after{animation:none !important;transition:none !important}';
  (document.head || html).appendChild(st);
})();

/* 🎬 スマホで「たまに動きが出ない」を直す（2026-09-25 本人の報告）
   原因：記事は写真を中に埋め込んでいて重い。スマホだと読み込みに時間がかかり、
   ・上のラベル・タイトル・写真の「ふわっと出る」動きが、画面に映る前に終わってしまう
   ・日本語などで読むとき、英語のまま動いたあと、途中で訳に差し替わってカクッとする
   なので、ページを読み終えて訳に差し替えたあと、最初の描画を待ってから動きを始める。
   カードは「少しでも見えたら」出す。もう通り過ぎたカードは、すぐ見せる。 */
(function () {
  var root = document.documentElement;
  if (!document.querySelector || root.classList.contains('motion-hold')) return;
  root.classList.add('motion-hold');
  var st = document.createElement('style');
  st.textContent = 'html.motion-hold main>.label,html.motion-hold main>h1,html.motion-hold main>.photo,' +
    'html.motion-hold main>figure.photo{animation-play-state:paused !important}';
  (document.head || root).appendChild(st);
  var done = false;
  function go() {
    if (done) return; done = true;
    var raf = window.requestAnimationFrame || function (f) { setTimeout(f, 16); };
    raf(function () { raf(function () { root.classList.remove('motion-hold'); }); });
  }
  setTimeout(go, 2500); // 保険：何があっても2.5秒で動き出す
  document.addEventListener('DOMContentLoaded', function () {
    setTimeout(go, 0); // 訳の差し替え（同じ DOMContentLoaded）が終わってから
    if (!('IntersectionObserver' in window)) return;
    var items = [].slice.call(document.querySelectorAll('.card, .next'));
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting || e.boundingClientRect.bottom < 0) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0, rootMargin: '0px 0px -6% 0px' });
    items.forEach(function (el) { io.observe(el); });
  });
  // 戻るボタンで戻ってきたとき（ページが保存されていたとき）は、止めたままにしない
  window.addEventListener('pageshow', function () { root.classList.remove('motion-hold'); });
})();
/* 🎬 動画・曲・地図（iframe）は、画面に近づいてから読む（2026-10-04 本人：「スマホで開くと少しラグがある」）
   YouTube は1つで 0.5〜1MB。前はページを開いた瞬間に読み始めて、本文や訳の読み込みと回線を取り合っていた。
   記事の HTML では <iframe data-src="…">（src を書かない）。ここで、画面の 600px 手前に来たら src に入れる */
(function () {
  function go() {
    var fs = [].slice.call(document.querySelectorAll('iframe[data-src]'));
    if (!fs.length) return;
    function load(f) { var u = f.getAttribute('data-src'); if (u) { f.setAttribute('src', u); f.removeAttribute('data-src'); } }
    if (!('IntersectionObserver' in window)) { fs.forEach(load); return; }
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { load(e.target); io.unobserve(e.target); } });
    }, { rootMargin: '600px 0px' });
    fs.forEach(function (f) { io.observe(f); });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', go); else go();
})();
/* 🎉 絵文字は押すと、ぽんっと弾ける（2026-10-05 本人：「妹が、押すと絵文字がふわっと動くのを気に入っていた。
   ただ読ませるより、触って遊べると笑顔が増える」）
   ・記事の中で「絵文字だけ」の部品（🐧 や 📦 など1〜2文字）は、押すと跳ねて、同じ絵文字が飛び散る
   ・リンク・ボタン・言語メニューの中の絵文字はそのまま（押したときの動きを変えない）
   ・画面に入った最初の3つだけ、1回ぴょんと跳ねて「押せるよ」と知らせる
   ・window.pengessoPop(x, y, ['💖','🇵🇭'], n) で、ほかの部品（いいね）からも呼べる
   ・動きを減らす設定の人には、飛び散らせずに小さく跳ねるだけ */
(function () {
  var doc = document, still = false;
  try { still = window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) {}
  var EMO;
  try { EMO = new RegExp('^(?:\\p{Extended_Pictographic}|\\p{Regional_Indicator}|[\\u200d\\ufe0f\\u20e3#*0-9\\u{1F3FB}-\\u{1F3FF}]|\\s)+$', 'u'); } catch (e) { return; }
  var layer = null, live = 0;
  function pop(x, y, list, n) {
    if (still || !doc.body || !list || !list.length) return;
    if (!layer) {
      layer = doc.createElement('div');
      layer.setAttribute('aria-hidden', 'true');
      layer.style.cssText = 'position:fixed;inset:0;pointer-events:none;z-index:2147483000;overflow:hidden';
      doc.body.appendChild(layer);
    }
    n = Math.min(n || 9, 40 - live);
    for (var i = 0; i < n; i++) {
      var s = doc.createElement('span');
      s.textContent = list[i % list.length];
      var size = 18 + Math.random() * 16;
      s.style.cssText = 'position:absolute;left:' + x + 'px;top:' + y + 'px;font-size:' + size.toFixed(0) +
        'px;line-height:1;margin:-.5em 0 0 -.5em;will-change:transform,opacity';
      layer.appendChild(s); live++;
      var a = -Math.PI / 2 + (Math.random() - .5) * 2.2, v = 70 + Math.random() * 90;
      var dx = Math.cos(a) * v, up = Math.sin(a) * v, fall = 120 + Math.random() * 80, r = (Math.random() - .5) * 120;
      var done = (function (el) { return function () { if (el.parentNode) el.parentNode.removeChild(el); live--; }; })(s);
      if (s.animate) {
        var an = s.animate([
          { transform: 'translate(0,0) scale(.4) rotate(0deg)', opacity: 1 },
          { transform: 'translate(' + (dx * .55).toFixed(0) + 'px,' + up.toFixed(0) + 'px) scale(1.1) rotate(' + (r / 2).toFixed(0) + 'deg)', opacity: 1, offset: .4 },
          { transform: 'translate(' + dx.toFixed(0) + 'px,' + (up + fall).toFixed(0) + 'px) scale(.9) rotate(' + r.toFixed(0) + 'deg)', opacity: 0 }
        ], { duration: 900 + Math.random() * 400, easing: 'cubic-bezier(.2,.7,.4,1)', fill: 'forwards' });
        an.onfinish = done;
      } else { setTimeout(done, 50); }
    }
  }
  window.pengessoPop = pop;

  function hop(el, big) {
    if (!el.animate) return;
    el.animate(still ? [{ transform: 'scale(1)' }, { transform: 'scale(1.15)' }, { transform: 'scale(1)' }] : [
      { transform: 'translate(0,0) scale(1) rotate(0)' },
      { transform: 'translate(0,' + (big ? -14 : -7) + 'px) scale(' + (big ? 1.3 : 1.1) + ') rotate(-8deg)', offset: .35 },
      { transform: 'translate(0,2px) scale(.95,1.05) rotate(4deg)', offset: .7 },
      { transform: 'translate(0,0) scale(1) rotate(0)' }
    ], { duration: big ? 520 : 700, easing: 'ease-out' });
  }
  var SKIP = 'a,button,input,select,textarea,label,summary,[role="button"],[contenteditable],nav,.post-tags,.px-strip,.px-end,.px-world,.lang-switch,.i18n-menu,.learn,.it-line,.sortbar';
  function setup() {
    var root = doc.querySelector('main') || doc.querySelector('article');
    if (!root) return;
    var css = doc.createElement('style');
    css.textContent = '.emo-pop{cursor:pointer;-webkit-user-select:none;user-select:none;-webkit-tap-highlight-color:transparent;touch-action:manipulation}' +
      '.emo-pop:not(.emo-inline){display:inline-block}';
    doc.head.appendChild(css);
    var all = [].slice.call(root.querySelectorAll('span,b,i,em,strong,div,p,small,figcaption,li,td,th,dt,dd'));
    var found = [];
    all.forEach(function (el) {
      if (el.children.length) return;
      var t = el.textContent;
      if (!t || t.length > 12 || !/\S/.test(t) || !EMO.test(t) || /^[\s#*0-9]+$/.test(t)) return;
      if (el.closest(SKIP)) return;
      el.classList.add('emo-pop');
      if (getComputedStyle(el).display === 'inline') el.classList.add('emo-inline');
      found.push(el);
    });
    if (!found.length) return;
    root.addEventListener('click', function (ev) {
      var el = ev.target.closest && ev.target.closest('.emo-pop');
      if (!el || !root.contains(el)) return;
      hop(el, true);
      var r = el.getBoundingClientRect();
      var list = (el.textContent.replace(/\s+/g, '').match(/(?:\p{Regional_Indicator}{2}|\p{Extended_Pictographic}(?:[\u{1F3FB}-\u{1F3FF}️]|‍\p{Extended_Pictographic}️?)*|[#*0-9]️?⃣)/gu) || [el.textContent.trim()]);
      pop(r.left + r.width / 2, r.top + r.height / 2, list, 10);
    });
    // 「押せるよ」の合図：画面に入った最初の3つだけ、1回ぴょんと跳ねる
    if (still || !('IntersectionObserver' in window)) return;
    var hinted = 0;
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        io.unobserve(e.target);
        if (hinted >= 3) return;
        hinted++;
        setTimeout(function () { hop(e.target, false); }, 500 + hinted * 250);
      });
    }, { threshold: 1, rootMargin: '0px 0px -15% 0px' });
    found.forEach(function (el) { io.observe(el); });
  }
  if (doc.readyState === 'loading') doc.addEventListener('DOMContentLoaded', setup); else setup();
})();
(function () {
  var holder = document.getElementById('i18n-data');
  if (!holder) return;
  var DATA;
  try { DATA = JSON.parse(holder.textContent); } catch (e) { return; }
  var LANGS = DATA.langs || {};
  var MENU = {};
  var THEME = {};
  /* ダーク切り替えの文言（lang はこの下で決まるので、使うときに引く） */
  var THEME_WORDS = { ja: ['ダーク表示', 'ライト表示'], ko: ['다크 모드', '라이트 모드'], zh: ['深色模式', '浅色模式'], 'zh-Hant': ['深色模式', '淺色模式'] };
  var KEY = 'pengesso-lang';
  var avail = ['en'].concat(Object.keys(LANGS));
  var NAMES = { en: 'English' };
  var EN_NAMES = { en: 'English' };
  var FLAGS = { en: '🇺🇸' };
  var UI_READY = Promise.resolve();
  function refreshLanguageMeta() {
    NAMES = { en: 'English' }; EN_NAMES = { en: 'English' }; FLAGS = { en: '🇺🇸' };
    Object.keys(LANGS).forEach(function (k) {
      NAMES[k] = LANGS[k].name || k;
      EN_NAMES[k] = LANGS[k].englishName || k;
      FLAGS[k] = LANGS[k].flag || '🌐';
    });
    MENU = (LANGS[lang] && LANGS[lang].menu) || {};
    THEME = (LANGS[lang] && LANGS[lang].theme) || {};
  }
  refreshLanguageMeta();
  if (DATA.uiData && window.fetch) {
    var uiUrl = new URL('../../i18n/ui-data.json', location.href);
    if (DATA.uiV) uiUrl.searchParams.set('v', DATA.uiV);
    UI_READY = fetch(uiUrl.toString(), { credentials: 'same-origin' })
      .then(function (res) { if (!res.ok) throw new Error('Language menu unavailable'); return res.json(); })
      .then(function (uiData) {
        var pageLangs = LANGS, commonLangs = uiData.langs || {}, merged = {};
        Object.keys(pageLangs).forEach(function (k) {
          if (commonLangs[k]) merged[k] = Object.assign({}, commonLangs[k], pageLangs[k]);
        });
        LANGS = merged; avail = ['en'].concat(Object.keys(LANGS));
        refreshLanguageMeta();
      }).catch(function () {});
  }

  function canonical(code) {
    var q = String(code || '').replace(/_/g, '-').toLowerCase();
    for (var i = 0; i < avail.length; i++) if (avail[i].toLowerCase() === q) return avail[i];
    for (var j = 0; j < avail.length; j++) {
      var aliases = (LANGS[avail[j]] && LANGS[avail[j]].aliases) || [];
      for (var k = 0; k < aliases.length; k++) if (String(aliases[k]).toLowerCase() === q) return avail[j];
    }
    return null;
  }

  function browserChoice() {
    var nl = navigator.languages || [navigator.language || 'en'];
    for (var i = 0; i < nl.length; i++) {
      var raw = String(nl[i] || '').replace(/_/g, '-');
      /* 台湾・香港の端末は繁體字へ。zh-Hans は簡体字の zh に寄せる */
      if (/^zh-(tw|hk|mo|hant)(-|$)/i.test(raw) && canonical('zh-Hant')) return canonical('zh-Hant');
      var exact = canonical(raw);
      if (exact) return exact;
      var base = raw.split('-')[0].toLowerCase();
      if (base === 'no' && canonical('nb')) return canonical('nb');
      if (base === 'tl' && canonical('fil')) return canonical('fil');
      var simple = canonical(base);
      if (simple) return simple;
    }
    return null;
  }

  function pick() {
    var q = (location.search.match(/[?&]lang=([a-zA-Z-]+)/) || [])[1];
    var queryLang = canonical(q);
    if (queryLang) { save(queryLang); return queryLang; }
    try { var s = canonical(localStorage.getItem(KEY)); if (s) return s; } catch (e) {}
    return browserChoice() || 'en';
  }
  function save(l) { try { localStorage.setItem(KEY, l); } catch (e) {} }

  var lang = pick();
  refreshLanguageMeta();

  /* ⚡ 訳のデータは、ページを読み終わるのを待たずに、いま取りに行く（2026-10-04 本人：「スマホで開くと少しラグがある」）
     前は DOMContentLoaded のあとに取りに行っていたので、写真の多い記事ほど訳が出るのが遅かった */
  function langUrl(name) {
    var u = new URL('i18n/' + name + '.' + encodeURIComponent(lang) + '.json', location.href);
    if (LANGS[lang] && LANGS[lang].v) u.searchParams.set('v', LANGS[lang].v);
    return u.toString();
  }
  function getJson(url) {
    return fetch(url, { credentials: 'same-origin' }).then(function (res) { if (!res.ok) throw new Error('Translation unavailable'); return res.json(); });
  }
  var EARLY = null;
  if (lang !== 'en' && window.fetch && LANGS[lang]) {
    if (DATA.lazyTop) EARLY = getJson(langUrl('top-data'));
    else if (!(LANGS[lang].dict && Object.keys(LANGS[lang].dict).length)) EARLY = getJson(langUrl('data'));
    if (EARLY) EARLY.catch(function () {});
  }
  /* トップページが「日本語のときだけ出す記事」を決めるのに使う。<head> で先に決めておく */
  window.PENGESSO_LANG = lang;
  if (lang !== 'en') document.documentElement.setAttribute('lang', lang);

  /* ── 細い文字は使わない（2026-09-24 本人の好み：「細い文字が全部嫌い。全部太字でいいぐらい」）──
     本文など太さを決めていない文字を、どの言語でも太字にする。
     :where() で詳しさを0にしてあるので、見出しなど元から太い指定（.big / h1 / ラベル）はそのまま */
  var bold = document.createElement('style');
  bold.textContent = 'html body :where(p, li, a, span, div, figcaption, td, th, button, small, label, blockquote) { font-weight: 700; }' +
    /* 📸 写真を別ファイルにしたとき <img width height> を付けた（読み込み中に文がガタッと動かないように）。
       記事の CSS が幅だけ決めている写真が縦に伸びないよう、高さは自動に。:where なので記事が高さを決めていればそちらが勝つ */
    ':where(img[width][height]) { height: auto; }';
  (document.head || document.getElementsByTagName('head')[0]).appendChild(bold);

  /* ── ✂️ 日本語の見出しを、言葉の途中で折り返さない（2026-09-26）──
     「大｜阪城」のように単語の途中で改行されていた。対応しているブラウザ（Chrome 系）では
     文節で折り返す。本文はそのまま（細かく割ると行がガタガタになるため）。対応していないブラウザは今までどおり */
  var jaWrap = document.createElement('style');
  jaWrap.textContent = 'html:lang(ja) :is(h1, h2, h3, .card-label, .next-title, .prev-title, .post-title, .big, .closing-line) ' +
    '{ word-break: auto-phrase; text-wrap: balance; }' +
    /* どの言語でも：見出しは行の長さをそろえ、本文は最後の行に1語だけ残らないようにする */
    'h1, .next-title, .post-title { text-wrap: balance; } main p, main li, .card p { text-wrap: pretty; }';
  (document.head || document.getElementsByTagName('head')[0]).appendChild(jaWrap);

  /* ── 🌙 ダークモード（2026-09-24 本人の希望：「まぶしい」）──────────────
     全ページ共通。初めての人はいつもライト（2026-09-25 本人の要望：明るい方がパッと見が好き）。
     ボタンで切り替えたら localStorage に覚えて、次からはその設定で開く。
     <head> で先に決めるので、白く光ってから暗くなる「ちらつき」が出ない */
  /* 2026-09-26 本人：「基本はライトで見せたい。ダークは見つけづらいところでいい」。
     覚える名前を変えて、前にダークを選んだ人も一度ライトに戻す。ボタンはページのいちばん下に小さく置く */
  var THEME_KEY = 'pengesso-theme-v2';
  function pickTheme() {
    var qt = (location.search.match(/[?&]theme=(dark|light)/) || [])[1];
    if (qt) return qt;
    try { var t = localStorage.getItem(THEME_KEY); if (t === 'dark' || t === 'light') return t; } catch (e) {}
    return 'light';
  }
  var theme = pickTheme();
  document.documentElement.setAttribute('data-theme', theme);
  /* 📱 スマホのブラウザの上の帯の色も、ダークのときは暗くする（2026-09-26）。ライトではページがもともと決めていた色に戻す */
  var barMeta = document.querySelector('meta[name="theme-color"]'), barOrig = barMeta ? barMeta.getAttribute('content') : null;
  function paintBar() {
    var head = document.head || document.getElementsByTagName('head')[0];
    if (theme === 'dark') {
      if (!barMeta) { barMeta = document.createElement('meta'); barMeta.name = 'theme-color'; head.appendChild(barMeta); }
      barMeta.setAttribute('content', '#15161d');
    } else if (barMeta) {
      if (barOrig) barMeta.setAttribute('content', barOrig); else { barMeta.remove(); barMeta = null; }
    }
  }
  paintBar();
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
      '.room,.job,.place,.chip,.nav a,.pagination button,.now > *,.series,.part-nav a,.credit,.era,.lead,.dek,.shift-summary,.codeblock){' +
      'background:#22242f !important;border-color:rgba(255,255,255,.08) !important;box-shadow:0 10px 28px rgba(0,0,0,.35) !important}' +
    D + '.chip[aria-pressed="true"],' + D + '.i18n-opt.on{background:#8b6de8 !important;color:#fff !important}' +
    /* 文字を明るく */
    D + ':is(h1,h2,h3,.brand-name,.about-name,.post-title,.next-title,.moment-title,.era-title){color:#f4f0fa !important;text-shadow:none !important}' +
    D + '.card :is(p,li,figcaption):not(.bubble):not(.big):not(.closing-line),' + D + '.mem figcaption p,' + D + '.panel :is(p,span,label),' +
      D + ':is(.post,.room,.job,.place,.chip,.nav a,.home,.wc-badge,.i18n-opt,.lead,.dek,.shift-summary,.part-nav a,.credit,.hint,.map-hint){color:#e6e1ee !important}' +
    D + ':is(.big,.closing-line){color:#f6c8e6 !important}' +
    D + '.timeline-item{background:#2a2c39 !important}' + D + '.timeline-item *{color:#ece8f3 !important}' +
    D + '.card :is(b,strong,.device,.stage:not(.stage-public)){color:#f4f0fa !important}' +
    D + '.card p.aside,' + D + '.ba-col.before{background:rgba(255,255,255,.06) !important}' +
    D + '.photo{background:#22242f !important;border-color:rgba(255,255,255,.10) !important}' +
    D + 'img{filter:brightness(.93)}' +
    D + '.stage-public{background:#23c98a !important;color:#04331d !important}' +
    /* 切り替えボタン */
    '.theme-foot{display:flex;flex-wrap:wrap;justify-content:center;gap:2px 6px;margin:26px auto 6px}' +
    '.theme-btn{display:inline-flex;align-items:center;gap:6px;min-height:32px;padding:4px 12px;border:0;border-radius:999px;' +
      'background:none;color:inherit;opacity:.5;font:inherit;font-size:12.5px;font-weight:700;cursor:pointer}' +
    '.theme-btn:hover,.theme-btn:focus-visible{opacity:.9}.theme-btn:focus-visible{outline:2px solid #8b6de8;outline-offset:2px}' +
    /* 読みやすさ（2026-09-25）：章のラベルは淡い色なので少し濃く／PUBLIC は緑の上の濃い字に統一 */
    '.chap .card-label{color:color-mix(in srgb,var(--c) 66%,#000) !important}' +
    D + '.chap .card-label{color:color-mix(in srgb,var(--c) 55%,#fff) !important}' +
    '.stage-public{color:#04331d !important}' +
    D + ':is(.card-label,.label,.series,.next-kicker){filter:none}';
  (document.head || document.getElementsByTagName('head')[0]).appendChild(darkCss);
  /* ✨ 動き（2026-10-04）：auto → on → off → auto と切り替わる。いまの状態が名前に出る */
  var MOTION_WORDS = {
    en: ['✨ Motion: Auto', '✨ Motion: On', '✨ Motion: Off'],
    ja: ['✨ 動き：自動', '✨ 動き：ON', '✨ 動き：OFF'],
    ko: ['✨ 움직임: 자동', '✨ 움직임: 켜짐', '✨ 움직임: 꺼짐'],
    zh: ['✨ 动效：自动', '✨ 动效：开', '✨ 动效：关'],
    'zh-Hant': ['✨ 動態：自動', '✨ 動態：開', '✨ 動態：關']
  };
  function motionButton() {
    var b = document.createElement('button'), M = window.pengessoMotion, order = ['auto', 'on', 'off'];
    b.type = 'button'; b.className = 'theme-btn motion-btn'; b.setAttribute('translate', 'no');
    function paint() { b.textContent = (MOTION_WORDS[lang] || MOTION_WORDS.en)[order.indexOf(M.mode())]; }
    paint();
    b.addEventListener('click', function () { M.set(order[(order.indexOf(M.mode()) + 1) % 3]); paint(); });
    document.addEventListener('pengesso:motion', paint);
    return b;
  }
  function themeButton() {
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'theme-btn'; b.setAttribute('translate', 'no');
    function paint() {
      var th = (LANGS[lang] && LANGS[lang].theme) || {}, w = THEME_WORDS[lang] || [];
      var t = theme === 'dark' ? (th.lightMode || w[1] || 'Light mode') : (th.darkMode || w[0] || 'Dark mode');
      b.textContent = (theme === 'dark' ? '☀️ ' : '🌙 ') + t;
    }
    paint();
    b.addEventListener('click', function () {
      theme = theme === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', theme);
      try { localStorage.setItem(THEME_KEY, theme); } catch (e) {}
      paint();
      paintBar();
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
  var LIGHT_ONLY = '.card-label,.label,.prev,.next-kicker,.moment-kicker,.series,rt,.value,.chap-title,.bubble,.key,.stage,.i18n-tip,.home,.topic,.bubble,.spotify-kicker,.spotify-title,.part-nav a';  /* 2026-09-25 戻る・カテゴリー・吹き出しも（白地で薄かった） */
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
      /* 2026-09-25 ライトは 3→4（小さい字がまだ薄かった）
         2026-09-26 15px 未満の小さい字（カードの見出し・「次の記事」の札など）は 4.5 まで。3.3 くらいのまま残っていた */
      var small = parseFloat(cs.fontSize) < 15;
      if (r >= (B.guess ? 2 : (small ? 4.5 : (light ? 4 : 3.2)))) continue;
      /* 明るい方・暗い方の両方を試して、先に 4.5 に届いたほう（＝元の色に近いほう）を使う。
         中くらいの明るさの地（金色のバッジなど）で、白→白のまま直らなかったため（2026-09-25） */
      var first = lum(B.c) > .35 ? [24, 22, 32] : [248, 246, 252], second = first[0] > 100 ? [24, 22, 32] : [248, 246, 252];
      var best = null, bestT = 9;
      [first, second].forEach(function (to) {
        for (var t = .15; t <= 1.001; t += .1) {
          var m = [0, 1, 2].map(function (i) { return Math.round(f[i] + (to[i] - f[i]) * t); }).concat(1);
          if (ratio(m, B.c) >= 4.5) { if (t < bestT) { best = m; bestT = t; } break; }
        }
      });
      if (!best) best = (ratio(first.concat(1), B.c) >= ratio(second.concat(1), B.c) ? first : second).concat(1);
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

  /* ── 🔢 章の番号（1 2 3）の丸（.chap-tracker）は、スマホでは「スクロールしている間だけ」出す（2026-09-25）
     右下に出しっぱなしだと、行の終わりの文字に重なって読めなかった。止まって1.2秒で消える ── */
  document.addEventListener('DOMContentLoaded', function () {
    if (!document.querySelector('.chap-tracker')) return;
    var st = document.createElement('style');
    st.textContent = '@media (max-width:700px){.chap-tracker{transform-origin:right bottom;scale:.82}' +
      'html:not(.is-scrolling) .chap-tracker.show{opacity:0 !important;transform:translateY(10px) !important}}';
    document.head.appendChild(st);
    var root = document.documentElement, t = 0;
    addEventListener('scroll', function () {
      root.classList.add('is-scrolling'); clearTimeout(t);
      t = setTimeout(function () { root.classList.remove('is-scrolling'); }, 1200);
    }, { passive: true });
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
    'zh-Hant': { css: 'Noto+Sans+TC:wght@700;900', name: '"Noto Sans TC"' }  /* 最初から太くて丸い。Gowun Dodum は細い1種類しかなく、太字にするとにじむので変えた */,
    /* タイ文字・インドの文字・アラビア文字・ヘブライ文字（2026-09-25）。端末に太いフォントがないことが多いので、太い Noto を読み込む */
    th: { css: 'Noto+Sans+Thai:wght@700;900', name: '"Noto Sans Thai"' },
    hi: { css: 'Noto+Sans+Devanagari:wght@700;900', name: '"Noto Sans Devanagari"' },
    mr: { css: 'Noto+Sans+Devanagari:wght@700;900', name: '"Noto Sans Devanagari"' },
    ne: { css: 'Noto+Sans+Devanagari:wght@700;900', name: '"Noto Sans Devanagari"' },
    bn: { css: 'Noto+Sans+Bengali:wght@700;900', name: '"Noto Sans Bengali"' },
    ta: { css: 'Noto+Sans+Tamil:wght@700;900', name: '"Noto Sans Tamil"' },
    te: { css: 'Noto+Sans+Telugu:wght@700;900', name: '"Noto Sans Telugu"' },
    pa: { css: 'Noto+Sans+Gurmukhi:wght@700;900', name: '"Noto Sans Gurmukhi"' },
    ar: { css: 'Noto+Sans+Arabic:wght@700;900', name: '"Noto Sans Arabic"' },
    fa: { css: 'Noto+Sans+Arabic:wght@700;900', name: '"Noto Sans Arabic"' },
    ur: { css: 'Noto+Nastaliq+Urdu:wght@700', name: '"Noto Nastaliq Urdu"' },
    he: { css: 'Noto+Sans+Hebrew:wght@700;900', name: '"Noto Sans Hebrew"' }
  };
  /* 右から書く言語は、ページ全体を右から左に（2026-09-25）。地図・写真・数字は CSS で向きを戻す */
  var RTL = { ar: 1, fa: 1, ur: 1, he: 1 };
  if (RTL[lang]) {
    document.documentElement.setAttribute('dir', 'rtl');
    var rtl = document.createElement('style');
    rtl.textContent = 'html[dir="rtl"] :is(svg, img, video, iframe, pre, code, .map2, .map-stage, .i18n-switch) { direction: ltr; }' +
      'html[dir="rtl"] .i18n-row { justify-content: flex-start; }' +
      'html[dir="rtl"] .i18n-float { right: auto; left: 10px; }';
    (document.head || document.documentElement).appendChild(rtl);
  }
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
  function go(l) {
    if (l === lang) return;
    save(l);
    var u = location.href.replace(/([?&])lang=[^&#]*&?/, '$1').replace(/[?&](#|$)/, '$1');
    if (u === location.href) location.reload(); else location.replace(u);
  }

  function option(l) {
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'i18n-opt' + (l === lang ? ' on' : '');
    b.setAttribute('aria-pressed', String(l === lang));
    b.setAttribute('lang', l);
    b.setAttribute('data-lang', l);
    var nativeName = document.createElement('span');
    nativeName.className = 'i18n-name';
    nativeName.textContent = NAMES[l];
    b.appendChild(nativeName);
    if (EN_NAMES[l] && EN_NAMES[l] !== NAMES[l]) {
      var englishName = document.createElement('span');
      englishName.className = 'i18n-en';
      englishName.textContent = EN_NAMES[l];
      b.appendChild(englishName);
    }
    b.addEventListener('click', function () { go(l); });
    return b;
  }

  function searchKey(s) {
    s = String(s || '').toLowerCase();
    try { s = s.normalize('NFD').replace(/[\u0300-\u036f]/g, ''); } catch (e) {}
    return s;
  }
  function drawSwitch() {
    if (avail.length < 2) return;
    var st = document.createElement('style');
    st.textContent =
      '.i18n-row{display:flex;justify-content:flex-end;align-items:center;margin:-6px 0 16px}' +
      '.i18n-switch{position:relative;display:inline-flex;gap:3px;padding:4px;background:#fff;' +
      'border:2px solid rgba(255,255,255,.9);border-radius:999px;box-shadow:0 6px 16px rgba(115,70,111,.10)}' +
      '.i18n-opt{display:inline-flex;align-items:center;gap:6px;border:0;background:transparent;color:#7a6a88;' +
      'font:inherit;font-size:13px;font-weight:700;line-height:1;min-height:34px;padding:8px 13px;border-radius:999px;cursor:pointer;' +  /* 2026-09-26 高さ29px→34px（指で押しやすく） */
      'white-space:nowrap;transition:background .2s,color .2s,transform .15s}' +
      '.i18n-opt:hover{background:rgba(139,109,232,.10)}' +
      '.i18n-opt.on{background:#8b6de8;color:#fff;box-shadow:0 4px 10px rgba(139,109,232,.35)}' +
      '.i18n-opt:active{transform:scale(.96)}' +
      '.i18n-opt:focus-visible{outline:3px solid rgba(139,109,232,.45);outline-offset:2px}' +
      '.i18n-flag{font-size:17px;line-height:1}' +
      '.i18n-menu{position:absolute;right:0;top:calc(100% + 6px);z-index:60;display:flex;flex-direction:column;gap:2px;' +
      'width:min(340px,calc(100vw - 32px));min-width:0;max-height:min(72vh,560px);overflow:hidden;padding:8px;' +
      'background:#fff;border-radius:18px;box-shadow:0 14px 34px rgba(115,70,111,.22)}' +
      '.i18n-menu[hidden]{display:none}.i18n-menu .i18n-opt{justify-content:flex-start;width:100%;white-space:normal;text-align:start}' +
      /* 🔤 頭文字のボタン（2026-09-25 本人：検索欄はスマホでキーボードが出てじゃま。A〜Zで飛べるほうがいい） */
      '.i18n-az{display:flex;flex-wrap:wrap;gap:4px;flex:none;padding:2px 2px 8px;border-bottom:1.5px solid rgba(0,0,0,.07);margin-bottom:4px}' +
      '.i18n-az button{min-width:30px;height:30px;padding:0 6px;border:0;border-radius:9px;background:#f3effc;color:#6a55c8;' +
      'font:inherit;font-size:13px;font-weight:900;line-height:1;cursor:pointer;transition:background .15s,color .15s}' +
      '.i18n-az button:hover{background:rgba(139,109,232,.2)}' +
      '.i18n-az button.on{background:#8b6de8;color:#fff}' +
      '.i18n-az button:focus-visible{outline:3px solid rgba(139,109,232,.45);outline-offset:1px}' +
      '.i18n-menu .i18n-opt.hit{background:rgba(139,109,232,.14)}' +
      '.i18n-results{min-height:0;overflow-y:auto;overscroll-behavior:contain}' +
      '.i18n-group-label{padding:8px 10px 4px;color:#8a7d99;font-size:11px;font-weight:900;letter-spacing:.04em}' +
      '.i18n-menu .i18n-name{min-width:0;overflow-wrap:anywhere}' +
      '.i18n-float{position:fixed;top:10px;right:10px;z-index:50}' +
      '.i18n-cur{gap:7px;max-width:min(100%,calc(100vw - 90px));padding:8px 12px 8px 10px;background:#8b6de8;color:#fff;box-shadow:0 4px 12px rgba(139,109,232,.35)}' +
      '.i18n-cur:hover{background:#7a5bdc}' +
      '.i18n-globe{font-size:17px;line-height:1}' +
      '.i18n-cur .i18n-name{overflow:hidden;text-overflow:ellipsis}' +
      '.i18n-stack{display:inline-flex;flex:none;margin-left:2px}.i18n-stack i{font-style:normal;font-size:13px;line-height:1;' +
      'margin-left:-5px;padding:2px;border-radius:50%;background:rgba(255,255,255,.92);box-shadow:0 0 0 1.5px #8b6de8}' +
      '.i18n-stack i:first-child{margin-left:0}.i18n-caret{font-size:11px;opacity:.9}' +
      '.i18n-head{padding:7px 10px 4px;font-size:11.5px;font-weight:900;letter-spacing:.04em;color:#8a7d99}' +
      '.i18n-en{margin-left:auto;padding-left:12px;font-size:11px;font-weight:700;opacity:.6}' +
      '.i18n-menu .i18n-opt.on .i18n-en{opacity:.85}' +
      '.i18n-menu .i18n-opt.on::after{content:"✓";margin-left:8px;font-weight:900}' +
      '.i18n-nudge .i18n-cur{animation:i18n-pulse 1.6s ease-in-out 3}' +
      '@keyframes i18n-pulse{0%,100%{box-shadow:0 4px 12px rgba(139,109,232,.35)}50%{box-shadow:0 0 0 7px rgba(139,109,232,.22),0 4px 12px rgba(139,109,232,.35)}}' +
      /* 2026-10-03 吹き出しは、言語ボタンの「左」に出す（下に出すと、題の上の札「⚡ 69秒」や題に重なっていた）。
         その行の左側はいつも空いている。入りきらない狭い画面では出さない（下の JS） */
      '.i18n-tip{position:absolute;right:calc(100% + 12px);top:0;bottom:0;margin:auto 0;width:max-content;max-width:250px;height:-webkit-fit-content;height:fit-content;z-index:55;' +
      'display:flex;align-items:center;gap:6px;white-space:normal;line-height:1.3;' +
      'padding:7px 7px 7px 12px;border-radius:14px;background:#2b2440;color:#fff;font-size:13px;font-weight:800;cursor:pointer;' +
      'box-shadow:0 10px 26px rgba(0,0,0,.2);animation:i18n-tip-in .35s cubic-bezier(.2,1.4,.4,1) both}' +
      '.i18n-tip::before{content:"";position:absolute;right:-5px;top:50%;margin-top:-6px;width:12px;height:12px;background:#2b2440;transform:rotate(45deg)}' +
      '.i18n-tip button{border:0;background:rgba(255,255,255,.14);color:#fff;width:32px;height:32px;flex:none;border-radius:50%;font-size:15px;line-height:1;cursor:pointer}' +
      'html[dir="rtl"] .i18n-tip{right:auto;left:calc(100% + 12px)}html[dir="rtl"] .i18n-tip::before{right:auto;left:-5px}' +
      '.i18n-tip .i18n-tip-text{color:#fff !important;font-weight:800}' +
      '.i18n-tip-text.in{animation:i18n-tip-in .3s ease-out both}.i18n-tip.bye{opacity:0;transition:opacity .35s}' +
      '@keyframes i18n-tip-in{from{opacity:0;transform:translateX(6px)}to{opacity:1;transform:none}}' +
      'html[data-theme="dark"] .i18n-tip,html[data-theme="dark"] .i18n-tip::before{background:#f1ecfb;color:#2b2440}' +
      'html[data-theme="dark"] .i18n-tip .i18n-tip-text{color:#2b2440 !important}' +
      'html[data-theme="dark"] .i18n-tip button{background:rgba(0,0,0,.08);color:#2b2440}' +
      'html[data-theme="dark"] .i18n-head{color:#b3aac4;border-color:rgba(255,255,255,.1)}' +
      'html[data-theme="dark"] .i18n-group-label{color:#b3aac4}' +
      'html[data-theme="dark"] .i18n-az{border-color:rgba(255,255,255,.1)}' +
      'html[data-theme="dark"] .i18n-az button{background:#3a3450;color:#d9ceff}' +
      'html[data-theme="dark"] .i18n-az button.on{background:#8b6de8;color:#fff}' +
      'html[data-theme="dark"] .i18n-stack i{background:#3a3450}' +
      '@media (prefers-reduced-motion: reduce){html:not([data-motion="on"]) :is(.i18n-nudge .i18n-cur,.i18n-tip,.i18n-tip-text.in){animation:none}}' +
      /* 読む人には関係ない「PUBLIC」は見せない（HTMLには残す。check.py が確かめるため） */
      '.stage-public{display:none !important}' +
      '@media (prefers-reduced-motion: reduce){html:not([data-motion="on"]) .i18n-opt{transition:none}}';
    document.head.appendChild(st);

    var wrap = document.createElement('div');
    wrap.className = 'i18n-switch';
    wrap.setAttribute('translate', 'no');
    wrap.setAttribute('role', 'group');
    wrap.setAttribute('aria-label', MENU.languageLabel || 'Language');

    if (avail.length <= 2) {
      avail.forEach(function (l) { wrap.appendChild(option(l)); });
    } else {
      /* 地球儀＋いまの言語＋代表的な言語の小さな旗を重ね、一覧は A〜Z の頭文字で飛べるようにする */
      var cur = document.createElement('button');
      cur.type = 'button';
      cur.className = 'i18n-opt i18n-cur';
      cur.setAttribute('aria-haspopup', 'true');
      cur.setAttribute('aria-expanded', 'false');
      cur.setAttribute('aria-label', (MENU.languageLabel || 'Language') + ': ' + NAMES[lang]);
      cur.setAttribute('aria-controls', 'i18n-language-menu');
      var globe = document.createElement('span');
      globe.className = 'i18n-globe'; globe.setAttribute('aria-hidden', 'true'); globe.textContent = '🌐';
      var currentName = document.createElement('span');
      currentName.className = 'i18n-name'; currentName.textContent = NAMES[lang];
      var stack = document.createElement('span');
      stack.className = 'i18n-stack'; stack.setAttribute('aria-hidden', 'true');
      ['en', 'ja', 'ko', 'zh', 'zh-Hant'].filter(function (l) { return l !== lang && avail.indexOf(l) >= 0; })
        .slice(0, 4).forEach(function (l) {
          var flag = document.createElement('i'); flag.textContent = FLAGS[l]; stack.appendChild(flag);
        });
      var caret = document.createElement('span');
      caret.className = 'i18n-caret'; caret.setAttribute('aria-hidden', 'true'); caret.textContent = '▾';
      cur.appendChild(globe); cur.appendChild(currentName); cur.appendChild(stack); cur.appendChild(caret);
      var menu = document.createElement('div');
      menu.className = 'i18n-menu';
      menu.id = 'i18n-language-menu';
      menu.setAttribute('role', 'group');
      menu.setAttribute('aria-label', MENU.chooseLanguage || 'Choose a language');
      menu.hidden = true;
      var az = document.createElement('div');
      az.className = 'i18n-az';
      az.setAttribute('role', 'group');
      az.setAttribute('aria-label', MENU.jumpByEnglishName || 'Jump by the first letter of the English name');
      menu.appendChild(az);

      var results = document.createElement('div'); results.className = 'i18n-results';
      var suggestedGroup = document.createElement('section');
      var suggestedTitle = document.createElement('div');
      suggestedTitle.className = 'i18n-group-label';
      suggestedTitle.textContent = MENU.suggested || 'Suggested';
      suggestedGroup.appendChild(suggestedTitle);
      var recommended = [];
      [browserChoice(), 'en', 'ja'].forEach(function (l) {
        if (l && avail.indexOf(l) >= 0 && recommended.indexOf(l) < 0 && recommended.length < 3) recommended.push(l);
      });
      recommended.forEach(function (l) { suggestedGroup.appendChild(option(l)); });
      results.appendChild(suggestedGroup);

      var allGroup = document.createElement('section');
      var allTitle = document.createElement('div');
      allTitle.className = 'i18n-group-label';
      allTitle.textContent = MENU.allLanguages || 'All languages';
      allGroup.appendChild(allTitle);
      var allOptions = avail.slice().sort(function (a, b) {
        return searchKey(EN_NAMES[a] || a).localeCompare(searchKey(EN_NAMES[b] || b), 'en');
      });
      allOptions.forEach(function (l) { allGroup.appendChild(option(l)); });
      results.appendChild(allGroup); menu.appendChild(results);

      /* 英語名の頭文字ごとに、最初の言語へ飛ぶ。言語のある文字だけボタンにする（押しても空振りしないように） */
      function letterOf(l) { return (searchKey(EN_NAMES[l] || l).charAt(0) || '#').toUpperCase(); }
      var firstOf = {};
      Array.prototype.forEach.call(allGroup.querySelectorAll('.i18n-opt'), function (b) {
        var k = letterOf(b.getAttribute('data-lang'));
        if (!firstOf[k]) firstOf[k] = b;
      });
      Object.keys(firstOf).sort().forEach(function (k) {
        var lb = document.createElement('button');
        lb.type = 'button'; lb.textContent = k;
        lb.addEventListener('click', function (e) {
          e.stopPropagation();
          Array.prototype.forEach.call(az.children, function (x) { x.classList.toggle('on', x === lb); });
          Array.prototype.forEach.call(allGroup.querySelectorAll('.i18n-opt.hit'), function (x) { x.classList.remove('hit'); });
          var target = firstOf[k];
          results.scrollTop = target.offsetTop - results.offsetTop - 4;
          Array.prototype.forEach.call(allGroup.querySelectorAll('.i18n-opt'), function (x) {
            if (letterOf(x.getAttribute('data-lang')) === k) x.classList.add('hit');
          });
        });
        az.appendChild(lb);
      });

      var tip = null;
      function closeMenu(returnFocus) {
        menu.hidden = true;
        cur.setAttribute('aria-expanded', 'false');
        if (returnFocus) cur.focus();
      }
      function positionMenu() {
        var anchor = cur.getBoundingClientRect();
        menu.style.position = 'fixed';
        menu.style.right = 'auto';
        menu.style.left = '0px';
        menu.style.top = Math.round(anchor.bottom + 6) + 'px';
        var margin = 12, width = menu.getBoundingClientRect().width;
        var left = Math.max(margin, Math.min(anchor.right - width, window.innerWidth - width - margin));
        var top = anchor.bottom + 6, height = menu.getBoundingClientRect().height;
        if (top + height > window.innerHeight - margin) top = Math.max(margin, anchor.top - height - 6);
        menu.style.left = Math.round(left) + 'px';
        menu.style.top = Math.round(top) + 'px';
      }
      function seenTip() { try { localStorage.setItem(TIP_KEY, '1'); } catch (e) {} if (tip) { tip.remove(); tip = null; } wrap.classList.remove('i18n-nudge'); }
      cur.addEventListener('click', function (e) {
        e.stopPropagation();
        seenTip();
        menu.hidden = !menu.hidden;
        cur.setAttribute('aria-expanded', String(!menu.hidden));
        if (!menu.hidden) positionMenu();
        /* 開いても入力欄にはフォーカスしない（スマホでキーボードが出ないように） */
      });
      window.addEventListener('resize', function () { if (!menu.hidden) positionMenu(); });
      window.addEventListener('scroll', function () { if (!menu.hidden) positionMenu(); }, { passive: true });
      document.addEventListener('click', function (e) { if (!wrap.contains(e.target)) closeMenu(false); });
      document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !menu.hidden) closeMenu(true); });
      wrap.addEventListener('focusout', function () {
        setTimeout(function () { if (!wrap.contains(document.activeElement)) closeMenu(false); }, 0);
      });
      menu.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') { e.preventDefault(); e.stopPropagation(); closeMenu(true); return; }
        if (e.key !== 'ArrowDown' && e.key !== 'ArrowUp') return;
        var buttons = Array.prototype.filter.call(menu.querySelectorAll('.i18n-opt'), function (b) {
          return !b.hidden && !b.closest('[hidden]');
        });
        if (!buttons.length) return;
        var at = buttons.indexOf(document.activeElement), next;
        if (at < 0) next = e.key === 'ArrowDown' ? 0 : buttons.length - 1;
        else next = (at + (e.key === 'ArrowDown' ? 1 : buttons.length - 1)) % buttons.length;
        e.preventDefault(); buttons[next].focus();
      });
      cur.addEventListener('keydown', function (e) {
        if (e.key !== 'ArrowDown' || menu.hidden) return;
        var first = menu.querySelector('.i18n-results .i18n-opt');
        if (first) { e.preventDefault(); first.focus(); }
      });
      wrap.appendChild(cur);
      wrap.appendChild(menu);

      var TIP_KEY = 'pengesso-lang-tip-seen', seen = false;
      try { seen = localStorage.getItem(TIP_KEY) === '1'; } catch (e) {}
      /* 2026-09-26 ×を押さないと、記事を開くたびに毎回出て、上の札に重なっていた。2回見せたら、もう出さない */
      try {
        var shown = +(localStorage.getItem(TIP_KEY + '-n') || 0);
        if (!seen && shown >= 2) seen = true;
        else if (!seen) localStorage.setItem(TIP_KEY + '-n', String(shown + 1));
      } catch (e) {}
      if (!seen) {
        var SAY = { en: 'Read in English', ja: '日本語で読めます', ko: '한국어로도 읽을 수 있어요', zh: '也可以用中文阅读', 'zh-Hant': '也可以用中文閱讀' };
        var lines = avail.filter(function (l) { return l !== lang && SAY[l]; }).map(function (l) { return SAY[l]; });
        if (lines.length) {
          tip = document.createElement('div');
          tip.className = 'i18n-tip';
          tip.setAttribute('role', 'status');
          tip.innerHTML = '<span class="i18n-tip-text"></span><button type="button">×</button>';
          tip.querySelector('button').setAttribute('aria-label', (LANGS[lang] && LANGS[lang].noticeDismiss) || 'Close');
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
          /* 置いたあとで、ボタンの左にどれだけ空きがあるかを測る。狭い（スマホの 320px など）ときは出さない */
          setTimeout(function () {
            if (!tip) return;
            var r = wrap.getBoundingClientRect(), rtl = document.documentElement.dir === 'rtl';
            var room = (rtl ? innerWidth - r.right : r.left) - 12 - 12;
            if (room < 130) { tip.remove(); tip = null; wrap.classList.remove('i18n-nudge'); clearInterval(iv); return; }
            tip.style.maxWidth = Math.min(room, 250) + 'px';
          }, 0);
        }
      }
    }

    /* 上のバーはスマホだと満員なので、そのすぐ下に1行つくって右に置く */
    var spot = document.querySelector('[data-i18n-switch]');
    var bar = document.querySelector('.topbar') || document.querySelector('body > header, main > header, header');
    var foot = document.createElement('div');
    foot.className = 'theme-foot'; foot.appendChild(themeButton()); foot.appendChild(motionButton());
    var tail = document.querySelector('footer') || document.querySelector('main') || document.body;
    tail.appendChild(foot);
    if (spot) { spot.appendChild(wrap); switchMount = spot; }
    else if (bar) {
      var row = document.createElement('div');
      row.className = 'i18n-row';
      row.appendChild(wrap);
      bar.parentNode.insertBefore(row, bar.nextSibling);
      switchMount = row;
    } else { wrap.className += ' i18n-float'; document.body.appendChild(wrap); switchMount = wrap; }
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
      '.i18n-notice p{margin:0;flex:1;font-size:13px;line-height:1.55;color:#6b5a3a;white-space:pre-line}' +
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

  /* ✨ 端末が「動きを減らす」設定のとき、最初の3回だけ、言語ボタンの下に小さなお知らせを出す（2026-10-04）
     「アニメーションが出ない」のは壊れているのではなく、端末の設定のせいだと分かるように。ここで ON にもできる */
  var MOTION_NOTE = {
    en: ['Your device is set to reduce motion, so the animations on this site are off.', 'Turn animations on', 'Keep them off'],
    ja: ['この端末は「動きを減らす」設定のため、このサイトのアニメーションを止めています。', '動きをつける', 'このまま'],
    ko: ['이 기기는 “동작 줄이기” 설정이라서, 이 사이트의 애니메이션을 멈추고 있어요.', '움직임 켜기', '그대로 두기'],
    zh: ['这台设备开启了“减少动态效果”，所以本站的动画已关闭。', '打开动效', '保持关闭'],
    'zh-Hant': ['這台裝置開啟了「減少動態效果」，所以本站的動畫已關閉。', '開啟動態', '保持關閉']
  };
  function drawMotionNote() {
    var M = window.pengessoMotion, KEYN = 'pengesso-motion-note';
    if (!M || !M.os() || M.mode() !== 'auto' || !switchMount) return;
    var n = 0; try { n = +localStorage.getItem(KEYN) || 0; } catch (e) {}
    if (n >= 3) return;
    try { localStorage.setItem(KEYN, String(n + 1)); } catch (e) {}
    var W = MOTION_NOTE[lang] || MOTION_NOTE.en;
    var st = document.createElement('style');
    st.textContent = '.motion-note{margin:8px 0 14px;padding:12px 14px;border-radius:16px;background:#eef6ff;border:2px solid #cfe3fb;color:#1f4b80;font-size:13px;font-weight:700;line-height:1.55}' +
      '.motion-note p{margin:0 0 10px}.motion-note .mn-btns{display:flex;flex-wrap:wrap;align-items:center;gap:6px 10px}' +
      '.motion-note button{flex:none;min-height:40px;padding:0 16px;border:0;border-radius:999px;font:inherit;font-size:13px;font-weight:800;cursor:pointer;-webkit-tap-highlight-color:transparent}' +
      '.motion-note .mn-on{background:#2f6fd0;color:#fff}.motion-note .mn-off{background:transparent;color:#1f4b80;text-decoration:underline}' +
      'html[data-theme="dark"] .motion-note{background:#182335;border-color:#2b4468;color:#cfe3ff}html[data-theme="dark"] .motion-note .mn-off{color:#cfe3ff}';
    document.head.appendChild(st);
    var box = document.createElement('div');
    box.className = 'motion-note'; box.setAttribute('role', 'note'); box.setAttribute('translate', 'no');
    box.innerHTML = '<p></p><div class="mn-btns"><button type="button" class="mn-on"></button><button type="button" class="mn-off"></button></div>';
    var bt = box.lastChild.children;
    box.firstChild.textContent = '✨ ' + W[0];
    bt[0].textContent = W[1]; bt[1].textContent = W[2];
    bt[0].addEventListener('click', function () { M.set('on'); box.remove(); try { localStorage.setItem(KEYN, '9'); } catch (e) {} });
    bt[1].addEventListener('click', function () { box.remove(); try { localStorage.setItem(KEYN, '9'); } catch (e) {} });
    if (switchMount.parentNode) switchMount.parentNode.insertBefore(box, switchMount.nextSibling);
  }

  /* ── 📚 勉強モード（2026-10-03 本人の要望）────────────────────────
     記事の言語ボタンの下に「勉強バー」を出す。
       英語以外で読むとき … 🇬🇧 英語の勉強をする（訳した文のすぐ下に、もとの英文）
       英語で読むとき     … 🌏 ほかの言語も見る（英文の下に、日本語・韓国語などの訳。言語は選べる）
       ○○の濃さ          … いま読んでいる言語の文を薄くして、下の言語に集中できる
       💻 IT用語で言うと   … works/<slug>/it.<lang>.json がある記事だけ。AIが文を強引に IT の言葉で言い換えたもの
                             （記事の <meta name="pengesso-it" content="ja en"> が目印）
       ？                  … なぜこの機能があるのか（飼い主が英語と IT 用語を勉強中）
     どれも localStorage に覚える（トップの「読みながら、ちょっと勉強」からもオンにできる）。
     最初の3回だけ、吹き出しで「英語の勉強もしますか？」「IT業界の人ですか？」と声をかける */
  var LEARN_KEY = 'pengesso-learn', NATIVE_KEY = 'pengesso-native-alpha', IT_KEY = 'pengesso-it', GCP_KEY = 'pengesso-gcp',
      STUDY_TIP_KEY = 'pengesso-study-tip', SUB_KEY = 'pengesso-learn-lang';
  var STUDY_WORDS = {
    ja: { en: '英語の勉強をする', say: '英語を聞く', it: 'IT用語で言うと', gcp: 'Google Cloud で言うと', dim: '日本語の濃さ', re: 'その他の勉強', off: 'なし', popT: 'ほかの言葉で、言い換えて読む', popS: 'AI が、日記をむりやりその分野の言葉で言い換えます。いちどに1つだけ',
          packs: { it: 'IT用語', gcp: 'Google Cloud', net: 'ネットワーク', srv: 'サーバー', sec: 'セキュリティ', biz: 'ビジネス横文字', fin: '金融', med: '医療', nur: '看護' },
          net: 'ネットワークで言うと', srv: 'サーバーで言うと', sec: 'セキュリティで言うと', biz: 'ビジネス横文字で言うと', fin: '金融で言うと', med: '医療で言うと', nur: '看護で言うと',
          tips: ['英語の勉強も、いっしょにしますか？ 🇬🇧 をオンにすると、日本語のすぐ下に英語が出ます',
                 'IT業界の人ですか？ 飼い主もIT用語を勉強中。「📚 その他の勉強」で「IT用語」を選ぶと、日記がめちゃくちゃ強引にIT用語に言い換わります'],
          itNote: '🤖 AIが、めちゃくちゃ強引に言い換えています。略語はフルスペルで書いています',
          about: '🐧 飼い主は、英語の勉強を続けたいと思っています。そして、IT企業で働いていてテクノロジーが好きなので、IT用語もついでに覚えたいと思っています。' +
                 'だから、このブログには小さな勉強モードが2つあります。🇬🇧 をオンにすると、日本語のすぐ下にもとの英文が出ます（日本語を薄くすると、英語に集中できます）。' +
                 '「📚 その他の勉強」を選ぶと、AIが日記をめちゃくちゃ強引に IT用語・金融・医療・看護などの言葉に言い換えます（いちどに1つだけ）。英語やIT用語に、ふわっとさわってみたい人は、よかったらどうぞ。' },
    ko: { en: '영어 공부하기', say: '영어 듣기', dim: '한국어 진하기', re: '다른 공부', off: '없음', popT: '다른 분야의 말로 바꿔 읽기', popS: 'AI가 일기를 억지로 그 분야의 말로 바꿔 말해요. 한 번에 하나만',
          packs: { net: '네트워크', srv: '서버', sec: '보안', biz: '비즈니스 용어', fin: '금융', med: '의료', nur: '간호' },
          net: '네트워크로 말하면', srv: '서버로 말하면', sec: '보안으로 말하면', biz: '비즈니스 용어로 말하면', fin: '금융으로 말하면', med: '의료로 말하면', nur: '간호로 말하면',
          itNote: '🤖 AI가 아주 억지로 각 분야의 말로 바꿔 말하고 있어요(베타). 약어는 풀어서 써요',
          tips: ['영어 공부도 같이 할까요? 🇬🇧 를 켜면 한국어 바로 아래에 영어가 나와요'],
          about: '🐧 주인은 영어 공부를 계속하고 싶어 합니다. 그리고 IT 회사에서 일하고 기술을 좋아해서, IT 용어도 같이 배우고 싶어 합니다. ' +
                 '그래서 이 블로그에는 작은 공부 모드가 있습니다. 🇬🇧 를 켜면 한국어 바로 아래에 원래 영어 문장이 나옵니다. 한국어를 연하게 하면 영어에 집중할 수 있어요.' },
    zh: { en: '学英语', say: '听英文', dim: '中文的浓淡',
          tips: ['要不要顺便学英语？打开 🇬🇧，中文下面就会出现英文'],
          about: '🐧 主人想继续学习英语。主人也在IT公司工作，喜欢科技，所以也想顺便学一些IT用语。所以这个博客有小小的学习模式。打开 🇬🇧，中文下面就会出现原来的英文。把中文调淡，就能专心看英文。' },
    'zh-Hant': { en: '學英語', say: '聽英文', dim: '中文的濃淡',
          tips: ['要不要順便學英文？打開 🇬🇧，中文下面就會出現英文'],
          about: '🐧 主人想繼續學習英文。主人也在IT公司工作，喜歡科技，所以也想順便學一些IT用語。所以這個部落格有小小的學習模式。打開 🇬🇧，中文下面就會出現原來的英文。把中文調淡，就能專心看英文。' }
  };
  var STUDY_DEFAULT = { en: 'Study English', say: 'Listen', dim: 'My language',
    tips: ['Learning English too? Turn on 🇬🇧 to see the English under each sentence'],
    about: '🐧 Pengesso’s owner wants to keep studying English, and also works at an IT company and loves technology. ' +
           'So this blog has small study modes. Turn on 🇬🇧 to see the original English under each sentence. Make your language lighter to focus on the English.' };
  var STUDY_EN = { en: 'Study Japanese', furi: 'Furigana', rom: 'Romaji', say: 'Listen', other: 'Other language', dim: 'English', it: 'IT words', gcp: 'Google Cloud', re: 'Other study', off: 'None', popT: 'Read it in other words', popS: 'AI re-says each line, very forcibly, with words from one field. One at a time',
    net: 'Network', srv: 'Server', sec: 'Security', biz: 'Business jargon', fin: 'Finance', med: 'Medical', nur: 'Nursing',
    tips: ['Learning Japanese? Turn on 🇯🇵 to see the original Japanese under each line, with furigana (reading help)',
           'Work in IT? Pick “✨ Reword”, then “IT words”, to see this diary in IT words, in a very forced way'],
    itNote: '🤖 AI re-says each line in a very forced way. Short forms are spelled out',
    about: '🐧 Pengesso’s owner writes every post in Japanese first, in simple everyday words, so every English line has the original Japanese. Turn on 🇯🇵 to see it under each line. ' +
           'Furigana shows how to read the kanji, Romaji shows the sounds in English letters, and 🔊 reads a line aloud. ' +
           'These aids are made automatically, so they can have mistakes. Make the English lighter to focus on the Japanese. ' +
           'You can also pick another language. ✨ Reword makes AI re-say each line with IT words (or Google Cloud, Network, and more), in a very forced way. One style at a time.' };
  function learnable(el) {
    if (!el.closest || !el.closest('main')) return false;
    if (el.closest('.topbar, .label, .card-head, .next, .prev, .related, .to-list, .i18n-row, .i18n-switch, .study-bar, .study-info, .theme-foot, nav, button, .part-nav, [translate="no"]')) return false;
    return /^(P|LI|H1|H2|H3|FIGCAPTION|BLOCKQUOTE|DT|DD)$/.test(el.tagName) || el.classList.contains('big');
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function get(k, d) { try { var v = localStorage.getItem(k); return v === null ? d : v; } catch (e) { return d; } }
  function set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  function plain(html) { var t = document.createElement('template'); t.innerHTML = html; return t.content.textContent; }

  /* 英語で読んでいるとき：訳はしないので、ここで英文の「かたまり」を集める（translate() の unitOf と同じ考え方） */
  function nrm(s) { return String(s).replace(/\s+/g, ' ').trim(); }
  function fp2(s) { var h = 0x811c9dc5; for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619) >>> 0; } return h.toString(36); }
  var INL = { A:1, ABBR:1, B:1, BR:1, CODE:1, EM:1, I:1, MARK:1, Q:1, S:1, SMALL:1, STRONG:1, SUB:1, SUP:1, U:1, TIME:1, WBR:1, SPAN:1 };
  function collectEnglish() {
    var out = [];
    document.querySelectorAll('main p, main li, main h1, main h2, main h3, main figcaption, main blockquote, main dt, main dd, main .big').forEach(function (el) {
      if (!learnable(el)) return;
      var parts = [], shown = [], direct = false;
      for (var c = el.firstChild; c; c = c.nextSibling) {
        if (c.nodeType === 3) { parts.push(c.nodeValue); shown.push(c.nodeValue); if (/\S/.test(c.nodeValue)) direct = true; }
        else if (c.nodeType === 1 && INL[c.tagName] && !c.hasAttribute('class') && !c.hasAttribute('id')) {
          parts.push(c.textContent); shown.push(c.tagName === 'BR' ? '\n' : c.textContent);
        }
      }
      if (direct) out.push({ el: el, en: nrm(parts.join('')) });
    });
    return out;
  }

  function drawLearn(list, enMode) {
    if (!list.length || document.querySelector('.study-bar')) return;
    var root = document.documentElement;
    var W = enMode ? STUDY_EN : (STUDY_WORDS[lang] || STUDY_DEFAULT);
    var itMeta = document.querySelector('meta[name="pengesso-it"]');
    var itLang = enMode ? 'en' : lang;
    /* 🧩 言い換えパック（2026-10-03）。meta の content は「ja en gcp」（💻・☁️ の古い形）か「net:ja,en,ko」の形。
       どのパックが、どの言語で読めるかを決める。ボタンの並びも、文の下の並びもこの順 */
    /* 2026-10-07 本人：言い換えは 💻 IT用語 と 💼 ビジネス用語 の2つだけ。ほかは archive/rewording-packs/ にしまった */
    var PACK_ORDER = ['it', 'biz'];
    var PACK_ICON = { it: '💻', gcp: '☁️', net: '🌐', srv: '🖥', sec: '🔐', biz: '💼', fin: '💴', med: '🩺', nur: '💉' };
    /* Google Cloud だけは絵文字の雲ではなく、本物のマークを絵文字の大きさで（2026-10-03 本人の要望） */
    var GCP_MARK = '<img class="gcp-mark" src="/assets/gcp-mark.png" alt="Google Cloud" width="20" height="16" decoding="async">';
    function packIcon(kind) { return kind === 'gcp' ? GCP_MARK : PACK_ICON[kind]; }
    var packLangs = {};
    if (itMeta) {
      var legacy = [];
      itMeta.content.split(/\s+/).forEach(function (t) {
        if (!t) return;
        var m = t.split(':');
        if (m.length === 2) packLangs[m[0]] = m[1].split(',');
        else if (t === 'gcp') packLangs.gcp = 'legacy';
        else legacy.push(t);
      });
      if (legacy.length && !packLangs.it) packLangs.it = legacy;
      if (packLangs.gcp === 'legacy') packLangs.gcp = packLangs.it || [];
    }
    var packs = PACK_ORDER.filter(function (k) { return packLangs[k] && packLangs[k].indexOf(itLang) >= 0 && W[k]; });
    var hasIt = packs.length > 0;
    var st = document.createElement('style');
    st.textContent =
      '.study-bar{position:relative;display:flex;flex-wrap:wrap;align-items:center;gap:8px 6px;margin:-8px 0 16px;padding-top:7px}' +
      '.study-btn{position:relative;display:inline-flex;align-items:center;gap:7px;min-height:44px;padding:6px 12px 6px 8px;' +
      'border:2px solid rgba(255,255,255,.9);border-radius:999px;background:#fff;color:#5b4bb0;font:inherit;font-size:13px;font-weight:800;' +
      'line-height:1;cursor:pointer;box-shadow:0 6px 16px rgba(115,70,111,.10);white-space:nowrap;-webkit-tap-highlight-color:transparent}' +
      '.study-btn:active,.study-re:active,.study-q:active,.study-chip:active,.dim-b:active{transform:scale(.96)}' +
      '.study-btn:focus-visible,.study-q:focus-visible,.study-sel:focus-visible,.study-chip:focus-visible,.dim-b:focus-visible{outline:3px solid rgba(139,109,232,.45);outline-offset:2px}' +
      '.study-sw{position:relative;flex:none;width:34px;height:20px;border-radius:999px;background:#ddd6f3;transition:background .2s}' +
            '.study-sw::after{content:"";position:absolute;left:3px;top:3px;width:14px;height:14px;border-radius:50%;background:#fff;' +
      'box-shadow:0 1px 3px rgba(0,0,0,.25);transition:transform .2s}' +
      '.study-btn[aria-pressed="true"] .study-sw{background:#8b6de8}' +
            '.study-btn[aria-pressed="true"] .study-sw::after{transform:translateX(14px)}' +
      'html[dir="rtl"] .study-btn[aria-pressed="true"] .study-sw::after{transform:translateX(-14px)}' +
      '.study-sel{min-height:40px;max-width:150px;padding:0 10px;border:2px solid rgba(255,255,255,.9);border-radius:999px;background:#fff;' +
      'color:#5b4bb0;font:inherit;font-size:13px;font-weight:800;box-shadow:0 6px 16px rgba(115,70,111,.10)}' +
      '.study-q{flex:none;width:40px;height:40px;padding:0;border:2px solid rgba(255,255,255,.9);border-radius:50%;background:#fff;color:#5b4bb0;' +
      'font:inherit;font-size:16px;font-weight:900;cursor:pointer;box-shadow:0 6px 16px rgba(115,70,111,.10);-webkit-tap-highlight-color:transparent}' +
      '.study-q[aria-expanded="true"]{background:#5b4bb0;color:#fff}' +
      '.study-info{margin:-6px 0 16px;padding:14px 16px;border-radius:18px;background:#f3effc;color:#3f3478;font-size:13.5px;font-weight:700;line-height:1.7}' +
      '.study-info[hidden]{display:none}' +
      /* 🎚 濃さは「指で押せる4つのボタン」（2026-10-04 本人：スマホで日本語を薄くできない。スライダーは高さ16pxで、指でつかみにくかった） */
      '.study-tray{display:none;flex:1 0 100%;flex-wrap:wrap;align-items:center;gap:8px 12px;padding:8px 10px;border-radius:22px;background:rgba(255,255,255,.55);box-shadow:inset 0 0 0 2px rgba(255,255,255,.85)}' +
      'html.learn-on .study-tray{display:flex;animation:learnIn .3s ease both}' +
      '.study-chip{display:none;align-items:center;gap:6px;min-height:40px;padding:0 14px;border:2px solid rgba(139,109,232,.28);border-radius:999px;background:#fff;color:#5b4bb0;' +
      'font:inherit;font-size:13px;font-weight:800;line-height:1;cursor:pointer;white-space:nowrap;-webkit-tap-highlight-color:transparent}' +
      '.study-chip[aria-pressed="true"]{background:#8b6de8;border-color:#8b6de8;color:#fff}.study-chip[aria-pressed="true"]::before{content:"✓";font-weight:900}' +
      'html.learn-on.sub-ja .study-chip.ja-only,html.learn-on.tts-ok .study-chip.say-btn{display:inline-flex}' +
      '.study-dim{display:inline-flex;flex-wrap:wrap;align-items:center;gap:6px;color:#5b4bb0;font-size:12.5px;font-weight:800}.dim-l{margin-right:2px}' +
      '.dim-b{display:inline-flex;align-items:center;justify-content:center;flex:none;width:46px;height:42px;padding:0;border:2px solid rgba(139,109,232,.28);border-radius:14px;background:#fff;color:#5b4bb0;' +
      'font:inherit;font-size:18px;font-weight:900;line-height:1;cursor:pointer;-webkit-tap-highlight-color:transparent;transition:transform .12s,box-shadow .15s,border-color .15s}' +
      '.dim-b i{font-style:normal;pointer-events:none}.dim-b[aria-pressed="true"]{border-color:#8b6de8;box-shadow:0 0 0 3px rgba(139,109,232,.28)}' +
      /* ✨ 言い換えは1つのメニュー（見えるのは飾り。本物の select は透明で上に重ねる＝スマホ標準の選び方が出る） */
      '.study-re{position:relative;display:inline-flex;align-items:center;gap:6px;min-height:44px;padding:6px 10px 6px 12px;border:2px solid rgba(255,255,255,.9);border-radius:999px;background:#fff;color:#5b4bb0;' +
      'font-size:13px;font-weight:800;line-height:1;white-space:nowrap;box-shadow:0 6px 16px rgba(115,70,111,.10);cursor:pointer;-webkit-tap-highlight-color:transparent}' +
      '.study-re .re-ic{font-size:15px;line-height:1}.study-re .re-caret{font-size:11px;opacity:.7}' +
      '.study-re .re-sel{position:absolute;left:0;top:0;width:100%;height:100%;margin:0;padding:0;border:0;background:transparent;color:transparent;-webkit-text-fill-color:transparent;opacity:0;cursor:pointer;font-size:16px;-webkit-appearance:none;appearance:none}' +
      '.study-re:focus-within{outline:3px solid rgba(139,109,232,.45);outline-offset:2px}' +
      '.study-re{font:inherit;font-size:13px;font-weight:800;cursor:pointer;-webkit-tap-highlight-color:transparent}' +
      /* 📱 2026-10-07：幅390pxで「英語の勉強をする」「その他の勉強」「？」が1行に入らず、？だけ2行目に落ちていた。せまい画面だけ少し詰める */
      '@media (max-width:430px){.study-bar{gap:8px 4px}.study-btn{gap:5px;padding:6px 9px 6px 6px;font-size:12.5px}.study-sw{width:30px}.study-re{gap:4px;padding:6px 8px 6px 9px;font-size:12.5px}.study-q{width:38px;height:38px}.study-btn[aria-pressed="true"] .study-sw::after{transform:translateX(10px)}html[dir="rtl"] .study-btn[aria-pressed="true"] .study-sw::after{transform:translateX(-10px)}}' +
      '.study-re:focus-visible{outline:3px solid rgba(139,109,232,.45);outline-offset:2px}' +
      '.study-pop{position:absolute;z-index:30;width:min(320px,calc(100vw - 32px));padding:14px 12px 10px;border-radius:22px;background:#fff;color:#2b2f45;' +
      'box-shadow:0 18px 48px rgba(35,44,72,.22),0 2px 6px rgba(35,44,72,.08);opacity:0;transform:translateY(-6px) scale(.97);transform-origin:20% 0;' +
      'transition:opacity .18s ease,transform .22s cubic-bezier(.2,.9,.3,1.2)}' +
      '.study-pop.in{opacity:1;transform:none}' +
      '.study-pop .sp-t{margin:0 6px 2px;font-size:14.5px;font-weight:900;color:#232c48}' +
      '.study-pop .sp-s{margin:0 6px 10px;font-size:12px;line-height:1.55;font-weight:700;color:#6b6585}' +
      '.sp-list{display:grid;gap:4px;max-height:min(60vh,420px);overflow:auto;overscroll-behavior:contain}' +
      '.sp-o{position:relative;display:grid;grid-template-columns:30px 1fr 22px;align-items:center;gap:8px;min-height:46px;padding:6px 10px;border-radius:14px;cursor:pointer;font-size:15px;font-weight:800;transition:background .15s}' +
      '.sp-o:hover{background:#f6f3ff}.sp-o input{position:absolute;opacity:0;pointer-events:none}' +
      '.sp-ic{display:grid;place-items:center;font-size:19px;line-height:1}.sp-ic .gcp-mark{width:20px;height:auto}' +
      '.sp-dot{width:20px;height:20px;border-radius:50%;border:2.5px solid #cfc7ea;box-sizing:border-box;transition:border-color .15s,border-width .15s}' +
      '.sp-o:has(input:checked){background:#f1ecff}.sp-o:has(input:checked) .sp-dot{border:6px solid #8b6de8}' +
      '.sp-o:has(input:focus-visible){outline:3px solid rgba(139,109,232,.45);outline-offset:-2px}' +
      'html[data-theme="dark"] .study-pop{background:#22242f;color:#ece8f8;box-shadow:0 18px 48px rgba(0,0,0,.5)}' +
      'html[data-theme="dark"] .study-pop .sp-t{color:#f4f0fa}html[data-theme="dark"] .study-pop .sp-s{color:#b8b3cc}' +
      'html[data-theme="dark"] .sp-o:hover,html[data-theme="dark"] .sp-o:has(input:checked){background:#2e2a44}html[data-theme="dark"] .sp-dot{border-color:#5a5378}' +
      '@media (prefers-reduced-motion:reduce){.study-pop{transition:none}}' +
      '@supports selector(:has(*)){.study-re:focus-within{outline:0}.study-re:has(.re-sel:focus-visible){outline:3px solid rgba(139,109,232,.45);outline-offset:2px}}' +
      '.study-re.on{border-color:var(--pc);background:var(--pb);color:var(--pc)}' +
      '.study-re.it{--pc:#1f7a55;--pb:#eaf7f0}.study-re.gcp{--pc:#1a56c4;--pb:#e8f0fe}.study-re.net{--pc:#0b6e78;--pb:#e4f6f6}' +
      '.study-re.srv{--pc:#3d4a86;--pb:#eef0f7}.study-re.sec{--pc:#a3263a;--pb:#fdeeee}.study-re.biz{--pc:#9a5408;--pb:#fff3e2}' +
      '@media (pointer:coarse){.study-sel{font-size:16px}}' +
      '.learn-en{display:none;margin-top:.4em;padding:.15em 0 .15em .7em;border-left:3px solid #c9bbf5;' +
      'font-size:.86em;line-height:1.55;font-weight:700;color:#5b4bb0;color:color-mix(in srgb,currentColor 35%,#6a55d8);white-space:pre-line;' +
      'text-align:start;unicode-bidi:isolate;letter-spacing:0;border-left-color:rgba(139,109,232,.55)}' +
      'h1 .learn-en,h1 .it-say{font-size:.5em;line-height:1.45}' +
      'html.learn-on .learn-en{display:block;animation:learnIn .45s ease both}' +
      'html.learn-on .learn-en[hidden]{display:none}' +
      'html.learn-on .learn-native{opacity:var(--native-a,1);transition:opacity .15s}' +
      '.it-say{display:none;margin-top:.45em;padding:.45em .7em;border-radius:12px;background:#eaf7f0;color:#1d5c41;' +
      'font-size:.84em;line-height:1.6;font-weight:700;text-align:start}' +
      '.gcp-mark{display:inline-block;width:1.25em;height:auto;vertical-align:-.2em;margin-right:1px}.pack-say{letter-spacing:0}' +
      '.it-say b{color:#0b5e3a;background:linear-gradient(transparent 48%,#a9e4c6 48%);padding:0 .15em;border-radius:3px;font-weight:900}' +
      '.study-beta{padding:1px 5px;border-radius:5px;background:#2d2845;color:#fff;font-size:9.5px;font-weight:900;letter-spacing:.06em;line-height:1.4}' +
      '.study-btn .study-beta,.study-re .study-beta{position:absolute;top:-7px;right:12px;margin:0;pointer-events:none}' +
      '.it-say small{display:block;margin-top:.2em;font-size:.86em;color:#4d7a66}' +
      'html.it-on .it-say{display:block;animation:learnIn .45s ease both}' +
      '.gcp-say{display:none;margin-top:.45em;padding:.45em .7em;border-radius:12px;background:#e8f0fe;color:#174ea6;font-size:.86em;line-height:1.6;font-weight:700;text-align:left}' +
      '.gcp-say b{color:#0b3d91;background:linear-gradient(transparent 48%,#c2d7fb 48%);padding:0 .15em;border-radius:3px;font-weight:900}' +
      '.gcp-say small{display:block;margin-top:.15em;font-size:.88em;opacity:.85}' +
      'html.gcp-on .gcp-say{display:block;animation:learnIn .45s ease both}h1 .gcp-say{font-size:.5em;line-height:1.45}' +
      /* 🌐 🖥 🔐 💼（2026-10-03 ベータ） */
      '.net-say,.srv-say,.sec-say,.biz-say,.fin-say,.med-say,.nur-say{display:none;margin-top:.45em;padding:.45em .7em;border-radius:12px;font-size:.86em;line-height:1.6;font-weight:700;text-align:start}' +
      '.net-say small,.srv-say small,.sec-say small,.biz-say small,.fin-say small,.med-say small,.nur-say small{display:block;margin-top:.15em;font-size:.88em;opacity:.85}' +
      'h1 .net-say,h1 .srv-say,h1 .sec-say,h1 .biz-say,h1 .fin-say,h1 .med-say,h1 .nur-say{font-size:.5em;line-height:1.45}' +
      '.net-say{background:#e4f6f6;color:#0b5e66}.net-say b{background:linear-gradient(transparent 48%,#aee2e5 48%)}' +
      '.srv-say{background:#eef0f7;color:#36406a}.srv-say b{background:linear-gradient(transparent 48%,#cbd2ec 48%)}' +
      '.sec-say{background:#fdeeee;color:#8a1f2b}.sec-say b{background:linear-gradient(transparent 48%,#f5c4c8 48%)}' +
      '.biz-say{background:#fff3e2;color:#87480a}.biz-say b{background:linear-gradient(transparent 48%,#ffd8a1 48%)}' +
      '.fin-say{background:#eef7e2;color:#3c5a0e}.fin-say b{background:linear-gradient(transparent 48%,#cfe8a6 48%)}' +
      '.med-say{background:#e8f1ff;color:#1b4a8a}.med-say b{background:linear-gradient(transparent 48%,#bcd5fb 48%)}' +
      '.nur-say{background:#fdedf5;color:#8a1f5c}.nur-say b{background:linear-gradient(transparent 48%,#f6c3dd 48%)}' +
      '.net-say b,.srv-say b,.sec-say b,.biz-say b,.fin-say b,.med-say b,.nur-say b{padding:0 .15em;border-radius:3px;font-weight:900;color:inherit}' +
      'html.net-on .net-say,html.srv-on .srv-say,html.sec-on .sec-say,html.biz-on .biz-say,html.fin-on .fin-say,html.med-on .med-say,html.nur-on .nur-say{display:block;animation:learnIn .45s ease both}' +
                        'html[data-theme="dark"] .net-say{background:#123236;color:#bdeef0}html[data-theme="dark"] .srv-say{background:#20243a;color:#d3d9f5}' +
      'html[data-theme="dark"] .sec-say{background:#3a1a20;color:#f8d0d5}html[data-theme="dark"] .biz-say{background:#3a2a14;color:#ffe2bd}' +
      'html[data-theme="dark"] .fin-say{background:#24321a;color:#dcefc0}html[data-theme="dark"] .med-say{background:#182a44;color:#cfe0fb}html[data-theme="dark"] .nur-say{background:#3a1a2e;color:#f8d0e6}' +
      'html[data-theme="dark"] .net-say b,html[data-theme="dark"] .srv-say b,html[data-theme="dark"] .sec-say b,html[data-theme="dark"] .biz-say b{background:rgba(255,255,255,.14)}' +
      'html[data-theme="dark"] .gcp-say{background:#16233d;color:#c6dafc}html[data-theme="dark"] .gcp-say b{background:linear-gradient(transparent 48%,#274b86 48%);color:#e3edff}' +
      '.it-note{display:none;width:fit-content;margin:-6px 0 14px;padding:6px 12px;border-radius:12px;background:#eaf7f0;font-size:12px;font-weight:700;color:#1d5c41}' +
      'html.pack-on .it-note{display:block}' +
      '@keyframes learnIn{from{opacity:0;transform:translateY(-4px)}to{opacity:1;transform:none}}' +
      '.study-tip{position:absolute;left:0;top:calc(100% + 10px);z-index:55;display:flex;align-items:flex-start;gap:6px;' +
      'max-width:min(310px,calc(100vw - 32px));padding:10px 8px 10px 14px;border-radius:16px;background:#5b4bb0;color:#fff;' +
      'font-size:13px;font-weight:800;line-height:1.5;box-shadow:0 10px 24px rgba(91,75,176,.35);animation:tipIn .4s ease both;cursor:pointer}' +
      '.study-tip.it{background:#1f7a55;box-shadow:0 10px 24px rgba(31,122,85,.35)}.study-tip.it::before{background:#1f7a55}' +
      '.study-tip::before{content:"";position:absolute;left:26px;top:-7px;width:14px;height:14px;background:#5b4bb0;transform:rotate(45deg);border-radius:3px}' +
      'html[dir="rtl"] .study-tip{left:auto;right:0}html[dir="rtl"] .study-tip::before{left:auto;right:26px}' +
      '.study-tip button{flex:none;width:28px;height:28px;margin:-4px 0;border:0;border-radius:50%;background:rgba(255,255,255,.18);color:#fff;font:inherit;cursor:pointer}' +
      '.study-tip .t{transition:opacity .25s}.study-tip .t.fade{opacity:0}' +
      '.study-tip.bye{opacity:0;transition:opacity .35s}' +
      /* 📱 スマホでは、吹き出しを題名の上に重ねない（2026-10-05：iPhone で最初の3回、題名が隠れていた）。ボタンの下の1行として出す */
      '@media (max-width:640px){.study-tip{position:relative;left:auto;top:auto;flex:1 1 100%;max-width:none;margin-top:6px}}' +
      '@keyframes tipIn{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:none}}' +
      'html[data-theme="dark"] .learn-en{color:#c9bbff;border-color:#7a66d8}' +
      'html[data-theme="dark"] :is(.study-btn,.study-sel,.study-q,.study-re,.study-chip,.dim-b){background:#22242f;border-color:#33364a;color:#c9bbff}' +
      'html[data-theme="dark"] .study-chip[aria-pressed="true"]{background:#8b6de8;border-color:#8b6de8;color:#fff}' +
      'html[data-theme="dark"] .study-tray{background:rgba(255,255,255,.06);box-shadow:inset 0 0 0 2px rgba(255,255,255,.1)}' +
      'html[data-theme="dark"] .study-dim{color:#c9bbff}html[data-theme="dark"] .dim-b[aria-pressed="true"]{border-color:#b9a8ff;box-shadow:0 0 0 3px rgba(185,168,255,.3)}' +
      'html[data-theme="dark"] .study-re.on{background:var(--pb);border-color:var(--pc);color:var(--pc)}' +
      'html[data-theme="dark"] .study-re.it{--pc:#8fe0b8;--pb:#163126}html[data-theme="dark"] .study-re.gcp{--pc:#9cc2ff;--pb:#16233d}html[data-theme="dark"] .study-re.net{--pc:#8fe3e8;--pb:#123236}' +
      'html[data-theme="dark"] .study-re.srv{--pc:#b8c2f2;--pb:#20243a}html[data-theme="dark"] .study-re.sec{--pc:#f5a9b2;--pb:#3a1a20}html[data-theme="dark"] .study-re.biz{--pc:#ffc88a;--pb:#3a2a14}' +
      'html[data-theme="dark"] .study-info{background:#2a2540;color:#ddd5ff}' +
            'html[data-theme="dark"] .it-say{background:#163126;color:#bfead4}html[data-theme="dark"] .it-say b{background:linear-gradient(transparent 48%,#2a6a4c 48%);color:#d8ffe9}' +
      'html[data-theme="dark"] .it-say small{color:#8fc7ad}html[data-theme="dark"] .it-note{background:#163126;color:#bfead4}' +
      '@media (prefers-reduced-motion:reduce){html:not([data-motion="on"]) :is(.learn-en,.it-say,.study-tray,.study-tip){animation:none}html:not([data-motion="on"]) :is(.study-sw,.study-sw::after,.dim-b){transition:none}' +
      'html:not([data-motion="on"]) :is(.study-btn,.study-re,.study-q,.study-chip,.dim-b):active{transform:none}}';
    /* 🇯🇵 日本語を学ぶ人のために（2026-10-04）：ふりがな・ローマ字・読み上げ */
    st.textContent +=
      '.learn-body{display:block;min-width:0;flex:1}.learn-line{display:inline;white-space:pre-line}' +
      '.learn-en ruby{ruby-position:over}.learn-en rt{font-size:.56em;font-weight:800;line-height:1;letter-spacing:0;color:#7a5ee0}' +
      'html:not(.furi-on) .learn-en rt{display:none}' +
      'html.furi-on .learn-en[lang="ja"] .learn-line,html.furi-on .learn-en .learn-line[lang="ja"]{line-height:2.15}' +
      '.learn-rom{display:none;margin-top:.12em;font-size:.84em;font-weight:700;line-height:1.5;color:#6a5a98;white-space:normal;text-align:start}' +
      'html.rom-on .learn-rom{display:block}' +
      '.learn-say{display:none;flex:none;align-items:center;justify-content:center;width:34px;height:34px;margin:-3px 0 -3px -3px;padding:0;border:0;border-radius:50%;' +
      'background:rgba(139,109,232,.14);color:#5b4bb0;font-size:15px;line-height:1;cursor:pointer;-webkit-tap-highlight-color:transparent}' +
      '.learn-say:active{transform:scale(.9);background:rgba(139,109,232,.3)}.learn-say.on{background:#8b6de8;color:#fff}' +
      'html.learn-on.tts-on.tts-ok .learn-en:not([hidden]){display:flex;gap:6px;align-items:flex-start}' +
      'html.learn-on.tts-on.tts-ok .learn-say{display:inline-flex}' +
      '.study-tray .study-sel,.study-tray .study-chip{flex:none}' +
      'h1 .learn-say{width:28px;height:28px;font-size:13px}' +
      'html[data-theme="dark"] .learn-en rt{color:#c9bbff}html[data-theme="dark"] .learn-rom{color:#b9acf0}' +
      'html[data-theme="dark"] .learn-say{background:rgba(185,168,255,.18);color:#d9ceff}';
    document.head.appendChild(st);

    /* 文ごとに：もとの文を .learn-native で包み（薄くするため）、下に出す言語の場所を足す */
    list.forEach(function (x) {
      var el = x.el;
      if (!el.isConnected) return;
      var wrap = document.createElement('span');
      wrap.className = 'learn-native';
      while (el.firstChild) wrap.appendChild(el.firstChild);
      el.appendChild(wrap);
      var s = document.createElement('span');
      s.className = 'learn-en'; s.setAttribute('translate', 'no');
      if (!enMode) { s.setAttribute('lang', 'en'); s.setAttribute('dir', 'ltr'); paintSub(x, 'en', x.show || x.en, s); }
      x.sub = s;
      el.appendChild(s);
    });

    /* 🔊 読み上げ（ブラウザの音声合成。端末に、その言語の声があるときだけボタンを出す）*/
    var synth = window.speechSynthesis;
    var TAGS = { en: 'en-US', ja: 'ja-JP', ko: 'ko-KR', zh: 'zh-CN', 'zh-Hant': 'zh-TW', es: 'es-ES', fr: 'fr-FR', de: 'de-DE', pt: 'pt-BR', it: 'it-IT', ru: 'ru-RU',
      id: 'id-ID', vi: 'vi-VN', th: 'th-TH', hi: 'hi-IN', ar: 'ar-SA', tr: 'tr-TR', pl: 'pl-PL', nl: 'nl-NL', sv: 'sv-SE', fil: 'fil-PH', ms: 'ms-MY' };
    function voiceFor(tag) {
      var vs = synth && synth.getVoices ? synth.getVoices() : [], base = tag.split('-')[0].toLowerCase(), exact = null, any = null;
      for (var i = 0; i < vs.length; i++) {
        var vl = String(vs[i].lang || '').replace('_', '-').toLowerCase();
        if (vl === tag.toLowerCase()) exact = exact || vs[i];
        else if (vl.indexOf(base) === 0) any = any || vs[i];
      }
      return exact || any;
    }
    function speakLang() { return enMode ? (sel ? sel.value : 'ja') : 'en'; }
    function updateTts() { root.classList.toggle('tts-ok', !!(synth && voiceFor(TAGS[speakLang()] || speakLang()))); }
    var speakingBtn = null;
    function speak(text, l, btn) {
      if (!synth) return;
      try {
        synth.cancel();
        if (speakingBtn) speakingBtn.classList.remove('on');
        if (speakingBtn === btn) { speakingBtn = null; return; }
        var u = new SpeechSynthesisUtterance(text), tag = TAGS[l] || l, v = voiceFor(tag);
        u.lang = tag; if (v) u.voice = v; u.rate = l === 'ja' ? .85 : .92;
        u.onend = u.onerror = function () { if (btn) btn.classList.remove('on'); if (speakingBtn === btn) speakingBtn = null; };
        speakingBtn = btn; if (btn) btn.classList.add('on');
        synth.speak(u);
      } catch (e) {}
    }
    /* 1文ぶんの「下に出す言語」の中身：🔊 ＋ 文（ふりがな）＋ ローマ字 */
    var readData = null, readTried = false;
    function rubyHtml(s) {
      return esc(s).replace(/｜?([0-9０-９,，㐀-䶿一-鿿々〆ヶ]+)\{([^}]+)\}/g, '<ruby>$1<rt>$2</rt></ruby>');
    }
    function paintSub(x, l, text, s) {
      s = s || x.sub;
      var f = fp2(x.en);
      s.textContent = '';
      var say = document.createElement('button');
      say.type = 'button'; say.className = 'learn-say'; say.textContent = '🔊'; say.setAttribute('aria-label', W.say || 'Listen');
      say.addEventListener('click', function (e) { e.preventDefault(); e.stopPropagation(); speak(text, l, say); });
      var body = document.createElement('span'); body.className = 'learn-body';
      var line = document.createElement('span'); line.className = 'learn-line'; line.setAttribute('lang', l);
      var rb = l === 'ja' && readData && readData.r ? readData.r[f] : null;
      if (rb) line.innerHTML = rubyHtml(rb); else line.textContent = text;
      body.appendChild(line);
      var rm = l === 'ja' && readData && readData.m ? readData.m[f] : null;
      if (rm) { var r = document.createElement('span'); r.className = 'learn-rom'; r.setAttribute('lang', 'ja-Latn'); r.textContent = rm; body.appendChild(r); }
      s.appendChild(say); s.appendChild(body);
    }
    /* ふりがな・ローマ字のデータ（works/<slug>/i18n/read.ja.json。tools/furigana.py が作る）。日本語を下に出すときだけ読む */
    function loadRead(then) {
      if (readData || readTried || !window.fetch) return then && then();
      readTried = true;
      fetch(new URL('i18n/read.ja.json', location.href).toString(), { credentials: 'same-origin' })
        .then(function (r) { if (!r.ok) throw 0; return r.json(); })
        .then(function (d) { readData = d; if (then) then(); }).catch(function () {});
    }

    /* 英語で読んでいるとき：選んだ言語の訳を読み込んで、英文の下に入れる */
    var subLoaded = {};
    function fillSub(l) {
      list.forEach(function (x) { if (x.sub) { x.sub.textContent = ''; x.sub.hidden = true; } });
      function put(dict) {
        list.forEach(function (x) {
          var t = dict[fp2(x.en)];
          if (!t || !x.sub) return;
          x.sub.hidden = false;
          x.sub.setAttribute('lang', l); x.sub.setAttribute('dir', /^(ar|ur|fa|he)$/.test(l) ? 'rtl' : 'ltr');
          paintSub(x, l, plain(t));
        });
        if (l === 'ja') loadRead(function () { if (sel.value === 'ja') list.forEach(function (x) { var t = subLoaded.ja && subLoaded.ja[fp2(x.en)]; if (t && x.sub) paintSub(x, 'ja', plain(t)); }); });
      }
      if (subLoaded[l]) return put(subLoaded[l]);
      var L = LANGS[l]; if (!L) return;
      if (L.dict && Object.keys(L.dict).length) { subLoaded[l] = L.dict; return put(L.dict); }
      if (!window.fetch) return;
      var u = new URL('i18n/data.' + encodeURIComponent(l) + '.json', location.href);
      if (L.v) u.searchParams.set('v', L.v);
      fetch(u.toString(), { credentials: 'same-origin' }).then(function (r) { if (!r.ok) throw 0; return r.json(); })
        .then(function (d) { subLoaded[l] = d.dict || {}; if (sel.value === l) put(subLoaded[l]); }).catch(function () {});
    }

    var bar = document.createElement('div');
    bar.className = 'study-bar'; bar.setAttribute('translate', 'no');
    /* 🧰 2段にした（2026-10-04 本人：言い換えの選択肢が多すぎる／スマホで日本語を薄くできない）
       1段目＝いつも見える：🇬🇧 英語も見る／✨ 言い換え（6つのパックを1つのメニューに）／？
       2段目（tray）＝🇬🇧 をオンにしたときだけ：言語・ふりがな・🔊・濃さ（指で押せる4つのボタン） */
    var tray = document.createElement('div');
    tray.className = 'study-tray';
    function toggle(cls, label, key, htmlClass, onOn, opts) {
      opts = opts || {};
      var b = document.createElement('button');
      b.type = 'button';
      if (opts.chip) {
        b.className = 'study-chip' + (cls ? ' ' + cls : '');
        b.textContent = label;
      } else {
        b.className = 'study-btn' + (cls ? ' ' + cls : '');
        b.innerHTML = '<span class="study-sw" aria-hidden="true"></span><span></span><span class="study-beta" aria-hidden="true">BETA</span>';  /* 2026-10-03 本人：どちらもベータ版 */
        b.children[1].textContent = label;
      }
      var on = get(key, opts.def ? '1' : '0') === '1';
      function paint() { b.setAttribute('aria-pressed', on ? 'true' : 'false'); root.classList.toggle(htmlClass, on); if (on && onOn) onOn(); }
      b.addEventListener('click', function () { on = !on; set(key, on ? '1' : '0'); paint(); closeTip(); });
      (opts.into || bar).appendChild(b);
      b._paint = paint;
      return b;
    }
    var sel = null;
    var enBtn = toggle('', (enMode ? '🇯🇵 ' : '🇬🇧 ') + W.en, LEARN_KEY, 'learn-on', function () { if (enMode) { fillSub(sel.value); updateTts(); } });
    function subName(l) { return (FLAGS[l] || '🌏') + ' ' + (NAMES[l] || l); }
    function paintSubState() {
      if (!enMode) return;
      root.classList.toggle('sub-ja', sel.value === 'ja');
      enBtn.children[1].textContent = sel.value === 'ja' ? '🇯🇵 ' + W.en : subName(sel.value);
      updateTts();
    }

    /* ✨ 言い換え：6つのパックを、1つのメニューにまとめた。いちどに1つだけ。選んだものは pengesso-pack に覚える
       （前の pengesso-it / pengesso-gcp などが '1' のままの人は、その中のいちばん上を選んだことにする） */
    var PACK_KEY = 'pengesso-pack', pack = 'off', packLoaded = {}, rePill = null, reIc = null, reTx = null, reSel = null, note = null;
    function curPack() {
      var v = get(PACK_KEY, '');
      if (!v) {
        for (var i = 0; i < PACK_ORDER.length; i++) { if (get('pengesso-' + PACK_ORDER[i], '0') === '1') { v = PACK_ORDER[i]; break; } }
      }
      return packs.indexOf(v) >= 0 ? v : 'off';
    }
    /* どのパックも同じしくみ。ファイル名（<pack>.<lang>.json）・色・目印だけちがう。文の下には PACK_ORDER の順に並べる */
    function loadPack(kind) {
      if (packLoaded[kind] || !window.fetch) return;
      packLoaded[kind] = true;
      var order = PACK_ORDER.indexOf(kind);
      fetch(new URL(kind + '.' + encodeURIComponent(itLang) + '.json', location.href).toString(), { credentials: 'same-origin' })
        .then(function (r) { if (!r.ok) throw new Error('no ' + kind); return r.json(); })
        .then(function (data) {
          var items = data.items || {};
          list.forEach(function (x) {
            var it = items[x.en];
            if (!it || !x.el.isConnected) return;
            var s = document.createElement('span');
            s.className = 'pack-say ' + kind + '-say'; s.setAttribute('translate', 'no'); s.setAttribute('data-o', String(order));
            s.innerHTML = packIcon(kind) + ' ' + esc(it.it).replace(/\*\*(.+?)\*\*/g, '<b>$1</b>') +
              (it.term && it.mean ? '<small>📖 ' + esc(it.term) + (enMode ? ' = ' : '＝') + esc(it.mean) + '</small>' : '');
            var after = null;
            [].forEach.call(x.el.querySelectorAll(':scope > .pack-say'), function (o) { if (!after && +o.getAttribute('data-o') > order) after = o; });
            if (after) x.el.insertBefore(s, after); else x.el.appendChild(s);
          });
        })
        .catch(function () { packLoaded[kind] = false; });
    }
    function paintPack() {
      PACK_ORDER.forEach(function (k) { root.classList.toggle(k + '-on', pack === k); });
      root.classList.toggle('pack-on', pack !== 'off');
      if (!rePill) return;
      rePill.className = 'study-re' + (pack === 'off' ? '' : ' on ' + pack);
      reIc.innerHTML = pack === 'off' ? '✨' : packIcon(pack);
      reTx.textContent = pack === 'off' ? (W.re || STUDY_EN.re) : ((W.packs && W.packs[pack]) || W[pack]);
      reSel.value = pack;
      if (pack !== 'off') loadPack(pack);
    }
    function setPack(k) { pack = k; set(PACK_KEY, k); paintPack(); closeTip(); }
    if (hasIt) {
      note = document.createElement('p');
      note.className = 'it-note'; note.setAttribute('translate', 'no');
      note.textContent = W.itNote || STUDY_EN.itNote;
      /* 📚 その他の勉強（2026-10-05 本人：「メインは英語の勉強。その右に『その他の勉強』。押すとふわっとラジオボタンが出て、選ぶとその言い換えが出る」）
         前は透明な <select> を重ねていて、iPhone ではくるくる回す選び方になっていた */
      rePill = document.createElement('button');
      rePill.type = 'button'; rePill.className = 'study-re';
      rePill.setAttribute('aria-haspopup', 'dialog'); rePill.setAttribute('aria-expanded', 'false');
      rePill.innerHTML = '<span class="re-ic" aria-hidden="true"></span><span class="re-tx"></span><span class="re-caret" aria-hidden="true">▾</span>' +
        '<span class="study-beta" aria-hidden="true">BETA</span>';
      reIc = rePill.children[0]; reTx = rePill.children[1];
      var pop = document.createElement('div');
      pop.className = 'study-pop'; pop.hidden = true; pop.setAttribute('role', 'dialog'); pop.setAttribute('translate', 'no');
      pop.setAttribute('aria-label', W.re || STUDY_EN.re);
      var popHtml = '<p class="sp-t">' + esc(W.popT || STUDY_EN.popT) + '</p><p class="sp-s">' + esc(W.popS || STUDY_EN.popS) + '</p><div class="sp-list">';
      ['off'].concat(packs).forEach(function (k) {
        var label = k === 'off' ? (W.off || STUDY_EN.off) : ((W.packs && W.packs[k]) || W[k]);
        popHtml += '<label class="sp-o sp-' + k + '"><input type="radio" name="pengesso-pack" value="' + k + '"><span class="sp-ic" aria-hidden="true">' +
          (k === 'off' ? '🚫' : packIcon(k)) + '</span><span class="sp-l">' + esc(label) + '</span><span class="sp-dot" aria-hidden="true"></span></label>';
      });
      pop.innerHTML = popHtml + '</div>';
      reSel = {
        set value(v) { [].forEach.call(pop.querySelectorAll('input'), function (r) { r.checked = r.value === v; }); },
        get value() { var c = pop.querySelector('input:checked'); return c ? c.value : 'off'; }
      };
      function openPop(on) {
        if (on === !pop.hidden) return;
        rePill.setAttribute('aria-expanded', on ? 'true' : 'false');
        if (on) {
          pop.hidden = false; pop.classList.remove('in');
          var br = bar.getBoundingClientRect(), rr = rePill.getBoundingClientRect();
          pop.style.top = (rr.bottom - br.top + 8) + 'px';
          pop.style.left = Math.max(0, Math.min(rr.left - br.left, br.width - pop.offsetWidth)) + 'px';
          void pop.offsetWidth; pop.classList.add('in');
          var cur = pop.querySelector('input:checked') || pop.querySelector('input'); if (cur) cur.focus({ preventScroll: true });
        } else {
          pop.classList.remove('in');
          setTimeout(function () { if (!pop.classList.contains('in')) pop.hidden = true; }, 180);
        }
      }
      rePill.addEventListener('click', function (e) { e.stopPropagation(); openPop(pop.hidden); closeTip(); });
      pop.addEventListener('click', function (e) { e.stopPropagation(); });
      pop.addEventListener('change', function (e) {
        if (!e.target || e.target.name !== 'pengesso-pack') return;
        setPack(e.target.value);
        setTimeout(function () { openPop(false); }, 260);   // 選んだ印が見えてから閉じる
      });
      document.addEventListener('click', function () { openPop(false); });
      document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !pop.hidden) { openPop(false); rePill.focus(); } });
      bar.appendChild(rePill);
      bar.appendChild(pop);
      pack = curPack();
    }

    /* ？：なぜこの機能があるのか */
    var q = document.createElement('button');
    q.type = 'button'; q.className = 'study-q'; q.textContent = '?';
    q.setAttribute('aria-expanded', 'false'); q.setAttribute('aria-label', 'About these study modes');
    var info = document.createElement('p');
    info.className = 'study-info'; info.hidden = true; info.setAttribute('translate', 'no');
    info.textContent = W.about;
    q.addEventListener('click', function () { info.hidden = !info.hidden; q.setAttribute('aria-expanded', info.hidden ? 'false' : 'true'); closeTip(); });
    bar.appendChild(q);
    bar.appendChild(tray);

    /* ── 2段目（🇬🇧 をオンにしたときだけ出る）── */
    if (enMode) {
      sel = document.createElement('select');
      sel.className = 'study-sel'; sel.setAttribute('aria-label', 'Language to show under English');
      var pref = ['ja', 'ko', 'zh', 'zh-Hant', 'es', 'fr', 'de', 'pt', 'id', 'vi', 'th', 'fil'];
      var opts = pref.filter(function (l) { return LANGS[l]; }).concat(Object.keys(LANGS).filter(function (l) { return pref.indexOf(l) < 0; }));
      opts.forEach(function (l) { var o = document.createElement('option'); o.value = l; o.textContent = (FLAGS[l] || '') + ' ' + (NAMES[l] || l); sel.appendChild(o); });
      var want = get(SUB_KEY, 'ja'); sel.value = LANGS[want] ? want : 'ja';
      sel.addEventListener('change', function () {
        set(SUB_KEY, sel.value);
        paintSubState();
        if (!root.classList.contains('learn-on')) enBtn.click(); else fillSub(sel.value);
      });
      tray.appendChild(sel);
      sel.setAttribute('aria-label', W.other || 'Other language');
    }
    /* ふりがな・ローマ字（日本語を下に出しているときだけ）と、🔊 聞く（その言語の声がある端末だけ） */
    var furiBtn = null, romBtn = null;
    if (enMode) {
      furiBtn = toggle('ja-only', 'あ ' + W.furi, 'pengesso-furi', 'furi-on', null, { chip: true, def: true, into: tray });
      romBtn = toggle('ja-only', 'Aa ' + W.rom, 'pengesso-rom', 'rom-on', null, { chip: true, into: tray });
    }
    var sayBtn = toggle('say-btn', '🔊 ' + (W.say || 'Listen'), 'pengesso-say', 'tts-on', null, { chip: true, def: true, into: tray });
    if (synth) { updateTts(); if (synth.addEventListener) synth.addEventListener('voiceschanged', updateTts); else synth.onvoiceschanged = updateTts; }

    /* 🎚 濃さ：指で押せる大きな4つのボタン（100・60・30・10％）。前のスライダーで決めた値は、いちばん近い段にする */
    var STEPS = [100, 60, 30, 10], SHOWN = { 100: 1, 60: .7, 30: .45, 10: .25 };
    var GLYPH = { ja: 'あ', ko: '가', zh: '字', 'zh-Hant': '字', ar: 'ع', ur: 'ع', fa: 'ع', hi: 'अ', bn: 'অ', ru: 'Я' };
    var dim = document.createElement('div'), dimBtns = [];
    dim.className = 'study-dim'; dim.setAttribute('role', 'group'); dim.setAttribute('aria-label', W.dim);
    var dl = document.createElement('span');
    dl.className = 'dim-l'; dl.textContent = W.dim; dim.appendChild(dl);
    function setDim(v, save) {
      root.style.setProperty('--native-a', String(v / 100));
      if (save) set(NATIVE_KEY, String(v));
      dimBtns.forEach(function (b) { b.setAttribute('aria-pressed', +b.getAttribute('data-v') === v ? 'true' : 'false'); });
    }
    STEPS.forEach(function (v) {
      var b = document.createElement('button'), g = document.createElement('i');
      b.type = 'button'; b.className = 'dim-b'; b.setAttribute('data-v', String(v)); b.setAttribute('aria-label', W.dim + ' ' + v + '%');
      g.textContent = enMode ? 'A' : (GLYPH[lang] || 'Aa'); g.style.opacity = String(SHOWN[v]);
      b.appendChild(g);
      b.addEventListener('click', function () { setDim(v, true); });
      dim.appendChild(b); dimBtns.push(b);
    });
    var saved = +get(NATIVE_KEY, '100') || 100, near = 100;
    STEPS.forEach(function (v) { if (Math.abs(v - saved) < Math.abs(near - saved)) near = v; });
    setDim(near, false);
    tray.appendChild(dim);

    var row = switchMount && switchMount.classList.contains('i18n-row') ? switchMount : null;
    if (row) row.parentNode.insertBefore(bar, row.nextSibling);
    else { var h1 = document.querySelector('main h1'); if (!h1) return; h1.parentNode.insertBefore(bar, h1); }
    bar.parentNode.insertBefore(info, bar.nextSibling);
    if (note) info.parentNode.insertBefore(note, info.nextSibling);
    enBtn._paint(); paintPack();
    [furiBtn, romBtn, sayBtn].forEach(function (b) { if (b) b._paint(); });
    paintSubState();
    if (enMode && root.classList.contains('learn-on')) fillSub(sel.value);

    /* 💬 吹き出し：まだ一度もさわっていない人に、最初の3回だけ。言葉は数秒ごとに入れかわる */
    var tip = null, iv = null;
    function closeTip() {
      if (!tip) return;
      var t = tip; tip = null; clearInterval(iv); set(STUDY_TIP_KEY, '9');
      t.classList.add('bye'); setTimeout(function () { t.remove(); }, 380);
    }
    var lines = (W.tips || []).slice(0, hasIt && packLangs.it && packLangs.it.indexOf(itLang) >= 0 ? 2 : 1);
    var shown = +get(STUDY_TIP_KEY, '0') || 0;
    if (lines.length && get(LEARN_KEY, null) === null && get(IT_KEY, null) === null && get(PACK_KEY, null) === null && shown < 3) {
      set(STUDY_TIP_KEY, String(shown + 1));
      var old = row && row.querySelector('.i18n-tip');   /* 言語の吹き出しと2つ同時に出さない */
      if (old) old.remove();
      tip = document.createElement('div');
      tip.className = 'study-tip'; tip.setAttribute('role', 'status');
      tip.innerHTML = '<span class="t"></span><button type="button" aria-label="×">×</button>';
      var tx = tip.firstChild, n = 0;
      tx.textContent = lines[0];
      tip.addEventListener('click', function (e) {
        if (e.target.tagName !== 'BUTTON') {
          if (n === 1 && rePill && packs.indexOf('it') >= 0) setPack('it'); else enBtn.click();
        }
        closeTip();
      });
      bar.appendChild(tip);
      var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
      if (lines.length > 1 && !reduce) iv = setInterval(function () {
        if (!tip) return clearInterval(iv);
        tx.classList.add('fade');
        setTimeout(function () { if (!tip) return; n = (n + 1) % lines.length; tx.textContent = lines[n]; tip.classList.toggle('it', n === 1); tx.classList.remove('fade'); }, 250);
      }, 4500);
      setTimeout(function () { if (tip) { var t = tip; tip = null; clearInterval(iv); t.classList.add('bye'); setTimeout(function () { t.remove(); }, 380); } }, 14000);
    }
  }

  /* 😊 気分のおすすめ（2026-10-03 本人の要望）
     トップで「ちょっと元気がほしい」などの気分を選んで記事に入った人には、記事のいちばん下の
     「こちらもどうぞ」（関連4本＋ちがう話1本）のあとに、同じ気分の記事をあと2本出す＝ぜんぶで7本。
     気分はタブを閉じるまで覚えておく（sessionStorage）。トップで気分を外したら消える。
     一覧は assets/moods.json（tools/build-site.py が作る）。題の訳はトップの訳（top-data）から引く */
  var MOOD_E = { lift: '🌧', laugh: '😂', travel: '✈️', think: '🤔', learn: '📚', energy: '⚡' };
  var MOOD_EN = { lift: 'Need a little lift', laugh: 'Want a laugh', travel: 'Want to go somewhere',
    think: 'Want to think a bit', learn: 'Want to learn something', energy: 'Full of energy' };
  var MOOD_HEAD = {
    en: ['For your mood: “{m}”', '2 more', 'Same mood', 'Change mood'],
    ja: ['いまの気分「{m}」の人に', 'あと2本', '同じ気分', '気分を変える'],
    ko: ['지금 기분 “{m}”인 분께', '2개 더', '같은 기분', '기분 바꾸기'],
    zh: ['给现在“{m}”的你', '再来2篇', '同样的心情', '换个心情'],
    'zh-Hant': ['給現在「{m}」的你', '再來2篇', '同樣的心情', '換個心情']
  };
  function ss(k, v) { try { if (v === undefined) return sessionStorage.getItem(k); if (v === null) sessionStorage.removeItem(k); else sessionStorage.setItem(k, v); } catch (e) { return null; } }
  window.pengessoEntryMood = function (k) { ss('pengesso-entry-mood', k || null); };
  function moodMore() {
    var rel = document.querySelector('section.related');
    var m = /\/(?:works|draft)\/([^\/]+)\//.exec(location.pathname);
    if (!m) return;
    var me = decodeURIComponent(m[1]);
    var read = []; try { read = JSON.parse(ss('pengesso-read') || '[]'); } catch (e) {}
    if (read.indexOf(me) < 0) { read.push(me); ss('pengesso-read', JSON.stringify(read.slice(-80))); }
    var mood = ss('pengesso-entry-mood');
    if (!rel || !mood || !MOOD_E[mood] || !window.fetch) return;
    var shown = {}; shown[me] = 1;
    [].forEach.call(document.querySelectorAll('a.next, a.prev, a.rel-card'), function (a) {
      var x = /\.\.\/([^\/]+)\/index\.html/.exec(a.getAttribute('href') || ''); if (x) shown[x[1]] = 1;
    });
    var T = MOOD_HEAD[lang] || MOOD_HEAD.en;
    var top = (lang === 'en') ? Promise.resolve({}) :
      fetch('/i18n/top-data.' + encodeURIComponent(lang) + '.json').then(function (r) { return r.ok ? r.json() : {}; }).then(function (d) { return d.dict || {}; }, function () { return {}; });
    Promise.all([fetch('/assets/moods.json').then(function (r) { return r.json(); }), top]).then(function (res) {
      var rows = res[0], dict = res[1];
      function tr(en) { var k = fp2(en); return Object.prototype.hasOwnProperty.call(dict, k) ? dict[k] : en; }
      var pool = rows.filter(function (r) { return r[3].indexOf(mood) >= 0 && !shown[r[0]]; });
      var fresh = pool.filter(function (r) { return read.indexOf(r[0]) < 0; });
      if (fresh.length >= 2) pool = fresh;
      var seed = 0; for (var i = 0; i < me.length; i++) seed = (seed * 31 + me.charCodeAt(i)) >>> 0;
      var picks = [];
      while (pool.length && picks.length < 2) { seed = (seed * 1103515245 + 12345) >>> 0; picks.push(pool.splice(seed % pool.length, 1)[0]); }
      if (!picks.length) return;
      var e = MOOD_E[mood], name = tr(MOOD_EN[mood]);
      var sec = document.createElement('section');
      sec.className = 'related mood-more'; sec.setAttribute('translate', 'no');
      sec.innerHTML = '<h2 class="related-h">' + e + ' ' + esc(T[0].replace('{m}', name)) + ' <span class="mm-n">' + esc(T[1]) + '</span></h2>' +
        '<ul class="related-list">' + picks.map(function (r) {
          return '<li><a class="rel-card mm-card" href="../' + encodeURIComponent(r[0]) + '/index.html">' +
            '<span class="rel-thumb" aria-hidden="true" style="background-image:url(\'../../assets/thumbs/' + encodeURIComponent(r[0]) + '.jpg\')"></span>' +
            '<div class="rel-body"><div class="rel-kicker"><span class="rel-sec">⚡ ' + r[2] + ' SEC</span><span class="rel-chip mm-chip">' + e + ' ' + esc(T[2]) + '</span></div>' +
            '<div class="rel-title">' + esc(tr(r[1])) + '</div></div><span class="rel-go" aria-hidden="true">→</span></a></li>';
        }).join('') + '</ul>' +
        '<a class="mm-change" href="../../index.html#mood">' + esc(T[3]) + ' →</a>';
      var st = document.createElement('style');
      st.textContent = '.mood-more{margin-top:22px;padding:14px;border-radius:24px;background:linear-gradient(135deg,#fff4d6,#ffe3ee)}' +
        '.mood-more .mm-n{display:inline-block;margin-left:4px;padding:2px 9px;border-radius:999px;background:#ff8a3d;color:#fff;font-size:12px;vertical-align:2px}' +
        '.mood-more .mm-chip{background:#ff8a3d}' +
        '.mm-change{display:inline-block;margin-top:10px;font-size:13px;font-weight:900;color:#b4521a;text-decoration:none}' +
        '.mm-change:hover{text-decoration:underline}' +
        'html[data-theme="dark"] .mood-more{background:linear-gradient(135deg,#3a2f1c,#3a2030)}html[data-theme="dark"] .mm-change{color:#ffb37a}';
      document.head.appendChild(st);
      rel.parentNode.insertBefore(sec, rel.nextSibling);
    }).catch(function () {});
  }

  /* 🗺 次はどこへ？（2026-10-08 本人：「それぞれの記事を読み終えるごとに、地図を表示して、好きな記事に飛べるように」）
     記事のいちばん下（「一覧に戻る」の上）に、アジアの点の地図。国を押すと、その国の記事が並ぶ。日本は街でもしぼれる。
     データは assets/jump.json（build-site.py が作る）と assets/worldmap-dots.json。題の訳はトップの訳（i18n/top-data.<lang>.json）。
     下に近づいたときだけ読む（ページを重くしない） */
  var JM_WORDS = {
    en: ['🗺 Where to next?', 'Tap a country, then pick a post.', 'posts', 'Show all', '🎲 Surprise me', 'Somewhere else'],
    ja: ['🗺 次はどこへ行く？', '国をタップして、読みたい記事を選んでください。', '本', 'ぜんぶ見る', '🎲 どこかへ連れていって', 'そのほか'],
    ko: ['🗺 다음은 어디로 갈까요?', '나라를 누르고, 읽고 싶은 글을 고르세요.', '개', '전부 보기', '🎲 아무 데나 데려가 줘', '그 밖에'],
    zh: ['🗺 下一站去哪里？', '点一个国家，再选一篇文章。', '篇', '全部显示', '🎲 随便带我去', '其他'],
    'zh-Hant': ['🗺 下一站去哪裡？', '點一個國家，再選一篇文章。', '篇', '全部顯示', '🎲 隨便帶我去', '其他'],
    hi: ['🗺 अब कहाँ चलें?', 'किसी देश पर टैप करें, फिर एक पोस्ट चुनें।', 'पोस्ट', 'सब दिखाएँ', '🎲 कहीं भी ले चलो', 'और'],
    es: ['🗺 ¿Adónde vamos ahora?', 'Toca un país y elige una entrada.', 'entradas', 'Ver todo', '🎲 Sorpréndeme', 'Otros'],
    ar: ['🗺 إلى أين بعد ذلك؟', 'اضغط على بلد، ثم اختر مقالة.', 'مقالات', 'عرض الكل', '🎲 فاجئني', 'أخرى'],
    fr: ['🗺 On va où maintenant ?', 'Touche un pays, puis choisis un article.', 'articles', 'Tout voir', '🎲 Surprends-moi', 'Autres'],
    bn: ['🗺 এরপর কোথায় যাবেন?', 'একটি দেশে ট্যাপ করুন, তারপর একটি লেখা বেছে নিন।', 'টি লেখা', 'সব দেখুন', '🎲 যেকোনো জায়গায় নিয়ে চলো', 'অন্যান্য'],
    pt: ['🗺 Para onde agora?', 'Toque em um país e escolha um post.', 'posts', 'Ver tudo', '🎲 Me surpreenda', 'Outros'],
    ru: ['🗺 Куда дальше?', 'Нажмите на страну и выберите запись.', 'записей', 'Показать все', '🎲 Удиви меня', 'Другое'],
    id: ['🗺 Ke mana selanjutnya?', 'Ketuk sebuah negara, lalu pilih tulisan.', 'tulisan', 'Lihat semua', '🎲 Kejutkan aku', 'Lainnya'],
    ur: ['🗺 اب کہاں چلیں؟', 'کسی ملک پر ٹیپ کریں، پھر ایک تحریر چنیں۔', 'تحریریں', 'سب دیکھیں', '🎲 کہیں بھی لے چلو', 'دیگر']
  };
  var JM_CC = { nagoya: 'JP', tokyo: 'JP', gifu: 'JP', mie: 'JP', osaka: 'JP', shiga: 'JP', seoul: 'KR', cebu: 'PH', baguio: 'PH', clark: 'PH', kl: 'MY', bangkok: 'TH', thailand: 'TH' };
  var JM_PLACE = { nagoya: 'Nagoya 🏯', tokyo: 'Tokyo 🗼', gifu: 'Gifu 🌿', mie: 'Mie 🏎️', osaka: 'Osaka 🏯', shiga: 'Shiga 🌊', seoul: 'Seoul 🇰🇷',
    cebu: 'Cebu 🌴', baguio: 'Baguio ⛰️', clark: 'Clark 🏫', kl: 'Kuala Lumpur 🇲🇾', bangkok: 'Bangkok 🛺', thailand: 'Kanchanaburi 🚂' };
  var JM_FLAG = { JP: '🇯🇵', KR: '🇰🇷', PH: '🇵🇭', MY: '🇲🇾', TH: '🇹🇭' };
  var JM_EN = { JP: 'Japan', KR: 'Korea', PH: 'Philippines', MY: 'Malaysia', TH: 'Thailand' };
  function jumpMap() {
    var m = /\/(works|lab)\/([^\/]+)\//.exec(location.pathname);
    if (!m || !window.fetch || document.querySelector('.jm')) return;
    var me = decodeURIComponent(m[2]);
    var anchor = document.querySelector('a.to-list') || document.querySelector('.lab-nav') || document.querySelector('a.next');
    if (!anchor) return;
    var box = document.createElement('section');
    box.className = 'jm'; box.setAttribute('translate', 'no');
    anchor.parentNode.insertBefore(box, anchor);
    var W = JM_WORDS[lang] || JM_WORDS.en;
    var go = function () {
      var top = (lang === 'en') ? Promise.resolve({}) :
        fetch('/i18n/top-data.' + encodeURIComponent(lang) + '.json').then(function (r) { return r.ok ? r.json() : {}; }).then(function (d) { return d.dict || {}; }, function () { return {}; });
      Promise.all([fetch('/assets/jump.json').then(function (r) { return r.json(); }),
                   fetch('/assets/worldmap-dots.json').then(function (r) { return r.json(); }), top]).then(function (res) {
        drawJump(box, me, res[0], res[1], res[2], W);
      }).catch(function () { box.remove(); });
    };
    if (!('IntersectionObserver' in window)) { go(); return; }
    var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { io.disconnect(); go(); } }, { rootMargin: '900px 0px' });
    io.observe(box);
  }
  function drawJump(box, me, rows, dots, dict, W) {
    function tr(en) { var k = fp2(en); return Object.prototype.hasOwnProperty.call(dict, k) ? dict[k] : en; }
    var regionName = null;
    try { regionName = new Intl.DisplayNames([lang === 'zh-Hant' ? 'zh-Hant' : lang], { type: 'region' }); } catch (e) {}
    function cname(cc) { try { return regionName ? regionName.of(cc) : JM_EN[cc]; } catch (e) { return JM_EN[cc]; } }
    var read = []; try { read = JSON.parse(ss('pengesso-read') || '[]'); } catch (e) {}
    var posts = rows.filter(function (r) { return r[0] !== me; });
    var mine = rows.filter(function (r) { return r[0] === me; })[0];
    var by = {}, other = [];
    posts.forEach(function (r) { var cc = JM_CC[r[3]]; if (cc) (by[cc] = by[cc] || []).push(r); else other.push(r); });
    var ccs = Object.keys(JM_FLAG).filter(function (c) { return by[c]; });
    // 地図の切り抜き：記事のある国の点が入る四角 ＋ 少し余白
    var pts = {}, x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
    for (var i = 0; i < dots.p.length; i += 3) {
      var a2 = dots.cc[dots.p[i + 2]], x = dots.p[i] / 10, y = dots.p[i + 1] / 10;
      (pts[a2] = pts[a2] || []).push([x, y]);
      if (JM_FLAG[a2] && by[a2]) { if (x < x0) x0 = x; if (x > x1) x1 = x; if (y < y0) y0 = y; if (y > y1) y1 = y; }
    }
    if (x0 > x1) { box.remove(); return; }
    var pad = 14; x0 -= pad; y0 -= pad; x1 += pad; y1 += pad;
    var vw = x1 - x0, vh = y1 - y0;
    var svg = '<svg class="jm-svg" viewBox="' + x0 + ' ' + y0 + ' ' + vw + ' ' + vh + '" aria-hidden="true">';
    var center = {};
    Object.keys(pts).forEach(function (a2) {
      var ps = pts[a2].filter(function (q) { return q[0] >= x0 && q[0] <= x1 && q[1] >= y0 && q[1] <= y1; });
      if (!ps.length) return;
      var on = JM_FLAG[a2] && by[a2];
      svg += '<g class="jm-c' + (on ? ' on' : '') + '" data-cc="' + a2 + '">' + ps.map(function (q) {
        return '<circle cx="' + q[0] + '" cy="' + q[1] + '" r="' + dots.r + '"/>'; }).join('') + '</g>';
      if (on) { var sx = 0, sy = 0; pts[a2].forEach(function (q) { sx += q[0]; sy += q[1]; }); center[a2] = [sx / pts[a2].length, sy / pts[a2].length]; }
    });
    svg += '</svg>';
    var pins = ccs.map(function (cc, k) {
      var c = center[cc]; if (!c) return '';
      return '<button type="button" class="jm-pin" data-cc="' + cc + '" style="left:' + ((c[0] - x0) / vw * 100).toFixed(1) + '%;top:' + ((c[1] - y0) / vh * 100).toFixed(1) + '%;animation-delay:' + (k * .08) + 's" aria-label="' + esc(cname(cc)) + '">' +
        '<span class="jm-flag">' + JM_FLAG[cc] + '</span><b>' + by[cc].length + '</b></button>';
    }).join('');
    box.innerHTML = '<h2 class="jm-h">' + esc(W[0]) + '</h2><p class="jm-sub">' + esc(W[1]) + '</p>' +
      '<div class="jm-map">' + svg + pins + '</div>' +
      '<div class="jm-tabs"></div><div class="jm-chips"></div><ul class="jm-list"></ul>' +
      '<div class="jm-foot"><button type="button" class="jm-more" hidden>' + esc(W[3]) + '</button>' +
      '<button type="button" class="jm-rand">' + esc(W[4]) + '</button></div>';
    var tabs = box.querySelector('.jm-tabs'), chips = box.querySelector('.jm-chips'), list = box.querySelector('.jm-list'), more = box.querySelector('.jm-more');
    var state = { cc: null, place: null, all: false };
    function card(r) {
      var unread = read.indexOf(r[0]) < 0;
      return '<li><a class="jm-card" href="/works/' + encodeURIComponent(r[0]) + '/index.html">' +
        '<span class="jm-th" style="background-image:url(\'/assets/thumbs/' + encodeURIComponent(r[0]) + '.jpg\')"></span>' +
        '<span class="jm-tx"><span class="jm-t">' + esc(tr(r[1])) + '</span><span class="jm-s">⚡ ' + r[2] + ' SEC' + (unread ? ' · 🆕' : '') + '</span></span>' +
        '<span class="jm-go" aria-hidden="true">→</span></a></li>';
    }
    function paint() {
      [].forEach.call(box.querySelectorAll('.jm-pin'), function (b) { b.setAttribute('aria-pressed', b.dataset.cc === state.cc ? 'true' : 'false'); });
      [].forEach.call(box.querySelectorAll('.jm-c'), function (g) { g.classList.toggle('sel', g.dataset.cc === state.cc); });
      tabs.innerHTML = ccs.map(function (cc) {
        return '<button type="button" class="jm-tab" data-cc="' + cc + '" aria-pressed="' + (cc === state.cc) + '">' + JM_FLAG[cc] + ' ' + esc(cname(cc)) + '</button>';
      }).join('') + (other.length ? '<button type="button" class="jm-tab" data-cc="__" aria-pressed="' + (state.cc === '__') + '">✨ ' + esc(W[5]) + '</button>' : '');
      var pool = state.cc === '__' ? other : (by[state.cc] || []);
      var places = {};
      pool.forEach(function (r) { places[r[3]] = (places[r[3]] || 0) + 1; });
      var pk = Object.keys(places);
      chips.innerHTML = (state.cc !== '__' && pk.length > 1) ? pk.sort(function (a, b) { return places[b] - places[a]; }).map(function (p) {
        return '<button type="button" class="jm-chip" data-p="' + p + '" aria-pressed="' + (p === state.place) + '">' + esc(tr(JM_PLACE[p] || p)) + ' <small>' + places[p] + '</small></button>';
      }).join('') : '';
      if (state.place) pool = pool.filter(function (r) { return r[3] === state.place; });
      pool = pool.slice().sort(function (a, b) { return (read.indexOf(a[0]) >= 0) - (read.indexOf(b[0]) >= 0); });
      var show = state.all ? pool : pool.slice(0, 5);
      list.innerHTML = show.map(card).join('');
      more.hidden = state.all || pool.length <= 5;
      more.textContent = W[3] + ' (' + pool.length + ' ' + W[2] + ')';
      list.classList.remove('in'); void list.offsetWidth; list.classList.add('in');
    }
    function pick(cc) { state.cc = cc; state.place = null; state.all = false; paint(); }
    box.addEventListener('click', function (e) {
      var t = e.target.closest && e.target.closest('button'); if (!t) return;
      if (t.classList.contains('jm-pin') || t.classList.contains('jm-tab')) {
        pick(t.dataset.cc);
        if (window.pengessoPop && t.classList.contains('jm-pin')) { var r = t.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top, [JM_FLAG[t.dataset.cc] || '✨', '✨'], 8); }
      } else if (t.classList.contains('jm-chip')) { state.place = state.place === t.dataset.p ? null : t.dataset.p; state.all = false; paint(); }
      else if (t.classList.contains('jm-more')) { state.all = true; paint(); }
      else if (t.classList.contains('jm-rand')) {
        var fresh = posts.filter(function (r) { return read.indexOf(r[0]) < 0; });
        var pool = fresh.length ? fresh : posts;
        var r = pool[Math.floor(Math.random() * pool.length)];
        if (r) location.href = '/works/' + encodeURIComponent(r[0]) + '/index.html';
      }
    });
    var start = mine && JM_CC[mine[3]] && by[JM_CC[mine[3]]] ? JM_CC[mine[3]] : (ccs[0] || '__');
    pick(start);
    var st = document.createElement('style');
    st.textContent =
      '.jm{margin:26px 0 18px;padding:18px 14px 16px;border-radius:26px;background:linear-gradient(160deg,#eef4ff,#fff6ea);border:2px solid rgba(47,86,201,.12);color:#232c48}' +
      '.jm-h{margin:0 0 4px;font-size:21px;font-weight:900;line-height:1.3}' +
      '.jm-sub{margin:0 0 10px;font-size:13.5px;font-weight:800;color:#5d6685;line-height:1.6}' +
      '.jm-map{position:relative;margin:0 -4px;border-radius:20px;background:#dfe9ff;overflow:hidden}' +
      '.jm-svg{display:block;width:100%;height:auto}' +
      '.jm-c circle{fill:#c4cde6;transition:fill .3s}.jm-c.on circle{fill:#8ea6ea}.jm-c.sel circle{fill:#2f56c9}' +
      '.jm-pin{position:absolute;transform:translate(-50%,-50%);display:inline-flex;align-items:center;gap:4px;min-height:40px;min-width:40px;padding:4px 10px 4px 7px;' +
      'border:2px solid #fff;border-radius:999px;background:#fff;color:#232c48;font:inherit;font-size:13px;font-weight:900;cursor:pointer;' +
      'box-shadow:0 6px 16px rgba(35,44,72,.22);animation:jmPop .5s cubic-bezier(.2,1.6,.4,1) both;-webkit-tap-highlight-color:transparent}' +
      '.jm-pin .jm-flag{font-size:19px;line-height:1}' +
      '.jm-pin[aria-pressed="true"]{background:#2f56c9;color:#fff;border-color:#2f56c9;z-index:2}' +
      '.jm-pin[aria-pressed="true"]::after{content:"";position:absolute;inset:-6px;border-radius:999px;border:3px solid rgba(47,86,201,.45);animation:jmRing 1.6s ease-out infinite}' +
      '@keyframes jmPop{from{opacity:0;transform:translate(-50%,-30%) scale(.5)}to{opacity:1;transform:translate(-50%,-50%) scale(1)}}' +
      '@keyframes jmRing{from{opacity:1;transform:scale(.9)}to{opacity:0;transform:scale(1.35)}}' +
      '.jm-tabs,.jm-chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}' +
      '.jm-tab,.jm-chip{min-height:40px;padding:6px 13px;border-radius:999px;border:2px solid rgba(35,44,72,.12);background:#fff;color:#232c48;font:inherit;font-size:13px;font-weight:900;cursor:pointer}' +
      '.jm-tab[aria-pressed="true"]{background:#232c48;color:#fff;border-color:#232c48}' +
      '.jm-chip small{opacity:.6;font-size:11px}.jm-chip[aria-pressed="true"]{background:#ffc42e;border-color:#ffc42e}' +
      '.jm-list{list-style:none;margin:12px 0 0;padding:0;display:grid;gap:8px}' +
      '.jm-list.in li{animation:jmIn .4s ease both}' +
      '.jm-list.in li:nth-child(2){animation-delay:.05s}.jm-list.in li:nth-child(3){animation-delay:.1s}.jm-list.in li:nth-child(4){animation-delay:.15s}.jm-list.in li:nth-child(5){animation-delay:.2s}' +
      '@keyframes jmIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}' +
      '.jm-card{display:flex;align-items:center;gap:12px;padding:9px 12px 9px 9px;border-radius:18px;background:#fff;color:inherit;text-decoration:none;border:1.5px solid rgba(35,44,72,.08)}' +
      '.jm-th{flex:none;width:56px;height:56px;border-radius:14px;background:#e6ebf7 center/cover no-repeat}' +
      '.jm-tx{flex:1;min-width:0;display:flex;flex-direction:column;gap:3px}' +
      '.jm-t{font-size:14.5px;font-weight:900;line-height:1.45}' +
      '.jm-s{font-size:11.5px;font-weight:800;color:#6d7593}' +
      '.jm-go{flex:none;font-weight:900;color:#2f56c9}' +
      '.jm-foot{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}' +
      '.jm-more,.jm-rand{flex:1 1 140px;min-height:48px;border-radius:16px;border:0;font:inherit;font-size:14px;font-weight:900;cursor:pointer}' +
      '.jm-more{background:#fff;color:#2f56c9;border:2px solid rgba(47,86,201,.25)}.jm-more[hidden]{display:none}' +
      '.jm-rand{background:linear-gradient(135deg,#ff8a3d,#ff6b8b);color:#fff;box-shadow:0 8px 18px rgba(255,107,139,.3)}' +
      'html[data-theme="dark"] .jm{background:linear-gradient(160deg,#1f2433,#2a2420);color:#f4f0fa;border-color:rgba(255,255,255,.1)}' +
      'html[data-theme="dark"] .jm-sub,html[data-theme="dark"] .jm-s{color:#b8b4c8}' +
      'html[data-theme="dark"] .jm-map{background:#1a2033}html[data-theme="dark"] .jm-c circle{fill:#3a4160}html[data-theme="dark"] .jm-c.on circle{fill:#5b6fae}html[data-theme="dark"] .jm-c.sel circle{fill:#8ea6ff}' +
      'html[data-theme="dark"] .jm-pin,html[data-theme="dark"] .jm-tab,html[data-theme="dark"] .jm-chip,html[data-theme="dark"] .jm-card,html[data-theme="dark"] .jm-more{background:#22242f;color:#f4f0fa;border-color:rgba(255,255,255,.14)}' +
      'html[data-theme="dark"] .jm-tab[aria-pressed="true"],html[data-theme="dark"] .jm-pin[aria-pressed="true"]{background:#8ea6ff;color:#14182a}' +
      '@media (prefers-reduced-motion: reduce){html:not([data-motion="on"]) .jm-pin,html:not([data-motion="on"]) .jm-list.in li{animation:none}html:not([data-motion="on"]) .jm-pin::after{display:none}}' +
      'html[data-motion="off"] .jm-pin,html[data-motion="off"] .jm-list.in li{animation:none}html[data-motion="off"] .jm-pin::after{display:none}';
    document.head.appendChild(st);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();

  function start() {
  UI_READY.then(startReady, startReady);
  }

  /* 🛠 診断（?debug=1 を付けて開いたときだけ）：スマホで「動かない」ときに、画面の写真を送ってもらえば原因が分かるように（2026-10-04）
     本人の端末（iPhone）は、こちらでは試せない。端末の設定・動きの設定・薄くする指定が、いま何になっているかを画面の左下に出す */
  function drawDebug() {
    if (!/[?&]debug=1\b/.test(location.search)) return;
    var box = document.createElement('div');
    box.setAttribute('translate', 'no');
    box.style.cssText = 'position:fixed;left:6px;bottom:6px;z-index:2147483600;max-width:calc(100vw - 12px);padding:8px 10px;border-radius:10px;' +
      'background:rgba(0,0,0,.85);color:#9ff0b5;font:11px/1.45 ui-monospace,Menlo,monospace;white-space:pre-wrap;word-break:break-all;pointer-events:none';
    document.body.appendChild(box);
    function ua() { var u = navigator.userAgent; return (/iPhone|iPad/.test(u) ? 'iOS' : /Android/.test(u) ? 'Android' : 'PC') + ' ' + (/CriOS/.test(u) ? 'Chrome' : /FxiOS/.test(u) ? 'Firefox' : /Edg/.test(u) ? 'Edge' : /Chrome/.test(u) ? 'Chrome' : /Safari/.test(u) ? 'Safari' : '?'); }
    function tick() {
      var r = document.documentElement, ln = document.querySelector('.learn-native'), os = '?';
      try { os = (window.pengessoMotion ? pengessoMotion.os() : false) ? 'YES(減らす設定)' : 'no'; } catch (e) {}
      var op = ln ? getComputedStyle(ln).opacity : '(なし)';
      box.textContent = '🛠 診断 ?debug=1\n' + ua() + ' / ' + innerWidth + 'x' + innerHeight + ' @' + (window.devicePixelRatio || 1) +
        '\n言語 ' + lang + ' / html lang=' + (r.getAttribute('lang') || '-') +
        '\n端末の「動きを減らす」: ' + os + ' / 動きの設定: ' + (r.getAttribute('data-motion') || 'auto') +
        '\nhtml.class: ' + r.className.replace(/\s+/g, ' ') +
        '\n--native-a: ' + (r.style.getPropertyValue('--native-a') || '(未設定)') +
        '\n.learn-native: ' + document.querySelectorAll('.learn-native').length + '個 / 先頭の opacity=' + op +
        '\n.learn-en: ' + document.querySelectorAll('.learn-en').length + '個';
    }
    tick(); setInterval(tick, 600);
  }
  /* ✂️ 日本語の見出しを文節で折り返す（2026-10-04）。Google の BudouX（assets/ja-phrase.js）で文節の境目を探し、<wbr> を入れる。
     Chrome にも CSS の auto-phrase はあるが、iPhone の Safari・Firefox にはない。端末で折り返しが変わらないよう、日本語のときは全部の端末で同じこれを使う。
     （「曲の｜カード」と割れるのが、BudouX だと「曲のカード、」のまま折れる）?phrase=0 を付けると読まない（比べるとき用） */
  function loadPhrase() {
    if (lang !== 'ja' || /[?&]phrase=0\b/.test(location.search)) return;
    var s = document.createElement('script');
    s.src = '/assets/ja-phrase.js'; s.async = true;
    (document.head || document.documentElement).appendChild(s);
  }
  function startReady() {
  try { loadPhrase(); } catch (e) {}
  try { drawDebug(); } catch (e) {}
  drawSwitch();
  try { drawMotionNote(); } catch (e) {}
  try { moodMore(); } catch (e) {}
  try { jumpMap(); } catch (e) {}
  window.pengessoLang = lang;   /* トップの「読みながら勉強」が、いまの言語を知るため */
  if (lang === 'en') { if (!DATA.lazyTop) drawLearn(collectEnglish(), true); return; }
  drawNotice(lang, LANGS[lang] || {});

  if (DATA.lazyTop) {
    if (!LANGS[lang] || !window.fetch) return;
    /* 訳を直したら URL の v も変わる＝古い訳を読まない */
    (EARLY || getJson(langUrl('top-data')))
      .then(function (topData) { translate(topData); })
      .catch(function () {}); /* 訳を読み込めなくても英語本文をそのまま表示する */
    return;
  }
  var articleLang = LANGS[lang];
  if (!articleLang) return;
  if (articleLang.dict && Object.keys(articleLang.dict).length) { translate(articleLang); return; }
  if (!window.fetch) return;
  (EARLY || getJson(langUrl('data')))
    .then(function (articleData) { articleLang.dict = articleData.dict || {}; translate(articleLang); })
    .catch(function () {}); /* 訳を読み込めなくても英語本文をそのまま表示する */
  }

  function translate(L) {
  if (!L) return;

  /* ── 差し替え ───────────────────────────────────── */
  var DICT = L.dict || {};
  var PATTERNS = (L.patterns || []).map(function (p) { return [new RegExp(p[0]), p[1]]; });
  var INLINE = { A:1, ABBR:1, B:1, BR:1, CODE:1, EM:1, I:1, MARK:1, Q:1, S:1, SMALL:1,
                 STRONG:1, SUB:1, SUP:1, U:1, TIME:1, WBR:1 };
  var SKIP = { SCRIPT:1, STYLE:1, NOSCRIPT:1, TEXTAREA:1, SELECT:1, OPTION:1, TEMPLATE:1 };
  var ATTRS = ['placeholder', 'title', 'aria-label'];
  var LETTER = /[A-Za-z]/;
  var LEARN = [];   /* 🇬🇧 英語学習モード用：訳した文と、もとの英文の組 */

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

  /* 🔢 数字と単位を、行の終わりで割らない（2026-10-04）：「2000｜年代」のように、数字だけが行末に残っていた。
     見えない「くっつける印」（U+2060）を、数字と単位のあいだに入れる。日本語・中国語だけ（韓国語は単語ごとに折るので不要） */
  var NUMJOIN = /([0-9０-９])(?=(?:年代|年|か月|ヶ月|ヵ月|月|日|時間|時|分|秒|曲|本|枚|人|円|歳|歲|代|倍|個|个|回|次|語|语|階|层|層|泊|度|％|%|冊|件|社|台|点|位|着|戦|試合|万|億|亿|千|百|番|目|割|元|キロ|メートル|km|cm|kg))/g;
  function joinNum(s) { return (lang === 'ja' || lang === 'zh' || lang === 'zh-Hant') ? String(s).replace(NUMJOIN, '$1\u2060') : s; }

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
        place(el, u.nodes, joinNum(tr));
        if (learnable(el)) LEARN.push({ el: el, en: u.key,   /* 画面に出す英文は、<br> を改行のまま残す */
          show: u.nodes.map(function (n) { return n.nodeName === 'BR' ? '\n' : (n.nodeType === 3 ? n.nodeValue : n.textContent); })
            .join('').split('\n').map(norm).filter(Boolean).join('\n') });
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
  /* この歌詞だけ、タミル語・テルグ語では英語の引用を保つ。
     それ以外の言語では works/<slug>/i18n/<lang>.json の訳を表示する。 */
  if (lang === 'ta' || lang === 'te') {
    document.querySelectorAll('.lyric-en').forEach(function (el) { el.setAttribute('translate', 'no'); });
  }
  walk(document.body);
  if (!DATA.lazyTop) drawLearn(LEARN);

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
