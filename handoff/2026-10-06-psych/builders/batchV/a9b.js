var seq=[1,3]; var i=0; var t=setInterval(function(){ __tap('.brk',seq[i]); i++; if(i>=seq.length){clearInterval(t); __log('st', __st());}}, 400);
