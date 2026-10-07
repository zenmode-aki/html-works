/* 📮 郵便屋さんゲーム：JS は data-i / data-f / data-end / class / 絵文字 / 数字だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var GOOD = [true, false, true, false, false];
  var i = 0, ok = 0, clouds = 0, busy = 0;
  var letter = g.querySelector('.letter'), react = g.querySelector('.react'), fb = g.querySelector('.fb');
  var row = g.querySelector('.mem-row'), lcN = g.querySelector('.lc-n'), scN = g.querySelector('.sc-n');
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function addMem(e) { var m = document.createElement('i'); m.className = 'new'; m.textContent = e; row.appendChild(m); row.classList.add('has'); }
  function choose(deliver) {
    if (busy || i > 4) return; busy = 1;
    var good = GOOD[i], f = (deliver ? 'd' : 'k') + (good ? 'g' : 'b');
    if ((deliver && good) || (!deliver && !good)) ok++;
    restart(letter, deliver ? 'go' : 'keep');
    setTimeout(function () {
      letter.classList.remove('go', 'keep');
      g.setAttribute('data-f', f); restart(fb, 'show');
      if (deliver) {
        addMem(good ? '☀️' : '🌧️');
        if (!good) clouds++;
        react.textContent = good ? '😊' : '😣'; restart(react, 'boing');
      }
      i++;
      g.setAttribute('data-i', String(i));
      lcN.textContent = Math.min(i + 1, 5) + '/5';
      if (i > 4) {
        g.setAttribute('data-end', clouds ? 'cloud' : 'sun');
        scN.textContent = ok + '/5';
        react.textContent = clouds ? '😟' : '😊';
        if (!clouds && window.pengessoPop) {
          var r = row.getBoundingClientRect();
          window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['☀️', '🐧', '💌', '✨'], 20);
        }
      } else { restart(letter, 'in-a'); }
      busy = 0;
    }, 430);
  }
  g.querySelector('.deliver').addEventListener('click', function () { choose(true); });
  g.querySelector('.keepb').addEventListener('click', function () { choose(false); });
  g.querySelector('.reset').addEventListener('click', function () {
    i = 0; ok = 0; clouds = 0; busy = 0;
    [].slice.call(row.querySelectorAll('i')).forEach(function (m) { m.remove(); });
    row.classList.remove('has');
    react.textContent = '🙂';
    g.setAttribute('data-i', '0'); g.setAttribute('data-f', ''); g.setAttribute('data-end', '');
    lcN.textContent = '1/5'; restart(letter, 'in-a');
  });
})();