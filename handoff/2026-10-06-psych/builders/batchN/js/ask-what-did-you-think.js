/* 💭 知ってる話の、知らない気持ち：JS は data-* / class / 絵文字 / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var tbs = [].slice.call(g.querySelectorAll('.tb'));
  var fx = g.querySelector('.me .fx'), fn = g.querySelector('.fn');
  var FACES = ['🤔', '😊', '😄', '🤩'];
  function count() { return tbs.filter(function (t) { return t.classList.contains('popped'); }).length; }
  function draw() {
    var n = count();
    fn.textContent = n + '/3';
    g.setAttribute('data-all', n === 3 ? '1' : '0');
    if (g.getAttribute('data-s') === 'open') fx.textContent = FACES[n];
    return n;
  }
  g.querySelector('.know').addEventListener('click', function () {
    g.setAttribute('data-s', 'cold'); fx.textContent = '😔';
  });
  g.querySelector('.ask').addEventListener('click', function () {
    g.setAttribute('data-s', 'open'); draw();
    if (window.pengessoPop) { var r = g.querySelector('.me').getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['💡', '✨'], 8); }
  });
  tbs.forEach(function (t) {
    t.addEventListener('click', function () {
      if (t.classList.contains('popped')) return;
      t.classList.add('popped');
      var n = draw();
      if (!window.pengessoPop) return;
      var r = t.getBoundingClientRect(), x = r.left + r.width / 2, y = r.top + r.height / 2;
      if (n === 3) window.pengessoPop(x, y, ['🎁', '🎉', '🐧', '💭', '✨'], 22);
      else window.pengessoPop(x, y, ['💭', '✨'], 10);
    });
  });
  g.querySelector('.reset').addEventListener('click', function () {
    tbs.forEach(function (t) { t.classList.remove('popped'); });
    g.setAttribute('data-s', 'idle'); fx.textContent = '😊'; draw();
  });
  draw();
})();