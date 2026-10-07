
/* 🔥 名前スイッチ：JS は data-*・style（🔥 の大きさ・メーター）・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var fire = g.querySelector('.fire'), bar = g.querySelector('.t-bar i'), tn = g.querySelector('.t-n');
  var z = 0, anger = 90;
  function paint() {
    g.setAttribute('data-z', String(z));
    fire.style.fontSize = Math.round(14 + anger * 0.36) + 'px';
    bar.style.width = anger + '%'; tn.textContent = String(anger);
  }
  g.querySelector('.b-i').addEventListener('click', function () {
    z = 0; anger = Math.min(100, anger + 15);
    g.setAttribute('data-b', '4'); g.setAttribute('data-done', '0');
    var v = g.querySelector('.view'); v.classList.remove('shake'); void v.offsetWidth; v.classList.add('shake');
    if (navigator.vibrate) { try { navigator.vibrate(20); } catch (e) {} }
    paint();
  });
  g.querySelector('.b-name').addEventListener('click', function () {
    if (z < 3) z++;
    anger = [90, 60, 35, 12][z];
    g.setAttribute('data-b', String(z));
    paint();
    if (z === 3 && g.getAttribute('data-done') !== '1') {
      g.setAttribute('data-done', '1');
      if (window.pengessoPop) { var r = g.querySelector('.view').getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['😌', '🌏', '🐧', '☁️', '✨'], 20); }
    }
  });
  paint();
})();
