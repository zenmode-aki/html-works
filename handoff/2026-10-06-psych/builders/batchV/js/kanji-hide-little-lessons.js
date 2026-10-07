/* 🀄 漢字を割ってみよう：タイルを押すと .open が付いて部品に分かれ、下に教え（HTML に用意したもの）が出る。JS は data-* と class と数字だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var ts = [].slice.call(g.querySelectorAll('.kt')), fn = g.querySelector('.fn'), again = g.querySelector('.again'), n = 0;
  function pop(el, list, k) {
    if (!window.pengessoPop) return;
    var b = el.getBoundingClientRect();
    window.pengessoPop(b.left + b.width / 2, b.top + b.height / 2, list, k);
  }
  ts.forEach(function (t, i) {
    t.addEventListener('click', function () {
      g.setAttribute('data-open', i);
      if (t.classList.contains('open')) return;
      t.classList.add('open'); n++; fn.textContent = n;
      pop(t, ['✨', '🀄'], 8);
      if (n >= 4) {
        g.setAttribute('data-s', 'done');
        setTimeout(function () { pop(t, ['📖', '🐧', '🍀', '✨', '💛'], 18); }, 350);
        if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
      }
    });
  });
  again.addEventListener('click', function () {
    n = 0; fn.textContent = '0';
    ts.forEach(function (t) { t.classList.remove('open'); });
    g.setAttribute('data-open', ''); g.setAttribute('data-s', 'play');
  });
})();