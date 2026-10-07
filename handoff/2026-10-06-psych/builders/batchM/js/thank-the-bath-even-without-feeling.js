
/* 🛁 ありがとう連打：JS は data-*・class・style（位置とメーター）・絵文字・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var objs = [].slice.call(g.querySelectorAll('.obj')), heart = g.querySelector('.heart'), bar = g.querySelector('.hm-bar i'),
      cnt = g.querySelector('.cnt-n'), ty = g.querySelector('.ty');
  var GOAL = 12, total = 0, counts = objs.map(function () { return 0; });
  var HEART = ['🤍', '💗', '❤️', '💖'];
  function stage(n) { return n >= GOAL ? 3 : n >= 8 ? 2 : n >= 4 ? 1 : 0; }
  function bump(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function paint() {
    var st = stage(total), old = g.getAttribute('data-st');
    g.setAttribute('data-st', String(st));
    heart.textContent = HEART[st];
    if (String(st) !== old) bump(heart, 'pop');
    bar.style.width = Math.min(100, total / GOAL * 100) + '%';
    cnt.textContent = String(total);
    return String(st) !== old ? st : -1;
  }
  objs.forEach(function (o, i) {
    o.addEventListener('click', function () {
      total++; counts[i]++;
      o.querySelector('.o-n').textContent = String(counts[i]);
      o.classList.add('got');
      bump(o.querySelector('.o-e'), 'jelly');
      var gr = g.getBoundingClientRect(), r = o.getBoundingClientRect();
      ty.style.left = (r.left - gr.left + r.width / 2) + 'px';
      ty.style.top = (r.top - gr.top + 10) + 'px';
      bump(ty, 'fly');
      var changed = paint();
      if (changed === 3 && window.pengessoPop) {
        var h = heart.getBoundingClientRect();
        window.pengessoPop(h.left + h.width / 2, h.top + h.height / 2, ['💖', '🛁', '☕', '🐧', '✨'], 22);
        if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
      }
      if (g.getAttribute('data-every') !== '1' && counts.every(function (c) { return c > 0; })) {
        g.setAttribute('data-every', '1');
        if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🌈', '✨'], 10);
      }
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    total = 0; counts = objs.map(function () { return 0; });
    objs.forEach(function (o) { o.classList.remove('got'); o.querySelector('.o-n').textContent = '0'; });
    g.setAttribute('data-every', '0'); ty.classList.remove('fly'); paint();
  });
  paint();
})();
