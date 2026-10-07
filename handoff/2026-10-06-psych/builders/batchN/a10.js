__tap('.wait');
setTimeout(function(){ __log('wait', __st()); }, 1400);
for (var k=0;k<7;k++) (function(k){ setTimeout(function(){ __tap('.invite'); }, 1600 + k*800); })(k);
setTimeout(function(){ __log('end', __st()); __log('n', document.querySelector('.cn').textContent); }, 7800);
