/* 🧬 人生いれかえマシン：JS は data-n・class・絵文字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var parts = [].slice.call(g.querySelectorAll('.part'));
  var slots = g.querySelectorAll('.me .sl');
  var icons = ['🧬', '🏠', '🎒'];
  var n = 0;
  function buzz() { g.classList.remove('buzz'); void g.offsetWidth; g.classList.add('buzz'); }
  parts.forEach(function (b) {
    b.addEventListener('click', function () {
      if (b.disabled) return;
      var i = +b.getAttribute('data-i');
      b.disabled = true; b.classList.add('done');
      slots[i].textContent = icons[i]; slots[i].classList.add('fill');
      n += 1; g.setAttribute('data-n', String(n)); buzz();
      if (n === 3) {
        if (window.pengessoPop) {
          var r = g.querySelector('.eq').getBoundingClientRect();
          window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🍵', '🐧', '✨', '🧬'], 16);
        }
        if (navigator.vibrate) { try { navigator.vibrate(25); } catch (e) {} }
      }
    });
  });
  g.querySelector('.again').addEventListener('click', function () {
    n = 0; g.setAttribute('data-n', '0'); g.classList.remove('buzz');
    parts.forEach(function (b) { b.disabled = false; b.classList.remove('done'); });
    [].forEach.call(slots, function (s) { s.textContent = '❔'; s.classList.remove('fill'); });
  });
})();