/* 🎐 レベルアップ：JS は data-lv / class / style / 絵文字 / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var HURT = [100, 62, 32, 8], YOU = ['😣', '😮', '😌', '😎'], THEM = ['🐧', '🐶', '🐧', '🐧'];
  var steps = [].slice.call(g.querySelectorAll('.step'));
  var bar = g.querySelector('.bar i'), say = g.querySelector('.say');
  var youTag = g.querySelector('.you .tag'), themIc = g.querySelector('.them .ic');
  var noren = g.querySelector('.noren'), shot = g.querySelector('.shot'), tn = g.querySelector('.tn');
  var lv = 0, through = 0;
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function draw() {
    g.setAttribute('data-lv', String(lv));
    steps.forEach(function (s, i) { s.classList.toggle('on', i < lv); });
    bar.style.width = HURT[lv] + '%';
    bar.classList.toggle('calm', lv >= 2);
    youTag.textContent = YOU[lv]; themIc.textContent = THEM[lv];
    tn.textContent = String(through);
  }
  function fire() {
    restart(shot, 'fly');
    setTimeout(function () { restart(noren, 'sway'); }, 420);
    through++; tn.textContent = String(through);
  }
  g.querySelector('.up').addEventListener('click', function (e) {
    if (lv >= 3) { lv = 0; through = 0; draw(); restart(say, 'show'); return; }
    lv++;
    draw(); restart(say, 'show');
    if (lv === 3) {
      setTimeout(fire, 450);
      if (window.pengessoPop) {
        var k = e.currentTarget.getBoundingClientRect();
        window.pengessoPop(k.left + k.width / 2, k.top, ['🎐', '😎', '🐧', '✨'], 18);
      }
    }
  });
  g.querySelector('.send').addEventListener('click', fire);
  draw();
})();