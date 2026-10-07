#!/usr/bin/env python3
"""t.py <slug> [actions.js] [--dark] [--reduce] [--h=2400] [--w=390] [--shot=name] [--game]
Copies draft/<slug>/index.html to scratchpad, injects an error catcher + actions, runs headless Chromium,
prints {errs, overflow, report} and saves a PNG screenshot. Read-only for the repo.
--game : scroll so the .game section is at the top of the screenshot."""
import glob, html, json, pathlib, re, shutil, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
ROOT = pathlib.Path("/Users/ezakimasaaki/Desktop/html-works")
args = [a for a in sys.argv[1:] if not a.startswith("--")]
flags = {a.split("=")[0]: (a.split("=", 1)[1] if "=" in a else True) for a in sys.argv[1:] if a.startswith("--")}
slug = args[0]
actions = pathlib.Path(args[1]).read_text() if len(args) > 1 else ""
H = int(flags.get("--h", 2400)); W = int(flags.get("--w", 390))
src = (ROOT / "draft" / slug / "index.html").read_text(encoding="utf-8")
head = """<script>window.__errs=[];window.addEventListener('error',function(e){window.__errs.push(String(e.message||e)+' @'+e.lineno);});
window.__pops=0;window.pengessoPop=function(){window.__pops++;};
try{localStorage.clear();}catch(e){}</script>"""
if flags.get("--game"):
    head += '<style>main > *:not(.game){display:none !important} main{padding-top:8px !important}</style>'
if flags.get("--dark"):
    head += '<script>document.documentElement.setAttribute("data-theme","dark");</script>'
body = """<script>
window.__report = {};
function __log(k, v) { window.__report[k] = v; }
function __tap(sel, i) { var els = document.querySelectorAll(sel); var el = els[i || 0]; if (!el) { __log('missing:' + sel, true); return; }
  try { el.dispatchEvent(new PointerEvent('pointerdown', {bubbles: true})); } catch (e) {}
  el.click(); }
function __st(sel) { var g = document.querySelector(sel || '.game'); var o = {}; [].slice.call(g.attributes).forEach(function (a) { if (a.name.indexOf('data-') === 0) o[a.name] = a.value; }); return o; }
window.addEventListener('load', function () {
  document.querySelectorAll('.card, .game').forEach(function (c) { c.classList.add('in'); });
  try { (function () { %s })(); } catch (e) { window.__errs.push('ACTIONS: ' + e.message); }
  setTimeout(function () {
    var r = { errs: window.__errs, overflow: document.documentElement.scrollWidth - window.innerWidth, pops: window.__pops, report: window.__report };
    %s
    var pre = document.createElement('pre'); pre.id = 'mc'; pre.textContent = JSON.stringify(r); document.body.appendChild(pre);
  }, %d);
});
</script>""" % (actions, "", int(flags.get("--wait", 6000)))
doc = src.replace("<head>", "<head>\n<base href=\"file://%s/draft/%s/\">" % (ROOT, slug) + head, 1).replace("</body>", body + "</body>", 1)
out = HERE / "test"; out.mkdir(exist_ok=True)
page = out / f"{slug}.html"; page.write_text(doc, encoding="utf-8")
shell = sorted(glob.glob(str(pathlib.Path.home() / "Library/Caches/ms-playwright/chromium_headless_shell-*/*/chrome-headless-shell")))[-1]
name = flags.get("--shot", slug)
png = out / f"{name}.png"
d = tempfile.mkdtemp(prefix="tchk")
cmd = [shell, "--disable-gpu", "--no-sandbox", f"--user-data-dir={d}", f"--window-size={W},{H}", "--hide-scrollbars",
       "--allow-file-access-from-files", f"--virtual-time-budget={int(flags.get('--budget', 9000))}"]
if flags.get("--reduce"): cmd.append("--force-prefers-reduced-motion")
r = subprocess.run(cmd + ["--dump-dom", page.as_uri()], capture_output=True, text=True, timeout=90)
m = re.search(r'<pre id="mc">(.*?)</pre>', r.stdout, re.S)
print(html.unescape(m.group(1)) if m else "NO REPORT\n" + r.stderr[-800:])
if not flags.get("--noshot"):
    subprocess.run(cmd + [f"--screenshot={png}", page.as_uri()], capture_output=True, text=True, timeout=90)
    print("shot:", png)
shutil.rmtree(d, ignore_errors=True)
