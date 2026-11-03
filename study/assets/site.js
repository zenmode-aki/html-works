/* ==========================================================
   サイト全体の設定。URL を変えるときは「ここだけ」直す。
   全ページの一番下の共通フッターは、この設定から作られます。
   ========================================================== */
window.SITE = {
  // 日常のブログ（15秒ブログ）のURL
  dailyBlogUrl: "https://15-second-blog.com/",
  // 日常ブログの名前（本人の Workflowy「作りたいブログの種類」の呼び方のまま。どの言語でもこのまま出す）
  dailyBlogName: "ともだちんこブログ",
  // 「アドバイスください！」の Googleフォーム（まだ仮。決まったらここを直す）
  adviceFormUrl: "https://forms.gle/REPLACE_ME"
};

/* ==========================================================
   ことば（日本語・English・한국어）
   HTML には日本語をそのまま書く。data-i18n="キー" を付けた所だけ、ここの訳に切りかわる。
   記事の本文は、記事の中に <div class="i18n" lang="ja">…</div> と en・ko を3つ並べる。
   ========================================================== */
var I18N = {
  en: {
    "brand.name": "15-Second Study Notes",
    "brand.sub": "with Pengesso",
    "hero.title": "What I'm learning,<br>in 15-second notes.",
    "hero.lead": "This site is just where I jot down what I'm studying right now. Every note takes 15 seconds to read — 30 at most.",
    "it.note": "Things I've figured out go here.",
    "self.title": "Self-control",
    "self.note": "How to steer myself. I write here now and then.",
    "others.title": "Other interests",
    "empty": "No notes yet.",
    "tag.network": "Network", "tag.security": "Security", "tag.dev": "System development",
    "tag.breath": "Breathing", "tag.money": "Finance & economics", "tag.brain": "Neuroscience",
    "tag.book": "Lessons from books", "tag.english": "English", "tag.training": "Strength training",
    "back": "← Back to top",
    "f.daily.kicker": "EVERYDAY LIFE", "f.daily.title": "{name} →", "f.daily.sub": "Not study stuff — everyday stories live here.",
    "f.advice.kicker": "HELP ME", "f.advice.title": "Give me advice!", "f.advice.ready": "Opens a Google Form", "f.advice.soon": "Form coming soon",
    "f.note": "© 15-Second Study Notes"
  },
  ko: {
    "brand.name": "15초 공부 노트",
    "brand.sub": "펭게소와 함께",
    "hero.title": "공부 중인 것을,<br>15초 메모로.",
    "hero.lead": "이 사이트는 지금 공부하고 있는 걸 그냥 메모해 두는 곳이에요. 모두 15초, 길어도 30초 안에 읽을 수 있게 썼어요.",
    "it.note": "알게 된 것을 여기에 메모해요.",
    "self.title": "자제력",
    "self.note": "나 자신을 다스리는 방법. 배운 걸 가끔 써요.",
    "others.title": "그 밖에 · 관심 있는 것",
    "empty": "아직 메모가 없어요.",
    "tag.network": "네트워크", "tag.security": "보안", "tag.dev": "시스템 개발",
    "tag.breath": "호흡", "tag.money": "금융 · 경제", "tag.brain": "뇌과학",
    "tag.book": "책에서 배운 것", "tag.english": "영어", "tag.training": "근력 운동",
    "back": "← 처음으로",
    "f.daily.kicker": "일상", "f.daily.title": "{name}은 여기", "f.daily.sub": "공부 말고, 평소 이야기는 여기에 써요.",
    "f.advice.kicker": "도와줘요", "f.advice.title": "조언 부탁해요!", "f.advice.ready": "구글 폼이 열려요", "f.advice.soon": "폼은 준비 중이에요",
    "f.note": "© 15초 공부 노트"
  },
  ja: {
    "f.daily.kicker": "日常のほう", "f.daily.title": "{name}はこっち", "f.daily.sub": "勉強やない、ふだんの話はここに書いてるで",
    "f.advice.kicker": "ヘルプみー", "f.advice.title": "アドバイスください！", "f.advice.ready": "Googleフォームが開くで", "f.advice.soon": "フォームは準備中やで",
    "f.note": "© 15秒の勉強ノート"
  }
};

(function () {
  var LANGS = ["ja", "en", "ko"];
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
  var q = (location.search.match(/[?&]lang=(ja|en|ko)/) || [])[1];
  var lang = q || store("study-lang") || "ja";
  if (LANGS.indexOf(lang) < 0) lang = "ja";

  // 日本語の元の文を覚えておく（ja にもどすとき用）
  var nodes = document.querySelectorAll("[data-i18n]");
  for (var i = 0; i < nodes.length; i++) nodes[i].setAttribute("data-ja", nodes[i].innerHTML);

  function t(key) { var d = I18N[lang] || {}; return d[key] != null ? d[key] : (I18N.ja[key] || ""); }

  function footer() {
    var f = document.getElementById("common-footer");
    if (!f) return;
    var s = window.SITE, root = f.getAttribute("data-root") || "";
    var ready = s.adviceFormUrl.indexOf("REPLACE_ME") < 0;
    f.innerHTML =
      '<div class="cf-inner">' +
        '<a class="cf-card cf-daily" href="' + s.dailyBlogUrl + '">' +
          '<img src="' + root + 'images/pengesso.webp" alt="" width="40" height="40">' +
          '<span class="cf-text"><span class="cf-kicker">' + t("f.daily.kicker") + '</span>' +
          '<span class="cf-title">' + t("f.daily.title").replace("{name}", s.dailyBlogName) + '</span>' +
          '<span class="cf-sub">' + t("f.daily.sub") + '</span></span>' +
        '</a>' +
        (ready ? '<a class="cf-card cf-advice" href="' + s.adviceFormUrl + '" target="_blank" rel="noopener">' : '<div class="cf-card cf-advice" aria-disabled="true">') +
          '<span class="cf-text"><span class="cf-kicker">' + t("f.advice.kicker") + '</span>' +
          '<span class="cf-title">' + t("f.advice.title") + '</span>' +
          '<span class="cf-sub">' + t(ready ? "f.advice.ready" : "f.advice.soon") + '</span></span>' +
        (ready ? '</a>' : '</div>') +
      '</div>' +
      '<p class="cf-note">' + t("f.note") + '</p>';
  }

  function apply(next) {
    lang = next;
    document.documentElement.lang = lang;
    for (var i = 0; i < nodes.length; i++) {
      var n = nodes[i], k = n.getAttribute("data-i18n");
      n.innerHTML = lang === "ja" ? n.getAttribute("data-ja") : ((I18N[lang] || {})[k] || n.getAttribute("data-ja"));
    }
    var blocks = document.querySelectorAll(".i18n[lang]");
    for (var j = 0; j < blocks.length; j++) blocks[j].hidden = blocks[j].getAttribute("lang") !== lang;
    var btns = document.querySelectorAll(".lang button");
    for (var b = 0; b < btns.length; b++) btns[b].setAttribute("aria-pressed", btns[b].getAttribute("data-lang") === lang ? "true" : "false");
    footer();
  }

  document.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest(".lang button");
    if (!b) return;
    store("study-lang", b.getAttribute("data-lang"));
    apply(b.getAttribute("data-lang"));
  });
  apply(lang);
})();
