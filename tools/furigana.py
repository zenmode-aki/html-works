#!/usr/bin/env python3
"""
📖 日本語のふりがな・ローマ字を作る
   （英語のページで、日本語を勉強したい人のため。2026-10-04 本人の要望：
     「日本語の記事で英語が出せるように、英語の記事でも日本語学習ができるように」）

  python3 tools/furigana.py             全記事の works/<slug>/i18n/read.ja.json を作る（変わった記事だけ）
  python3 tools/furigana.py --force     ぜんぶ作り直す
  python3 tools/furigana.py --check     作り直しが要るか確かめる（道具いらず。check.py --site から呼ぶ）
  python3 tools/furigana.py --test      数字＋助数詞の読みの単体テスト
  python3 tools/furigana.py --sample 30 ランダムに30文を出す（目で確かめる）
  python3 tools/furigana.py --pairs 400 （漢字, よみ）の一覧を、よく出る順に出す（まちがいさがし用）

元になるもの：works/<slug>/i18n/data.ja.json（画面に出る日本語。python3 tools/i18n.py が作る）。
  → 先に i18n.py、そのあとにこれ。
読みの辞書：fugashi + unidic-lite（MeCab の UniDic）。ローマ字（ヘボン式）はこのファイルの kana_to_romaji() と romaji()。入れかた：
  pip install fugashi unidic-lite
自動で作るので、まちがいがありえる（画面にも「自動で作っています」と出す）。
・直したい読みは tools/furigana-overrides.json に { "表記": "よみ" } で足す（例：私 → わたし。UniDic は「わたくし」と読む）
・数字のあとの助数詞（9月・14日・45分・3階 …）は UniDic が読めないので、このファイルの counter_reading() で決める。
  表にないものは、まちがえるより、ふりがなを付けない

出力 read.ja.json：
  {"h": "<元の日本語と上書きのハッシュ>",
   "r": {"<指紋>": "跳{は}ねて、14日{じゅうよっか}"},   ← 漢字や数字のあとの {よみ} がふりがな。漢字がない文は入れない
   "m": {"<指紋>": "Haneru…"}}                         ← ローマ字（ヘボン式・単語ごとに空白）
・前のかなや漢字と混ざらないよう、ふりがなの前に ｜ を入れることがある（｜は画面に出さない）
指紋は data.ja.json のキーと同じ（画面の英文から作る FNV）。
"""
import hashlib
import json
import pathlib
import random
import re
import sys
from collections import Counter, namedtuple

ROOT = pathlib.Path(__file__).resolve().parent.parent
WORKS = ROOT / "works"
OVERRIDES = ROOT / "tools" / "furigana-overrides.json"
VERSION = "2"

KANJI_CH = "㐀-䶿一-鿿々〆ヶ"
KANJI = re.compile(f"[{KANJI_CH}]")
BASE_CH = KANJI_CH + "0-9０-９,，"           # ふりがなの「もと」になる文字（画面側の正規表現と同じ）
KANJI_RUN = re.compile(f"([{KANJI_CH}]+)")
BAR = "｜"


def kata2hira(s):
    return "".join(chr(ord(ch) - 0x60) if 0x30A1 <= ord(ch) <= 0x30F6 else ch for ch in s)


def load_overrides():
    if not OVERRIDES.exists():
        return {}
    d = json.loads(OVERRIDES.read_text(encoding="utf-8"))
    return {k: v for k, v in d.items() if not k.startswith("_")}


# ── 送りがなを外して、漢字のところだけにふりがなを付ける ───────────────────────
def align(surface, reading):
    """跳ね + はね → 跳{は}ね"""
    runs = KANJI_RUN.split(surface)              # ['', '跳', 'ね'] のように、漢字の塊とかなの塊が交互に出る
    if len(runs) == 1:
        return surface
    pat = ""
    for i, r in enumerate(runs):
        if not r:
            continue
        pat += "(.+?)" if i % 2 == 1 else re.escape(kata2hira(r))
    m = re.fullmatch(pat, reading)
    if not m:
        return f"{surface}{{{reading}}}"
    out, g = [], 0
    for i, r in enumerate(runs):
        if not r:
            continue
        if i % 2 == 1:
            g += 1
            out.append(f"{r}{{{m.group(g)}}}")
        else:
            out.append(r)
    return "".join(out)


