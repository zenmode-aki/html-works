/* 🥂 やさしさのタワー：JS は data-st / class / style / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var KIDS = { 0: [1, 2], 1: [3, 4], 2: [4, 5] };
  var glasses = [].slice.call(g.querySelectorAll('.glass'));
  var fills = glasses.map(function (b) { return b.querySelector('.fill'); });
  var cn = g.querySelector('.cn');
  var lv = [0, 0, 0, 0, 0, 0], done = false;
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function pour(i, a) {                       /* あふれた分は、下の2つに半分ずつ（いちばん下は、テーブルへこぼれる） */
    var room = 1 - lv[i];
    if (a <= room) { lv[i] += a; return; }
    lv[i] = 1;
    var rest = a - room;
    if (KIDS[i]) KIDS[i].forEach(function (k) { pour(k, rest / 2); });
  }
  function draw() {
    var n = 0;
    lv.forEach(function (v, i) {
      fills[i].style.height = Math.round(v * 100) + '%';
      var full = v >= 0.999; glasses[i].classList.toggle('full', full); if (full) n++;
    });
    cn.textContent = n + '/6';
    return n;
  }
  glasses.forEach(function (b) {
    b.addEventListener('click', function () {
      var i = +b.getAttribute('data-i');
      pour(i, 1);
      restart(b, 'hit');
      var n = draw();
      if (n === 6) {
        g.setAttribute('data-st', 'full');
        if (!done && window.pengessoPop) {
          var k = glasses[0].getBoundingClientRect();
          window.pengessoPop(k.left + k.width / 2, k.top + k.height / 2, ['🥂', '✨', '🐧', '💛'], 22);
        }
        done = true;
        return;
      }
      if (lv[0] < 0.999) {
        var others = lv.slice(1).reduce(function (s, v) { return s + v; }, 0);
        if (others > 0) { g.setAttribute('data-st', 'top'); void g.offsetWidth; }   /* 吹き出しのゆれを毎回出す */
        g.setAttribute('data-st', others > 0 ? 'grumble' : 'top');
      } else {
        g.setAttribute('data-st', 'flow');
      }
    });
  });
  g.querySelector('.reset').addEventListener('click', function () {
    lv = [0, 0, 0, 0, 0, 0]; done = false; draw(); g.setAttribute('data-st', 'start');
  });
  draw();
})();