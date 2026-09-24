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

  /* ── やわらかい丸ゴシック（2026-09-24 本人の希望）────────────────
     端末ごとに入っているフォントが違うので、日本語・韓国語のときだけ Google Fonts から読み込む。
     英字は今までのフォント（Arial Rounded など）を先に並べてそのまま使い、
     日本語・韓国語の文字だけが丸ゴシックに落ちる。英語表示のときは何も読み込まない */
  var SOFT = {
    ja: { css: 'Zen+Maru+Gothic:wght@400;500;700', name: '"Zen Maru Gothic"' },
    ko: { css: 'Gowun+Dodum', name: '"Gowun Dodum"' }
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

  function option(l) {
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'i18n-opt' + (l === lang ? ' on' : '');
    b.setAttribute('aria-pressed', String(l === lang));
    b.setAttribute('lang', l);
    b.innerHTML = '<span class="i18n-flag" aria-hidden="true">' + FLAGS[l] + '</span>' +
                  '<span class="i18n-name">' + NAMES[l] + '</span>';
    b.addEventListener('click', function () { go(l); });
    return b;
  }

  function drawSwitch() {
    if (avail.length < 2) return;
    var st = document.createElement('style');
    st.textContent =
      '.i18n-row{display:flex;justify-content:flex-end;margin:-6px 0 16px}' +
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
      '.i18n-menu{position:absolute;right:0;top:calc(100% + 6px);z-index:60;display:grid;gap:2px;min-width:170px;' +
      'padding:6px;background:#fff;border-radius:18px;box-shadow:0 14px 34px rgba(115,70,111,.22)}' +
      '.i18n-menu[hidden]{display:none}.i18n-menu .i18n-opt{justify-content:flex-start;width:100%}' +
      '.i18n-float{position:fixed;top:10px;right:10px;z-index:50}' +
      '@media (prefers-reduced-motion: reduce){.i18n-opt{transition:none}}';
    document.head.appendChild(st);

    var wrap = document.createElement('div');
    wrap.className = 'i18n-switch';
    wrap.setAttribute('translate', 'no');
    wrap.setAttribute('role', 'group');
    wrap.setAttribute('aria-label', 'Language');

    if (avail.length <= 3) {
      avail.forEach(function (l) { wrap.appendChild(option(l)); });
    } else {
      var cur = option(lang);
      cur.querySelector('.i18n-name').textContent = NAMES[lang] + ' ▾';
      cur.setAttribute('aria-haspopup', 'true');
      cur.setAttribute('aria-expanded', 'false');
      var menu = document.createElement('div');
      menu.className = 'i18n-menu';
      menu.hidden = true;
      avail.forEach(function (l) { menu.appendChild(option(l)); });
      cur.addEventListener('click', function (e) {
        e.stopPropagation();
        menu.hidden = !menu.hidden;
        cur.setAttribute('aria-expanded', String(!menu.hidden));
      });
      document.addEventListener('click', function () { menu.hidden = true; cur.setAttribute('aria-expanded', 'false'); });
      wrap.appendChild(cur);
      wrap.appendChild(menu);
    }

    /* 上のバーはスマホだと満員なので、そのすぐ下に1行つくって右に置く */
    var spot = document.querySelector('[data-i18n-switch]');
    var bar = document.querySelector('.topbar') || document.querySelector('body > header, main > header, header');
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
