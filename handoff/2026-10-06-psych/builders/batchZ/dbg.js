const { webkit, devices } = require(require('os').homedir() + '/node_modules/playwright');
(async () => {
  const b = await webkit.launch(); const ctx = await b.newContext({ ...devices['iPhone 15'] }); const p = await ctx.newPage();
  p.on('pageerror', e => console.log('ERR', e.message));
  await p.goto('http://localhost:8765/draft/outline-before-you-start/', { waitUntil: 'load' });
  const r = await p.evaluate(async () => {
    const g = document.querySelector('.game'); g.classList.add('in');
    const out = [];
    const b1 = g.querySelector('.b1');
    out.push(getComputedStyle(b1).backgroundColor, getComputedStyle(b1).opacity, b1.disabled, b1.className);
    for (const c of ['.b1','.b2','.b3']) { g.querySelector(c).click(); await new Promise(r=>setTimeout(r,250)); }
    g.querySelector('.go').click();
    await new Promise(r=>setTimeout(r,2600));
    out.push(g.dataset.s, g.dataset.r);
    return out;
  });
  console.log(r); await b.close();
})();
