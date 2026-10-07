/* 🌱 3つのドア：とてもやさしく。点数も紙吹雪もなし。JS は class / data-n / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var doors = [].slice.call(g.querySelectorAll('.door'));
  function count() {
    var n = doors.filter(function (d) { return d.classList.contains('open'); }).length;
    g.setAttribute('data-n', String(n));
  }
  doors.forEach(function (d) {
    d.addEventListener('click', function () {
      if (d.classList.contains('open')) return;      /* 開いたドアは、開いたまま */
      d.classList.add('open'); d.setAttribute('aria-pressed', 'true');
      var w = g.querySelector('.w' + d.getAttribute('data-d'));
      if (w) w.classList.add('show');
      count();
    });
  });
  g.querySelector('.close').addEventListener('click', function () {
    doors.forEach(function (d) { d.classList.remove('open'); d.setAttribute('aria-pressed', 'false'); });
    [].slice.call(g.querySelectorAll('.w')).forEach(function (w) { w.classList.remove('show'); });
    count();
  });
})();