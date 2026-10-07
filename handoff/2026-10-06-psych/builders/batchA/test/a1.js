setTimeout(function(){ __tap('.pick',4); __log('after5', __st()); }, 300);
setTimeout(function(){ __tap('.pick',0); __tap('.pick',1); __tap('.pick',2); __tap('.pick',3); __log('all', __st()); __log('fn', document.querySelector('.f-n').textContent); }, 600);
setTimeout(function(){ __tap('.pick',0); __log('hearts', document.querySelectorAll('.hearts i.on').length); }, 900);
