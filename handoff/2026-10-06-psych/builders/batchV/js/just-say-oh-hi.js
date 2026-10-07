/* 🎫 話しかけ予約券：3つのひとことで相手の反応が変わる（data-c）。「あっ、どうも」だけ予約券 → 5分後「この席、空いてますか？」。JS は data-* と class と絵文字だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var a = g.querySelector('.ch-a'), b = g.querySelector('.ch-b'), c = g.querySelector('.ch-c'), seat = g.querySelector('.seat'), again = g.querySelector('.again');
  var me = g.querySelector('.me'), them = g.querySelector('.them'), face = g.querySelector('.pp-f');
  function pop(el, list, k) {
    if (!window.pengessoPop) return;
    var r = el.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, k);
  }
  function redo(el, cl) { el.classList.remove(cl); void el.offsetWidth; el.classList.add(cl); }
  var busy = false;
  function can() { return g.getAttribute('data-s') === 'ask' && !busy; }
  a.addEventListener('click', function () { if (!can()) return; g.setAttribute('data-c', 'a'); face.textContent = '🤨'; redo(them, 'shake'); });
  b.addEventListener('click', function () { if (!can()) return; g.setAttribute('data-c', 'b'); face.textContent = '😐'; redo(them, 'shake'); });
  c.addEventListener('click', function () {
    if (!can()) return;
    busy = true;
    g.setAttribute('data-c', 'c'); face.textContent = '🙂'; redo(me, 'bow');
    setTimeout(function () {
      busy = false;
      if (g.getAttribute('data-s') !== 'ask') return;
      g.setAttribute('data-s', 'ticket');
      pop(g.querySelector('.ticket'), ['🎫', '✨'], 10);
    }, 700);
  });
  seat.addEventListener('click', function () {
    if (g.getAttribute('data-s') !== 'ticket') return;
    g.setAttribute('data-c', 'd'); face.textContent = '😊';
    g.setAttribute('data-s', 'done');
    setTimeout(function () { pop(them, ['🐧', '🪑', '🎫', '✨', '💛'], 16); }, 300);
    if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
  });
  again.addEventListener('click', function () {
    face.textContent = '😶';
    g.setAttribute('data-c', ''); g.setAttribute('data-s', 'ask');
  });
})();