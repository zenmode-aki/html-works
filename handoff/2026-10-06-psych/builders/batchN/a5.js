var t=0; for (var k=0;k<9;k++) (function(k){ setTimeout(function(){ __tap('.pour', k%3); }, k*600); })(k);
setTimeout(function(){ __log('mid', __st()); __log('n', [].map.call(document.querySelectorAll('.pct .n'), function(x){return x.textContent;})); }, 2500);
setTimeout(function(){ __log('end', __st()); __log('n2', [].map.call(document.querySelectorAll('.pct .n'), function(x){return x.textContent;})); }, 6500);
