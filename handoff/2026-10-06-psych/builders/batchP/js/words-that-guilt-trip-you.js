/* 🔍 罪悪感ことばの翻訳機：JS は class / data-* / 数字 / 絵文字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var flips = [].slice.call(g.querySelectorAll('.flip'));
  var bar = g.querySelector('.bar i'), cn = g.querySelector('.cn'), ln = g.querySelector('.ln');
  var bub = g.querySelector('.ask-bub'), spin = g.querySelector('.spin'), mark = g.querySelector('.mark');
  var loops = 0;
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function opened() { return flips.filter(function (f) { return f.classList.contains('open'); }).length; }
  function draw() {
    var n = opened();
    cn.textContent = n + '/4';
    bar.style.width = Math.max(4, 100 - n * 22 - (g.getAttribute('data-end') === '1' ? 30 : 0)) + '%';
    if (n === 4 && g.getAttribute('data-done') !== '1') g.setAttribute('data-done', '1');
  }
  flips.forEach(function (f) {
    f.addEventListener('click', function () {
      var was = opened();
      f.classList.toggle('open');
      f.setAttribute('aria-pressed', f.classList.contains('open') ? 'true' : 'false');
      draw();
      if (was < 4 && opened() === 4 && window.pengessoPop) {
        var k = f.getBoundingClientRect();
        window.pengessoPop(k.left + k.width / 2, k.top + k.height / 2, ['🔍', '💡', '🐧'], 12);
      }
    });
  });
  g.querySelector('.give').addEventListener('click', function () {
    loops = Math.min(loops + 1, 9);
    ln.textContent = String(loops);
    g.setAttribute('data-loop', String(Math.min(loops, 3)));
    mark.textContent = loops >= 3 ? '😤' : '💬';
    restart(bub, 'boing'); restart(spin, 'go');
    if (navigator.vibrate) { try { navigator.vibrate(20); } catch (e) {} }
  });
  g.querySelector('.say-no').addEventListener('click', function (e) {
    g.setAttribute('data-end', '1');
    mark.textContent = '💨';
    draw();
    if (window.pengessoPop) {
      var k = e.currentTarget.getBoundingClientRect();
      window.pengessoPop(k.left + k.width / 2, k.top + k.height / 2, ['🛡️', '🐧', '✨', '💪'], 18);
    }
  });
  g.querySelector('.reset').addEventListener('click', function () {
    flips.forEach(function (f) { f.classList.remove('open'); f.setAttribute('aria-pressed', 'false'); });
    loops = 0; ln.textContent = '0'; mark.textContent = '💬';
    g.setAttribute('data-done', '0'); g.setAttribute('data-loop', '0'); g.setAttribute('data-end', '0');
    draw();
  });
  draw();
})();