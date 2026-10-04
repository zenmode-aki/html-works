#!/usr/bin/env python3
"""
📱 スマホで壊れていないかを、本物のブラウザ（ヘッドレスChrome）で確かめる（2026-10-04）

2026-10-04 に「スマホで日本語の濃さが変わらない・アニメーションが出ない」が起きた。原因は、端末が「動きを減らす」設定のとき、
記事のCSSが全部の要素に opacity:1 !important を付けていたこと。パソコンでは起きないので、見つけにくかった。
同じことを二度と起こさないために、「スマホの幅」と「動きを減らす設定」で、記事を開いて確かめる。

  python3 tools/mobile-check.py                 # 見本の記事（いつもの12本）× 普通・動きを減らす
  python3 tools/mobile-check.py --all           # 全記事（時間がかかる）
  python3 tools/mobile-check.py seoul-stadium-station-exit jump-one-music-card   # 記事を指定

確かめること（日本語で開いて、勉強モードをオンにした状態で）：
  1. ページが開く・ランタイムが動いて JavaScript のエラーが出ない
  2. 横にはみ出さない（スマホで横スクロールが出ない）
  3. 勉強バーが出る（1段目：英語の勉強／言い換え／？）。2段目（濃さの4ボタン）は、オンにしたときだけ見える
  4. 「日本語の濃さ」を30％にしたら、日本語の文字（.learn-native）の opacity が本当に0.3になる ← 2026-10-04 の事故
  5. 動きを減らす設定のときは、カードが全部見える（opacity 1）。透明にして重ねた部品（言い換えの select）は、どちらでも見えない
  6. 日本語の見出しが文節で折り返される（BudouX が動いて .ja-ph が付く）

Chrome の場所：環境変数 CHROME、なければ Mac / Linux の普通の場所（Playwright の Chromium も探す）。
"""
import functools, glob, html, http.server, json, os, pathlib, re, shutil, subprocess, sys, tempfile, threading
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parent.parent
for _a in sys.argv:
    if _a.startswith("--root="): ROOT = pathlib.Path(_a.split("=", 1)[1]).resolve()   # 別の場所（古い版を取り出したもの）で確かめるとき

SAMPLE = [
    "jump-one-music-card", "seoul-stadium-station-exit", "120-eggs", "paste-one-at-a-time", "a-jeepney-all-to-myself",
    "ai-average-score", "best-buys-2026", "korean-ballpark-food-is-cheap", "a-little-cold-makes-you-sleepy",
    "baguio-language-school-memories", "udemy-new-hobby", "two-claude-apps",
]

# 見張り番のスクリプト。ページの先頭（<head> の中）に入れて、設定を先に書く → 読み込み後に調べて、結果を <pre id="mc"> に出す
HEAD_JS = """<script>
try { localStorage.setItem('pengesso-learn', '1'); localStorage.setItem('pengesso-native-alpha', '30');
      localStorage.setItem('pengesso-study-tip', '9'); localStorage.setItem('pengesso-tip-seen', '1'); localStorage.setItem('pengesso-motion-note', '9');
      localStorage.removeItem('pengesso-motion'); } catch (e) {}
window.__errs = [];
window.addEventListener('error', function (e) { window.__errs.push(String(e.message || e)); });
</script>"""

BODY_JS = """<script>
window.addEventListener('load', function () { setTimeout(function () {
  var r = { errs: window.__errs, ow: document.documentElement.scrollWidth - window.innerWidth, vw: window.innerWidth };
  var bar = document.querySelector('.study-bar');
  r.bar = !!bar;
  r.reduce = window.matchMedia ? window.matchMedia('(prefers-reduced-motion: reduce)').matches : null;
  var tray = document.querySelector('.study-tray');
  r.tray = tray ? getComputedStyle(tray).display : null;
  r.dimBtns = document.querySelectorAll('.dim-b').length;
  var ln = document.querySelector('.learn-native');
  r.nativeOp = ln ? parseFloat(getComputedStyle(ln).opacity) : null;
  r.nativeA = document.documentElement.style.getPropertyValue('--native-a');
  var cards = [].slice.call(document.querySelectorAll('main .card'));
  r.cards = cards.length;
  r.hiddenCards = cards.filter(function (c) { var o = 1; for (var e = c; e && e.nodeType === 1; e = e.parentElement) o *= parseFloat(getComputedStyle(e).opacity); return o < 0.9; }).length;
  r.phrase = document.querySelectorAll('.ja-ph').length;
  var sel = document.querySelector('.re-sel');
  r.selOp = sel ? parseFloat(getComputedStyle(sel).opacity) : null;
  r.selColor = sel ? getComputedStyle(sel).color : null;
  var pre = document.createElement('pre'); pre.id = 'mc'; pre.textContent = JSON.stringify(r); document.body.appendChild(pre);
}, 1500); });
</script>"""


class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass

    def do_GET(self):
        path = self.path.split("?")[0]
        f = ROOT / path.lstrip("/")
        if f.is_dir(): f = f / "index.html"
        if f.suffix == ".html" and f.exists():
            s = f.read_text(encoding="utf-8")
            s = s.replace("<head>", "<head>" + HEAD_JS, 1).replace("</body>", BODY_JS + "</body>", 1)
            b = s.encode()
            self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)
        else:
            super().do_GET()


