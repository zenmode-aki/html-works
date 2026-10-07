/* 🎚️ 自分のレバーを探そう：JS は data-r・data-ok・data-say・class・disabled・数字・絵文字だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var opts = [].slice.call(g.querySelectorAll('.opt'));
  var num = g.querySelector('.found .num'), ms = g.querySelector('.m-s'), lever = g.querySelector('.lever');
  var r = 1, found = 0;
  function set(k, v) { g.setAttribute(k, String(v)); }
  function say(v) { g.setAttribute('data-say', ''); void g.offsetWidth; g.setAttribute('data-say', v); }
  opts.forEach(function (b) {
    b.addEventListener('click', function () {
      if (b.disabled || g.getAttribute('data-ok') === '1') return;
      if (b.getAttribute('data-good') === '1') {
        b.disabled = true; b.classList.add('right');
        found += 1; num.textContent = String(found);
        set('data-ok', 1); ms.textContent = '🍀';
        say(r === 3 ? 'end' : 'ok');
        if (window.pengessoPop) {
          var k = lever.getBoundingClientRect();
          window.pengessoPop(k.left + k.width / 2, k.top + k.height / 2, r === 3 ? ['🎚️', '🐭', '🍀', '✨'] : ['🎚️', '✨'], r === 3 ? 18 : 8);
        }
        if (navigator.vibrate) { try { navigator.vibrate(r === 3 ? 35 : 20); } catch (e) {} }
      } else {
        b.disabled = true; b.classList.add('locked');
        say('no');
      }
    });
  });
  g.querySelector('.nextb').addEventListener('click', function () {
    r += 1; set('data-r', r); set('data-ok', 0); say('ask'); ms.textContent = '💦';
  });
  g.querySelector('.again').addEventListener('click', function () {
    r = 1; found = 0; num.textContent = '0'; ms.textContent = '💦';
    opts.forEach(function (b) { b.disabled = false; b.classList.remove('locked', 'right'); });
    set('data-r', 1); set('data-ok', 0); say('ask');
  });
})();