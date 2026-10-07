/* 🎡 軽い言葉ルーレット：JS は data-* / class / style / hidden だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var wheel = g.querySelector('.wheel'), spin = g.querySelector('.spin'), said = g.querySelector('.said'), mark = g.querySelector('.mark'),
      bags = [].slice.call(g.querySelectorAll('.bag')), again = g.querySelector('.again');
  var rot = 0, last = -1, left = 4, busy = false, t1 = 0, t2 = 0;
  g.querySelector('.again-row').hidden = true;
  function paint() {
    g.setAttribute('data-left', left);
    mark.style.left = ((4 - left) / 4 * 100) + '%';
  }
  spin.addEventListener('click', function () {
    if (busy || left <= 0) return;
    busy = true; spin.disabled = true;
    var k; do { k = Math.floor(Math.random() * 6); } while (k === last);
    last = k;
    var target = 360 - (k * 60 + 30);
    var cur = ((rot % 360) + 360) % 360;
    rot += 360 * 3 + ((target - cur + 360) % 360);
    wheel.style.transform = 'rotate(' + rot + 'deg)';
    t1 = setTimeout(function () {
      g.setAttribute('data-w', k + 1);
      said.classList.remove('show'); void said.offsetWidth; said.classList.add('show');
      var b = bags.filter(function (x) { return !x.hidden && !x.classList.contains('drop'); });
      var bag = b[b.length - 1];
      if (bag) { bag.classList.add('drop'); t2 = setTimeout(function () { bag.hidden = true; }, 560); }
      left -= 1; paint();
      var r = g.querySelector('.pen').getBoundingClientRect();
      if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 3, left ? ['🪶', '✨'] : ['🐕', '🪶', '✨', '🐧'], left ? 8 : 20);
      if (left === 0) { g.querySelector('.again-row').hidden = false; if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} } }
      busy = false; spin.disabled = false;
    }, 1550);
  });
  again.addEventListener('click', function () {
    clearTimeout(t1); clearTimeout(t2); busy = false; spin.disabled = false;
    left = 4; bags.forEach(function (x) { x.hidden = false; x.classList.remove('drop'); });
    g.setAttribute('data-w', '0'); g.querySelector('.again-row').hidden = true; paint();
  });
  paint();
})();