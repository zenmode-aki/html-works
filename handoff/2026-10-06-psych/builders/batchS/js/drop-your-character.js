/* 🥟 グリンピース：JS は data-step / class / 絵文字 / aria だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var pea = g.querySelector('.pea'), stars = g.querySelector('.stars'), me = g.querySelector('.me');
  var locks = [].slice.call(g.querySelectorAll('.lock'));
  var accs = [].slice.call(g.querySelectorAll('.acc'));
  var timer = 0;
  function restart(el, c) { el.classList.remove(c); void el.offsetWidth; el.classList.add(c); }
  function center(el) { var r = el.getBoundingClientRect(); return [r.left + r.width / 2, r.top + r.height / 2]; }
  pea.addEventListener('click', function () {
    if (g.getAttribute('data-step') !== 'pea') return;
    pea.classList.add('gone');
    var p = center(pea);
    if (window.pengessoPop) window.pengessoPop(p[0], p[1], ['🟢', '✨'], 8);
    clearTimeout(timer);
    timer = setTimeout(function () { g.setAttribute('data-step', 'wish'); restart(stars, 'twinkle'); }, 700);
  });
  locks.forEach(function (b, i) {
    b.addEventListener('click', function () {
      if (b.classList.contains('open') || g.getAttribute('data-step') === 'pea') return;
      b.classList.add('open'); b.setAttribute('aria-pressed', 'true');
      b.querySelector('.lk').textContent = '🔓';
      accs[i].classList.add('on'); restart(me, 'hop-me');
      var p = center(b);
      var n = g.querySelectorAll('.lock.open').length;
      if (n === 3) {
        g.setAttribute('data-step', 'done');
        var m = center(me);
        if (window.pengessoPop) window.pengessoPop(m[0], m[1], ['🌈', '🎤', '🧣', '🐧', '✨'], 24);
      } else if (window.pengessoPop) {
        window.pengessoPop(p[0], p[1], [accs[i].textContent, '✨'], 10);
      }
    });
  });
  g.querySelector('.reset').addEventListener('click', function () {
    clearTimeout(timer);
    pea.classList.remove('gone');
    locks.forEach(function (b) { b.classList.remove('open'); b.setAttribute('aria-pressed', 'false'); b.querySelector('.lk').textContent = '🔒'; });
    accs.forEach(function (a) { a.classList.remove('on'); });
    g.setAttribute('data-step', 'pea');
  });
})();