/* 🚲 練習を1回するたびにレベルが上がり、走った線のグラグラが小さくなる。8回目で補助輪がはずれる。JS は data-lv / class / 数字 / style / svg の線だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var btn = g.querySelector('.practice'), again = g.querySelector('.again'), lvEl = g.querySelector('.lv');
  var rungs = g.querySelectorAll('.ladder i'), rider = g.querySelector('.rider'), wob = g.querySelector('.wob');
  var trail = g.querySelector('.trail'), said = g.querySelector('.said'), wm = g.querySelector('.wmeter i');
  var MAX = 8, lv = 0;
  function bump(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function line(amp) {   /* 左から右へ。amp が大きいほどグラグラ */
    var d = 'M10,92', x = 10, up = true;
    for (var i = 0; i < 8; i++) {
      var nx = x + 35, cy = 92 + (up ? -amp : amp) * (0.7 + Math.random() * 0.6);
      d += ' Q' + (x + 17.5) + ',' + cy.toFixed(1) + ' ' + nx + ',92';
      x = nx; up = !up;
    }
    trail.setAttribute('d', d);
  }
  function render(ride) {
    g.setAttribute('data-lv', lv);
    lvEl.textContent = lv;
    for (var i = 0; i < rungs.length; i++) rungs[i].classList.toggle('on', i < lv);
    var left = 1 - lv / MAX;
    wm.style.width = Math.max(4, left * 100) + '%';
    wob.style.setProperty('--w', (2 + left * 16) + 'deg');
    line(lv === 0 ? 0 : 3 + left * 34);
    bump(said, 'swap');
    if (ride) bump(rider, 'go');
  }
  btn.addEventListener('click', function () {
    if (lv >= MAX) return;
    lv++;
    render(true);
    if (lv >= MAX) {
      setTimeout(function () {
        if (window.pengessoPop) {
          var r = rider.getBoundingClientRect();
          window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🛞', '🚲', '🐧', '✨', '🎉'], 20);
        }
        if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
      }, 900);
    }
  });
  again.addEventListener('click', function () { lv = 0; rider.classList.remove('go'); render(false); });
  render(false);
})();