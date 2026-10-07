/* ⏳ やりたいことタイムマシン：JS は data-y / data-r / data-st / class / style / 数字 / disabled だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var RATE = [0.03, 0.045, 0.035, 0.022];
  var wishes = [].slice.call(g.querySelectorAll('.wish'));
  var yn = g.querySelector('.yn'), say = g.querySelector('.say');
  var minus = g.querySelector('.minus'), plus = g.querySelector('.plus');
  var y = 0, pinned = [false, false, false, false];
  function restart(el, c) { el.classList.remove(c); void el.offsetWidth; el.classList.add(c); }
  function draw() {
    yn.textContent = String(y); g.setAttribute('data-y', String(y));
    var anyGone = false, anyLow = false, all = true;
    wishes.forEach(function (w, i) {
      var f = pinned[i] ? 1 : Math.max(0, 1 - RATE[i] * y);
      var st = pinned[i] ? 'pin' : f <= 0 ? 'gone' : 'ok';
      w.setAttribute('data-st', st);
      w.querySelector('.want i').style.width = (f * 100) + '%';
      w.querySelector('.bal').style.transform = 'scale(' + (0.4 + 0.6 * f).toFixed(3) + ')';
      var p = w.querySelector('.pin');
      p.setAttribute('aria-pressed', pinned[i] ? 'true' : 'false');
      p.disabled = st === 'gone';
      if (!pinned[i]) all = false;
      if (st === 'gone') anyGone = true; else if (f < 0.6) anyLow = true;
    });
    var r = all ? 'all' : anyGone ? 'gone' : anyLow ? 'fade' : 'start';
    if (r !== g.getAttribute('data-r')) { g.setAttribute('data-r', r); restart(say, 'show'); }
    minus.disabled = y <= 0; plus.disabled = y >= 40;
    return r;
  }
  draw();
  plus.addEventListener('click', function () { if (y < 40) { y += 5; draw(); restart(yn, 'tick'); } });
  minus.addEventListener('click', function () { if (y > 0) { y -= 5; draw(); restart(yn, 'tick'); } });
  wishes.forEach(function (w, i) {
    w.querySelector('.pin').addEventListener('click', function () {
      if (w.getAttribute('data-st') === 'gone') return;
      pinned[i] = !pinned[i];
      var r = draw();
      if (!pinned[i] || !window.pengessoPop) return;
      var b = w.querySelector('.bal').getBoundingClientRect(), x = b.left + b.width / 2, yy = b.top + b.height / 2;
      if (r === 'all') window.pengessoPop(x, yy, ['📌', '🎈', '🐧', '✨', '🌌'], 24);
      else window.pengessoPop(x, yy, ['📌', '✨', w.querySelector('.bal').textContent], 10);
    });
  });
  g.querySelector('.reset').addEventListener('click', function () {
    y = 0; pinned = [false, false, false, false]; draw();
  });
})();