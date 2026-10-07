const { webkit, devices } = require(require('os').homedir() + '/node_modules/playwright');
(async () => {
  const slugs = process.argv.slice(2);
  const b = await webkit.launch();
  for (const s of slugs) {
    const ctx = await b.newContext({ ...devices['iPhone SE'] });
    const p = await ctx.newPage(); const errs = [];
    p.on('pageerror', e => errs.push(e.message));
    await p.goto('file:///Users/ezakimasaaki/Desktop/html-works/draft/' + s + '/index.html');
    await p.evaluate(() => document.querySelectorAll('.card,.game').forEach(e => e.classList.add('in')));
    for (let round = 0; round < 4; round++) {
      const btns = await p.$$('.game button');
      for (const bt of btns) { if (await bt.isVisible() && await bt.isEnabled()) { try { await bt.click({ timeout: 800 }); } catch (e) {} await p.waitForTimeout(120); } }
      await p.waitForTimeout(round === 1 ? 3500 : 900);
    }
    const ov = await p.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1);
    const st = await p.evaluate(() => { const g = document.querySelector('.game'); return [...g.attributes].filter(a => a.name.startsWith('data-')).map(a => a.name + '=' + a.value).join(' '); });
    await p.locator('.game').screenshot({ path: `${process.env.OUT}/${s}.png` });
    console.log(s, 'errors:', errs.length ? errs : 'none', 'overflow:', ov, '|', st);
    await ctx.close();
  }
  await b.close();
})();
