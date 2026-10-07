/* 🎁 まわりの「今」を見つける：JS は data-n / class / aria だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var senses = [].slice.call(g.querySelectorAll('.sense')), clouds = [].slice.call(g.querySelectorAll('.cl')),
      stars = [].slice.call(g.querySelectorAll('.stars i')), timers = [];
  function n() { return senses.filter(function (s) { return s.classList.contains('felt'); }).length; }
  function pop(el, list, k) {
    if (!window.pengessoPop) return;
    var r = el.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, k);
  }
  senses.forEach(function (s) {
    s.addEventListener('click', function () {
      if (s.classList.contains('felt')) return;
      s.classList.add('felt'); s.setAttribute('aria-pressed', 'true');
      var k = n();
      var c = clouds.filter(function (x) { return !x.classList.contains('gone'); })[0];
      if (c) { c.classList.add('gone'); timers.push(setTimeout(function () { c.hidden = true; }, 520)); }
      stars.forEach(function (st, i) { st.classList.toggle('on', i < k); });
      g.setAttribute('data-n', k);
      pop(s, [s.querySelector('.se').textContent, '✨'], 6);
      if (k === 5) {
        timers.push(setTimeout(function () { pop(g.querySelector('.me'), ['🎁', '✨', '🍃', '🐦', '🐧'], 18); }, 350));
        if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
      }
    });
  });
  g.querySelector('.again').addEventListener('click', function () {
    timers.forEach(clearTimeout); timers = [];
    senses.forEach(function (s) { s.classList.remove('felt'); s.setAttribute('aria-pressed', 'false'); });
    clouds.forEach(function (c) { c.hidden = false; c.classList.remove('gone'); });
    stars.forEach(function (st) { st.classList.remove('on'); });
    g.setAttribute('data-n', '0');
  });
})();