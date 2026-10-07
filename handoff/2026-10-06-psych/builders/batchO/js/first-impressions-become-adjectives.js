/* 🏷️ 形容詞スロット：JS は data-l / data-c / data-all / class / disabled / 絵文字だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var KEY = 'pengesso-first-impressions-become-adjectives-board';
  var AE = ['📚', '😂', '🧹'];
  var lens = [].slice.call(g.querySelectorAll('.ln')), acts = [].slice.call(g.querySelectorAll('.act'));
  var cells = [].slice.call(g.querySelectorAll('.cell'));
  var reel = g.querySelector('.reel'), sky = g.querySelector('.sky'), ae = g.querySelector('.act-e');
  var l = '', done = {}, spinT = 0, stopT = 0;
  try { done = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch (e) { done = {}; }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(done)); } catch (e) {} }
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function drawBoard() {
    var n = 0;
    cells.forEach(function (c) { var i = +c.getAttribute('data-i'); var on = !!done[i]; c.classList.toggle('on', on); c.textContent = on ? (i < 3 ? '👎' : '👍') : '·'; if (on) n++; });
    g.setAttribute('data-all', n === 6 ? '1' : '0');
    return n;
  }
  function setLens(v) {
    l = v; g.setAttribute('data-l', v); g.setAttribute('data-c', 'n');
    lens.forEach(function (b) { var on = b.getAttribute('data-l') === v; b.classList.toggle('sel', on); b.setAttribute('aria-pressed', on ? 'true' : 'false'); });
    acts.forEach(function (a) { a.disabled = !v; });
    sky.textContent = v === 'b' ? '☀️' : '☁️';
    ae.textContent = '';
  }
  lens.forEach(function (b) { b.addEventListener('click', function () { setLens(b.getAttribute('data-l')); }); });
  acts.forEach(function (a) {
    a.addEventListener('click', function () {
      if (!l) return;
      var ai = +a.getAttribute('data-a'), target = (l === 'b' ? 3 : 0) + ai, k = 0;
      ae.textContent = AE[ai]; restart(ae, 'boing');
      clearInterval(spinT); clearTimeout(stopT);
      reel.classList.remove('land'); reel.classList.add('spin');
      var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
      spinT = setInterval(function () { g.setAttribute('data-c', String(k++ % 6)); }, 80);
      stopT = setTimeout(function () {
        clearInterval(spinT);
        g.setAttribute('data-c', String(target));
        reel.classList.remove('spin'); restart(reel, 'land');
        var before = drawBoard(); done[target] = 1; save(); var after = drawBoard();
        if (window.pengessoPop) {
          var r = reel.getBoundingClientRect(), x = r.left + r.width / 2, y = r.top + r.height / 2;
          if (after === 6 && before < 6) window.pengessoPop(x, y, ['🎉', '🏷️', '🐧', '✨'], 22);
          else if (target >= 3) window.pengessoPop(x, y, ['☀️', '✨', '🐧'], 10);
        }
      }, reduce ? 60 : 850);
    });
  });
  g.querySelector('.reset').addEventListener('click', function () { clearInterval(spinT); clearTimeout(stopT); reel.classList.remove('spin'); done = {}; save(); setLens(''); drawBoard(); });
  drawBoard();
})();