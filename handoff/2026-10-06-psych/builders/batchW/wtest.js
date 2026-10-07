const { webkit, devices } = require(require('os').homedir() + '/node_modules/playwright');
(async () => {
  const slugs = process.argv.slice(2);
  const b = await webkit.launch();
  for (const s of slugs) {
    const ctx = await b.newContext({ ...devices['iPhone 15'] });
    const p = await ctx.newPage(); const errs = [];
    p.on('pageerror', e => errs.push(e.message));
    await p.goto('file:///Users/ezakimasaaki/Desktop/html-works/draft/' + s + '/index.html');
    await p.evaluate(() => document.querySelectorAll('.card,.game').forEach(e => e.classList.add('in')));
    const g = await p.$('.game'); await g.scrollIntoViewIfNeeded();
    await g.screenshot({ path: `shot-${s}-0.png` });
    for (let round = 0; round < 9; round++) {
      const bs = await p.$$('.game button:not(.b-reset)');
      for (const bt of bs) { if (await bt.isVisible() && await bt.isEnabled()) { await bt.click({ force: true }).catch(()=>{}); await p.waitForTimeout(round < 2 ? 700 : 350); } }
    }
    await p.waitForTimeout(1600);
    await g.screenshot({ path: `shot-${s}-1.png` });
    const ov = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth);
    const st = await p.evaluate(() => { const g = document.querySelector('.game'); return [...g.attributes].map(a => a.name + '=' + a.value).join(' '); });
    console.log(s, 'overflow', ov, 'errs', errs, st);
    await ctx.close();
  }
  await b.close();
})();
