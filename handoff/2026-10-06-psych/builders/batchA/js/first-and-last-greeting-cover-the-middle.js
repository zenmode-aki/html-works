/* 🥪 1日サンドイッチ：JS は data-* / class / aria-pressed / 幅だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var fills = [].slice.call(g.querySelectorAll('.fill'));
  var bTop = g.querySelector('.bread.top'), bBot = g.querySelector('.bread.bot');
  var tTop = g.querySelector('.t-top'), tBot = g.querySelector('.t-bot');
  var add = g.querySelector('.add'), less = g.querySelector('.less'), serve = g.querySelector('.serve');
  var bar = g.querySelector('.fm-bar i');
  var n = 2, top = false, bot = false;
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function draw() {
    fills.forEach(function (f, i) { f.classList.toggle('on', i < n); });
    bTop.classList.toggle('off', !top); bBot.classList.toggle('off', !bot);
    tTop.setAttribute('aria-pressed', top ? 'true' : 'false');
    tBot.setAttribute('aria-pressed', bot ? 'true' : 'false');
    add.disabled = n >= fills.length; less.disabled = n <= 0;
    g.setAttribute('data-top', top ? '1' : '0'); g.setAttribute('data-bot', bot ? '1' : '0'); g.setAttribute('data-n', String(n));
  }
  function edit() { g.setAttribute('data-s', 'build'); g.setAttribute('data-r', ''); bar.style.width = '0'; }
  tTop.addEventListener('click', function () { top = !top; edit(); draw(); if (top) restart(bTop, 'on-anim'); });
  tBot.addEventListener('click', function () { bot = !bot; edit(); draw(); if (bot) restart(bBot, 'on-anim'); });
  add.addEventListener('click', function () { if (n < fills.length) { n++; edit(); draw(); } });
  less.addEventListener('click', function () { if (n > 0) { n--; edit(); draw(); } });
  serve.addEventListener('click', function () {
    var r = (top && bot) ? 'good' : (top || bot) ? 'half' : (n ? 'bad' : 'empty');
    g.setAttribute('data-s', 'served');
    g.setAttribute('data-r', '');
    void g.offsetWidth;   /* 同じ結果でも、もう一度動かす */
    g.setAttribute('data-r', r);
    bar.style.width = { good: '100%', half: '40%', bad: '6%', empty: '0' }[r];
    if (r === 'good' && window.pengessoPop) {
      var k = g.querySelector('.sandwich').getBoundingClientRect();
      window.pengessoPop(k.left + k.width / 2, k.top + k.height / 2, ['🥪', '🍞', '🐧', '✨', '😋'], 18);
    }
  });
  draw();
})();