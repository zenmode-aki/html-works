/* 😎 3つのメガネ：JS は data-*・aria-pressed・数字・絵文字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var lenses = [].slice.call(g.querySelectorAll('.lens')), face = g.querySelector('.face'), num = g.querySelector('.scnum');
  var next = g.querySelector('.nextsc'), again = g.querySelector('.again');
  var FACE = ['😤', '😠', '😎'];
  var sc = 0, picks = [];
  function set(k, v) { g.setAttribute('data-' + k, v); }
  function bounce(el) { el.classList.remove('boing'); void el.offsetWidth; el.classList.add('boing'); }
  function pick(k) {
    if (g.getAttribute('data-s') !== 'play') return;
    lenses.forEach(function (b, i) { b.setAttribute('aria-pressed', i === k ? 'true' : 'false'); });
    picks[sc] = k; face.textContent = FACE[k];
    set('l', ''); void g.offsetWidth; set('l', String(k));
    if (k === 2) {
      bounce(face);
      if (window.pengessoPop) { var r = face.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['😎', '✨'], 8); }
    }
  }
  function scene(i) {
    sc = i; set('sc', String(i)); set('l', ''); num.textContent = String(i + 1); face.textContent = '🐧';
    lenses.forEach(function (b) { b.setAttribute('aria-pressed', 'false'); });
  }
  next.addEventListener('click', function () {
    if (sc < 2) { scene(sc + 1); return; }
    var cool = picks.filter(function (p) { return p === 2; }).length;
    set('r', cool === 3 ? '3' : cool > 0 ? 'some' : '0'); set('s', 'end');
    face.textContent = cool === 3 ? '😎' : cool > 0 ? '🙂' : '😤';
    if (cool === 3 && window.pengessoPop) { var r = face.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['😎', '🐧', '✨', '🥫'], 18); }
  });
  lenses.forEach(function (b, i) { b.addEventListener('click', function () { pick(i); }); });
  again.addEventListener('click', function () { picks = []; set('s', 'play'); set('r', ''); scene(0); });
  scene(0);
})();