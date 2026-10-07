/* 🐕 脳は小さな犬：JS は data-* / class / style / 絵文字 / 数字だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var dog = g.querySelector('.dog'), bark = g.querySelector('.bark'), nbar = g.querySelector('.nbar i'),
      paws = [].slice.call(g.querySelectorAll('.paws i'));
  var noise = 2, calm = 0, lastB = 0, timer = 0;
  function st(s) { g.setAttribute('data-st', s); }
  function paint() {
    nbar.style.width = (noise / 6 * 100) + '%';
    paws.forEach(function (p, i) { p.classList.toggle('on', i < calm); });
    dog.style.setProperty('--ds', (0.85 + noise * 0.09).toFixed(2));
  }
  function restart(el, c) { el.classList.remove(c); void el.offsetWidth; el.classList.add(c); }
  function nextBark() {
    var b; do { b = 1 + Math.floor(Math.random() * 4); } while (b === lastB);
    lastB = b;
    g.setAttribute('data-b', b); restart(bark, 'new'); restart(dog, 'yap');
    dog.textContent = '🐕';
    st('bark');
  }
  function later(fn, ms) { clearTimeout(timer); timer = setTimeout(fn, ms); }
  g.querySelector('.start').addEventListener('click', function () {
    noise = 2; calm = 0; g.setAttribute('data-mood', ''); paint();
    nextBark();
  });
  g.querySelector('.back').addEventListener('click', function () {
    if (g.getAttribute('data-st') !== 'bark') return;
    noise = Math.min(6, noise + 2); calm = 0;
    g.setAttribute('data-mood', 'back'); paint();
    restart(dog, 'yap');
    if (navigator.vibrate) { try { navigator.vibrate([20, 40, 20]); } catch (e) {} }
    if (noise >= 6) { st('lose'); return; }
    st('wait'); later(nextBark, 900);
  });
  g.querySelector('.say').addEventListener('click', function () {
    if (g.getAttribute('data-st') !== 'bark') return;
    noise = Math.max(0, noise - 1); calm++;
    g.setAttribute('data-mood', 'say'); paint();
    if (calm >= 3) {
      g.setAttribute('data-b', '0'); dog.textContent = '🐶'; noise = 0; paint(); st('win');
      var r = dog.getBoundingClientRect();
      if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['💤', '🐾', '🐧', '✨'], 18);
      return;
    }
    g.setAttribute('data-b', '5'); restart(bark, 'new');
    st('wait'); later(nextBark, 1300);
  });
  paint();
})();