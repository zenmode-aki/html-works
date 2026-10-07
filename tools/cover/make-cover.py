#!/usr/bin/env python3
"""
🐧💭 表紙を作る（2026-10-07〜 新しい表紙のデザイン）

本人：「今の表紙のペンギンがあまり好きじゃない」（2026-10-06）
→ 本家ペンゲッソ（紺色・青い帽子・サングラスのぬいぐるみ。assets/pengesso/pengesso-01.jpg を切り抜いたもの）が、
  記事のテーマを「考えごとの吹き出し」に浮かべている絵にした。吹き出しの中は立体の絵文字1つ（Microsoft Fluent Emoji 3D・MIT）。
  背景は記事の色をうすくしたグラデーション。文字は入れない。画像生成AIは使わない（毎回同じキャラ・同じ品質になる）

  python3 tools/cover/make-cover.py <slug> 🎁 '#e0457b'          # 下書きに表紙を付ける（右にペンギン＝ --flip）
  python3 tools/cover/make-cover.py <slug> 🎁 '#e0457b' --flip
  python3 tools/cover/make-cover.py --picks                       # tools/cover/picks.json の全部（作り直し）
  python3 tools/cover/make-cover.py <slug> 🎁 '#e0457b' --only    # 画像だけ作る（記事には入れない。見比べ用）→ tools/cover/out/

絵文字の決まり：人・顔のある人・手（🏃🙋👍 など）・恋愛・こわいもの・小さな穴や粒のかたまり（本人が苦手）を使わない。
吹き出しが白いので、白っぽい絵文字（💭 など）は見えない。黄色い顔（😊😋）は OK。
記事に入れる流れ：images/cover.jpg → tools/embed.py --draft → assets/thumbs-src → tools/thumbs.py（macOS の sips。Linux では使えない）
必要なもの：Python の Pillow、Node の playwright（Chromium）。絵文字の画像は初回だけ GitHub から取ってくる（tools/cover/emo/ は git に入れない）
"""
import json, os, pathlib, shutil, subprocess, sys, tempfile, urllib.parse

D = pathlib.Path(__file__).resolve().parent
ROOT = D.parent.parent


def hx(c):
    c = c.lstrip('#'); return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def mix(a, b, t):
    return '#%02x%02x%02x' % tuple(round(a[i] * (1 - t) + b[i] * t) for i in range(3))


def code(g):
    return '-'.join('%x' % ord(c) for c in g.replace('️', ''))


def emoji_png(g):
    m = json.loads((D / 'emoji3d.json').read_text())
    norm = {k.replace('️', ''): v for k, v in m.items()}
    path = m.get(g) or norm.get(g.replace('️', ''))
    if not path: sys.exit(f'❌ {g} は Fluent Emoji 3D にない（tools/cover/emoji3d.json）')
    out = D / 'emo' / f'{code(g)}.png'
    if not out.exists():
        out.parent.mkdir(exist_ok=True)
        url = 'https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/' + urllib.parse.quote(path)
        subprocess.run(['curl', '-sSf', '-o', str(out), url], check=True)
    return out


