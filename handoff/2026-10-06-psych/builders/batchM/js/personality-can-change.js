
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
