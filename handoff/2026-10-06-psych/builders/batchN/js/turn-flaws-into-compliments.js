/* 📖 言い換え辞書：JS は class / aria / 絵文字 / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var cards = [].slice.call(g.querySelectorAll('.fc'));
  var face = g.querySelector('.me-face'), bar = g.querySelector('.p-bar i'), num = g.querySelector('.p-n');
  var FACES = ['😔', '😐', '😐', '🙂', '🙂', '😊', '😊', '😄', '🤩'];
  function restart(el, c) { el.classList.remove(c); void el.offsetWidth; el.classList.add(c); }
  function draw() {
    var n = cards.filter(function (c) { return c.classList.contains('on'); }).length;
    num.textContent = n + '/8';
    bar.style.width = (n / 8 * 100) + '%';
    if (face.textContent !== FACES[n]) { face.textContent = FACES[n]; restart(face, 'boing'); }
    g.setAttribute('data-all', n === 8 ? '1' : '0');
    return n;
  }
  cards.forEach(function (c) {
    c.addEventListener('click', function () {
      var before = draw();
      var on = !c.classList.contains('on');
      c.classList.toggle('on', on);
      c.setAttribute('aria-pressed', on ? 'true' : 'false');
      var after = draw();
      if (!on || !window.pengessoPop) return;
      var r = c.getBoundingClientRect(), x = r.left + r.width / 2, y = r.top + r.height / 2;
      if (after === 8 && before < 8) window.pengessoPop(x, y, ['🎉', '📖', '🐧', '✨', '🌟'], 22);
      else window.pengessoPop(x, y, ['✨', '🌟'], 8);
    });
  });
  g.querySelector('.reset').addEventListener('click', function () {
    cards.forEach(function (c) { c.classList.remove('on'); c.setAttribute('aria-pressed', 'false'); });
    draw();
  });
  draw();
})();