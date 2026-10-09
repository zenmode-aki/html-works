// 本物の WebKit（Safari のエンジン）× iPhone 13 で URL を開き、最後までスクロールして「隠れたままの文字」とJSエラーを数え、全体を撮る。
// usage: node wk-safari.js <出力先> <url...>   （~/node_modules/playwright と webkit が要る）
const { webkit, devices } = require('playwright');
(async () => {
  const b = await webkit.launch(); const out=process.argv[2];
  for (const [i,u] of process.argv.slice(3).entries()) {
    const ctx = await b.newContext({ ...devices['iPhone 13'], locale:'ja-JP' }); const p = await ctx.newPage();
    const errs=[]; p.on('pageerror',e=>errs.push(e.message.slice(0,150)));
    await p.goto(u,{waitUntil:'load'}); await p.waitForTimeout(800);
    const h = await p.evaluate(()=>document.body.scrollHeight);
    for (let y=0;y<h;y+=250){await p.evaluate(v=>scrollTo(0,v),y);await p.waitForTimeout(120);}
    await p.waitForTimeout(800);
    const r = await p.evaluate(()=>{const els=[...document.querySelectorAll('main *, article *, .card, section')].filter(e=>e.children.length===0&&e.textContent.trim().length>3&&e.getBoundingClientRect().height>0);
      const bad=els.filter(e=>{let n=e;while(n&&n!==document.body){const s=getComputedStyle(n);if(+s.opacity<0.3||s.visibility==='hidden')return true;n=n.parentElement;}return false;});
      return {n:els.length,bad:bad.length,sample:bad.slice(0,6).map(e=>e.className+':'+e.textContent.trim().slice(0,25))};});
    await p.screenshot({path:`${out}/full-${i}.png`, fullPage:true});
    console.log(u, JSON.stringify(r), errs); await ctx.close();
  }
  await b.close();
})();
