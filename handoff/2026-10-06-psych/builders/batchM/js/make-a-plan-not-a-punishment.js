
/* ⏰ 遅刻ループ：JS は data-s / data-r・絵文字・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var tm = g.querySelector('.tm'), ck = g.querySelector('.ck-e'), runner = g.querySelector('.runner'), dn = g.querySelector('.dn'),
      hh = g.querySelector('.hh'), scs = g.querySelectorAll('.sc'), ple = g.querySelector('.pl-e');
  var day = 1, scratches = 0, busy = false, timers = [], ivs = [];
  function calm() { try { return !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches); } catch (e) { return false; } }
  function later(fn, ms) { timers.push(setTimeout(fn, calm() ? 0 : ms)); }
  function stopAll() { timers.forEach(clearTimeout); ivs.forEach(clearInterval); timers = []; ivs = []; g.classList.remove('running'); }
  function set(s, r) { g.setAttribute('data-s', s); if (r !== undefined) g.setAttribute('data-r', r); }
  function fmt(min) { var h = Math.floor(min / 60), m = min % 60; return h + ':' + (m < 10 ? '0' : '') + m; }
  function place(p, instant) {
    if (instant) runner.style.transition = 'none';
    runner.style.left = (5 + p * 73) + '%';
    if (instant) { void runner.offsetWidth; runner.style.transition = ''; }
  }
  function bump(el) { el.classList.remove('pop'); void el.offsetWidth; el.classList.add('pop'); }
  function paintHeart() { for (var i = 0; i < scs.length; i++) scs[i].textContent = i < scratches ? '🩹' : ''; }
  function pop(list, n) {
    if (!window.pengessoPop) return;
    var r = runner.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, n);
  }
  /* 次の朝のリプレイ：家から出発して、時計の数字を進める */
  function replay(from, to, done) {
    day++; dn.textContent = String(day); bump(dn);
    set('run'); ck.textContent = '🕗';
    place(0, true); tm.textContent = fmt(from);
    if (calm()) { place(1, true); tm.textContent = fmt(to); done(); return; }
    g.classList.add('running');
    later(function () {
      place(1);
      var t0 = Date.now(), dur = 1500;
      var iv = setInterval(function () {
        var k = Math.min(1, (Date.now() - t0) / dur);
        tm.textContent = fmt(Math.round(from + (to - from) * k));
        if (k >= 1) { clearInterval(iv); g.classList.remove('running'); done(); }
      }, 50);
      ivs.push(iv);
    }, 450);
  }
  g.querySelector('.b-blame').addEventListener('click', function () {
    if (busy || g.getAttribute('data-s') !== 'late') return;
    busy = true;
    scratches = Math.min(3, scratches + 1); paintHeart();
    hh.classList.remove('shake'); void hh.offsetWidth; hh.classList.add('shake');
    set('blame');
    if (navigator.vibrate) { try { navigator.vibrate(20); } catch (e) {} }
    later(function () {
      replay(525, 545, function () { ck.textContent = '🕘'; set('late', scratches >= 3 ? 'again3' : 'again'); busy = false; });
    }, 1500);
  });
  g.querySelector('.b-plan').addEventListener('click', function () {
    if (busy || g.getAttribute('data-s') !== 'late') return;
    set('choose');
  });
  [].forEach.call(g.querySelectorAll('.pick'), function (b) {
    b.addEventListener('click', function () {
      if (busy || g.getAttribute('data-s') !== 'choose') return;
      busy = true;
      ple.textContent = b.getAttribute('data-e'); bump(ple);
      replay(515, 535, function () {
        ck.textContent = '🕣'; hh.textContent = '💖'; bump(hh);
        set('win'); busy = false;
        pop(['⏰', '✨', '🐧', '🌅', '💖'], 18);
        if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
      });
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    stopAll(); busy = false; day = 1; scratches = 0;
    dn.textContent = '1'; paintHeart(); hh.textContent = '❤️'; ple.textContent = '❔'; ck.textContent = '🕘';
    tm.textContent = '9:05'; place(1, true); set('late', '');
  });
  place(1, true);
})();
