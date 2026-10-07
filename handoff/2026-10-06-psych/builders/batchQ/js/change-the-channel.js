/* 📺 リモコン：JS は data-ch・data-w・class・高さ・数字・絵文字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var fill = g.querySelector('.wtube i'), num = g.querySelector('.wnum'), face = g.querySelector('.wface');
  var chs = [].slice.call(g.querySelectorAll('.ch'));
  var worry = 0, ch = 0, timer = 0;
  function draw() {
    fill.style.height = worry + '%';
    num.textContent = String(Math.round(worry));
    face.textContent = worry >= 85 ? '😵' : worry >= 50 ? '😟' : worry > 0 ? '😐' : '😊';
  }
  function setW(w) { if (g.getAttribute('data-w') !== w) g.setAttribute('data-w', w); }
  function tick() {
    if (ch === 1) { worry = Math.min(100, worry + 3); setW(worry >= 100 ? 'max' : 'up'); }
    else {
      worry = Math.max(0, worry - 5); setW('down');
      if (worry === 0) {
        clearInterval(timer); timer = 0; setW('win');
        if (window.pengessoPop) { var r = g.querySelector('.screen').getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['😊', '✈️', '🐧', '✨'], 16); }
        if (navigator.vibrate) { try { navigator.vibrate(25); } catch (e) {} }
      }
    }
    draw();
  }
  function tune(c) {
    ch = c; g.setAttribute('data-ch', String(c));
    chs.forEach(function (b) { b.classList.toggle('on', +b.getAttribute('data-c') === c); });
    if (g.getAttribute('data-w') === 'win') return;
    if (!timer) timer = setInterval(tick, 250);
    tick();
  }
  g.querySelector('.power').addEventListener('click', function () { worry = 45; tune(1); });
  chs.forEach(function (b) { b.addEventListener('click', function () { tune(+b.getAttribute('data-c')); }); });
  g.querySelector('.again').addEventListener('click', function () {
    clearInterval(timer); timer = 0; worry = 0; ch = 0;
    g.setAttribute('data-ch', '0'); setW('idle');
    chs.forEach(function (b) { b.classList.remove('on'); });
    draw();
  });
  draw();
})();