#!/usr/bin/env python3
"""
🔢 記事の公開順（meta.json の "seq"）を、gitの履歴からいちど計算しなおす道具

  python3 tools/renumber-seq.py            決めた番号を表示するだけ（書き換えない）
  python3 tools/renumber-seq.py --write    実際に全記事の meta.json に書き込む

## これは何のためにあるか

トップページの記事一覧は「公開した順」に並ぶのが自然だが、
同じ日に何本も記事を出す日があるので、meta.json の "date"（日付だけ）では
同じ日の中の順番が決まらない。そこで git の履歴から「そのフォルダが
最初にリポジトリに追加されたのはどのコミットか」を数えて、
古い方から 1, 2, 3... という通し番号を振る。これが "seq"。

⚠️ CIは浅いclone（直近のコミットしか持っていない）なので、
   ビルド時（tools/build-site.py）に毎回 git log を読みに行く作り方はできない。
   なので、この道具で一度だけ計算して、結果を meta.json に**焼き込む**。
   以後は新しい記事を作るたびに、そのときの最大値+1 を書けばいいだけになる。

## 同じコミットに複数の記事が一気に追加されたとき

gitはコミットの中の順番（誰が先に書いたか）を教えてくれないので、
git show が返すパス順（だいたいアルファベット順）で決まる。
本当の生成順が分かっているバッチだけ、下の KNOWN_BATCH_ORDER に書けば、
そちらを優先する。

## 新しい記事を1本足すとき

このスクリプトを再実行する必要はない。
既存の最大 seq を確認して +1 するだけでいい：

    python3 -c "
import json, pathlib
m = max(json.loads((p/'meta.json').read_text())['seq']
        for p in pathlib.Path('works').iterdir() if (p/'meta.json').exists())
print('次の記事の seq は', m + 1)
"
"""
import json, pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# 本当の生成順が分かっているバッチ（このリストの中だけ、アルファベット順より優先する）
KNOWN_BATCH_ORDER = [
 ["why-not-japan", "ai-can-translate", "cant-explain", "en-to-jp-harder",
  "skill-over-language", "engineers-30-min",
  "translate-back", "not-i-can-do-it", "get-a-stamp", "trust-the-buffer",
  "only-japanese-person", "that-email", "after-the-meeting", "minutes-in-one-minute",
  "no-public-scolding", "walking-on-the-7th-floor", "concierge-downstairs",
  "my-room-on-video", "120-eggs"],
 ["chiikawa-before-you-visit", "grandmothers-house-in-gifu", "splatoon-favorite-weapon",
  "cebu-condo-poolside", "freezing-not-fleeing", "mario-kart-any-age",
  "gifu-drive-service-areas", "chawanmushi-first-time", "kanayama-station-ceiling",
  "rain-sound-feature"],
]


def compute():
    current = {p.name for p in (ROOT / "works").iterdir() if p.is_dir()}
    commits = subprocess.run(["git", "log", "--reverse", "--pretty=%H"],
                              cwd=ROOT, capture_output=True, text=True).stdout.split()

    seq, counter = {}, 0
    for c in commits:
        out = subprocess.run(
            ["git", "show", "--diff-filter=AR", "--name-status", "-M", "--pretty=format:", c],
            cwd=ROOT, capture_output=True, text=True).stdout.splitlines()
        for line in out:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            dest = parts[-1]  # "A path" → [path] / "R100 old new" → [old, new]
            if dest.startswith("works/") and dest.endswith("/meta.json"):
                slug = dest.split("/")[1]
                if slug in current and slug not in seq:
                    counter += 1
                    seq[slug] = counter

    missing = current - set(seq)
    if missing:
        print(f"⚠️ gitの履歴から見つからなかった記事: {sorted(missing)}", file=sys.stderr)

    for batch in KNOWN_BATCH_ORDER:
        nums = sorted(seq[s] for s in batch if s in seq)
        if len(nums) != len(batch):
            continue
        for s, n in zip(batch, nums):
            seq[s] = n

    return seq


def main():
    write = "--write" in sys.argv
    seq = compute()
    if not write:
        for slug, n in sorted(seq.items(), key=lambda kv: kv[1]):
            print(n, slug)
        print(f"\n{len(seq)}本ぶん計算しました。書き込むには --write を付けてください。")
        return 0

    for slug, n in seq.items():
        p = ROOT / "works" / slug / "meta.json"
        m = json.loads(p.read_text(encoding="utf-8"))
        m["seq"] = n
        p.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"✅ {len(seq)}本の meta.json に seq を書き込みました。")
    print("   python3 tools/build-site.py で一覧に反映してください。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
