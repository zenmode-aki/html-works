/* 🎩 警報のタネあかし：JS は data-s と絵文字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var btn = g.querySelector('.tap'), face = g.querySelector('.face'), box = g.querySelector('.stagebox');
  var NEXT = { idle: 'alarm', alarm: 'reveal', reveal: 'calm', calm: 'idle' };
  var FACE = { idle: '🙂', alarm: '😰', reveal: '😮', calm: '😌' };
  btn.addEventListener('click', function () {
    var s = NEXT[g.getAttribute('data-s')] || 'idle';
    g.setAttribute('data-s', s);
    face.textContent = FACE[s];
    if (s === 'alarm' && navigator.vibrate) { try { navigator.vibrate([40, 60, 40]); } catch (e) {} }
    if (s === 'calm' && window.pengessoPop) {
      var r = box.getBoundingClientRect();
      window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['😌', '🐧', '✨', '🎤'], 16);
    }
  });
})();