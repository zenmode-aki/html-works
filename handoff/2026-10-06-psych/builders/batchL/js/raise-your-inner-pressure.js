/* 🎈 深海の風船：JS は data-* / style / 絵文字 / 数字だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var ball = g.querySelector('.balloon'), face = g.querySelector('.bf'), dv = g.querySelector('.dv'),
      outBar = g.querySelector('.bar.out i'), inBar = g.querySelector('.bar.in i'), arrs = [].slice.call(g.querySelectorAll('.arr'));
  var d = 1, inn = 1, words = 0;
  function paint() {
    var diff = inn - d, sx = 1, sy = 1, s;
    if (diff < 0) { var k = Math.min(3, -diff); sx = 1 + 0.16 * k; sy = Math.max(0.42, 1 - 0.2 * k); face.textContent = k >= 2 ? '😖' : '😣'; s = 'sq'; }
    else if (diff > 0) { sx = sy = 1.1; face.textContent = '😄'; s = 'big'; }
    else { face.textContent = '😊'; s = 'ok'; }
    if (d === 5 && inn >= 5) { s = 'done'; face.textContent = '😎'; }
    ball.style.setProperty('--sx', sx); ball.style.setProperty('--sy', sy);
    g.setAttribute('data-d', d); g.setAttribute('data-s', s);
    g.setAttribute('data-w', (words % 5) + 1);
    dv.textContent = d * 10;
    outBar.style.width = (d / 6 * 100) + '%';
    inBar.style.width = (Math.min(inn, 6) / 6 * 100) + '%';
    arrs.forEach(function (a) { a.style.setProperty('--p', (0.12 + d * 0.17).toFixed(2)); });
    return s;
  }
  g.querySelector('.dive').addEventListener('click', function () {
    if (d < 5) d++;
    paint();
    if (navigator.vibrate && inn < d) { try { navigator.vibrate(15); } catch (e) {} }
  });
  g.querySelector('.strong').addEventListener('click', function (e) {
    inn = Math.min(d + 1, inn + 1); words++;
    var s = paint();
    if (window.pengessoPop) {
      var r = ball.getBoundingClientRect();
      window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, s === 'done' ? ['🎈', '🏆', '🐧', '✨'] : ['🔥', '✨'], s === 'done' ? 20 : 6);
    }
  });
  g.querySelector('.weak').addEventListener('click', function () { inn = Math.max(0, inn - 1); paint(); });
  g.querySelector('.again').addEventListener('click', function () { d = 1; inn = 1; words = 0; paint(); });
  paint();
})();