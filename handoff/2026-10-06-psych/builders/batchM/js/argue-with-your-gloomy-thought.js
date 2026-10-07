
/* 📓 3ステップ・ノート：JS は data-*・class・style（メーター）・絵文字・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var bar = g.querySelector('.m-bar i'), pc = g.querySelector('.m-pc'), face = g.querySelector('.m-face'), scn = g.querySelector('.sc-n');
  var c = 1, done = 0;
  function mood(v) {
    bar.style.width = v + '%'; pc.textContent = String(v);
    face.textContent = v <= 15 ? '😣' : v <= 30 ? '😞' : '😊';
    face.classList.remove('pop'); void face.offsetWidth; face.classList.add('pop');
  }
  function page(n) {
    c = n; g.setAttribute('data-c', String(c)); g.setAttribute('data-w', '');
    [].forEach.call(g.querySelectorAll('.opt'), function (o) { o.classList.remove('pick-ok', 'pick-bad', 'shake'); });
    mood(20);
  }
  [].forEach.call(g.querySelectorAll('.opt'), function (o) {
    o.addEventListener('click', function () {
      if (g.getAttribute('data-w') === 'ok') return;
      var k = o.getAttribute('data-k');
      g.setAttribute('data-w', k);
      if (k === 'ok') {
        o.classList.add('pick-ok'); mood(85);
        done++; scn.textContent = String(done);
        scn.classList.remove('pop'); void scn.offsetWidth; scn.classList.add('pop');
        var r = o.getBoundingClientRect();
        if (done >= 3) {
          g.setAttribute('data-all', '1');
          if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🌤️', '📓', '🐧', '✨', '🎯'], 24);
        } else if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🎯', '✨', '📓'], 12);
        if (navigator.vibrate) { try { navigator.vibrate(25); } catch (e) {} }
      } else {
        o.classList.remove('shake'); void o.offsetWidth; o.classList.add('pick-bad', 'shake');
        mood(k === 'agree' ? 10 : 20);
      }
    });
  });
  g.querySelector('.b-next').addEventListener('click', function () { if (c < 3) page(c + 1); });
  g.querySelector('.b-reset').addEventListener('click', function () {
    done = 0; scn.textContent = '0'; g.setAttribute('data-all', '0'); page(1);
  });
  page(1);
})();
