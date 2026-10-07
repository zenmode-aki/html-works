/* 🏥 待合室：JS は data-s・data-mode・data-res・class・幅・数字・絵文字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var minEl = g.querySelector('.clock .num'), pagesEl = g.querySelector('.pages .num'), bar = g.querySelector('.bar i'), face = g.querySelector('.face');
  var MAD = { plain: [0, 35, 65, 90, 100], expect: [0, 5, 10, 15, 30] };
  var FACE = { plain: ['🙂', '😐', '😒', '😤', '💢'], expect: ['🙂', '🙂', '😊', '😊', '🙂'] };
  var mode = '', min = 0, callAt = 30, last = '';
  function set(k, v) { g.setAttribute(k, v); }
  function pickCall() { var x = Math.random(); return x < 0.15 ? 10 : x < 0.4 ? 20 : x < 0.8 ? 30 : 40; }
  function draw() {
    var step = min / 10;
    bar.style.width = MAD[mode][step] + '%';
    face.textContent = FACE[mode][step];
    minEl.textContent = String(min);
    pagesEl.textContent = String(step * 12);
  }
  [].forEach.call(g.querySelectorAll('.mode'), function (b) {
    b.addEventListener('click', function () {
      mode = b.getAttribute('data-m'); last = mode; min = 0; callAt = pickCall();
      set('data-mode', mode); set('data-res', ''); set('data-s', 'wait'); draw();
    });
  });
  g.querySelector('.wait').addEventListener('click', function () {
    if (min >= 40) return;
    min += 10; draw();
    g.classList.remove('tock'); void g.offsetWidth; g.classList.add('tock');
    if (min >= callAt) {
      var res = mode === 'plain' ? 'plain' : (min < 30 ? 'lucky' : 'calm');
      set('data-res', res); set('data-s', 'done');
      if (res !== 'plain' && window.pengessoPop) {
        var r = g.querySelector('.call').getBoundingClientRect();
        window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, res === 'lucky' ? ['🍀', '🔔', '🐧', '✨'] : ['📖', '🔔', '✨'], res === 'lucky' ? 18 : 10);
      }
      if (navigator.vibrate) { try { navigator.vibrate(25); } catch (e) {} }
    }
  });
  g.querySelector('.again').addEventListener('click', function () {
    mode = last === 'plain' ? 'expect' : 'plain'; min = 0; callAt = pickCall();
    set('data-mode', mode); set('data-res', ''); set('data-s', 'wait'); draw();
  });
})();