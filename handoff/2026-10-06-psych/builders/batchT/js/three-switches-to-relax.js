/* 🎚 3つのスイッチ（顔・呼吸・肩）をオフにするたびに、ペンギンの力みが1つずつ消える。全部オフでとろける。JS は aria-pressed / data-* / 数字 / 絵文字だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var sws = g.querySelectorAll('.sw'), lv = g.querySelector('.lv'), faceb = g.querySelector('.faceb'), peng = g.querySelector('.peng');
  var FACES = ['😣', '😕', '🙂', '😌'], was = false;
  function render() {
    var n = 0;
    for (var i = 0; i < sws.length; i++) {
      var off = sws[i].getAttribute('aria-pressed') === 'true';
      if (off) n++;
      g.setAttribute('data-' + sws[i].getAttribute('data-k'), off ? 'off' : 'on');
    }
    lv.textContent = n;
    faceb.textContent = FACES[n];
    faceb.classList.remove('boing'); void faceb.offsetWidth; faceb.classList.add('boing');
    g.setAttribute('data-all', n === 3 ? '1' : '0');
    if (n === 3 && !was) {
      if (window.pengessoPop) {
        var r = peng.getBoundingClientRect();
        window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🫠', '🐧', '🍃', '✨', '💤'], 18);
      }
      if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
    }
    was = n === 3;
  }
  for (var i = 0; i < sws.length; i++) {
    sws[i].addEventListener('click', function () {
      this.setAttribute('aria-pressed', this.getAttribute('aria-pressed') === 'true' ? 'false' : 'true');
      render();
    });
  }
})();