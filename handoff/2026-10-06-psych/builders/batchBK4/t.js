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


/* ⚡ 8つの合言葉 → 今日の1つ：JS は class・data-*・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var cards = [].slice.call(g.querySelectorAll('.mc')), mn = g.querySelector('.mn'), KEY = 'pengesso-just-one-thing-today-pick';
  function opened() { return g.querySelectorAll('.mc.open').length; }
  cards.forEach(function (c) {
    c.addEventListener('click', function () {
      if (c.classList.contains('turn')) return;
      c.classList.add('turn');
      /* 横向き（幅0）のときに表と裏を入れかえる。backface は使わない（iPhone で裏の字が鏡文字で透けるため） */
      setTimeout(function () {
        c.classList.toggle('open');
        var k = opened(); mn.textContent = k;
        if (k === 8 && g.getAttribute('data-s') === 'cards') {
          g.setAttribute('data-s', 'pick');
          var r = g.getBoundingClientRect();
          if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, Math.max(80, r.top + 120), ['💰', '🔢', '🚢', '😬', '⏹️', '🌊', '🌌', '👣'], 16);
        }
      }, 180);
      setTimeout(function () { c.classList.remove('turn'); }, 380);
    });
  });
  [].slice.call(g.querySelectorAll('.chip')).forEach(function (ch) {
    ch.addEventListener('click', function () {
      var p = ch.getAttribute('data-p');
      g.setAttribute('data-p', p); g.setAttribute('data-s', 'one');
      try { localStorage.setItem(KEY, p); } catch (e) {}
    });
  });
  g.querySelector('.b-done').addEventListener('click', function (e) {
    g.setAttribute('data-s', 'done');
    var r = g.querySelector('.one').getBoundingClientRect();
    if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['✅', '🐧', '🎉', '✨'], 20);
    if (navigator.vibrate) { try { navigator.vibrate(30); } catch (er) {} }
  });
  g.querySelector('.b-re').addEventListener('click', function () { g.setAttribute('data-p', ''); g.setAttribute('data-s', 'pick'); });
  g.querySelector('.b-over').addEventListener('click', function () {
    cards.forEach(function (c) { c.classList.remove('open', 'turn'); }); mn.textContent = '0';
    g.setAttribute('data-p', ''); g.setAttribute('data-s', 'cards');
  });
})();
