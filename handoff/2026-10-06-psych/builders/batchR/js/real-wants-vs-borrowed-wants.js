/* 🏷️ シールをはがす：JS は class・数字・style だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var items = [].slice.call(g.querySelectorAll('.item')), ln = g.querySelector('.ln'), again = g.querySelector('.again');
  function count() { return items.filter(function (it) { return !it.classList.contains('off'); }).length; }
  function bounce(el) { el.classList.remove('boing'); void el.offsetWidth; el.classList.add('boing'); }
  items.forEach(function (it) {
    var peel = it.querySelector('.peel'), bar = it.querySelector('.want i');
    peel.addEventListener('click', function () {
      if (it.classList.contains('off')) return;
      it.classList.add('off');
      var real = it.classList.contains('real');
      bar.style.width = real ? '100%' : '14%';
      bounce(it.querySelector('.ie'));
      var left = count(); ln.textContent = String(left);
      if (window.pengessoPop) {
        var r = it.getBoundingClientRect();
        window.pengessoPop(r.left + r.width / 2, r.top + r.height / 3, real ? ['💛', '📚', '✨'] : ['💨'], real ? 12 : 4);
      }
      if (left === 0) {
        g.setAttribute('data-s', 'end');
        if (window.pengessoPop) { var r2 = g.querySelector('.result').getBoundingClientRect(); window.pengessoPop(r2.left + r2.width / 2, r2.top, ['💛', '🐧', '✨'], 14); }
      }
    });
  });
  again.addEventListener('click', function () {
    items.forEach(function (it) { it.classList.remove('off'); it.querySelector('.want i').style.width = ''; });
    ln.textContent = String(items.length); g.setAttribute('data-s', 'play');
  });
})();