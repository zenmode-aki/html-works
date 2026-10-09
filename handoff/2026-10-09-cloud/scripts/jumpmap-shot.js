const pw=require('/opt/node22/lib/node_modules/playwright');
(async()=>{const b=await pw.chromium.launch();const [out,slug,lang]=process.argv.slice(2);
const c=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true});
const p=await c.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto(`http://localhost:8765/works/${slug}/index.html?lang=${lang}`);await p.waitForTimeout(800);
await p.evaluate(()=>window.scrollTo(0,document.body.scrollHeight));await p.waitForTimeout(3000);
const jm=await p.$('.jm');if(!jm){console.log('no jm',errs);await b.close();return;}
await jm.scrollIntoViewIfNeeded();await p.waitForTimeout(600);
await p.waitForTimeout(1500);await jm.screenshot({path:`${out}/jm-${slug}-${lang}-1.png`});
const g=await p.$('.jm-city[data-cc="JP"]');if(g){await g.click({force:true});await p.waitForTimeout(700);await jm.screenshot({path:`${out}/jm-${slug}-${lang}-2.png`});}
const n=await p.$('.jm-city[data-p="nagoya"]');if(n){await n.click({force:true});await p.waitForTimeout(700);await (await p.$('.jm-map')).screenshot({path:`${out}/jm-${slug}-${lang}-3.png`});}
const bk=await p.$('.jm-back');if(bk){await bk.click({force:true});await p.waitForTimeout(500);}
const ph=await p.$('.jm-city[data-cc="PH"]');if(ph){await ph.click({force:true});await p.waitForTimeout(700);await (await p.$('.jm-map')).screenshot({path:`${out}/jm-${slug}-${lang}-4.png`});}
console.log(JSON.stringify({sw:await p.evaluate(()=>document.documentElement.scrollWidth),errs}));
await b.close();})();
