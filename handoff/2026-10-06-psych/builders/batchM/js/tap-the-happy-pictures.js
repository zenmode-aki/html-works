
/* 🎈 うれしい絵さがし：JS は data-*・class・絵文字・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var tiles = [].slice.call(g.querySelectorAll('.tile'));
  var rn = g.querySelector('.rn'), ms = g.querySelector('.ms'), clock = g.querySelector('.clock'),
      avgEl = g.querySelector('.avg'), stars = g.querySelector('.stars'), best = g.querySelector('.best');
  var HAPPY = ['🌸', '☀️', '🍰', '🌈', '🎁', '🍦', '🐶', '🎈', '🍓', '🌻'];
  var GLOOM = ['🌧️', '🧾', '🗑️', '🥀', '🌪️', '💸', '🪫', '🌩️'];
  var KEY = 'pengesso-tap-the-happy-pictures-best';
  var ROUNDS = 8, round = 0, misses = 0, times = [], happyAt = -1, t0 = 0, lock = true, tick = 0, happyList = [];
  function now() { return (window.performance && performance.now) ? performance.now() : Date.now(); }
  function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function set(s) { g.setAttribute('data-s', s); }
  function showBest() {
    var b = 0; try { b = parseFloat(localStorage.getItem(KEY)) || 0; } catch (e) {}
    if (b) { best.hidden = false; best.querySelector('.best-v').textContent = b.toFixed(2); }
  }
  function deal() {
    round++; rn.textContent = String(round);
    var gl = shuffle(GLOOM);
    happyAt = Math.floor(Math.random() * tiles.length);
    var k = 0;
    tiles.forEach(function (t, i) {
      t.classList.remove('good', 'bad', 'deal');
      t.textContent = i === happyAt ? happyList[round - 1] : gl[k++];
      void t.offsetWidth; t.classList.add('deal');
    });
    t0 = now(); lock = false;
  }
  function start() {
    round = 0; misses = 0; times = []; ms.textContent = '0';
    happyList = shuffle(HAPPY);
    g.setAttribute('data-r', ''); g.setAttribute('data-learn', '0');
    set('play'); deal();
    clearInterval(tick);
    tick = setInterval(function () { if (!lock) clock.textContent = ((now() - t0) / 1000).toFixed(1); }, 100);
  }
  function mean(a) { var s = 0; for (var i = 0; i < a.length; i++) s += a[i]; return a.length ? s / a.length : 0; }
  function finish() {
    clearInterval(tick); lock = true;
    var avg = mean(times) / 1000;
    var r = avg < 0.9 ? 'gold' : avg < 1.5 ? 'ok' : 'slow';
    avgEl.textContent = avg.toFixed(2);
    stars.textContent = r === 'gold' ? '⭐⭐⭐' : r === 'ok' ? '⭐⭐☆' : '⭐☆☆';
    var learn = mean(times.slice(-3)) < mean(times.slice(0, 3)) * 0.92;
    g.setAttribute('data-learn', learn ? '1' : '0');
    g.setAttribute('data-r', r);
    set('done');
    try { var b = parseFloat(localStorage.getItem(KEY)) || 0; if (!b || avg < b) localStorage.setItem(KEY, avg.toFixed(2)); } catch (e) {}
    showBest();
    if (window.pengessoPop && (r !== 'slow' || learn)) {
      var q = stars.getBoundingClientRect();
      window.pengessoPop(q.left + q.width / 2, q.top + q.height / 2, ['🌸', '☀️', '🌈', '🎈', '🐧', '✨'], r === 'gold' ? 24 : 14);
    }
  }
  tiles.forEach(function (t, i) {
    t.addEventListener('click', function () {
      if (lock || g.getAttribute('data-s') !== 'play') return;
      if (i === happyAt) {
        lock = true;
        var dt = now() - t0; times.push(dt);
        clock.textContent = (dt / 1000).toFixed(1);
        t.classList.remove('deal'); t.classList.add('good');
        if (window.pengessoPop) { var q = t.getBoundingClientRect(); window.pengessoPop(q.left + q.width / 2, q.top + q.height / 2, ['✨', t.textContent], 6); }
        setTimeout(function () { if (round < ROUNDS) deal(); else finish(); }, 320);
      } else if (!t.classList.contains('bad')) {
        misses++; ms.textContent = String(misses);
        t.classList.remove('deal'); t.classList.add('bad');
        if (navigator.vibrate) { try { navigator.vibrate(15); } catch (e) {} }
      }
    });
  });
  g.querySelector('.b-start').addEventListener('click', function () {
    var s = g.getAttribute('data-s');
    if (s === 'idle' || s === 'done') start();
  });
  showBest();
})();
