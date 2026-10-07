/* 👗 趣味の試着室：押すたびにカーテンが閉じて開き、次の趣味に着替える。3〜6着目で「ぴったり」。JS は data-* と数字と絵文字だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var btn = g.querySelector('.trybtn'), prop = g.querySelector('.prop'), tn = g.querySelector('.tn');
  var hooks = [].slice.call(g.querySelectorAll('.hook'));
  var PROPS = ['🎸', '🎨', '🧶', '📷', '🏸', '🍳', '♟️', '🌱'];
  var order = [], tries = 0, goal = 0, busy = false;
  function shuffle() {
    order = [0, 1, 2, 3, 4, 5, 6, 7];
    for (var i = order.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = order[i]; order[i] = order[j]; order[j] = t; }
    goal = 3 + Math.floor(Math.random() * 4);   /* 3〜6着目でぴったり */
  }
  function reset() {
    tries = 0; shuffle(); tn.textContent = 0; prop.textContent = '❔';
    hooks.forEach(function (h) { h.removeAttribute('data-on'); });
    g.setAttribute('data-h', '-1'); g.setAttribute('data-fit', '0'); g.setAttribute('data-c', '1');
  }
  reset();
  btn.addEventListener('click', function () {
    if (busy) return;
    if (g.getAttribute('data-fit') === '3') { reset(); return; }
    busy = true;
    g.setAttribute('data-c', '1');
    setTimeout(function () {
      var h = order[tries % 8]; tries++;
      var fit = tries >= goal ? 3 : (Math.random() < 0.5 ? 1 : 2);
      prop.textContent = PROPS[h];
      hooks[h].setAttribute('data-on', '1');
      tn.textContent = tries;
      g.setAttribute('data-h', h);
      g.setAttribute('data-fit', fit);
      g.setAttribute('data-c', '0');
      busy = false;
      if (fit === 3) {
        if (window.pengessoPop) {
          var k = prop.getBoundingClientRect();
          window.pengessoPop(k.left + k.width / 2, k.top + k.height / 2, ['✨', '⭐', PROPS[h], '🐧'], 16);
        }
        if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
      }
    }, 340);
  });
})();