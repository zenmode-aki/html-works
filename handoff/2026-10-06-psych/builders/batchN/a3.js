__tap('.go');
[300,1300,2300,5600].forEach(function(t,i){ setTimeout(function(){ __tap('.ph', i%3); }, t); });
setTimeout(function(){ __log('mid', __st()); }, 1000);
setTimeout(function(){ __log('end', __st()); __log('sc', document.querySelector('.r-ok .sc').textContent); __log('days', document.querySelector('.d-n').textContent); }, 9500);
