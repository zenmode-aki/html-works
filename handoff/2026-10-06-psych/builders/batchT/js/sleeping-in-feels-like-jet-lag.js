/* ✈️ 日曜に起きる時間（7〜12時）→ 体の時計が飛んでいく国・体が思っている時間・時差ボケのメーター。JS は data-h と数字と style だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var minus = g.querySelector('.minus'), plus = g.querySelector('.plus'), again = g.querySelector('.again');
  var hh = g.querySelector('.hh'), bt = g.querySelector('.bt'), clockT = g.querySelector('.clock-t'), place = g.querySelector('.place');
  var plane = g.querySelector('.plane'), bar = g.querySelector('.lag i'), stops = g.querySelectorAll('.stops span');
  var againRow = g.querySelector('.again-row');
  var h = 0, far = 0;
  function bump(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function pop(el, list, k) {
    if (!window.pengessoPop || !el) return;
    var r = el.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, k);
  }
  function render(moved) {
    g.setAttribute('data-h', h);
    hh.textContent = 7 + h;
    bt.textContent = 7 - h;
    plane.style.left = 'calc((100% - 32px) * ' + (h / 5) + ')';
    bar.style.width = (h * 20) + '%';
    for (var i = 0; i < stops.length; i++) stops[i].classList.toggle('here', i === h);
    minus.disabled = h === 0;
    plus.disabled = h === 5;
    againRow.hidden = h === 0;
    if (moved) { bump(clockT, 'tick'); bump(place, 'swap'); }
  }
  function go(d) {
    var nh = Math.max(0, Math.min(5, h + d));
    if (nh === h) return;
    h = nh; far = Math.max(far, h);
    render(true);
    if (h === 5) pop(plane, ['✈️', '💤', '😵'], 12);
    if (h === 0 && far >= 3) { pop(stops[0], ['🏠', '✨', '🐧', '😊'], 16); far = 0; }
  }
  minus.addEventListener('click', function () { go(-1); });
  plus.addEventListener('click', function () { go(1); });
  again.addEventListener('click', function () { far = Math.max(far, h); go(-h); });
  render(false);
})();