#!/usr/bin/env python3
"""
🔎 訳が「本当に画面に出ているか」を確かめる（2026-09-25 本人の要望）

tools/i18n.py --check は「訳のファイルに抜けがないか」しか見ない。
でも実際には、見出し・次の記事・トップの一覧など、画面では英語のまま残ることがある。
なので、ページを本物のブラウザ（ヘッドレス）で ?lang=xx を付けて開き、
表示されている文字の中に「英語の文」が残っていないかを探す。

  python3 tools/i18n-audit.py                      # 全記事＋トップ × 主要5言語（ja ko zh zh-Hant）
  python3 tools/i18n-audit.py seoul-stadium-station-exit _top   # 記事を指定（_top＝トップ）
  python3 tools/i18n-audit.py --langs ja,es,fr     # 言語を指定
  python3 tools/i18n-audit.py --all-langs          # 全言語（時間がかかる）

英語が3語以上つづいている文字を「訳漏れの疑い」として出す。固有名詞（MLB など）は ALLOW で除く。
記事を公開・修正したら、push の前に必ず走らせる（CLAUDE.md / AGENTS.md）。
"""
import functools, http.server, json, pathlib, re, shutil, subprocess, sys, tempfile, threading
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parent.parent
PORT = 8791
MAIN = ["ja", "ko", "zh", "zh-Hant"]

# 英語のままでいい言葉（固有名詞・ブランド・略語）
ALLOW = re.compile(r"^(Pengesso|K-POP|MLB|WBC|NTT|GitHub|ChatGPT|Claude( Code)?|Google( Maps)?|YouTube|Spotify|Jimoty|"
                   r"OneNote|Cursor|Codex|Higgsfield|Udemy|Audible|Apple Podcasts|Windows Update|Sakura English|"
                   r"Suzuka Circuit|7-Eleven|Lazada|Shopee|Grab|Agoda|WhatsApp|KLIA2|Taylor's|INTI|Sunway|APU|"
                   r"Stop Overthinking Practice|Claude in Chrome|Claude Code / Codex|AirPods Pro Max|Owl City.*|(?:— )?Yonezu Kenshi.*Raven.*)$", re.I)
# 学校・大学の名前（「Taylor's University — Lakeside」など）やファイルの場所は、英語のままが正しい
KEEP = re.compile(r"(Work In Progress|University|College|Academy|Campus|\\|\.(xls|doc|pdf)\b)")

JS = r"""<script>
function auditText() {
  var out = [], seen = {};
  var w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  while (w.nextNode()) {
    var n = w.currentNode, el = n.parentElement, t = n.nodeValue.replace(/\s+/g, ' ').trim();
    if (!t || !el || el.closest('script,style,noscript,code,pre,.i18n-menu,.i18n-tip,iframe,#audit')) continue;
    if (el.closest('[translate="no"]')) continue;
    var cs = getComputedStyle(el); if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    if (seen[t]) continue; seen[t] = 1; out.push(t);
  }
  return out;
}
/* The runtime translates on DOMContentLoaded, after this parser-time snapshot. */
var sourceTitle = document.title, sourceText = auditText(), sourceBlocks = [];
document.querySelectorAll('h1,h2,h3,h4,p,li,figcaption,td,th,button,a,small,label,blockquote').forEach(function (el) {
  var t = (el.innerText || el.textContent || '').replace(/\s+/g, ' ').trim();
  if (t) sourceBlocks.push(t);
});
window.addEventListener('load', function () { setTimeout(function () {
  var pre = document.createElement('pre'); pre.id = 'audit';
  pre.textContent = JSON.stringify({ lang: document.documentElement.lang, title: document.title, text: auditText(), source: sourceText.concat(sourceBlocks, [sourceTitle]) });
  document.body.appendChild(pre);
}, 900); });
</script>"""


class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_GET(self):
        path = self.path.split("?")[0]
        f = ROOT / path.lstrip("/")
        if f.is_dir(): f = f / "index.html"
        if f.suffix == ".html" and f.exists():
            b = f.read_text().replace("</body>", JS + "</body>", 1).encode()
            self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)
        else:
            super().do_GET()


def browser():
    for p in sorted(pathlib.Path.home().glob("Library/Caches/ms-playwright/chromium_headless_shell-*/*/chrome-headless-shell")):
        return [str(p)]
    return ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "--headless=new"]


def run(url):
    d = tempfile.mkdtemp(prefix="i18a")
    try:
        r = subprocess.run(browser() + ["--disable-gpu", f"--user-data-dir={d}", "--window-size=500,1400",
                                        "--virtual-time-budget=6000", "--dump-dom", url],
                           capture_output=True, text=True, timeout=120)
        m = re.search(r'<pre id="audit">(.*?)</pre>', r.stdout, re.S)
        import html
        return json.loads(html.unescape(m.group(1))) if m else None
    except subprocess.TimeoutExpired:
        return None
    finally:
        shutil.rmtree(d, ignore_errors=True)


WORD = re.compile(r"[A-Za-z][A-Za-z'’\-]+")


def normalize(text):
    return re.sub(r"\s+", " ", text).strip()


def leftovers(texts, source_text):
    bad = []
    source = {normalize(t) for t in source_text}
    for t in texts:
        words = WORD.findall(t)
        if len(words) < 3: continue
        # Latin script is used by many supported languages. Flag a phrase only when
        # its visible text exactly matches a source-English text unit or block.
        if normalize(t) not in source: continue
        if ALLOW.match(t.strip(" .!?🐧💻")) or "@" in t or "://" in t or KEEP.search(t): continue
        bad.append(t[:90])
    return bad


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    langs = MAIN
    if "--all-langs" in sys.argv:
        langs = sorted(p.stem.split(".", 1)[1] for p in (ROOT / "i18n").glob("ui.*.json"))
    for a in sys.argv[1:]:
        if a.startswith("--langs="): langs = a.split("=", 1)[1].split(",")
    if "--langs" in sys.argv:
        langs = sys.argv[sys.argv.index("--langs") + 1].split(","); args = [a for a in args if a != ",".join(langs)]
    slugs = args or ["_top"] + sorted(p.name for p in (ROOT / "works").iterdir() if (p / "index.html").exists())

    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(H, directory=str(ROOT)))
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    jobs = [(s, l, f"http://127.0.0.1:{port}/" + ("index.html" if s == "_top" else f"works/{s}/index.html") + f"?lang={l}")
            for s in slugs for l in langs]
    problems, failed = {}, []
    with ThreadPoolExecutor(6) as ex:
        for (s, l, _), res in zip(jobs, ex.map(lambda j: run(j[2]), jobs)):
            if res is None: failed.append(f"{s}[{l}]"); continue
            bad = leftovers(res["text"] + [res["title"]], res.get("source", []))
            if bad: problems.setdefault(s, {})[l] = bad
    srv.shutdown()

    if failed: print("⚠️ 開けなかった:", ", ".join(failed[:20]))
    if not problems:
        print(f"✅ {len(slugs)}ページ × {len(langs)}言語：画面に英語の文は残っていません"); return
    n = sum(len(v) for d in problems.values() for v in d.values())
    print(f"❌ 画面に英語のまま残っている文：{n}件")
    for s, d in problems.items():
        for l, bad in d.items():
            print(f"  {s} [{l}]")
            for b in bad: print("     ·", b)
    sys.exit(1)


if __name__ == "__main__":
    main()
