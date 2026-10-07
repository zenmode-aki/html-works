/* 🍀 不運をひっくり返そう：JS は data-n・class・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var cards = [].slice.call(g.querySelectorAll('.flip'));
  var num = g.querySelector('.cnt .num');
  var n = 0;
  cards.forEach(function (c) {
    c.addEventListener('click', function () {
      if (c.classList.contains('on')) return;
      c.classList.add('on');
      n += 1; num.textContent = String(n); g.setAttribute('data-n', String(n));
      var r = c.getBoundingClientRect();
      if (window.pengessoPop) {
        if (n < 4) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🍀', '✨'], 8);
        else { var d = g.querySelector('.deck').getBoundingClientRect(); window.pengessoPop(d.left + d.width / 2, d.top + d.height / 2, ['🍀', '☂️', '🥤', '🐧', '✨'], 20); }
      }
      if (navigator.vibrate) { try { navigator.vibrate(n < 4 ? 12 : 30); } catch (e) {} }
    });
  });
  g.querySelector('.again').addEventListener('click', function () {
    n = 0; num.textContent = '0'; g.setAttribute('data-n', '0');
    cards.forEach(function (c) { c.classList.remove('on'); });
  });
})();