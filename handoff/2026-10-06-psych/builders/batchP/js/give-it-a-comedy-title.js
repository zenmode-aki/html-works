/* 🎬 コントのタイトル：JS は data-st / class / style / 絵文字 / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var KEY = 'pengesso-give-it-a-comedy-title-found';
  var titles = [].slice.call(g.querySelectorAll('.slot span'));
  var reel = [].slice.call(g.querySelectorAll('.reel i'));
  var bar = g.querySelector('.bar i'), fn = g.querySelector('.fn'), youT = g.querySelector('.you-t'), clap = g.querySelector('.clap');
  var cur = 0, busy = false, found = {};
  try { found = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch (e) { found = {}; }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(found)); } catch (e) {} }
  function show(i) { cur = i; titles.forEach(function (t, k) { t.classList.toggle('on', k === i); }); }
  function drawFound() {
    var n = 0;
    reel.forEach(function (r, i) { var on = !!found[i + 1]; r.classList.toggle('on', on); if (on) n++; });
    fn.textContent = n + '/4';
    return n;
  }
  function reduced() { try { return window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) { return false; } }
  clap.addEventListener('click', function () {
    if (busy) return;
    busy = true;
    g.setAttribute('data-st', 'spin');
    bar.style.width = '70%';
    var pick; do { pick = 1 + Math.floor(Math.random() * 4); } while (pick === cur && cur > 0);
    var steps = reduced() ? 1 : 12, i = 0, k = cur || 1;
    (function spin() {
      i++;
      if (i < steps) { k = k % 4 + 1; show(k); setTimeout(spin, 60 + i * 9); return; }
      show(pick);
      g.setAttribute('data-st', 'comedy');
      bar.style.width = '15%'; youT.textContent = '😏';
      var before = drawFound(); found[pick] = 1; save(); var after = drawFound();
      busy = false;
      if (window.pengessoPop) {
        var r = clap.getBoundingClientRect();
        window.pengessoPop(r.left + r.width / 2, r.top, after === 4 && before < 4 ? ['🎬', '👏', '😆', '🐧', '🎉'] : ['👏', '😆', '🎬'], after === 4 && before < 4 ? 22 : 12);
      }
    })();
  });
  g.querySelector('.reset').addEventListener('click', function () {
    if (busy) return;
    show(0); g.setAttribute('data-st', 'tense'); bar.style.width = '90%'; youT.textContent = '😰';
  });
  drawFound();
})();