/* 🧱 ていねいの壁：レンガを押すと崩れて、下に気さくな言葉が1つ出る。2羽が近づき、仲良し度が上がる。JS は data-* と class と幅と絵文字だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var bs = [].slice.call(g.querySelectorAll('.brk')), chips = [].slice.call(g.querySelectorAll('.chip'));
  var fl = g.querySelector('.pg-l .pg-f'), fr = g.querySelector('.pg-r .pg-f'), bar = g.querySelector('.cl-bar i'), again = g.querySelector('.again');
  var n = 0, FACE = ['😐', '🙂', '🙂', '😊', '😄', '😆'];
  function pop(el, list, k) {
    if (!window.pengessoPop) return;
    var r = el.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, k);
  }
  bs.forEach(function (b) {
    b.addEventListener('click', function () {
      if (b.classList.contains('gone')) return;
      pop(b, ['🧱', '💨'], 6);
      b.classList.add('gone'); b.setAttribute('aria-hidden', 'true'); b.tabIndex = -1;
      chips[n].classList.add('on');
      n++;
      g.setAttribute('data-n', n);
      fl.textContent = FACE[n]; fr.textContent = FACE[n];
      bar.style.width = (n * 20) + '%';
      if (n >= bs.length) {
        g.setAttribute('data-s', 'done');
        setTimeout(function () { pop(g.querySelector('.field'), ['🐧', '💛', '💬', '✨'], 18); }, 450);
        if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
      }
    });
  });
  again.addEventListener('click', function () {
    n = 0; bar.style.width = '0'; fl.textContent = FACE[0]; fr.textContent = FACE[0];
    bs.forEach(function (b) { b.classList.remove('gone'); b.removeAttribute('aria-hidden'); b.tabIndex = 0; });
    chips.forEach(function (c) { c.classList.remove('on'); });
    g.setAttribute('data-n', '0'); g.setAttribute('data-s', 'play');
  });
})();