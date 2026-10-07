setTimeout(function(){ __tap('.sw',0); __log('s1', __st()); }, 300);
setTimeout(function(){ __tap('.sw',1); __tap('.sw',2); __log('s3', __st()); }, 700);
setTimeout(function(){ __log('pts', document.querySelector('.pts').textContent); }, 2000);
