__tap('.startbtn');
var k=0; function go(){ var b=document.querySelectorAll('.bub:not(.popped)')[0]; if(b) b.click(); k++; if(k<4) setTimeout(go,300); }
setTimeout(go, 500);
setTimeout(function(){ __log('a', __st()); }, 3000);
