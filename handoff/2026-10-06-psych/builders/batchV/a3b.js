var seq=['.walk','.vent','.walk','.vent','.change']; var i=0; var t=setInterval(function(){ __tap(seq[i]); i++; if(i>=seq.length){clearInterval(t); __log('st', __st());}}, 400);
