/* 🌧️ 動いて悩みの雲を小さくする：JS は data-* / class / style / 絵文字 / 数字だけを変える */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var cloud = g.querySelector('.cloud'), pb = g.querySelector('.pb'), tool = g.querySelector('.tool'), bar = g.querySelector('.meter2 i'),
      cn = g.querySelector('.cn'), btn = g.querySelector('.tapbtn'), mvs = [].slice.call(g.querySelectorAll('.mv'));
  var W = 100, combo = 0, lastTap = 0, tick = 0;
  var ICON = { walk: '👟', clean: '🧹', shop: '🛒', sport: '⚽' };
  function now() { return Date.now(); }
  function st(s) { g.setAttribute('data-st', s); }
  function paint() {
    cloud.style.setProperty('--s', (0.28 + 0.72 * W / 100).toFixed(3));
    cloud.textContent = W > 60 ? '🌧️' : W > 25 ? '☁️' : '🌥️';
    bar.style.width = Math.max(0, W) + '%';
    cn.textContent = combo;
  }
  function restart(el, c) { el.classList.remove(c); void el.offsetWidth; el.classList.add(c); }
  mvs.forEach(function (b) {
    b.addEventListener('click', function () {
      mvs.forEach(function (x) { x.classList.toggle('sel', x === b); x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      g.setAttribute('data-mv', b.getAttribute('data-m'));
      tool.textContent = ICON[b.getAttribute('data-m')] || '👟';
      restart(tool, 'go');
    });
  });
  function loop() {
    if (g.getAttribute('data-st') === 'done' || g.getAttribute('data-st') === 'idle') return;
    if (now() - lastTap > 900) {
      if (combo) { combo = 0; }
      st('still');
      W = Math.min(100, W + 0.8);
      paint();
    }
    tick = setTimeout(loop, 120);
  }
  btn.addEventListener('click', function () {
    var s = g.getAttribute('data-st');
    if (s === 'done') {
      W = 100; combo = 0; st('idle'); paint(); return;
    }
    var t = now();
    combo = (t - lastTap < 900) ? combo + 1 : 1;
    lastTap = t;
    W -= combo >= 8 ? 8 : 6;
    restart(pb, 'hop'); restart(tool, 'go'); restart(cn, 'bump');
    if (W <= 0) {
      W = 0; clearTimeout(tick); st('done'); paint();
      cloud.textContent = '☀️';
      var r = cloud.getBoundingClientRect();
      if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['☀️', tool.textContent, '🐧', '✨'], 18);
      if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
      return;
    }
    if (s === 'idle') { st('move'); clearTimeout(tick); tick = setTimeout(loop, 120); }
    else st('move');
    paint();
  });
  paint();
})();