/* 💌 ありがとうタイムライン：JS は data-* / class / style / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var stops = [].slice.call(g.querySelectorAll('.stop'));
  var heart = g.querySelector('.heart'), bar = g.querySelector('.gbar i');
  var thx = g.querySelector('.thx'), later = g.querySelector('.later');
  var st = 0, level = 0, count = 0, said = false;
  var MAX = 7;
  function restart(el, c) { el.classList.remove(c); void el.offsetWidth; el.classList.add(c); }
  function draw() {
    g.setAttribute('data-st', String(st));
    stops.forEach(function (s, i) { s.classList.toggle('here', i === st); });
    thx.disabled = said;
    heart.style.transform = 'scale(' + (0.5 + Math.min(level, MAX) * 0.17) + ')';
    heart.classList.toggle('lit', level > 0);
    heart.classList.toggle('glow', level >= 5);
    bar.style.width = (Math.min(level, MAX) / MAX * 100) + '%';
  }
  thx.addEventListener('click', function () {
    if (said || st > 2) return;
    said = true; stops[st].classList.add('said');
    var say, add;
    if (st === 0) { say = 'a'; add = 1; }
    else if (st === 1) { say = count ? 'b' : 'd'; add = 2; }
    else { say = count ? 'c' : 'd'; add = count ? 4 : 2; }
    count++; level += add;
    g.setAttribute('data-say', say);
    draw();
    if (window.pengessoPop) {
      var r = heart.getBoundingClientRect();
      window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, say === 'c' ? ['💛', '✨', '🐧', '💌'] : ['💌', '✨'], say === 'c' ? 20 : 8);
    }
  });
  later.addEventListener('click', function () {
    if (st > 2) return;
    st++; said = false;
    if (st === 3) g.setAttribute('data-end', level >= 5 ? 'big' : level > 0 ? 'mid' : 'zero');
    else g.setAttribute('data-say', '');
    draw();
  });
  g.querySelector('.again').addEventListener('click', function () {
    st = 0; level = 0; count = 0; said = false;
    stops.forEach(function (s) { s.classList.remove('said'); });
    g.setAttribute('data-say', ''); g.setAttribute('data-end', '');
    draw();
  });
  draw();
})();