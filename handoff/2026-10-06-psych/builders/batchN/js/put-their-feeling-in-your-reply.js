/* 💬 話がつづくあいづち：JS は data-* / class / style / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var tabs = [].slice.call(g.querySelectorAll('.tab'));
  var bar = g.querySelector('.mb i'), num = g.querySelector('.mn'), snore = g.querySelector('.snore');
  var s = 0, timers = [], got = [false, false];
  function q(sel) { return [].slice.call(g.querySelectorAll(sel)); }
  function len(n) { num.textContent = String(n); bar.style.width = Math.min(100, n / 5 * 100) + '%'; }
  function clear() { timers.forEach(clearTimeout); timers = []; g.setAttribute('data-busy', '0'); }
  function scene(k) {
    clear(); s = k;
    g.setAttribute('data-s', String(s)); g.setAttribute('data-r', '');
    q('.msg').forEach(function (m) { m.classList.remove('show', 'cold'); });
    q('.m0.set' + s).forEach(function (m) { m.classList.add('show'); });
    tabs.forEach(function (t, i) { t.setAttribute('aria-pressed', i === s ? 'true' : 'false'); t.classList.toggle('got', got[i]); });
    len(1);
  }
  q('.rc').forEach(function (b) {
    b.addEventListener('click', function () {
      if (g.getAttribute('data-busy') === '1') return;
      scene(s);
      var warm = b.getAttribute('data-w') === '1';
      var mine = g.querySelector('.set' + s + (warm ? '.warm-' : '.cold-') + s);
      mine.classList.add('show'); if (!warm) mine.classList.add('cold');
      len(2);
      if (!warm) {
        timers.push(setTimeout(function () { snore.classList.add('show'); g.setAttribute('data-r', 'flat'); }, 500));
        return;
      }
      g.setAttribute('data-busy', '1');
      q('.more.set' + s).forEach(function (m, i) {
        timers.push(setTimeout(function () {
          m.classList.add('show'); len(3 + i);
          if (window.pengessoPop && i === 2) {
            var r = m.getBoundingClientRect();
            got[s] = true;
            var all = got[0] && got[1];
            g.setAttribute('data-all', all ? '1' : '0');
            tabs[s].classList.add('got');
            window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, all ? ['🏆', '💬', '🐧', '✨'] : ['💬', '🌱', '✨'], all ? 22 : 12);
          } else if (i === 2) { got[s] = true; g.setAttribute('data-all', got[0] && got[1] ? '1' : '0'); tabs[s].classList.add('got'); }
          if (i === 2) { g.setAttribute('data-r', 'warm'); g.setAttribute('data-busy', '0'); }
        }, 550 * (i + 1)));
      });
    });
  });
  tabs.forEach(function (t, i) { t.addEventListener('click', function () { scene(i); }); });
  g.querySelector('.reset').addEventListener('click', function () { got = [false, false]; g.setAttribute('data-all', '0'); scene(0); });
  scene(0);
})();