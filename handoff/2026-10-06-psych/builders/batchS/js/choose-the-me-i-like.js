/* 🍟 どっちの自分が好き？：JS は data-q / data-a / data-end / data-sc / class / 絵文字 / 数字だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var SCENE = ['🍟', '🛒', '🥤'];
  var q = 1, score = 0;
  var hearts = [].slice.call(g.querySelectorAll('.hearts i'));
  var se = g.querySelector('.scene-e'), qn = g.querySelector('.qn'), peng = g.querySelector('.peng'), pf = g.querySelector('.pf');
  var next = g.querySelector('.nextq');
  function restart(el, c) { el.classList.remove(c); void el.offsetWidth; el.classList.add(c); }
  function draw() {
    g.setAttribute('data-q', String(q));
    qn.textContent = String(q);
    se.textContent = SCENE[q - 1];
    hearts.forEach(function (h, i) { h.classList.toggle('on', i < score); });
  }
  [].slice.call(g.querySelectorAll('.opt')).forEach(function (b) {
    b.addEventListener('click', function () {
      if (g.getAttribute('data-a')) return;
      var v = b.getAttribute('data-v');
      g.setAttribute('data-a', v);
      if (v === 'b') {
        score++; pf.textContent = '😊'; peng.classList.remove('hmm'); restart(peng, 'happy');
        if (window.pengessoPop) { var r = b.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['💛', '🐧', '✨'], 12); }
      } else {
        pf.textContent = '😶'; peng.classList.remove('happy'); restart(peng, 'hmm');
      }
      draw();
    });
  });
  next.addEventListener('click', function () {
    if (q < 3) {
      q++; g.setAttribute('data-a', ''); pf.textContent = '💭';
      peng.classList.remove('happy', 'hmm'); draw();
      return;
    }
    g.setAttribute('data-sc', score === 3 ? '3' : score ? '12' : '0');
    g.setAttribute('data-end', '1');
    if (score === 3 && window.pengessoPop) {
      var r = g.querySelector('.like-row').getBoundingClientRect();
      window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['💛', '🐧', '🎉', '✨'], 22);
    }
  });
  g.querySelector('.reset').addEventListener('click', function () {
    q = 1; score = 0; pf.textContent = '💭'; peng.classList.remove('happy', 'hmm');
    g.setAttribute('data-a', ''); g.setAttribute('data-end', '0'); g.setAttribute('data-sc', '');
    draw();
  });
})();