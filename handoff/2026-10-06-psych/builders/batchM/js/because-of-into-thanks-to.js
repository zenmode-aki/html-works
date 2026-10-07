
/* 🐻‍❄️ シロクマ実験 ＋ 🔄 ひっくり返しカード：JS は data-*・class・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var bears = [].slice.call(g.querySelectorAll('.bear')), bcn = g.querySelector('.bc-n'), flips = [].slice.call(g.querySelectorAll('.flip'));
  var n = 1;
  function awake() { return bears.filter(function (b) { return b.classList.contains('on') && !b.classList.contains('zz'); }).length; }
  function paint() { bcn.textContent = String(awake()); g.setAttribute('data-n', String(n)); }
  g.querySelector('.b-forget').addEventListener('click', function () {
    if (n < bears.length) { bears[n].classList.add('on'); n++; }
    else { bears.forEach(function (b) { b.classList.remove('zz'); }); var h = g.querySelector('.head'); h.classList.remove('shake'); void h.offsetWidth; h.classList.add('shake'); }
    if (n >= 3) g.setAttribute('data-b3', '1');
    paint();
  });
  flips.forEach(function (f) {
    f.addEventListener('click', function () {
      if (f.classList.contains('on')) return;
      f.classList.add('on');
      var k = 0;
      bears.forEach(function (b) { if (k < 2 && b.classList.contains('on') && !b.classList.contains('zz')) { b.classList.add('zz'); k++; } });
      paint();
      var r = f.getBoundingClientRect();
      if (flips.every(function (x) { return x.classList.contains('on'); })) {
        g.setAttribute('data-all', '1');
        if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['☀️', '🐻‍❄️', '💤', '🐧', '✨'], 22);
        if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
      } else if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['☀️', '✨'], 8);
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    n = 1;
    bears.forEach(function (b, i) { b.classList.remove('zz'); b.classList.toggle('on', i === 0); });
    flips.forEach(function (f) { f.classList.remove('on'); });
    g.setAttribute('data-b3', '0'); g.setAttribute('data-all', '0'); paint();
  });
  paint();
})();
