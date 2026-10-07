/* 🧭 だれが点数を決める？：JS は data-m / data-st / class / aria だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var bO = g.querySelector('.m-others'), bM = g.querySelector('.m-mine'), boo = g.querySelector('.boo');
  var stars = [].slice.call(g.querySelectorAll('.star'));
  function restart(el, c) { el.classList.remove(c); void el.offsetWidth; el.classList.add(c); }
  function mode(m) {
    g.setAttribute('data-m', m);
    bO.setAttribute('aria-pressed', m === 'others' ? 'true' : 'false');
    bM.setAttribute('aria-pressed', m === 'mine' ? 'true' : 'false');
  }
  bO.addEventListener('click', function () { mode('others'); setTimeout(function () { restart(boo, 'shake2'); }, 350); });
  bM.addEventListener('click', function () { mode('mine'); });
  stars.forEach(function (s, i) {
    s.addEventListener('click', function () {
      var n = i + 1;
      g.setAttribute('data-st', String(n));
      stars.forEach(function (t, k) {
        var on = k < n; t.classList.toggle('on', on);
        if (on) restart(t, 'pop1'); else t.classList.remove('pop1');
      });
      if (window.pengessoPop) {
        var r = s.getBoundingClientRect();
        window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, n === 5 ? ['🌟', '⭐', '🐧', '⚾', '✨'] : ['⭐', '✨'], n === 5 ? 20 : 6);
      }
    });
  });
})();