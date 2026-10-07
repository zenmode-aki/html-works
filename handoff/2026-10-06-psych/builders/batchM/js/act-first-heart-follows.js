
/* 🛗 気分エレベーター：JS は data-*・class・絵文字・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var fls = [].slice.call(g.querySelectorAll('.fl')), pg = g.querySelector('.pg'), face = g.querySelector('.face'), mv = g.querySelector('.mv');
  var FACE = ['😞', '😐', '🙂', '😊', '😆'];
  var floor = 0, moves = 0;
  function paint() {
    fls.forEach(function (f) { f.classList.toggle('on', parseInt(f.getAttribute('data-n'), 10) === floor); });
    face.textContent = FACE[floor];
    face.classList.remove('pop'); void face.offsetWidth; face.classList.add('pop');
    g.setAttribute('data-f', String(floor));
    mv.textContent = String(moves);
  }
  function play(a) { pg.className = 'pg'; void pg.offsetWidth; pg.className = 'pg a' + a; }
  [].forEach.call(g.querySelectorAll('.act'), function (b) {
    b.addEventListener('click', function () {
      var a = parseInt(b.getAttribute('data-a'), 10);
      moves++;
      play(a);
      if (a === 4) { floor = Math.max(0, floor - 1); g.setAttribute('data-top', '0'); g.setAttribute('data-a', '4'); }
      else {
        floor = Math.min(4, floor + 1);
        if (floor === 4) {
          g.setAttribute('data-a', '5');
          if (g.getAttribute('data-top') !== '1') {
            g.setAttribute('data-top', '1');
            if (window.pengessoPop) { var r = pg.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['☀️', '🎵', '🐧', '✨', '🌅'], 20); }
            if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
          }
        } else { g.setAttribute('data-a', String(a)); }
      }
      paint();
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    floor = 0; moves = 0; pg.className = 'pg';
    g.setAttribute('data-a', '0'); g.setAttribute('data-top', '0'); paint();
  });
  paint();
})();
