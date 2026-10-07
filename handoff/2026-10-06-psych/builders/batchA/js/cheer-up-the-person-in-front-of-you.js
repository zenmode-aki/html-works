/* 🔋 元気どろぼうをパチン：JS は data-* / class / disabled / 絵文字 / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var bubs = [].slice.call(g.querySelectorAll('.bub'));
  var segs = [].slice.call(g.querySelectorAll('.bat i'));
  var face = g.querySelector('.fr-badge'), pct = g.querySelector('.pct');
  var FACE = ['😔', '😐', '🙂', '🙂', '😊', '😄', '🤩'];
  var n = 0;
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function draw() {
    segs.forEach(function (s, i) { s.classList.toggle('on', i < n); });
    face.textContent = FACE[n];
    pct.textContent = Math.round(n / bubs.length * 100) + '%';
    g.setAttribute('data-e', String(n));
    g.setAttribute('data-stage', n === 0 ? '0' : n < 4 ? '1' : n < bubs.length ? '2' : '3');
  }
  bubs.forEach(function (b) {
    b.addEventListener('click', function () {
      if (b.classList.contains('gone')) return;
      b.classList.add('gone'); b.disabled = true;
      n++; draw(); restart(face, 'boing');
      if (navigator.vibrate) { try { navigator.vibrate(12); } catch (e) {} }
      if (n === bubs.length && window.pengessoPop) {
        var r = g.querySelector('.fr-face').getBoundingClientRect();
        window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['⚡', '🔋', '🐧', '💛', '✨'], 22);
      }
    });
  });
  g.querySelector('.reset').addEventListener('click', function () {
    bubs.forEach(function (b) { b.classList.remove('gone'); b.disabled = false; });
    n = 0; draw();
  });
  draw();
})();