def browser():
    if os.environ.get("CHROME"): return [os.environ["CHROME"], "--headless=new"]
    cands = []
    cands += sorted(glob.glob(str(pathlib.Path.home() / "Library/Caches/ms-playwright/chromium_headless_shell-*/*/chrome-headless-shell")))
    cands += sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))
    cands += ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser"]
    for c in cands:
        if os.path.exists(c):
            return [c] if "headless_shell" in c else [c, "--headless=new"]
    sys.exit("❌ Chrome が見つかりません（環境変数 CHROME に場所を入れてください）")


def run(url, reduce):
    for _ in range(2):          # 開けなかったら、1回だけやり直す
        res = run_once(url, reduce)
        if res is not None: return res
    return None


def run_once(url, reduce):
    d = tempfile.mkdtemp(prefix="mchk")
    try:
        # 外のサイト（YouTube・地図・フォントなど）には行かせない。待たされて遅くなる・不安定になるのを防ぐ（自分のサーバーだけ見る）
        cmd = browser() + ["--disable-gpu", "--no-sandbox", f"--user-data-dir={d}", "--window-size=390,844",
                           "--host-resolver-rules=MAP * ~NOTFOUND , EXCLUDE 127.0.0.1",
                           "--virtual-time-budget=7000", "--dump-dom"]
        if reduce: cmd.append("--force-prefers-reduced-motion")
        r = subprocess.run(cmd + [url], capture_output=True, text=True, timeout=60)
        m = re.search(r'<pre id="mc">(.*?)</pre>', r.stdout, re.S)
        return json.loads(html.unescape(m.group(1))) if m else None
    except subprocess.TimeoutExpired:
        return None
    finally:
        shutil.rmtree(d, ignore_errors=True)


def judge(r, reduce):
    """問題の一覧（日本語）を返す"""
    bad = []
    if r["errs"]: bad.append("JavaScript のエラー：" + "; ".join(r["errs"][:2]))
    if r["ow"] > 1: bad.append(f"横にはみ出している（{r['ow']}px）")
    if not r["bar"]: bad.append("勉強バーが出ていない")
    else:
        if r["tray"] != "flex": bad.append("勉強をオンにしたのに、2段目（濃さのボタン）が出ていない")
        if r["dimBtns"] != 4: bad.append(f"濃さのボタンが {r['dimBtns']} 個（4個のはず）")
        if r["nativeOp"] is None: bad.append("日本語の文字（.learn-native）がない")
        elif abs(r["nativeOp"] - 0.3) > 0.02: bad.append(f"日本語の濃さを30％にしたのに opacity={r['nativeOp']}（0.3のはず）← 動きを減らす設定などが打ち消している疑い")
    # 普通のときは、スクロールするまで下のカードを隠しておくのが仕様。動きを減らす設定のときだけ、全部見えていなければおかしい
    if reduce and r["cards"] and r["hiddenCards"]: bad.append(f"動きを減らす設定なのに、見えないカードが {r['hiddenCards']} 枚ある")
    if r["selOp"] is not None and r["selOp"] > 0.01 and "0, 0, 0, 0" not in str(r["selColor"]) and "transparent" not in str(r["selColor"]):
        bad.append("言い換えの select（透明にして重ねるもの）が見えてしまっている")
    if r.get("phrase", 0) < 1: bad.append("日本語の見出しの文節折り返し（.ja-ph・BudouX）が効いていない")
    if reduce and r["reduce"] is not True: bad.append("（検査の不具合）動きを減らす設定が効いていない")
    return bad


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--all" in sys.argv:
        slugs = sorted(p.name for p in (ROOT / "works").iterdir() if (p / "index.html").exists())
    else:
        slugs = args or [s for s in SAMPLE if (ROOT / "works" / s / "index.html").exists()]
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(H, directory=str(ROOT)))
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    jobs = [(s, rd) for s in slugs for rd in (False, True)]
    urls = {j: f"http://127.0.0.1:{port}/works/{j[0]}/index.html?lang=ja" for j in jobs}
    problems, failed = {}, []
    with ThreadPoolExecutor(4) as ex:
        for j, res in zip(jobs, ex.map(lambda j: run(urls[j], j[1]), jobs)):
            tag = f"{j[0]} [{'動きを減らす' if j[1] else '普通'}]"
            if res is None: failed.append(tag); continue
            bad = judge(res, j[1])
            if bad: problems[tag] = bad
    srv.shutdown()
    if failed: print("⚠️ 開けなかった:", ", ".join(failed[:12]))
    if not problems and not failed:
        print(f"✅ スマホ幅（390px）× 普通／動きを減らす：{len(slugs)}本とも問題なし"); return
    if problems:
        print(f"❌ スマホで問題があるページ：{len(problems)}件")
        for tag, bad in problems.items():
            print("  ", tag)
            for b in bad: print("      ·", b)
    sys.exit(1)


if __name__ == "__main__":
    main()