# ── 数字＋助数詞（9月・14日・45分・3階 …）の読み ──────────────────────────────
# UniDic は数字を読めず、助数詞も数に合わせた音の変化（さんがい・じゅうよっか・しがつ …）が付けられない。
ONES = ["", "いち", "に", "さん", "よん", "ご", "ろく", "なな", "はち", "きゅう"]
STOP = {1: "いっ", 6: "ろっ", 8: "はっ"}          # 「っ」が入る数


def _under10000(n):
    out = ""
    th, r = divmod(n, 1000)
    if th:
        out += {1: "せん", 3: "さんぜん", 8: "はっせん"}.get(th, ONES[th] + "せん")
    h, r = divmod(r, 100)
    if h:
        out += {1: "ひゃく", 3: "さんびゃく", 6: "ろっぴゃく", 8: "はっぴゃく"}.get(h, ONES[h] + "ひゃく")
    tn, o = divmod(r, 10)
    if tn:
        out += "じゅう" if tn == 1 else ONES[tn] + "じゅう"
    if o:
        out += ONES[o]
    return out


def num_kana(n):
    if n == 0:
        return "ぜろ"
    m, r = divmod(n, 10000)
    return (_under10000(m) + "まん" if m else "") + _under10000(r)


def _swap_last(n, table):
    """数の読みの最後の桁だけ差し替える（4→よ、7→しち、9→く）。数が 4・14・24… のとき"""
    s = num_kana(n)
    d = n % 10
    if d in table and s.endswith(ONES[d]):
        return s[: len(s) - len(ONES[d])] + table[d]
    return s


def _stops(n, ones=(1, 6, 8)):
    d = n % 10
    return d in ones or (d == 0 and n >= 10)


def _stop_form(n, tail):
    """か行・さ行・た行・ぱ行などで始まる助数詞：1・6・8 と、10 の倍数のあとに「っ」が入る（tail は「っ」のあとの形）"""
    s = num_kana(n)
    d = n % 10
    if d == 0 and n >= 10 and s.endswith("じゅう"):
        return s[: -len("じゅう")] + "じゅっ" + tail
    if d in STOP and s.endswith(ONES[d]):
        return s[: len(s) - len(ONES[d])] + STOP[d] + tail
    return s + tail


def _fun(n):
    d = n % 10
    if _stops(n):
        return _stop_form(n, "ぷん")
    if d in (3, 4):
        return num_kana(n) + "ぷん"
    return num_kana(n) + "ふん"


def _hon(n, h, p, b):
    if n % 10 == 3:
        return num_kana(n) + b
    if _stops(n):
        return _stop_form(n, p)
    return num_kana(n) + h


DATE = {2: "ふつか", 3: "みっか", 4: "よっか", 5: "いつか", 6: "むいか", 7: "なのか", 8: "ようか", 9: "ここのか",
        10: "とおか", 14: "じゅうよっか", 20: "はつか", 24: "にじゅうよっか",
        17: "じゅうしちにち", 19: "じゅうくにち", 27: "にじゅうしちにち", 29: "にじゅうくにち"}


def _day(n, as_date):
    if n == 1:
        return "ついたち" if as_date else "いちにち"
    return DATE.get(n) or num_kana(n) + "にち"


