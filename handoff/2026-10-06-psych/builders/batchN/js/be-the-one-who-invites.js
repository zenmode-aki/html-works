/* 📮 誘ってみよう：JS は data-* / class / 絵文字 / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var days = [].slice.call(g.querySelectorAll('.day'));
  var plane = g.querySelector('.plane'), pal = g.querySelector('.pal'), reply = g.querySelector('.reply'), cn = g.querySelector('.cn');
  var waitB = g.querySelector('.wait'), invB = g.querySelector('.invite');
  var PALS = ['🦭', '🐻‍❄️', '🦦', '🐨', '🐧', '🦊'];
  var FUN = ['☕', '🍜', '🎳', '🎬', '⚾', '🍦', '🧺'];
  var plans = 0, sent = 0, timers = [], busy = false;
  function restart(el, c) { el.classList.remove(c); void el.offsetWidth; el.classList.add(c); }
  function state(s) { g.setAttribute('data-s', s); restart(reply, 'fresh'); }
  function clearDays() { days.forEach(function (d) { d.classList.remove('plan', 'quiet'); d.querySelector('.di').textContent = '·'; }); }
  function clear() { timers.forEach(clearTimeout); timers = []; busy = false; }
  waitB.addEventListener('click', function () {
    clear(); plans = 0; sent = 0; cn.textContent = '0'; clearDays();
    g.setAttribute('data-s', 'wait'); busy = true;
    days.forEach(function (d, i) {
      timers.push(setTimeout(function () { d.classList.add('quiet'); d.querySelector('.di').textContent = '🍃'; if (i === 6) busy = false; }, 160 * (i + 1)));
    });
  });
  invB.addEventListener('click', function () {
    if (busy) return;
    if (g.getAttribute('data-s') === 'wait') { clear(); clearDays(); }
    if (plans >= 7) return;
    busy = true;
    var who = PALS[sent % PALS.length]; sent++;
    pal.textContent = who;
    restart(plane, 'fly');
    var yes = sent === 1 || Math.random() < 0.72;
    timers.push(setTimeout(function () {
      busy = false;
      restart(pal, 'boing');
      if (!yes) { state('later'); return; }
      var d = days[plans]; plans++;
      d.classList.remove('quiet'); d.classList.add('plan'); d.querySelector('.di').textContent = FUN[(plans - 1) % FUN.length];
      cn.textContent = String(plans);
      if (plans === 5) {
        state('full');
        if (window.pengessoPop) { var r = g.querySelector('.week').getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🎉', '🐧', '📮', '☕', '✨'], 22); }
      } else {
        state(plans > 5 ? 'full' : 'yes');
        if (window.pengessoPop) { var b = d.getBoundingClientRect(); window.pengessoPop(b.left + b.width / 2, b.top + b.height / 2, ['✨', FUN[(plans - 1) % FUN.length]], 8); }
      }
      invB.disabled = plans >= 7;
    }, 650));
  });
  g.querySelector('.reset').addEventListener('click', function () {
    clear(); plans = 0; sent = 0; cn.textContent = '0'; clearDays(); invB.disabled = false; pal.textContent = '🦭'; state('idle');
  });
})();