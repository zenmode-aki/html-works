/* 🎯 2つの輪：JS は data-i・data-in・data-say・class・hidden・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var ANSWER = ['out', 'in', 'out', 'in', 'out', 'in'];
  var dots = g.querySelectorAll('.dot'), num = g.querySelector('.cnt .num'), rings = g.querySelector('.rings');
  var i = 1, inner = 0;
  function say(v) { g.setAttribute('data-say', ''); void g.offsetWidth; g.setAttribute('data-say', v); }
  [].forEach.call(g.querySelectorAll('.bin'), function (b) {
    b.addEventListener('click', function () {
      if (i > 6) return;
      if (b.getAttribute('data-b') !== ANSWER[i - 1]) {
        g.classList.remove('wrong'); void g.offsetWidth; g.classList.add('wrong');
        say('no'); return;
      }
      dots[i - 1].hidden = false;
      if (ANSWER[i - 1] === 'in') { inner += 1; g.setAttribute('data-in', String(inner)); }
      num.textContent = String(i);
      i += 1; g.setAttribute('data-i', String(i));
      if (i > 6) {
        say('end');
        if (window.pengessoPop) { var r = rings.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🎯', '🌱', '🐧', '✨'], 18); }
        if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
      } else { say('ok'); }
    });
  });
  g.querySelector('.again').addEventListener('click', function () {
    i = 1; inner = 0; num.textContent = '0';
    [].forEach.call(dots, function (d) { d.hidden = true; });
    g.classList.remove('wrong');
    g.setAttribute('data-i', '1'); g.setAttribute('data-in', '0'); say('ask');
  });
})();