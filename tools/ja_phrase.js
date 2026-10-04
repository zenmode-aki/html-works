/* ✂️ 日本語の見出しを、文節（言葉のまとまり）で折り返す（2026-10-04）
   Chrome は CSS の word-break: auto-phrase でできるが、iPhone の Safari・Firefox にはまだない。
   なので Google の BudouX（Apache License 2.0。https://github.com/google/budoux）の日本語モデルで文節の境目を探し、
   そこに <wbr>（「ここで折ってよい」印）を入れる。そのうえで CSS（.ja-ph）が「<wbr> のところだけで折る」にする。
   見出しだけ（本文は、行がガタガタになるので、いままでどおり）。i18n_runtime.js が、必要なときだけ読み込む（Chrome では読まない）。
   モデルは tools/ja_phrase_model.json。assets/ja-phrase.js は tools/i18n.py が作る（手で書かない） */
(function () {
  var LICENSE = 'BudouX (c) 2021 Google LLC. Apache License 2.0. https://github.com/google/budoux';
  var M = __MODEL__;
  var BASE = 0, g, k;
  for (g in M) for (k in M[g]) BASE -= M[g][k] * 0.5;
  var has = Object.prototype.hasOwnProperty;
  function w(group, s) { var t = M[group]; return t && has.call(t, s) ? t[s] : 0; }

  /* 文を、文節ごとの配列にする（BudouX の parse と同じ計算） */
  function cut(s) {
    var out = [], last = 0;
    for (var i = 1; i < s.length; i++) {
      var sc = BASE;
      sc += w('UW1', s.substring(i - 3, i - 2)) + w('UW2', s.substring(i - 2, i - 1)) + w('UW3', s.substring(i - 1, i)) +
            w('UW4', s.substring(i, i + 1)) + w('UW5', s.substring(i + 1, i + 2)) + w('UW6', s.substring(i + 2, i + 3));
      sc += w('BW1', s.substring(i - 2, i)) + w('BW2', s.substring(i - 1, i + 1)) + w('BW3', s.substring(i, i + 2));
      sc += w('TW1', s.substring(i - 3, i)) + w('TW2', s.substring(i - 2, i + 1)) + w('TW3', s.substring(i - 1, i + 2)) + w('TW4', s.substring(i, i + 3));
      if (sc > 0) { out.push(s.slice(last, i)); last = i; }
    }
    out.push(s.slice(last));
    return out;
  }

  var SEL = 'h1,h2,h3,.card-label,.next-title,.prev-title,.post-title,.rel-title,.big,.closing-line';
  var SKIP = 'script,style,ruby,[translate="no"],.learn-en,.pack-say,.study-bar,.i18n-switch,.i18n-menu';
  var CJK = /[぀-ヿ㐀-鿿]/;
  var doc = document;

  function one(el) {
    if (el.__ph || el.closest(SKIP)) return;
    var nodes = [], tw = doc.createTreeWalker(el, 4, null, false), n, did = false;
    while ((n = tw.nextNode())) nodes.push(n);
    nodes.forEach(function (t) {
      if (!t.parentNode || !CJK.test(t.nodeValue) || (t.parentNode !== el && t.parentNode.closest(SKIP))) return;
      var parts = cut(t.nodeValue);
      if (parts.length < 2) return;
      var frag = doc.createDocumentFragment();
      parts.forEach(function (p, i) {
        if (i) frag.appendChild(doc.createElement('wbr'));
        frag.appendChild(doc.createTextNode(p));
      });
      t.parentNode.replaceChild(frag, t);
      did = true;
    });
    if (did) { el.__ph = 1; el.classList.add('ja-ph'); }
  }

  function apply(root) {
    if (!root || !root.querySelectorAll) return;
    if (root.matches && root.matches(SEL)) one(root);
    var els = root.querySelectorAll(SEL);
    for (var i = 0; i < els.length; i++) one(els[i]);
  }
  window.pengessoPhrase = apply;
  window.pengessoPhraseLicense = LICENSE;

  var st = doc.createElement('style');
  st.textContent = 'html:lang(ja) .ja-ph,.ja-ph{word-break:keep-all;overflow-wrap:anywhere}';   /* i18n_runtime.js の auto-phrase（同じ強さ）より後に書くので、こちらが勝つ */
  (doc.head || doc.documentElement).appendChild(st);

  apply(doc);

  /* あとから入る見出し（訳の差し替え・トップの一覧）も、同じように */
  if ('MutationObserver' in window) {
    var pending = [], timer = 0;
    new MutationObserver(function (ms) {
      ms.forEach(function (m) {
        [].forEach.call(m.addedNodes, function (a) {
          var e = a.nodeType === 3 ? a.parentElement : a.nodeType === 1 ? a : null;
          if (!e || (e.tagName === 'WBR')) return;
          var host = e.closest ? e.closest(SEL) : null;
          pending.push(host || e);
        });
      });
      if (pending.length && !timer) timer = setTimeout(function () {
        timer = 0;
        var list = pending; pending = [];
        list.forEach(function (e) { if (e.isConnected) { if (e.matches && e.matches(SEL)) one(e); else apply(e); } });
      }, 60);
    }).observe(doc.body || doc.documentElement, { childList: true, subtree: true });
  }
})();
