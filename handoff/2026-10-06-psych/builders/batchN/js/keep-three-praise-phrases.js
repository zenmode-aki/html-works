/* 🎯 褒め言葉の早撃ち：JS は data-* / class / 絵文字 / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var KEY = 'pengesso-keep-three-praise-phrases-days';
  var Q = 5, T = 3000;
  var bar = g.querySelector('.clock i'), react = g.querySelector('.fr-react');
  var stars = [].slice.call(g.querySelectorAll('.stars i'));
  var days = g.querySelector('.days'), dN = g.querySelector('.d-n');
  var q = 0, score = 0, t0 = 0, tick = 0, busy = false;
  function now() { return (window.performance && performance.now) ? performance.now() : Date.now(); }
  function restart(el, c) { el.classList.remove(c); void el.offsetWidth; el.classList.add(c); }
  function loadDays() { try { return JSON.parse(localStorage.getItem(KEY) || '[]') || []; } catch (e) { return []; } }
  function showDays() {
    var d = loadDays();
    if (d.length) { days.hidden = false; dN.textContent = Math.min(d.length, 21) + '/21'; }
  }
  function addDay() {
    var t = new Date(), k = t.getFullYear() + '-' + (t.getMonth() + 1) + '-' + t.getDate(), d = loadDays();
    if (d.indexOf(k) < 0) d.push(k);
    try { localStorage.setItem(KEY, JSON.stringify(d.slice(-60))); } catch (e) {}
  }
  function ask() {
    busy = false;
    g.setAttribute('data-q', String(q)); g.setAttribute('data-hit', '');
    react.textContent = '💭';
    bar.classList.remove('low'); bar.style.width = '100%';
    t0 = now();
    clearInterval(tick);
    tick = setInterval(function () {
      var left = 1 - (now() - t0) / T;
      bar.style.width = Math.max(0, left * 100) + '%';
      bar.classList.toggle('low', left < 0.35);
      if (left <= 0) answer(false, null);
    }, 40);
  }
  function answer(ok, btn) {
    if (busy) return;
    busy = true; clearInterval(tick);
    g.setAttribute('data-hit', ok ? 'ok' : 'miss');
    react.textContent = ok ? '😊' : '😶';
    restart(react, 'boing');
    if (ok) {
      score++; stars[q].classList.add('on');
      if (btn && window.pengessoPop) { var r = btn.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['⭐', '✨', '💖'], 8); }
    } else stars[q].classList.add('miss');
    setTimeout(function () { q++; if (q < Q) ask(); else finish(); }, 700);
  }
  function finish() {
    var r = score === Q ? 'gold' : score >= 3 ? 'ok' : 'low';
    g.querySelectorAll('.sc').forEach(function (s) { s.textContent = String(score); });
    g.setAttribute('data-hit', ''); g.setAttribute('data-r', r); g.setAttribute('data-s', 'done');
    react.textContent = score >= 3 ? '🥰' : '🙂';
    addDay(); showDays();
    if (r === 'gold' && window.pengessoPop) {
      var b = g.querySelector('.stars').getBoundingClientRect();
      window.pengessoPop(b.left + b.width / 2, b.top + b.height / 2, ['🥇', '⭐', '🐧', '✨'], 20);
    }
  }
  g.querySelector('.go').addEventListener('click', function () {
    if (g.getAttribute('data-s') === 'run') return;
    q = 0; score = 0;
    stars.forEach(function (s) { s.classList.remove('on', 'miss'); });
    g.setAttribute('data-s', 'run'); g.setAttribute('data-r', '');
    ask();
  });
  [].slice.call(g.querySelectorAll('.ph')).forEach(function (b) {
    b.addEventListener('click', function () { if (g.getAttribute('data-s') === 'run') answer(true, b); });
  });
  showDays();
})();