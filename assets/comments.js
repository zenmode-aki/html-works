(function () {
'use strict';
var px = window.__px;
if (!px || !px.cm || window.__pxComments) return;
window.__pxComments = 1;
var C = px.cm, doc = document;
var LANG = C.lang, esc = C.esc, flag = C.flag, country = C.country, langName = C.langName;
var KEY_NICK = 'pengesso-cm-nick', KEY_HOME = 'pengesso-cm-home';
function get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
function put(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
var T = {
en: { title: '💬 Leave a note', sub: 'Comments appear 3 days later. An AI reads each one first. If the words are a bit sharp, it says them more gently. Questions for the owner go only to the owner.',
none: 'No comments yet. Be the first?', toAll: '💬 For everyone', toOwner: '📮 Only to the owner',
toAllHint: 'Shown on this page after 3 days.', toOwnerHint: 'Not shown on the page. Only the owner reads it.',
ph: 'Write something… (up to 500 characters)', phOwner: 'A question or a wish for the owner…', nick: 'Name (optional)', nickPh: 'A penguin with no name',
home: 'Where you live', homeNone: 'Rather not say', reading: 'Reading in', send: 'Send', sending: 'Sending…',
sentAll: 'Thank you! 💌 It will appear here in about 3 days.', sentOwner: 'Thank you! 📮 It went to the owner. It will not be shown on the page.',
mine: 'Your notes on this post', wait: '⏳ Waiting · about {d} more days', waitSoon: '⏳ Waiting · soon', ok: '✅ Shown', inbox: '📮 Delivered to the owner',
soft: '🪄 Said more gently by AI', anon: 'A penguin with no name', err: 'Could not send. Please try again later.', limit: 'That is a lot for today. Please try again tomorrow.',
short: 'A little more, please.', long: 'Up to 500 characters, please.', more: 'Show all {n}', rules: 'No links, no ads, no names of other people.' },
ja: { title: '💬 ひとこと、どうぞ', sub: 'コメントは3日後に出ます。その前に AI が読みます。言い方が少しきついときは、やさしい言い方に直して出します。ご主人への質問は、ご主人だけが読みます。',
none: 'まだコメントはありません。最初のひとことを、どうぞ。', toAll: '💬 みんなに', toOwner: '📮 ご主人だけに',
toAllHint: '3日後に、このページに出ます。', toOwnerHint: 'ページには出ません。ご主人だけが読みます。',
ph: 'ひとこと、どうぞ…（500文字まで）', phOwner: 'ご主人への質問や、書いてほしいこと…', nick: '名前（なくてもいい）', nickPh: '名無しのペンギン',
home: '住んでいる国', homeNone: '書かない', reading: '読んでいる言語', send: '送る', sending: '送っています…',
sentAll: 'ありがとうございます！💌 3日くらいで、ここに出ます。', sentOwner: 'ありがとうございます！📮 ご主人に届けました。ページには出ません。',
mine: 'この記事に書いたもの', wait: '⏳ 公開待ち・あと{d}日くらい', waitSoon: '⏳ 公開待ち・もうすぐ', ok: '✅ 公開されました', inbox: '📮 ご主人に届きました',
soft: '🪄 AI がやさしく言い換えました', anon: '名無しのペンギン', err: 'うまく送れませんでした。少したってから、もう一度どうぞ。', limit: '今日はたくさん書いてもらいました。また明日どうぞ。',
short: 'もう少しだけ、どうぞ。', long: '500文字までで、お願いします。', more: '{n}件ぜんぶ見る', rules: 'リンク・宣伝・ほかの人の名前は書かないでください。' },
ko: { title: '💬 한마디 남겨 주세요', sub: '댓글은 3일 뒤에 보여요. 그 전에 AI가 읽어요. 말투가 조금 날카로우면 부드럽게 바꿔서 보여 줘요. 주인에게 하는 질문은 주인만 읽어요.',
none: '아직 댓글이 없어요. 첫 한마디를 남겨 주세요.', toAll: '💬 모두에게', toOwner: '📮 주인에게만',
toAllHint: '3일 뒤에 이 페이지에 보여요.', toOwnerHint: '페이지에는 안 보여요. 주인만 읽어요.',
ph: '한마디 남겨 주세요… (500자까지)', phOwner: '주인에게 질문이나 바라는 것…', nick: '이름 (없어도 돼요)', nickPh: '이름 없는 펭귄',
home: '사는 나라', homeNone: '안 쓸래요', reading: '읽는 언어', send: '보내기', sending: '보내는 중…',
sentAll: '고마워요! 💌 3일쯤 뒤에 여기에 보여요.', sentOwner: '고마워요! 📮 주인에게 전했어요. 페이지에는 안 보여요.',
mine: '이 글에 쓴 것', wait: '⏳ 공개 대기 · {d}일쯤 남음', waitSoon: '⏳ 공개 대기 · 곧', ok: '✅ 공개됐어요', inbox: '📮 주인에게 전달됐어요',
soft: '🪄 AI가 부드럽게 바꿨어요', anon: '이름 없는 펭귄', err: '보내지 못했어요. 조금 뒤에 다시 해 주세요.', limit: '오늘은 많이 써 주셨어요. 내일 또 와 주세요.',
short: '조금만 더 써 주세요.', long: '500자까지 부탁해요.', more: '{n}개 모두 보기', rules: '링크·광고·다른 사람의 이름은 쓰지 말아 주세요.' },
zh: { title: '💬 留下一句话吧', sub: '评论会在3天后显示。在那之前 AI 会先读一遍。如果语气有点重，会改成温和的说法再显示。给主人的问题只有主人会看。',
none: '还没有评论。来留下第一句话吧。', toAll: '💬 给大家', toOwner: '📮 只给主人',
toAllHint: '3天后显示在这个页面。', toOwnerHint: '不会显示在页面上，只有主人会看。',
ph: '写点什么吧…（最多500字）', phOwner: '想问主人的问题或想看的内容…', nick: '名字（可以不填）', nickPh: '无名企鹅',
home: '居住的国家', homeNone: '不填', reading: '阅读语言', send: '发送', sending: '发送中…',
sentAll: '谢谢！💌 大约3天后会显示在这里。', sentOwner: '谢谢！📮 已送到主人那里，不会显示在页面上。',
mine: '你在这篇写的', wait: '⏳ 等待公开 · 大约还有{d}天', waitSoon: '⏳ 等待公开 · 快了', ok: '✅ 已公开', inbox: '📮 已送到主人那里',
soft: '🪄 AI 改成了温和的说法', anon: '无名企鹅', err: '没能发送，请稍后再试。', limit: '今天已经写了很多啦，明天再来吧。',
short: '再多写一点吧。', long: '请写在500字以内。', more: '查看全部 {n} 条', rules: '请不要写链接、广告或别人的名字。' },
'zh-Hant': { title: '💬 留下一句話吧', sub: '留言會在3天後顯示。在那之前 AI 會先讀一遍。如果語氣有點重，會改成溫和的說法再顯示。給主人的問題只有主人會看。',
none: '還沒有留言。來留下第一句話吧。', toAll: '💬 給大家', toOwner: '📮 只給主人',
toAllHint: '3天後顯示在這個頁面。', toOwnerHint: '不會顯示在頁面上，只有主人會看。',
ph: '寫點什麼吧…（最多500字）', phOwner: '想問主人的問題或想看的內容…', nick: '名字（可以不填）', nickPh: '無名企鵝',
home: '居住的國家', homeNone: '不填', reading: '閱讀語言', send: '送出', sending: '送出中…',
sentAll: '謝謝！💌 大約3天後會顯示在這裡。', sentOwner: '謝謝！📮 已送到主人那裡，不會顯示在頁面上。',
mine: '你在這篇寫的', wait: '⏳ 等待公開 · 大約還有{d}天', waitSoon: '⏳ 等待公開 · 快了', ok: '✅ 已公開', inbox: '📮 已送到主人那裡',
soft: '🪄 AI 改成了溫和的說法', anon: '無名企鵝', err: '沒能送出，請稍後再試。', limit: '今天已經寫了很多啦，明天再來吧。',
short: '再多寫一點吧。', long: '請寫在500字以內。', more: '查看全部 {n} 則', rules: '請不要寫連結、廣告或別人的名字。' }
};
var L = T[LANG] || T.en;
function t(k, o) { var s = L[k] != null ? L[k] : T.en[k]; return o ? String(s).replace(/\{(\w+)\}/g, function (m, x) { return o[x] != null ? o[x] : m; }) : s; }
var HOMES = ['JP', 'KR', 'TW', 'CN', 'HK', 'PH', 'MY', 'SG', 'TH', 'VN', 'ID', 'IN', 'PK', 'BD', 'NP', 'LK', 'US', 'CA', 'MX', 'BR', 'AR', 'CL', 'CO', 'PE',
'GB', 'IE', 'FR', 'DE', 'NL', 'BE', 'CH', 'AT', 'IT', 'ES', 'PT', 'SE', 'NO', 'DK', 'FI', 'PL', 'CZ', 'RO', 'GR', 'UA', 'RU', 'TR',
'AE', 'SA', 'QA', 'EG', 'IL', 'IR', 'NG', 'KE', 'ZA', 'AU', 'NZ'];
var READ = ['en', 'ja', 'ko', 'zh', 'zh-Hant', 'es', 'fr', 'de', 'pt', 'id', 'vi', 'th', 'fil', 'ms', 'hi', 'ar', 'ru'];
function guessHome() {
var saved = get(KEY_HOME);
if (saved !== null) return saved;
var langs = navigator.languages || [navigator.language || ''];
for (var i = 0; i < langs.length; i++) { var m = /-([A-Z]{2})$/i.exec(langs[i] || ''); if (m && HOMES.indexOf(m[1].toUpperCase()) >= 0) return m[1].toUpperCase(); }
return '';
}
var css = [
'.cm{margin:22px 0 8px;padding:22px 20px 20px;border-radius:26px;background:#fff;border:1.5px solid rgba(35,44,72,.08);box-shadow:0 10px 30px rgba(35,44,72,.06)}',
'.cm h3{margin:0 0 6px;font-size:20px;font-weight:900;color:#232c48}',
'.cm .cm-sub{margin:0 0 16px;font-size:13.5px;line-height:1.7;font-weight:700;color:#5d6280}',
'.cm-list{display:grid;gap:10px;margin:0 0 18px;padding:0;list-style:none}',
'.cm-item{display:grid;grid-template-columns:38px 1fr;gap:10px;align-items:start;animation:cm-in .45s ease both}',
'.cm-av{display:grid;place-items:center;width:38px;height:38px;border-radius:50%;background:#f3effc;font-size:20px}',
'.cm-bub{position:relative;padding:10px 14px 11px;border-radius:6px 18px 18px 18px;background:#f7f4ff;font-size:15px;line-height:1.7;font-weight:700;color:#2b2f45;overflow-wrap:anywhere;white-space:pre-wrap}',
'.cm-who{display:flex;flex-wrap:wrap;gap:4px 8px;align-items:center;margin-bottom:2px;font-size:12px;font-weight:900;color:#6b6585;white-space:normal}',
'.cm-who .cm-lang{padding:1px 7px;border-radius:999px;background:#fff;border:1px solid rgba(35,44,72,.1);font-size:11px}',
'.cm-soft{display:inline-block;margin-top:6px;padding:2px 9px;border-radius:999px;background:#fff6dc;color:#8a6200;font-size:11.5px;font-weight:900;white-space:normal}',
'.cm-none{margin:0 0 16px;padding:14px 16px;border-radius:16px;background:#faf8f3;font-size:14px;font-weight:800;color:#6b6585;text-align:center}',
'.cm-more{display:block;margin:-6px auto 16px;padding:8px 16px;border:0;border-radius:999px;background:#f3effc;color:#5b45c9;font:inherit;font-size:13px;font-weight:900;cursor:pointer}',
'.cm-mine{margin:0 0 16px;padding:12px 14px;border-radius:16px;background:#f2fbf6;border:1.5px dashed rgba(34,139,94,.25)}',
'.cm-mine b{display:block;margin-bottom:6px;font-size:12.5px;font-weight:900;color:#1f7a52}',
'.cm-mine div{display:flex;flex-wrap:wrap;gap:4px 10px;align-items:baseline;padding:4px 0;font-size:13.5px;font-weight:700;color:#2b2f45}',
'.cm-mine div q{flex:1 1 180px;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;quotes:none}',
'.cm-mine div span{font-size:12px;font-weight:900;color:#5d6280;white-space:nowrap}',
'.cm-seg{display:grid;grid-template-columns:1fr 1fr;gap:6px;padding:5px;border-radius:999px;background:#f1eef8;margin-bottom:6px}',
'.cm-seg button{min-height:44px;border:0;border-radius:999px;background:transparent;color:#5d6280;font:inherit;font-size:14px;font-weight:900;cursor:pointer;transition:background .2s,color .2s,box-shadow .2s}',
'.cm-seg button[aria-pressed="true"]{background:#fff;color:#232c48;box-shadow:0 2px 10px rgba(35,44,72,.12)}',
'.cm-hint{margin:0 4px 10px;font-size:12.5px;font-weight:800;color:#6b6585}',
'.cm textarea,.cm input,.cm select{box-sizing:border-box;width:100%;border:1.5px solid rgba(35,44,72,.14);border-radius:16px;background:#fffdf8;color:#232c48;font:inherit;font-size:16px;font-weight:700}',
'.cm textarea{min-height:110px;padding:12px 14px;line-height:1.7;resize:vertical}',
'.cm textarea:focus,.cm input:focus,.cm select:focus{outline:3px solid rgba(139,109,232,.35);border-color:#8b6de8}',
'.cm-count{margin:4px 6px 0;text-align:right;font-size:11.5px;font-weight:900;color:#8a86a0}',
'.cm-count.over{color:#d23c6a}',
'.cm-row{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:10px}',
'.cm-row label{display:grid;gap:4px;font-size:12px;font-weight:900;color:#5d6280}',
'.cm-row .cm-nick{grid-column:1/-1}',
'.cm input,.cm select{min-height:46px;padding:8px 12px}',
'.cm select{-webkit-appearance:none;appearance:none;padding-right:34px;text-overflow:ellipsis;background-image:url("data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 12 8%27%3E%3Cpath d=%27M1 1l5 5 5-5%27 fill=%27none%27 stroke=%27%238b6de8%27 stroke-width=%272.4%27 stroke-linecap=%27round%27 stroke-linejoin=%27round%27/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 13px center;background-size:12px 8px}',
'.cm-hp{position:absolute!important;left:-9999px!important;width:1px;height:1px;overflow:hidden}',
'.cm-foot{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:10px;margin-top:14px}',
'.cm-rules{flex:1 1 200px;margin:0;font-size:11.5px;font-weight:800;color:#8a86a0;line-height:1.6}',
'.cm-send{min-height:50px;padding:10px 28px;border:0;border-radius:999px;background:#8b6de8;color:#fff;font:inherit;font-size:16px;font-weight:900;cursor:pointer;box-shadow:0 5px 0 #6a50c9;transition:transform .12s,box-shadow .12s}',
'.cm-send:active{transform:translateY(4px);box-shadow:0 1px 0 #6a50c9}',
'.cm-send[disabled]{opacity:.55;cursor:default}',
'.cm-msg{margin:12px 0 0;padding:12px 14px;border-radius:14px;background:#f2fbf6;color:#1f7a52;font-size:14px;font-weight:900}',
'.cm-msg.bad{background:#fff0f3;color:#b52a55}',
'@keyframes cm-in{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}',
'@media (max-width:420px){.cm{padding:18px 14px 16px;border-radius:22px}.cm-row{gap:8px}.cm-send{width:100%}}',
'@media (prefers-reduced-motion:reduce){.cm-item{animation:none}.cm-seg button,.cm-send{transition:none}}',
'html[data-theme="dark"] .cm{background:#1d1f29;border-color:rgba(255,255,255,.08)}',
'html[data-theme="dark"] .cm h3{color:#f2eefc}html[data-theme="dark"] .cm .cm-sub,html[data-theme="dark"] .cm-hint,html[data-theme="dark"] .cm-row label{color:#b8b3cc}',
'html[data-theme="dark"] .cm-bub{background:#2a2540;color:#ece8f8}html[data-theme="dark"] .cm-who{color:#c4bde0}html[data-theme="dark"] .cm-who .cm-lang{background:#1d1f29;border-color:#3a3550}',
'html[data-theme="dark"] .cm-av{background:#2a2540}html[data-theme="dark"] .cm-none{background:#22242f;color:#b8b3cc}',
'html[data-theme="dark"] .cm-mine{background:#1c2a24;border-color:rgba(120,220,170,.25)}html[data-theme="dark"] .cm-mine b{color:#8fe0b8}html[data-theme="dark"] .cm-mine div,html[data-theme="dark"] .cm-mine div span{color:#d8f2e5}',
'html[data-theme="dark"] .cm-seg{background:#262838}html[data-theme="dark"] .cm-seg button{color:#b8b3cc}html[data-theme="dark"] .cm-seg button[aria-pressed="true"]{background:#3a3552;color:#fff}',
'html[data-theme="dark"] .cm textarea,html[data-theme="dark"] .cm input,html[data-theme="dark"] .cm select{background:#151720;color:#ece8f8;border-color:#3a3550}',
'html[data-theme="dark"] .cm-more{background:#2a2540;color:#cfc2ff}html[data-theme="dark"] .cm-soft{background:#3a3010;color:#ffd77a}',
'html[data-theme="dark"] .cm-msg{background:#1c2a24;color:#8fe0b8}html[data-theme="dark"] .cm-msg.bad{background:#3a1c26;color:#ff9fb8}'
].join('');
var box = null, data = { pub: [], mine: [], hold: 3 }, mode = 'c', showAll = false, sending = false;
function ago(ms) { var d = Math.ceil((ms + 3 * 86400000 - Date.now()) / 86400000); return d; }
function dateOf(ms) { try { return new Intl.DateTimeFormat(LANG, { month: 'short', day: 'numeric' }).format(new Date(ms)); } catch (e) { return ''; } }
function renderList() {
var pub = data.pub || [];
var html = '';
if (!pub.length) html += '<p class="cm-none">' + esc(t('none')) + '</p>';
else {
var list = showAll ? pub : pub.slice(0, 5);
html += '<ul class="cm-list">' + list.map(function (c) {
var who = esc(c.n || t('anon'));
var meta = '<span>' + who + '</span>' + (c.h ? '<span title="' + esc(country(c.h)) + '">' + flag(c.h) + ' ' + esc(country(c.h)) + '</span>' : '') +
(c.l ? '<span class="cm-lang">' + esc(langName(c.l)) + '</span>' : '') + (c.at ? '<span>' + esc(dateOf(c.at)) + '</span>' : '');
return '<li class="cm-item"><span class="cm-av" aria-hidden="true">' + (c.h ? flag(c.h) : '🐧') + '</span><div class="cm-bub"><div class="cm-who">' + meta + '</div>' +
esc(c.t) + (c.soft ? '<br><span class="cm-soft">' + esc(t('soft')) + '</span>' : '') + '</div></li>';
}).join('') + '</ul>';
if (!showAll && pub.length > 5) html += '<button type="button" class="cm-more">' + esc(t('more', { n: pub.length })) + '</button>';
}
var mine = data.mine || [];
if (mine.length) {
html += '<div class="cm-mine"><b>' + esc(t('mine')) + '</b>' + mine.slice(0, 5).map(function (m) {
var s = m.st === 'inbox' ? t('inbox') : m.st === 'ok' ? t('ok') : (ago(m.at) > 0 ? t('wait', { d: ago(m.at) }) : t('waitSoon'));
return '<div><q>' + esc(m.t) + '</q><span>' + esc(s) + '</span></div>';
}).join('') + '</div>';
}
var wrap = box.querySelector('.cm-body');
wrap.innerHTML = html;
var more = wrap.querySelector('.cm-more');
if (more) more.addEventListener('click', function () { showAll = true; renderList(); });
}
function options(list, sel, labelOf, none) {
var out = none != null ? '<option value="">' + esc(none) + '</option>' : '';
var named = list.map(function (v) { return [v, labelOf(v)]; });
named.sort(function (a, b) { return a[1].localeCompare(b[1], LANG); });
return out + named.map(function (x) { return '<option value="' + esc(x[0]) + '"' + (x[0] === sel ? ' selected' : '') + '>' + esc(x[1]) + '</option>'; }).join('');
}
function build(anchor) {
var st = doc.createElement('style'); st.textContent = css; doc.head.appendChild(st);
box = doc.createElement('section');
box.className = 'cm'; box.id = 'comments'; box.setAttribute('translate', 'no'); box.setAttribute('aria-label', t('title'));
var home = guessHome(), readL = READ.indexOf(LANG) >= 0 ? LANG : 'en';
box.innerHTML = '<h3>' + esc(t('title')) + '</h3><p class="cm-sub">' + esc(t('sub')) + '</p><div class="cm-body"></div>' +
'<form class="cm-form" novalidate>' +
'<div class="cm-seg" role="group"><button type="button" data-k="c" aria-pressed="true">' + esc(t('toAll')) + '</button><button type="button" data-k="q" aria-pressed="false">' + esc(t('toOwner')) + '</button></div>' +
'<p class="cm-hint">' + esc(t('toAllHint')) + '</p>' +
'<textarea name="t" maxlength="600" placeholder="' + esc(t('ph')) + '" aria-label="' + esc(t('ph')) + '"></textarea>' +
'<p class="cm-count">0 / 500</p>' +
'<div class="cm-row"><label class="cm-nick">' + esc(t('nick')) + '<input name="n" maxlength="24" autocomplete="nickname" placeholder="' + esc(t('nickPh')) + '" value="' + esc(get(KEY_NICK) || '') + '"></label>' +
'<label>' + esc(t('home')) + '<select name="h">' + options(HOMES, home, function (c) { return flag(c) + ' ' + country(c); }, t('homeNone')) + '</select></label>' +
'<label>' + esc(t('reading')) + '<select name="l">' + options(READ, readL, function (l) { return langName(l); }) + '</select></label></div>' +
'<label class="cm-hp" aria-hidden="true">Website<input name="url" tabindex="-1" autocomplete="off"></label>' +
'<div class="cm-foot"><p class="cm-rules">' + esc(t('rules')) + '</p><button type="submit" class="cm-send">' + esc(t('send')) + '</button></div>' +
'<p class="cm-msg" hidden></p></form>';
anchor.parentNode.insertBefore(box, anchor.nextSibling);
var form = box.querySelector('form'), ta = form.querySelector('textarea'), cnt = form.querySelector('.cm-count'), hint = form.querySelector('.cm-hint');
var seg = [].slice.call(form.querySelectorAll('.cm-seg button')), msg = form.querySelector('.cm-msg'), btn = form.querySelector('.cm-send');
seg.forEach(function (b) {
b.addEventListener('click', function () {
mode = b.getAttribute('data-k');
seg.forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
hint.textContent = mode === 'q' ? t('toOwnerHint') : t('toAllHint');
ta.placeholder = mode === 'q' ? t('phOwner') : t('ph');
});
});
function count() { var n = ta.value.trim().length; cnt.textContent = n + ' / 500'; cnt.classList.toggle('over', n > 500); }
ta.addEventListener('input', count);
function say(text, bad) { msg.hidden = false; msg.textContent = text; msg.classList.toggle('bad', !!bad); }
form.addEventListener('submit', function (e) {
e.preventDefault();
if (sending) return;
var text = ta.value.trim();
if (text.length < 2) { say(t('short'), true); ta.focus(); return; }
if (text.length > 500) { say(t('long'), true); return; }
var nick = form.n.value.trim(), h = form.h.value, l = form.l.value;
put(KEY_NICK, nick); put(KEY_HOME, h);
sending = true; btn.disabled = true; btn.textContent = t('sending');
C.api('POST', '/v1/comment', { p: C.slug, v: C.vid(), n: nick, h: h, l: l, t: text, k: mode, hp: form.url.value }).then(function (r) {
if (r && r.ok) {
ta.value = ''; count();
say(r.st === 'inbox' ? t('sentOwner') : t('sentAll'));
if (r.list) { data = r.list; renderList(); }
if (window.pengessoPop) { var b = btn.getBoundingClientRect(); window.pengessoPop(b.left + b.width / 2, b.top, mode === 'q' ? ['📮', '💌', '✨'] : ['💌', '💬', '✨', '🐧'], 16); }
} else say(r && r.e === 'limit' ? t('limit') : r && r.e === 'short' ? t('short') : t('err'), true);
}).catch(function () { say(t('err'), true); }).then(function () { sending = false; btn.disabled = false; btn.textContent = t('send'); });
});
renderList();
C.api('GET', '/v1/comments?p=' + encodeURIComponent(C.slug) + '&v=' + C.vid()).then(function (r) {
if (r && r.ok) { data = r; renderList(); }
}).catch(function () {});
}
px.cmMount = build;
if (C.anchor) build(C.anchor);
})();
