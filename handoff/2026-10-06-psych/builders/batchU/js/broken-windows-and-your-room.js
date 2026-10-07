/* ☕ 最初の1つ：1日＝1.1秒。散らかりが1つでもあると次の日に物が増える（多いほど速く増える）。最初のコップをすぐ片付ければ1タップ。JS は data-* と数字と絵文字だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var mess = [].slice.call(g.querySelectorAll('.mess')), btn = g.querySelector('.gobtn'), tn = g.querySelector('.tn');
  var dots = [].slice.call(g.querySelectorAll('.dots i')), mood = g.querySelector('.desk .mood');
  var day = 0, taps = 0, shown = 0, timer = 0;
  function onCount() { return mess.filter(function (m) { return m.getAttribute('data-on') === '1'; }).length; }
  function face() {
    var n = onCount();
    mood.textContent = n === 0 ? '😊' : n <= 2 ? '😐' : n <= 4 ? '😟' : '😵';
    g.setAttribute('data-clean', n === 0 ? '1' : '0');
  }
  function spawn(k) {
    var off = mess.filter(function (m) { return m.getAttribute('data-on') !== '1' && !m.classList.contains('first'); });
    for (var i = 0; i < k && off.length; i++) { off.shift().setAttribute('data-on', '1'); shown++; }
  }
  function tick() {
    day++;
    g.setAttribute('data-d', day);
    dots.forEach(function (d, i) { d.classList.toggle('on', i < day); });
    if (day > 1) { var n = onCount(); if (n > 0) spawn(n >= 3 ? 2 : 1); }
    face();
    if (day >= 7) { timer = setTimeout(end, 1100); return; }
    timer = setTimeout(tick, 1100);
  }
  function end() {
    var n = onCount();
    var r = n > 0 ? 'messy' : (shown === 1 && taps === 1) ? 'early' : 'late';
    g.setAttribute('data-r', r); g.setAttribute('data-s', 'end');
    if (r === 'early') {
      if (window.pengessoPop) {
        var k = g.querySelector('.desk').getBoundingClientRect();
        window.pengessoPop(k.left + k.width / 2, k.top + k.height / 2, ['✨', '☕', '🐧', '🧹'], 18);
      }
      if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
    }
  }
  function start() {
    clearTimeout(timer);
    mess.forEach(function (m) { m.removeAttribute('data-on'); });
    day = 0; taps = 0; shown = 1; tn.textContent = 0;
    g.setAttribute('data-s', 'run'); g.setAttribute('data-r', '');
    mess[0].setAttribute('data-on', '1');   /* 月曜日：コップが1つ */
    tick();
  }
  mess.forEach(function (m) {
    m.addEventListener('click', function () {
      if (g.getAttribute('data-s') !== 'run' || m.getAttribute('data-on') !== '1') return;
      m.removeAttribute('data-on');
      taps++; tn.textContent = taps;
      face();
      if (window.pengessoPop) {
        var k = m.getBoundingClientRect();
        window.pengessoPop(k.left + k.width / 2, k.top + k.height / 2, ['✨'], 4);
      }
    });
  });
  btn.addEventListener('click', start);
})();