/* ☀️ 100点の挨拶：JS は data-* / aria-checked / 絵文字 / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var sws = [].slice.call(g.querySelectorAll('.sw'));
  var PTS = [30, 55, 80, 100], TFACE = ['😐', '🙂', '😊', '🥰'];
  var pts = g.querySelector('.pts'), bar = g.querySelector('.meter i'), tface = g.querySelector('.t-face');
  var sface = g.querySelector('.s-face'), talk = g.querySelector('.talk');
  var shown = 30, raf = 0, fin = 0, lastN = 0;
  function still() { try { return window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) { return false; } }
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function tween(to) {
    cancelAnimationFrame(raf); clearTimeout(fin);
    if (still()) { shown = to; pts.textContent = to; return; }
    fin = setTimeout(function () { cancelAnimationFrame(raf); shown = to; pts.textContent = to; }, 520);
    var from = shown, t0 = 0;
    function step(t) {
      if (!t0) t0 = t;
      var k = Math.min(1, (t - t0) / 420);
      shown = Math.round(from + (to - from) * (1 - Math.pow(1 - k, 3)));
      pts.textContent = shown;
      if (k < 1) raf = requestAnimationFrame(step);
    }
    raf = requestAnimationFrame(step);
  }
  function draw() {
    var n = 0;
    sws.forEach(function (b) {
      var on = b.getAttribute('aria-checked') === 'true';
      g.setAttribute('data-' + b.getAttribute('data-k'), on ? '1' : '0');
      if (on) n++;
    });
    g.setAttribute('data-n', String(n));
    sface.textContent = g.getAttribute('data-smile') === '1' ? '😄' : '😐';
    tface.textContent = TFACE[n];
    bar.style.width = PTS[n] + '%';
    tween(PTS[n]);
    if (n !== lastN) restart(tface, 'boing');
    var hit = n === 3 && lastN !== 3;
    lastN = n;
    return hit;
  }
  sws.forEach(function (b) {
    b.addEventListener('click', function () {
      b.setAttribute('aria-checked', b.getAttribute('aria-checked') === 'true' ? 'false' : 'true');
      if (b.getAttribute('data-k') === 'first') restart(talk, 'swap');
      if (draw() && window.pengessoPop) {
        var r = tface.getBoundingClientRect();
        window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['💯', '☀️', '🐧', '✨', '📛'], 20);
      }
    });
  });
  g.querySelector('.reset').addEventListener('click', function () {
    sws.forEach(function (b) { b.setAttribute('aria-checked', 'false'); });
    draw();
  });
  draw();
})();