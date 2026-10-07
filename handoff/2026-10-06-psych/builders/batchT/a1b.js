var k=0; function go(){ __tap('.sleep'); k++; if(k<6) setTimeout(go, 900); }
go();
setTimeout(function(){ __log('end', __st()); }, 6200);
