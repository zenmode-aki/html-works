/* 📦 手放しタイム：押すと物が箱へ飛んでいき、空いた場所と光がふえる。もう一度押すと戻る。JS は data-* と style と数字と絵文字だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var items = [].slice.call(g.querySelectorAll('.item')), bar = g.querySelector('.bar i'), pc = g.querySelector('.pc');
  var shade = g.querySelector('.shade'), sun = g.querySelector('.se');
  var SUN = ['☁️', '🌥️', '⛅', '🌤️', '🌤️', '☀️'];
  var cheered = false;
  function draw() {
    var n = items.filter(function (it) { return it.getAttribute('data-gone') === '1'; }).length;
    var pct = 8 + n * 18;
    g.setAttribute('data-n', n);
    bar.style.width = pct + '%'; pc.textContent = pct;
    shade.style.opacity = String(.28 - n * .056);
    sun.textContent = SUN[n];
    sun.style.transform = 'scale(' + (1 + n * .06) + ')';
    return n;
  }
  items.forEach(function (it) {
    it.addEventListener('click', function () {
      var gone = it.getAttribute('data-gone') === '1';
      if (gone) it.removeAttribute('data-gone'); else it.setAttribute('data-gone', '1');
      var n = draw();
      if (!gone && window.pengessoPop) {
        var k = it.querySelector('.ib').getBoundingClientRect();
        window.pengessoPop(k.left + k.width / 2, k.top + k.height / 2, ['✨', '📦'], 6);
      }
      if (n === 5 && !cheered) {
        cheered = true;
        if (window.pengessoPop) {
          var s = sun.getBoundingClientRect();
          window.pengessoPop(s.left + s.width / 2, s.top + s.height / 2, ['☀️', '✨', '🐧', '🧹'], 18);
        }
        if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
      }
      if (n < 5) cheered = false;
    });
  });
  draw();
})();