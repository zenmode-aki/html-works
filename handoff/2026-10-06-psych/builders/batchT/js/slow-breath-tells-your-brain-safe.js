/* 🌬 ゆっくり呼吸（吸う3秒・吐く4秒 × 3回）で部屋のランプがつき、脳が「安全」。速い呼吸だと警報。JS は data-* / class / 数字だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var slowBtn = g.querySelector('.slowbtn'), fastBtn = g.querySelector('.fastbtn'), again = g.querySelector('.again');
  var lamps = g.querySelectorAll('.lamps span'), sec = g.querySelector('.cue .sec'), brain = g.querySelector('.brain');
  var IN = 3, OUT = 4, ROUNDS = 3, timers = [];
  function later(fn, ms) { timers.push(setTimeout(fn, ms)); }
  function clear() { while (timers.length) clearTimeout(timers.pop()); }
  function set(s) { g.setAttribute('data-s', s); }
  function lamp(k) {
    g.setAttribute('data-k', k);
    for (var i = 0; i < lamps.length; i++) lamps[i].classList.toggle('on', i < k);
  }
  function count(n, done) {
    sec.textContent = n;
    if (n <= 1) { later(done, 1000); return; }
    later(function () { count(n - 1, done); }, 1000);
  }
  function round(r) {
    g.setAttribute('data-ph', 'in');
    count(IN, function () {
      g.setAttribute('data-ph', 'out');
      count(OUT, function () {
        lamp(r + 1);
        if (r + 1 >= ROUNDS) { finish(); return; }
        round(r + 1);
      });
    });
  }
  function finish() {
    set('done');
    if (window.pengessoPop) {
      var b = brain.getBoundingClientRect();
      window.pengessoPop(b.left + b.width / 2, b.top + b.height / 2, ['💡', '🧠', '✨', '🐧', '🌬️'], 18);
    }
    if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
  }
  slowBtn.addEventListener('click', function () {
    clear(); lamp(0); set('slow');
    g.setAttribute('data-ph', 'out');
    later(function () { round(0); }, 60);   /* 小さい円から始めて、吸うと大きくなる */
  });
  fastBtn.addEventListener('click', function () {
    clear(); lamp(0); set('fast');
    if (navigator.vibrate) { try { navigator.vibrate([40, 60, 40, 60, 40]); } catch (e) {} }
    later(function () { set('idle'); }, 2600);
  });
  again.addEventListener('click', function () { clear(); lamp(0); set('idle'); g.setAttribute('data-ph', 'in'); });
})();