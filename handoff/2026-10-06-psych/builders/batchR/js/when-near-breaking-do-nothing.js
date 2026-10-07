/* 🌙 10秒のおやすみモード：JS は data-*・class・数字・style だけを変える。文字は上の HTML（訳がそのまま効く）。
   勝ち負けはなし。途中で押しても、やり直しにはしない（やさしく声をかけるだけ） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var go = g.querySelector('.go'), again = g.querySelector('.again'), room = g.querySelector('.room');
  var bar = g.querySelector('.rest-bar i'), secN = g.querySelector('.sec-n');
  var stars = [].slice.call(g.querySelectorAll('.stars span'));
  var DUR = 10, left = DUR, tick = 0, tapT = 0, breathT = 0;
  function set(k, v) { g.setAttribute('data-' + k, v); }
  function reset() {
    clearInterval(tick); clearInterval(breathT); clearTimeout(tapT);
    left = DUR; secN.textContent = String(DUR); bar.style.width = '0';
    stars.forEach(function (s) { s.classList.remove('on'); });
    set('tap', '0'); set('b', 'in');
  }
  function start() {
    reset(); set('s', 'rest');
    var phase = 0;
    breathT = setInterval(function () { phase = 1 - phase; set('b', phase ? 'out' : 'in'); }, 2500);
    tick = setInterval(function () {
      left--;
      secN.textContent = String(Math.max(0, left));
      bar.style.width = ((DUR - left) / DUR * 100) + '%';
      var lit = Math.floor((DUR - left) / 2);
      stars.forEach(function (s, k) { s.classList.toggle('on', k < lit); });
      if (left <= 0) done();
    }, 1000);
  }
  function done() {
    clearInterval(tick); clearInterval(breathT); clearTimeout(tapT);
    set('tap', '0'); set('s', 'done');
    if (window.pengessoPop) {
      var r = room.getBoundingClientRect();
      window.pengessoPop(r.left + r.width / 2, r.top + r.height * 0.4, ['🌙', '⭐', '🐧'], 8);
    }
  }
  room.addEventListener('click', function () {
    if (g.getAttribute('data-s') !== 'rest') return;
    set('tap', '1'); clearTimeout(tapT);
    tapT = setTimeout(function () { set('tap', '0'); }, 1800);
  });
  go.addEventListener('click', start);
  again.addEventListener('click', start);
})();