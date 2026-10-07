/* 🫑 ピーマンの試食会：JS は data-t / class / 絵文字 / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var FACES = ['🍽️', '🐱', '🐰', '🐻', '🐶', '🐧'];
  var face = g.querySelector('.t-face'), pep = g.querySelector('.pepper');
  var qs = [].slice.call(g.querySelectorAll('.q'));
  var nFan = g.querySelector('.n-fan'), nChange = g.querySelector('.n-change');
  var t = 0;
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function draw() {
    g.setAttribute('data-t', String(t));
    face.textContent = FACES[t];
    qs.forEach(function (q, i) { q.classList.toggle('done', i < t - 1); q.classList.toggle('now', i === t - 1); });
    nFan.textContent = t === 5 ? '1' : '0';
  }
  g.querySelector('.go').addEventListener('click', function () {
    if (t >= 5) { t = 0; draw(); return; }
    t++;
    draw();
    restart(face, 'in');
    if (t < 5) {
      restart(pep, 'wob'); restart(nChange, 'bump');
    } else {
      restart(pep, 'love'); restart(nFan, 'bump');
      if (window.pengessoPop) {
        var k = pep.getBoundingClientRect();
        window.pengessoPop(k.left + k.width / 2, k.top + k.height / 2, ['🫑', '💚', '🐧', '✨'], 18);
      }
      if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
    }
  });
  draw();
})();