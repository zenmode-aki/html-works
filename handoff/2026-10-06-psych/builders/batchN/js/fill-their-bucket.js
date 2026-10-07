/* 🪣 バケツに水を注ごう：JS は data-* / class / style / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var fr = g.querySelector('.t-fr'), me = g.querySelector('.t-me'), ret = g.querySelector('.ret');
  var a = 20, b = 20, timer = 0;
  function restart(el, c) { el.classList.remove(c); void el.offsetWidth; el.classList.add(c); }
  function clamp(v) { return Math.max(0, Math.min(100, v)); }
  function paint(t, v) {
    t.querySelector('.water').style.height = v + '%';
    t.querySelector('.n').textContent = String(v);
    t.classList.toggle('full', v >= 100);
  }
  function draw() { paint(fr, a); paint(me, b); }
  function finishCheck(btn) {
    if (a >= 100 && b >= 100 && g.getAttribute('data-s') !== 'done') {
      g.setAttribute('data-s', 'done');
      if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
      if (window.pengessoPop) { var r = g.querySelector('.tanks').getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 3, ['💧', '🎉', '🐧', '💙', '✨'], 22); }
      return true;
    }
    return false;
  }
  [].slice.call(g.querySelectorAll('.pour')).forEach(function (btn) {
    btn.addEventListener('click', function () {
      if (g.getAttribute('data-s') === 'done') {
        if (window.pengessoPop) { var q = btn.getBoundingClientRect(); window.pengessoPop(q.left + q.width / 2, q.top, ['💧', '💙'], 8); }
        return;
      }
      clearTimeout(timer);
      var overflow = a >= 100;
      a = clamp(a + 20);
      restart(fr.querySelector('.drop'), 'fall');
      draw();
      if (finishCheck(btn)) return;
      g.setAttribute('data-s', overflow ? 'over' : 'give');
      timer = setTimeout(function () {
        b = clamp(b + (overflow ? 25 : 15));
        restart(ret, 'fly'); restart(me.querySelector('.drop'), 'fall');
        draw();
        finishCheck(btn);
      }, 420);
      if (window.pengessoPop) { var r = btn.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top, ['💧'], 5); }
    });
  });
  g.querySelector('.mean').addEventListener('click', function () {
    clearTimeout(timer);
    a = clamp(a - 15); b = clamp(b - 15);
    draw(); restart(fr, 'shake'); restart(me, 'shake');
    g.setAttribute('data-s', 'mean');
  });
  g.querySelector('.reset').addEventListener('click', function () {
    clearTimeout(timer); a = 20; b = 20; draw(); g.setAttribute('data-s', 'idle');
  });
  draw();
})();