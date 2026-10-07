/* 🍜 笑顔ダイヤル：JS は data-lv / class / 絵文字 / 数字だけを変える。文字は上の HTML（訳がそのまま効く） */
(function () {
  var g = document.querySelector('.game'); if (!g) return;
  var CLERK = ['', '😶', '😐', '🙂', '😊', '😄'], CUST = ['', '😟', '😕', '🙂', '😊', '🤩'];
  var minus = g.querySelector('.minus'), plus = g.querySelector('.plus'), num = g.querySelector('.lv-n');
  var clerk = g.querySelector('.clerk-b'), cust = g.querySelector('.cust-b');
  var say = g.querySelector('.say'), feel = g.querySelector('.feel');
  var groups = [g.querySelectorAll('.waves i'), g.querySelectorAll('.stars i'), g.querySelectorAll('.lv-dots i')];
  var lv = 1, popped = false;
  function restart(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  function set(v) {
    var old = lv;
    lv = Math.max(1, Math.min(5, v));
    g.setAttribute('data-lv', String(lv));
    num.textContent = lv;
    clerk.textContent = CLERK[lv]; cust.textContent = CUST[lv];
    groups.forEach(function (list) { [].forEach.call(list, function (el, i) { el.classList.toggle('on', i < lv); }); });
    minus.disabled = lv <= 1; plus.disabled = lv >= 5;
    if (lv !== old) { restart(say, 'boing'); restart(feel, 'boing'); restart(num, 'boing'); restart(clerk, 'boing'); restart(cust, 'boing'); }
    if (lv === 5 && old !== 5 && !popped && window.pengessoPop) {
      popped = true;
      var r = g.querySelector('.bowl-e').getBoundingClientRect();
      window.pengessoPop(r.left + r.width / 2, r.top + r.height / 2, ['🍜', '✨', '🐧', '⭐', '♨️'], 18);
    }
  }
  minus.addEventListener('click', function () { set(lv - 1); });
  plus.addEventListener('click', function () { set(lv + 1); });
  g.querySelector('.reset').addEventListener('click', function () { popped = false; set(1); });
  set(1);
})();