setTimeout(function(){ __tap('.tap'); __log('late1', __st()); __tap('.tap'); __log('other', __st()); __tap('.tap'); __log('late2', __st()); __log('pops', window.__pops); }, 300);
