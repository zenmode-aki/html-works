/* 👀 笑顔をキープ：JS は data-* / 幅 / 絵文字 / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var KEY = 'pengesso-keep-smiling-until-eyes-meet-best';
  var btn = g.querySelector('.tap'), fill = g.querySelector('.sm-fill'), face = g.querySelector('.me-badge');
  var them = g.querySelector('.them'), stN = g.querySelector('.streak-n'), bestN = g.querySelector('.best-n');
  var level = 100, tick = 0, turnT = 0, twitchT = 0, lock = 0, streak = 0, best = 0;
  try { best = parseInt(localStorage.getItem(KEY), 10) || 0; } catch (e) {}
  bestN.textContent = best;
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function faceFor(l) { return l >= 75 ? '😄' : l >= 50 ? '😊' : l >= 25 ? '😐' : '😑'; }
  function draw() {
    fill.style.width = level + '%';
    face.textContent = faceFor(level);
    g.setAttribute('data-ok', level >= 50 ? '1' : '0');
  }
  function stop() { clearInterval(tick); clearTimeout(turnT); clearTimeout(twitchT); }
  function start() {
    stop();
    level = 100; draw();
    g.setAttribute('data-look', 'away');
    g.setAttribute('data-s', 'run');
    var wait = 2600 + Math.random() * 2800;
    tick = setInterval(function () { level = Math.max(0, level - 2.1); draw(); }, 50);
    twitchT = setTimeout(function () { restart(them, 'twitch'); }, wait * (0.35 + Math.random() * 0.25));
    turnT = setTimeout(turn, wait);
  }
  function turn() {
    stop();
    g.setAttribute('data-look', 'here');
    var win = level >= 50;
    streak = win ? streak + 1 : 0;
    if (streak > best) { best = streak; try { localStorage.setItem(KEY, String(best)); } catch (e) {} }
    stN.textContent = streak; bestN.textContent = best;
    g.setAttribute('data-s', win ? 'win' : 'lose');
    lock = Date.now() + 900;   /* 連打の勢いで、すぐ次が始まらないように */
    if (win && window.pengessoPop) {
      var r = g.querySelector('.lane').getBoundingClientRect();
      window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['💫', '😊', '🐧', '💌', '✨'], 18);
    }
    if (win && navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
  }
  btn.addEventListener('click', function () {
    if (Date.now() < lock) return;
    if (g.getAttribute('data-s') === 'run') {
      level = Math.min(100, level + 16); draw(); restart(face, 'boing');
      return;
    }
    start();
  });
  draw();
})();