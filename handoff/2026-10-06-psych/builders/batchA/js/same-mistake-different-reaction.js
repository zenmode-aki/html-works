/* ⏰ 同じミス、2つの世界：JS は data-* / aria-pressed / 幅 / 絵文字 / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var worlds = [].slice.call(g.querySelectorAll('.world'));
  var bar = g.querySelector('.tr-bar i'), num = g.querySelector('.tr-n'), badge = g.querySelector('.rb');
  var log = { chat: g.querySelector('.lg-chat'), none: g.querySelector('.lg-none') };
  var TRUST = { chat: 90, none: 15 }, FACE = { chat: '🥺', none: '😤' };
  var w = 'chat', seen = { chat: false, none: false };
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function setW(x) {
    w = x;
    g.setAttribute('data-w', x);
    g.setAttribute('data-s', 'ready');
    worlds.forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-w') === x ? 'true' : 'false'); });
    bar.style.width = '0'; num.textContent = '?';
  }
  worlds.forEach(function (b) { b.addEventListener('click', function () { setW(b.getAttribute('data-w')); }); });
  g.querySelector('.tap').addEventListener('click', function () {
    if (g.getAttribute('data-s') === 'late') { setW(w === 'chat' ? 'none' : 'chat'); return; }
    g.setAttribute('data-s', 'late');
    badge.textContent = FACE[w];
    bar.style.width = TRUST[w] + '%'; num.textContent = TRUST[w] + '%';
    var first = !seen[w]; seen[w] = true;
    log[w].textContent = FACE[w]; restart(log[w], 'boing');
    var both = seen.chat && seen.none;
    var fresh = both && g.getAttribute('data-both') !== '1';
    g.setAttribute('data-both', both ? '1' : '0');
    if (!window.pengessoPop) return;
    var r = g.querySelector('.flipcard').getBoundingClientRect();
    if (fresh) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🔍', '💬', '🐧', '✨', '🍀'], 20);
    else if (w === 'chat' && first) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['💗', '🐧', '💬'], 12);
  });
  g.querySelector('.reset').addEventListener('click', function () {
    seen = { chat: false, none: false };
    log.chat.textContent = '❔'; log.none.textContent = '❔';
    g.setAttribute('data-both', '0');
    setW('chat');
  });
})();