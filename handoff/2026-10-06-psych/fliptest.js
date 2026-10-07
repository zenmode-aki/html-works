// flip the first 2 cards of each page and screenshot the game (WebKit iPhone)
const { webkit, devices } = require(require('os').homedir() + '/node_modules/playwright');
const [out, ...pairs] = process.argv.slice(2);
(async () => {
  const b = await webkit.launch();
  for (const pr of pairs) {
    const [slug, sel] = pr.split('=');
    const ctx = await b.newContext({ ...devices['iPhone 15'] }); const p = await ctx.newPage();
    await p.goto(`http://localhost:8765/draft/${slug}/?lang=ja`, { waitUntil: 'load' });
    await p.evaluate(() => document.querySelectorAll('.card,.game').forEach(e => e.classList.add('in','show','visible')));
    const g = await p.$('.game'); await g.scrollIntoViewIfNeeded(); await p.waitForTimeout(1500);
    const cs = await p.$$(sel);
    for (const c of cs.slice(0, 2)) { await c.click({ force: true }); await p.waitForTimeout(900); }
    await g.screenshot({ path: `${out}/${slug}.png` });
    await ctx.close();
  }
  await b.close();
})();
