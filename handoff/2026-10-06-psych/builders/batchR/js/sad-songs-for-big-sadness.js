/* 🎵 曲を気持ちにそろえる：JS は data-*・数字・絵文字・style だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var minus = g.querySelector('.minus'), plus = g.querySelector('.plus'), we = g.querySelector('.we'), wn = g.querySelector('.wn');
  var bBright = g.querySelector('.s-bright'), bSlow = g.querySelector('.s-slow'), again = g.querySelector('.again');
  var bar = g.querySelector('.gmeter i'), nowSong = g.querySelector('.now-song');
  var WX = ['', '🌤️', '⛅', '☁️', '🌧️', '⛈️'];
  var RISE = ['🎻', '🎸', '🎹', '🎺'];
  var lv = 4, busy = false, timers = [];
  function set(k, v) { g.setAttribute('data-' + k, v); }
  function clear() { timers.forEach(clearTimeout); timers = []; }
  function paintLv() {
    set('lv', String(lv)); we.textContent = WX[lv]; wn.textContent = String(lv);
    minus.disabled = busy || lv <= 1; plus.disabled = busy || lv >= 5;
  }
  function lock(on) { busy = on; bBright.disabled = on; bSlow.disabled = on; paintLv(); }
  function match(song) { var mood = song === 'bright' ? 1 : 4.5; return Math.max(6, Math.min(100, Math.round(100 - Math.abs(lv - mood) * 22))); }
  function bounce(el) { el.classList.remove('boing'); void el.offsetWidth; el.classList.add('boing'); }
  function play(song) {
    if (busy) return;
    clear();
    var m = match(song);
    set('song', song); bar.style.width = m + '%';
    nowSong.textContent = song === 'bright' ? '🎺' : '🎻';
    bounce(nowSong);
    if (song === 'bright') { set('r', ''); void g.offsetWidth; set('r', m >= 60 ? 'up' : 'empty'); if (m >= 60) pop(['🎺', '✨', '🐧'], 10); return; }
    if (m < 60) { set('r', 'slowok'); return; }
    set('r', 'sync');
    lock(true);
    var k = 0;
    function stepUp() {
      if (lv > 1) {
        lv--; k = Math.min(RISE.length - 1, k + 1);
        nowSong.textContent = RISE[k]; bounce(nowSong); set('r', 'rise'); set('song', lv <= 2 ? 'bright' : 'slow');
        bar.style.width = '100%'; paintLv();
        timers.push(setTimeout(stepUp, 1300));
      } else {
        nowSong.textContent = '🎺'; set('song', 'bright'); set('r', 'sun'); lock(false);
        pop(['🌤️', '🎶', '🐧', '✨'], 16);
      }
    }
    timers.push(setTimeout(stepUp, 1700));
  }
  function pop(list, n) {
    if (!window.pengessoPop) return;
    var r = nowSong.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, n);
  }
  function change(d) {
    if (busy) return;
    lv = Math.max(1, Math.min(5, lv + d)); clear();
    set('r', ''); set('song', ''); bar.style.width = '0'; nowSong.textContent = ' ';
    paintLv(); bounce(we);
  }
  minus.addEventListener('click', function () { change(-1); });
  plus.addEventListener('click', function () { change(1); });
  bBright.addEventListener('click', function () { play('bright'); });
  bSlow.addEventListener('click', function () { play('slow'); });
  again.addEventListener('click', function () { clear(); lock(false); lv = 4; change(0); });
  paintLv();
})();