def page(emo, acc, flip):
    a = hx(acc); W = (255, 255, 255)
    p1, p2, p3 = mix(a, W, .86), mix(a, W, .66), mix(a, W, .45)
    px, bx = (630, 150) if flip else (150, 560)          # ペンギンの x、吹き出しの x
    tr = 'scaleX(-1)' if flip else ''
    t1x, t2x = (bx + 400, bx + 450) if flip else (bx + 40, bx - 10)
    cloud = ''.join(f'<div style="position:absolute;left:{bx + dx}px;top:{60 + dy}px;width:{d}px;height:{d}px;border-radius:50%;background:#fff"></div>'
                    for dx, dy, d in [(60, 40, 360), (0, 140, 240), (240, 120, 250), (150, 0, 220), (120, 180, 280)])
    return f"""<!doctype html><meta charset=utf-8><style>html,body{{margin:0;width:1200px;height:900px;overflow:hidden}}body{{position:relative}}img{{position:absolute;display:block}}</style><body>
<div style="position:absolute;inset:0;background:radial-gradient(ellipse 90% 80% at {'30' if flip else '70'}% 25%,{p1},{p2} 75%,{p3})"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:150px;background:linear-gradient(transparent,{mix(a, W, .5)});opacity:.7"></div>
<div style="position:absolute;left:{px + 10}px;top:800px;width:440px;height:56px;border-radius:50%;background:rgba(0,0,0,.24);filter:blur(16px)"></div>
<img src="{(D / 'pengesso.png').as_uri()}" style="left:{px}px;top:225px;height:600px;transform:{tr}">
<div style="position:absolute;inset:0;filter:drop-shadow(0 16px 30px rgba(0,0,0,.13))">{cloud}
<div style="position:absolute;left:{t1x}px;top:470px;width:64px;height:64px;border-radius:50%;background:#fff"></div>
<div style="position:absolute;left:{t2x}px;top:560px;width:36px;height:36px;border-radius:50%;background:#fff"></div></div>
<img src="{emoji_png(emo).as_uri()}" style="left:{bx + 110}px;top:110px;width:270px;filter:drop-shadow(0 8px 10px rgba(0,0,0,.15));transform:rotate(-4deg)">
</body>"""


RENDER_JS = """
let pw; try { pw = require('playwright'); } catch (e) { pw = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright'); }
const jobs = JSON.parse(require('fs').readFileSync(process.argv[2]));
(async () => {
  const b = await pw.chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 900 } });
  for (const j of jobs) { await p.goto('file://' + j.html); await p.waitForTimeout(150); await p.screenshot({ path: j.out, type: 'jpeg', quality: 90 }); }
  await b.close();
})();
"""


def render(items):
    """items: [(slug, emo, acc, flip, out_path)]"""
    tmp = pathlib.Path(tempfile.mkdtemp())
    jobs = []
    for slug, emo, acc, flip, out in items:
        h = tmp / f'{slug}.html'; h.write_text(page(emo, acc, flip))
        jobs.append({'html': str(h), 'out': str(out)})
    (tmp / 'jobs.json').write_text(json.dumps(jobs)); (tmp / 'r.js').write_text(RENDER_JS)
    subprocess.run(['node', str(tmp / 'r.js'), str(tmp / 'jobs.json')], check=True)
    shutil.rmtree(tmp, ignore_errors=True)


def apply(slug):
    d = ROOT / 'draft' / slug
    subprocess.run([sys.executable, str(ROOT / 'tools/embed.py'), '--draft', slug], check=True, capture_output=True)
    shutil.copy(d / 'images/cover.jpg', ROOT / 'assets/thumbs-src' / f'{slug}.jpg')
    r = subprocess.run([sys.executable, str(ROOT / 'tools/thumbs.py'), slug], capture_output=True)
    print(('✓ ' if r.returncode == 0 else '⚠️ サムネは作れなかった（sips がない？）') + slug)


def main():
    a = [x for x in sys.argv[1:] if not x.startswith('--')]
    only, flip = '--only' in sys.argv, '--flip' in sys.argv
    if '--picks' in sys.argv:
        picks = json.loads((D / 'picks.json').read_text())
        items = [(s, v['emo'], v['acc'], bool(v.get('flip')), s) for s, v in picks.items()]
    elif len(a) == 3:
        items = [(a[0], a[1], a[2], flip, a[0])]
    else:
        print(__doc__); return
    out = []
    for slug, emo, acc, fl, _ in items:
        if only:
            (D / 'out').mkdir(exist_ok=True); p = D / 'out' / f'{slug}.jpg'
        else:
            (ROOT / 'draft' / slug / 'images').mkdir(parents=True, exist_ok=True); p = ROOT / 'draft' / slug / 'images/cover.jpg'
        out.append((slug, emo, acc, fl, p))
    render(out)
    if only: print('→', D / 'out'); return
    picks = json.loads((D / 'picks.json').read_text()) if (D / 'picks.json').exists() else {}
    for slug, emo, acc, fl, _ in out:
        picks[slug] = {'emo': emo, 'acc': acc, 'flip': fl}
        apply(slug)
    (D / 'picks.json').write_text(json.dumps(picks, ensure_ascii=False, indent=0))


if __name__ == '__main__':
    main()
