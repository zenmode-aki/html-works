#!/usr/bin/env python3
"""
🗓 週に1回の「まとめて翻訳」の対象を出す（2026-09-29 本人が決めた）

  python3 tools/i18n-due.py            訳してよい記事と、足りない言語を出す
  python3 tools/i18n-due.py --slugs    記事の slug だけを1行ずつ（ほかの道具に渡す用）

決まりごと
- 本番に出すときは **英・日・韓・中（簡体・繁體）の5つだけ** 訳す（Claude）
- 本番に出して **3日たち、そのあと3日間どこも直していない記事** は「落ち着いた」とみなす
- 落ち着いた記事のうち、ほかの言語の訳がまだのものを、**週に1回まとめて**訳す（Codex など安いAI）
  → 途中で本文を直すたびに35言語を訳し直す、というムダをなくすため

「直した日」は、本人の言葉が入っているファイル（source.md・meta.json・images/）と、
英語の本文（index.html の <main> の中の文）が最後に変わったコミットの日付で見る。
index.html はまわりの道具（次の記事・こちらもどうぞ など）が毎回書き換えるので、ファイルの日付では見ない。
"""
import datetime, importlib.util, json, pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
WORKS = ROOT / "works"
MAIN = {"ja", "ko", "zh", "zh-Hant"}
DAYS = 3

_spec = importlib.util.spec_from_file_location("i18n", ROOT / "tools" / "i18n.py")
i18n = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(i18n)


def git_dates(*paths):
    out = subprocess.run(["git", "log", "--format=%cI", "--", *paths], cwd=ROOT, capture_output=True, text=True).stdout.split()
    # Mac の Python 3.9 は末尾の「Z」を読めない（2026-10-03 ここで止まっていた）→ +00:00 に置きかえる
    return [datetime.datetime.fromisoformat(x.replace("Z", "+00:00")) for x in out]


def main():
    now = datetime.datetime.now(datetime.timezone.utc)
    langs = [l for l in i18n.langs_available() if l not in MAIN]
    _, _, _, report, _, _ = i18n.build_all()
    missing = {}
    for slug, l, miss in report:
        if l in langs and slug != "(トップページ)":
            missing.setdefault(slug, set()).add(l)
    due, waiting = [], []
    for d in sorted(p.parent for p in WORKS.glob("*/index.html")):
        s = d.name
        if s not in missing:
            continue
        ds = git_dates(f"works/{s}/source.md", f"works/{s}/meta.json", f"works/{s}/images")
        if not ds:
            continue
        first, last = min(ds), max(ds)
        if (now - first).days >= DAYS and (now - last).days >= DAYS:
            due.append((s, sorted(missing[s]), last.date()))
        else:
            waiting.append((s, (DAYS - (now - last).days)))
    if "--slugs" in sys.argv:
        print("\n".join(s for s, _, _ in due)); return 0
    print(f"🗓 まとめて翻訳してよい記事：{len(due)}本（本番に出して{DAYS}日、そのあと{DAYS}日直していない・英日韓中以外の訳が足りない）")
    for s, ls, last in due:
        print(f"   {s:<44} 最後に直した日 {last}  足りない言語 {len(ls)}：{' '.join(ls[:8])}{' …' if len(ls) > 8 else ''}")
    if waiting:
        print(f"⏳ まだ待つ記事：{len(waiting)}本（直したばかり）: " + ", ".join(f"{s}（あと{max(1, n)}日）" for s, n in waiting[:12]))
    print("\n→ Codex への頼み方：「python3 tools/i18n-due.py に出た記事だけ、works/<slug>/i18n/<lang>.json を足して、"
          "python3 tools/i18n.py → python3 tools/i18n-audit.py --all-langs で確かめてから push して」")
    return 0


if __name__ == "__main__":
    sys.exit(main())
