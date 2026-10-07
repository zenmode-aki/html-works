/* 🌪️ タワーを倒してみよう：JS は data-ev / data-m / data-end / class / 数字だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var tower = g.querySelector('.tower'), b1 = g.querySelector('.b1'), b2 = g.querySelector('.b2'), b3 = g.querySelector('.b3');
  var bubble = g.querySelector('.bubble'), hn = g.querySelector('.hn');
  var hits = 0;
  function restart(el, c) { el.classList.remove(c); void el.offsetWidth; el.classList.add(c); }
  g.querySelector('.bad').addEventListener('click', function () {
    if (hits >= 5) return;
    hits++;
    hn.textContent = String(hits);
    g.setAttribute('data-ev', String(hits)); restart(bubble, 'show');
    restart(tower, 'quake');
    if (hits === 1) { b1.classList.add('fallen'); g.setAttribute('data-m', 'fall'); }
    else { restart(b2, 'wob'); restart(b3, 'wob'); g.setAttribute('data-m', 'hold'); }
    if (hits === 5) {
      g.setAttribute('data-m', 'end'); g.setAttribute('data-end', '1');
      if (window.pengessoPop) { var r = b3.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['💖', '🐧', '✨', '🧱'], 22); }
    }
  });
  b3.addEventListener('click', function () {
    restart(b3, 'wob');
    if (g.getAttribute('data-end') !== '1') g.setAttribute('data-m', 'tap');
    if (window.pengessoPop) { var r = b3.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['💖'], 6); }
  });
  g.querySelector('.reset').addEventListener('click', function () {
    hits = 0; hn.textContent = '0';
    b1.classList.remove('fallen'); b2.classList.remove('wob'); b3.classList.remove('wob');
    g.setAttribute('data-ev', '0'); g.setAttribute('data-m', 'idle'); g.setAttribute('data-end', '0');
  });
})();