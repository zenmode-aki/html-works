/* 🙏 返却カウンター：JS は data-s / data-st / class / style / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var cards = [].slice.call(g.querySelectorAll('.rent'));
  var DUR = [2500, 4000, 5500, 7000];
  var tn = g.querySelector('.tn');
  var t0 = 0, tick = 0;
  function restart(el, c) { el.classList.remove(c); void el.offsetWidth; el.classList.add(c); }
  function bar(c, f) { c.querySelector('.bar i').style.width = (f * 100) + '%'; }
  function count() { var n = g.querySelectorAll('.rent[data-st="back"]').length; tn.textContent = String(n); return n; }
  function loop() {
    var el = Date.now() - t0, running = 0;
    cards.forEach(function (c, i) {
      if (c.getAttribute('data-st') !== 'run') return;
      var left = Math.max(0, 1 - el / DUR[i]);
      bar(c, left);
      if (left <= 0) { c.setAttribute('data-st', 'up'); restart(c, 'buzz'); }
      else running++;
    });
    if (!running) { clearInterval(tick); tick = 0; }
  }
  g.querySelector('.start').addEventListener('click', function () {
    cards.forEach(function (c) { c.setAttribute('data-st', 'run'); bar(c, 1); });
    g.setAttribute('data-s', 'run'); count();
    t0 = Date.now(); clearInterval(tick); tick = setInterval(loop, 80);
  });
  cards.forEach(function (c) {
    c.addEventListener('click', function () {
      if (c.getAttribute('data-st') !== 'up') return;
      c.setAttribute('data-st', 'back');
      restart(c.querySelector('.stamp'), 'thud');
      var r = c.getBoundingClientRect(), x = r.left + r.width / 2, y = r.top + r.height / 2;
      if (count() === 4) {
        g.setAttribute('data-s', 'done');
        if (window.pengessoPop) window.pengessoPop(x, y, ['🙏', '🐧', '✨', '🚲', '🌸'], 24);
      } else if (window.pengessoPop) {
        window.pengessoPop(x, y, ['🙏', '✨'], 10);
      }
    });
  });
  g.querySelector('.reset').addEventListener('click', function () {
    clearInterval(tick); tick = 0;
    cards.forEach(function (c) { c.setAttribute('data-st', 'wait'); c.classList.remove('buzz'); bar(c, 1); });
    g.setAttribute('data-s', 'idle'); count();
  });
})();