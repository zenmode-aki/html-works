/* 💐 スイッチ2つの褒め言葉：JS は data-* / class / 絵文字 / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var KEY = 'pengesso-praise-with-you-and-i-done';
  var tabs = [].slice.call(g.querySelectorAll('.scene-tab'));
  var swY = g.querySelector('.sw-you'), swI = g.querySelector('.sw-i');
  var react = g.querySelector('.fr-react'), bar = g.querySelector('.hm-bar i'), num = g.querySelector('.hm-n');
  var dots = [].slice.call(g.querySelectorAll('.cdot')), cN = g.querySelector('.c-n');
  var REACT = { '0': '💭', y: '🙂', i: '❔', yi: '🥰' };
  var LEVEL = { '0': 0, y: 45, i: 15, yi: 100 };
  var scene = 0, you = false, me = false, done = {};
  try { done = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch (e) { done = {}; }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(done)); } catch (e) {} }
  function restart(el, c) { el.classList.remove(c); void el.offsetWidth; el.classList.add(c); }
  function count() {
    var n = 0;
    dots.forEach(function (d, k) { var on = !!done[k]; d.classList.toggle('on', on); if (on) n++; });
    cN.textContent = n + '/3';
    g.setAttribute('data-all', n === 3 ? '1' : '0');
    return n;
  }
  function draw() {
    var l = you && me ? 'yi' : you ? 'y' : me ? 'i' : '0';
    g.setAttribute('data-scene', String(scene));
    g.setAttribute('data-y', you ? '1' : '0');
    g.setAttribute('data-i', me ? '1' : '0');
    g.setAttribute('data-l', l);
    swY.setAttribute('aria-pressed', you ? 'true' : 'false');
    swI.setAttribute('aria-pressed', me ? 'true' : 'false');
    tabs.forEach(function (t, k) { t.setAttribute('aria-pressed', k === scene ? 'true' : 'false'); });
    react.textContent = REACT[l];
    bar.style.width = LEVEL[l] + '%';
    num.textContent = String(LEVEL[l]);
    return l;
  }
  function flip(which) {
    if (which === 'y') you = !you; else me = !me;
    var l = draw();
    restart(react, 'boing');
    if (l !== 'yi') return;
    var before = count();
    done[scene] = 1; save();
    var after = count();
    if (navigator.vibrate) { try { navigator.vibrate(25); } catch (e) {} }
    if (!window.pengessoPop) return;
    var r = bar.getBoundingClientRect(), x = r.left + r.width / 2, y = r.top + r.height / 2;
    if (after === 3 && before < 3) window.pengessoPop(x, y, ['🎉', '🐧', '💖', '💐', '✨'], 22);
    else window.pengessoPop(x, y, ['💖', '✨', '🐧'], 14);
  }
  tabs.forEach(function (t, k) {
    t.addEventListener('click', function () { scene = k; you = false; me = false; draw(); restart(react, 'boing'); });
  });
  swY.addEventListener('click', function () { flip('y'); });
  swI.addEventListener('click', function () { flip('i'); });
  g.querySelector('.reset').addEventListener('click', function () {
    done = {}; save(); scene = 0; you = false; me = false; draw(); count();
  });
  draw(); count();
})();