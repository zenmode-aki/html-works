/* 🎁 小さなプレゼント：JS は data-lv / data-given / class / style の幅 / 絵文字 / 数字だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var KEY = 'pengesso-be-easily-delighted-given';
  var GIFTS = ['🍬', '🌼', '🍪', '🍩', '🍊', '🧁'];
  var REACT = ['', '😐', '🙂', '😊', '😄', '🤩'];
  var lv = 1, given = 0, gi = 0, busy = 0;
  var them = g.querySelector('.them'), react = g.querySelector('.react'), gift = g.querySelector('.gift'), say = g.querySelector('.say');
  var bars = [].slice.call(g.querySelectorAll('.bars i')), bar = g.querySelector('.meter i'), cN = g.querySelector('.c-n');
  var minus = g.querySelector('.minus'), plus = g.querySelector('.plus'), give = g.querySelector('.give');
  try { given = parseInt(localStorage.getItem(KEY), 10) || 0; } catch (e) { given = 0; }
  function save() { try { localStorage.setItem(KEY, String(given)); } catch (e) {} }
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function drawLv() {
    g.setAttribute('data-lv', String(lv));
    bars.forEach(function (b, i) { b.classList.toggle('on', i < lv); });
    minus.disabled = lv <= 1; plus.disabled = lv >= 5;
  }
  function setLv(n) {
    lv = Math.max(1, Math.min(5, n));
    g.setAttribute('data-given', '0');
    them.className = 'who them'; react.textContent = '😐';
    bar.style.width = '0';
    drawLv();
  }
  minus.addEventListener('click', function () { setLv(lv - 1); });
  plus.addEventListener('click', function () { setLv(lv + 1); });
  give.addEventListener('click', function () {
    if (busy) return; busy = 1;
    gi = (gi + 1) % GIFTS.length;
    gift.textContent = GIFTS[gi];
    restart(gift, 'fly');
    setTimeout(function () {
      busy = 0;
      g.setAttribute('data-given', '1');
      react.textContent = REACT[lv];
      them.className = 'who them'; void them.offsetWidth; them.classList.add('r' + lv);
      restart(say, 'show');
      bar.style.width = (lv * 20) + '%';
      given += lv === 5 ? 2 : 1; save();
      cN.textContent = String(given);
      if (window.pengessoPop && lv >= 4) {
        var r = them.getBoundingClientRect(), x = r.left + r.width / 2, y = r.top + r.height / 3;
        window.pengessoPop(x, y, lv === 5 ? ['💖', GIFTS[gi], '🐧', '✨', '🎁'] : ['💗', GIFTS[gi], '✨'], lv === 5 ? 22 : 10);
      }
    }, 480);
  });
  g.querySelector('.reset').addEventListener('click', function () { given = 0; save(); cN.textContent = '0'; setLv(1); });
  cN.textContent = String(given);
  drawLv();
})();