def counter_reading(n, c, as_date=False):
    """数 n（整数）と助数詞 c から、読み（ひらがな）を返す。分からなければ None"""
    if n < 0 or n >= 100000000:
        return None
    if c == "月":
        return ({4: "し", 7: "しち", 9: "く"}.get(n) or num_kana(n)) + "がつ" if 1 <= n <= 12 else None
    if c == "日":
        return _day(n, as_date) if n <= 31 else num_kana(n) + "にち"
    if c in ("日目", "日間"):
        if n > 31:
            return None
        return _day(n, False) + ("め" if c == "日目" else "かん")
    if c in ("時", "時半", "時間"):
        return _swap_last(n, {4: "よ", 7: "しち", 9: "く"}) + {"時": "じ", "時半": "じはん", "時間": "じかん"}[c]
    if c in ("年", "年前", "年代"):
        return _swap_last(n, {4: "よ", 7: "しち", 9: "く"}) + {"年": "ねん", "年前": "ねんまえ", "年代": "ねんだい"}[c]
    if c == "円":
        return _swap_last(n, {4: "よ"}) + "えん"
    if c == "万円":
        return num_kana(n) + "まんえん"
    if c == "万":
        return num_kana(n) + "まん"
    if c == "分":
        return _fun(n)
    if c == "分間":
        return _fun(n) + "かん"
    if c == "秒":
        return num_kana(n) + "びょう"
    if c == "本":
        return _hon(n, "ほん", "ぽん", "ぼん")
    if c == "泊":
        return _hon(n, "はく", "ぱく", "ぱく")           # 3泊 さんぱく
    if c in ("回", "個", "曲", "店"):
        tail = {"回": "かい", "個": "こ", "曲": "きょく", "店": "てん"}[c]
        return _stop_form(n, tail) if _stops(n) else num_kana(n) + tail
    if c == "階":
        if n % 10 == 3:
            return num_kana(n) + "がい"
        return _stop_form(n, "かい") if _stops(n) else num_kana(n) + "かい"
    if c == "週間":
        return _stop_form(n, "しゅうかん") if _stops(n, (1, 8)) else num_kana(n) + "しゅうかん"
    if c in ("か月", "ヶ月", "カ月", "ケ月"):
        return _stop_form(n, "かげつ") if _stops(n) else num_kana(n) + "かげつ"
    if c in ("歳", "才"):
        if n == 20:
            return "はたち"
        return _stop_form(n, "さい") if _stops(n, (1, 8)) else num_kana(n) + "さい"
    if c == "人":
        if n == 1:
            return "ひとり"
        if n == 2:
            return "ふたり"
        return _swap_last(n, {4: "よ"}) + "にん"
    simple = {"位": "い", "倍": "ばい", "割": "わり", "条": "じょう", "代": "だい", "秒": "びょう"}
    if c in simple:
        return num_kana(n) + simple[c]
    return None


# 長いものから先に当てる（「日目」を「日」より先に）
COUNTERS = sorted(["月", "日", "日目", "日間", "時", "時半", "時間", "年", "年前", "年代", "円", "万円", "万", "分", "分間", "秒", "本", "泊",
                   "回", "個", "曲", "階", "週間", "か月", "ヶ月", "カ月", "ケ月", "歳", "才", "人", "位", "倍", "割", "条", "店", "代"],
                  key=lambda x: -len(x))
NUM_RE = re.compile(r"([0-9０-９]+(?:[,，][0-9０-９]{3})*)")
ZEN = str.maketrans("０１２３４５６７８９，", "0123456789,")

TESTS = [  # (数, 助数詞, 月のあとか, 正しい読み)
    (9, "月", False, "くがつ"), (4, "月", False, "しがつ"), (7, "月", False, "しちがつ"), (12, "月", False, "じゅうにがつ"),
    (1, "日", True, "ついたち"), (1, "日", False, "いちにち"), (12, "日", True, "じゅうににち"), (14, "日", True, "じゅうよっか"),
    (20, "日", True, "はつか"), (24, "日", True, "にじゅうよっか"), (3, "日間", False, "みっかかん"), (2, "日目", False, "ふつかめ"),
    (15, "分", False, "じゅうごふん"), (45, "分間", False, "よんじゅうごふんかん"), (5, "分", False, "ごふん"), (1, "分", False, "いっぷん"),
    (3, "分", False, "さんぷん"), (6, "分", False, "ろっぷん"), (8, "分", False, "はっぷん"), (10, "分", False, "じゅっぷん"),
    (30, "分", False, "さんじゅっぷん"), (4, "分", False, "よんぷん"),
    (3, "階", False, "さんがい"), (6, "階", False, "ろっかい"), (7, "階", False, "ななかい"), (8, "階", False, "はっかい"),
    (1, "階", False, "いっかい"), (10, "階", False, "じゅっかい"), (13, "階", False, "じゅうさんがい"),
    (1, "本", False, "いっぽん"), (3, "本", False, "さんぼん"), (4, "本", False, "よんほん"), (6, "本", False, "ろっぽん"), (10, "本", False, "じゅっぽん"),
    (2, "人", False, "ふたり"), (1, "人", False, "ひとり"), (3, "人", False, "さんにん"), (4, "人", False, "よにん"),
    (4, "時", False, "よじ"), (7, "時", False, "しちじ"), (9, "時", False, "くじ"), (6, "時", False, "ろくじ"), (1, "時間", False, "いちじかん"),
    (2000, "年代", False, "にせんねんだい"), (2026, "年", False, "にせんにじゅうろくねん"), (4, "年", False, "よねん"),
    (30, "代", False, "さんじゅうだい"), (500, "円", False, "ごひゃくえん"), (300, "円", False, "さんびゃくえん"), (4, "円", False, "よえん"),
    (1000, "円", False, "せんえん"), (5, "万円", False, "ごまんえん"), (4000, "円", False, "よんせんえん"),
    (20, "歳", False, "はたち"), (1, "歳", False, "いっさい"), (5, "歳", False, "ごさい"),
    (1, "か月", False, "いっかげつ"), (6, "か月", False, "ろっかげつ"), (3, "か月", False, "さんかげつ"),
    (1, "回", False, "いっかい"), (3, "回", False, "さんかい"), (10, "回", False, "じゅっかい"),
    (2, "位", False, "にい"), (3, "週間", False, "さんしゅうかん"), (1, "週間", False, "いっしゅうかん"),
    (10, "曲", False, "じゅっきょく"), (8, "秒", False, "はちびょう"), (2, "泊", False, "にはく"), (3, "泊", False, "さんぱく"),
]


