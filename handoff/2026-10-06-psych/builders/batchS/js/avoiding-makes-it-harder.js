/* 🫧 世界を大きく保とう：JS は data-s / data-r / class / style / 絵文字 / 数字だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var zone = g.querySelector('.zone'), peng = g.querySelector('.peng'), face = g.querySelector('.zf');
  var cn = g.querySelector('.cn'), tbar = g.querySelector('.tbar i');
  var chips = [].slice.call(g.querySelectorAll('.ch'));
  var SLOT = ['0%', '34%', '68%'], DUR = 15000;
  var z = 1, coins = 0, t0 = 0, shrinkAt = 0, born = 0, tick = 0, cur = -1, last = -1;
  function restart(el, c) { el.classList.remove(c); void el.offsetWidth; el.classList.add(c); }
  function setZ() {
    zone.style.transform = 'scale(' + z.toFixed(3) + ')';
    face.textContent = z < 0.5 ? '😣' : z < 0.8 ? '🙂' : '😊';
  }
  function hide() { if (cur >= 0) chips[cur].classList.remove('on'); }
  function spawn() {
    hide();
    var k, s;
    do { k = Math.floor(Math.random() * chips.length); } while (k === cur);
    do { s = Math.floor(Math.random() * 3); } while (s === last);
    cur = k; last = s;
    chips[k].style.left = SLOT[s];
    chips[k].classList.add('on');
    born = Date.now();
  }
  function end() {
    clearInterval(tick); tick = 0; hide(); cur = -1;
    tbar.style.width = '0%';
    g.setAttribute('data-r', coins >= 10 ? 'big' : coins >= 4 ? 'mid' : 'small');
    g.setAttribute('data-s', 'done');
    if (coins >= 10 && window.pengessoPop) {
      var r = zone.getBoundingClientRect();
      window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🌏', '🪙', '🐧', '✨'], 24);
    }
  }
  function loop() {
    var now = Date.now(), el = now - t0;
    tbar.style.width = Math.max(0, 100 - el / DUR * 100) + '%';
    if (el >= DUR) { end(); return; }
    if (now - shrinkAt >= 500) { z = Math.max(0.3, z - 0.035); setZ(); shrinkAt = now; }
    if (now - born > 1500) spawn();
  }
  function start() {
    clearInterval(tick);
    z = 1; coins = 0; cn.textContent = '0'; setZ();
    g.setAttribute('data-r', ''); g.setAttribute('data-s', 'run');
    t0 = shrinkAt = Date.now(); tbar.style.width = '100%';
    spawn();
    tick = setInterval(loop, 100);
  }
  chips.forEach(function (b) {
    b.addEventListener('click', function () {
      if (g.getAttribute('data-s') !== 'run' || !b.classList.contains('on')) return;
      coins++; cn.textContent = String(coins); restart(cn, 'ping');
      z = Math.min(1, z + 0.12); setZ(); restart(peng, 'hop2');
      var r = b.getBoundingClientRect();
      if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🪙', b.querySelector('.che').textContent], 8);
      spawn();
    });
  });
  g.querySelector('.start').addEventListener('click', start);
  g.querySelector('.again').addEventListener('click', start);
})();