/* 🍢 じっくり焼き鳥：JS は data-*・aria-pressed・class・絵文字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var grill = g.querySelector('.grill'), skewer = g.querySelector('.skewer'), smoke = g.querySelector('.smoke');
  var turnb = g.querySelector('.turnb'), hearts = g.querySelector('.hearts'), again = g.querySelector('.again');
  var mDeep = g.querySelector('.m-deep'), mMulti = g.querySelector('.m-multi');
  var cook = 0, fun = 0, dT = 0;
  function set(k, v) { g.setAttribute('data-' + k, v); }
  function again2(k, v) { set(k, ''); void g.offsetWidth; set(k, v); }
  function anim(el, c) { el.classList.remove(c); void el.offsetWidth; el.classList.add(c); }
  function paint() {
    grill.setAttribute('data-c', String(cook));
    var s = ''; for (var i = 0; i < 6; i++) s += i < fun ? '💛' : '🤍';
    hearts.textContent = s;
  }
  function reset() { clearTimeout(dT); cook = 0; fun = 0; grill.setAttribute('data-d', ''); set('r', ''); paint(); }
  function mode(m) {
    set('mode', m);
    mDeep.setAttribute('aria-pressed', m === 'deep' ? 'true' : 'false');
    mMulti.setAttribute('aria-pressed', m === 'multi' ? 'true' : 'false');
    reset();
  }
  turnb.addEventListener('click', function () {
    if (cook >= 6) return;
    cook++;
    anim(skewer, 'turn');
    var multi = g.getAttribute('data-mode') === 'multi';
    if (multi) {
      grill.setAttribute('data-d', String((cook - 1) % 3));
      clearTimeout(dT); dT = setTimeout(function () { grill.setAttribute('data-d', ''); }, 1100);
      again2('r', 'busy');
    } else {
      fun++; anim(smoke, 'go'); again2('r', 'cook');
    }
    paint();
    if (cook >= 6) {
      if (multi) { set('r', 'blur'); }
      else {
        set('r', 'deep');
        if (window.pengessoPop) { var r = skewer.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🍢', '💛', '🐧', '✨'], 18); }
      }
    }
  });
  mDeep.addEventListener('click', function () { mode('deep'); });
  mMulti.addEventListener('click', function () { mode('multi'); });
  again.addEventListener('click', reset);
  paint();
})();