def self_test():
    bad = 0
    for n, c, d, want in TESTS:
        got = counter_reading(n, c, d)
        if got != want:
            bad += 1
            print(f"❌ {n}{c}（月のあと={d}）：{got} ≠ {want}")
    print(f"{'❌' if bad else '✅'} 数字＋助数詞の読み：{len(TESTS) - bad}/{len(TESTS)} 合っている")
    return 1 if bad else 0


Chunk = namedtuple("Chunk", "surface reading on pos1 pos2")      # on = ふりがなを付けるか


# ── かな → ローマ字（ヘボン式。長音は母音を重ねる：きょう → kyou、ゆうえん → yuuen）──────────────
_ROM = {}
for _k, _v in {
    "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o", "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
    "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so", "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",
    "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no", "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",
    "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo", "や": "ya", "ゆ": "yu", "よ": "yo",
    "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro", "わ": "wa", "ゐ": "i", "ゑ": "e", "を": "o", "ん": "n",
    "が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go", "ざ": "za", "じ": "ji", "ず": "zu", "ぜ": "ze", "ぞ": "zo",
    "だ": "da", "ぢ": "ji", "づ": "zu", "で": "de", "ど": "do", "ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo",
    "ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぺ": "pe", "ぽ": "po", "ゔ": "vu",
    "ぁ": "a", "ぃ": "i", "ぅ": "u", "ぇ": "e", "ぉ": "o",
}.items():
    _ROM[_k] = _v
_DIGRAPH = {}
for _c, _r in {"き": "ky", "ぎ": "gy", "し": "sh", "じ": "j", "ち": "ch", "に": "ny", "ひ": "hy", "び": "by", "ぴ": "py", "み": "my", "り": "ry"}.items():
    for _s, _v in {"ゃ": "a", "ゅ": "u", "ょ": "o"}.items():
        _DIGRAPH[_c + _s] = (_r + _v) if _r not in ("sh", "j", "ch") else (_r + _v if _r != "j" else "j" + _v)
for _k, _v in {"しぇ": "she", "じぇ": "je", "ちぇ": "che", "ふぁ": "fa", "ふぃ": "fi", "ふぇ": "fe", "ふぉ": "fo", "てぃ": "ti", "でぃ": "di",
               "うぃ": "wi", "うぇ": "we", "うぉ": "wo", "ゔぁ": "va", "ゔぃ": "vi", "ゔぇ": "ve", "ゔぉ": "vo", "とぅ": "tu", "どぅ": "du",
               "つぁ": "tsa", "つぃ": "tsi", "つぇ": "tse", "つぉ": "tso", "いぇ": "ye", "くぁ": "kwa", "ぐぁ": "gwa"}.items():
    _DIGRAPH[_k] = _v
_PUNCT = {"、": ",", "。": ".", "！": "!", "？": "?", "「": "\"", "」": "\"", "『": "\"", "』": "\"", "（": "(", "）": ")", "・": " ", "〜": "~",
          "…": "...", "：": ":", "；": ";", "　": " "}


