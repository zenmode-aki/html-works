/* 📚 本棚クイズ：今の悩みに合う本を押すと、木がぐんと育って次の悩みへ。合わない本は「いつか」の付箋。JS は data-* と class と style と数字と絵文字だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var books = [].slice.call(g.querySelectorAll('.book')), bar = g.querySelector('.grow-bar i'), tr = g.querySelector('.tr');
  var sn = g.querySelector('.sn'), again = g.querySelector('.again');
  var TREE = ['🌱', '🌿', '🪴', '🌳'];
  var q = 0, grow = 0, busy = false;
  function draw() {
    g.setAttribute('data-q', q); sn.textContent = q; tr.textContent = TREE[q];
    bar.style.width = grow + '%';
  }
  books.forEach(function (b) {
    b.addEventListener('click', function () {
      if (busy || q >= 3) return;
      books.forEach(function (x) { x.classList.remove('later'); });
      if (+b.getAttribute('data-k') === q) {
        busy = true;
        b.classList.remove('ok'); void b.offsetWidth; b.classList.add('ok');
        g.setAttribute('data-fb', 'ok');
        grow = Math.min(100, grow + 30 + (q === 2 ? 10 : 0));
        bar.style.width = grow + '%';
        tr.textContent = TREE[q + 1]; tr.classList.remove('grow'); void tr.offsetWidth; tr.classList.add('grow');
        if (window.pengessoPop) {
          var k = b.getBoundingClientRect();
          window.pengessoPop(k.left + k.width / 2, k.top + k.height / 2, ['✨', '🌱', '📚'], 10);
        }
        setTimeout(function () {
          b.classList.remove('ok');
          q++; g.removeAttribute('data-fb'); draw(); busy = false;
          if (q === 3) {
            if (window.pengessoPop) {
              var t = tr.getBoundingClientRect();
              window.pengessoPop(t.left + t.width / 2, t.top + t.height / 2, ['🌳', '📚', '🐧', '✨'], 18);
            }
            if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
          }
        }, 1100);
      } else {
        void b.offsetWidth; b.classList.add('later');
        g.setAttribute('data-fb', 'later');
        grow = Math.min(100, grow + 2);
        bar.style.width = grow + '%';
      }
    });
  });
  again.addEventListener('click', function () {
    q = 0; grow = 0; g.removeAttribute('data-fb');
    books.forEach(function (x) { x.classList.remove('later', 'ok'); });
    draw();
  });
  draw();
})();