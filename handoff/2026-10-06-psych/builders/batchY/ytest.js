const { webkit, devices } = require(require('os').homedir() + '/node_modules/playwright');
const out = __dirname + '/shots'; require('fs').mkdirSync(out, { recursive: true });
const plans = {
  'growth-is-a-tool': ['.blk[data-k=w]', '.blk[data-k=r]', '.blk[data-k=g]'],
  'notice-what-can-be-automated': ['.b-bot', '.b-bot', '.b-me', '.b-bot', '.b-me', '.b-bot'],
  'growth-chasing-is-an-endless-sprint': ['.b-fast', '.b-fast', '.b-fast', '.b-fast', '.b-fast', '.b-fast'],
  'five-regrets-at-the-end': ['.rc[data-i="1"]', '.rc[data-i="2"]', '.rc[data-i="3"]', '.rc[data-i="4"]', '.rc[data-i="5"]', '.rc[data-i="4"]'],
  'dont-run-on-being-thanked': ['.day[data-i="1"]', '.day[data-i="2"]', '.day[data-i="3"]'],
  'thanks-shows-you-what-you-have': ['.it:nth-child(1)', '.it:nth-child(2)', '.it:nth-child(3)', '.it:nth-child(4)', '.it:nth-child(5)', '.it:nth-child(6)'],
  'help-without-wanting-anything-back': ['.b-give'],
  'holding-on-makes-it-hurt': ['.b-plus', '.b-plus', '.b-wind'],
  'three-ways-to-see-what-you-do': ['.ln[data-v="1"]', '.ln[data-v="2"]', '.ln[data-v="3"]'],
};
(async () => {
  const b = await webkit.launch();
  for (const [slug, steps] of Object.entries(plans)) {
    const ctx = await b.newContext({ ...devices['iPhone 15'] }); const p = await ctx.newPage();
    const errs = []; p.on('pageerror', e => errs.push(e.message));
    await p.goto(`http://localhost:8765/draft/${slug}/`); await p.waitForTimeout(500);
    const g = await p.$('.game'); await g.scrollIntoViewIfNeeded(); await p.waitForTimeout(700);
    for (const s of steps) { const el = await p.$('.game ' + s); const bx = await el.boundingBox(); await p.touchscreen.tap(bx.x + bx.width/2, bx.y + bx.height/2); await p.waitForTimeout(450); }
    await p.waitForTimeout(2600);
    await g.screenshot({ path: `${out}/y-${slug}.png` });
    console.log(slug, errs);
    await ctx.close();
  }
  // feelings: timing — start, wait ~1.3s, tap
  const ctx = await b.newContext({ ...devices['iPhone 15'] }); const p = await ctx.newPage();
  await p.goto('http://localhost:8765/draft/feelings-start-in-the-body/'); await p.waitForTimeout(500);
  const g = await p.$('.game'); await g.scrollIntoViewIfNeeded(); await p.waitForTimeout(700);
  const t = await p.$('.game .tap'); let bx = await t.boundingBox();
  for (let i = 0; i < 3; i++) { await p.touchscreen.tap(bx.x+50, bx.y+30); await p.waitForTimeout(1350); await p.touchscreen.tap(bx.x+50, bx.y+30); await p.waitForTimeout(500); }
  await g.screenshot({ path: `${out}/y-feelings.png` }); console.log('feelings', await g.getAttribute('data-s'), await p.textContent('.sc'));
  await b.close();
})();
