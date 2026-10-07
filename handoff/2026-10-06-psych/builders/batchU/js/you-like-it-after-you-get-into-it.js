/* 🧩 パズル：ピースを押すと枠にはまる。「好き」メーターは最初は0のまま → 後半で一気に上がる。JS は data-* と style と絵文字だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var work = g.querySelector('.work'), slots = [].slice.call(g.querySelectorAll('.slot'));
  var pieces = [].slice.call(g.querySelectorAll('.piece')), tray = g.querySelector('.tray');
  var wbar = g.querySelector('.b-work .track i'), lbar = g.querySelector('.b-like .track i');
  var face = g.querySelector('.pface'), again = g.querySelector('.again');
  var LIKE = [0, 0, 5, 25, 60, 85, 100], FACE = ['😐', '😐', '🤔', '🤔', '🙂', '😄', '😍'], SAY = [0, 1, 1, 2, 3, 3, 4];
  var n = 0;
  function draw() {
    wbar.style.width = (n / 6 * 100) + '%';
    lbar.style.width = LIKE[n] + '%';
    face.textContent = FACE[n];
    work.setAttribute('data-l', SAY[n]);
    face.classList.remove('hop'); void face.offsetWidth; face.classList.add('hop');
  }
  pieces.forEach(function (p) {
    p.addEventListener('click', function () {
      if (p.getAttribute('data-used') === '1') return;
      p.setAttribute('data-used', '1');
      slots[+p.getAttribute('data-to')].setAttribute('data-on', '1');
      n++; draw();
      if (n === 6) {
        g.setAttribute('data-done', '1');
        if (window.pengessoPop) {
          var k = work.getBoundingClientRect();
          window.pengessoPop(k.left + k.width / 2, k.top + k.height / 3, ['🧩', '💖', '🐧', '✨'], 18);
        }
        if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
      }
    });
  });
  again.addEventListener('click', function () {
    n = 0;
    slots.forEach(function (s) { s.removeAttribute('data-on'); });
    pieces.sort(function () { return Math.random() - 0.5; }).forEach(function (p) { p.removeAttribute('data-used'); tray.appendChild(p); });
    g.setAttribute('data-done', '0');
    draw();
  });
})();