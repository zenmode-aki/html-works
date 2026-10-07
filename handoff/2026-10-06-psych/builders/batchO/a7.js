var seq=['.nod','.nod','.look','.nod','.nod','.flip','.nod','.nod']; var k=0; function nx(){ if(k>=seq.length){ __log('st',__st()); return;} __tap(seq[k]); k++; setTimeout(nx,400);} nx();