def kana_to_romaji(k):
    """ひらがな（ほかの文字はそのまま）→ ローマ字"""
    out, i, n = [], 0, len(k)
    sok = False
    while i < n:
        c = k[i]
        two = k[i:i + 2]
        if c == "っ":
            sok = True
            i += 1
            continue
        if two in _DIGRAPH:
            r = _DIGRAPH[two]
            i += 2
        elif c == "ー":
            r = out[-1][-1] if out and out[-1] and out[-1][-1] in "aiueo" else ""
            i += 1
        elif c in _ROM:
            r = _ROM[c]
            i += 1
        else:
            r = c
            i += 1
        if sok and r:
            r = ("t" if r.startswith("ch") else "") + r[0] + r if r[0].isalpha() and not r.startswith("ch") else ("t" + r if r.startswith("ch") else r)
            sok = False
        # ん のあとに母音・や行が来るときは n'
        if out and out[-1] == "n" and r and r[0] in "aiueoy":
            out[-1] = "n'"
        out.append(r)
    return "".join(out)


_HYPHEN = {"さん", "様", "ちゃん", "君", "くん", "さま"}
_NO_SPACE_BEFORE = set(",.!?:;)")


class Reader:
    def __init__(self):
        try:
            import fugashi
        except ImportError:
            raise SystemExit("❌ 道具が入っていません：pip install fugashi unidic-lite")
        self.tagger = fugashi.Tagger()
        self.ov = load_overrides()
        self.ov_keys = sorted(self.ov, key=lambda k: -len(k))
        self.unknown = Counter()

    def _tokens(self, text):
        """(開始位置, 表記, よみ（ひらがな）または None, 品詞1, 品詞2) の並び"""
        out, pos = [], 0
        for w in self.tagger(text):
            s = w.surface
            i = text.find(s, pos)
            if i < 0:
                continue
            f = w.feature
            k = getattr(f, "kana", None)
            out.append((i, s, kata2hira(k) if k and k != "*" else None, getattr(f, "pos1", "") or "", getattr(f, "pos2", "") or ""))
            pos = i + len(s)
        return out

    def chunks(self, text):
        """text を Chunk の並びに分ける（元の空白も1つの Chunk として残す）。数字＋助数詞は、まとめて1つ（9月・14日 …）。
        数字のあとの、読めない助数詞には、ふりがなを付けない"""
        return self._with_gaps(text, self._chunks(text))

    def _with_gaps(self, text, chunks):
        out, cursor = [], 0
        for c in chunks:
            i = text.find(c.surface, cursor)
            if i > cursor:
                out.append(Chunk(text[cursor:i], None, False, "空白", ""))
            out.append(c)
            cursor = (i if i >= 0 else cursor) + len(c.surface)
        if cursor < len(text):
            out.append(Chunk(text[cursor:], None, False, "空白", ""))
        return out

    def _chunks(self, text):
        toks = self._tokens(text)
        res, i, n = [], 0, len(toks)
        month_before = False
        while i < n:
            pos, s, r, p1, p2 = toks[i]
            if NUM_RE.fullmatch(s):
                # 数字のかたまり（UniDic が「1」「,」「000」と割ることがあるので、本文から取り直す）
                digits = NUM_RE.match(text, pos).group(1)
                end = pos + len(digits)
                rest = text[end:]
                hit = next((c for c in COUNTERS if rest.startswith(c)), None)
                val = int(digits.translate(ZEN).replace(",", ""))
                rd = counter_reading(val, hit, month_before) if hit else None
                if hit and rd:
                    res.append(Chunk(digits + hit, rd, True, "名詞", ""))
                    month_before = (hit == "月")
                    stop = end + len(hit)
                else:
                    res.append(Chunk(digits, None, False, "名詞", "数詞"))      # 助数詞が分からない：数字はそのまま
                    month_before = False
                    stop = end
                while i < n and toks[i][0] < stop:
                    i += 1
                if not (hit and rd) and i < n and toks[i][0] == stop and KANJI.search(toks[i][1]):
                    # 数のあとの漢字は、数に合わせた音の変化があるかもしれないので、読みを付けない
                    res.append(Chunk(toks[i][1], None, False, toks[i][3], toks[i][4]))
                    i += 1
                continue
            month_before = False
            hit = next((k for k in self.ov_keys if text.startswith(k, pos)), None)
            if hit and KANJI.search(hit):
                # 上書きの表（私・誕生日・山手 …）は、本文から直接さがす。2つ以上のトークンにまたがるものも拾える
                res.append(Chunk(hit, self.ov[hit], True, p1, p2))
                stop = pos + len(hit)
                while i < n and toks[i][0] < stop:
                    i += 1
                continue
            if not KANJI.search(s):
                res.append(Chunk(s, r, False, p1, p2))
            else:
                rd = r
                if s == "人" and res and res[-1].pos2 == "固有名詞":
                    rd = "じん"                        # 日本人・韓国人・インド人（UniDic は「にん」と読んでしまう）
                if not rd:
                    self.unknown[s] += 1
                res.append(Chunk(s, rd, bool(rd), p1, p2))
            i += 1
        return res

    def ruby(self, text):
        out = []
        for c in self.chunks(text):
            if not c.on:
                out.append(c.surface)
                continue
            s, rd = c.surface, c.reading
            seg = align(s, rd) if KANJI.search(s) and not NUM_RE.match(s) else f"{s}{{{rd}}}"
            if out and re.match(f"[{BASE_CH}]", seg) and re.search(f"[{BASE_CH}]$", out[-1][-1:] or " "):
                out.append(BAR)                     # 前の漢字や数字とくっつかないように
            out.append(seg)
        return "".join(out)

    def romaji(self, text):
        """ヘボン式。単語ごとに空白。ふりがなと同じ読み（上書き・数字＋助数詞）を使う。
        つなげて読む部分（動詞＋ます＋た、お＋茶 …）は、かなのままつなげてから変換する（「行っ＋て」→ itte）"""
        t = re.sub("[\U0001F000-\U0001FFFF☀-➿️‍]", "", text)
        items, prev1 = [], ""
        for c in self.chunks(t):
            s = c.surface
            if c.pos1 == "空白":
                prev1 = prev1 if prev1 else ""
                items.append({"gap": True})
                continue
            if s in ("「", "『"):
                items.append({"punct": "\"", "role": "open"})
                prev1 = "補助記号"
                continue
            if s in ("」", "』"):
                items.append({"punct": "\"", "role": "close"})
                prev1 = "補助記号"
                continue
            if s in _PUNCT:
                items.append({"punct": _PUNCT[s], "role": "mid"})
                prev1 = "補助記号"
                continue
            if c.pos1 == "助詞" and s in ("は", "へ", "を"):
                k = {"は": "わ", "へ": "え", "を": "お"}[s]
            elif c.reading and (c.on or not re.search("[A-Za-z0-9]", s)):
                k = c.reading
            elif re.fullmatch("[぀-ヿ]+", s):
                k = kata2hira(s)
            else:
                k = None
            glue = "space"
            if c.pos1 == "助動詞" and prev1 in ("動詞", "形容詞", "助動詞"):
                glue = "join"
            elif c.pos1 == "接尾辞":
                glue = "hyphen" if s in _HYPHEN else "join"
            elif c.pos1 == "助詞" and s in ("て", "で", "たり", "だり", "ば", "ず") and prev1 in ("動詞", "形容詞", "助動詞"):
                glue = "join"
            elif prev1 == "接頭辞":
                glue = "join"
            items.append({"kana": k, "lit": s if k is None else None, "glue": glue, "proper": c.pos2 == "固有名詞"})
            prev1 = c.pos1
        # つなげる
        groups = []
        for it in items:
            if it.get("gap"):
                continue
            if "punct" in it:
                groups.append(it)
                continue
            last = groups[-1] if groups else None
            if (it["glue"] in ("join", "hyphen") and last and "pieces" in last and it["kana"] is not None and last["pieces"][-1][0] is not None):
                if it["glue"] == "hyphen":
                    last["pieces"].append([it["kana"], True])
                else:
                    last["pieces"][-1][0] += it["kana"]
                continue
            groups.append({"pieces": [[it["kana"] if it["kana"] is not None else it["lit"], False, it["kana"] is None]], "proper": it["proper"]})
        out = ""
        for g in groups:
            if "punct" in g:
                role, ch = g["role"], g["punct"]
                if role == "open":
                    out += (" " if out and not out.endswith(" ") else "") + ch
                elif role == "close":
                    out = out.rstrip(" ") + ch + " "
                else:
                    out = out.rstrip(" ") + ch + (" " if ch in ",.!?:;" else "")
                continue
            parts = []
            for pc in g["pieces"]:
                lit = len(pc) > 2 and pc[2]
                parts.append(pc[0] if lit else kana_to_romaji(kata2hira(pc[0])))
            word = "-".join(parts)
            if g["proper"]:
                word = word[:1].upper() + word[1:]
            if out == "" or out.endswith((" ", "\"", "(")) and not out.endswith(" \"") or out.endswith(" "):
                out += word
            else:
                out += " " + word
        out = re.sub(r"\s+", " ", out).strip()
        return out[:1].upper() + out[1:]


