import sys,re,pathlib
R=pathlib.Path("/Users/ezakimasaaki/Desktop/html-works/draft")
for s in open(sys.argv[1]).read().split():
    t=(R/s/"index.html").read_text(); src=(R/s/"source.md").read_text(); ja=(R/s/"i18n/ja.json").read_text()
    body=re.sub(r"<script.*?</script>|<style.*?</style>","",t,flags=re.S)
    out=[]
    for w in ["僕","会社","職場","上司","同僚","残業","恋人","彼氏","彼女","デート","告白","部下"]:
        if w in ja or w in re.sub(r"## 出どころ.*?\n## ","",src,flags=re.S): out.append(w)
    out+= [c for c in "🙅🙆🧑👩👨🙋💁🤷🏃🧍🙇💏💑" if c in t]
    for w in ["boss","company","office","coworker","girlfriend","boyfriend","manager"]:
        if re.search(r"\b"+w+r"\b", body, re.I): out.append(w)
    if out: print(s, out)
