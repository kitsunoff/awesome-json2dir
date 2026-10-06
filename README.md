<div align="center">

# Awesome json2dir [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**A curated list of implementations, ports, rewrites and heresies of [`json2dir`](https://github.com/alurm/json2dir).**

*One JSON object in. One directory tree out. Many languages, many opinions.*

[![Projects](https://img.shields.io/badge/projects-9-blueviolet?style=flat-square)](#contents)
[![Languages](https://img.shields.io/badge/languages-Rust%20%C2%B7%20Zig%20%C2%B7%20C%23%20%C2%B7%20Scheme%20%C2%B7%20Go%20%C2%B7%20MSBuild-orange?style=flat-square)](#ports-and-rewrites)
[![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-lightgrey?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)

</div>

---

```text
{                                              .
  "greeting": "Hello, world!",                 ├── greeting      "Hello, world!"
  "dir": {                                     ├── dir/
    "subfile": "Content.\n",       json2dir    │   ├── subfile   "Content.\n"
    "subdir": {}                  ─────────▶   │   └── subdir/
  },                                           ├── symlink ──▶ target path
  "symlink": ["link", "target path"],          └── script*       #!/bin/sh …
  "script": ["script", "#!/bin/sh\necho Howdy!"]
}
```

## Contents

- [The format](#the-format)
- [Reference implementation](#reference-implementation)
- [Ports and rewrites](#ports-and-rewrites)
- [Alternative takes](#alternative-takes)
- [Inverse tools](#inverse-tools)
- [Rebuttals](#rebuttals)
- [At a glance](#at-a-glance)
- [Wanted](#wanted)
- [Contributing](#contributing)

## The format

Every implementation in this list speaks the same conversion scheme, defined by the original `json2dir`:

| JSON value | Filesystem entry |
| --- | --- |
| Object | Directory, populated recursively |
| String | Regular file with exactly that content |
| `["link", "target"]` | Symbolic link pointing to `target` |
| `["script", "content"]` | File with the executable bit set |

The root of the document must be an object. See the [upstream conversion scheme](https://github.com/alurm/json2dir#conversion-scheme) for the full rules.

## Reference implementation

- [alurm/json2dir](https://github.com/alurm/json2dir) ![Rust](https://img.shields.io/badge/-Rust-000000?style=flat-square&logo=rust&logoColor=white) - The original. Directory archives, made human-readable. Ships a Nix flake and a guide for [managing dotfiles with `nix profile`](https://github.com/alurm/json2dir/blob/main/home.md) as a `home-manager` replacement.

## Ports and rewrites

- [71g3pf4c3/json2dir-zig](https://github.com/71g3pf4c3/json2dir-zig) ![Zig](https://img.shields.io/badge/-Zig-F7A41D?style=flat-square&logo=zig&logoColor=white) - From-scratch, drop-in compatible rewrite focused on safety: never follows symlinks on the way down (`O_NOFOLLOW`, `AT_SYMLINK_NOFOLLOW`), adds a dry-run mode and a target directory flag, and builds as a single static binary with no libc.
- [TheMaxMur/json2dir-scheme](https://github.com/TheMaxMur/json2dir-scheme) ![Scheme](https://img.shields.io/badge/-Guile%20Scheme-3B5BA5?style=flat-square&logo=gnu&logoColor=white) - Guile Scheme port that preserves the original Unix behavior, with its own JSON parser built on Guile 3.0 standard modules only. Packaged as a Nix flake.
- [daniilvaino/json2dir-cs](https://github.com/daniilvaino/json2dir-cs) ![C#](https://img.shields.io/badge/-C%23-512BD4?style=flat-square&logo=dotnet&logoColor=white) - The whole tool as a single C# expression: `System.Text.Json`, LINQ and a self-applied recursive lambda.
- [daniilvaino/json2dir-msbuild](https://github.com/daniilvaino/json2dir-msbuild) ![MSBuild](https://img.shields.io/badge/-MSBuild-512BD4?style=flat-square&logo=dotnet&logoColor=white) - A single MSBuild project file. No C#, no inline tasks, no `Exec`: JSON is parsed with .NET regex balancing groups, and recursion goes through the `<MSBuild>` task calling its own project.

## Alternative takes

- [lcensies/json2llm](https://github.com/lcensies/json2llm) ![Go](https://img.shields.io/badge/-Go-00ADD8?style=flat-square&logo=go&logoColor=white) - Same JSON in, same tree out, except a language model does the compiling. Go validates the model's plan and performs the writes. Backends: OpenAI-compatible API, `claude`, `codex`, `opencode`, `pi`, or `local` for the cowards.

## Inverse tools

- [71g3pf4c3/dir2json](https://github.com/71g3pf4c3/dir2json) ![Rust](https://img.shields.io/badge/-Rust-000000?style=flat-square&logo=rust&logoColor=white) - The scheme in reverse: walks a directory and prints a `json2dir`-compatible JSON object. Never follows symlinks.

## Rebuttals

Projects that exist to explain why `json2dir` should not.

- [71g3pf4c3/json2json](https://github.com/71g3pf4c3/json2json) ![Rust](https://img.shields.io/badge/-Rust-000000?style=flat-square&logo=rust&logoColor=white) - Reads JSON and writes the same JSON back, preserving key order, duplicate keys and number forms. Argues that `json → dir → json` is a round-trip best done in one step.
- [71g3pf4c3/dir2dir](https://github.com/71g3pf4c3/dir2dir) ![README only](https://img.shields.io/badge/-README%20only-lightgrey?style=flat-square) - A manifesto for copying directory trees through a typed intermediate representation, with plans, diffs and dry-runs. No code yet.

## At a glance

| Project | Language | Direction | License |
| --- | --- | --- | --- |
| [json2dir](https://github.com/alurm/json2dir) | Rust | JSON → dir | ISC |
| [json2dir-zig](https://github.com/71g3pf4c3/json2dir-zig) | Zig | JSON → dir | GPL-3.0 |
| [json2dir-scheme](https://github.com/TheMaxMur/json2dir-scheme) | Guile Scheme | JSON → dir | ISC |
| [json2dir-cs](https://github.com/daniilvaino/json2dir-cs) | C# | JSON → dir | Unlicense |
| [json2dir-msbuild](https://github.com/daniilvaino/json2dir-msbuild) | MSBuild | JSON → dir | Unlicense |
| [json2llm](https://github.com/lcensies/json2llm) | Go + LLM | JSON → LLM → dir | None specified |
| [dir2json](https://github.com/71g3pf4c3/dir2json) | Rust | dir → JSON | GPL-3.0 |
| [json2json](https://github.com/71g3pf4c3/json2json) | Rust | JSON → JSON | GPL-3.0 |
| [dir2dir](https://github.com/71g3pf4c3/dir2dir) | none yet | dir → dir | GPL-3.0 |

## Wanted

Implementations that have been requested but do not exist yet. Be the first:

- [ ] Haskell
- [ ] Nix (pure evaluation, `builtins` only)
- [ ] Assembly
- [ ] A test harness that checks every implementation against the same fixtures

## Contributing

Wrote your own `json2dir`? Open a pull request. Read the [contribution guidelines](CONTRIBUTING.md) first.

---

<div align="center">

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related rights to this work.

</div>
