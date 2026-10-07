const { webkit, devices } = require(require('os').homedir() + '/node_modules/playwright');
(async () => { const b = await webkit.launch(); const c = await b.newContext({ ...devices['iPhone 13'] }); const p = await c.newPage();
await p.goto('file:///Users/ezakimasaaki/Desktop/html-works/draft/drop-your-character/index.html');
await p.evaluate(() => document.querySelectorAll('.card,.game').forEach(e => e.classList.add('in')));
const r = 0;
console.log(r); await p.locator('.plate').screenshot({ path: 'plate.png' }); await b.close(); })();
