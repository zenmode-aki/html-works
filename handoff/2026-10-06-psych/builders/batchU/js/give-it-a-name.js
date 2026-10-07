/* 🏷️ 名前ルーレット：押すと名前がくるくる回って止まる → そのものが大切にされる。JS は data-* と数字だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var things = [].slice.call(g.querySelectorAll('.thing')), cn = g.querySelector('.cn'), again = g.querySelector('.again');
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  function count() {
    var n = things.filter(function (t) { return t.getAttribute('data-done') === '1'; }).length;
    cn.textContent = n;
    if (n === things.length && g.getAttribute('data-all') !== '1') {
      g.setAttribute('data-all', '1');
      if (window.pengessoPop) {
        var k = g.getBoundingClientRect();
        window.pengessoPop(k.left + k.width / 2, k.top + k.height / 2, ['🏷️', '⚽', '🪴', '☕', '🐧'], 18);
      }
      if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
    }
  }
  things.forEach(function (t) {
    var btn = t.querySelector('.namebtn'), obj = t.querySelector('.obj');
    btn.addEventListener('click', function () {
      if (t.getAttribute('data-roll') === '1' || t.getAttribute('data-done') === '1') return;
      t.setAttribute('data-roll', '1');
      var i = Math.floor(Math.random() * 4), steps = reduce ? 1 : 10 + Math.floor(Math.random() * 4);
      (function spin() {
        i = (i + 1) % 4; t.setAttribute('data-n', i);
        if (--steps > 0) { setTimeout(spin, 70 + (12 - steps) * 8); return; }
        t.setAttribute('data-roll', '0');
        t.setAttribute('data-done', '1');
        obj.classList.remove('bump'); void obj.offsetWidth; obj.classList.add('bump');
        if (window.pengessoPop) {
          var k = obj.getBoundingClientRect();
          window.pengessoPop(k.left + k.width / 2, k.top + k.height / 2, ['💖', '✨'], 8);
        }
        count();
      })();
    });
  });
  again.addEventListener('click', function () {
    things.forEach(function (t) { t.removeAttribute('data-n'); t.removeAttribute('data-done'); t.removeAttribute('data-roll'); });
    g.setAttribute('data-all', '0'); cn.textContent = 0;
  });
})();