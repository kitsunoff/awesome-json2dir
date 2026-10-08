# Results

Every implementation from this list that can be built and run on Linux, tested with the same black-box cases by [json2dir-tester](https://github.com/json2dir-guru/json2dir-tester). The cases are this list's [conformance suite](../conformance/README.md), cases collected from other implementations' own test suites, and a security set: nothing may be written outside the target directory. Each implementation is built from its own repository with its own toolchain, and the resulting directory tree is compared with the expected one.

<div id="results" data-src="results.json">
  <p>The interactive table needs JavaScript. The raw data is in <a href="results.json">results.json</a>.</p>
</div>

<script src="results.js" defer></script>

## Performance

The latest benchmark campaign compares complete CLI invocations, including runtime
startup, parsing and filesystem operations. Disk and RAM-backed tmpfs results are
separate; disk times measure buffered writes through process exit, without `fsync`.
Each output is verified before its measurements enter a comparison.

Select a workload to compare median time and its interquartile range, throughput,
CPU time and maximum process RSS. RSS measures the largest process, not combined
process-tree memory. Each timing starts a fresh process after discarded warmups.
There is no combined score: startup, many small files and large payloads exercise
different costs. Ratios compare implementations within the same campaign and
storage condition; they are not regression verdicts across different machines.

<link rel="stylesheet" href="benchmarks.css">

<div id="benchmarks" data-src="benchmarks.json">
  <p>The interactive comparison needs JavaScript.</p>
</div>

<script src="benchmarks.js" defer></script>

[Summary data](benchmarks.json) · [Raw samples](benchmark-samples.json)

## Updating

The page renders [`results.json`](results.json) and nothing else, so replacing that file is the whole update. The tester writes it from a test campaign:

```sh
json2dir-tester export --dir <campaign directory> --out <directory>
cp <directory>/results.json results/results.json
```

Benchmark data follows the same export-and-replace pipeline. Download a benchmark
campaign artifact from the tester, then export and update both files together:

```sh
json2dir-tester bench-export --dir <campaign directory> --out <directory>
cp <directory>/benchmarks.json <directory>/benchmark-samples.json results/
```

Submit the data update through a PR; the existing Pages workflow publishes it.
Only the latest campaign is shown here. See the tester's
[benchmark methodology](https://github.com/json2dir-guru/json2dir-tester/blob/main/docs/benchmarks.md)
for workloads, limits and reproduction using the exported lock.
