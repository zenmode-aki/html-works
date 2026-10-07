/* 🔭 動物園モード：JS は data-* / class / style / 絵文字 だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var ANIM = { 1: 'roar', 2: 'turn', 3: 'show' };
  var modes = [].slice.call(g.querySelectorAll('.mode'));
  var pens = [].slice.call(g.querySelectorAll('.pen'));
  var bar = g.querySelector('.bar i'), msg = g.querySelector('.msg');
  var anger = 30, notes = {};
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function drawAnger() { bar.style.width = Math.max(3, anger) + '%'; }
  function setMode(m) {
    g.setAttribute('data-mode', m);
    modes.forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-v') === m ? 'true' : 'false'); });
  }
  modes.forEach(function (b) { b.addEventListener('click', function () { setMode(b.getAttribute('data-v')); }); });
  pens.forEach(function (p) {
    p.addEventListener('click', function () {
      var a = p.getAttribute('data-a'), zoo = g.getAttribute('data-mode') === 'zoo';
      var stamp = p.querySelector('.stamp');
      restart(p.querySelector('.an'), ANIM[a]);
      if (zoo) {
        anger = Math.max(0, anger - 30);
        notes[a] = 1; stamp.textContent = '📝'; p.classList.remove('mad'); p.classList.add('noted');
        var n = Object.keys(notes).length;
        g.setAttribute('data-m', n >= 3 && anger === 0 ? 'zall' : 'z' + a);
        if (n >= 3 && anger === 0 && window.pengessoPop) {
          var k = p.getBoundingClientRect();
          window.pengessoPop(k.left + k.width / 2, k.top + k.height / 2, ['🔭', '📝', '🦁', '🦍', '🦚', '🐧'], 18);
        }
      } else {
        anger = Math.min(100, anger + 25);
        stamp.textContent = '💢'; p.classList.remove('noted'); p.classList.add('mad');
        g.setAttribute('data-m', 'j' + a);
        if (navigator.vibrate) { try { navigator.vibrate(25); } catch (e) {} }
      }
      drawAnger(); restart(msg, 'show');
    });
  });
  g.querySelector('.flipw').addEventListener('click', function () {
    g.setAttribute('data-word', g.getAttribute('data-word') === 'back' ? 'fwd' : 'back');
  });
  g.querySelector('.reset').addEventListener('click', function () {
    anger = 30; notes = {};
    pens.forEach(function (p) { p.classList.remove('noted', 'mad'); });
    setMode('judge'); g.setAttribute('data-m', '0'); g.setAttribute('data-word', 'fwd'); drawAnger();
  });
  drawAnger();
})();