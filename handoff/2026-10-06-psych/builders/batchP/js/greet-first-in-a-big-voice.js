/* 📣 不機嫌雲パトロール：JS は data-s / class / style / 絵文字 だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var NEED = 8, TIME = 4600;
  var btn = g.querySelector('.tapbig'), bar = g.querySelector('.bar i'), cloud = g.querySelector('.cloud');
  var ce = g.querySelector('.ce'), me = g.querySelector('.me'), face = g.querySelector('.me .t'), hello = g.querySelector('.hello'), mad = g.querySelector('.mad');
  var taps = 0, t0 = 0, raf = 0, skip = false;
  function now() { return (window.performance && performance.now) ? performance.now() : Date.now(); }
  function set(s) { g.setAttribute('data-s', s); }
  function drawVoice() {
    var p = Math.min(1, taps / NEED);
    bar.style.width = (p * 100) + '%';
    me.style.transform = 'scale(' + (1 + p * 0.35) + ')';
    hello.style.transform = 'scale(' + (taps ? 0.75 + p * 0.55 : 0) + ')';
    face.textContent = p >= 1 ? '😄' : p >= 0.5 ? '🙂' : '😶';
  }
  function place(x) { cloud.style.left = x + '%'; }
  function reset() {
    cancelAnimationFrame(raf); taps = 0; drawVoice();
    ce.textContent = '🌩️'; mad.textContent = '💢'; place(-2);
  }
  function tick() {
    var k = (now() - t0) / TIME;           /* 0 → 1：左のはしから、あなたの上（右から3番目の位置）まで */
    place(-2 + Math.min(1, k) * 85);
    if (k >= 1) { set('miss'); mad.textContent = '💢'; return; }
    raf = requestAnimationFrame(tick);
  }
  function start() {
    reset(); set('run'); t0 = now(); raf = requestAnimationFrame(tick);
  }
  function win() {
    cancelAnimationFrame(raf); set('win');
    ce.textContent = '☁️'; mad.textContent = '😳';
    if (window.pengessoPop) {
      var k = btn.getBoundingClientRect();
      window.pengessoPop(k.left + k.width / 2, k.top, ['☀️', '📣', '🐧', '✨'], 18);
    }
    if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
  }
  function hit() {
    taps++; drawVoice();
    if (taps >= NEED) win();
  }
  btn.addEventListener('pointerdown', function () {
    if (g.getAttribute('data-s') !== 'run') return;
    skip = true; hit();                       /* 連打は指が触れた瞬間に数える */
  });
  btn.addEventListener('click', function () {
    if (skip) { skip = false; return; }
    var s = g.getAttribute('data-s');
    if (s === 'run') hit(); else start();
  });
  reset();
})();