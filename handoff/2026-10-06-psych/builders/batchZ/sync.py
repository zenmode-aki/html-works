import re,sys
R='/Users/ezakimasaaki/Desktop/html-works/draft/'
for s in sys.argv[1:]:
    p=R+s+'/index.html'; h=open(p).read()
    m=re.search(r'class="wc-badge">⚡ (\d+) words · (\d+) sec',h)
    h=re.sub(r'(<span class="topic">🐧 EVERYDAY LIFE</span>⚡ )\d+( SEC)', r'\g<1>'+m.group(2)+r'\2', h)
    open(p,'w').write(h); print(s, m.group(1), m.group(2))
