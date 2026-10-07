/* 🌳 チャンスの木：JS は data-* / class / style(--g) / 絵文字 / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var MAXN = 9, RIPE = [3, 6, 9], EMOJI = ['🏸', '☕', '📚'];
  var garden = g.querySelector('.garden'), tree = g.querySelector('.tree'), nChat = g.querySelector('.n-chat');
  var fruits = [].slice.call(g.querySelectorAll('.fruit')), slots = [].slice.call(g.querySelectorAll('.ch'));
  var flies = [].slice.call(g.querySelectorAll('.fly'));
  var n = 0, picked = [false, false, false];
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function draw() {
    garden.style.setProperty('--g', String(n / MAXN));
    nChat.textContent = n;
    g.setAttribute('data-n', String(n));
    var ripe = false;
    fruits.forEach(function (f, i) {
      var on = n >= RIPE[i] && !picked[i];
      f.classList.toggle('ripe', on); f.disabled = !on;
      if (on) ripe = true;
    });
    slots.forEach(function (s, i) { s.classList.toggle('open', picked[i]); });
    var done = picked[0] && picked[1] && picked[2];
    g.setAttribute('data-done', done ? '1' : '0');
    g.setAttribute('data-hint', done ? 'done' : ripe ? 'ripe' : n ? 'grow' : 'start');
  }
  [].forEach.call(g.querySelectorAll('.place'), function (b) {
    b.addEventListener('click', function () {
      var p = +b.getAttribute('data-p');
      flies[p].textContent = EMOJI[p];
      restart(flies[p], 'go');
      if (n < MAXN) { n++; restart(tree, 'grow'); }
      draw();
    });
  });
  fruits.forEach(function (f) {
    f.addEventListener('click', function () {
      var i = +f.getAttribute('data-i');
      if (!f.classList.contains('ripe')) return;
      var r = f.getBoundingClientRect();
      picked[i] = true;
      draw();
      if (window.pengessoPop) {
        var all = picked[0] && picked[1] && picked[2];
        window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, all ? ['🍎', '🍊', '🍋', '🐧', '✨'] : [f.textContent, '✨', '💬'], all ? 22 : 10);
      }
    });
  });
  g.querySelector('.reset').addEventListener('click', function () {
    n = 0; picked = [false, false, false];
    draw();
  });
  draw();
})();