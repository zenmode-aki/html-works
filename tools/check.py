#!/usr/bin/env python3
"""
⚡ 15 Second Blog — 納品チェック

  python3 tools/check.py              全記事をチェック
  python3 tools/check.py pawapuro     1本だけ
  python3 tools/check.py --fix-badge  ワード数バッジを正しい数字に書き直す
  python3 tools/check.py --drafts     公開前の下書き（drafts/）を検査する

チェックすること:
  1. index.html が 400KB 以内か
  2. 画像がすべて base64 か（相対パス・外部URL・絶対パスが残っていないか）
  3. 本文が 35〜55 words に収まっているか（＝15秒）
  4. ワード数バッジの数字が本文と合っているか
  5. SOURCE MAP があり「追加した文：0」になっているか
  6. source.md があるか
  7. カードに英単語2〜3語の見出しラベルが付いているか  ← 15秒版で追加
  8. .quip（AIのボケ）が2個以内か                      ← 15秒版で追加
  9. アニメを使うなら prefers-reduced-motion があるか   ← 15秒版で追加

2026-08 に書いた10本は「1分ブログ」時代のもの。本人の英文なので書き換えない。
LEGACY に入れて、当時のルール（120〜180 words）のまま守る。新しい検査もかけない。
"""
import re, sys, os, html, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
MAX_BYTES = 400 * 1024
MIN_WORDS, MAX_WORDS = 35, 55        # ⚡ 15秒（180wpm で 12〜18秒）
WPM = 180
MAX_QUIP = 2                          # 1記事に入れていいAIのボケの数

# 📖 1分ブログ時代の10本。当時のルールで判定する
LEGACY_MIN, LEGACY_MAX = 120, 180
LEGACY = {
    "pawapuro",
    "knowledge-metabo-1", "knowledge-metabo-2", "knowledge-metabo-3",
    "perfectionist-1", "perfectionist-2", "perfectionist-3",
    "japan-philippines-shops", "japan-philippines-work",
    "stop-overthinking-practice",
}

OK, NG, WARN = "✅", "❌", "⚠️ "


def body_words(doc: str):
    """<p> の中身だけを数える。見出し・UIテキスト・altは数えない。"""
    body = doc.split("<body", 1)[-1]
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    text = " ".join(re.findall(r"<p\b[^>]*>(.*?)</p>", body, flags=re.S | re.I))
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    return [t for t in text.split() if re.search(r"[A-Za-z0-9]", t)]


def count_class(doc: str, cls: str) -> int:
    """class="card" は数え、class="youtube-card" や "card-label" は数えない。"""
    return sum(1 for attr in re.findall(r'class="([^"]*)"', doc) if cls in attr.split())


def check(work: pathlib.Path, fix_badge: bool):
    name = work.name
    idx = work / "index.html"
    problems, notes = [], []

    if not idx.exists():
        return [f"{NG} {name}: index.html がありません"], []

    legacy = name in LEGACY
    lo, hi = (LEGACY_MIN, LEGACY_MAX) if legacy else (MIN_WORDS, MAX_WORDS)
    if legacy:
        notes.append(f"📖 1分ブログ時代の記事（{lo}〜{hi} words で判定・15秒版の検査はかけない）")

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
    if n > hi:
        problems.append(f"{NG} 本文 {n} words（上限 {hi}）→ {n - hi} words 削ってください")
    elif n < lo:
        notes.append(f"{WARN}本文 {n} words（目安の下限 {lo}）— 短いぶんには問題なし")
    else:
        notes.append(f"{OK} 本文 {n} words ≒ {sec}秒")

    # 時計は ⏱（1分時代）でも ⚡（15秒）でもいい。
    # 末尾の "read" まで飲み込ませておかないと --fix-badge が "sec read read" を作る
    icon = "⏱" if legacy else "⚡"
    badge_re = r'class="wc-badge"[^>]*>\s*[⏱⚡]\s*([0-9]+)\s*words\s*·\s*([0-9]+)\s*sec(?:\s*read)?'
    m = re.search(badge_re, doc)
    if not m:
        problems.append(f"{NG} ワード数バッジがありません"
                        f"（<div class=\"wc-badge\">{icon} {n} words · {sec} sec</div>）")
    else:
        shown = int(m.group(1))
        if abs(shown - n) > 3:
            if fix_badge:
                doc = doc[:m.start()] + f'class="wc-badge">{icon} {n} words · {sec} sec' + doc[m.end():]
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

    # 7-9. 15秒版だけの検査（1分時代の10本にはかけない）
    if not legacy:
        # 7. カードの見出しは絵文字だけにしない。英単語2〜3語のラベルを必ず付ける
        n_card = count_class(doc, "card")
        labels = re.findall(r'class="card-label"[^>]*>(.*?)</', doc, flags=re.S)
        if n_card and len(labels) < n_card:
            problems.append(f"{NG} 見出しラベルが足りません: card {n_card}枚 / card-label {len(labels)}個"
                            f"  → 絵文字だけの見出しは禁止。THE PROBLEM のように英単語2〜3語を付けてください")
        else:
            bad = [l.strip() for l in labels if not 2 <= len(l.split()) <= 3]
            if bad:
                problems.append(f"{NG} 見出しラベルは英単語2〜3語にしてください: {bad[:3]}")
            elif labels:
                notes.append(f"{OK} 見出しラベル {len(labels)}個すべて2〜3語")

        # 8. AIのボケは盛りすぎない
        n_quip = count_class(doc, "quip")
        if n_quip > MAX_QUIP:
            problems.append(f"{NG} .quip が {n_quip}個あります（上限 {MAX_QUIP}）→ 盛りすぎです")
        elif n_quip:
            notes.append(f"{OK} .quip {n_quip}個（上限 {MAX_QUIP}）")

        # 9. 動きを付けたなら、動きが苦手な人のための逃げ道を必ず用意する
        if "@keyframes" in doc or "transition:" in doc:
            if "prefers-reduced-motion" not in doc:
                problems.append(f"{NG} prefers-reduced-motion がありません"
                                f"  → アニメを止める @media ブロックを必ず入れてください")
            else:
                notes.append(f"{OK} prefers-reduced-motion あり")

    # 6. source.md
    if not (work / "source.md").exists():
        problems.append(f"{NG} source.md がありません（次にAIへ渡す素材が残りません）")
    else:
        notes.append(f"{OK} source.md あり")

    return problems, notes


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    fix = "--fix-badge" in sys.argv
    # 毎朝AIが作る下書きも、公開物と同じ基準で検査する。
    # drafts/ を works/ にコピーして検査する、のような回り道をしないため
    drafts = "--drafts" in sys.argv

    base = ROOT / ("drafts" if drafts else "works")
    if not base.exists():
        print(f"ℹ️  {base.relative_to(ROOT)}/ がありません")
        return 0
    works = sorted(p for p in base.iterdir() if p.is_dir())
    if args:
        works = [w for w in works if w.name in args]
        if not works:
            where = "下書き" if drafts else "記事"
            print(f"{NG} そんな{where}はありません: {args}")
            return 1
    if not works:
        print(f"ℹ️  {base.relative_to(ROOT)}/ は空です")
        return 0

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
