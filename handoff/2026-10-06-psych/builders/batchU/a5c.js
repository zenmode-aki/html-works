for (var i=0;i<5;i++) __tap('.quest',i);
setTimeout(function(){var g=document.querySelector('.game'); __log('op',getComputedStyle(g).opacity); __log('anim', document.getAnimations().map(function(a){return (a.animationName||a.transitionProperty)+':'+a.playState+':'+(a.effect&&a.effect.target&&a.effect.target.className)}).join(','));},3000);
