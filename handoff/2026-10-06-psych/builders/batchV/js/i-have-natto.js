/* 🍀 プラスのスイッチ：同じ場面でスイッチを入れると、ひとことがプラスに変わってクローバーが1つ育つ。JS は data-* と class と絵文字だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var sw = g.querySelector('.sw'), ke = g.querySelector('.ke'), face = g.querySelector('.who-face');
  var nx = g.querySelector('.nextsc'), again = g.querySelector('.again'), scn = g.querySelector('.sc-n');
  var pe = g.querySelector('.pe'), PICS = ['🍚', '🏚️', '🚃'];
  var cl = [].slice.call(g.querySelectorAll('.clover')), sc = 0, got = [false, false, false];
  function pop(el, list, k) {
    if (!window.pengessoPop) return;
    var b = el.getBoundingClientRect();
    window.pengessoPop(b.left + b.width / 2, b.top + b.height / 2, list, k);
  }
  function setPlus(on) {
    g.setAttribute('data-plus', on ? '1' : '0');
    sw.setAttribute('aria-pressed', on ? 'true' : 'false');
    ke.textContent = on ? '😄' : '🙁';
    face.textContent = on ? '😄' : '😞';
  }
  sw.addEventListener('click', function () {
    if (g.getAttribute('data-s') !== 'play') return;
    var on = g.getAttribute('data-plus') !== '1';
    setPlus(on);
    if (on && !got[sc]) {
      got[sc] = true;
      cl[sc].classList.add('got'); cl[sc].querySelector('.cv').textContent = '🍀';
      pop(cl[sc], ['🍀', '✨'], 8);
      if (got[0] && got[1] && got[2]) {
        g.setAttribute('data-s', 'done');
        setTimeout(function () { pop(sw, ['🍀', '🐧', '🍚', '✨', '🌈'], 18); }, 300);
        if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
      }
    }
  });
  nx.addEventListener('click', function () {
    if (sc >= 2) return;
    sc++; scn.textContent = sc + 1;
    g.setAttribute('data-sc', sc); pe.textContent = PICS[sc];
    setPlus(false);
  });
  again.addEventListener('click', function () {
    sc = 0; got = [false, false, false]; scn.textContent = '1';
    cl.forEach(function (c) { c.classList.remove('got'); c.querySelector('.cv').textContent = '🌱'; });
    g.setAttribute('data-sc', '0'); g.setAttribute('data-s', 'play'); pe.textContent = PICS[0];
    setPlus(false);
  });
})();