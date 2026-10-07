/* 🐷 仲よし貯金箱：JS は data-* / class / 幅 / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var PER = 3, MAX = 12;
  var coin = g.querySelector('.coin'), paper = g.querySelector('.paper'), pig = g.querySelector('.pig');
  var topic = g.querySelector('.topic'), lvN = g.querySelector('.lv-n'), lvName = g.querySelector('.lv-name');
  var bar = g.querySelector('.lv-bar i'), cN = g.querySelector('.c-n'), stars = [].slice.call(g.querySelectorAll('.stars i'));
  var coins = 0, ui = -1, si = -1;
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function level() { return Math.min(5, 1 + Math.floor(coins / PER)); }
  function draw() {
    var lv = level();
    g.setAttribute('data-lv', String(lv));
    lvN.textContent = lv; cN.textContent = coins;
    bar.style.width = (coins >= MAX ? 100 : (coins % PER) / PER * 100) + '%';
    stars.forEach(function (s, i) { s.classList.toggle('on', i < lv); });
  }
  g.querySelector('.useful').addEventListener('click', function () {
    ui = (ui + 1) % 3;
    g.setAttribute('data-tp', 'u' + ui);
    g.setAttribute('data-last', 'u');
    restart(topic, 'boing'); restart(paper, 'fly');
  });
  g.querySelector('.silly').addEventListener('click', function () {
    si = (si + 1) % 4;
    g.setAttribute('data-tp', 's' + si);
    var before = level(), was = coins;
    if (coins < MAX) coins++;
    draw();
    restart(topic, 'boing'); restart(coin, 'drop'); restart(pig, 'jiggle');
    g.setAttribute('data-last', coins >= MAX ? 'max' : 's');
    if (level() > before) restart(lvName, 'up');
    if (coins === MAX && was < MAX && window.pengessoPop) {
      var r = pig.getBoundingClientRect();
      window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🪙', '💛', '🐷', '🐧', '✨'], 22);
    }
  });
  g.querySelector('.reset').addEventListener('click', function () {
    coins = 0; ui = -1; si = -1;
    g.setAttribute('data-tp', ''); g.setAttribute('data-last', '');
    draw();
  });
  draw();
})();