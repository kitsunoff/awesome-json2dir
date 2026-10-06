# json2dir Conformance Suite

A language-agnostic test suite for implementations of the [json2dir format](../spec/rfc-json2dir.md).

It feeds JSON documents to an implementation, then compares the directory tree it produced with the expected tree. Each case cites the RFC section it checks.

## Requirements

- Python 3.9 or newer, standard library only.
- A POSIX system: Linux or macOS.

## Running

The runner executes `COMMAND` with `/bin/sh` inside an empty target directory and passes the document on standard input. This is the interface of the reference implementation:

```bash
python3 conformance/run.py json2dir
```

Use absolute paths in `COMMAND`. The command runs inside a temporary directory, so relative paths do not resolve.

If an implementation reads a file or writes to a given directory, use the placeholders:

| Placeholder | Replaced with |
| --- | --- |
| `{input}` | Path to a file holding the input document |
| `{output}` | Path to the target directory |

```bash
python3 conformance/run.py '/path/to/json2dir -o {output} {input}'
```

### Options

| Option | Meaning |
| --- | --- |
| `--level core` | Run one conformance level only. Repeat for several |
| `--filter TEXT` | Run cases whose name contains `TEXT` |
| `--timeout SECONDS` | Time limit per case. Default: 10 |
| `--json FILE` | Also write results as JSON |
| `--verbose` | Print standard error of failing cases |

The exit status is 0 when every selected case passes and 1 otherwise.

### Example output

```text
✓ core/001-empty-object An empty object produces nothing
✓ core/002-regular-file A string becomes a regular file
✗ overwrite/207-file-does-not-follow-symlink Writing a file over a symlink replaces the link and leaves its target intact
    real: expected "secret", got "pwned"; victim: expected "pwned", got ["link", "real"]  [RFC §5.3]

core       52/52 passed — conformant
overwrite  15/16 passed — not conformant
```

## Conformance levels

| Level | Checks | RFC |
| --- | --- | --- |
| `core` | Parsing, the conversion scheme, name and value validation | Sections 3 and 4 |
| `overwrite` | Behavior when the target directory already has content | Section 5 |

An implementation is **core-conformant** when it passes every `core` case, and **fully conformant** when it passes both levels.

## How results are judged

1. Success cases must exit with status 0 and produce exactly the expected tree.
2. Error cases must exit with a non-zero status. The tree left behind is not checked: the RFC allows partial results on error.
3. Every case fails if the implementation creates anything outside the target directory.
4. Cases marked `accept_error` pass on either the expected tree or a non-zero exit.

The runner reads the produced tree back in the json2dir scheme itself:

| Found on disk | Read as |
| --- | --- |
| Directory | Object |
| Regular file without execute bits | String |
| Regular file with all three execute bits | `["script", content]` |
| Symbolic link | `["link", target]`, never followed |
| Regular file with some execute bits | `["mode", "0744", content]`, never matches |
| File that is not UTF-8 | `["bytes", base64]`, never matches |

## Case format

Cases live in [`cases/`](cases), one JSON file per case:

```json
{
  "description": "Writing a file over a symlink replaces the link and leaves its target intact",
  "section": "5.3",
  "level": "overwrite",
  "setup": { "real": "secret", "victim": ["link", "real"] },
  "input": { "victim": "pwned" },
  "expect": { "tree": { "real": "secret", "victim": "pwned" } }
}
```

| Field | Required | Meaning |
| --- | --- | --- |
| `description` | Yes | One sentence describing the behavior |
| `section` | Yes | RFC section the case checks |
| `level` | Yes | `core` or `overwrite` |
| `setup` | No | Tree created in the target directory before the run |
| `input` | One of three | Document as a JSON value |
| `input_text` | One of three | Document as raw text, for invalid JSON or duplicate names |
| `input_base64` | One of three | Document as base64 bytes, for invalid UTF-8 |
| `expect.tree` | One of two | Expected tree after a successful run |
| `expect.error` | One of two | `true` when the run must fail |
| `expect.accept_error` | No | With `tree`: a non-zero exit is also accepted |

## Self-test

The suite tests itself against [`selftest/model.py`](selftest/model.py), a step-by-step Python model of the reference implementation:

```bash
python3 -m unittest discover --start-directory conformance
```

The model is a test oracle, not a recommended implementation.
