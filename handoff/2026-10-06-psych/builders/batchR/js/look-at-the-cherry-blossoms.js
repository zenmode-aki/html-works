/* 🌸 同じ公園：JS は data-*・class・数字・style だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var park = g.querySelector('.park'), meter = g.querySelector('.meter-h'), bar = meter.querySelector('i'), hn = g.querySelector('.h-n');
  var nice = [].slice.call(g.querySelectorAll('.it.nice')), trash = [].slice.call(g.querySelectorAll('.it.trash'));
  var up = g.querySelector('.up'), down = g.querySelector('.down'), lotto = g.querySelector('.lotto'), again = g.querySelector('.again');
  var START = 30, h = START, ni = 0, ti = 0, timers = [], done = false;
  function clear() { timers.forEach(clearTimeout); timers = []; meter.classList.remove('slow'); }
  function show(v) { bar.style.width = v + '%'; hn.textContent = String(v); }
  function set(r) { g.setAttribute('data-r', ''); void g.offsetWidth; g.setAttribute('data-r', r); }
  function bounce(el) { el.classList.remove('boing'); void el.offsetWidth; el.classList.add('boing'); }
  function pop(el, list, n) {
    if (!window.pengessoPop) return;
    var r = el.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, n);
  }
  function lookUp() {
    if (done) return;
    clear(); park.setAttribute('data-look', 'up');
    var el = nice[ni % nice.length]; el.classList.add('on'); bounce(el); ni++;
    h = Math.min(100, h + 14); show(h);
    if (h >= 100) { done = true; set('full'); up.disabled = down.disabled = lotto.disabled = true; pop(park, ['🌸', '🐧', '✨', '🌸'], 18); }
    else { set('up'); pop(el, ['🌸'], 5); }
  }
  function lookDown() {
    if (done) return;
    clear(); park.setAttribute('data-look', 'down');
    var el = trash[ti % trash.length]; el.classList.add('on'); bounce(el); ti++;
    h = Math.max(0, h - 14); show(h); set('down');
  }
  function win() {
    if (done) return;
    clear(); set('lotto'); show(100); bounce(lotto);
    pop(lotto, ['🎫', '💰', '✨'], 14);
    timers.push(setTimeout(function () {
      meter.classList.add('slow'); set('fade'); show(h);
    }, 1800));
    timers.push(setTimeout(function () { meter.classList.remove('slow'); }, 4400));
  }
  function reset() {
    clear(); done = false; h = START; ni = 0; ti = 0;
    nice.concat(trash).forEach(function (el) { el.classList.remove('on'); });
    park.setAttribute('data-look', ''); up.disabled = down.disabled = lotto.disabled = false;
    show(h); set('');
  }
  up.addEventListener('click', lookUp);
  down.addEventListener('click', lookDown);
  lotto.addEventListener('click', win);
  again.addEventListener('click', reset);
  show(h);
})();