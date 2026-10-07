# usage: python3 prompts.py slug... → JSON [{slug, prompt}]
import sys, json, re, pathlib
R = pathlib.Path("/Users/ezakimasaaki/Desktop/html-works/draft")
out = []
for s in sys.argv[1:]:
    t = (R / s / "source.md").read_text()
    m = re.search(r"## 表紙のプロンプト\s*\n+(.*?)(\n## |\Z)", t, re.S)
    p = m.group(1).strip() if m else ""
    p = re.sub(r"^```\w*\n|```$", "", p).strip()
    out.append({"slug": s, "prompt": " ".join(p.split())})
print(json.dumps(out, ensure_ascii=False, indent=0))
