var seq=[['.fr',0],['.fr',1],['.fr',2],['.later',0]]; var i=0; var t=setInterval(function(){ __tap(seq[i][0],seq[i][1]); i++; if(i>=seq.length){clearInterval(t); __log('st', __st());}}, 400);
