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
    for (const slug of ['raci-matrix', 'gantt-chart', 'dependency-map']) {
      for (const scenario of ['software', 'migration']) {
        const stem = path.join(root, 'skills', slug, 'examples', 'assets', scenario);
        for (const [view, width, height] of [['desktop',1440,1000], ['portrait',390,844], ['landscape',844,390]]) {
          await page.setViewport({width,height});
          await page.goto(pathToFileURL(stem+'.html').href);
          assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true, `${slug}: page overflow at ${width}`);
          if (slug === 'gantt-chart') assert.deepEqual(await page.$$eval('.gantt-row.is-related',rows=>rows.map(row=>row.dataset.taskId).sort()),['A','D','E']);
          await page.screenshot({path:path.join(output,`${slug}-${scenario}-${view}-viewport.png`)});
          if (view !== 'desktop') {
            const contentSelector = slug === 'gantt-chart' ? '.gantt-scroll' : (slug === 'dependency-map' ? '.graph-shell' : (view === 'portrait' ? '.mobile article' : '.scroll'));
            await page.$eval(contentSelector, x=>x.scrollIntoView());
            await page.screenshot({path:path.join(output,`${slug}-${scenario}-${view}-content.png`)});
            await page.evaluate(()=>scrollTo(0,0));
          }
          if (slug === 'dependency-map') {
            await page.type('#search','NO-MATCH-LITERAL');
            assert.match(await page.$eval('#count',x=>x.textContent), /^0 of/);
            await page.click('#reset');
            await page.focus('.edge');
            await page.keyboard.press('Enter');
            assert.match(await page.$eval('#detail',x=>x.textContent), /Evidence:/);
            const before = await page.$eval('#graph',x=>Number(x.getAttribute('width')));
            await page.click('#plus');
            const after = await page.$eval('#graph',x=>Number(x.getAttribute('width')));
            assert.ok(after > before);
            await page.click('#matrixTab');
            assert.equal(await page.$eval('#matrix',x=>getComputedStyle(x).display),'block');
            await page.click('#graphTab');
            await page.click('#links');
            assert.ok(await page.$$eval('.dim',x=>x.length) > 0);
            if (scenario === 'software' && view === 'desktop') {
              await page.click('#reset');
              await page.click('#editToggle');
              await page.click('#register tr[data-dependency-id="DEP-AUDIT"]');
              await page.select('#editReceiver','PLATFORM');
              await page.click('#saveDependency');
              assert.match(await page.$eval('#editError',x=>x.textContent),/different nodes/i);
              assert.equal(await page.$eval('#editReceiver',x=>x.value),'PLATFORM');
              await page.select('#editReceiver','INTEGRATION');
              await page.$eval('#editCommitted',x=>x.value='2026-10-21');
              await page.click('#saveDependency');
              assert.match(await page.$eval('#editError',x=>x.textContent),/requires commitment evidence/i);
              await page.$eval('#editCommitted',x=>x.value='');
              await page.select('#editProvider','SECURITY');
              await page.$eval('#editForecast',x=>x.value='2026-10-20');
              await page.click('#saveDependency');
              assert.match(await page.$eval('#detailSummary',x=>x.textContent),/directed cycle/i);
              assert.equal(await page.$eval('#register tr[data-dependency-id="DEP-AUDIT"]',x=>x.classList.contains('edited-row')),true);
              assert.match(await page.$eval('#register tr[data-dependency-id="DEP-AUDIT"]',x=>x.textContent),/Security → Integration team/);
              assert.equal(await page.$eval('.metric[data-metric="known date gap"] b',x=>x.textContent),'none');
              assert.deepEqual(await page.evaluate(()=>({provider:draftSnapshot().dependencies.find(d=>d.id==='DEP-AUDIT').provider,changed:draftSnapshot().local_draft.changed_dependencies})),{provider:'SECURITY',changed:1});
              await page.reload({waitUntil:'load'});
              assert.equal(await page.$eval('#register tr[data-dependency-id="DEP-AUDIT"]',x=>x.classList.contains('edited-row')),true);
              assert.match(await page.$eval('#register tr[data-dependency-id="DEP-AUDIT"]',x=>x.textContent),/Security → Integration team/);
              await page.click('#undoEdit');
              assert.match(await page.$eval('#register tr[data-dependency-id="DEP-AUDIT"]',x=>x.textContent),/Platform team → Integration team/);
              assert.match(await page.$eval('#count',x=>x.textContent),/no local draft changes/);
              assert.equal(await page.$eval('.metric[data-metric="known date gap"] b',x=>x.textContent),'−2 days');
            }
          } else {
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
             await page.click('#auditTab');
             assert.equal(await page.$eval('#auditView',x=>getComputedStyle(x).display),'block');
             await page.click('#rolesTab');
             assert.equal(await page.$eval('#rolesView',x=>getComputedStyle(x).display),'block');
             await page.click('#authority');
             assert.equal(await page.$eval('#authority',x=>x.getAttribute('aria-pressed')),'true');
             await page.click('#matrixTab');
             if (scenario === 'software' && view === 'desktop') {
               await page.click('#reset');
               await page.click('#editToggle');
               await page.click('#matrixView .cell[data-row-id="R-5"][data-role-id="Ada"]');
               await page.select('#editState','confirmed');
               await page.$eval('#editSource',x=>x.value='');
               await page.click('#saveCell');
               assert.match(await page.$eval('#editError',x=>x.textContent),/require an evidence/i);
               assert.equal(await page.$eval('#editState',x=>x.value),'confirmed');
               await page.select('#editCode','A');
               await page.select('#editState','confirmed');
               await page.$eval('#editNote',x=>x.value='Sponsor supplies a second approval');
               await page.$eval('#editSource',x=>x.value='D-EDITOR-QA');
               await page.click('#saveCell');
               assert.equal(await page.$eval('#matrixView .cell[data-row-id="R-5"][data-role-id="Ada"] b',x=>x.textContent),'A');
               assert.equal(await page.$eval('#matrixView .cell[data-row-id="R-5"][data-role-id="Ada"]',x=>x.classList.contains('edited')),true);
               assert.equal(await page.$eval('.metric[data-metric="confirmed cells"] b',x=>x.textContent),'1');
               assert.match(await page.$eval('#auditView [data-audit-row="R-5"]',x=>x.textContent),/2 A assignments/);
               assert.deepEqual(await page.evaluate(()=>({code:draftSnapshot().rows.find(row=>row.id==='R-5').cells.Ada.code,changed:draftSnapshot().local_draft.changed_cells})),{code:'A',changed:1});
               await page.reload({waitUntil:'load'});
               assert.equal(await page.$eval('#matrixView .cell[data-row-id="R-5"][data-role-id="Ada"] b',x=>x.textContent),'A');
               await page.click('#undoEdit');
               assert.equal(await page.$eval('#matrixView .cell[data-row-id="R-5"][data-role-id="Ada"] b',x=>x.textContent),'I');
               assert.match(await page.$eval('#scope',x=>x.textContent),/No local draft changes/);
               assert.equal(await page.$eval('.metric[data-metric="confirmed cells"] b',x=>x.textContent),'0');
             }
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
            if (scenario === 'software' && view === 'desktop') {
              await page.click('#reset');
              await page.click('#editToggle');
              assert.equal(await page.$eval('#editId',x=>x.value),'B');
              await page.click('#saveTask');
              assert.match(await page.$eval('#editError',x=>x.textContent),/No changes/);
              await page.$eval('#editForecastStart',x=>x.value='2026-10-20');
              await page.click('#saveTask');
              assert.match(await page.$eval('#editError',x=>x.textContent),/finish on or after start/i);
              await page.$eval('#editForecastStart',x=>x.value='2026-10-07');
              await page.$eval('#editForecastFinish',x=>x.value='2026-10-16');
              await page.click('#saveTask');
              assert.equal(await page.$eval('.gantt-row[data-task-id="B"]',x=>x.classList.contains('is-edited')),true);
              assert.match(await page.$eval('#draftDiagnostics',x=>x.textContent),/L-3: forecast violates/);
              await page.click('.gantt-row[data-task-id="E"] .task-button');
              await page.$eval('#editForecastFinish',x=>x.value='2026-10-18');
              await page.click('#saveTask');
              assert.match(await page.$eval('#editError',x=>x.textContent),/Milestone dates must coincide/);
              await page.$eval('#editForecastStart',x=>x.value='2026-10-17');
              await page.$eval('#editForecastFinish',x=>x.value='2026-10-17');
              await page.click('#saveTask');
              assert.equal(await page.$eval('.summary-card[data-metric="forecast finish"] .value',x=>x.textContent),'17 Oct');
              assert.equal(await page.$eval('.summary-card[data-metric="finish change"] .value',x=>x.textContent),'+3 days');
              assert.deepEqual(await page.evaluate(()=>({finish:draftSnapshot().tasks.find(task=>task.id==='E').forecast.finish,changed:draftSnapshot().local_draft.changed_tasks})),{finish:'2026-10-17',changed:2});
              await page.reload({waitUntil:'load'});
              assert.match(await page.$eval('#scope',x=>x.textContent),/2 locally edited/);
              await page.click('#undoEdit');
              assert.equal(await page.$eval('.summary-card[data-metric="forecast finish"] .value',x=>x.textContent),'16 Oct');
              await page.click('#undoEdit');
              assert.equal(await page.$eval('.gantt-row[data-task-id="B"]',x=>x.classList.contains('is-edited')),false);
              assert.match(await page.$eval('#scope',x=>x.textContent),/no local draft changes/);
            }
          }}
          await page.click('#reset');
          reports.push({slug,scenario,view,viewport:[width,height],overflow:false,searchResetKeyboard:true});
        }
        const exports = slug === 'dependency-map'
          ? await page.$$eval('a[download]',async els=>Promise.all(els.map(async x=>({name:x.download,body:await (await fetch(x.href)).text()}))))
          : await page.$$eval('a[download]',els=>els.map(x=>({name:x.download,body:x.href.split(',')[1]})));
        for (const exported of exports) {
          const ext = path.extname(exported.name), actual = slug === 'dependency-map' ? exported.body : Buffer.from(exported.body,'base64').toString('utf8');
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
    for (const slug of ['project-budget','benefits-realization','resource-capacity-plan','scope-and-wbs','stakeholder-map','risk-workshop','release-readiness']) {
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
