__tap('.rc', 0);
setTimeout(function(){ __log('flat', __st()); __tap('.rc', 1); }, 800);
setTimeout(function(){ __log('warm', __st()); __tap('.tab', 1); __tap('.rc', 2); }, 3000);
setTimeout(function(){ __log('end', __st()); __log('n', document.querySelector('.mn').textContent); }, 5500);
