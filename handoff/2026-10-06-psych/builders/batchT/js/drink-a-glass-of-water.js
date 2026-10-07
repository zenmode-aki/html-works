/* 💧 不機嫌の理由を選ぶ → 水なら4口飲んで、ごきげんメーターが上がる。JS は data-* / class / 数字 / 絵文字 / style だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var mood = g.querySelector('.who .mood'), bubble = g.querySelector('.bubble'), bar = g.querySelector('.meter i');
  var choices = g.querySelectorAll('.choices .gbtn'), sip = g.querySelector('.sip'), water = g.querySelector('.cup .water');
  var cup = g.querySelector('.cup'), sn = g.querySelector('.sn'), again = g.querySelector('.again');
  var FACES = ['😤', '😐', '🙂', '😊', '😄'], SIPS = 4, n = 0;
  function bump(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function face(i) { mood.textContent = FACES[i]; bump(mood, 'boing'); }
  function state(s, t) { g.setAttribute('data-s', s); g.setAttribute('data-t', t || ''); bump(bubble, 'swap'); }
  function render() {
    sn.textContent = n;
    water.style.height = (88 - n * 22) + '%';
    bar.style.width = (10 + n * 22.5) + '%';
  }
  for (var i = 0; i < choices.length; i++) {
    choices[i].addEventListener('click', function () {
      var c = this.getAttribute('data-c');
      if (c === 'water') { state('drink'); face(0); return; }
      this.classList.add('tried');
      g.setAttribute('data-t', '');
      state('ask', c);
      face(0);
    });
  }
  sip.addEventListener('click', function () {
    if (n >= SIPS) return;
    n++;
    render(); face(n); bump(cup, 'gulp');
    if (n >= SIPS) {
      state('done');
      if (window.pengessoPop) {
        var r = cup.getBoundingClientRect();
        window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['💧', '✨', '🐧', '😊'], 16);
      }
      if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
    }
  });
  again.addEventListener('click', function () {
    n = 0; render();
    for (var j = 0; j < choices.length; j++) choices[j].classList.remove('tried');
    state('ask'); face(0);
  });
  render();
})();