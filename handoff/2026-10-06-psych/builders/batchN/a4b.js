__tap('.go'); for (var k=0;k<6;k++) __tap('.vw', k%5);
setTimeout(function(){ var n=document.querySelector('.news'); var cs=getComputedStyle(n); __log('bg', cs.backgroundColor+' '+cs.color+' '+cs.opacity+' '+n.className); }, 3000);
