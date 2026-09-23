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

  /* ── 切り替えボタン ─────────────────────────────── */
  function drawSwitch() {
    if (avail.length < 2) return;
    var st = document.createElement('style');
    st.textContent =
      '.i18n-row{display:flex;justify-content:flex-end;margin:-6px 0 16px}' +
      '.i18n-switch{display:inline-flex;align-items:center;gap:4px;font-size:13px;line-height:1;' +
      'background:#fff;color:#6b5a7b;border:2px solid rgba(255,255,255,.9);border-radius:999px;' +
      'padding:5px 6px 5px 12px;box-shadow:0 6px 16px rgba(115,70,111,.08);white-space:nowrap}' +
      '.i18n-switch select{font:inherit;color:inherit;background:transparent;border:0;padding:2px 2px;cursor:pointer}' +
      '.i18n-switch select option{color:#222;background:#fff}' +
      '.i18n-float{position:fixed;top:10px;right:10px;z-index:50;background:rgba(255,255,255,.9);color:#222}' +
      '.i18n-note{margin:28px 0 8px;padding:18px 20px;border:1.5px dashed currentColor;border-radius:18px;' +
      'font-size:14px;line-height:1.8;opacity:.9}' +
      '.i18n-note p{margin:0 0 .7em}.i18n-note p:last-child{margin:0}' +
      '.i18n-note .i18n-note-head{font-weight:700;margin-bottom:.5em}';
    document.head.appendChild(st);

    var wrap = document.createElement('label');
    wrap.className = 'i18n-switch';
    wrap.setAttribute('translate', 'no');
    var sel = document.createElement('select');
    sel.setAttribute('aria-label', 'Language');
    avail.forEach(function (l) {
      var o = document.createElement('option');
      o.value = l; o.textContent = NAMES[l];
      if (l === lang) o.selected = true;
      sel.appendChild(o);
    });
    sel.addEventListener('change', function () {
      save(sel.value);
      var u = location.href.replace(/([?&])lang=[^&#]*&?/, '$1').replace(/[?&](#|$)/, '$1');
      if (u === location.href) location.reload(); else location.replace(u);
    });
    wrap.appendChild(document.createTextNode('🌐'));
    wrap.appendChild(sel);

    /* 上のバーはスマホだと満員なので、そのすぐ下に1行つくって右に置く */
    var spot = document.querySelector('[data-i18n-switch]');
    var bar = document.querySelector('.topbar') || document.querySelector('body > header, main > header, header');
    if (spot) spot.appendChild(wrap);
    else if (bar) {
      var row = document.createElement('div');
      row.className = 'i18n-row';
      row.appendChild(wrap);
      bar.parentNode.insertBefore(row, bar.nextSibling);
    } else { wrap.className += ' i18n-float'; document.body.appendChild(wrap); }
  }

  drawSwitch();
  if (lang === 'en') return;

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

  /* ── 日本語版だけの一言 ─────────────────────────── */
  if (L.note) {
    var box = document.createElement('aside');
    box.className = 'i18n-note';
    box.innerHTML = L.note;
    var main = document.querySelector('main') || document.body;
    var nx = main.querySelector('.next');
    var slot = document.querySelector('[data-i18n-note]');
    if (slot) slot.appendChild(box);
    else if (nx) nx.parentNode.insertBefore(box, nx);
    else main.appendChild(box);
  }

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
})();
