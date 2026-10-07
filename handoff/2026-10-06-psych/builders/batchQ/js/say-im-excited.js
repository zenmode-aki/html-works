/* 💓 同じドキドキ：心拍の数字は120のまま。JS は data-pick・data-both・class・絵文字だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var face = g.querySelector('.face'), st = g.querySelector('.st');
  var btns = [].slice.call(g.querySelectorAll('.choice'));
  var seen = {};
  btns.forEach(function (b) {
    b.addEventListener('click', function () {
      var p = b.getAttribute('data-p');
      g.setAttribute('data-pick', '');
      void g.offsetWidth;
      g.setAttribute('data-pick', p);
      btns.forEach(function (x) { x.classList.toggle('on', x === b); });
      face.textContent = p === 'calm' ? '😰' : '🤩';
      st.textContent = p === 'calm' ? '★☆☆' : '★★★';
      seen[p] = true;
      if (seen.calm && seen.excite) g.setAttribute('data-both', '1');
      if (p === 'excite') {
        if (window.pengessoPop) { var r = b.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top, ['✨', '🎤', '🐧', '⭐'], 16); }
        if (navigator.vibrate) { try { navigator.vibrate(25); } catch (e) {} }
      }
    });
  });
})();