/* 📦 悩みの仕分け：JS は data-s・class・数字・style だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var cards = [].slice.call(g.querySelectorAll('.wcard'));
  var boxes = [].slice.call(g.querySelectorAll('.box'));
  var cntN = g.querySelector('.cnt-n'), bar = g.querySelector('.gmeter i'), cloud = g.querySelector('.cloud'), again = g.querySelector('.again');
  var i = 0, counts = [0, 0, 0, 0], busy = false, t1 = 0, t2 = 0;
  function paint() {
    cards.forEach(function (c, k) { c.classList.toggle('now', k === i); c.classList.remove('fly'); c.removeAttribute('data-to'); });
    cntN.textContent = String(Math.min(i + 1, cards.length));
    bar.style.width = (i / cards.length * 100) + '%';
    cloud.style.transform = 'scale(' + (0.35 + 0.65 * (cards.length - i) / cards.length).toFixed(2) + ')';
    boxes.forEach(function (b, k) { b.querySelector('.bn').textContent = String(counts[k]); });
  }
  function bump(el) { el.classList.remove('boing'); void el.offsetWidth; el.classList.add('boing'); }
  function sortInto(k) {
    var s = g.getAttribute('data-s');
    if (busy || s !== 'play') return;
    busy = true;
    var c = cards[i];
    c.setAttribute('data-to', String(k)); c.classList.add('fly');
    t1 = setTimeout(function () {
      counts[k]++; i++;
      bump(boxes[k]);
      if (i >= cards.length) { paint(); finish(); } else { paint(); }
      busy = false;
    }, 300);
  }
  function finish() {
    g.setAttribute('data-s', 'end');
    t2 = setTimeout(function () {
      g.setAttribute('data-s', 'hungry');
      if (window.pengessoPop) {
        var r = g.querySelector('.result').getBoundingClientRect();
        window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🍙', '🐧', '📦', '✨'], 16);
      }
    }, 1300);
  }
  boxes.forEach(function (b, k) { b.addEventListener('click', function () { sortInto(k); }); });
  again.addEventListener('click', function () {
    clearTimeout(t1); clearTimeout(t2); busy = false;
    i = 0; counts = [0, 0, 0, 0]; g.setAttribute('data-s', 'play'); paint();
  });
  paint();
})();