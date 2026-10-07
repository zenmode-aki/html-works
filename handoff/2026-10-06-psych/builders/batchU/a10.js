__tap('.gobtn'); __tap('.mess',0);
setTimeout(function(){__log('early',__st()); __tap('.gobtn');},9500);
setTimeout(function(){__log('messy',__st()); __log('n',document.querySelectorAll('.mess[data-on="1"]').length);},19500);
