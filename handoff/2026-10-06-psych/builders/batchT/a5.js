__tap('.choices .gbtn',0);
setTimeout(function(){ __tap('.choices .gbtn',1); __log('a', __st()); }, 300);
setTimeout(function(){ __tap('.choices .gbtn',2); __tap('.sip'); __tap('.sip'); __log('b', __st()); }, 600);
