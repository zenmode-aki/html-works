setTimeout(function(){ __tap('.serve'); __log('bad', __st()); }, 200);
setTimeout(function(){ __tap('.t-top'); __tap('.serve'); __log('half', __st()); }, 500);
setTimeout(function(){ __tap('.t-bot'); __tap('.add'); __tap('.add'); __tap('.add'); __log('n', __st()); __log('addDisabled', document.querySelector('.add').disabled); __tap('.serve'); __log('good', __st()); }, 800);
