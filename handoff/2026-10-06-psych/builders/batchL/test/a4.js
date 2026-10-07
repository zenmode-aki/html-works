var b=document.querySelector('.bag'), cs=getComputedStyle(b);
__log('ws', cs.whiteSpace); __log('bagW', b.getBoundingClientRect().width); __log('stageW', document.querySelector('.stage').getBoundingClientRect().width);
__log('bagsW', document.querySelector('.bags').getBoundingClientRect().width); __log('disp', cs.display);
