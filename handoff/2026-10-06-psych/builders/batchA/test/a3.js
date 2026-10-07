setTimeout(function(){ __tap('.tap'); __log('s0', __st()); var k=setInterval(function(){ if(document.querySelector('.game').getAttribute('data-s')!=='run'){clearInterval(k);__log('end1', __st());return;} __tap('.tap'); }, 200); }, 200);
setTimeout(function(){ __tap('.tap'); __log('s2start', __st()); }, 7500);
setTimeout(function(){ __log('end2', __st()); __log('streak', document.querySelector('.streak-n').textContent + '/' + document.querySelector('.best-n').textContent); }, 14000);