def plain(t):
    return re.sub(r"<[^>]+>", "", t)


def digest(d, ov):
    s = json.dumps(d, sort_keys=True, ensure_ascii=False) + json.dumps(ov, sort_keys=True, ensure_ascii=False) + VERSION
    return hashlib.sha1(s.encode()).hexdigest()[:12]


def articles():
    for p in sorted(WORKS.glob("*/i18n/data.ja.json")):
        yield p.parent.parent.name, p


def read_dict(p):
    return json.loads(p.read_text(encoding="utf-8")).get("dict", {})


def build(slug, p, rd, force=False):
    d = read_dict(p)
    h = digest(d, rd.ov)
    out = p.parent / "read.ja.json"
    if out.exists() and not force:
        try:
            if json.loads(out.read_text(encoding="utf-8")).get("h") == h:
                return False
        except ValueError:
            pass
    r, m = {}, {}
    for fp, v in d.items():
        t = plain(v)
        if not re.search(r"[぀-ヿ㐀-鿿]", t):
            continue
        assert BAR not in t and "{" not in t and "}" not in t, (slug, t)
        a = rd.ruby(t)
        if a != t:
            r[fp] = a
        m[fp] = rd.romaji(t)
    data = {"h": h, "r": r, "m": m}
    out.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":"), sort_keys=True) + "\n", encoding="utf-8")
    return True


