var seq=[1,1,0,0,1]; var k=0; function nx(){ if(k>=seq.length){ __log('st',__st()); return;} __tap(seq[k]?'.deliver':'.keepb'); k++; setTimeout(nx,600);} nx();
