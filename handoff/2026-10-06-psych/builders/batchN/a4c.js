__tap('.go'); __tap('.vw', 0);
setTimeout(function(){ var n=document.querySelector('.news'); __log('an', n.getAnimations().map(function(a){return a.animationName+' '+a.playState+' '+a.currentTime;})); __log('op', getComputedStyle(n).opacity); var r=document.querySelector('.r-run'); __log('rop', getComputedStyle(r).opacity); }, 3000);
