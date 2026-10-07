/* 💌 挨拶の暗号：JS は data-pick / data-all / class / 絵文字 / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var KEY = 'pengesso-a-smile-greeting-says-i-like-you-found';
  var HEARTS = [0, 5, 4, 2, 1, 0];
  var REACT = ['❔', '💖', '😊', '🙂', '😕', '💔'];
  var FACE = ['✨', '😄', '🙂', '😐', '😑', '🙈'];
  var picks = [].slice.call(g.querySelectorAll('.pick'));
  var rows = [].slice.call(g.querySelectorAll('.hearts'));
  var dots = [].slice.call(g.querySelectorAll('.dot'));
  var react = g.querySelector('.react'), me = g.querySelector('.me-badge'), wave = g.querySelector('.wave');
  var msg = g.querySelector('.msg'), fN = g.querySelector('.f-n');
  var found = {};
  try { found = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch (e) { found = {}; }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(found)); } catch (e) {} }
  function drawFound() {
    var n = 0;
    dots.forEach(function (d, i) { var on = !!found[i + 1]; d.classList.toggle('on', on); if (on) n++; });
    fN.textContent = n + '/5';
    g.setAttribute('data-all', n === 5 ? '1' : '0');
    return n;
  }
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function show(v) {
    g.setAttribute('data-pick', String(v));
    picks.forEach(function (x) {
      var on = +x.getAttribute('data-v') === v;
      x.classList.toggle('sel', on); x.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
    rows.forEach(function (r) {
      [].slice.call(r.children).forEach(function (h, i) { h.classList.toggle('on', i < HEARTS[v]); });
      restart(r, 'fill');
    });
    react.textContent = REACT[v]; me.textContent = FACE[v];
  }
  drawFound();
  picks.forEach(function (b) {
    b.addEventListener('click', function () {
      var v = +b.getAttribute('data-v');
      show(v);
      restart(wave, 'go'); restart(react, 'boing'); restart(msg, 'show');
      var before = drawFound();
      found[v] = 1; save();
      var after = drawFound();
      if (!window.pengessoPop) return;
      var r = b.getBoundingClientRect(), x = r.left + r.width / 2, y = r.top + r.height / 2;
      if (after === 5 && before < 5) window.pengessoPop(x, y, ['🎉', '🐧', '💌', '✨'], 20);
      else if (v === 1) window.pengessoPop(x, y, ['💖', '🐧', '✨', '💕'], 16);
    });
  });
  g.querySelector('.reset').addEventListener('click', function () {
    found = {}; save();
    show(0); drawFound();
  });
})();