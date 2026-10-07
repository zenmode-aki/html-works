__tap('.go'); for (var k=0;k<6;k++) __tap('.vw', k%5);
__log('done', __st());
setTimeout(function(){ __tap('.go'); __tap('.vw',0); __tap('.flat'); __log('flat', __st()); __tap('.go'); for (var k=0;k<6;k++) __tap('.vw', k%5); }, 1500);
