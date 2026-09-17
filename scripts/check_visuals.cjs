/* Optional browser QA; Puppeteer/Chrome are development tools, never skill runtime dependencies.
   Set PUPPETEER_MODULE to a locally installed module and CHROME_PATH if needed. */
const puppeteer = require(process.env.PUPPETEER_MODULE || 'puppeteer');
const fs = require('fs');
const path = require('path');
const assert = require('assert/strict');
const {pathToFileURL} = require('url');
const root = path.resolve(__dirname, '..');
const output = path.resolve(root, process.env.VISUAL_QA_OUTPUT || '.work/visual-qa');
fs.mkdirSync(output, {recursive: true});

(async () => {
  const browser = await puppeteer.launch({headless: true, ...(process.env.CHROME_PATH ? {executablePath: process.env.CHROME_PATH} : {})});
  const reports = [];
  try {
    const page = await browser.newPage();
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    for (const slug of ['raci-matrix', 'gantt-chart']) {
      for (const scenario of ['software', 'migration']) {
        const stem = path.join(root, 'skills', slug, 'examples', 'assets', scenario);
        for (const [view, width, height] of [['desktop',1440,1000], ['portrait',390,844], ['landscape',844,390]]) {
          await page.setViewport({width,height});
          await page.goto(pathToFileURL(stem+'.html').href);
          assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true, `${slug}: page overflow at ${width}`);
          if (slug === 'gantt-chart') assert.deepEqual(await page.$$eval('.gantt-row.is-related',rows=>rows.map(row=>row.dataset.taskId).sort()),['A','D','E']);
          await page.screenshot({path:path.join(output,`${slug}-${scenario}-${view}-viewport.png`)});
          if (view !== 'desktop') {
            const contentSelector = slug === 'gantt-chart' ? '.gantt-scroll' : (view === 'portrait' ? '.mobile article' : '.scroll');
            await page.$eval(contentSelector, x=>x.scrollIntoView());
            await page.screenshot({path:path.join(output,`${slug}-${scenario}-${view}-content.png`)});
            await page.evaluate(()=>scrollTo(0,0));
          }
          await page.type('#search','NO-MATCH-LITERAL');
          assert.match(await page.$eval('#scope',x=>x.textContent), /^0 \//);
          await page.click('#reset');
          await page.evaluate(() => [...document.querySelectorAll('[data-detail]')].find(x=>x.getBoundingClientRect().height>0).focus());
          await page.keyboard.press('Enter');
          assert.doesNotMatch(await page.$eval('#detail-text',x=>x.textContent), /^Select/);
          if (slug === 'raci-matrix') {
            const role = await page.$eval('#role',x=>x.options[1].value);
            await page.select('#role',role);
            assert.match(await page.$eval('#scope',x=>x.textContent), /other columns are hidden/);
            assert.equal(await page.$$eval('[data-role]',els=>els.filter(x=>!x.hidden).every(x=>x.dataset.role===document.querySelector('#role').value)),true);
          } else {
            const focused = await page.$eval('[data-detail]:focus',x=>x.dataset.taskId);
            await page.keyboard.press('ArrowDown');
            assert.notEqual(await page.$eval('[data-detail]:focus',x=>x.dataset.taskId),focused);
            await page.keyboard.press('Escape');
            assert.equal(await page.$eval('#detailPanel',x=>x.hidden),true);
            const before = await page.$eval(':root',x=>parseFloat(getComputedStyle(x).getPropertyValue('--day-width')));
            await page.click('#zoomIn');
            const after = await page.$eval(':root',x=>parseFloat(getComputedStyle(x).getPropertyValue('--day-width')));
            assert.ok(after > before);
            if (await page.$eval('#comparisonToggle',x=>!x.hidden)) {
              await page.click('#comparisonToggle');
              assert.equal(await page.$eval('#comparisonToggle',x=>x.getAttribute('aria-pressed')),'false');
            }
            await page.click('#linksToggle');
            assert.equal(await page.$eval('#linksToggle',x=>x.getAttribute('aria-pressed')),'false');
            await page.click('#criticalToggle');
            assert.match(await page.$eval('#scope',x=>x.textContent),/critical-only/);
            await page.click('#reset');
            const phase = await page.$eval('#phaseFilter',x=>x.options[1].value);
            await page.select('#phaseFilter',phase);
            assert.doesNotMatch(await page.$eval('#scope',x=>x.textContent),/^5 \/ 5/);
          }
          await page.click('#reset');
          reports.push({slug,scenario,view,viewport:[width,height],overflow:false,searchResetKeyboard:true});
        }
        const exports = await page.$$eval('a[download]',els=>els.map(x=>({name:x.download,body:x.href.split(',')[1]})));
        for (const exported of exports) {
          const ext = path.extname(exported.name), actual = Buffer.from(exported.body,'base64').toString('utf8');
          const expected = fs.readFileSync(stem+ext,'utf8');
          if (ext === '.json') assert.deepEqual(JSON.parse(actual),JSON.parse(expected));
          else assert.equal(actual.replace(/\r\n/g,'\n'),expected.replace(/\r\n/g,'\n'));
        }
      }
    }
    // Independent challenge: one clean row must disappear in the findings-only view.
    await page.setViewport({width:1440,height:1000});
    await page.goto(pathToFileURL(path.join(root,'evals/visual/corrected/raci-matrix-handoffs.html')).href);
    await page.select('#issues','findings');
    assert.match(await page.$eval('#scope',x=>x.textContent),/^2 \/ 3/);
    assert.equal(await page.$eval('tr[data-row="H-8"]',x=>x.hidden),true);
    for (const slug of ['project-budget','benefits-realization','resource-capacity-plan','scope-and-wbs','dependency-map','stakeholder-map','risk-workshop','release-readiness']) {
      await page.setViewport({width:1120,height:760});
      await page.goto(pathToFileURL(path.join(root,'skills',slug,'examples/assets/software-visual.svg')).href);
      const overflow=await page.evaluate(()=>[...document.querySelectorAll('text')].filter(t=>{const b=t.getBBox();return b.x<0||b.x+b.width>1120||b.y+b.height>760}).map(t=>t.textContent));
      assert.deepEqual(overflow,[],slug+' SVG text bounds');
      await page.screenshot({path:path.join(output,slug+'.png')});
      reports.push({slug,staticSVGTextBounds:true});
    }
    assert.deepEqual(errors,[]);
    fs.writeFileSync(path.join(output,'browser-checks.json'),JSON.stringify({browser:await browser.version(),reports,completeExportsMatch:true,cleanRowExcludedFromFindings:true,consoleErrors:errors},null,2)+'\n');
    console.log(`Passed ${reports.length} view/artifact checks, keyboard controls and export equality.`);
  } finally { await browser.close(); }
})().catch(error => {console.error(error);process.exitCode=1;});
