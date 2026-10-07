/* 🎧 100回「うんうん」：うんうん1回＝5、速い連打＝10。100になる前に言うと扉が閉じる。JS は data-* と数字と絵文字だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var uh = g.querySelector('.uh'), say = g.querySelector('.say'), again = g.querySelector('.again');
  var ln = g.querySelector('.ln'), bar = g.querySelector('.lmeter i'), face = g.querySelector('.fr-face');
  var pts = 0, last = 0, t = 0, ct = 0;
  function now() { return (window.performance && performance.now) ? performance.now() : Date.now(); }
  function draw() {
    ln.textContent = pts;
    bar.style.width = pts + '%';
    face.textContent = pts >= 100 ? '😊' : pts >= 60 ? '🙂' : pts >= 25 ? '😐' : '😣';
    g.setAttribute('data-full', pts >= 100 ? '1' : '0');
  }
  function nod() { face.classList.remove('nod'); void face.offsetWidth; face.classList.add('nod'); }
  function pop(el, list, n) {
    if (!window.pengessoPop) return;
    var k = el.getBoundingClientRect();
    window.pengessoPop(k.left + k.width / 2, k.top + k.height / 2, list, n);
  }
  uh.addEventListener('click', function () {
    if (g.getAttribute('data-s') !== 'talk') return;
    var n = now(), fast = n - last < 450; last = n;
    var before = pts;
    pts = Math.min(100, pts + (fast ? 10 : 5));
    g.setAttribute('data-combo', fast ? '1' : '0');
    clearTimeout(ct); ct = setTimeout(function () { g.setAttribute('data-combo', '0'); }, 700);
    t = (t + 1) % 4; g.setAttribute('data-t', t);
    draw(); nod();
    if (before < 100 && pts >= 100) pop(face, ['🎧', '💗', '✨'], 10);
  });
  say.addEventListener('click', function () {
    if (g.getAttribute('data-s') !== 'talk') return;
    if (pts < 100) { face.textContent = '😤'; g.setAttribute('data-s', 'early'); return; }
    face.textContent = '😊';
    g.setAttribute('data-s', 'done');
    pop(face, ['🐧', '💗', '✨', '🌙'], 16);
    if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
  });
  again.addEventListener('click', function () {
    pts = 0; t = 0; last = 0;
    g.setAttribute('data-t', '0'); g.setAttribute('data-combo', '0'); g.setAttribute('data-s', 'talk');
    draw();
  });
})();