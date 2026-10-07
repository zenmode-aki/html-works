/* 🎤 スローモーション・スタート：JS は data-i / data-busy / data-end / data-r / class / style だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var DUR = [1600, 1500, 1800, 3000, 1400];
  var lis = [].slice.call(g.querySelectorAll('.steps li'));
  var btn = g.querySelector('.go'), fill = g.querySelector('.go .fill');
  var voice = g.querySelector('.voice'), vbar = g.querySelector('.v-track i');
  var i = 0, shaky = 0, busy = false, t = 0;
  function restart(el, c) { el.classList.remove(c); void el.offsetWidth; el.classList.add(c); }
  function setFill(w, ms) {
    fill.style.transition = 'none'; fill.style.width = w === 100 ? '0%' : w + '%';
    void fill.offsetWidth;
    if (ms) { fill.style.transition = 'width ' + ms + 'ms linear'; fill.style.width = w + '%'; }
  }
  function draw() {
    g.setAttribute('data-i', String(i));
    g.setAttribute('data-busy', busy ? '1' : '0');
    lis.forEach(function (li, k) { li.classList.toggle('now', k === i); });
    vbar.style.width = Math.min(100, shaky * 25) + '%';
  }
  function finish() {
    g.setAttribute('data-r', shaky === 0 ? 'calm' : shaky <= 2 ? 'bit' : 'shaky');
    g.setAttribute('data-end', '1');
    if (shaky === 0 && window.pengessoPop) {
      var r = g.querySelector('.result').getBoundingClientRect();
      window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🐢', '🎤', '🐧', '✨'], 20);
    }
  }
  function done(rushed) {
    busy = false;
    lis[i].classList.add('done');
    if (rushed) lis[i].classList.add('rushed');
    i++;
    setFill(0);
    draw();
    if (i >= lis.length) finish();
  }
  btn.addEventListener('click', function () {
    if (g.getAttribute('data-end') === '1') return;
    if (!busy) {
      busy = true; draw();
      setFill(100, DUR[i]);
      t = setTimeout(function () { done(false); }, DUR[i]);
    } else {
      clearTimeout(t);
      shaky++; restart(voice, 'jit');
      done(true);
    }
  });
  g.querySelector('.reset').addEventListener('click', function () {
    clearTimeout(t);
    i = 0; shaky = 0; busy = false;
    lis.forEach(function (li) { li.classList.remove('done', 'rushed'); });
    setFill(0);
    g.setAttribute('data-end', '0'); g.setAttribute('data-r', '');
    draw();
  });
  draw();
})();