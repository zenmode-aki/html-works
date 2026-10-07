
/* 🚦 合図の解読機：JS は data-*・class・絵文字・数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var pcs = [].slice.call(g.querySelectorAll('.pc')), scn = g.querySelector('.sc-n'), siren = g.querySelector('.siren');
  var sel = null, got = 0, wt = 0;
  function side(el) { return el.classList.contains('ou') ? 'ou' : 'sg'; }
  function shake(el) { el.classList.remove('shake'); void el.offsetWidth; el.classList.add('shake'); }
  function say(w) { g.setAttribute('data-w', w); clearTimeout(wt); if (w !== '0') wt = setTimeout(function () { g.setAttribute('data-w', '0'); }, 1800); }
  pcs.forEach(function (p) {
    p.addEventListener('click', function () {
      if (p.classList.contains('done')) return;
      if (!sel || side(sel) === side(p)) {
        if (sel) sel.classList.remove('sel');
        sel = (sel === p) ? null : p;
        if (sel) sel.classList.add('sel');
        return;
      }
      var a = sel; sel = null; a.classList.remove('sel');
      if (a.getAttribute('data-k') === p.getAttribute('data-k')) {
        a.classList.add('done'); p.classList.add('done', 'pop'); a.classList.add('pop');
        got++; scn.textContent = String(got);
        say('2');
        var r = p.getBoundingClientRect();
        if (got >= 4) {
          g.setAttribute('data-all', '1'); siren.textContent = '🛡️';
          siren.classList.remove('pop'); void siren.offsetWidth; siren.classList.add('pop');
          if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🛡️', '🚦', '🐧', '✨', '💚'], 22);
          if (navigator.vibrate) { try { navigator.vibrate(30); } catch (e) {} }
        } else if (window.pengessoPop) window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['💚', '✨'], 8);
      } else {
        shake(a); shake(p); say('1');
        if (navigator.vibrate) { try { navigator.vibrate(15); } catch (e) {} }
      }
    });
  });
  g.querySelector('.b-reset').addEventListener('click', function () {
    sel = null; got = 0; scn.textContent = '0'; siren.textContent = '🚨';
    pcs.forEach(function (p) { p.classList.remove('done', 'sel', 'pop', 'shake'); });
    clearTimeout(wt); g.setAttribute('data-w', '0'); g.setAttribute('data-all', '0');
  });
})();
