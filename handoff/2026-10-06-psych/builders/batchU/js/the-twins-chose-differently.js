/* 🪧 分かれ道：道を押すと、双子Bがそこへ移る。何度でも選び直せる（勝ち負けなし）。JS は data-pick だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var dests = [].slice.call(g.querySelectorAll('.dest'));
  var picked = {};
  dests.forEach(function (b) {
    b.addEventListener('click', function () {
      var i = b.getAttribute('data-i');
      g.setAttribute('data-pick', i);
      if (!picked[i] && window.pengessoPop) {
        var k = b.querySelector('.here').getBoundingClientRect();
        window.pengessoPop(k.left + k.width / 2, k.top + k.height / 2, [['🌻', '✨'], ['📚', '✨'], ['💛', '✨']][+i].concat(['🐧']), 10);
      }
      picked[i] = true;
    });
  });
})();