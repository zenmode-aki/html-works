/* 🫧 泡をタップ（＝今を見る）でエンジンが下がる。雑念の雲が出ている間はじわじわ上がり、雲をタップするとぐっと上がる。10%以下で完成。JS は data-* / class / 数字 / style だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var bubs = g.querySelectorAll('.bub'), thought = g.querySelector('.thought'), start = g.querySelector('.startbtn');
  var rpmEl = g.querySelector('.rpm'), needle = g.querySelector('.needle'), nn = g.querySelector('.nn'), sink = g.querySelector('.sink');
  var rpm = 80, seen = 0, th = 0, creep = 0, cloud = 0, oops = 0;
  function set(k, v) { g.setAttribute('data-' + k, v); }
  function render() {
    rpm = Math.max(0, Math.min(100, rpm));
    rpmEl.textContent = Math.round(rpm);
    needle.style.left = rpm + '%';
    nn.textContent = seen;
  }
  function place(b) {   /* 泡は3つの場所（左・まん中・右）に1つずつ。重ならない */
    var slot = [].indexOf.call(bubs, b);
    b.style.left = (20 + slot * 30 + (Math.random() * 12 - 6)) + '%';
    b.style.top = (48 + Math.random() * 36) + '%';
  }
  function stopTimers() { clearInterval(creep); clearTimeout(cloud); clearTimeout(oops); }
  function showCloud() {
    th = (th + 1) % 4; set('th', th); set('tv', '1');
    cloud = setTimeout(function () { set('tv', '0'); cloud = setTimeout(showCloud, 1600 + Math.random() * 1200); }, 2600);
  }
  function finish() {
    stopTimers(); set('s', 'done'); set('tv', '0'); set('oops', '0');
    if (window.pengessoPop) {
      var r = sink.getBoundingClientRect();
      window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🫧', '🤫', '🐧', '✨'], 18);
    }
    if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
  }
  start.addEventListener('click', function () {
    stopTimers();
    rpm = 80; seen = 0; render();
    for (var i = 0; i < bubs.length; i++) { bubs[i].classList.remove('popped'); place(bubs[i]); }
    set('s', 'run'); set('tv', '0'); set('oops', '0');
    cloud = setTimeout(showCloud, 900);
    creep = setInterval(function () {
      rpm += g.getAttribute('data-tv') === '1' ? 3 : 1;
      render();
    }, 600);
  });
  for (var i = 0; i < bubs.length; i++) {
    bubs[i].addEventListener('click', function () {
      if (g.getAttribute('data-s') !== 'run' || this.classList.contains('popped')) return;
      var b = this;
      b.classList.add('popped');
      rpm -= 10; seen++; set('oops', '0'); render();
      if (rpm <= 10) { finish(); return; }
      setTimeout(function () { place(b); b.classList.remove('popped'); }, 450);
    });
  }
  thought.addEventListener('click', function () {
    if (g.getAttribute('data-s') !== 'run') return;
    rpm += 15; render();
    set('oops', '1'); set('tv', '0');
    clearTimeout(oops);
    oops = setTimeout(function () { set('oops', '0'); }, 1800);
    if (navigator.vibrate) { try { navigator.vibrate(20); } catch (e) {} }
  });
  render();
})();