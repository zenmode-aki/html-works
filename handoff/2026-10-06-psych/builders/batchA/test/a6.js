setTimeout(function(){ __tap('.bub',0); __tap('.bub',0); __tap('.bub',2); __log('two', __st()); __log('pct', document.querySelector('.pct').textContent); }, 300);
setTimeout(function(){ __tap('.bub',1); __tap('.bub',3); __tap('.bub',4); __tap('.bub',5); __log('all', __st()); }, 600);
