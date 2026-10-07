/* 👟 小さすぎる靴：歩く＝痛さが増える。愚痴＝痛さが0に戻るけど、日数と「慣れ」が増える。靴をかえる＝おしまい。JS は data-* と幅と数字と絵文字だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var walk = g.querySelector('.walk'), vent = g.querySelector('.vent'), change = g.querySelector('.change'), again = g.querySelector('.again');
  var ouchI = g.querySelector('.b-ouch i'), numbI = g.querySelector('.b-numb i'), dn = g.querySelector('.dn');
  var face = g.querySelector('.pg-face'), av = g.querySelector('.pg-av'), puff = g.querySelector('.puff');
  var ouch = 0, numb = 0, days = 1;
  function pop(el, list, k) {
    if (!window.pengessoPop) return;
    var b = el.getBoundingClientRect();
    window.pengessoPop(b.left + b.width / 2, b.top + b.height / 2, list, k);
  }
  function redo(el, c) { el.classList.remove(c); void el.offsetWidth; el.classList.add(c); }
  function draw() {
    ouchI.style.width = ouch + '%';
    numbI.style.width = Math.min(100, numb * 25) + '%';
    dn.textContent = days;
    g.setAttribute('data-numb', numb >= 3 ? 'hi' : 'lo');
  }
  walk.addEventListener('click', function () {
    if (g.getAttribute('data-s') !== 'play') return;
    ouch = Math.min(100, ouch + 25);
    g.setAttribute('data-say', ouch >= 100 ? 'full' : 'walk');
    face.textContent = ouch >= 100 ? '😫' : '😣';
    redo(av, 'ouch'); draw();
  });
  vent.addEventListener('click', function () {
    if (g.getAttribute('data-s') !== 'play') return;
    ouch = 0; numb++; days++;
    g.setAttribute('data-say', numb >= 3 ? 'numb' : 'vent');
    face.textContent = numb >= 3 ? '😑' : '😮‍💨';
    redo(puff, 'go'); draw();
  });
  change.addEventListener('click', function () {
    if (g.getAttribute('data-s') !== 'play') return;
    g.setAttribute('data-r', numb >= 2 ? 'slow' : 'fast');
    g.setAttribute('data-s', 'done');
    face.textContent = '😄'; ouch = 0; draw();
    setTimeout(function () { pop(av, ['👟', '🐧', '✨', '🎉'], 16); }, 250);
    if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
  });
  again.addEventListener('click', function () {
    ouch = 0; numb = 0; days = 1; face.textContent = '🙁';
    g.setAttribute('data-say', 'idle'); g.setAttribute('data-r', ''); g.setAttribute('data-s', 'play');
    draw();
  });
})();