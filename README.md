<div align="center">

# Awesome json2dir [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**A curated list of implementations, ports, rewrites and heresies of [`json2dir`](https://github.com/alurm/json2dir).**

*One JSON object in. One directory tree out. Many languages, many opinions.*

**[Website](https://kitsunoff.github.io/awesome-json2dir/) · [RFC J2D-1](spec/rfc-json2dir.md) · [Conformance suite](conformance/README.md) · [Manifesto](MANIFESTO.md)**

[![Projects](https://img.shields.io/badge/projects-25-blueviolet?style=flat-square)](#contents)
[![Languages](https://img.shields.io/badge/languages-Rust%20%C2%B7%20Zig%20%C2%B7%20C%23%20%C2%B7%20Scheme%20%C2%B7%20Go%20%C2%B7%20MSBuild%20%C2%B7%20Nix%20%C2%B7%20Lean%20%C2%B7%20LLVM%20IR%20%C2%B7%20F%2A%20%C2%B7%20Agda%20%C2%B7%20ATS%20%C2%B7%20Brainfuck%20%C2%B7%20bimbo--lang%20%C2%B7%20Haskell%20%C2%B7%20Typst%20%C2%B7%20Python%20%C2%B7%20Shell-orange?style=flat-square)](#ports-and-rewrites)
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
- [Specification and tests](#specification-and-tests)
- [Reference implementation](#reference-implementation)
- [Ports and rewrites](#ports-and-rewrites)
- [Alternative takes](#alternative-takes)
- [Inverse tools](#inverse-tools)
- [Tooling](#tooling)
- [Rebuttals](#rebuttals)
- [At a glance](#at-a-glance)
- [Wanted](#wanted)
- [Contributing](#contributing)

## The format

Every implementation in this list speaks the same conversion scheme, defined by the original `json2dir` and specified in [RFC J2D-1](spec/rfc-json2dir.md):

| JSON value | Filesystem entry |
| --- | --- |
| Object | Directory, populated recursively |
| String | Regular file with exactly that content |
| `["link", "target"]` | Symbolic link pointing to `target` |
| `["script", "content"]` | File with the executable bit set |

The root of the document must be an object. See [RFC J2D-1](spec/rfc-json2dir.md) for the full rules.

## Specification and tests

- [RFC J2D-1](spec/rfc-json2dir.md) - The format, the processing model and the security rules, written down with MUST and SHOULD.
- [Conformance suite](conformance/README.md) - 68 language-agnostic test cases and a runner. Point it at any implementation: `python3 conformance/run.py /path/to/json2dir`.
- [Manifesto](MANIFESTO.md) - Why a tree is a value, and why four shapes are enough.

## Reference implementation

- [alurm/json2dir](https://github.com/alurm/json2dir) ![Rust](https://img.shields.io/badge/-Rust-000000?style=flat-square&logo=rust&logoColor=white) - The original. Directory archives, made human-readable. Ships a Nix flake and a guide for [managing dotfiles with `nix profile`](https://github.com/alurm/json2dir/blob/main/home.md) as a `home-manager` replacement.

## Ports and rewrites

- [71g3pf4c3/json2dir-zig](https://github.com/71g3pf4c3/json2dir-zig) ![Zig](https://img.shields.io/badge/-Zig-F7A41D?style=flat-square&logo=zig&logoColor=white) - From-scratch, drop-in compatible rewrite focused on safety: never follows symlinks on the way down (`O_NOFOLLOW`, `AT_SYMLINK_NOFOLLOW`), adds a dry-run mode and a target directory flag, and builds as a single static binary with no libc.
- [TheMaxMur/json2dir-scheme](https://github.com/TheMaxMur/json2dir-scheme) ![Scheme](https://img.shields.io/badge/-Guile%20Scheme-3B5BA5?style=flat-square&logo=gnu&logoColor=white) - Guile Scheme port that preserves the original Unix behavior, with its own JSON parser built on Guile 3.0 standard modules only. Packaged as a Nix flake.
- [daniilvaino/json2dir-cs](https://github.com/daniilvaino/json2dir-cs) ![C#](https://img.shields.io/badge/-C%23-512BD4?style=flat-square&logo=dotnet&logoColor=white) - The whole tool as a single C# expression: `System.Text.Json`, LINQ and a self-applied recursive lambda.
- [daniilvaino/json2dir-msbuild](https://github.com/daniilvaino/json2dir-msbuild) ![MSBuild](https://img.shields.io/badge/-MSBuild-512BD4?style=flat-square&logo=dotnet&logoColor=white) - A single MSBuild project file. No C#, no inline tasks, no `Exec`: JSON is parsed with .NET regex balancing groups, and recursion goes through the `<MSBuild>` task calling its own project.
- [TheMaxMur/json2dir-nix](https://github.com/TheMaxMur/json2dir-nix) ![Nix](https://img.shields.io/badge/-Nix-5277C3?style=flat-square&logo=nixos&logoColor=white) - JSON parsing, validation and traversal in `lib.nix` using only Nix builtins; a small shell launcher runs the generated filesystem operations, since evaluation cannot write files. Validates the whole tree before touching the destination. Also a library: `mkTree` builds a tree into the Nix store as a derivation.
- [tsalkenov/json2dir-lean](https://github.com/tsalkenov/json2dir-lean) ![Lean 4](https://img.shields.io/badge/-Lean%204-000000?style=flat-square) - Lean 4 port whose key parsing and value classification are pure functions with proofs: every accepted key is one nonempty relative component without `.` or `..`, and each JSON form maps to the intended operation. Filesystem effects are not covered by the proofs.
- [TheMaxMur/json2dir-llvm-IR](https://github.com/TheMaxMur/json2dir-llvm-IR) ![LLVM IR](https://img.shields.io/badge/-LLVM%20IR-262D3A?style=flat-square&logo=llvm&logoColor=white) - Handwritten textual LLVM IR: JSON parser, UTF-8 handling, key sorting and tree creation, linked only against libc. Differentially tested against the Rust original on 2460 input and directory-state combinations.
- [TheMaxMur/json2dir-F-](https://github.com/TheMaxMur/json2dir-F-) ![F\*](https://img.shields.io/badge/-F%2A-1B4F72?style=flat-square) - The whole CLI written in F\* and extracted to OCaml: JSON parser, UTF-8 handling, path checks and tree traversal. Ports every theorem from json2dir-lean's `Spec.lean` as F\* lemmas checked with Z3, without `admit`. Differentially tested against the Rust original.
- [TheMaxMur/json2dir-agda](https://github.com/TheMaxMur/json2dir-agda) ![Agda](https://img.shields.io/badge/-Agda-5E5086?style=flat-square) - JSON parser, name checks, duplicate handling, ordering and traversal written in Agda and compiled through the GHC backend; only small `COMPILE GHC` bindings for IO are handwritten. Pure modules use `--safe`, and the name checker and classifier carry proofs that follow json2dir-lean's specification.
- [TheMaxMur/json2dir-ats](https://github.com/TheMaxMur/json2dir-ats) ![ATS](https://img.shields.io/badge/-ATS2-4A4A4A?style=flat-square) - ATS2 port with the JSON parser, Unicode decoder, key sorting, path validation and tree writer in one `main.dats`. Owned trees and buffers use linear types and are freed explicitly, with no garbage collector. Documents its compatibility with the Rust original rule by rule.
- [TheMaxMur/json2dir-bimbo](https://github.com/TheMaxMur/json2dir-bimbo) ![bimbo-lang](https://img.shields.io/badge/-%F0%9F%92%85%20bimbo--lang-E75480?style=flat-square) - A new compiled language built for one mission: rewriting json2dir. The JSON parser and tree walk live in `src/json2dir.bimbo`; a Python frontend emits LLVM IR, and a small C runtime supplies strings, maps and POSIX calls. Functions are `bestie`, loops `strut`, returns `gimme`.
- [KovalevDima/json2dir-hs](https://github.com/KovalevDima/json2dir-hs) ![Haskell](https://img.shields.io/badge/-Haskell-5D4F85?style=flat-square&logo=haskell&logoColor=white) ![No AI](https://img.shields.io/badge/%E2%9C%8B%20handwritten-no%20AI-black?style=flat-square) - Written by HAND, no LLMs, according to its author. A one-file Haskell take on the scheme with `aeson` and `directory`. Looser than [RFC J2D-1](spec/rfc-json2dir.md): names are joined as paths without validation, scripts get no execute bit, and numbers, booleans and `null` are written to files instead of rejected.
- [TheMaxMur/json2dir-thesis](https://github.com/TheMaxMur/json2dir-thesis) ![Typst](https://img.shields.io/badge/-Typst-239DAD?style=flat-square&logo=typst&logoColor=white) - The converter written in Typst: validation, traversal, planning and shell quoting live in `.typ` files, and Typst's bundle export emits a shell program that a small launcher runs. Validates the whole tree first, rejects every key with a slash, and offers `--plan` and `--emit` dry runs. Ships with a satirical PhD dissertation and diploma in Doctor of Philosophical Directories.

## Alternative takes

- [lcensies/json2llm](https://github.com/lcensies/json2llm) ![Go](https://img.shields.io/badge/-Go-00ADD8?style=flat-square&logo=go&logoColor=white) - Same JSON in, same tree out, except a language model does the compiling. Go validates the model's plan and performs the writes. Backends: OpenAI-compatible API, `claude`, `codex`, `opencode`, `pi`, or `local` for the cowards.
- [71g3pf4c3/kube-operator2dir](https://github.com/71g3pf4c3/kube-operator2dir) ![Go](https://img.shields.io/badge/-Go-00ADD8?style=flat-square&logo=go&logoColor=white) ![Kubernetes](https://img.shields.io/badge/-Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white) - The scheme as a Kubernetes operator: a cluster-scoped `DirTree` resource holds the tree, and a DaemonSet agent materializes it on nodes matched by `nodeSelector`. Replaces instead of merging, reverts external drift on a resync and prunes the tree when the resource is deleted.
- [71g3pf4c3/zakon2dir](https://github.com/71g3pf4c3/zakon2dir) ![DOCX only](https://img.shields.io/badge/-DOCX%20only-lightgrey?style=flat-square) - The scheme as a parody Russian federal constitutional law, in a `.docx`: objects, strings, links and scripts as articles, plus the right to reverse conversion and `dir2json --check` exit codes as legal facts. Has no legal force.
- [71g3pf4c3/brainfuck2dir](https://github.com/71g3pf4c3/brainfuck2dir) ![Brainfuck](https://img.shields.io/badge/-Brainfuck-2F2F2F?style=flat-square) - The scheme as an output format for brainfuck: runs of a command become files and loops become directories. The converter itself is about 94 KB of brainfuck, generated by a macro assembler and run by a Zig VM.
- [71g3pf4c3/json2philosophy](https://github.com/71g3pf4c3/json2philosophy) ![PDF](https://img.shields.io/badge/-PDF%20book-lightgrey?style=flat-square) - *Being and JSON*, a 51-page book in Russian on the ontology of conversion: Plato's two worlds as eidos and inode, Heidegger's Dasein of the user, and `--check` exit code 3 as the call of conscience. Built from HTML with WeasyPrint.
- [71g3pf4c3/voice2dir](https://github.com/71g3pf4c3/voice2dir) ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) - Dictate a tree in Russian: whisper transcribes the audio, a deterministic DSL parser turns it into a json2dir document, the tree is created and then checked by reading it back. Takes any audio ffmpeg can decode, or the microphone.
- [71g3pf4c3/json2dir](https://github.com/71g3pf4c3/json2dir) ![Novella](https://img.shields.io/badge/-Novella-lightgrey?style=flat-square) - *J son's plan to become a director*: a Russian novella in a prologue, eight chapters and an epilogue about J's son, a value at `J/son`, who leaves the house of braces to become a directory.

## Inverse tools

- [71g3pf4c3/dir2json](https://github.com/71g3pf4c3/dir2json) ![Rust](https://img.shields.io/badge/-Rust-000000?style=flat-square&logo=rust&logoColor=white) - The scheme in reverse: walks a directory and prints a `json2dir`-compatible JSON object. Never follows symlinks.

## Tooling

- [lcensies/json2slop](https://github.com/lcensies/json2slop) ![Shell](https://img.shields.io/badge/-Shell-4EAA25?style=flat-square&logo=gnubash&logoColor=white) ![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white) - One CLI and one container image in front of the other implementations: pick a backend with `-b` (`rust`, `zig`, `scheme`, `cs`, `llm`) or run `reverse` through `dir2json`. Options a backend cannot honour are a usage error, never silently dropped. Includes a smoke test that applies the same fixtures with every backend and compares the trees.

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
| [json2dir-nix](https://github.com/TheMaxMur/json2dir-nix) | Nix | JSON → dir | ISC |
| [json2dir-lean](https://github.com/tsalkenov/json2dir-lean) | Lean 4 | JSON → dir | WTFPL |
| [json2dir-llvm-IR](https://github.com/TheMaxMur/json2dir-llvm-IR) | LLVM IR | JSON → dir | ISC |
| [json2dir-F-](https://github.com/TheMaxMur/json2dir-F-) | F\* | JSON → dir | ISC |
| [json2dir-agda](https://github.com/TheMaxMur/json2dir-agda) | Agda | JSON → dir | ISC |
| [json2dir-ats](https://github.com/TheMaxMur/json2dir-ats) | ATS2 | JSON → dir | ISC |
| [json2dir-bimbo](https://github.com/TheMaxMur/json2dir-bimbo) | bimbo-lang → LLVM IR | JSON → dir | ISC |
| [json2dir-hs](https://github.com/KovalevDima/json2dir-hs) | Haskell | JSON → dir | BSD-3-Clause |
| [json2dir-thesis](https://github.com/TheMaxMur/json2dir-thesis) | Typst | JSON → dir | ISC |
| [json2llm](https://github.com/lcensies/json2llm) | Go + LLM | JSON → LLM → dir | None specified |
| [kube-operator2dir](https://github.com/71g3pf4c3/kube-operator2dir) | Go + Kubernetes | CR → node dirs | Apache-2.0 (per README) |
| [zakon2dir](https://github.com/71g3pf4c3/zakon2dir) | Russian legalese | JSON ⇄ dir, by law | GPL-3.0 |
| [brainfuck2dir](https://github.com/71g3pf4c3/brainfuck2dir) | Brainfuck + Zig | brainfuck → JSON → dir | GPL-3.0 |
| [json2philosophy](https://github.com/71g3pf4c3/json2philosophy) | Russian prose | JSON → Being | GPL-3.0 |
| [voice2dir](https://github.com/71g3pf4c3/voice2dir) | Python + whisper | voice → JSON → dir | GPL-3.0 |
| [json2dir (novella)](https://github.com/71g3pf4c3/json2dir) | Russian prose | J/son → director | None specified |
| [json2slop](https://github.com/lcensies/json2slop) | Shell + Docker | JSON → any backend → dir | None specified |
| [dir2json](https://github.com/71g3pf4c3/dir2json) | Rust | dir → JSON | GPL-3.0 |
| [json2json](https://github.com/71g3pf4c3/json2json) | Rust | JSON → JSON | GPL-3.0 |
| [dir2dir](https://github.com/71g3pf4c3/dir2dir) | none yet | dir → dir | GPL-3.0 |

## Wanted

Implementations that have been requested but do not exist yet. Be the first:

- [x] Haskell: [json2dir-hs](https://github.com/KovalevDima/json2dir-hs)
- [x] Nix (pure evaluation, `builtins` only): [json2dir-nix](https://github.com/TheMaxMur/json2dir-nix), with a shell launcher for the writes
- [ ] Assembly
- [ ] JS
- [ ] TS
- [ ] Wasm (Bun)
- [ ] jsonscript (Node)
- [ ] Jsonnet (launcher approach)
- [ ] JScript (Wine)
- [ ] CMake
- [ ] Lisp (Emacs Lisp)
- [ ] LuaJIT
- [ ] Zsh
- [ ] Bat
- [ ] Pwsh
- [ ] Puppet
- [ ] Ansible
- [ ] LuaTeX (launcher approach)
- [ ] Vim (launcher approach)
- [ ] Java
- [ ] Python
- [ ] Ruby
- [ ] PHP
- [ ] nginx njs + WebDAV (self recursion with requests)
- [x] A test harness that checks every implementation against the same fixtures: the [conformance suite](conformance/README.md)

## Contributing

Wrote your own `json2dir`? Run the [conformance suite](conformance/README.md) against it, then open a pull request. Read the [contribution guidelines](CONTRIBUTING.md) first.

---

<div align="center">

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related rights to this work.

</div>
