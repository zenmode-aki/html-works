/* 🪙 ごきげん貯金：JS は data-* / class / 数字だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var evs = [].slice.call(g.querySelectorAll('.ev[data-v]')), askEv = g.querySelector('.ev-ask'),
      pens = { a: g.querySelector('.pa'), b: g.querySelector('.pb') }, ln = g.querySelector('.ln');
  var bal = { a: 2, b: 2 }, order = [], k = 0;
  function shuffle(a) { for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function paintJar(w) { [].slice.call(pens[w].querySelectorAll('.jar i')).forEach(function (c, i) { c.classList.toggle('on', i < bal[w]); }); }
  function showEvent() {
    evs.forEach(function (e) { e.classList.remove('show'); }); askEv.classList.remove('show');
    if (k < order.length) { void order[k].offsetWidth; order[k].classList.add('show'); ln.textContent = order.length - k; }
    else { askEv.classList.add('show'); g.setAttribute('data-st', 'ask'); }
  }
  function restart(el, c) { el.classList.remove('plus', 'minus'); void el.offsetWidth; el.classList.add(c); }
  function send(w) {
    if (g.getAttribute('data-st') !== 'sort' || k >= order.length) return;
    var v = parseInt(order[k].getAttribute('data-v'), 10);
    bal[w] = Math.max(0, Math.min(5, bal[w] + v));
    paintJar(w);
    var face = pens[w].querySelector('.pf');
    restart(face, v > 0 ? 'plus' : 'minus');
    if (v > 0 && window.pengessoPop) { var r = face.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🪙', '✨'], 6); }
    k++; showEvent();
  }
  function mood(b) { return b >= 4 ? 'kind' : b >= 2 ? 'meh' : 'grump'; }
  g.querySelector('.to-a').addEventListener('click', function () { send('a'); });
  g.querySelector('.to-b').addEventListener('click', function () { send('b'); });
  g.querySelector('.ask').addEventListener('click', function () {
    var ra = mood(bal.a), rb = mood(bal.b);
    pens.a.setAttribute('data-r', ra); pens.b.setAttribute('data-r', rb);
    g.setAttribute('data-same', ra === rb ? '1' : '0');
    g.setAttribute('data-st', 'asked');
    var happy = ra === 'kind' ? pens.a : rb === 'kind' ? pens.b : null;
    if (happy && window.pengessoPop) { var r = happy.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 3, ['🪙', '😄', '🐧', '✨'], 16); }
  });
  function reset() {
    bal = { a: 2, b: 2 }; k = 0; order = shuffle(evs.slice());
    paintJar('a'); paintJar('b');
    pens.a.setAttribute('data-r', ''); pens.b.setAttribute('data-r', '');
    g.setAttribute('data-same', '0'); g.setAttribute('data-st', 'sort');
    showEvent();
  }
  g.querySelector('.again').addEventListener('click', reset);
  reset();
})();