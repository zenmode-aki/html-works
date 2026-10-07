/* ☕ 「今日はおごるよ」クイズ：JS は data-a / data-all / class / 絵文字 / 数字だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var KEY = 'pengesso-next-time-its-my-treat-tried';
  var REACT = { a: '😊', b: '😅', c: '😆' };
  var opts = [].slice.call(g.querySelectorAll('.opt'));
  var react = g.querySelector('.react'), say = g.querySelector('.say'), verdict = g.querySelector('.verdict'), trN = g.querySelector('.tr-n');
  var tried = {};
  try { tried = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch (e) { tried = {}; }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(tried)); } catch (e) {} }
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function count() {
    var n = (tried.a ? 1 : 0) + (tried.b ? 1 : 0) + (tried.c ? 1 : 0);
    trN.textContent = n + '/3';
    g.setAttribute('data-all', n === 3 ? '1' : '0');
    return n;
  }
  function choose(a) {
    g.setAttribute('data-a', a || '0');
    opts.forEach(function (o) { var on = o.getAttribute('data-a') === a; o.classList.toggle('sel', on); o.setAttribute('aria-pressed', on ? 'true' : 'false'); });
    react.textContent = a ? REACT[a] : '🍰';
    if (a) { restart(react, 'boing'); restart(say, 'show'); restart(verdict, 'show'); }
  }
  count();
  opts.forEach(function (o) {
    o.addEventListener('click', function () {
      var a = o.getAttribute('data-a');
      choose(a);
      var before = count(); tried[a] = 1; save(); var after = count();
      if (!window.pengessoPop) return;
      var r = o.getBoundingClientRect(), x = r.left + r.width / 2, y = r.top + r.height / 2;
      if (after === 3 && before < 3) window.pengessoPop(x, y, ['🏆', '🐧', '☕', '✨'], 20);
      else if (a === 'c') window.pengessoPop(x, y, ['🍰', '☕', '🐧', '💛'], 16);
    });
  });
  g.querySelector('.reset').addEventListener('click', function () { tried = {}; save(); choose(''); count(); });
})();