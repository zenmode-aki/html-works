import re,sys,glob
bad=0
for f in sorted(glob.glob('works/*/index.html')):
    s=open(f).read()
    for m in re.finditer(r'<section class="toy[^"]*"[^>]*>.*?</section>',s,re.S):
        sec=m.group(0)
        attrs=re.findall(r'(?:aria-label|title|alt)="([^"]*)"',sec)
        txt=re.sub(r'<[^>]+>',' ',re.sub(r'<(script|style)[^>]*>.*?</\1>','',sec,flags=re.S))
        hits=[t for t in attrs+[txt] if re.search(r'[A-Za-z]{2,}',t)]
        if hits: bad+=1; print(f.split('/')[1], [h.strip()[:60] for h in hits][:3])
print('toys',len([f for f in glob.glob('works/*/index.html') if 'class="toy' in open(f).read()]),'bad',bad)