def stale():
    """check.py --site から呼ぶ。作り直しが要る記事の名前の一覧（道具は読み込まない）"""
    ov = load_overrides()
    bad = []
    for slug, p in articles():
        out = p.parent / "read.ja.json"
        try:
            ok = out.exists() and json.loads(out.read_text(encoding="utf-8")).get("h") == digest(read_dict(p), ov)
        except ValueError:
            ok = False
        if not ok:
            bad.append(slug)
    return bad


def corpus():
    seen = set()
    for slug, p in articles():
        for v in read_dict(p).values():
            t = plain(v)
            if t not in seen:
                seen.add(t)
                yield t


def main():
    args = sys.argv[1:]
    if "--test" in args:
        return self_test()
    if "--check" in args:
        bad = stale()
        print(f"{'❌' if bad else '✅'} ふりがな・ローマ字：{len(bad)}本が古い" + (f"（例：{', '.join(bad[:5])}）→ python3 tools/furigana.py" if bad else ""))
        return 1 if bad else 0
    rd = Reader()
    if "--pairs" in args:
        c = Counter()
        for t in corpus():
            for ch in rd.chunks(t):
                if ch.on:
                    c[(ch.surface, ch.reading)] += 1
        k = args.index("--pairs")
        for (s, r), n in c.most_common(int(args[k + 1]) if len(args) > k + 1 else 400):
            print(f"{n:4d}  {s}  {r}")
        return 0
    if "--sample" in args:
        n = int(args[args.index("--sample") + 1])
        rows = [t for t in corpus() if KANJI.search(t) and len(t) > 8]
        random.seed(int(args[args.index("--seed") + 1]) if "--seed" in args else 7)
        for t in random.sample(rows, min(n, len(rows))):
            print(rd.ruby(t))
            print("   ", rd.romaji(t))
        return 0
    n = 0
    for slug, p in articles():
        if build(slug, p, rd, force="--force" in args):
            n += 1
    print(f"📖 ふりがな・ローマ字：{n}本を作り直した（全{len(list(articles()))}本）")
    if rd.unknown:
        print("⚠️ 読みが分からなかった漢字：", ", ".join(f"{k}×{v}" for k, v in rd.unknown.most_common(20)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
