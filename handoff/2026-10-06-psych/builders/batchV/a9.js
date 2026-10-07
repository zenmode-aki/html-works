var seq=[0,1,2,3,4]; var i=0; var t=setInterval(function(){ __tap('.brk',seq[i]); i++; if(i>=seq.length){clearInterval(t); __log('st', __st());}}, 400);
