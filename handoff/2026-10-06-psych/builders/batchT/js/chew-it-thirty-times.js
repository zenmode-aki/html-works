/* 😋 「もぐっ！」を30回。おにぎりが小さくなって、数とメーターが増える。コアラはずっと1枚目。JS は data-* / class / 数字 / style だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var btn = g.querySelector('.chew'), again = g.querySelector('.again'), cn = g.querySelector('.cn'), bar = g.querySelector('.prog i');
  var food = g.querySelector('.food'), peng = g.querySelector('.peng'), ts = g.querySelector('.ts');
  var GOAL = 30, n = 0, t0 = 0;
  function now() { return (window.performance && performance.now) ? performance.now() : Date.now(); }
  function bump(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function render() {
    cn.textContent = n;
    bar.style.width = (n / GOAL * 100) + '%';
    food.style.transform = 'scale(' + (1 - n / GOAL * 0.75) + ')';
    g.setAttribute('data-m', n === 0 ? 0 : n < 10 ? 1 : n < 20 ? 2 : 3);
    g.setAttribute('data-done', n >= GOAL ? '1' : '0');
  }
  btn.addEventListener('click', function () {
    if (n >= GOAL) return;
    if (n === 0) t0 = now();
    n++;
    render(); bump(cn, 'tick'); bump(peng, 'chomp');
    if (n >= GOAL) {
      ts.textContent = Math.max(1, Math.round((now() - t0) / 1000));
      if (window.pengessoPop) {
        var r = peng.getBoundingClientRect();
        window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🍙', '😋', '🐧', '✨', '🎉'], 18);
      }
      if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
    } else if (n % 10 === 0 && navigator.vibrate) { try { navigator.vibrate(12); } catch (e) {} }
  });
  again.addEventListener('click', function () { n = 0; render(); });
  render();
})();