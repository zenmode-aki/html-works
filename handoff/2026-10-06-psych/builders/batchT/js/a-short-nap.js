/* ⏰ 昼寝アラーム：1秒＝10分で時計が進む。止めた分数で結果を出す。JS は data-s / data-r と数字と style だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var btn = g.querySelector('.wakebtn'), mm = g.querySelector('.mm'), marker = g.querySelector('.marker');
  var face = g.querySelector('.bed .face'), sn = g.querySelector('.sn');
  var MAX = 90, PER_SEC = 10, t0 = 0, raf = 0, mins = 0, streak = 0, skip = false;
  function now() { return (window.performance && performance.now) ? performance.now() : Date.now(); }
  function set(s, r) { g.setAttribute('data-s', s); g.setAttribute('data-r', r || ''); }
  function show(m) {
    mm.textContent = Math.floor(m);
    marker.style.left = (Math.min(m, MAX) / MAX * 100) + '%';
  }
  function tick() {
    mins = (now() - t0) / 1000 * PER_SEC;
    if (mins >= MAX) { mins = MAX; show(mins); finish(); return; }
    show(mins);
    raf = requestAnimationFrame(tick);
  }
  function start() {
    set('run'); mins = 0; show(0); t0 = now();
    raf = requestAnimationFrame(tick);
  }
  function finish() {
    if (g.getAttribute('data-s') !== 'run') return;
    cancelAnimationFrame(raf);
    var m = Math.floor(mins);
    var r = m < 10 ? 'short' : m <= 25 ? 'good' : m < 50 ? 'heavy' : 'long';
    show(m);
    face.textContent = r === 'good' ? '😊' : r === 'short' ? '🙂' : r === 'heavy' ? '😪' : '😵';
    streak = r === 'good' ? streak + 1 : 0;
    sn.textContent = streak;
    set('done', r);
    if (r === 'good' && window.pengessoPop) {
      var k = btn.getBoundingClientRect();
      window.pengessoPop(k.left + k.width / 2, k.top + k.height / 2, ['🔋', '⏰', '🐧', '✨'], 16);
      if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
    }
  }
  btn.addEventListener('pointerdown', function () {
    if (g.getAttribute('data-s') !== 'run') return;
    skip = true; finish();   /* 指が触れた瞬間に止める */
  });
  btn.addEventListener('click', function () {
    if (skip) { skip = false; return; }
    var s = g.getAttribute('data-s');
    if (s === 'run') finish();
    else start();
  });
})();