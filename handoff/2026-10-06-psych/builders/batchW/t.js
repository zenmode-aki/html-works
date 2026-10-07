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


/* ⚡ 朝の3分ノート（ぼんやりした感謝を具体的にすると、日がのぼる）：JS は class・data-*・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var m = 0, happy = 3, bar = g.querySelector('.hp-bar i');
  function paint() {
    g.setAttribute('data-m', String(m));
    g.querySelector('.mm').textContent = m;
    g.querySelector('.hp-n').textContent = happy;
    bar.style.width = Math.round(happy / 9 * 100) + '%';
  }
  [].forEach.call(g.querySelectorAll('.ln'), function (b) {
    b.addEventListener('click', function () {
      if (b.getAttribute('data-v') === '1') return;
      b.setAttribute('data-v', '1');
      m++; happy += 2; paint();   /* ぼんやり +1 → 具体的 +3 なので、1行につき +2 */
      if (window.pengessoPop) {
        var r = b.getBoundingClientRect();
        window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, m === 3 ? ['☀️', '🌅', '🐧', '✨', '🍵'] : ['✨', '😊'], m === 3 ? 20 : 8);
      }
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    m = 0; happy = 3;
    [].forEach.call(g.querySelectorAll('.ln'), function (b) { b.setAttribute('data-v', '0'); });
    paint();
  });
})();
