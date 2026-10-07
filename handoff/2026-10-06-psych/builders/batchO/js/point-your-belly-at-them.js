/* 🐧 3つのスイッチ：JS は data-b / data-h / data-s / data-n / aria-pressed / 絵文字だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var REACT = ['🥶', '😐', '🙂', '🥰'];
  var sws = [].slice.call(g.querySelectorAll('.sw'));
  var react = g.querySelector('.react'), say = g.querySelector('.say');
  var st = { b: 0, h: 0, s: 0 };
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function draw(anim) {
    var n = st.b + st.h + st.s;
    g.setAttribute('data-b', String(st.b)); g.setAttribute('data-h', String(st.h)); g.setAttribute('data-s', String(st.s));
    var before = +g.getAttribute('data-n');
    g.setAttribute('data-n', String(n));
    sws.forEach(function (w) { w.setAttribute('aria-pressed', st[w.getAttribute('data-k')] ? 'true' : 'false'); });
    react.textContent = REACT[n];
    if (anim) { restart(react, 'boing'); restart(say, 'show'); }
    if (anim && n === 3 && before < 3 && window.pengessoPop) {
      var r = react.getBoundingClientRect();
      window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🔥', '💖', '🐧', '✨'], 20);
    }
  }
  sws.forEach(function (w) {
    w.addEventListener('click', function () { var k = w.getAttribute('data-k'); st[k] = st[k] ? 0 : 1; draw(true); });
  });
  g.querySelector('.reset').addEventListener('click', function () { st = { b: 0, h: 0, s: 0 }; draw(true); });
  draw(false);
})();