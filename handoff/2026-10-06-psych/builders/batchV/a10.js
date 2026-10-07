var seq=[0,2,1]; var i=0; var t=setInterval(function(){ __tap('.lc',seq[i]); i++; if(i>=seq.length){clearInterval(t); __log('st', __st());}}, 400);
