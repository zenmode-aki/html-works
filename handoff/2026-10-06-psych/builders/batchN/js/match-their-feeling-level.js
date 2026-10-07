/* 🎚️ 気持ちのチューナー：JS は data-* / class / style / 絵文字 / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var R = [{ f: 'happy', t: 80, face: '😄' }, { f: 'angry', t: 30, face: '😕' }, { f: 'sad', t: 60, face: '😢' }];
  var FACES = { happy: ['😐', '🙂', '😊', '😄', '🤩'], angry: ['😐', '😕', '😤', '😠', '😡'], sad: ['😐', '🙁', '😟', '😢', '😭'] };
  var r = 0, v = 0, got = [false, false, false];
  var tBar = g.querySelector('.t-bar'), tN = g.querySelector('.t-n'), mBar = g.querySelector('.m-bar'), mN = g.querySelector('.m-n');
  var frFx = g.querySelector('.face .fx'), myFx = g.querySelector('.my-fx');
  var stars = [].slice.call(g.querySelectorAll('.rounds i'));
  function restart(el, c) { el.classList.remove(c); void el.offsetWidth; el.classList.add(c); }
  function drawMe() {
    mBar.style.width = v + '%'; mN.textContent = String(v);
    var f = FACES[R[r].f][Math.round(v / 25)];
    if (myFx.textContent !== f) { myFx.textContent = f; restart(myFx, 'boing'); }
  }
  function load(k) {
    r = k; v = 0;
    g.setAttribute('data-r', String(r)); g.setAttribute('data-f', R[r].f); g.setAttribute('data-v', '');
    tBar.style.width = R[r].t + '%'; tN.textContent = String(R[r].t);
    frFx.textContent = R[r].face; restart(frFx, 'boing');
    drawMe();
  }
  function step(d) {
    if (g.getAttribute('data-v') === 'match' || g.getAttribute('data-v') === 'end') return;
    v = Math.max(0, Math.min(100, v + d));
    g.setAttribute('data-v', v === 0 ? '' : 'tuning');
    drawMe();
  }
  g.querySelector('.minus').addEventListener('click', function () { step(-10); });
  g.querySelector('.plus').addEventListener('click', function () { step(10); });
  g.querySelector('.listen').addEventListener('click', function () {
    var t = R[r].t, d = v - t, res;
    if (v === 0) res = 'flat';
    else if (Math.abs(d) <= 10) res = 'match';
    else if (d > 0) res = 'over';
    else res = 'under';
    if (res === 'match') {
      got[r] = true; stars[r].classList.add('on');
      var all = got[0] && got[1] && got[2];
      res = all ? 'end' : 'match';
      if (window.pengessoPop) {
        var b = g.querySelector('.verdict').getBoundingClientRect();
        window.pengessoPop(b.left + b.width / 2, b.top, all ? ['🏅', '💞', '🐧', '✨'] : ['💞', '✨'], all ? 22 : 10);
      }
      frFx.textContent = { happy: '🥰', angry: '😌', sad: '🥲' }[R[r].f]; restart(frFx, 'boing');
    } else if (res === 'flat' || res === 'over') { frFx.textContent = res === 'flat' ? '😟' : '😳'; restart(frFx, 'boing'); }
    g.setAttribute('data-v', res);
  });
  g.querySelector('.nextr').addEventListener('click', function () {
    for (var k = 1; k <= 3; k++) { var n = (r + k) % 3; if (!got[n]) { load(n); return; } }
  });
  g.querySelector('.again').addEventListener('click', function () {
    got = [false, false, false]; stars.forEach(function (s) { s.classList.remove('on'); }); load(0);
  });
  load(0);
})();