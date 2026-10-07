/* 🍰 ランチョン・テクニック：JS は data-place / data-res / data-all / class / 絵文字だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var pls = [].slice.call(g.querySelectorAll('.pl'));
  var word = g.querySelector('.word'), react = g.querySelector('.react'), say = g.querySelector('.say');
  var rRoom = g.querySelector('.r-room'), rCake = g.querySelector('.r-cake');
  var place = 'room', tried = {}, timer = 0, busy = 0;
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function setPlace(p) {
    place = p; g.setAttribute('data-place', p); g.setAttribute('data-res', '');
    pls.forEach(function (b) { var on = b.getAttribute('data-pl') === p; b.classList.toggle('sel', on); b.setAttribute('aria-pressed', on ? 'true' : 'false'); });
    react.textContent = p === 'cake' ? '😋' : '😐';
  }
  pls.forEach(function (b) { b.addEventListener('click', function () { if (!busy) setPlace(b.getAttribute('data-pl')); }); });
  g.querySelector('.sayit').addEventListener('click', function () {
    if (busy) return; busy = 1;
    var cake = place === 'cake';
    g.setAttribute('data-res', '');
    word.textContent = '💬';
    word.classList.remove('fly-ok', 'fly-back'); void word.offsetWidth;
    word.classList.add(cake ? 'fly-ok' : 'fly-back');
    if (!cake) setTimeout(function () { word.textContent = '🪃'; }, 480);
    clearTimeout(timer);
    timer = setTimeout(function () {
      busy = 0;
      g.setAttribute('data-res', cake ? 'ok' : 'bounce');
      restart(say, 'show');
      react.textContent = cake ? '😊' : '😤'; restart(react, 'boing');
      var b = cake ? rCake : rRoom;
      b.textContent = cake ? '⭕' : '🪃'; restart(b, 'new');
      tried[place] = 1;
      var all = tried.room && tried.cake;
      var was = g.getAttribute('data-all') === '1';
      g.setAttribute('data-all', all ? '1' : '0');
      if (cake && window.pengessoPop) {
        var r = react.getBoundingClientRect();
        window.pengessoPop(r.left, r.top + 10, all && !was ? ['🍰', '🎉', '🐧', '✨'] : ['🍰', '💗', '✨'], all && !was ? 20 : 12);
      }
    }, cake ? 700 : 1100);
  });
  g.querySelector('.reset').addEventListener('click', function () {
    clearTimeout(timer); busy = 0; tried = {};
    rRoom.textContent = '❔'; rCake.textContent = '❔';
    word.classList.remove('fly-ok', 'fly-back');
    g.setAttribute('data-all', '0'); setPlace('room');
  });
})();