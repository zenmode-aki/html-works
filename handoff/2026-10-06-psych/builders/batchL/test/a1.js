__tap('.app',0); __tap('.app',1); __tap('.app',2);
__log('afterTaps', __st());
__tap('.go');
__log('run', __st());
setTimeout(function(){ for (var i=3;i<8;i++) __tap('.app',i); __log('mid', __st()); }, 1500);
setTimeout(function(){ __log('end', __st()); __log('tm', document.querySelector('.tm').textContent); __log('best', document.querySelector('.best').hidden); }, 4500);
