// usage: node shot.js out.png slug "sel1|sel2|..."  (taps in order, then screenshots .game) ; sel may be "wait:ms"
const { webkit, devices } = require(require('os').homedir() + '/node_modules/playwright');
(async () => {
  const [out, slug, seq, lang] = process.argv.slice(2);
  const b = await webkit.launch(); const ctx = await b.newContext({ ...devices['iPhone 15'] }); const p = await ctx.newPage();
  const errs=[]; p.on('pageerror', e => errs.push(e.message));
  await p.goto(`http://localhost:8765/draft/${slug}/${lang?'?lang='+lang:''}`, { waitUntil: 'load' });
  await p.evaluate(()=>document.querySelectorAll('.card,.game').forEach(e=>e.classList.add('in')));
  const g = await p.$('.game'); await g.scrollIntoViewIfNeeded(); await p.waitForTimeout(400);
  for (const s of (seq||'').split('|').filter(Boolean)) {
    if (s.startsWith('wait:')) { await p.waitForTimeout(+s.slice(5)); continue; }
    const el = await p.$(s); if (!el) { console.log('missing', s); continue; }
    await el.scrollIntoViewIfNeeded(); const bx = await el.boundingBox();
    await p.touchscreen.tap(bx.x + bx.width/2, bx.y + bx.height/2); await p.waitForTimeout(250);
  }
  await p.waitForTimeout(900);
  await g.screenshot({ path: out });
  console.log(JSON.stringify(await p.evaluate(()=>{const g=document.querySelector('.game');const o={};for(const a of g.attributes)if(a.name.startsWith('data-'))o[a.name]=a.value;return o;})), errs);
  await b.close();
})();
