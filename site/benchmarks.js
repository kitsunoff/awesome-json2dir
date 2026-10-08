// Benchmark summaries are data, never executable markup. No runtime dependencies.
(function () {
  "use strict";
  var root = document.getElementById("benchmarks");
  if (!root) return;
  var data, state = { implementation: "", family: "startup", workload: "empty", storage: "disk", mode: "create", baseline: "json2dir", log: false, sort: "time" };
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function number(n) { return typeof n === "number" && Number.isFinite(n) && n >= 0 ? n : null; }
  function text(v) { return typeof v === "string" ? v : ""; }
  function array(v) { return Array.isArray(v) ? v : []; }
  function url(v) { return typeof v === "string" && /^https:\/\//i.test(v) ? v : ""; }
  function fmt(n, digits) { return n == null ? "—" : n.toLocaleString("en", { maximumFractionDigits: digits == null ? 2 : digits }); }
  function stats(v) {
    if (!v || number(v.count) == null || v.count < 1 || !Number.isInteger(v.count)) return null;
    var values = [v.minimum, v.q1, v.median, v.q3, v.maximum].map(number);
    if (values.some(function (n) { return n == null; }) || values.some(function (n, i) { return i && n < values[i - 1]; })) return null;
    return { count: v.count, minimum: v.minimum, q1: v.q1, median: v.median, q3: v.q3, maximum: v.maximum };
  }
  function normalize(input) {
    if (!input || input.schemaVersion !== 1) throw Error("Unsupported benchmark data version");
    return {
      id: text(input.id), created: text(input.created), completed: input.completed === true, environment: input.environment || {}, lock: input.lock || {},
      implementations: array(input.implementations).filter(Boolean).map(function (x) {
        var d = x.definition || {};
        return { name: text(d.name), language: text(d.language), description: text(d.description), repo: url(d.repo),
          revision: text(d.revision), command: text(d.command), build: text(d.build),
          status: text(x.status), reason: text(x.reason), conformance: array(x.conformance) };
      }),
      workloads: array(input.workloads).filter(Boolean).map(function (w) {
        return { id: text(w.id), family: text(w.family), mode: text(w.mode), size: number(w.size),
          inputBytes: number(w.inputBytes), payloadBytes: number(w.payloadBytes), files: number(w.files),
          directories: number(w.directories), links: number(w.links), scripts: number(w.scripts), depth: number(w.depth), hash: text(w.hash) };
      }),
      results: array(input.results).filter(Boolean).map(function (r) {
        return { implementation: text(r.implementation), workload: text(r.workload), storage: text(r.storage),
          status: text(r.status), reason: text(r.reason), timing: stats(r.timing), entriesPerSecond: number(r.entriesPerSecond),
          miBPerSecond: number(r.miBPerSecond), userSeconds: number(r.userSeconds), systemSeconds: number(r.systemSeconds), maxRssKiB: number(r.maxRssKiB) };
      })
    };
  }
  function select(key, label, options, all) {
    return '<label>' + label + '<select data-b="' + key + '">' + (all ? '<option value="">All</option>' : "") +
      options.map(function (v) { return '<option value="' + esc(v) + '"' + (state[key] === v ? " selected" : "") + '>' + esc(v) + '</option>'; }).join("") + '</select></label>';
  }
  function distinct(values) { return Array.from(new Set(values)).sort(); }
  function eligible(r) { return r.status === "ok" && r.timing; }
  function render() {
    var modes = distinct(data.workloads.map(function (w) { return w.mode; }));
    if (modes.indexOf(state.mode) < 0) state.mode = modes[0];
    var families = distinct(data.workloads.filter(function (w) { return w.mode === state.mode; }).map(function (w) { return w.family; }));
    if (families.indexOf(state.family) < 0) state.family = families[0];
    var workloads = data.workloads.filter(function (w) { return w.family === state.family && w.mode === state.mode; }).sort(function (a, b) { return a.size - b.size || a.id.localeCompare(b.id); });
    if (!workloads.some(function (w) { return w.id === state.workload; })) state.workload = workloads.length ? workloads[0].id : "";
    var names = data.implementations.map(function (i) { return i.name; });
    if (names.indexOf(state.baseline) < 0) state.baseline = names[0] || "";
    var rows = data.results.filter(function (r) { return r.workload === state.workload && r.storage === state.storage && (!state.implementation || r.implementation === state.implementation); });
    var baseline = data.results.find(function (r) { return r.workload === state.workload && r.storage === state.storage && r.implementation === state.baseline && eligible(r); });
    var metrics = { time: function (r) { return eligible(r) ? r.timing.median : null; }, rss: function (r) { return r.maxRssKiB; }, name: function () { return null; } };
    rows.sort(function (a, b) {
      var av = metrics[state.sort](a), bv = metrics[state.sort](b);
      return state.sort === "name" ? a.implementation.localeCompare(b.implementation) : (av == null ? Infinity : av) - (bv == null ? Infinity : bv) || a.implementation.localeCompare(b.implementation);
    });
    var maximum = Math.max(1, ...rows.filter(eligible).map(function (r) { return r.timing.maximum; }));
    var info = data.workloads.find(function (w) { return w.id === state.workload; });
    root.innerHTML = '<p class="b-meta">Campaign ' + esc(data.id) + ' · ' + esc(data.created) + (data.completed ? ' · finished' : ' · interrupted / incomplete') + '</p>' +
      '<div class="b-controls">' + select("implementation", "Implementation", names, true) + select("mode", "Operation", modes) +
      select("family", "Workload family", families) + select("workload", "Size / fixture", workloads.map(function (w) { return w.id; })) +
      select("storage", "Storage", ["disk", "tmpfs"]) + select("baseline", "Reference", names) +
      '<label class="b-check"><input type="checkbox" data-log' + (state.log ? " checked" : "") + '> Logarithmic chart axes</label></div>' +
      (info ? '<p class="b-meta">' + fmt(info.inputBytes, 0) + ' input bytes · ' + fmt(info.payloadBytes, 0) + ' output bytes · ' +
        fmt(info.files, 0) + ' files · ' + fmt(info.directories, 0) + ' directories · ' + fmt(info.links, 0) + ' links · ' + fmt(info.scripts, 0) + ' scripts · depth ' + fmt(info.depth, 0) + '</p>' : "") +
      '<div class="b-scroll"><table class="b-table"><thead><tr><th><button data-sort="name">Implementation</button></th><th>Status</th><th><button data-sort="time">Median ms</button></th>' +
      '<th>Q1–Q3 ms / samples</th><th>Timing spread</th><th>Reference time / time</th><th>Entries/s</th><th>Output MiB/s</th><th>CPU user/system s</th>' +
      '<th><button data-sort="rss">Maximum process RSS KiB</button></th></tr></thead><tbody>' + rows.map(function (r) {
        var impl = data.implementations.find(function (i) { return i.name === r.implementation; });
        var name = impl && impl.repo ? '<a href="' + esc(impl.repo) + '">' + esc(r.implementation) + '</a>' : esc(r.implementation);
        var t = r.timing;
        var scale = function (v) { return 100 * (state.log ? Math.log1p(v) / Math.log1p(maximum) : v / maximum); };
        var bar = eligible(r) ? '<span class="b-bar" role="img" aria-label="' + esc('Median ' + fmt(t.median) + ' ms; Q1 ' + fmt(t.q1) + '; Q3 ' + fmt(t.q3)) + '">' +
          '<i class="b-iqr" style="left:' + scale(t.q1) + '%;width:' + (scale(t.q3) - scale(t.q1)) + '%"></i><i class="b-median" style="left:' + scale(t.median) + '%"></i></span>' : "—";
        var ratio = eligible(r) && baseline && t.median > 0 && baseline.timing.median > 0 ? fmt(baseline.timing.median / t.median) + '×' : "—";
        return '<tr><td>' + name + '</td><td>' + esc(r.status) + (r.reason ? '<details><summary>Reason</summary>' + esc(r.reason) + '</details>' : "") + '</td>' +
          '<td>' + (t ? fmt(t.median) + (eligible(r) ? "" : " (partial)") : "—") + '</td><td>' + (t ? fmt(t.q1) + '–' + fmt(t.q3) + ' / ' + t.count : "—") + '</td><td>' + bar + '</td>' +
          '<td>' + ratio + '</td><td>' + fmt(r.entriesPerSecond, 0) + '</td><td>' + fmt(r.miBPerSecond) + '</td><td>' + fmt(r.userSeconds) + ' / ' + fmt(r.systemSeconds) + '</td><td>' + fmt(r.maxRssKiB, 0) + '</td></tr>';
      }).join("") + '</tbody></table></div>' +
      '<p class="b-meta">Bars show median and interquartile range. Partial or incorrect runs are excluded from relative comparisons. RSS is the largest process, not combined process-tree memory.</p>' +
      (workloads.length > 1 ? scaling(workloads, names) : "") +
      '<details><summary>Environment, revisions and conformance</summary><pre>' + esc(JSON.stringify(data.environment, null, 2)) + '</pre><pre>' + esc(JSON.stringify(data.lock.toolchains || {}, null, 2)) + '</pre>' +
      data.implementations.map(function (i) {
        var passed = i.conformance.filter(function (c) { return c.status === "pass"; }).length;
        return '<details><summary>' + esc(i.name) + ' · ' + esc(i.language) + ' · ' + passed + '/' + i.conformance.length + ' conformance cases passed</summary><pre>' + esc(i.revision + '\n' + i.command + '\nBuild: ' + i.build) + '</pre>' +
          (i.reason ? '<p>' + esc(i.reason) + '</p>' : "") + '<pre>' + esc(JSON.stringify(i.conformance.filter(function (c) { return c.status !== "pass"; }), null, 2)) + '</pre></details>';
      }).join("") + '</details>';
    root.querySelectorAll('[data-b]').forEach(function (s) { s.onchange = function () { state[s.dataset.b] = s.value; render(); }; });
    root.querySelectorAll('[data-sort]').forEach(function (b) { b.onclick = function () { state.sort = b.dataset.sort; render(); }; });
    root.querySelector('[data-log]').onchange = function (e) { state.log = e.target.checked; render(); };
  }
  function scaling(workloads, names) {
    var series = names.filter(function (n) { return !state.implementation || n === state.implementation; }).map(function (name) {
      return { name: name, points: workloads.map(function (w) {
        var r = data.results.find(function (r) { return r.implementation === name && r.workload === w.id && r.storage === state.storage && eligible(r); });
        return { workload: w, result: r };
      }) };
    });
    var values = series.flatMap(function (s) { return s.points.filter(function (p) { return p.result; }).map(function (p) { return p.result.timing.median; }); });
    if (!values.length) return '<p>No complete scaling measurements for this selection.</p>';
    var transform = function (v) { return state.log ? Math.log1p(v) : v; };
    var xmin = Math.min(...workloads.map(function (w) { return transform(w.size); })), xmax = Math.max(...workloads.map(function (w) { return transform(w.size); }));
    var ymax = Math.max(1, ...values.map(transform));
    var x = function (w) { return 70 + 610 * (transform(w.size) - xmin) / (xmax - xmin || 1); };
    var y = function (ms) { return 230 - 200 * transform(ms) / ymax; };
    var colors = ['#2563eb', '#c2410c', '#15803d', '#9333ea', '#b91c1c', '#0e7490', '#a16207', '#475569'];
    var lines = series.map(function (s, i) {
      // Missing points break lines: never imply a successful result through a timeout.
      var path = '', previous = false;
      s.points.forEach(function (p) { if (p.result) { path += (previous ? ' L' : ' M') + x(p.workload) + ' ' + y(p.result.timing.median); previous = true; } else previous = false; });
      return '<path d="' + path + '" fill="none" stroke="' + colors[i % colors.length] + '" stroke-width="2"/>' + s.points.filter(function (p) { return p.result; }).map(function (p) {
        return '<circle cx="' + x(p.workload) + '" cy="' + y(p.result.timing.median) + '" r="4" fill="' + colors[i % colors.length] + '"><title>' + esc(s.name + ': ' + p.workload.id + ', ' + fmt(p.result.timing.median) + ' ms') + '</title></circle>';
      }).join('');
    }).join('');
    var labels = workloads.map(function (w) { return '<text x="' + x(w) + '" y="252" text-anchor="middle">' + fmt(w.size, 0) + '</text>'; }).join('');
    var ticks = [0, .5, 1].map(function (fraction) {
      var value = state.log ? Math.expm1(ymax * fraction) : ymax * fraction;
      return '<text x="62" y="' + (234 - 200 * fraction) + '" text-anchor="end">' + fmt(value) + '</text>';
    }).join('');
    var fallback = series.map(function (s) { return '<tr><th>' + esc(s.name) + '</th>' + s.points.map(function (p) { return '<td>' + (p.result ? fmt(p.result.timing.median) : '—') + '</td>'; }).join('') + '</tr>'; }).join('');
    return '<h3>Scaling: median milliseconds versus workload size</h3><svg class="b-chart" viewBox="0 0 740 280" role="img" aria-label="Scaling comparison; numeric values in the table below">' +
      '<path d="M70 30 V230 H680" fill="none" stroke="currentColor"/>' + ticks + labels + lines + '</svg><p>' + series.map(function (s, i) { return '<span class="b-legend" style="color:' + colors[i % colors.length] + '">' + esc(s.name) + '</span>'; }).join(' ') + '</p>' +
      '<details><summary>Scaling values (ms)</summary><div class="b-scroll"><table class="b-table"><thead><tr><th>Implementation</th>' + workloads.map(function (w) { return '<th>' + esc(w.id) + '</th>'; }).join('') + '</tr></thead><tbody>' + fallback + '</tbody></table></div></details>';
  }
  fetch(root.dataset.src || 'benchmarks.json').then(function (response) {
    if (!response.ok) throw Error('Benchmark data could not be loaded');
    return response.json();
  }).then(function (input) {
    data = normalize(input);
    if (!data.results.length) { root.textContent = 'No benchmark campaign has been published yet.'; return; }
    state.workload = data.workloads.some(function (w) { return w.id === 'empty'; }) ? 'empty' : data.workloads[0].id;
    var first = data.workloads.find(function (w) { return w.id === state.workload; });
    state.family = first.family; state.mode = first.mode;
    render();
  }).catch(function (error) { root.textContent = error.message; });
})();
