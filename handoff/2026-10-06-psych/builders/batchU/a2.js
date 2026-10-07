__tap('.namebtn',0); __tap('.namebtn',1);
setTimeout(function(){ __log('mid', __st()); __tap('.namebtn',2); }, 2000);
setTimeout(function(){ __log('end', __st()); __log('cn', document.querySelector('.cn').textContent); }, 4500);
