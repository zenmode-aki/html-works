/* 🍯 しあわせのびん：JS は data-*・aria-pressed・数字・絵文字・style だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var mQuiet = g.querySelector('.m-quiet'), mSay = g.querySelector('.m-say');
  var foods = [].slice.call(g.querySelectorAll('.food'));
  var fill = g.querySelector('.jar .fill'), hearts = g.querySelector('.jar .hearts'), jn = g.querySelector('.jn'), pg = g.querySelector('.pg');
  var again = g.querySelector('.again');
  var EMO = ['🍵', '🍤', '🛏️', '☀️'];
  var STEP = 13, v = 0, quietTaps = 0, list = [];
  function set(k, val) { g.setAttribute('data-' + k, val); }
  function again2(k, val) { set(k, ''); void g.offsetWidth; set(k, val); }
  function mode(m) {
    set('mode', m);
    mQuiet.setAttribute('aria-pressed', m === 'quiet' ? 'true' : 'false');
    mSay.setAttribute('aria-pressed', m === 'say' ? 'true' : 'false');
    if (g.getAttribute('data-r') === 'hint') set('r', '');
  }
  function paint() {
    fill.style.height = v + '%'; jn.textContent = String(v);
    hearts.textContent = list.slice(-4).join('') || ' ';
  }
  function bounce(el) { el.classList.remove('boing'); void el.offsetWidth; el.classList.add('boing'); }
  function eat(k) {
    if (g.getAttribute('data-r') === 'full') return;
    bounce(pg);
    if (g.getAttribute('data-mode') === 'quiet') {
      again2('say', 'quiet');
      quietTaps++;
      if (quietTaps >= 2) set('r', 'hint');
      return;
    }
    again2('say', String(k));
    v = Math.min(100, v + STEP); list.push(EMO[k]); paint();
    if (window.pengessoPop) { var r = fill.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + 10, ['💛', EMO[k]], 5); }
    if (v >= 100) {
      set('r', 'full');
      if (window.pengessoPop) { var r2 = fill.getBoundingClientRect(); window.pengessoPop(r2.left + r2.width / 2, r2.top + r2.height / 2, ['🍯', '💛', '🐧', '✨'], 18); }
    }
  }
  mQuiet.addEventListener('click', function () { mode('quiet'); });
  mSay.addEventListener('click', function () { mode('say'); });
  foods.forEach(function (b, k) { b.addEventListener('click', function () { eat(k); }); });
  again.addEventListener('click', function () { v = 0; quietTaps = 0; list = []; set('r', ''); set('say', ''); mode('quiet'); paint(); });
  paint();
})();