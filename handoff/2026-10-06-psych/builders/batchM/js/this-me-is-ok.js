
/* 💮 OK♪スタンプ：JS は data-lv・class・絵文字・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var qs = [].slice.call(g.querySelectorAll('.q')), mood = g.querySelector('.mood'), rn = g.querySelector('.rn');
  var FACE = ['😣', '😕', '🙂', '😌', '😊', '🥰'];
  function paint() {
    var n = qs.filter(function (q) { return q.classList.contains('on'); }).length;
    g.setAttribute('data-lv', String(n));
    mood.textContent = FACE[n];
    mood.classList.remove('pop'); void mood.offsetWidth; mood.classList.add('pop');
    rn.textContent = String(n);
    return n;
  }
  qs.forEach(function (q) {
    q.addEventListener('click', function () {
      if (q.classList.contains('on')) return;
      q.classList.add('on');
      if (navigator.vibrate) { try { navigator.vibrate(20); } catch (e) {} }
      var n = paint(), r = q.getBoundingClientRect();
      if (window.pengessoPop) {
        if (n === 5) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['💮', '🐧', '☕', '🧦', '🍰', '✨'], 24);
        else window.pengessoPop(r.right - 40, r.top + r.height / 2, ['💮', '✨'], 6);
      }
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    qs.forEach(function (q) { q.classList.remove('on'); }); paint();
  });
})();
