/* 🏁 7日レース：気合は最初だけ速くて4日目に燃え尽きる。ごほうびは毎日同じだけ進む。JS は data-* と style と数字と絵文字だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var btn = g.querySelector('.nextbtn'), dn = g.querySelector('.dn');
  var wp = g.querySelector('.lane.wp'), rw = g.querySelector('.lane.rw');
  var wRun = wp.querySelector('.runner'), rRun = rw.querySelector('.runner');
  var wFuel = wp.querySelector('.fuel'), wTag = wp.querySelector('.tag'), rTag = rw.querySelector('.tag');
  var WPOS = [0, 2.6, 4.0, 4.6, 4.6, 4.6, 4.6, 4.6];
  var WFUEL = ['🔥🔥🔥', '🔥🔥🔥', '🔥🔥', '🔥', '💨', '💨', '💨', '💨'];
  var WTAG = ['💥', '💥', '💦', '💦', '💤', '💤', '💤', '💤'];
  var RTAG = ['☕', '☕', '🍪', '☕', '🍪', '☕', '🍪', '☕'];
  var d = 0;
  function place(el, pos) { el.style.left = 'calc(' + (pos / 7) + ' * (100% - 84px) + 4px)'; }
  function draw() {
    dn.textContent = d;
    g.setAttribute('data-d', d);
    g.setAttribute('data-w', d === 0 ? '0' : d <= 3 ? String(d) : 'out');
    place(wRun, WPOS[d]); place(rRun, d);
    wFuel.textContent = WFUEL[d]; wTag.textContent = WTAG[d]; rTag.textContent = RTAG[d];
  }
  btn.addEventListener('click', function () {
    if (d === 7) { d = 0; draw(); return; }
    d++; draw();
    rTag.classList.remove('hop'); void rTag.offsetWidth; rTag.classList.add('hop');
    if (window.pengessoPop) {
      var k = rTag.getBoundingClientRect();
      if (d < 7) window.pengessoPop(k.left + k.width / 2, k.top + k.height / 2, [RTAG[d]], 4);
      else window.pengessoPop(k.left + k.width / 2, k.top + k.height / 2, ['🏁', '☕', '🐧', '✨'], 18);
    }
    if (d === 7 && navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
  });
  draw();
})();