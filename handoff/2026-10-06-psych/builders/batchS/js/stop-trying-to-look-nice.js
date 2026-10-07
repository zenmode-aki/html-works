/* 💭 心配の泡をわろう：JS は data-n / data-done / class / style / 絵文字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var bubs = [].slice.call(g.querySelectorAll('.bub'));
  var knob = g.querySelector('.look-knob'), me = g.querySelector('.me'), mf = g.querySelector('.mf');
  var timers = [];
  function restart(el, c) { el.classList.remove(c); void el.offsetWidth; el.classList.add(c); }
  function left() { return bubs.filter(function (b) { return !b.classList.contains('gone'); }).length; }
  function draw() {
    var n = left();
    g.setAttribute('data-n', String(n));
    knob.style.left = ((5 - n) / 5 * 100) + '%';
    knob.textContent = n === 0 ? '😆' : '👀';
    mf.textContent = n === 0 ? '😆' : n <= 2 ? '🙂' : n <= 4 ? '😅' : '😰';
    if (n === 0 && g.getAttribute('data-done') !== '1') {
      g.setAttribute('data-done', '1'); restart(me, 'hop-me');
      if (window.pengessoPop) { var r = me.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🎉', '🎈', '🐧', '🎶', '✨'], 24); }
    }
  }
  function pop(b) {
    if (b.classList.contains('gone')) return;
    b.classList.add('gone');
    var r = b.getBoundingClientRect();
    if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['💥', '🫧'], 6);
    timers.push(setTimeout(function () { b.classList.add('hide'); }, 320));
    restart(me, 'hop-me');
    draw();
  }
  bubs.forEach(function (b) { b.addEventListener('click', function () { pop(b); }); });
  g.querySelector('.laugh').addEventListener('click', function () {
    bubs.filter(function (b) { return !b.classList.contains('gone'); }).forEach(function (b, i) {
      timers.push(setTimeout(function () { pop(b); }, i * 140));
    });
  });
  g.querySelector('.reset').addEventListener('click', function () {
    timers.forEach(clearTimeout); timers = [];
    bubs.forEach(function (b) { b.classList.remove('gone', 'hide'); });
    g.setAttribute('data-done', '0');
    draw();
  });
})();