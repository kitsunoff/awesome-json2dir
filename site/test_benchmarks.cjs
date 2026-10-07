// Run with node --test site/test_benchmarks.cjs. Exercise rendering and controls
// with an HTML sink; no browser or downloaded DOM package is needed.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const vm = require('node:vm');
const script = fs.readFileSync(path.join(__dirname, 'benchmarks.js'), 'utf8');

function fixture() {
  const timing = { count: 15, minimum: 8, q1: 9, median: 10, q3: 11, maximum: 12 };
  return { schemaVersion: 1, id: 'campaign', created: 'today', completed: true, environment: { cpu: 'CPU' }, lock: { toolchains: { rust: 'nightly' } },
    implementations: ['json2dir', 'other'].map(name => ({ definition: { name, repo: 'https://example.com/' + name, revision: 'abc', language: 'Rust', command: 'tool' }, status: 'ready', conformance: [{ status: 'pass' }] })),
    workloads: [100, 1000].map(size => ({ id: 'files-' + size, family: 'files', mode: 'create', size, inputBytes: size * 80, payloadBytes: size * 64, files: size, directories: 0, links: 0, scripts: 0, depth: 0 })),
    results: [100, 1000].flatMap(size => ['json2dir', 'other'].map(implementation => ({ implementation, workload: 'files-' + size, storage: 'disk', status: 'ok', timing: { ...timing, median: implementation === 'other' ? 11 : 10 }, entriesPerSecond: 100, miBPerSecond: 2, maxRssKiB: 1000, userSeconds: 0, systemSeconds: 0 }))) };
}

async function render(data, responseOk = true) {
  const sink = { dataset: { src: 'benchmarks.json' }, innerHTML: '', textContent: '' };
  const controls = new Map();
  sink.querySelectorAll = selector => {
    const expression = selector === '[data-b]' ? /data-b="([^"]+)"/g : /data-sort="([^"]+)"/g;
    return [...sink.innerHTML.matchAll(expression)].map(match => {
      const element = { dataset: selector === '[data-b]' ? { b: match[1] } : { sort: match[1] }, value: '', onchange: null, onclick: null };
      controls.set(match[1], element); return element;
    });
  };
  const log = {};
  sink.querySelector = () => log;
  vm.runInNewContext(script, { document: { getElementById: () => sink }, fetch: async () => ({ ok: responseOk, json: async () => data }) });
  await new Promise(resolve => setImmediate(resolve));
  return { sink, controls, log };
}

test('latest campaign renders timing, resource and scaling tables', async () => {
  const { sink, controls, log } = await render(fixture());
  assert.match(sink.innerHTML, /campaign.*finished/);
  assert.match(sink.innerHTML, /Q1–Q3/);
  assert.match(sink.innerHTML, /Maximum process RSS/);
  assert.match(sink.innerHTML, /Scaling values/);
  assert.match(sink.innerHTML, /1×/);
  controls.get('implementation').value = 'other'; controls.get('implementation').onchange();
  assert.doesNotMatch(sink.innerHTML, /<td><a href="https:\/\/example.com\/json2dir">/);
  log.onchange({ target: { checked: true } });
  assert.match(sink.innerHTML, /data-log checked/);
});

test('partial runs retain samples but have no bar or reference ratio', async () => {
  const data = fixture();
  data.completed = false;
  data.results.filter(r => r.implementation === 'other').forEach(r => { r.status = 'timeout'; r.reason = 'deadline'; });
  const { sink } = await render(data);
  assert.match(sink.innerHTML, /interrupted \/ incomplete/);
  assert.match(sink.innerHTML, /11 \(partial\)/);
  assert.match(sink.innerHTML, /deadline/);
  assert.equal((sink.innerHTML.match(/class="b-bar"/g) || []).length, 1);
});

test('malformed measurements stay missing and repository links use HTTPS only', async () => {
  const data = fixture();
  data.implementations[1].definition.repo = 'javascript:alert(1)';
  data.implementations[1].definition.command = '<script>alert(1)</script>';
  data.environment.cpu = '<img src=x onerror=alert(1)>';
  data.results.filter(r => r.implementation === 'other').forEach(r => { r.timing.median = Infinity; r.maxRssKiB = -1; r.reason = '<script>bad</script>'; });
  const { sink } = await render(data);
  assert.doesNotMatch(sink.innerHTML, /href="javascript:|<script>|<img /);
  assert.match(sink.innerHTML, /&lt;script&gt;/);
  assert.equal((sink.innerHTML.match(/class="b-bar"/g) || []).length, 1);
});

test('empty initial data and fetch/schema failures are explicit', async () => {
  assert.equal((await render({ schemaVersion: 1, results: [] })).sink.textContent, 'No benchmark campaign has been published yet.');
  assert.match((await render({ schemaVersion: 999 })).sink.textContent, /Unsupported/);
  assert.match((await render(fixture(), false)).sink.textContent, /could not be loaded/);
});
