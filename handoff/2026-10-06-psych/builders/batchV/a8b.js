var seq=['.ch-b','.ch-c','.ch-c','.seat']; var i=0; var t=setInterval(function(){ __tap(seq[i]); i++; if(i>=seq.length){clearInterval(t); __log('st', __st());}}, 600);
