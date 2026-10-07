/* 📱 ごきげんの読み込み：JS は data-* と数字と style だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var apps = [].slice.call(g.querySelectorAll('.app')), go = g.querySelector('.go'), bar = g.querySelector('.load i'),
      cnt = g.querySelector('.cnt'), phone = g.querySelector('.phone'), best = g.querySelector('.best');
  var KEY = 'pengesso-unfinished-tasks-weigh-on-you-best', p = 0, t0 = 0, last = 0;
  function now() { return (window.performance && performance.now) ? performance.now() : Date.now(); }
  function open() { return apps.filter(function (a) { return !a.classList.contains('done'); }).length; }
  function paint() {
    var n = open();
    g.setAttribute('data-open', n);
    cnt.textContent = n;
    g.setAttribute('data-light', n <= 2 ? '1' : '0');
    phone.style.setProperty('--clear', ((8 - n) / 8).toFixed(3));
    phone.style.setProperty('--spin', (0.5 + n * 0.3).toFixed(2) + 's');
  }
  function showBest() {
    var b = 0; try { b = parseFloat(localStorage.getItem(KEY)) || 0; } catch (e) {}
    if (b) { best.hidden = false; best.querySelector('.best-s').textContent = b.toFixed(1); }
  }
  function pop(el, list, n) {
    if (!window.pengessoPop) return;
    var r = el.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, n);
  }
  apps.forEach(function (a) {
    a.addEventListener('click', function () {
      if (a.classList.contains('done') || g.getAttribute('data-st') === 'done') return;
      a.classList.add('done'); a.setAttribute('aria-pressed', 'true');
      cnt.classList.remove('bump'); void cnt.offsetWidth; cnt.classList.add('bump');
      paint();
      pop(a, ['✅', '✨'], 6);
      if (navigator.vibrate) { try { navigator.vibrate(12); } catch (e) {} }
    });
  });
  function step() {
    var t = now(), dt = Math.min(0.1, (t - last) / 1000); last = t;
    p += dt * 100 / (1 + open() * 2.2);
    if (p >= 100) { bar.style.width = '100%'; finish(); return; }
    bar.style.width = p.toFixed(1) + '%';
    setTimeout(step, 30);
  }
  function finish() {
    var sec = (now() - t0) / 1000, n = open();
    g.querySelector('.tm').textContent = sec.toFixed(1);
    g.setAttribute('data-r', n === 0 ? 'light' : 'heavy');
    g.setAttribute('data-st', 'done');
    if (n === 0) {
      try { var b = parseFloat(localStorage.getItem(KEY)) || 0; if (!b || sec < b) localStorage.setItem(KEY, sec.toFixed(1)); } catch (e) {}
      showBest();
      pop(g.querySelector('.time'), ['☀️', '🧹', '✨', '🐧'], 18);
    }
  }
  go.addEventListener('click', function () {
    var s = g.getAttribute('data-st');
    if (s === 'idle') {
      g.setAttribute('data-st', 'run'); p = 0; bar.style.width = '0';
      t0 = last = now(); setTimeout(step, 30);
    } else if (s === 'done') {
      apps.forEach(function (a) { a.classList.remove('done'); a.setAttribute('aria-pressed', 'false'); });
      p = 0; bar.style.width = '0'; g.setAttribute('data-r', ''); g.setAttribute('data-st', 'idle'); paint();
    }
  });
  showBest(); paint();
})();