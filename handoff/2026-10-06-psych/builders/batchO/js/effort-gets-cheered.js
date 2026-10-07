/* 📣 かけっこ：JS は data-s / class / style の位置と幅 / 絵文字だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var sp = g.querySelector('.sp-r'), me = g.querySelector('.me-r'), pg = g.querySelector('.me-r .pg'), meFx = g.querySelector('.me-r .fx'), spFx = g.querySelector('.sp-r .fx');
  var barSp = g.querySelector('.bar.sp i'), barYou = g.querySelector('.bar.you i'), crowd = g.querySelector('.crowd');
  var pS = 0, pM = 0, cS = 0, cM = 0, fell = false, spDone = false, tick = 0, FALL_AT = 42;
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function place(el, p) { el.style.left = 'calc((100% - 66px) * ' + (p / 100) + ')'; }
  function bars() { barSp.style.width = cS + '%'; barYou.style.width = cM + '%'; }
  function set(s) { g.setAttribute('data-s', s); }
  function reset() {
    clearInterval(tick); pS = 0; pM = 0; cS = 0; cM = 0; fell = false; spDone = false;
    place(sp, 0); place(me, 0); meFx.textContent = ''; spFx.textContent = ''; crowd.classList.remove('cheer'); bars();
  }
  function start() {
    reset(); set('run');
    tick = setInterval(function () {
      if (spDone) return;
      pS = Math.min(100, pS + 3.2); place(sp, pS); cS = Math.round(pS * .4); bars();
      if (pS >= 100) { spDone = true; spFx.textContent = '🥇'; }
    }, 60);
  }
  function finish() {
    clearInterval(tick); set('done');
    cM = 100; bars(); meFx.textContent = '🏅';
    crowd.classList.add('cheer');
    if (window.pengessoPop) { var r = me.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top, ['📣', '🎉', '🐧', '💖', '✨'], 24); }
    if (navigator.vibrate) { try { navigator.vibrate(40); } catch (e) {} }
  }
  g.querySelector('.b-start').addEventListener('click', start);
  g.querySelector('.b-again').addEventListener('click', start);
  g.querySelector('.b-run').addEventListener('click', function () {
    if (g.getAttribute('data-s') !== 'run') return;
    pM = Math.min(100, pM + 6.5); place(me, pM); restart(pg, 'wob');
    cM = Math.min(95, cM + (fell ? 9 : 1)); bars();
    if (fell) crowd.classList.add('cheer');
    if (!fell && pM >= FALL_AT) { fell = true; set('fall'); meFx.textContent = '💥'; return; }
    if (pM >= 100) finish();
  });
  g.querySelector('.b-up').addEventListener('click', function () {
    meFx.textContent = '💦'; set('run'); cM = Math.min(95, cM + 15); bars(); crowd.classList.add('cheer');
  });
  reset();
})();