/* 🐶 どっちの子犬がかわいい？：JS は data-* / class / disabled だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var wa = g.querySelector('.wa'), wb = g.querySelector('.wb');
  var hA = [].slice.call(wa.querySelectorAll('.whearts i')), hB = [].slice.call(wb.querySelectorAll('.whearts i'));
  var mh = [].slice.call(g.querySelectorAll('.mhearts i'));
  var bWait = g.querySelector('.b-wait'), bGo = g.querySelector('.b-go');
  var a = 0, b = 0;
  function fill(list, k) { list.forEach(function (h, i) { h.classList.toggle('on', i < k); }); }
  function draw() {
    g.setAttribute('data-a', a ? '1' : '0'); g.setAttribute('data-b', b ? '1' : '0');
    fill(hA, Math.min(5, a ? a + 2 : 0)); fill(hB, b ? 1 : 0);
    var un = a && b;
    g.setAttribute('data-unlock', un ? '1' : '0');
    bWait.disabled = !un; bGo.disabled = !un;
  }
  function center(el) { var r = el.getBoundingClientRect(); return [r.left + r.width / 2, r.top + r.height / 2]; }
  wa.addEventListener('click', function () {
    a = Math.min(3, a + 1); draw();
    if (window.pengessoPop) { var c = center(wa); window.pengessoPop(c[0], c[1], ['💖', '🐶', '🐾'], 8); }
  });
  wb.addEventListener('click', function () {
    b = 1; g.setAttribute('data-b', '0'); void g.offsetWidth; draw();
  });
  bWait.addEventListener('click', function () { g.setAttribute('data-me', 'wait'); fill(mh, 0); });
  bGo.addEventListener('click', function () {
    var again = g.getAttribute('data-me') === 'go';
    g.setAttribute('data-me', 'go'); fill(mh, 5);
    if (!again && window.pengessoPop) { var c = center(g.querySelector('.party')); window.pengessoPop(c[0], c[1], ['💖', '🐧', '🐾', '✨'], 20); }
  });
  g.querySelector('.reset').addEventListener('click', function () {
    a = 0; b = 0; g.setAttribute('data-me', ''); fill(mh, 0); draw();
  });
  draw();
})();