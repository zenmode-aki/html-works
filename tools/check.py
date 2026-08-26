#!/usr/bin/env python3
"""
🐧 1 Minute Blog — 納品チェック

  python3 tools/check.py              全記事をチェック
  python3 tools/check.py pawapuro     1本だけ
  python3 tools/check.py --fix-badge  ワード数バッジを正しい数字に書き直す

チェックすること:
  1. index.html が 400KB 以内か
  2. 画像がすべて base64 か（相対パス・外部URL・絶対パスが残っていないか）
  3. 本文が 120〜180 words に収まっているか
  4. ワード数バッジの数字が本文と合っているか
  5. SOURCE MAP があり「追加した文：0」になっているか
  6. source.md があるか
"""
import re, sys, os, html, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
MAX_BYTES = 400 * 1024
MIN_WORDS, MAX_WORDS = 120, 180
WPM = 180

OK, NG, WARN = "✅", "❌", "⚠️ "


def body_words(doc: str):
    """<p> の中身だけを数える。見出し・UIテキスト・altは数えない。"""
    body = doc.split("<body", 1)[-1]
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    text = " ".join(re.findall(r"<p\b[^>]*>(.*?)</p>", body, flags=re.S | re.I))
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    return [t for t in text.split() if re.search(r"[A-Za-z0-9]", t)]


def check(work: pathlib.Path, fix_badge: bool):
    name = work.name
    idx = work / "index.html"
    problems, notes = [], []

    if not idx.exists():
        return [f"{NG} {name}: index.html がありません"], []

    doc = idx.read_text(encoding="utf-8")
    size = len(doc.encode())

    # 1. サイズ
    if size > MAX_BYTES:
        problems.append(f"{NG} 大きすぎます: {size/1024:.0f}KB（上限 400KB）→ 画像をさらに縮小してください")
    else:
        notes.append(f"{OK} サイズ {size/1024:.0f}KB / 400KB")

    # 2. 画像の参照
    bad_src = [s for s in re.findall(r'<img[^>]*\bsrc="([^"]*)"', doc) if not s.startswith("data:")]
    if bad_src:
        problems.append(f"{NG} base64になっていない画像があります: {bad_src}")
    abs_paths = re.findall(r"(/Users/[^\s\"'<>)]+|/mnt/data/[^\s\"'<>)]+)", doc)
    if abs_paths:
        problems.append(f"{NG} 絶対パスが残っています: {sorted(set(abs_paths))[:3]}")
    n_img = doc.count("data:image/")
    if not bad_src and not abs_paths:
        notes.append(f"{OK} 画像 {n_img}枚すべて自己完結（リンク切れの余地なし）")

    # 外部URL（YouTubeサムネだけは許可。下地のグラデーションで崩れないため）
    ext = [u for u in re.findall(r'url\(["\']?(https?://[^)"\']+)', doc)
           if "img.youtube.com" not in u]
    if ext:
        problems.append(f"{NG} 外部画像URLがあります（オフラインで消えます）: {ext}")

    # 3-4. ワード数とバッジ
    words = body_words(doc)
    n = len(words)
    sec = round(n / (WPM / 60))
    if n > MAX_WORDS:
        problems.append(f"{NG} 本文 {n} words（上限 {MAX_WORDS}）→ {n - MAX_WORDS} words 削ってください")
    elif n < MIN_WORDS:
        notes.append(f"{WARN}本文 {n} words（目安の下限 {MIN_WORDS}）— 短いぶんには問題なし")
    else:
        notes.append(f"{OK} 本文 {n} words ≒ {sec}秒")

    m = re.search(r'class="wc-badge"[^>]*>\s*⏱\s*([0-9]+)\s*words\s*·\s*([0-9]+)\s*sec', doc)
    if not m:
        problems.append(f"{NG} ワード数バッジがありません（<div class=\"wc-badge\">⏱ {n} words · {sec} sec read</div>）")
    else:
        shown = int(m.group(1))
        if abs(shown - n) > 3:
            if fix_badge:
                doc = doc[:m.start()] + f'class="wc-badge">⏱ {n} words · {sec} sec read' + doc[m.end():]
                idx.write_text(doc, encoding="utf-8")
                notes.append(f"{OK} バッジを直しました: {shown} → {n} words · {sec} sec")
            else:
                problems.append(f"{NG} バッジの数字が違います: 表示 {shown} words / 実際 {n} words"
                                f"  → python3 tools/check.py --fix-badge で直せます")
        else:
            notes.append(f"{OK} バッジの数字が本文と一致")

    # 5. SOURCE MAP
    if "SOURCE MAP" not in doc:
        problems.append(f"{NG} SOURCE MAP がありません（AIが足していないことを確認できません）")
    else:
        m2 = re.search(r"追加した文\s*[:：]\s*(\S+)", doc)
        if not m2:
            problems.append(f"{NG} SOURCE MAP に「追加した文：0」の行がありません")
        elif m2.group(1).strip() not in ("0", "０", "なし"):
            problems.append(f"{NG} 追加した文が {m2.group(1)} 件あります → AIが書いた文が混ざっています")
        else:
            cut = re.search(r"削った文\s*[:：]\s*(.+)", doc)
            notes.append(f"{OK} 追加した文：0" + (f"（削った文: {cut.group(1).strip()[:40]}）" if cut else ""))

    # 6. source.md
    if not (work / "source.md").exists():
        problems.append(f"{NG} source.md がありません（次にAIへ渡す素材が残りません）")
    else:
        notes.append(f"{OK} source.md あり")

    return problems, notes


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    fix = "--fix-badge" in sys.argv
    works = sorted(p for p in (ROOT / "works").iterdir() if p.is_dir())
    if args:
        works = [w for w in works if w.name in args]
        if not works:
            print(f"{NG} そんな記事はありません: {args}")
            return 1

    total_ng = 0
    for w in works:
        problems, notes = check(w, fix)
        head = f"🐧 {w.name}"
        print(f"\n{head}\n{'─' * (len(head) + 2)}")
        for line in notes:
            print("  " + line)
        for line in problems:
            print("  " + line)
        total_ng += len(problems)

    print()
    if total_ng == 0:
        print(f"{OK} 全部OK。push して大丈夫です。")
        return 0
    print(f"{NG} 直すところが {total_ng} 件あります。")
    return 1


if __name__ == "__main__":
    sys.exit(main())
