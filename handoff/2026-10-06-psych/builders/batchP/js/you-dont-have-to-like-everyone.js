/* 🍽 今日のメニュー：JS は data-r / data-c / data-e / class / 絵文字 / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var chs = [].slice.call(g.querySelectorAll('.ch'));
  var pips = [].slice.call(g.querySelectorAll('.pip'));
  var bar = g.querySelector('.bar i'), nums = [].slice.call(g.querySelectorAll('.en-n'));
  var fx = g.querySelector('.fx'), face = g.querySelector('.me-face');
  var r = 1, energy = 100, paid = {};
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function drawEnergy() {
    bar.style.width = Math.max(4, energy) + '%';
    bar.classList.toggle('low', energy < 60);
    nums.forEach(function (n) { n.textContent = String(energy); });
  }
  function setRound(n) {
    r = n;
    g.setAttribute('data-r', String(n)); g.setAttribute('data-c', '');
    pips.forEach(function (p, i) { p.classList.toggle('on', i < n); });
    chs.forEach(function (b) { b.classList.remove('sel'); });
    fx.textContent = '❔';
  }
  chs.forEach(function (b) {
    b.addEventListener('click', function () {
      var c = b.getAttribute('data-c');
      g.setAttribute('data-c', '');
      void g.offsetWidth;            /* 同じ答えを2回押しても、ゆれ・ジャンプがもう一度出るように */
      g.setAttribute('data-c', c);
      chs.forEach(function (x) { x.classList.toggle('sel', x === b); });
      if (c === 'a') {
        fx.textContent = '💦';
        if (!paid[r]) { paid[r] = 1; energy = Math.max(0, energy - 30); drawEnergy(); }
        if (navigator.vibrate) { try { navigator.vibrate([20, 40, 20]); } catch (e) {} }
      } else {
        fx.textContent = '😌';
        if (window.pengessoPop) {
          var k = b.getBoundingClientRect();
          window.pengessoPop(k.left + k.width / 2, k.top + k.height / 2, r === 3 ? ['👋', '🐧', '✨'] : ['😌', '🍽️', '✨'], 10);
        }
      }
    });
  });
  g.querySelector('.go-next').addEventListener('click', function () {
    if (r < 3) { setRound(r + 1); return; }
    g.setAttribute('data-e', energy === 100 ? 'full' : 'low');
    g.setAttribute('data-r', 'end');
    if (energy === 100 && window.pengessoPop) {
      var k = g.querySelector('.end').getBoundingClientRect();
      window.pengessoPop(k.left + k.width / 2, k.top + 30, ['🐧', '💛', '✨', '🍽️'], 18);
    }
  });
  g.querySelector('.reset').addEventListener('click', function () {
    energy = 100; paid = {}; drawEnergy(); setRound(1); g.setAttribute('data-e', 'full');
  });
  drawEnergy();
})();