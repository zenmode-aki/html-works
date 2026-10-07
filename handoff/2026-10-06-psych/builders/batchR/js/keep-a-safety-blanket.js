/* ⛈️ 心の毛布：JS は data-*・aria-pressed・hidden・絵文字・style だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var picks = [].slice.call(g.querySelectorAll('.pick'));
  var think = g.querySelector('.think'), bar = g.querySelector('.gmeter i'), again = g.querySelector('.again');
  var last = g.querySelector('.last'), lastE = g.querySelector('.last-e');
  var EMO = ['😊', '🐶', '🏞️', '🍙'];
  var KEY = 'pengesso-keep-a-safety-blanket-pick';
  function showLast() {
    var v = null; try { v = localStorage.getItem(KEY); } catch (e) {}
    var k = parseInt(v, 10);
    if (k >= 0 && k < EMO.length) { lastE.textContent = EMO[k]; last.hidden = false; }
  }
  function pick(k) {
    picks.forEach(function (b, i) { b.setAttribute('aria-pressed', i === k ? 'true' : 'false'); });
    g.setAttribute('data-pick', String(k));
    think.textContent = EMO[k];
    g.setAttribute('data-s', 'warm');
    bar.style.width = '100%';
    try { localStorage.setItem(KEY, String(k)); } catch (e) {}
    if (window.pengessoPop) {
      var r = think.getBoundingClientRect();
      window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, [EMO[k], '💛', '🐧', '✨'], 14);
    }
  }
  picks.forEach(function (b, i) { b.addEventListener('click', function () { pick(i); }); });
  again.addEventListener('click', function () {
    picks.forEach(function (b) { b.setAttribute('aria-pressed', 'false'); });
    g.setAttribute('data-s', 'cold'); g.setAttribute('data-pick', ''); bar.style.width = '8%';
    showLast();
  });
  bar.style.width = '8%';
  showLast();
})();