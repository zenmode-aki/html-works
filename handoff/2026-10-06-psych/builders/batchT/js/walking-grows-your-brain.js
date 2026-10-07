/* 👟 歩いた日をタップ → 週3回で季節が1つ進み、脳の木が育つ。4つの季節で1年。JS は class / data-* / 数字 / 絵文字だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var days = g.querySelectorAll('.day'), seasons = g.querySelectorAll('.se');
  var sprout = g.querySelector('.sprout'), steps = g.querySelector('.steps'), wn = g.querySelector('.wn');
  var again = g.querySelector('.again'), plant = g.querySelector('.plant');
  var TREE = ['', '🌱', '🌿', '🪴', '🌳'];
  var season = 0, total = 0, busy = false;
  function count() { var c = 0; for (var i = 0; i < days.length; i++) if (days[i].classList.contains('on')) c++; return c; }
  function fmt(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ','); }
  function pop(el, list, k) {
    if (!window.pengessoPop || !el) return;
    var r = el.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, k);
  }
  function render() {
    g.setAttribute('data-season', season);
    g.setAttribute('data-done', season >= 4 ? '1' : '0');
    sprout.textContent = TREE[season];
    for (var i = 0; i < seasons.length; i++) seasons[i].classList.toggle('on', i < season);
    steps.textContent = fmt(total);
    wn.textContent = count();
  }
  for (var i = 0; i < days.length; i++) {
    days[i].addEventListener('click', function () {
      if (busy || season >= 4) return;
      var on = this.classList.toggle('on');
      total += on ? 4000 : -4000;
      render();
      if (count() >= 3) {
        busy = true;
        setTimeout(function () {
          season++;
          for (var j = 0; j < days.length; j++) days[j].classList.remove('on');
          render();
          sprout.classList.remove('grow'); void sprout.offsetWidth; sprout.classList.add('grow');
          busy = false;
          if (season >= 4) {
            pop(plant, ['🌳', '🧠', '👟', '✨', '🐧'], 20);
            if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
          } else {
            pop(plant, ['🌱', '👟', '✨'], 8);
          }
        }, 450);
      }
    });
  }
  again.addEventListener('click', function () {
    season = 0; total = 0; busy = false;
    for (var j = 0; j < days.length; j++) days[j].classList.remove('on');
    render();
  });
  render();
})();