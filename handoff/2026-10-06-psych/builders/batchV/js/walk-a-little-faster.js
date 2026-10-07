/* 💨 歩くペースのつまみ：−/＋でペース1〜5。景色の流れる速さ（style）・カフェまでの分数・気分の顔とメーターが変わる。JS は data-* と style と数字と絵文字だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var minus = g.querySelector('.minus'), plus = g.querySelector('.plus'), mn = g.querySelector('.mn'), fe = g.querySelector('.fe');
  var feel = g.querySelector('.feel i'), dots = [].slice.call(g.querySelectorAll('.dots i')), street = g.querySelector('.street');
  var MIN = [0, 20, 15, 12, 10, 8], DUR = [0, 16, 10, 7, 5.5, 3], STEP = [0, 1.1, .7, .5, .4, .25];
  var FEEL = [0, 30, 55, 88, 95, 35], FACE = ['', '😪', '🙂', '😄', '😆', '🥵'];
  var p = 2, found = false;
  function pop(el, list, k) {
    if (!window.pengessoPop) return;
    var b = el.getBoundingClientRect();
    window.pengessoPop(b.left + b.width / 2, b.top + b.height / 2, list, k);
  }
  function draw() {
    g.setAttribute('data-p', p);
    street.style.setProperty('--dur', DUR[p] + 's');
    street.style.setProperty('--step', STEP[p] + 's');
    mn.textContent = MIN[p]; fe.textContent = FACE[p]; feel.style.width = FEEL[p] + '%';
    dots.forEach(function (d, i) { d.classList.toggle('on', i < p); });
    minus.disabled = p <= 1; plus.disabled = p >= 5;
    if ((p === 3 || p === 4) && !found) {
      found = true; g.setAttribute('data-found', '1');
      pop(fe, ['⭐', '🐧', '☕', '✨'], 14);
      if (navigator.vibrate) { try { navigator.vibrate(25); } catch (e) {} }
    }
  }
  minus.addEventListener('click', function () { if (p > 1) { p--; draw(); } });
  plus.addEventListener('click', function () { if (p < 5) { p++; draw(); } });
  draw();
})();