/* 🪙 コインのリレー：ボタンを押すたびにコインが次の人へ動き、その人に「ありがとう」が灯る。JS は data-* と class と数字だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var go = g.querySelector('.go'), again = g.querySelector('.again'), n = g.querySelector('.ty-n');
  var coin = g.querySelector('.coin'), st = [].slice.call(g.querySelectorAll('.st'));
  var step = 0;
  function pop(el, list, k) {
    if (!window.pengessoPop) return;
    var b = el.getBoundingClientRect();
    window.pengessoPop(b.left + b.width / 2, b.top + b.height / 2, list, k);
  }
  go.addEventListener('click', function () {
    if (g.getAttribute('data-s') !== 'play') return;
    step++;
    var at = step % 4;
    g.setAttribute('data-at', at);
    coin.classList.remove('spin'); void coin.offsetWidth; coin.classList.add('spin');
    st[at].classList.remove('lit'); void st[at].offsetWidth; st[at].classList.add('lit');
    n.textContent = step;
    if (step >= 4) {
      g.setAttribute('data-s', 'done');
      setTimeout(function () { pop(coin, ['🪙', '💛', '🥐', '🐧', '✨'], 18); }, 450);
      if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
    } else {
      g.setAttribute('data-step', step);
      pop(st[at], ['💛'], 6);
    }
  });
  again.addEventListener('click', function () {
    step = 0; n.textContent = '0';
    st.forEach(function (s) { s.classList.remove('lit'); });
    g.setAttribute('data-at', '0'); g.setAttribute('data-step', '0'); g.setAttribute('data-s', 'play');
  });
})();