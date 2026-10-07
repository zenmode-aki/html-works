const { webkit, devices } = require(require('os').homedir() + '/node_modules/playwright');
const U = s => 'file:///Users/ezakimasaaki/Desktop/html-works/draft/' + s + '/index.html';
(async () => {
  const b = await webkit.launch(); const out = {};
  async function page(s) { const c = await b.newContext({ ...devices['iPhone 13'] }); const p = await c.newPage(); p.errs = []; p.on('pageerror', e => p.errs.push(e.message)); await p.goto(U(s)); await p.evaluate(() => document.querySelectorAll('.card,.game').forEach(e => e.classList.add('in'))); return p; }
  const attrs = p => p.evaluate(() => [...document.querySelector('.game').attributes].filter(a => a.name.startsWith('data-')).map(a => a.name + '=' + a.value).join(' '));
  let p;
  p = await page('collect-ways-to-cheer-yourself-up'); for (const c of await p.$$('.chip')) await c.click(); out.collect = await attrs(p) + ' n=' + await p.textContent('.n'); await p.locator('.game').screenshot({ path: process.env.OUT + '/f-collect.png' });
  p = await page('choose-the-me-i-like'); for (let i = 0; i < 3; i++) { await p.click('.opt[data-v="b"]:visible'); await p.click('.nextq'); } out.choose = await attrs(p);
  p = await page('drop-your-character'); await p.click('.pea'); await p.waitForTimeout(900); for (const l of await p.$$('.lock')) await l.click(); out.pea = await attrs(p); await p.locator('.game').screenshot({ path: process.env.OUT + '/f-pea.png' });
  p = await page('not-lost-just-returned'); await p.click('.start'); await p.waitForTimeout(7400); for (const r of await p.$$('.rent')) await r.click(); out.lost = await attrs(p);
  p = await page('wishes-have-an-expiry-date'); for (let i = 0; i < 6; i++) await p.click('.plus'); out.wish1 = await attrs(p); await p.locator('.game').screenshot({ path: process.env.OUT + '/f-wish.png' });
  p = await page('three-kinds-of-confidence'); for (let i = 0; i < 5; i++) { await p.click('.bad'); await p.waitForTimeout(200); } out.conf = await attrs(p);
  p = await page('avoiding-makes-it-harder'); await p.click('.start'); for (let i = 0; i < 40; i++) { const c = await p.$('.ch.on'); if (c) { try { await c.click({ timeout: 300 }); } catch (e) {} } await p.waitForTimeout(350); } await p.waitForTimeout(1500); out.avoid = await attrs(p) + ' coins=' + await p.textContent('.cn');
  p = await page('stop-trying-to-look-nice'); await p.click('.laugh'); await p.waitForTimeout(1200); out.nice = await attrs(p); await p.locator('.game').screenshot({ path: process.env.OUT + '/f-nice.png' });
  p = await page('three-slow-things-before-a-speech'); for (let i = 0; i < 5; i++) { await p.click('.go'); await p.waitForTimeout(3200); } out.speechCalm = await attrs(p);
  await p.click('.reset'); for (let i = 0; i < 5; i++) { await p.click('.go'); await p.waitForTimeout(100); await p.click('.go'); await p.waitForTimeout(100); } out.speechRush = await attrs(p);
  p = await page('your-own-scorecard'); await p.click('.m-others'); await p.waitForTimeout(800); await p.locator('.game').screenshot({ path: process.env.OUT + '/f-score.png' });
  console.log(JSON.stringify(out, null, 1)); await b.close();
})();
