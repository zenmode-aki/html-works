// iPhone (WebKit) smoke test for draft articles.
// usage: node mtest.js <outdir> slug1 slug2 ...   (local server http://localhost:8765 serving the repo)
const { chromium: webkit, devices } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
(async () => {
  const [out, ...slugs] = process.argv.slice(2);
  fs.mkdirSync(out, { recursive: true });
  const browser = await webkit.launch();
  const results = [];
  for (const slug of slugs) {
    const ctx = await browser.newContext({ ...devices['iPhone 13'], isMobile:true, hasTouch:true });
    const page = await ctx.newPage();
    const errors = [];
    page.on('pageerror', e => errors.push(String(e.message).slice(0, 160)));
    page.on('console', m => { if (m.type() === 'error' && !/Failed to load resource|stats|px|comments/i.test(m.text())) errors.push('console: ' + m.text().slice(0, 160)); });
    let r = { slug };
    try {
      await page.goto(`http://localhost:8765/lab/${slug}/index.html`, { waitUntil: 'load', timeout: 20000 });
      await page.waitForTimeout(600);
      // scroll whole page so reveal animations fire
      const h = await page.evaluate(() => document.body.scrollHeight);
      for (let y = 0; y < h; y += 300) { await page.evaluate(v => window.scrollTo(0, v), y); await page.waitForTimeout(60); }
      r.overflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1);
      r.wideEls = await page.evaluate(() => [...document.querySelectorAll('body *')].filter(e => { const b = e.getBoundingClientRect(); return b.width > 0 && b.right > window.innerWidth + 2 && getComputedStyle(e).position !== 'fixed'; }).slice(0, 4).map(e => e.tagName + '.' + (e.className && e.className.baseVal === undefined ? e.className : '')));
      const game = await page.$('.game');
      r.hasGame = !!game;
      if (game) {
        await game.scrollIntoViewIfNeeded();
        await page.waitForTimeout(500);
        await game.screenshot({ path: `${out}/${slug}-0.png` });
        r.gameVisible = await page.evaluate(() => { const g = document.querySelector('.game'); return getComputedStyle(g).opacity; });
        const btns = await page.$$('.game button, .game [role=button], .game .tap');
        r.buttons = btns.length;
        r.small = [];
        let taps = 0;
        // tap each visible button up to 3 rounds, take screenshots in between
        for (let round = 0; round < 3; round++) {
          const list = await page.$$('.game button, .game [role=button]');
          for (const b of list) {
            const box = await b.boundingBox();
            if (!box || box.width < 2 || box.height < 2) continue;
            if (round === 0 && box.height < 40) r.small.push(Math.round(box.height) + 'px:' + (await b.innerText()).slice(0, 20));
            await b.scrollIntoViewIfNeeded();
            const box2 = await b.boundingBox();
            if (!box2) continue;
            await page.touchscreen.tap(box2.x + box2.width / 2, box2.y + box2.height / 2);
            taps++;
            await page.waitForTimeout(350);
          }
          await page.waitForTimeout(1200);
          await game.screenshot({ path: `${out}/${slug}-${round + 1}.png` });
        }
        r.taps = taps;
      }
      r.overflowAfter = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1);
      // Japanese
      await page.goto(`http://localhost:8765/lab/${slug}/index.html?lang=ja`, { waitUntil: 'load' });
      await page.waitForTimeout(900);
      const h2 = await page.evaluate(() => document.body.scrollHeight);
      for (let y = 0; y < h2; y += 400) { await page.evaluate(v => window.scrollTo(0, v), y); await page.waitForTimeout(40); }
      r.jaOverflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1);
      const g2 = await page.$('.game');
      if (g2) { await g2.scrollIntoViewIfNeeded(); await page.waitForTimeout(400); await g2.screenshot({ path: `${out}/${slug}-ja.png` }); }
    } catch (e) { r.fail = String(e.message).slice(0, 200); }
    r.errors = errors;
    results.push(r);
    console.log(JSON.stringify(r));
    await ctx.close();
  }
  await browser.close();
})();
