/* 🌟 ペンギン座：カードをめくると、その教えの星が灯る（頭＝言葉、心＝まず自分、つばさ＝手放す・完璧じゃなくていい、足＝小さな一歩・体が土台）。
   両はしの星が灯った線は、つながって描かれる。6つでペンギンとパンダが出てきて「読んでくれてありがとう」。JS は data-* と class と数字だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var cards = [].slice.call(g.querySelectorAll('.lc')), stars = [].slice.call(g.querySelectorAll('.st')), lines = [].slice.call(g.querySelectorAll('.ln'));
  var cn = g.querySelector('.cn'), again = g.querySelector('.again'), stamp = g.querySelector('.stamp'), sky = g.querySelector('.sky');
  var KEY = 'pengesso-six-lessons-from-the-panda-done', lit = [false, false, false, false, false, false], n = 0;
  try { if (localStorage.getItem(KEY) === '1') stamp.hidden = false; } catch (e) {}
  function pop(el, list, k) {
    if (!window.pengessoPop) return;
    var r = el.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, k);
  }
  function drawLines() {
    lines.forEach(function (l) {
      var a = +l.getAttribute('data-a'), b = +l.getAttribute('data-b');
      l.classList.toggle('on', lit[a] && lit[b]);
    });
  }
  cards.forEach(function (c, i) {
    c.addEventListener('click', function () {
      g.setAttribute('data-open', i);
      if (lit[i]) return;
      lit[i] = true; n++; cn.textContent = n;
      c.classList.add('flip');
      stars[i].classList.add('on', 'twinkle');
      drawLines();
      pop(c, i === 1 ? ['💗', '✨'] : ['⭐', '✨'], 8);
      if (n >= 6) {
        g.setAttribute('data-s', 'done');
        try { localStorage.setItem(KEY, '1'); } catch (e) {}
        setTimeout(function () { pop(sky, ['🐧', '🐼', '⭐', '🌟', '✨', '💛'], 26); }, 700);
        setTimeout(function () { pop(g.querySelector('.finale'), ['💛', '🐧', '🐼', '✨'], 16); }, 1300);
        if (navigator.vibrate) { try { navigator.vibrate([30, 60, 30]); } catch (e) {} }
      }
    });
  });
  again.addEventListener('click', function () {
    lit = [false, false, false, false, false, false]; n = 0; cn.textContent = '0';
    cards.forEach(function (c) { c.classList.remove('flip'); });
    stars.forEach(function (s) { s.classList.remove('on', 'twinkle'); });
    drawLines();
    g.setAttribute('data-open', ''); g.setAttribute('data-s', 'play');
    if (sky.scrollIntoView) { try { sky.scrollIntoView({ block: 'center', behavior: 'smooth' }); } catch (e) {} }
  });
})();