const { webkit, devices } = require(require('os').homedir() + '/node_modules/playwright');
(async () => {
  const b = await webkit.launch(); const ctx = await b.newContext({ ...devices['iPhone 15'] }); const p = await ctx.newPage();
  const [slug, ...sels] = process.argv.slice(2);
  await p.goto('http://localhost:8765/draft/' + slug + '/', { waitUntil: 'load' }); await p.waitForTimeout(800);
  for (const s of sels) console.log(s, JSON.stringify(await p.$$eval(s, els => els.map(e => getComputedStyle(e).display + (e.classList.contains('emo-pop') ? '*' : '')))));
  await b.close();
})();
