// Renders results/results.json (written by `json2dir-tester export`) as a
// filterable, sortable table. No dependencies.
(function () {
  "use strict";

  var root = document.getElementById("results");
  if (!root) return;

  var DIMENSIONS = [
    ["kinds", "Language"],
    ["verification", "Verification"],
    ["origin", "Author"],
    ["approach", "Approach"],
  ];
  var COLUMNS = [
    ["name", "Implementation"],
    ["passed", "Passed"],
    ["failed", "Failed"],
    ["score", "Score"],
  ];

  var data = null;
  var filters = {};
  var sortKey = "score";
  var open = {};

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  // results.json is data, not markup: counts must be numbers, links must be
  // https, and lists must be lists before anything reaches innerHTML.
  function count(n) {
    n = Number(n);
    return isFinite(n) && n >= 0 ? Math.floor(n) : 0;
  }

  function link(url) {
    return typeof url === "string" && /^https:\/\//i.test(url) ? url : "";
  }

  function list(v) {
    return [].concat(v == null ? [] : v).map(String);
  }

  function normalize(x) {
    return {
      name: String(x.name),
      language: String(x.language),
      repo: link(x.repo),
      passed: count(x.passed),
      failed: count(x.failed),
      state: String(x.state),
      kinds: list(x.kinds),
      verification: String(x.verification),
      origin: list(x.origin),
      approach: list(x.approach),
      failures: [].concat(x.failures || []).map(function (f) {
        return { case: String(f && f.case), reason: String(f && f.reason) };
      }),
    };
  }

  function score(x) {
    var run = x.passed + x.failed;
    return run ? x.passed / run : 0;
  }

  function values(x, key) {
    return [].concat(x[key]);
  }

  var compare = {
    name: function (a, b) { return a.language.localeCompare(b.language) || a.name.localeCompare(b.name); },
    passed: function (a, b) { return b.passed - a.passed; },
    failed: function (a, b) { return b.failed - a.failed; },
    score: function (a, b) { return score(b) - score(a) || b.passed - a.passed; },
  };

  function visible() {
    return data.impls.filter(function (x) {
      return DIMENSIONS.every(function (d) {
        var want = filters[d[0]];
        return !want || values(x, d[0]).indexOf(want) >= 0;
      });
    }).sort(function (a, b) {
      return compare[sortKey](a, b) || compare.name(a, b);
    });
  }

  function filterControls() {
    return DIMENSIONS.map(function (d) {
      var seen = {};
      data.impls.forEach(function (x) {
        values(x, d[0]).forEach(function (v) { seen[v] = (seen[v] || 0) + 1; });
      });
      var options = Object.keys(seen).sort().map(function (v) {
        return '<option value="' + esc(v) + '"' + (filters[d[0]] === v ? " selected" : "") + ">" +
          esc(v) + " (" + seen[v] + ")</option>";
      }).join("");
      return '<label>' + d[1] + '<select data-filter="' + d[0] + '"><option value="">All</option>' +
        options + "</select></label>";
    }).join("");
  }

  function row(x) {
    var s = score(x);
    var project = x.repo ? '<a href="' + esc(x.repo) + '">' + esc(x.name) + "</a>" : esc(x.name);
    var name = esc(x.language) + " (" + project + ")";
    var tags = x.kinds.join(" · ") + (x.verification !== "None" ? " · " + x.verification : "");
    var partial = x.state !== "done" ? ' <span class="r-partial">partial</span>' : "";
    var html = '<tr class="r-row" data-name="' + esc(x.name) + '">' +
      '<td><span class="r-name">' + name + partial + '</span><span class="r-tags">' + esc(tags) + "</span></td>" +
      '<td class="r-num">' + x.passed + "</td>" +
      '<td class="r-num' + (x.failed ? " r-bad" : "") + '">' + x.failed + "</td>" +
      '<td class="r-score"><span class="r-bar"><i style="width:' + (100 * s).toFixed(1) + '%"></i></span>' +
      '<span class="r-num">' + (100 * s).toFixed(1) + "%</span></td></tr>";
    if (open[x.name] && x.failures.length) {
      html += '<tr class="r-failures"><td colspan="4"><ul>' + x.failures.map(function (f) {
        return "<li><code>" + esc(f.case) + "</code><br>" + esc(f.reason) + "</li>";
      }).join("") + "</ul></td></tr>";
    }
    return html;
  }

  function render() {
    var rows = visible();
    var passed = 0, failed = 0, perfect = 0;
    rows.forEach(function (x) {
      passed += x.passed;
      failed += x.failed;
      if (x.state === "done" && x.failed === 0) perfect++;
    });
    root.innerHTML =
      '<div class="r-filters">' + filterControls() + "</div>" +
      '<p class="r-summary"><b>' + rows.length + "</b> of " + data.impls.length + " implementations · <b>" +
      perfect + "</b> pass every case · " + passed.toLocaleString("en") + " passed, " +
      failed.toLocaleString("en") + " failed · data from " + esc(data.now) + "</p>" +
      '<table class="r-table"><thead><tr>' + COLUMNS.map(function (c) {
        return '<th data-sort="' + c[0] + '"' + (c[0] === sortKey ? ' aria-sort="descending"' : "") + ">" +
          c[1] + "</th>";
      }).join("") + "</tr></thead><tbody>" + rows.map(row).join("") + "</tbody></table>" +
      '<p class="r-hint">Click a row to see its failing cases. Click a column header to sort.</p>';
  }

  root.addEventListener("change", function (e) {
    var key = e.target.getAttribute("data-filter");
    if (key) {
      filters[key] = e.target.value;
      render();
    }
  });

  root.addEventListener("click", function (e) {
    if (e.target.closest("a")) return;
    var th = e.target.closest("th[data-sort]");
    if (th) {
      sortKey = th.getAttribute("data-sort");
      render();
      return;
    }
    var tr = e.target.closest("tr.r-row");
    if (tr) {
      var name = tr.getAttribute("data-name");
      open[name] = !open[name];
      render();
    }
  });

  fetch(root.getAttribute("data-src"), { cache: "no-cache" })
    .then(function (r) {
      if (!r.ok) throw new Error(r.status + " " + r.statusText);
      return r.json();
    })
    .then(function (json) {
      data = { now: String(json.now), impls: [].concat(json.impls || []).map(normalize) };
      render();
    })
    .catch(function (err) {
      root.insertAdjacentHTML("beforeend", "<p>Could not load the results: " + esc(err.message) + "</p>");
    });
})();
