/* 👏 ぐるぐるを止める：JS は data-left・data-train・class・数字・絵文字だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var rings = [].slice.call(g.querySelectorAll('.ring'));
  var clap = g.querySelector('.clap'), mood = g.querySelector('.mood'), num = g.querySelector('.num');
  var orbit = g.querySelector('.orbit');
  var MOODS = ['😌', '😮‍💨', '😤', '💢'];
  var left = 3;
  function restart(cls) { g.classList.remove(cls); void g.offsetWidth; g.classList.add(cls); }
  function mid(el) { var r = el.getBoundingClientRect(); return [r.left + r.width / 2, r.top + r.height / 2]; }
  clap.addEventListener('click', function () {
    if (left <= 0) return;
    var c = mid(clap);
    restart('clapped');
    rings[3 - left].classList.add('stop');
    left -= 1;
    g.setAttribute('data-left', String(left));
    num.textContent = String(left);
    mood.textContent = MOODS[left];
    if (window.pengessoPop) {
      if (left > 0) window.pengessoPop(c[0], c[1] - 20, ['👏', '💥'], 8);
      else { var o = mid(orbit); window.pengessoPop(o[0], o[1], ['🍃', '🐧', '✨', '👏'], 18); }
    }
    if (navigator.vibrate) { try { navigator.vibrate(left ? 15 : 35); } catch (e) {} }
  });
  g.querySelector('.to-train').addEventListener('click', function () {
    g.setAttribute('data-train', '1');
    if (window.pengessoPop) { var t = mid(g.querySelector('.train')); window.pengessoPop(t[0], t[1], ['❗', '🚃'], 8); }
  });
  g.querySelector('.again').addEventListener('click', function () {
    left = 3;
    rings.forEach(function (r) { r.classList.remove('stop'); });
    g.classList.remove('clapped');
    g.setAttribute('data-left', '3'); g.setAttribute('data-train', '0');
    num.textContent = '3'; mood.textContent = MOODS[3];
  });
})();