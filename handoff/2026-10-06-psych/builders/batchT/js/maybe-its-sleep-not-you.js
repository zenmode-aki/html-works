/* 💤 ぐっすり眠るたびに夜→朝。2晩ごとにラベルが1枚はがれる。JS は data-* と数字と絵文字だけを変える */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var btn = g.querySelector('.sleep'), again = g.querySelector('.again'), cn = g.querySelector('.cn');
  var mood = g.querySelector('.mood'), pips = g.querySelectorAll('.pip'), tags = g.querySelectorAll('.tag');
  var FACES = ['😠', '😠', '😐', '😐', '🙂', '🙂', '😊'];
  var MAX = 6, n = 0, busy = false;
  function render() {
    cn.textContent = n;
    g.setAttribute('data-n', n);
    for (var i = 0; i < pips.length; i++) pips[i].classList.toggle('on', i < n);
    for (var j = 0; j < tags.length; j++) tags[j].classList.toggle('off', n >= (j + 1) * 2);
    mood.textContent = FACES[n];
    g.setAttribute('data-done', n >= MAX ? '1' : '0');
  }
  function pop(el, list, k) {
    if (!window.pengessoPop || !el) return;
    var r = el.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, k);
  }
  btn.addEventListener('click', function () {
    if (busy || n >= MAX) return;
    busy = true;
    g.setAttribute('data-phase', 'night');
    setTimeout(function () {
      g.setAttribute('data-phase', 'morning');
      n++;
      render();
      busy = false;
      if (n % 2 === 0) pop(tags[n / 2 - 1], ['🏷️', '💤', '✨'], 8);
      if (n >= MAX) {
        pop(g.querySelector('.peng'), ['🐧', '💤', '🌙', '✨', '😊'], 18);
        if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
      }
    }, 800);
  });
  again.addEventListener('click', function () {
    n = 0; busy = false;
    g.setAttribute('data-phase', 'day');
    render();
  });
  render();
})();