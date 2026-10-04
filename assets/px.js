(function () {
'use strict';
if (window.__px) return;
var px = window.__px = { version: 1 };
var doc = document, root = doc.documentElement, loc = location;
var LANG = window.PENGESSO_LANG || root.getAttribute('lang') || 'en';
var KEY_VID = 'pengesso-vid', KEY_LIKED = 'pengesso-liked', KEY_OFF = 'pengesso-nocount';
function get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
function put(k, v) { try { if (v === null) localStorage.removeItem(k); else localStorage.setItem(k, v); } catch (e) {} }
function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
function el(tag, cls, html) { var e = doc.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
function qs(s, r) { return (r || doc).querySelector(s); }
function qsa(s, r) { return [].slice.call((r || doc).querySelectorAll(s)); }
var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
var T = {
en: { devices: 'Devices', countriesW: 'countries', viewsF: '{n} views', viewsF1: '{n} view', countriesF: '{n} countries', countriesF1: '{n} country', liveF: '{n} reading now', views: 'views', countries: 'countries', live: 'reading now', likeLabel: 'Like', liked: 'Liked', likeAria: 'Like this post',
endTitle: 'Liked this post?', endSub: 'Tap the heart. It tells the next reader this post was worth it.', how: 'How are these numbers counted?',
howTitle: 'How these numbers work', since: 'Counting since {d}.',
b1: 'Only real readers are counted. Search-engine robots and similar programs are left out.',
b2: 'The same person reading the same post is counted once a day.',
b3: 'No cookies. No name, no email. The IP address is never saved. Only the country (like JP) is kept.',
b4: 'Likes: one per person per post, and you can take it back. A random ID in your browser tells us it is you. It holds no personal data.',
b5: 'The owner’s own visits are left out. Numbers are shown as they are, small or big.',
dnt: 'People who turn on “Do Not Track” are not counted.', offBtn: 'Do not count this browser', onBtn: 'Count this browser again',
offNow: 'This browser is not counted. Likes are off too.', onNow: 'This browser is counted.',
world: 'Readers around the world', thisWeek: 'This week', allTime: 'All time', topCountries: 'Where readers are', languages: 'Reading languages',
dash: '📊 See all the numbers →',
arrive: 'How readers arrive', showAll: 'Show all {n} countries', popular: 'Popular this week', likesWord: 'likes', today: 'Today',
nowReading: '{n} reading right now', fromWhere: 'from {n} countries', err: 'Could not save. Please try again.',
demo: '🧪 SAMPLE DATA. These are not real numbers.', offToast: 'This browser will not be counted.', onToast: 'This browser will be counted.',
close: 'Close', start: 'The numbers are real. They start small, and they grow.', dev: { phone: 'Phone', desktop: 'Computer', tablet: 'Tablet' },
ref: { direct: 'Direct', google: 'Google', bing: 'Bing', yahoo: 'Yahoo', x: 'X', facebook: 'Facebook', instagram: 'Instagram', line: 'LINE', youtube: 'YouTube', github: 'GitHub', reddit: 'Reddit', hatena: 'Hatena', other: 'Other' } },
ja: { devices: '端末', countriesW: '国', viewsF: '閲覧 {n}', countriesF: '{n}か国', liveF: 'いま{n}人が読んでいます', views: '閲覧', countries: 'か国', live: 'いま読んでいる', likeLabel: 'いいね', liked: 'いいね済み', likeAria: 'この記事にいいねする',
endTitle: 'この記事、よかったら', endSub: 'ハートを押すと、次に読む人に「この記事、いいよ」と伝わります。', how: 'この数字は、どう数えていますか？',
howTitle: 'この数字の数え方', since: '{d} から数えています。',
b1: '本物の読者だけを数えています。検索ロボットなどは除いています。',
b2: '同じ人が同じ記事を読んでも、1日に1回だけ数えます。',
b3: 'Cookie は使いません。名前もメールも集めません。IPアドレスは保存せず、国（JP など）だけを使います。',
b4: 'いいねは、1人が1つの記事に1つだけです。取り消せます。ブラウザに置いたランダムなIDで見分けます。個人の情報は入っていません。',
b5: '運営者自身のアクセスは除いています。数字は、小さくても大きくても、そのまま出しています。',
dnt: '「トラッキングしない」（Do Not Track）設定の人は、数えません。', offBtn: 'このブラウザのアクセスを数えない', onBtn: 'このブラウザも数える',
offNow: 'このブラウザは数えていません。いいねもできません。', onNow: 'このブラウザは数えています。',
world: '世界の読者', thisWeek: '今週', allTime: 'これまで', topCountries: '読まれている国', languages: '読まれている言語',
dash: '📊 数字をぜんぶ見る →',
arrive: 'どこから来たか', showAll: '{n}か国ぜんぶ見る', popular: '今週よく読まれている記事', likesWord: 'いいね', today: '今日',
nowReading: 'いま {n}人が読んでいます', fromWhere: '{n}か国から', err: 'うまく保存できませんでした。もう一度どうぞ。',
demo: '🧪 サンプルの数字です。本物ではありません。', offToast: 'このブラウザは数えません。', onToast: 'このブラウザも数えます。',
close: '閉じる', start: '数字は本物です。小さく始まって、少しずつ育ちます。', dev: { phone: 'スマホ', desktop: 'パソコン', tablet: 'タブレット' },
ref: { direct: '直接', google: 'Google', bing: 'Bing', yahoo: 'Yahoo!', x: 'X', facebook: 'Facebook', instagram: 'Instagram', line: 'LINE', youtube: 'YouTube', github: 'GitHub', reddit: 'Reddit', hatena: 'はてな', other: 'そのほか' } },
ko: { devices: '기기', countriesW: '나라', viewsF: '조회 {n}', countriesF: '{n}개국', liveF: '지금 {n}명이 읽는 중', views: '조회', countries: '개국', live: '지금 읽는 중', likeLabel: '좋아요', liked: '좋아요 완료', likeAria: '이 글에 좋아요',
endTitle: '이 글이 좋았다면', endSub: '하트를 누르면, 다음에 읽는 분에게 “이 글 괜찮아요”가 전해져요.', how: '이 숫자는 어떻게 세나요?',
howTitle: '숫자 집계 방식', since: '{d}부터 세고 있어요.',
b1: '진짜 독자만 세요. 검색 로봇 같은 것은 빼요.',
b2: '같은 사람이 같은 글을 읽어도 하루에 한 번만 세요.',
b3: '쿠키는 쓰지 않아요. 이름도 이메일도 모으지 않아요. IP 주소는 저장하지 않고, 나라(JP 등)만 써요.',
b4: '좋아요는 한 사람이 한 글에 하나만, 취소할 수 있어요. 브라우저의 무작위 ID로 구분하고, 개인 정보는 들어 있지 않아요.',
b5: '운영자 본인의 접속은 뺐어요. 숫자는 작아도 커도 있는 그대로 보여 드려요.',
dnt: '“추적하지 않음”(Do Not Track)을 켠 분은 세지 않아요.', offBtn: '이 브라우저는 세지 않기', onBtn: '이 브라우저도 다시 세기',
offNow: '이 브라우저는 세지 않아요. 좋아요도 꺼져 있어요.', onNow: '이 브라우저도 세고 있어요.',
world: '세계의 독자', thisWeek: '이번 주', allTime: '지금까지', topCountries: '읽고 있는 나라', languages: '읽는 언어',
dash: '📊 숫자 모두 보기 →',
arrive: '어디서 왔나요', showAll: '{n}개국 모두 보기', popular: '이번 주 인기 글', likesWord: '좋아요', today: '오늘',
nowReading: '지금 {n}명이 읽고 있어요', fromWhere: '{n}개국에서', err: '저장하지 못했어요. 다시 해 주세요.',
demo: '🧪 샘플 숫자예요. 진짜가 아니에요.', offToast: '이 브라우저는 세지 않아요.', onToast: '이 브라우저도 세요.',
close: '닫기', start: '숫자는 진짜예요. 작게 시작해서 조금씩 자라요.', dev: { phone: '휴대폰', desktop: '컴퓨터', tablet: '태블릿' },
ref: { direct: '직접', google: 'Google', bing: 'Bing', yahoo: 'Yahoo', x: 'X', facebook: 'Facebook', instagram: 'Instagram', line: 'LINE', youtube: 'YouTube', github: 'GitHub', reddit: 'Reddit', hatena: 'Hatena', other: '기타' } },
zh: { devices: '设备', countriesW: '国家', viewsF: '浏览 {n}', countriesF: '{n}个国家', liveF: '现在 {n} 人在读', views: '浏览', countries: '个国家', live: '正在阅读', likeLabel: '点赞', liked: '已点赞', likeAria: '给这篇文章点赞',
endTitle: '觉得这篇不错的话', endSub: '点一下爱心，下一位读者就会知道“这篇值得读”。', how: '这些数字是怎么统计的？',
howTitle: '数字是怎么统计的', since: '从 {d} 开始统计。',
b1: '只统计真实的读者，搜索引擎机器人之类的不算。',
b2: '同一个人读同一篇文章，一天只算一次。',
b3: '不使用 Cookie，不收集姓名和邮箱，不保存 IP 地址，只用国家（如 JP）。',
b4: '点赞：一个人对一篇文章只能点一次，可以取消。用浏览器里的随机 ID 来区分，里面没有个人信息。',
b5: '运营者自己的访问不算。数字不论大小，都如实显示。',
dnt: '开启“请勿跟踪”（Do Not Track）的人不会被统计。', offBtn: '不统计这个浏览器', onBtn: '重新统计这个浏览器',
offNow: '这个浏览器不被统计，点赞也已关闭。', onNow: '这个浏览器被统计。',
world: '世界各地的读者', thisWeek: '本周', allTime: '到目前为止', topCountries: '读者所在的国家', languages: '阅读语言',
dash: '📊 查看全部数字 →',
arrive: '读者从哪里来', showAll: '查看全部 {n} 个国家', popular: '本周热门文章', likesWord: '点赞', today: '今天',
nowReading: '现在有 {n} 人在读', fromWhere: '来自 {n} 个国家', err: '保存失败，请再试一次。',
demo: '🧪 这是示例数字，不是真实数据。', offToast: '这个浏览器不会被统计。', onToast: '这个浏览器会被统计。',
close: '关闭', start: '数字是真实的。从小开始，慢慢长大。', dev: { phone: '手机', desktop: '电脑', tablet: '平板' },
ref: { direct: '直接访问', google: 'Google', bing: 'Bing', yahoo: 'Yahoo', x: 'X', facebook: 'Facebook', instagram: 'Instagram', line: 'LINE', youtube: 'YouTube', github: 'GitHub', reddit: 'Reddit', hatena: 'Hatena', other: '其他' } },
'zh-Hant': { devices: '裝置', countriesW: '國家', viewsF: '瀏覽 {n}', countriesF: '{n}個國家', liveF: '現在 {n} 人在讀', views: '瀏覽', countries: '個國家', live: '正在閱讀', likeLabel: '按讚', liked: '已按讚', likeAria: '為這篇文章按讚',
endTitle: '覺得這篇不錯的話', endSub: '按一下愛心，下一位讀者就會知道「這篇值得讀」。', how: '這些數字是怎麼統計的？',
howTitle: '數字是怎麼統計的', since: '從 {d} 開始統計。',
b1: '只統計真實的讀者，搜尋引擎機器人之類的不算。',
b2: '同一個人讀同一篇文章，一天只算一次。',
b3: '不使用 Cookie，不蒐集姓名和電子郵件，不儲存 IP 位址，只用國家（如 JP）。',
b4: '按讚：一個人對一篇文章只能按一次，可以取消。用瀏覽器裡的隨機 ID 來區分，裡面沒有個人資訊。',
b5: '營運者自己的造訪不算。數字不論大小，都如實顯示。',
dnt: '開啟「請勿追蹤」（Do Not Track）的人不會被統計。', offBtn: '不統計這個瀏覽器', onBtn: '重新統計這個瀏覽器',
offNow: '這個瀏覽器不被統計，按讚也已關閉。', onNow: '這個瀏覽器被統計。',
world: '世界各地的讀者', thisWeek: '本週', allTime: '到目前為止', topCountries: '讀者所在的國家', languages: '閱讀語言',
dash: '📊 查看全部數字 →',
arrive: '讀者從哪裡來', showAll: '查看全部 {n} 個國家', popular: '本週熱門文章', likesWord: '按讚', today: '今天',
nowReading: '現在有 {n} 人在讀', fromWhere: '來自 {n} 個國家', err: '儲存失敗，請再試一次。',
demo: '🧪 這是範例數字，不是真實資料。', offToast: '這個瀏覽器不會被統計。', onToast: '這個瀏覽器會被統計。',
close: '關閉', start: '數字是真實的。從小開始，慢慢長大。', dev: { phone: '手機', desktop: '電腦', tablet: '平板' },
ref: { direct: '直接造訪', google: 'Google', bing: 'Bing', yahoo: 'Yahoo', x: 'X', facebook: 'Facebook', instagram: 'Instagram', line: 'LINE', youtube: 'YouTube', github: 'GitHub', reddit: 'Reddit', hatena: 'Hatena', other: '其他' } }
};
var L = T[LANG] || T.en;
function t(k) { return L[k] != null ? L[k] : T.en[k]; }
function fill(s, o) { return String(s).replace(/\{(\w+)\}/g, function (m, k) { return o[k] != null ? o[k] : m; }); }
px.t = t;
function pat(k, n) { return fill(n === 1 && L[k + '1'] ? L[k + '1'] : t(k), { n: fmt(n) }); }
var nf, nfc, regionNames = null, langNames = null, df;
try { nf = new Intl.NumberFormat(LANG); nfc = new Intl.NumberFormat(LANG, { notation: 'compact', maximumFractionDigits: 1 }); } catch (e) { nf = { format: String }; nfc = nf; }
try { regionNames = new Intl.DisplayNames([LANG], { type: 'region' }); } catch (e) {}
try { langNames = new Intl.DisplayNames([LANG], { type: 'language' }); } catch (e) {}
try { df = new Intl.DateTimeFormat(LANG, { dateStyle: 'long' }); } catch (e) { df = null; }
function fmt(n) { n = +n || 0; return n >= 10000 ? nfc.format(n) : nf.format(n); }
function flag(cc) {
if (!/^[A-Z]{2}$/.test(cc)) return '🌐';
return String.fromCodePoint(0x1F1E6 + cc.charCodeAt(0) - 65, 0x1F1E6 + cc.charCodeAt(1) - 65);
}
function country(cc) { try { return (regionNames && regionNames.of(cc)) || cc; } catch (e) { return cc; } }
function langName(l) { try { return (langNames && langNames.of(l === 'zh-hant' ? 'zh-Hant' : l)) || l; } catch (e) { return l; } }
function dateText(iso) {
try { return df ? df.format(new Date(iso + 'T00:00:00')) : iso; } catch (e) { return iso; }
}
var path = loc.pathname.replace(/index\.html$/, '');
var m = /^\/works\/([a-z0-9][a-z0-9-]*)\/$/.exec(path);
var slug = m ? m[1] : (path === '/' ? '_home' : '');
var kind = m ? 'post' : (slug === '_home' ? 'home' : '');
var params = new URLSearchParams(loc.search);
var demo = params.get('pxdemo') === '1';
var local = /^(localhost|127\.0\.0\.1)$/.test(loc.hostname);
px.slug = slug; px.kind = kind;
if (params.get('count') === 'off') { put(KEY_OFF, '1'); px.justToggled = 'off'; }
if (params.get('count') === 'on') { put(KEY_OFF, null); px.justToggled = 'on'; }
function blocked() { return get(KEY_OFF) === '1'; }
function dnt() {
return navigator.doNotTrack === '1' || window.doNotTrack === '1' || navigator.msDoNotTrack === '1' || navigator.globalPrivacyControl === true;
}
function vid() {
var v = get(KEY_VID);
if (v && /^[A-Za-z0-9_-]{16,64}$/.test(v)) return v;
var a = new Uint8Array(18), s = '';
try { crypto.getRandomValues(a); } catch (e) { for (var i = 0; i < 18; i++) a[i] = Math.floor(Math.random() * 256); }
for (var j = 0; j < a.length; j++) s += ('0' + a[j].toString(16)).slice(-2);
put(KEY_VID, s);
return s;
}
function likedLocal() { try { return JSON.parse(get(KEY_LIKED) || '[]'); } catch (e) { return []; } }
function setLikedLocal(slug_, on) {
var a = likedLocal().filter(function (x) { return x !== slug_; });
if (on) a.push(slug_);
put(KEY_LIKED, JSON.stringify(a.slice(-500)));
}
var cfg = null;
function api(method, p, body) {
if (cfg.demo) return demoApi(method, p, body);
var ctl = window.AbortController ? new AbortController() : null;
var timer = ctl ? setTimeout(function () { ctl.abort(); }, 7000) : 0;
return fetch(cfg.endpoint + p, {
method: method, mode: 'cors', credentials: 'omit', keepalive: method === 'POST',
headers: body ? { 'Content-Type': 'text/plain;charset=UTF-8' } : undefined,
body: body ? JSON.stringify(body) : undefined, signal: ctl ? ctl.signal : undefined
}).then(function (r) { clearTimeout(timer); if (!r.ok) throw new Error('http ' + r.status); return r.json(); });
}
var demoLikes = {};
function seedOf(s) { var h = 7; for (var i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) >>> 0; return h; }
var DEMO_CC = [['JP', 5120], ['US', 1630], ['KR', 880], ['PH', 640], ['TW', 410], ['GB', 330], ['DE', 260], ['BR', 190], ['IN', 180], ['FR', 160], ['MY', 150], ['TH', 120], ['AU', 110], ['CA', 105], ['ID', 90], ['ES', 70], ['MX', 60], ['VN', 55], ['SG', 50], ['NL', 40]];
function demoPost(s) {
var h = seedOf(s), v = 80 + (h % 3200), cc = DEMO_CC.slice(0, 4 + (h % 14)).map(function (x, i) { return [x[0], Math.max(1, Math.round(v * x[1] / 9000))]; });
return { p: s, v: v, v7: Math.round(v / 5), l: 3 + (h % 140) + (demoLikes[s] ? 1 : 0), lk: !!demoLikes[s], nc: cc.length, cc: cc, live: { n: 6, here: 1 + (h % 4), cc: [['JP', 3], ['US', 1], ['KR', 1]] } };
}
function demoApi(method, p, body) {
return new Promise(function (ok) {
setTimeout(function () {
if (p.indexOf('/v1/stats') === 0) {
var posts = window.POSTS || [];
ok({ ok: 1, site: { since: '2026-10-04', v: 48210, vt: 612, v7: 5320, l: 2840, nc: 62, cc: DEMO_CC.map(function (x) { return [x[0], x[1] * 5]; }),
top7: posts.slice(2, 12).map(function (q, i) { return [q.slug, 900 - i * 61]; }), topAll: [], topLiked: [],
lang: [['en', 20100], ['ja', 15400], ['ko', 5200], ['zh', 3300], ['es', 1500], ['fr', 900], ['pt', 700], ['zh-hant', 600]],
ref: [['direct', 18000], ['line', 9000], ['x', 8000], ['google', 7000], ['instagram', 3000], ['other', 3210]], dev: [['phone', 33000], ['desktop', 13000], ['tablet', 2210]],
live: { n: 14, here: 0, cc: [['JP', 6], ['US', 3], ['KR', 2], ['PH', 1], ['GB', 1], ['DE', 1]] },
per: posts.map(function (q) { var h = seedOf(q.slug); return [q.slug, 60 + (h % 3000), h % 120]; }) } });
} else if (p.indexOf('/v1/like') === 0) {
demoLikes[body.p] = !!body.on; ok({ ok: 1, post: demoPost(body.p) });
} else {
ok({ ok: 1, n: 1, post: demoPost(slug || '_home') });
}
}, 250);
});
}
var css = [
'.px-strip{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin:0;max-height:0;opacity:0;overflow:hidden;transition:max-height .5s ease,opacity .5s ease,margin .5s ease}',
'.px-strip.in{max-height:140px;opacity:1;margin:-2px 0 18px;overflow:visible}',
'.px-chip{display:inline-flex;align-items:center;gap:6px;min-height:34px;padding:6px 13px;border-radius:999px;background:#fff;border:1.5px solid rgba(35,44,72,.10);',
'color:#4a3d58;font-weight:800;font-size:13px;line-height:1.2;font-family:inherit;text-decoration:none;white-space:nowrap;box-shadow:0 4px 12px rgba(115,70,111,.07)}',
'button.px-chip{cursor:pointer}',
'.px-chip b{font-weight:900;color:#2b2440}',
'.px-chip.px-info{padding:6px 11px;color:#6a55c8}',
'.px-chip:focus-visible,.px-heart:focus-visible,.px-link:focus-visible,.px-x:focus-visible,.px-btn:focus-visible{outline:3px solid rgba(139,109,232,.6);outline-offset:2px}',
'.px-dot{width:9px;height:9px;border-radius:50%;background:#2fc27b;flex:none;animation:px-pulse 1.9s ease-out infinite}',
'@keyframes px-pulse{0%{box-shadow:0 0 0 0 rgba(47,194,123,.55)}100%{box-shadow:0 0 0 9px rgba(47,194,123,0)}}',
'.px-heart-ic{width:1.25em;height:1.25em;flex:none;fill:none;stroke:currentColor;stroke-width:2;stroke-linejoin:round}',
'.px-chip[aria-pressed="true"]{background:#ffe6ef;border-color:#ff92b8;color:#c2255c}',
'.px-chip[aria-pressed="true"] .px-heart-ic,.px-heart[aria-pressed="true"] .px-heart-ic{fill:#ef4a7f;stroke:#ef4a7f}',
'.px-end{position:relative;margin:26px 0 0;padding:24px 20px 20px;border-radius:28px;text-align:center;color:#322536;',
'background:linear-gradient(135deg,rgba(255,255,255,.96),rgba(255,240,247,.96));border:2px solid rgba(255,255,255,.95);box-shadow:0 14px 36px rgba(115,70,111,.13)}',
'.px-end h3{margin:0;font-size:19px;line-height:1.35;font-weight:900;color:#3b2745}',
'.px-end p{margin:6px auto 0;max-width:34ch;font-size:14px;line-height:1.6;font-weight:700;color:#7a6a88}',
'.px-heart{position:relative;display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:58px;margin-top:16px;padding:12px 30px;border:0;border-radius:999px;',
'cursor:pointer;font-weight:900;font-size:17px;line-height:1;font-family:inherit;color:#c2255c;background:#fff;box-shadow:0 8px 0 #f3c3d4,0 14px 26px rgba(194,37,92,.16);transition:transform .15s ease,box-shadow .15s ease}',
'.px-heart:active{transform:translateY(5px) scale(.98);box-shadow:0 3px 0 #f3c3d4,0 6px 14px rgba(194,37,92,.12)}',
'.px-heart .px-heart-ic{width:1.5em;height:1.5em}',
'.px-heart[aria-pressed="true"]{background:#fff0f5;color:#ef4a7f}',
'.px-heart.pop .px-heart-ic{animation:px-pop .55s cubic-bezier(.2,1.6,.4,1)}',
'@keyframes px-pop{0%{transform:scale(1)}35%{transform:scale(1.55)}100%{transform:scale(1)}}',
'.px-burst{position:absolute;left:50%;top:50%;width:14px;height:14px;margin:-7px 0 0 -7px;pointer-events:none;fill:#ef4a7f;opacity:0;animation:px-fly .75s ease-out forwards}',
'@keyframes px-fly{0%{opacity:1;transform:translate(0,0) scale(.5)}100%{opacity:0;transform:translate(var(--dx),var(--dy)) scale(1.1)}}',
'.px-flags{display:flex;flex-wrap:wrap;justify-content:center;gap:4px 6px;margin:18px 0 0;font-size:25px;line-height:1.2}',
'.px-flags span{display:inline-block;cursor:default}',
'.px-sum{margin:12px 0 0;font-size:13.5px;font-weight:800;color:#6a5a78}',
'.px-link{display:inline-block;margin-top:12px;padding:8px 12px;border:0;background:none;color:#6a55c8;font-weight:800;font-size:13px;line-height:1.3;font-family:inherit;text-decoration:underline;text-underline-offset:3px;cursor:pointer}',
'.px-ov{position:fixed;inset:0;z-index:2147483200;display:flex;align-items:flex-end;justify-content:center;background:rgba(20,16,36,.46);opacity:0;transition:opacity .25s ease}',
'.px-ov.in{opacity:1}',
'.px-sheet{position:relative;width:min(560px,calc(100% - 16px));max-height:min(86vh,720px);margin:0 0 8px;overflow:auto;overscroll-behavior:contain;padding:22px 20px 22px;border-radius:28px;background:#fff;color:#2b2440;',
'box-shadow:0 -10px 50px rgba(0,0,0,.3);transform:translateY(40px);transition:transform .32s cubic-bezier(.2,.9,.3,1)}',
'.px-ov.in .px-sheet{transform:none}',
'.px-sheet h2{margin:0 36px 14px 0;font-size:20px;line-height:1.35;font-weight:900}',
'.px-sheet ul{margin:0;padding:0;list-style:none;display:grid;gap:10px}',
'.px-sheet li{position:relative;padding:12px 14px 12px 40px;border-radius:16px;background:#f6f2fc;font-size:14.5px;line-height:1.6;font-weight:700}',
'.px-sheet li::before{content:"✓";position:absolute;left:14px;top:12px;font-weight:900;color:#2f9e6e}',
'.px-sheet .px-since{margin:14px 2px 0;font-size:13.5px;font-weight:800;color:#6a5a78}',
'.px-x{position:absolute;right:12px;top:12px;width:44px;height:44px;border:0;border-radius:50%;background:#f1ecfb;color:#4a3d58;font-size:18px;font-weight:900;cursor:pointer}',
'.px-btn{display:flex;align-items:center;justify-content:center;width:100%;min-height:50px;margin-top:14px;padding:12px 16px;border:0;border-radius:16px;background:#2b2440;color:#fff;font-weight:900;font-size:15px;line-height:1.3;font-family:inherit;cursor:pointer}',
'.px-btn.alt{background:#e8f6ee;color:#14633f}',
'.px-state{margin:10px 2px 0;font-size:13px;font-weight:800;color:#6a5a78}',
'.px-toast{position:fixed;left:50%;bottom:22px;z-index:2147483300;max-width:min(92vw,420px);padding:12px 18px;border-radius:16px;background:#2b2440;color:#fff;font-weight:800;font-size:14px;line-height:1.45;font-family:inherit;',
'transform:translate(-50%,20px);opacity:0;transition:transform .3s ease,opacity .3s ease;text-align:center}',
'.px-toast.in{transform:translate(-50%,0);opacity:1}',
'.px-demo{position:fixed;left:0;right:0;top:8px;z-index:2147483300;width:fit-content;max-width:calc(100% - 24px);margin:0 auto;text-align:center;padding:7px 14px;border-radius:999px;background:#ffd54a;color:#4a3500;font-weight:900;font-size:12.5px;line-height:1.3;font-family:inherit;box-shadow:0 6px 16px rgba(0,0,0,.2)}',
'.px-hs{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:8px 14px;margin:-14px 0 26px;padding:12px 16px;border-radius:20px;background:#fffdf8;border:1.5px solid rgba(35,44,72,.10);',
'color:#232c48;font-weight:800;font-size:14px;line-height:1.4;font-family:inherit;box-shadow:0 8px 24px rgba(35,44,72,.06)}',
'.px-hs b{font-weight:900;font-size:16px}',
'.px-hs .px-sep{opacity:.3}',
'.px-world{margin-top:18px;padding:24px;border-radius:22px;background:#fffdf8;border:1.5px solid rgba(35,44,72,.10);box-shadow:0 10px 30px rgba(35,44,72,.06);color:#1b2138}',
'.px-world h2{margin:0;font-size:clamp(20px,3vw,27px);letter-spacing:-.02em}',
'.px-world .px-lead{margin:6px 0 0;font-size:14px;font-weight:700;color:#6d7593}',
'.px-big{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:12px;margin:18px 0 6px}',
'.px-big div{padding:14px 12px;border-radius:18px;background:#f3f1ea;text-align:center}',
'.px-big b{display:block;font-size:clamp(22px,4vw,30px);font-weight:900;letter-spacing:-.02em;color:#232c48}',
'.px-big small{display:block;margin-top:4px;font-size:12.5px;font-weight:800;color:#6d7593}',
'.px-h3{margin:20px 0 10px;font-size:15px;font-weight:900;color:#232c48}',
'.px-bars{display:grid;gap:8px;margin:0;padding:0;list-style:none}',
'.px-bars li{display:grid;grid-template-columns:30px minmax(0,1fr) auto;align-items:center;gap:10px;font-size:14px;font-weight:800}',
'.px-bars .px-fl{font-size:22px;line-height:1}',
'.px-bar{position:relative;height:30px;border-radius:10px;background:#eef2fb;overflow:hidden}',
'.px-bar i{position:absolute;left:0;top:0;bottom:0;border-radius:10px;background:linear-gradient(90deg,#567cf0,#8b6de8);transform-origin:left;animation:px-grow .9s cubic-bezier(.2,.9,.3,1) both}',
'.px-bar span{position:relative;display:block;padding:0 10px;line-height:30px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:#1b2138;mix-blend-mode:normal}',
'@keyframes px-grow{from{transform:scaleX(0)}to{transform:scaleX(1)}}',
'.px-bars em{font-style:normal;color:#232c48;font-weight:900}',
'.px-chips{display:flex;flex-wrap:wrap;gap:8px}',
'.px-chips .px-chip{min-height:32px;padding:5px 12px;font-size:13px}',
'.px-pop{margin:26px 0 0}',
'.px-pop h2{margin:0 0 12px;font-size:clamp(20px,3vw,27px);letter-spacing:-.02em}',
'.px-pop ol{display:flex;gap:12px;margin:0 -16px;padding:4px 16px 14px;list-style:none;overflow-x:auto;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch}',
'.px-pop li{flex:0 0 min(78%,260px);scroll-snap-align:start}',
'.px-pop a{display:grid;gap:10px;height:100%;padding:12px;border-radius:20px;background:#fffdf8;border:1.5px solid rgba(35,44,72,.10);box-shadow:0 8px 22px rgba(35,44,72,.07);color:#1b2138;text-decoration:none}',
'.px-pop .px-th{aspect-ratio:1/1;border-radius:14px;background:#e9e4d8 center/cover no-repeat}',
'.px-pop .px-tt{font-size:14.5px;line-height:1.4;font-weight:800;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}',
'.px-pop .px-nn{font-size:12.5px;font-weight:900;color:#6d7593}',
'.px-pop .px-rk{display:inline-grid;place-items:center;width:26px;height:26px;margin-right:6px;border-radius:50%;background:#ffc42e;color:#4a2c00;font-size:13px;font-weight:900}',
'.post-meta .px-n{white-space:nowrap}',
'html[data-theme="dark"] .px-chip,html[data-theme="dark"] .px-heart{background:#22242f;border-color:rgba(255,255,255,.12);color:#e6e1ee}',
'html[data-theme="dark"] .px-chip b{color:#fff}',
'html[data-theme="dark"] .px-end{background:linear-gradient(135deg,#22242f,#2a2233);border-color:rgba(255,255,255,.08);color:#ece8f3}',
'html[data-theme="dark"] .px-end h3{color:#f4f0fa}html[data-theme="dark"] .px-end p,html[data-theme="dark"] .px-sum{color:#b3aac4}',
'html[data-theme="dark"] .px-sheet{background:#22242f;color:#ece8f3}html[data-theme="dark"] .px-sheet li{background:#2a2c39}',
'html[data-theme="dark"] .px-x{background:#33364a;color:#ece8f3}html[data-theme="dark"] .px-link{color:#b9a8ff}',
'html[data-theme="dark"] :is(.px-hs,.px-world,.px-pop a){background:#22242f;border-color:rgba(255,255,255,.1);color:#ece8f3}',
'html[data-theme="dark"] :is(.px-world h2,.px-big b,.px-h3,.px-bars em,.px-bar span){color:#f4f0fa}',
'html[data-theme="dark"] .px-big div{background:#2a2c39}html[data-theme="dark"] .px-bar{background:#2a2c39}',
'html[data-theme="dark"] :is(.px-world .px-lead,.px-big small,.px-pop .px-nn){color:#b3aac4}',
'html[dir="rtl"] .px-bar i{transform-origin:right;left:auto;right:0}',
'@media (max-width:420px){.px-chip{padding:6px 11px;font-size:12.5px}.px-world{padding:20px 16px}.px-heart{width:100%}}',
'@media (prefers-reduced-motion:reduce){html:not([data-motion="on"]) :is(.px-strip,.px-ov,.px-sheet,.px-toast,.px-heart){transition:none}html:not([data-motion="on"]) :is(.px-dot,.px-bar i,.px-heart.pop .px-heart-ic,.px-burst){animation:none}}'
].join('\n');
function addCss() {
if (qs('#px-css')) return;
var s = el('style'); s.id = 'px-css'; s.textContent = css; (doc.head || root).appendChild(s);
}
var HEART = '<svg class="px-heart-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>';
var toastTimer = 0;
function toast(msg) {
var x = qs('.px-toast') || el('div', 'px-toast'); x.setAttribute('role', 'status'); x.setAttribute('translate', 'no');
x.textContent = msg; if (!x.parentNode) doc.body.appendChild(x);
void x.offsetWidth; x.classList.add('in'); clearTimeout(toastTimer);
toastTimer = setTimeout(function () { x.classList.remove('in'); }, 2600);
}
px.toast = toast;
var lastFocus = null;
function openSheet(title, body) {
closeSheet(true);
lastFocus = doc.activeElement;
var ov = el('div', 'px-ov'); ov.setAttribute('translate', 'no');
var sh = el('div', 'px-sheet'); sh.setAttribute('role', 'dialog'); sh.setAttribute('aria-modal', 'true'); sh.tabIndex = -1;
var h = el('h2'); h.id = 'px-sheet-h'; h.textContent = title; sh.setAttribute('aria-labelledby', 'px-sheet-h');
var x = el('button', 'px-x', '✕'); x.type = 'button'; x.setAttribute('aria-label', t('close'));
sh.appendChild(h); sh.appendChild(x); sh.appendChild(body); ov.appendChild(sh); doc.body.appendChild(ov);
root.style.overflow = 'hidden';
function onKey(e) {
if (e.key === 'Escape') { closeSheet(); return; }
if (e.key !== 'Tab') return;
var f = qsa('button,a[href],[tabindex]:not([tabindex="-1"])', sh); if (!f.length) return;
var first = f[0], last = f[f.length - 1];
if (e.shiftKey && doc.activeElement === first) { e.preventDefault(); last.focus(); }
else if (!e.shiftKey && doc.activeElement === last) { e.preventDefault(); first.focus(); }
}
ov.__key = onKey; doc.addEventListener('keydown', onKey);
x.addEventListener('click', function () { closeSheet(); });
ov.addEventListener('click', function (e) { if (e.target === ov) closeSheet(); });
requestAnimationFrame(function () { ov.classList.add('in'); sh.focus(); });
}
function closeSheet(now) {
var ov = qs('.px-ov'); if (!ov) return;
doc.removeEventListener('keydown', ov.__key); root.style.overflow = '';
if (now || reduce) ov.remove(); else { ov.classList.remove('in'); setTimeout(function () { ov.remove(); }, 260); }
if (lastFocus && lastFocus.focus) try { lastFocus.focus(); } catch (e) {}
}
px.sheet = { open: openSheet, close: closeSheet };
function explainer() {
var wrap = el('div');
var ul = el('ul'); ['b1', 'b2', 'b3', 'b4', 'b5'].forEach(function (k) { ul.appendChild(el('li', '', esc(t(k)))); });
ul.appendChild(el('li', '', esc(t('dnt'))));
wrap.appendChild(ul);
var since = (state.site && state.site.since) || cfg.since;
if (since) wrap.appendChild(el('p', 'px-since', esc(fill(t('since'), { d: dateText(since) }))));
wrap.appendChild(el('p', 'px-since', esc(t('start'))));
var btn = el('button', 'px-btn' + (blocked() ? ' alt' : '')); btn.type = 'button';
var st = el('p', 'px-state');
function paint() { btn.textContent = blocked() ? t('onBtn') : t('offBtn'); btn.classList.toggle('alt', blocked()); st.textContent = blocked() ? t('offNow') : t('onNow'); }
paint();
btn.addEventListener('click', function () {
if (blocked()) { put(KEY_OFF, null); toast(t('onToast')); } else { put(KEY_OFF, '1'); toast(t('offToast')); }
paint(); render();
});
wrap.appendChild(btn); wrap.appendChild(st);
return wrap;
}
function openExplainer() { openSheet(t('howTitle'), explainer()); }
px.explain = openExplainer;
var state = { post: null, site: null };
px.state = state;
function min(k, d) { if (blocked()) return 1; var v = cfg && cfg[k]; return typeof v === 'number' ? v : d; }
function emit() { try { doc.dispatchEvent(new CustomEvent('px:update', { detail: state })); } catch (e) {} }
var strip = null;
function ensureStrip() {
if (strip && strip.isConnected) return strip;
var anchor = qs('main .post-tags') || qs('main h1');
if (!anchor) return null;
strip = el('div', 'px-strip'); strip.setAttribute('translate', 'no'); strip.setAttribute('role', 'group');
anchor.parentNode.insertBefore(strip, anchor.nextSibling);
return strip;
}
function chip(inner, tag, cls) { var c = el(tag || 'span', 'px-chip' + (cls ? ' ' + cls : ''), inner); return c; }
function renderStrip() {
var p = state.post; if (!p) return;
var parts = [];
var s = ensureStrip(); if (!s) return;
s.innerHTML = '';
if (p.v >= min('minViews', 10)) parts.push(chip('👀 <b>' + esc(pat('viewsF', p.v)) + '</b>'));
if (p.l >= Math.max(1, min('minLikes', 1))) {
var b = chip(HEART + ' <b>' + esc(fmt(p.l)) + '</b>', 'button'); b.type = 'button';
b.setAttribute('aria-pressed', p.lk ? 'true' : 'false'); b.setAttribute('aria-label', t('likeAria') + ' (' + p.l + ')');
b.addEventListener('click', function () { toggleLike(b); });
parts.push(b);
}
if (p.nc >= min('minCountries', 3)) parts.push(chip('🌏 <b>' + esc(pat('countriesF', p.nc)) + '</b>'));
if (p.live && p.live.here >= min('minLive', 2)) parts.push(chip('<i class="px-dot"></i> <b>' + esc(pat('liveF', p.live.here)) + '</b>'));
if (!parts.length) { s.classList.remove('in'); return; }
var info = chip('ⓘ', 'button', 'px-info'); info.type = 'button'; info.setAttribute('aria-label', t('how'));
info.addEventListener('click', openExplainer); parts.push(info);
parts.forEach(function (c) { s.appendChild(c); });
requestAnimationFrame(function () { s.classList.add('in'); });
}
var endCard = null;
function ensureEnd() {
if (endCard && endCard.isConnected) return endCard;
var main = qs('main'); if (!main) return null;
var next = qs('a.next', main) || qs('a.draft-next', main);
endCard = el('section', 'px-end'); endCard.setAttribute('translate', 'no'); endCard.setAttribute('aria-label', t('endTitle'));
if (next) next.parentNode.insertBefore(endCard, next); else main.appendChild(endCard);
return endCard;
}
function renderEnd() {
var p = state.post; if (!p) return;
var c = ensureEnd(); if (!c) return;
var liked = !!p.lk;
var html_ = '<h3>' + esc(t('endTitle')) + '</h3><p>' + esc(t('endSub')) + '</p>' +
'<button type="button" class="px-heart" aria-pressed="' + (liked ? 'true' : 'false') + '">' + HEART +
'<span class="px-hl">' + esc(liked ? t('liked') : t('likeLabel')) + '</span>' +
(p.l >= 1 ? '<b class="px-hn">' + esc(fmt(p.l)) + '</b>' : '') + '</button>';
var bits = [];
if (p.v >= min('minViews', 10)) bits.push('👀 ' + esc(pat('viewsF', p.v)));
if (p.nc >= min('minCountries', 3)) bits.push('🌏 ' + esc(fill(t('fromWhere'), { n: fmt(p.nc) })));
if (bits.length) html_ += '<p class="px-sum">' + bits.join(' · ') + '</p>';
if (p.nc >= min('minCountries', 3) && p.cc && p.cc.length) {
html_ += '<div class="px-flags">' + p.cc.slice(0, 12).map(function (x) {
return '<span title="' + esc(country(x[0]) + ' ' + fmt(x[1])) + '" aria-label="' + esc(country(x[0])) + '">' + flag(x[0]) + '</span>';
}).join('') + '</div>';
}
html_ += '<button type="button" class="px-link">' + esc(t('how')) + '</button>';
c.innerHTML = html_;
var hb = qs('.px-heart', c); hb.addEventListener('click', function () { toggleLike(hb); });
qs('.px-link', c).addEventListener('click', openExplainer);
}
function burst(btn) {
if (reduce) return;
for (var i = 0; i < 7; i++) {
var b = doc.createElementNS('http://www.w3.org/2000/svg', 'svg'); b.setAttribute('viewBox', '0 0 24 24'); b.setAttribute('class', 'px-burst');
b.innerHTML = '<path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>';
var a = (Math.PI * 2 * i) / 7 - Math.PI / 2, r = 44 + (i % 3) * 10;
b.style.setProperty('--dx', Math.round(Math.cos(a) * r) + 'px'); b.style.setProperty('--dy', Math.round(Math.sin(a) * r) + 'px');
btn.appendChild(b); (function (n) { setTimeout(function () { n.remove(); }, 800); })(b);
}
}
var liking = false;
function toggleLike(btn) {
if (!cfg || !state.post || liking) return;
if (blocked()) { openExplainer(); return; }
var p = state.post, on = !p.lk, before = { l: p.l, lk: p.lk };
liking = true;
p.lk = on; p.l = Math.max(0, p.l + (on ? 1 : -1)); setLikedLocal(slug, on);
render();
var hb = qs('.px-heart'); if (on && hb) { hb.classList.add('pop'); burst(hb); setTimeout(function () { hb.classList.remove('pop'); }, 700); }
api('POST', '/v1/like', { p: slug, v: vid(), on: on }).then(function (r) {
liking = false;
if (r && r.ok && r.post) { state.post = r.post; render(); }
else if (r && r.e === 'limit') { toast(t('err')); }
}).catch(function () {
liking = false; p.l = before.l; p.lk = before.lk; setLikedLocal(slug, before.lk); render(); toast(t('err'));
});
}
function sumBy(a, k) { return (a || []).reduce(function (s, x) { return s + (x[k] || 0); }, 0); }
function renderHomeStrip() {
var s = state.site; if (!s) return;
var old = qs('.px-hs'); if (old) old.remove();
var ok = s.v >= min('minViews', 10) && s.nc >= min('minCountries', 3);
if (!ok) return;
var hero = qs('.hero'); if (!hero) return;
var b = el('div', 'px-hs'); b.setAttribute('translate', 'no');
var bits = ['🌍 <b>' + esc(pat('countriesF', s.nc)) + '</b>', '👀 <b>' + esc(pat('viewsF', s.v)) + '</b>'];
if (s.l >= 1) bits.push('<span style="color:#c2255c">♥</span> <b>' + esc(fmt(s.l)) + '</b>');
if (s.live && s.live.n >= min('minLive', 2)) bits.push('<i class="px-dot"></i> <b>' + esc(pat('liveF', s.live.n)) + '</b>');
b.innerHTML = bits.join(' <span class="px-sep">|</span> ');
hero.parentNode.insertBefore(b, hero.nextSibling);
}
function bars(list, total, n) {
var max = list.length ? list[0][1] : 1;
return '<ol class="px-bars">' + list.slice(0, n).map(function (x) {
return '<li><span class="px-fl" aria-hidden="true">' + flag(x[0]) + '</span><span class="px-bar"><i style="width:' + Math.max(4, Math.round(100 * x[1] / max)) + '%;opacity:.28"></i><span>' + esc(country(x[0])) + '</span></span><em>' + esc(fmt(x[1])) + '</em></li>';
}).join('') + '</ol>';
}
function renderWorld() {
var s = state.site; var old = qs('#px-world'); if (old) old.remove();
if (!s || s.v < min('minViews', 10) || s.nc < min('minCountries', 3)) return;
var after = qs('#goal'); if (!after) return;
var sec = el('section', 'px-world reveal'); sec.id = 'px-world'; sec.setAttribute('translate', 'no');
var h = '<h2>🌍 ' + esc(t('world')) + '</h2><p class="px-lead">' + esc(fill(t('since'), { d: dateText(s.since) })) + '</p>';
h += '<div class="px-big"><div><b>' + esc(fmt(s.nc)) + '</b><small>' + esc(t('countriesW')) + '</small></div>' +
'<div><b>' + esc(fmt(s.v)) + '</b><small>' + esc(t('allTime')) + ' · ' + esc(t('views')) + '</small></div>' +
'<div><b>' + esc(fmt(s.v7)) + '</b><small>' + esc(t('thisWeek')) + '</small></div>' +
'<div><b>' + esc(fmt(s.l)) + '</b><small>♥ ' + esc(t('likesWord')) + '</small></div></div>';
if (s.live && s.live.n >= 1) {
h += '<p class="px-sum" style="text-align:left"><i class="px-dot" style="display:inline-block;vertical-align:1px"></i> ' + esc(fill(t('nowReading'), { n: fmt(s.live.n) })) + ' ' +
(s.live.cc || []).slice(0, 8).map(function (x) { return flag(x[0]); }).join(' ') + '</p>';
}
h += '<h3 class="px-h3">' + esc(t('topCountries')) + '</h3>' + bars(s.cc, s.v, 8);
if (s.cc.length > 8) {
h += '<button type="button" class="px-link" data-more="1" style="padding-left:0">' + esc(fill(t('showAll'), { n: s.cc.length })) + '</button>';
}
if (s.lang && s.lang.length) {
h += '<h3 class="px-h3">' + esc(t('languages')) + '</h3><div class="px-chips">' + s.lang.slice(0, 10).map(function (x) {
return '<span class="px-chip">' + esc(langName(x[0])) + ' <b>' + esc(fmt(x[1])) + '</b></span>';
}).join('') + '</div>';
}
if (s.ref && s.ref.length) {
h += '<h3 class="px-h3">' + esc(t('arrive')) + '</h3><div class="px-chips">' + s.ref.slice(0, 8).map(function (x) {
return '<span class="px-chip">' + esc((L.ref && L.ref[x[0]]) || T.en.ref[x[0]] || x[0]) + ' <b>' + esc(fmt(x[1])) + '</b></span>';
}).join('') + '</div>';
}
if (s.dev && s.dev.length) {
h += '<h3 class="px-h3">' + esc(t('devices')) + '</h3><div class="px-chips">' + s.dev.map(function (x) {
return '<span class="px-chip">' + ({ phone: '📱', desktop: '💻', tablet: '📲' }[x[0]] || '') + ' ' + esc((L.dev && L.dev[x[0]]) || T.en.dev[x[0]] || x[0]) + ' <b>' + esc(fmt(x[1])) + '</b></span>';
}).join('') + '</div>';
}
h += '<a class="px-link px-dash" href="/stats/" style="padding-left:0;display:block">' + esc(t('dash')) + '</a>';
h += '<button type="button" class="px-link" data-how="1" style="padding-left:0">' + esc(t('how')) + '</button>';
sec.innerHTML = h;
after.parentNode.insertBefore(sec, after.nextSibling);
qs('[data-how]', sec).addEventListener('click', openExplainer);
var more = qs('[data-more]', sec);
if (more) more.addEventListener('click', function () {
var ol = qs('.px-bars', sec); ol.outerHTML = bars(s.cc, s.v, s.cc.length); more.remove();
});
sec.classList.add('in');
}
function renderPopular() {
var s = state.site; var old = qs('#px-pop'); if (old) old.remove();
var posts = window.POSTS || [];
if (!s || !s.top7 || s.top7.length < 3) return;
var by = {}; posts.forEach(function (q) { by[q.slug] = q; });
var items = s.top7.filter(function (x) { return by[x[0]]; }).slice(0, 8);
if (items.length < 3) return;
var target = qs('#posts'); if (!target) return;
var sec = el('section', 'px-pop'); sec.id = 'px-pop';
sec.innerHTML = '<h2 translate="no">🔥 ' + esc(t('popular')) + '</h2><ol>' + items.map(function (x, i) {
var q = by[x[0]];
return '<li><a href="' + esc(q.href) + '"><span class="px-th" style="background-image:url(' + esc(q.thumb) + ')"></span>' +
'<span class="px-tt"><span class="px-rk" translate="no">' + (i + 1) + '</span>' + esc(q.title) + '</span><span class="px-nn" translate="no">👀 ' + esc(fmt(x[1])) + '</span></a></li>';
}).join('') + '</ol>';
target.parentNode.insertBefore(sec, target);
}
function decorateFeed() {
var s = state.site; if (!s || !s.per) return;
var map = {}; s.per.forEach(function (x) { map[x[0]] = x; });
qsa('#feed a.post').forEach(function (a) {
if (a.__px) return; a.__px = 1;
var mm = /works\/([^\/]+)\//.exec(a.getAttribute('href') || ''); if (!mm) return;
var x = map[mm[1]]; if (!x || x[1] < min('minViews', 10)) return;
var meta = qs('.post-meta', a); if (!meta) return;
var sp = el('span', 'px-n', '👀 ' + esc(fmt(x[1])) + (x[2] >= 1 ? ' · ♥ ' + esc(fmt(x[2])) : '')); sp.setAttribute('translate', 'no');
meta.appendChild(sp);
});
}
function render() {
if (!cfg) return;
if (kind === 'post') { renderStrip(); renderEnd(); }
if (kind === 'home') { renderHomeStrip(); renderWorld(); renderPopular(); decorateFeed(); }
emit();
}
function refCategory() {
var r = doc.referrer; if (!r) return 'direct';
var h = ''; try { h = new URL(r).hostname.replace(/^www\./, ''); } catch (e) { return 'other'; }
if (h === loc.hostname.replace(/^www\./, '')) return 'direct';
if (/(^|\.)google\./.test(h)) return 'google';
if (/(^|\.)bing\.com$/.test(h)) return 'bing';
if (/(^|\.)yahoo\./.test(h)) return 'yahoo';
if (/^(t\.co|x\.com|twitter\.com)$/.test(h)) return 'x';
if (/(^|\.)(facebook|fb)\.com$|^l\.facebook\.com$/.test(h)) return 'facebook';
if (/instagram\.com$/.test(h)) return 'instagram';
if (/(^|\.)line\.me$|(^|\.)lin\.ee$/.test(h)) return 'line';
if (/(^|\.)(youtube\.com|youtu\.be)$/.test(h)) return 'youtube';
if (/github\.(com|io)$/.test(h)) return 'github';
if (/reddit\.com$/.test(h)) return 'reddit';
if (/hatena\./.test(h)) return 'hatena';
return 'other';
}
var lastActive = Date.now(), pingTimer = 0, counted = false;
['scroll', 'touchstart', 'mousemove', 'keydown', 'click'].forEach(function (e) {
addEventListener(e, function () { lastActive = Date.now(); }, { passive: true });
});
function mayCount() { return !cfg.demo && !blocked() && !dnt() && !navigator.webdriver; }
function startCounting() {
if (counted) return; counted = true;
var body = { p: slug, l: LANG, r: refCategory(), v: vid() };
api('POST', '/v1/hit', body).then(function (r) {
if (r && r.ok && r.post) { state.post = r.post; render(); }
}).catch(function () {});
clearInterval(pingTimer);
pingTimer = setInterval(function () {
if (doc.hidden || Date.now() - lastActive > 5 * 60000) return;
api('POST', '/v1/ping', { p: slug }).then(function (r) {
if (r && r.ok && r.live && state.post) { state.post.live = r.live; renderStrip(); }
}).catch(function () {});
}, 45000);
}
function whenReady(fn) {
function go() { setTimeout(fn, 1200); }
if (doc.visibilityState === 'visible') go();
else doc.addEventListener('visibilitychange', function once() { if (doc.visibilityState === 'visible') { doc.removeEventListener('visibilitychange', once); go(); } });
}
function start() {
addCss();
if (cfg.demo) { var d = el('div', 'px-demo', esc(t('demo'))); d.setAttribute('translate', 'no'); doc.body.appendChild(d); }
if (px.justToggled) toast(px.justToggled === 'off' ? t('offToast') : t('onToast'));
if (kind === 'post') {
var showOnly = function () { api('GET', '/v1/post?p=' + encodeURIComponent(slug) + '&v=' + vid()).then(function (r) { if (r && r.ok) { state.post = r.post; render(); } }).catch(function () {}); };
if (mayCount()) whenReady(startCounting); else showOnly();
} else if (kind === 'home') {
if (mayCount()) whenReady(function () { api('POST', '/v1/hit', { p: '_home', l: LANG, r: refCategory(), v: vid() }).catch(function () {}); });
var loadSite = function () {
api('GET', '/v1/stats').then(function (r) { if (r && r.ok) { state.site = r.site; render(); } }).catch(function () {});
};
loadSite();
var feed = qs('#feed');
if (feed && window.MutationObserver) new MutationObserver(function () { decorateFeed(); }).observe(feed, { childList: true });
}
}
function boot() {
if (!kind) return;
var cfgUrl = '/assets/stats-config.json';
var go = function (c) {
cfg = c || {};
var hosts = cfg.hosts || ['15-second-blog.com', 'www.15-second-blog.com'];
if (demo) { cfg = Object.assign({}, cfg, { demo: true, enabled: true, endpoint: 'demo', minViews: 0, minLikes: 1, minCountries: 1, minLive: 1 }); }
else {
var dev = local && params.get('pxstats');
if (dev) {
cfg = Object.assign({}, cfg, { enabled: true, endpoint: dev });
var pm = params.get('pxmin');                      // 手元のテスト用：しきい値を下げる
if (pm !== null && !isNaN(+pm)) cfg = Object.assign(cfg, { minViews: +pm, minLikes: +pm, minCountries: +pm, minLive: +pm });
}
else if (hosts.indexOf(loc.hostname) < 0) return;          // 本番のドメイン以外では数えない・出さない
}
if (!cfg.enabled || !cfg.endpoint) return;                   // まだつながっていない：何も出さない
cfg.endpoint = String(cfg.endpoint).replace(/\/+$/, '');
if (doc.readyState === 'loading') doc.addEventListener('DOMContentLoaded', start); else start();
};
if (demo) { go({}); return; }
fetch(cfgUrl, { credentials: 'same-origin' }).then(function (r) { return r.ok ? r.json() : null; }).then(go).catch(function () {});
}
px.like = { toggle: function () { toggleLike(); }, state: function () { return state.post; } };
px.refresh = render;
boot();
})();
