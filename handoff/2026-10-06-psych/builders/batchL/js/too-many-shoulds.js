/* 🪨→🎈 「べき」を「〜だといいな」に：JS は class / aria / style / 絵文字 / data-* だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var stones = [].slice.call(g.querySelectorAll('.stone')), balloons = [].slice.call(g.querySelectorAll('.balloons i')),
      rocks = [].slice.call(g.querySelectorAll('.rocks i')), rider = g.querySelector('.rider'), face = g.querySelector('.face'),
      barMe = g.querySelector('.bar.me i'), barOt = g.querySelector('.bar.ot i');
  var FACES = ['😣', '😟', '😐', '🙂', '😊', '😄'];
  function paint() {
    var on = stones.filter(function (s) { return s.classList.contains('on'); });
    var n = on.length;
    var me = stones.filter(function (s) { return s.getAttribute('data-t') === 'me' && !s.classList.contains('on'); }).length;
    var ot = stones.filter(function (s) { return s.getAttribute('data-t') === 'ot' && !s.classList.contains('on'); }).length;
    g.setAttribute('data-n', n);
    balloons.forEach(function (b, i) { b.classList.toggle('on', i < n); });
    rocks.forEach(function (r, i) { r.classList.toggle('off', i < n); });
    rider.style.setProperty('--up', n === 5 ? 48 : n * 8);
    face.textContent = FACES[n];
    barMe.style.width = (me / 3 * 100) + '%';
    barOt.style.width = (ot / 2 * 100) + '%';
    return n;
  }
  stones.forEach(function (s) {
    s.addEventListener('click', function () {
      if (s.classList.contains('on')) return;
      s.classList.remove('flip'); void s.offsetWidth; s.classList.add('flip');
      setTimeout(function () {
        s.classList.add('on'); s.setAttribute('aria-pressed', 'true');
        var n = paint();
        if (window.pengessoPop) {
          var r = n === 5 ? g.querySelector('.pen').getBoundingClientRect() : s.getBoundingClientRect();
          window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, n === 5 ? ['🎈', '🐧', '✨', '💛'] : ['🎈', '✨'], n === 5 ? 20 : 6);
        }
      }, 200);
    });
  });
  g.querySelector('.again').addEventListener('click', function () {
    stones.forEach(function (s) { s.classList.remove('on', 'flip'); s.setAttribute('aria-pressed', 'false'); });
    paint();
  });
  paint();
})();