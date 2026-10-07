/* 📱 カフェのおしゃべり：JS は data-i / data-buzz / data-w / data-end / data-r / class / 絵文字 / 数字だけを変える。文字は上の HTML */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var BUZZ_AT = { 2: 1, 4: 1 };
  var i = 0, combo = 0, looks = 0, hearts = 0, buzzed = {};
  var story = g.querySelector('.story'), react = g.querySelector('.react'), phone = g.querySelector('.phone'), cbN = g.querySelector('.cb-n');
  var hs = [].slice.call(g.querySelectorAll('.link i'));
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function drawHearts() { hs.forEach(function (h, k) { h.classList.toggle('on', k < hearts); }); }
  function setCombo(n) { combo = n; cbN.textContent = String(n); restart(cbN, 'bump'); }
  function maybeBuzz() {
    if (BUZZ_AT[i] && !buzzed[i]) {
      buzzed[i] = 1;
      phone.classList.remove('down'); phone.textContent = '📱';
      g.setAttribute('data-buzz', '1');
      if (navigator.vibrate) { try { navigator.vibrate([40, 60, 40]); } catch (e) {} }
    }
  }
  function next() {
    i++;
    g.setAttribute('data-i', String(i)); restart(story, 'show');
    if (i >= 6) {
      g.setAttribute('data-end', '1');
      g.setAttribute('data-r', looks ? 'alone' : 'good');
      react.textContent = looks ? '😶' : '🥰'; restart(react, 'boing');
      if (!looks && window.pengessoPop) {
        var r = story.getBoundingClientRect();
        window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['💞', '🍰', '🐧', '☕', '✨'], 22);
      }
      return;
    }
    maybeBuzz();
  }
  g.querySelector('.nod').addEventListener('click', function () {
    if (g.getAttribute('data-buzz') === '1' || i >= 6) return;
    g.setAttribute('data-w', '0');
    hearts = Math.min(hs.length, hearts + 1); drawHearts();
    setCombo(combo + 1);
    react.textContent = looks ? '🙂' : '😊';
    next();
  });
  g.querySelector('.look').addEventListener('click', function () {
    looks++;
    g.setAttribute('data-buzz', '0'); g.setAttribute('data-w', '1');
    hearts = Math.max(0, hearts - 2); drawHearts();
    setCombo(0);
    react.textContent = '😶'; restart(react, 'boing');
  });
  g.querySelector('.flip').addEventListener('click', function () {
    g.setAttribute('data-buzz', '0');
    phone.classList.add('down'); phone.textContent = '🔕';
    hearts = Math.min(hs.length, hearts + 1); drawHearts();
    setCombo(combo + 1);
    react.textContent = '😊'; restart(react, 'boing');
    if (window.pengessoPop) { var r = phone.getBoundingClientRect(); window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['💞', '✨'], 8); }
  });
  g.querySelector('.reset').addEventListener('click', function () {
    i = 0; looks = 0; hearts = 0; buzzed = {};
    setCombo(0); drawHearts();
    phone.classList.remove('down'); phone.textContent = '📱'; react.textContent = '😊';
    g.setAttribute('data-i', '0'); g.setAttribute('data-buzz', '0'); g.setAttribute('data-w', '0'); g.setAttribute('data-end', '0'); g.setAttribute('data-r', '');
    restart(story, 'show');
  });
})();