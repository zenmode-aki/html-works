/* 🏆 自分だけのトロフィー：願いを1つ選ぶ → トロフィーの上にその絵文字、台座に願いの文字（HTML に用意したもの）。JS は data-* と class と絵文字だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var ws = [].slice.call(g.querySelectorAll('.wish')), make = g.querySelector('.make'), cmp = g.querySelector('.cmp');
  var again = g.querySelector('.again'), we = g.querySelector('.cup-we'), cup = g.querySelector('.cup'), ruler = g.querySelector('.ruler');
  var EM = ['🎣', '🍳', '✈️', '☕', '📚', '🏡'], pick = -1;
  function pop(el, list, k) {
    if (!window.pengessoPop) return;
    var b = el.getBoundingClientRect();
    window.pengessoPop(b.left + b.width / 2, b.top + b.height / 2, list, k);
  }
  ws.forEach(function (w, i) {
    w.addEventListener('click', function () {
      if (g.getAttribute('data-s') !== 'pick') return;
      pick = i;
      ws.forEach(function (x) { x.classList.remove('sel'); x.setAttribute('aria-pressed', 'false'); });
      w.classList.add('sel'); w.setAttribute('aria-pressed', 'true');
      we.textContent = EM[i];
      g.setAttribute('data-w', i); g.setAttribute('data-pick', '1');
      make.disabled = false;
    });
  });
  make.addEventListener('click', function () {
    if (pick < 0) return;
    g.setAttribute('data-s', 'done');
    setTimeout(function () { pop(cup, ['🏆', EM[pick], '✨', '🐧', '🌟'], 18); }, 250);
    if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
  });
  cmp.addEventListener('click', function () {
    ruler.classList.remove('no'); void ruler.offsetWidth; ruler.classList.add('no');
    g.setAttribute('data-cmp', '1');
  });
  again.addEventListener('click', function () {
    pick = -1; we.textContent = '❔'; make.disabled = true;
    ws.forEach(function (x) { x.classList.remove('sel'); x.setAttribute('aria-pressed', 'false'); });
    g.setAttribute('data-w', ''); g.setAttribute('data-pick', '0'); g.setAttribute('data-cmp', '0'); g.setAttribute('data-s', 'pick');
  });
})();