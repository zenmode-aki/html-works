/* ⏱️ サインを読もう：JS は data-t / data-p / data-f / class / style の幅 / 絵文字 / 数字だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var SLOW = [false, true, false, true];
  var SEC = [0.4, 2.6, 0.3, 2.2];
  var order = [0, 1, 2, 3], r = 0, score = 0, timer = 0, t0 = 0, raf = 0;
  var bar = g.querySelector('.sp-bar i'), secN = g.querySelector('.sec-n'), react = g.querySelector('.react');
  var stars = [].slice.call(g.querySelectorAll('.stars i')), rdN = g.querySelector('.rd-n'), bigN = g.querySelector('.big-n');
  function shuffle() { for (var k = order.length - 1; k > 0; k--) { var j = Math.floor(Math.random() * (k + 1)), x = order[k]; order[k] = order[j]; order[j] = x; } if (SLOW[order[0]]) { order.push(order.shift()); } }
  function setP(p) { g.setAttribute('data-p', p); }
  function startRound() {
    var t = order[r];
    g.setAttribute('data-t', String(t)); g.setAttribute('data-f', ''); setP('q');
    bar.style.width = '0'; secN.textContent = '0.0'; react.textContent = '🙂';
    rdN.textContent = (r + 1) + '/4';
  }
  function tick() {
    var t = order[r], s = Math.min(SEC[t], ((window.performance ? performance.now() : Date.now()) - t0) / 1000);
    secN.textContent = s.toFixed(1);
    bar.style.width = Math.min(100, s / 3 * 100) + '%';
    if (s < SEC[t]) raf = requestAnimationFrame(tick);
  }
  g.querySelector('.ask').addEventListener('click', function () {
    var t = order[r];
    setP('wait'); react.textContent = SLOW[t] ? '😶' : '😃';
    t0 = window.performance ? performance.now() : Date.now();
    cancelAnimationFrame(raf); raf = requestAnimationFrame(tick);
    clearTimeout(timer);
    timer = setTimeout(function () {
      cancelAnimationFrame(raf);
      secN.textContent = SEC[t].toFixed(1); bar.style.width = Math.min(100, SEC[t] / 3 * 100) + '%';
      react.textContent = SLOW[t] ? '😅' : '😄';
      setP('ans');
    }, SEC[t] * 1000);
  });
  function judge(dig) {
    var t = order[r], ok = dig ? !SLOW[t] : SLOW[t];
    g.setAttribute('data-f', (dig ? 'dig' : 'chg') + (ok ? '-ok' : '-bad'));
    setP('fb');
    if (ok) score++;
    stars[r].classList.add(ok ? 'ok' : 'ng'); stars[r].textContent = ok ? '⭐' : '💦';
    react.textContent = ok ? (dig ? '🤩' : '😌') : (dig ? '😣' : '🙁');
    if (ok && window.pengessoPop) { var b = stars[r].getBoundingClientRect(); window.pengessoPop(b.left + b.width / 2, b.top + b.height / 2, ['⭐', '✨'], 8); }
  }
  g.querySelector('.dig').addEventListener('click', function () { judge(true); });
  g.querySelector('.chg').addEventListener('click', function () { judge(false); });
  g.querySelector('.nextb').addEventListener('click', function () {
    r++;
    if (r >= 4) {
      bigN.textContent = score + '/4'; setP('end');
      if (score === 4 && window.pengessoPop) { var b = bigN.getBoundingClientRect(); window.pengessoPop(b.left + b.width / 2, b.top + b.height / 2, ['🏆', '🐧', '⭐', '✨'], 22); }
      return;
    }
    startRound();
  });
  g.querySelector('.reset').addEventListener('click', function () {
    clearTimeout(timer); cancelAnimationFrame(raf);
    r = 0; score = 0; shuffle();
    stars.forEach(function (s) { s.className = ''; s.textContent = '⭐'; });
    startRound();
  });
  shuffle(); startRound();
})();