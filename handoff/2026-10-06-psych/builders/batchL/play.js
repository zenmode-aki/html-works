const { webkit, devices } = require(require('os').homedir() + '/node_modules/playwright');
const out = process.argv[2];
const plans = {
  'unfinished-tasks-weigh-on-you': async p => { await tapAll(p, '.go'); await p.waitForTimeout(800); await shot(p,'mid'); await tapAll(p, '.app'); await p.waitForTimeout(2500); },
  'feel-more-think-less': async p => { await tapN(p,'.sense',2); await shot(p,'mid'); await tapAll(p, '.sense'); await p.waitForTimeout(1200); },
  'when-worried-move-your-body': async p => { await tapN(p,'.mv',2,1); for (let i=0;i<9;i++){ await tap(p,'.tapbtn'); await p.waitForTimeout(150);} await shot(p,'mid'); for (let i=0;i<14;i++){ await tap(p,'.tapbtn'); await p.waitForTimeout(150);} await p.waitForTimeout(800); },
  'a-slouch-means-something-is-heavy': async p => { await tap(p,'.spin'); await p.waitForTimeout(1900); await shot(p,'mid'); for (let i=0;i<3;i++){ await tap(p,'.spin'); await p.waitForTimeout(1900);} await p.waitForTimeout(500); },
  'good-mood-savings': async p => { for (let i=0;i<6;i++){ const v = await p.$eval('.ev.show', e=>e.getAttribute('data-v')); await tap(p, v==='1'?'.to-a':'.to-b'); await p.waitForTimeout(300);} await shot(p,'mid'); await tap(p,'.ask'); await p.waitForTimeout(1200); },
  'raise-your-inner-pressure': async p => { await tap(p,'.dive'); await tap(p,'.dive'); await p.waitForTimeout(600); await shot(p,'mid'); for (let i=0;i<3;i++) await tap(p,'.strong'); for (let i=0;i<3;i++){ await tap(p,'.dive'); await tap(p,'.strong'); } await p.waitForTimeout(900); },
  'your-brain-barks-like-a-dog': async p => { await tap(p,'.start'); await p.waitForTimeout(400); await tap(p,'.back'); await p.waitForTimeout(1200); await shot(p,'mid'); for (let i=0;i<3;i++){ await tap(p,'.say'); await p.waitForTimeout(1500);} await p.waitForTimeout(500); },
  'the-documentary-camera': async p => { await tap(p,'.cam-btn'); await p.waitForTimeout(1500); await shot(p,'mid'); for (let i=0;i<2;i++){ await tap(p,'.nextsc'); await tap(p,'.cam-btn'); await p.waitForTimeout(700);} await p.waitForTimeout(800); },
  'its-ok-to-feel-annoyed': async p => { for (let i=0;i<5;i++){ await tap(p,'.bub'); await p.waitForTimeout(250);} await p.waitForTimeout(500); await shot(p,'mid'); await tap(p,'.okbtn'); await p.waitForTimeout(800); await shot(p,'soft'); await p.waitForTimeout(2600); },
  'too-many-shoulds': async p => { await tapN(p,'.stone',2); await p.waitForTimeout(700); await shot(p,'mid'); await tapAll(p,'.stone'); await p.waitForTimeout(1200); },
};
let cur;
async function tap(p, sel, i=0) { const els = await p.$$('.game ' + sel); const el = els[i]; if (!el || !(await el.isVisible())) { console.log('skip', sel); return; } await el.scrollIntoViewIfNeeded(); const b = await el.boundingBox(); await p.touchscreen.tap(b.x + b.width/2, b.y + b.height/2); await p.waitForTimeout(120); }
async function tapN(p, sel, n, start=0) { for (let i=start;i<start+n;i++) await tap(p, sel, i); }
async function tapAll(p, sel) { const n = (await p.$$('.game ' + sel)).length; for (let i=0;i<n;i++) await tap(p, sel, i); }
async function shot(p, tag) { const g = await p.$('.game'); await g.screenshot({ path: `${out}/${cur}-${tag}.png` }); }
(async () => {
  const b = await webkit.launch();
  for (const slug of Object.keys(plans)) {
    cur = slug;
    for (const lang of ['', 'dark']) {
      const ctx = await b.newContext({ ...devices['iPhone 15'], colorScheme: 'light' }); const p = await ctx.newPage(); const errs = [];
      p.on('pageerror', e => errs.push(e.message));
      await p.goto(`http://localhost:8765/draft/${slug}/`, { waitUntil: 'load' }); await p.waitForTimeout(500);
      if (lang === 'dark') await p.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
      const g = await p.$('.game'); await g.scrollIntoViewIfNeeded(); await p.waitForTimeout(700);
      if (lang === 'dark') { await shot(p, 'dark'); await ctx.close(); continue; }
      await plans[slug](p); await shot(p, 'end');
      const st = await p.$eval('.game', g => [...g.attributes].filter(a => a.name.startsWith('data-')).map(a => a.name + '=' + a.value).join(' '));
      const ov = await p.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1);
      console.log(slug, st, 'overflow=' + ov, errs.join('|'));
      await ctx.close();
    }
  }
  await b.close();
})();
