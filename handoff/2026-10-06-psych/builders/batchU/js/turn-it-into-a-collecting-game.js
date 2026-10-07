/* 🃏 カード集め：やったことを押すとカードが1枚（ノーマル／レア／超レア）。5枚でごほうび。JS は data-* と数字と絵文字だけ */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var card = g.querySelector('.newcard'), ce = g.querySelector('.nc-e');
  var quests = [].slice.call(g.querySelectorAll('.quest')), slots = [].slice.call(g.querySelectorAll('.acard'));
  var an = g.querySelector('.an'), again = g.querySelector('.again');
  var n = 0, supers = 0;
  function pop(el, list, k) {
    if (!window.pengessoPop) return;
    var r = el.getBoundingClientRect();
    window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, list, k);
  }
  quests.forEach(function (q) {
    q.addEventListener('click', function () {
      if (q.getAttribute('data-done') === '1' || n >= 5) return;
      q.setAttribute('data-done', '1');
      var x = Math.random();
      var rar = x < 0.2 ? 3 : x < 0.55 ? 2 : 1;
      if (n === 4 && supers === 0) rar = 3;   /* 最後の1枚は、超レアがまだなら超レアにする（ごほうび感） */
      if (rar === 3) supers++;
      var e = q.getAttribute('data-e');
      ce.textContent = e;
      card.setAttribute('data-rar', rar);
      card.classList.remove('in'); void card.offsetWidth; card.classList.add('in');
      slots[n].querySelector('.ae').textContent = e;
      slots[n].setAttribute('data-rar', rar);
      n++; an.textContent = n;
      if (rar === 3) pop(card, ['⭐', '✨', e], 12);
      if (n === 5) {
        g.setAttribute('data-all', '1');
        setTimeout(function () { pop(g.querySelector('.r-done'), ['🍨', '🃏', '🐧', '✨'], 18); }, 120);
        if (navigator.vibrate) { try { navigator.vibrate(30); } catch (err) {} }
      }
    });
  });
  again.addEventListener('click', function () {
    n = 0; supers = 0; an.textContent = 0;
    quests.forEach(function (q) { q.removeAttribute('data-done'); });
    slots.forEach(function (s) { s.removeAttribute('data-rar'); });
    card.setAttribute('data-rar', '0'); ce.textContent = '🐧';
    g.setAttribute('data-all', '0');
  });
})();