/* ⚖️ 人気のてんびん：JS は data-m / data-only / class / style / 絵文字 / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var lv = g.querySelector('.lv'), beam = g.querySelector('.beam'), ego = g.querySelector('.ego');
  var sP = g.querySelector('.s-praise'), sC = g.querySelector('.s-crit');
  var nP = g.querySelector('.n-praise'), nC = g.querySelector('.n-crit');
  var fame = g.querySelector('.fame'), only = g.querySelector('.only');
  var pans = [].slice.call(g.querySelectorAll('.pan'));
  var level = 0, praise = 0, crit = 0, puff = 0, busy = false;
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function rep(e, n) { var s = ''; for (var i = 0; i < Math.min(n, 6); i++) s += e; return s; }
  function setOnly(on) {
    g.setAttribute('data-only', on ? '1' : '0');
    only.setAttribute('aria-pressed', on ? 'true' : 'false');
  }
  function draw() {
    lv.textContent = String(level);
    nP.textContent = String(praise); nC.textContent = String(crit);
    sP.textContent = rep('💐', praise); sC.textContent = rep('🌵', crit);
    var tilt = Math.max(-16, Math.min(16, (crit - praise) * 4));
    beam.style.transform = 'rotate(' + tilt + 'deg)';
    pans.forEach(function (p) { p.style.transform = 'translateX(-50%) rotate(' + (-tilt) + 'deg)'; });  /* お皿は、いつも下にぶら下がる */
    ego.textContent = '🎈';
    ego.style.transform = 'scale(' + (puff ? 0.8 + puff * 0.45 : 0) + ')';
  }
  fame.addEventListener('click', function () {
    if (busy) return;
    level++; restart(lv, 'bump');
    if (g.getAttribute('data-only') === '1') {
      praise++; puff++; restart(nP, 'bump');
      draw();
      if (puff >= 5) {
        busy = true;
        g.setAttribute('data-m', 'pop');
        ego.style.transform = ''; ego.textContent = '💥'; restart(ego, 'boom');
        if (window.pengessoPop) {
          var k = ego.getBoundingClientRect();
          window.pengessoPop(k.left + k.width / 2, k.top + k.height / 2, ['💥', '🎈', '💨'], 14);
        }
        if (navigator.vibrate) { try { navigator.vibrate([30, 30, 60]); } catch (e) {} }
        setTimeout(function () {
          ego.classList.remove('boom');
          puff = 0; crit = praise; setOnly(false); busy = false; draw();
        }, 1300);
      } else {
        g.setAttribute('data-m', 'only');
      }
    } else {
      praise++; crit++; restart(nP, 'bump'); restart(nC, 'bump');
      g.setAttribute('data-m', level >= 6 ? 'big' : 'even');
      draw();
      if (level === 6 && window.pengessoPop) {
        var r = fame.getBoundingClientRect();
        window.pengessoPop(r.left + r.width / 2, r.top, ['⭐', '💐', '🌵', '🐧'], 16);
      }
    }
  });
  only.addEventListener('click', function () {
    if (busy) return;
    var on = g.getAttribute('data-only') !== '1';
    setOnly(on);
    if (!on) { puff = 0; draw(); }
  });
  g.querySelector('.reset').addEventListener('click', function () {
    level = 0; praise = 0; crit = 0; puff = 0; busy = false;
    ego.classList.remove('boom'); setOnly(false); g.setAttribute('data-m', 'start'); draw();
  });
  draw();
})();