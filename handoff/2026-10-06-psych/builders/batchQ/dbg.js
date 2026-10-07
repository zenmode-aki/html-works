const { webkit, devices } = require(require('os').homedir() + '/node_modules/playwright');
(async () => {
  const b = await webkit.launch(); const ctx = await b.newContext({ ...devices['iPhone 15'] }); const p = await ctx.newPage();
  p.on('pageerror', e => console.log('ERR', e.message));
  await p.goto('http://localhost:8765/draft/it-could-have-been-cola/'); await p.waitForTimeout(500);
  const g = await p.$('.game'); await g.scrollIntoViewIfNeeded(); await p.waitForTimeout(800);
  const cards = await p.$$('.flip');
  for (const c of cards) { const bx = await c.boundingBox(); await p.touchscreen.tap(bx.x + bx.width/2, bx.y + bx.height/2); await p.waitForTimeout(300); }
  console.log(await p.evaluate(() => [document.querySelector('.game').dataset.n, document.querySelector('.cnt .num').textContent, document.elementFromPoint(100, 100) && document.elementFromPoint(100,100).className]));
  await p.waitForTimeout(900); await g.screenshot({ path: 'batchQ/dbg.png' });
  await b.close();
})();
