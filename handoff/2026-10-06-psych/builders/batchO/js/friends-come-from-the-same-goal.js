/* 🧲 自分の輪を見つけよう：JS は data-pick / data-all / class / style の位置 / 絵文字 / 数字だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var KEY = 'pengesso-friends-come-from-the-same-goal-found';
  var ICON = { ball: '⚾', cafe: '☕', book: '📚', play: '🎮' };
  var SLOTS = [[25, 44], [75, 44]];
  var pgs = [].slice.call(g.querySelectorAll('.pg'));
  var chips = [].slice.call(g.querySelectorAll('.chip'));
  var stamps = [].slice.call(g.querySelectorAll('.stamp'));
  var me = g.querySelector('.me'), meHob = g.querySelector('.me .hob'), talk = g.querySelector('.talk'), fN = g.querySelector('.f-n');
  var homes = pgs.map(function (p) { return [p.style.left, p.style.top]; });
  var found = {}, hopTimer = 0;
  try { found = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch (e) { found = {}; }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(found)); } catch (e) {} }
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function drawFound() {
    var n = 0;
    stamps.forEach(function (s) { var on = !!found[s.getAttribute('data-h')]; s.classList.toggle('on', on); if (on) n++; });
    fN.textContent = n + '/4';
    g.setAttribute('data-all', n === 4 ? '1' : '0');
    return n;
  }
  function pick(h) {
    g.setAttribute('data-pick', h || '0');
    chips.forEach(function (c) { var on = c.getAttribute('data-h') === h; c.classList.toggle('sel', on); c.setAttribute('aria-pressed', on ? 'true' : 'false'); });
    var k = 0;
    clearTimeout(hopTimer);
    pgs.forEach(function (p, i) {
      p.classList.remove('hop');
      var match = h && p.getAttribute('data-h') === h;
      if (match) { p.style.left = SLOTS[k][0] + '%'; p.style.top = SLOTS[k][1] + '%'; k++; }
      else { p.style.left = homes[i][0]; p.style.top = homes[i][1]; }
      p.classList.toggle('close', !!match);
      p.classList.toggle('dim', !!h && !match);
    });
    meHob.textContent = h ? ICON[h] : '❔';
    if (h) {
      restart(meHob, 'boing'); restart(talk, 'show');
      hopTimer = setTimeout(function () { pgs.forEach(function (p) { if (p.classList.contains('close')) restart(p, 'hop'); }); }, 760);
    }
  }
  drawFound();
  chips.forEach(function (c) {
    c.addEventListener('click', function () {
      var h = c.getAttribute('data-h');
      pick(h);
      var before = drawFound();
      found[h] = 1; save();
      var after = drawFound();
      if (!window.pengessoPop) return;
      var r = me.getBoundingClientRect(), x = r.left + r.width / 2, y = r.top + r.height / 2;
      setTimeout(function () {
        if (after === 4 && before < 4) window.pengessoPop(x, y, ['🎉', '🐧', ICON[h], '✨'], 22);
        else window.pengessoPop(x, y, [ICON[h], '🐧', '✨'], 12);
      }, 650);
    });
  });
  g.querySelector('.reset').addEventListener('click', function () { found = {}; save(); pick(''); drawFound(); });
})();