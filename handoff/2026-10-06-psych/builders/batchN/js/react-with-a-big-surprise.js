/* 🎉 驚きコンボ：JS は data-* / class / 絵文字 / 数字 / style だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var N = 6;
  var news = g.querySelector('.news'), react = g.querySelector('.fr-react');
  var bar = g.querySelector('.heat-bar i'), cbN = g.querySelector('.cb-n');
  var vws = [].slice.call(g.querySelectorAll('.vw'));
  var FACE = ['🙂', '😊', '😄', '😆', '🤩', '🤩', '🥳'];
  var q = 0, combo = 0, used = {}, lock = false;
  function restart(el, c) { el.classList.remove(c); void el.offsetWidth; el.classList.add(c); }
  function state(s) { g.setAttribute('data-s', s); }
  function drawHeat() {
    cbN.textContent = String(combo); restart(cbN, 'boing');
    bar.style.width = (combo / N * 100) + '%';
  }
  function start() {
    q = 0; combo = 0; used = {}; lock = false;
    vws.forEach(function (v) { v.classList.remove('used'); });
    g.setAttribute('data-all', '0'); g.setAttribute('data-q', '0');
    react.textContent = '🙂'; drawHeat(); state('run'); restart(news, 'fresh');
  }
  g.querySelector('.go').addEventListener('click', start);
  vws.forEach(function (v) {
    v.addEventListener('click', function () {
      if (g.getAttribute('data-s') !== 'run' || lock) return;
      combo++; used[v.getAttribute('data-v')] = 1; v.classList.add('used');
      react.textContent = FACE[combo]; restart(react, 'boing'); drawHeat();
      var r = v.getBoundingClientRect();
      if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top, ['✨', '🎉', '💜'], 6 + combo);
      if (combo >= N) {
        lock = true;
        var all = Object.keys(used).length === 5;
        g.setAttribute('data-all', all ? '1' : '0');
        setTimeout(function () {
          state('done'); react.textContent = '🥳'; restart(news, 'fresh');
          if (window.pengessoPop) { var b = news.getBoundingClientRect(); window.pengessoPop(b.left + b.width / 2, b.top + b.height / 2, all ? ['🏅', '🎉', '🐧', '✨', '🔥'] : ['🎉', '🐧', '✨', '🔥'], 22); }
        }, 350);
        return;
      }
      q++; g.setAttribute('data-q', String(q)); restart(news, 'fresh');
    });
  });
  g.querySelector('.flat').addEventListener('click', function () {
    if (g.getAttribute('data-s') !== 'run' || lock) return;
    combo = 0; drawHeat();
    react.textContent = '😶'; restart(react, 'boing');
    state('flat'); restart(news, 'fresh');
  });
})();