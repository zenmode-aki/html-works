/* 💢 押しのけると増える気持ち：JS は class / style / 絵文字 / 数字 / data-* だけを変える。新しい玉は HTML の玉を複製するだけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var arena = g.querySelector('.arena'), first = arena.querySelector('.bub'), cn = g.querySelector('.cn');
  var MAX = 14, timers = [];
  function bubs() { return [].slice.call(arena.querySelectorAll('.bub')); }
  function live() { return bubs().filter(function (b) { return !b.classList.contains('away'); }); }
  function count() { cn.textContent = live().length; cn.classList.remove('bump'); void cn.offsetWidth; cn.classList.add('bump'); }
  function restart(el, c) { el.classList.remove(c); void el.offsetWidth; el.classList.add(c); }
  arena.addEventListener('click', function (e) {
    var b = e.target.closest ? e.target.closest('.bub') : null;
    if (!b || b.classList.contains('soft')) return;
    var s = g.getAttribute('data-st');
    if (s === 'soft') return;
    restart(b, 'hit');
    var n = live().length;
    var add = n >= MAX ? 0 : Math.min(2, MAX - n);
    for (var i = 0; i < add; i++) {
      var c = first.cloneNode(true);
      c.className = 'bub born';
      c.style.left = (12 + Math.random() * 64) + '%';
      c.style.top = (18 + Math.random() * 64) + '%';
      c.textContent = ['💢', '😤', '💢', '😣'][Math.floor(Math.random() * 4)];
      arena.insertBefore(c, arena.querySelector('.pen'));
    }
    g.setAttribute('data-st', live().length >= MAX ? 'full' : 'more');
    count();
    if (navigator.vibrate) { try { navigator.vibrate(15); } catch (e2) {} }
  });
  g.querySelector('.okbtn').addEventListener('click', function () {
    g.setAttribute('data-st', 'soft');
    var list = live();
    list.forEach(function (b, i) {
      b.classList.remove('hit', 'born'); b.classList.add('soft'); b.textContent = '🫧';
      timers.push(setTimeout(function () { b.classList.add('away'); count(); }, 500 + i * 120));
    });
    var r = arena.getBoundingClientRect();
    if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['💛', '🫧', '🐧', '✨'], 18);
  });
  g.querySelector('.again').addEventListener('click', function () {
    timers.forEach(clearTimeout); timers = [];
    bubs().forEach(function (b) { if (b !== first) b.parentNode.removeChild(b); });
    first.className = 'bub'; first.textContent = '💢';
    g.setAttribute('data-st', 'start'); count();
  });
})();