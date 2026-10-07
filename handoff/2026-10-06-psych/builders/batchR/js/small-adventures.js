/* 🧭 分かれ道ガチャ：JS は data-*・class・数字・絵文字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var road = g.querySelector('.road'), brain = g.querySelector('.brain'), card = g.querySelector('.card2');
  var ads = [].slice.call(g.querySelectorAll('.ad'));
  var idle = ads[0], same = ads[1], adv = ads.slice(2);
  var boxes = [].slice.call(g.querySelectorAll('.tries i')), tn = g.querySelector('.tn');
  var left = g.querySelector('.left'), right = g.querySelector('.right'), again = g.querySelector('.again');
  var BRAIN = ['🧠', '🧠', '😪', '😴', '💤'];
  var tries = 0, yawns = 0, goldAt = 0, order = [], walkT = 0;
  function shuffle(a) { for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function showAd(el) { ads.forEach(function (a) { a.classList.remove('now'); }); void el.offsetWidth; el.classList.add('now'); }
  function setR(r) { g.setAttribute('data-r', ''); void g.offsetWidth; g.setAttribute('data-r', r); }
  function walk(dir) { clearTimeout(walkT); road.setAttribute('data-go', dir); walkT = setTimeout(function () { road.setAttribute('data-go', ''); }, 900); }
  function reset() {
    tries = 0; yawns = 0; goldAt = 5 + Math.floor(Math.random() * 6); order = shuffle(adv.slice());
    tn.textContent = '0'; brain.textContent = BRAIN[0];
    boxes.forEach(function (b) { b.className = ''; b.textContent = ''; });
    showAd(idle); g.setAttribute('data-s', 'play'); g.setAttribute('data-r', ''); road.setAttribute('data-go', '');
  }
  left.addEventListener('click', function () {
    if (g.getAttribute('data-s') !== 'play') return;
    walk('left'); yawns = Math.min(BRAIN.length - 1, yawns + 1); brain.textContent = BRAIN[yawns];
    showAd(same); setR('same');
  });
  right.addEventListener('click', function () {
    if (g.getAttribute('data-s') !== 'play') return;
    walk('right'); tries++; yawns = 0; brain.textContent = '🧠';
    var el = order[(tries - 1) % order.length]; showAd(el);
    var b = boxes[tries - 1]; b.className = 'done';
    tn.textContent = String(tries);
    if (tries === goldAt) {
      b.className = 'gold'; b.textContent = '💛'; setR('gold');
      if (window.pengessoPop) { var r = card.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['💛', '🌟', '🐧', '✨'], 18); }
    } else {
      setR(['ok', 'oh', 'nice'][Math.floor(Math.random() * 3)]);
    }
    if (tries >= 10) {
      g.setAttribute('data-s', 'end');
      if (window.pengessoPop) { var r2 = card.getBoundingClientRect(); window.pengessoPop(r2.left + r2.width / 2, r2.top + r2.height / 2, ['🧭', '🐧', '🎉'], 12); }
    }
  });
  again.addEventListener('click', reset);
  reset();
})();