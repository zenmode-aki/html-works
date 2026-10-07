/* 💛 「手伝おうか？」を集める：友だちを押すと助けた数が増える。1週間後、助けた数だけ仲間が来て、雪のかたまりを動かす。JS は data-* と class と数字と絵文字だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var frs = [].slice.call(g.querySelectorAll('.fr')), later = g.querySelector('.later'), again = g.querySelector('.again');
  var cn = g.querySelector('.cn'), pw = g.querySelector('.pw'), n = 0;
  var BAD = ['🧣', '📦', '🗺️'];
  function pop(el, list, k) {
    if (!window.pengessoPop) return;
    var b = el.getBoundingClientRect();
    window.pengessoPop(b.left + b.width / 2, b.top + b.height / 2, list, k);
  }
  frs.forEach(function (f) {
    f.addEventListener('click', function () {
      if (g.getAttribute('data-s') !== 'help' || f.classList.contains('ok')) return;
      f.classList.add('ok');
      f.querySelector('.fr-badge').textContent = '💛';
      n++; cn.textContent = n;
      pop(f.querySelector('.fr-av'), ['💛', '✨'], 8);
    });
  });
  later.addEventListener('click', function () {
    g.setAttribute('data-n', n); pw.textContent = n + 1;
    g.setAttribute('data-win', n >= 3 ? '1' : '0');
    g.setAttribute('data-s', 'big');
    var y = g.querySelector('.bigday');
    if (y.scrollIntoView) { try { y.scrollIntoView({ block: 'center', behavior: 'smooth' }); } catch (e) {} }
    if (n >= 3) {
      setTimeout(function () { pop(g.querySelector('.l-nice .blk'), ['🐧', '💛', '❄️', '✨', '🎉'], 18); }, 600);
      if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
    }
  });
  again.addEventListener('click', function () {
    n = 0; cn.textContent = '0'; pw.textContent = '1';
    frs.forEach(function (f, i) { f.classList.remove('ok'); f.querySelector('.fr-badge').textContent = BAD[i]; });
    g.setAttribute('data-n', '0'); g.setAttribute('data-win', ''); g.setAttribute('data-s', 'help');
  });
})();