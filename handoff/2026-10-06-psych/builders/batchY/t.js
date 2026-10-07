document.documentElement.className += " js";

(function () {
  var items = [].slice.call(document.querySelectorAll('.card, .game, .next'));
  function showAll() { items.forEach(function (el) { el.classList.add('in'); }); }
  if (!('IntersectionObserver' in window)) { showAll(); return; }
  var seen = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); seen.unobserve(e.target); } });
  }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
  items.forEach(function (el) { seen.observe(el); });
  setTimeout(function () { if (!document.querySelector('.card.in, .next.in')) showAll(); }, 1600);
})();


/* ⚡ 機械？自分？（くり返しの作業を機械に分けると、ういた時間がたまる）：JS は class・data-*・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var ANS = ['m', 'm', 'p', 'm', 'p', 'm'], MIN = [40, 30, 0, 5, 0, 20];
  var q = 0, saved = 0, qi = g.querySelector('.qi'), sv = g.querySelector('.sv-n');
  function paint() { g.setAttribute('data-q', String(q)); qi.textContent = String(Math.min(q + 1, 6)); sv.textContent = String(saved); }
  [].forEach.call(g.querySelectorAll('.bin'), function (b) {
    b.addEventListener('click', function () {
      if (q >= 6) return;
      var a = b.getAttribute('data-a');
      g.setAttribute('data-fb', '');
      void g.offsetWidth;   /* 同じ答えが続いても、動きをもう一度 */
      if (a !== ANS[q]) { g.setAttribute('data-fb', 'x'); return; }
      g.setAttribute('data-fb', a);
      saved += MIN[q]; q++; paint();
      if (q === 6) {
        g.setAttribute('data-end', '1');
        if (window.pengessoPop) { var r = g.querySelector('.taskbox').getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🤖', '⏱', '🐧', '✨'], 20); }
      } else if (a === 'm' && window.pengessoPop) {
        var k = b.getBoundingClientRect(); window.pengessoPop(k.left + k.width / 2, k.top + k.height / 2, ['⚡', '🤖'], 6);
      }
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    q = 0; saved = 0; g.setAttribute('data-fb', ''); g.setAttribute('data-end', '0'); paint();
  });
  paint();
})();
