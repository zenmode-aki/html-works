/* 🎥 カメラON/OFF：JS は data-* / class / aria / 数字だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var btn = g.querySelector('.cam-btn'), tc = g.querySelector('.tc'), stars = [].slice.call(g.querySelectorAll('.st i'));
  var sc = 1, seen = {}, sec = 0, iv = 0;
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function setCam(on) {
    g.setAttribute('data-cam', on ? 'on' : 'off');
    btn.setAttribute('aria-pressed', on ? 'true' : 'false');
    clearInterval(iv);
    if (on) {
      sec = 0; tc.textContent = '00:00';
      iv = setInterval(function () { sec++; tc.textContent = pad(Math.floor(sec / 60)) + ':' + pad(sec % 60); }, 1000);
      if (!seen[sc]) {
        seen[sc] = 1;
        var n = Object.keys(seen).length;
        stars.forEach(function (s, i) { s.classList.toggle('on', i < n); });
        var r = g.querySelector('.pen').getBoundingClientRect();
        if (n === 3) {
          g.setAttribute('data-all', '1');
          if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🎬', '🏆', '🐧', '✨'], 20);
        } else if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🎬', '✨'], 8);
      }
    }
  }
  btn.addEventListener('click', function () { setCam(g.getAttribute('data-cam') !== 'on'); });
  g.querySelector('.nextsc').addEventListener('click', function () {
    sc = sc % 3 + 1;
    g.setAttribute('data-sc', sc);
    setCam(false);
  });
})();