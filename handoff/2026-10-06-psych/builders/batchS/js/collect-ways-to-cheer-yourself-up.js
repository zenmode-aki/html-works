/* 📒 ご機嫌ブック：JS は class / data-lv / data-empty / 数字 / style だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var KEY = 'pengesso-collect-ways-to-cheer-yourself-up-picks';
  var chips = [].slice.call(g.querySelectorAll('.chip'));
  var sts = [].slice.call(g.querySelectorAll('.st'));
  var n = g.querySelector('.n'), fill = g.querySelector('.fill'), msg = g.querySelector('.msg');
  var mk = { 5: g.querySelector('.m5'), 15: g.querySelector('.m15'), 25: g.querySelector('.m25') };
  var order = [];
  try { order = JSON.parse(localStorage.getItem(KEY) || '[]') || []; } catch (e) { order = []; }
  if (!Array.isArray(order)) order = [];
  order = order.filter(function (i, k) { return typeof i === 'number' && i >= 0 && i < chips.length && order.indexOf(i) === k; });
  function save() { try { localStorage.setItem(KEY, JSON.stringify(order)); } catch (e) {} }
  function lv(c) { return c >= 25 ? 3 : c >= 15 ? 2 : c >= 5 ? 1 : 0; }
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function draw() {
    var c = order.length;
    chips.forEach(function (b, i) {
      var on = order.indexOf(i) >= 0;
      b.classList.toggle('on', on); b.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
    sts.forEach(function (s, i) {
      var k = order.indexOf(i);
      s.classList.toggle('on', k >= 0); s.style.order = k >= 0 ? String(k) : '99';
    });
    n.textContent = String(c);
    fill.style.width = (c / 25 * 100) + '%';
    [5, 15, 25].forEach(function (m) { mk[m].classList.toggle('got', c >= m); });
    g.setAttribute('data-lv', String(lv(c)));
    g.setAttribute('data-empty', c ? '0' : '1');
  }
  draw();
  chips.forEach(function (b, i) {
    b.addEventListener('click', function () {
      var before = lv(order.length), k = order.indexOf(i);
      if (k >= 0) order.splice(k, 1); else order.push(i);
      save(); draw();
      var after = lv(order.length);
      if (k < 0) restart(sts[i], 'pop');
      if (after !== before) restart(msg, 'show');
      if (after > before && window.pengessoPop) {
        var r = b.getBoundingClientRect(), x = r.left + r.width / 2, y = r.top + r.height / 2;
        if (after === 3) window.pengessoPop(x, y, ['🥇', '🐧', '🎉', '✨', '📒'], 26);
        else if (after === 2) window.pengessoPop(x, y, ['🥈', '🐧', '✨'], 16);
        else window.pengessoPop(x, y, ['🥉', '🐧', '✨'], 12);
      }
    });
  });
  g.querySelector('.reset').addEventListener('click', function () { order = []; save(); draw(); restart(msg, 'show'); });
})();