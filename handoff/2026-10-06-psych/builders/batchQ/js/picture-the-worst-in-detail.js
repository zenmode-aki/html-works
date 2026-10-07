/* ☁️ もやもやおばけ：JS は data-n・class・hidden・数字・絵文字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var qs = [].slice.call(g.querySelectorAll('.q'));
  var ans = g.querySelectorAll('.ans');
  var face = g.querySelector('.fface'), num = g.querySelector('.num'), fog = g.querySelector('.fog');
  var FACES = ['😱', '😟', '😐', '🙂'], FOG = ['100', '66', '33', '0'];
  var n = 0;
  function puff() { g.classList.remove('puff'); void g.offsetWidth; g.classList.add('puff'); }
  qs.forEach(function (b) {
    b.addEventListener('click', function () {
      if (b.disabled) return;
      var i = +b.getAttribute('data-q');
      b.disabled = true; b.classList.add('done');
      ans[i].hidden = false;
      n += 1;
      g.setAttribute('data-n', String(n));
      face.textContent = FACES[n]; num.textContent = FOG[n];
      puff();
      if (n === 3) {
        if (window.pengessoPop) {
          var r = fog.getBoundingClientRect();
          window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['☀️', '🐧', '✨', '🔍'], 16);
        }
        if (navigator.vibrate) { try { navigator.vibrate(25); } catch (e) {} }
      }
    });
  });
  g.querySelector('.again').addEventListener('click', function () {
    n = 0; g.setAttribute('data-n', '0'); g.classList.remove('puff');
    face.textContent = FACES[0]; num.textContent = FOG[0];
    qs.forEach(function (b) { b.disabled = false; b.classList.remove('done'); });
    [].forEach.call(ans, function (a) { a.hidden = true; });
  });
})();