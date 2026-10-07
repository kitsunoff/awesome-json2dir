<div align="center">

# Awesome json2dir [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**A curated list of implementations, ports, rewrites and heresies of [`json2dir`](https://github.com/alurm/json2dir).**

*One JSON object in. One directory tree out. Many languages, many opinions.*

**[Website](https://kitsunoff.github.io/awesome-json2dir/) · [RFC J2D-1](spec/rfc-json2dir.md) · [Conformance suite](conformance/README.md) · [Manifesto](MANIFESTO.md)**

[![Projects](https://img.shields.io/badge/projects-167-blueviolet?style=flat-square)](#contents)
[![Languages](https://img.shields.io/badge/languages-Rust%20%C2%B7%20Zig%20%C2%B7%20C%23%20%C2%B7%20Scheme%20%C2%B7%20Go%20%C2%B7%20MSBuild%20%C2%B7%20Nix%20%C2%B7%20Lean%20%C2%B7%20LLVM%20IR%20%C2%B7%20F%2A%20%C2%B7%20Agda%20%C2%B7%20ATS%20%C2%B7%20Brainfuck%20%C2%B7%20bimbo--lang%20%C2%B7%20Haskell%20%C2%B7%20Typst%20%C2%B7%20Python%20%C2%B7%20Shell%20%C2%B7%20Ada%20%C2%B7%20Aheui%20%C2%B7%20ALGOL%2060%20%C2%B7%20ALGOL%2068%20%C2%B7%20Ansible%20%C2%B7%20APL%20%C2%B7%20ArnoldC%20%C2%B7%20x86--64%20assembly%20%C2%B7%20AWK%20%C2%B7%20Bash%20%C2%B7%20FreeBASIC%20%C2%B7%20Batch-orange?style=flat-square)](#ports-and-rewrites)
[![Languages](https://img.shields.io/badge/-BCPL%20%C2%B7%20Befunge--98%20%C2%B7%20BQN%20%C2%B7%20Braincopter%20%C2%B7%20Brainloller%20%C2%B7%20C17%20%C2%B7%20C23%20%C2%B7%20C89%20%C2%B7%20Cforall%20%C2%B7%20Checked%20C%20%C2%B7%20Chef%20%C2%B7%20Chez%20Scheme%20%C2%B7%20CIL%20%C2%B7%20Cilk%20%C2%B7%20Clojure%20%C2%B7%20CMake%20%C2%B7%20COBOL%20%C2%B7%20Common%20Lisp%20%C2%B7%20C%20%28CompCert%29%20%C2%B7%20COW%20%C2%B7%20C%2B%2B%20%C2%B7%20Crystal%20%C2%B7%20D%20%C2%B7%20Dafny%20%C2%B7%20Dart%20%C2%B7%20Eiffel%20%C2%B7%20Emacs%20Lisp%20%C2%B7%20Elixir-orange?style=flat-square)](#ports-and-rewrites)
[![Languages](https://img.shields.io/badge/-Emojicode%20%C2%B7%20Erlang%20%C2%B7%20FALSE%20%C2%B7%20Fennel%20%C2%B7%20%3E%3C%3E%20%28Fish%29%20%C2%B7%20Forth%20%C2%B7%20Fortran%20%C2%B7%20Fractran%20%C2%B7%20Free%20Pascal%20%C2%B7%20F%23%20%C2%B7%20Gleam%20%C2%B7%20GNU%20C%20%C2%B7%20Groovy%20%C2%B7%20Hare%20%C2%B7%20Hexagony%20%C2%B7%20HolyC%20%C2%B7%20Idris%202%20%C2%B7%20INTERCAL%20%C2%B7%20J%20%C2%B7%20Janet%20%C2%B7%20Java%20%C2%B7%20jq%20%C2%B7%20JavaScript%20%C2%B7%20JScript%20%C2%B7%20Jsonnet%20%C2%B7%20JSONScript%20%C2%B7%20Julia%20%C2%B7%20K-orange?style=flat-square)](#ports-and-rewrites)
[![Languages](https://img.shields.io/badge/-Koka%20%C2%B7%20Kotlin%20%C2%B7%20K%26R%20C%20%C2%B7%20ksh93%20%C2%B7%20Logo%20%C2%B7%20LOLCODE%20%C2%B7%20Lua%20%C2%B7%20LuaJIT%20%C2%B7%20LuaTeX%20%C2%B7%20Malbolge%20Unshackled%20%C2%B7%20Mercury%20%C2%B7%20Modula--2%20%C2%B7%20Mojo%20%C2%B7%20Neovim%20Lua%20%C2%B7%20Nim%20%C2%B7%20nginx%20njs%20%C2%B7%20Objective--C%20%C2%B7%20OCaml%20%C2%B7%20MATLAB%2FOctave%20%C2%B7%20Odin%20%C2%B7%20Ook%21%20%C2%B7%20Perl%20%C2%B7%20PHP%20%C2%B7%20Piet%20%C2%B7%20Pikachu%20%C2%B7%20PL%2FI%20%C2%B7%20Pony-orange?style=flat-square)](#ports-and-rewrites)
[![Languages](https://img.shields.io/badge/-Prolog%20%C2%B7%20Puppet%20%C2%B7%20PureScript%20%C2%B7%20PowerShell%20%C2%B7%20R%20%C2%B7%20Racket%20%C2%B7%20Raku%20%C2%B7%20REXX%20%C2%B7%20Roc%20%C2%B7%20Rockstar%20%C2%B7%20Rocq%20%C2%B7%20Ruby%20%C2%B7%20Scala%20%C2%B7%20sed%20%C2%B7%20Shakespeare%20%C2%B7%20Smalltalk%20%C2%B7%20Standard%20ML%20%C2%B7%20SNOBOL4%20%C2%B7%20SQL%20%C2%B7%20Subleq%20%C2%B7%20Swift%20%C2%B7%20SystemVerilog%20%C2%B7%20Taxi%20%C2%B7%20Tcl%20%C2%B7%20Thue%20%C2%B7%20TypeScript%20%C2%B7%20Unicon%20%C2%B7%20Unlambda-orange?style=flat-square)](#ports-and-rewrites)
[![Languages](https://img.shields.io/badge/-V%20%C2%B7%20Vala%20%C2%B7%20VB.NET%20%C2%B7%20VBScript%20%C2%B7%20Velato%20%C2%B7%20VHDL%20%C2%B7%20Vim%20script%20%C2%B7%20WebAssembly%20%C2%B7%20Whitespace%20%C2%B7%20WhyML%20%C2%B7%20XSLT%20%C2%B7%20zsh-orange?style=flat-square)](#ports-and-rewrites)
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
- [json2dir-guru/json2dir-ada](https://github.com/json2dir-guru/json2dir-ada) ![Ada](https://img.shields.io/badge/-Ada-0F766E?style=flat-square) - json2dir in Ada. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-aheui](https://github.com/json2dir-guru/json2dir-aheui) ![Aheui](https://img.shields.io/badge/-Aheui-5D4F85?style=flat-square) - json2dir in Aheui, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-algol60](https://github.com/json2dir-guru/json2dir-algol60) ![ALGOL 60](https://img.shields.io/badge/-ALGOL%2060-374151?style=flat-square) - json2dir in ALGOL 60, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-algol68](https://github.com/json2dir-guru/json2dir-algol68) ![ALGOL 68](https://img.shields.io/badge/-ALGOL%2068-374151?style=flat-square) - json2dir in ALGOL 68, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-ansible](https://github.com/json2dir-guru/json2dir-ansible) ![Ansible](https://img.shields.io/badge/-Ansible-0F766E?style=flat-square) - json2dir in Ansible. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-aot](https://github.com/json2dir-guru/json2dir-aot) ![C#](https://img.shields.io/badge/-C%23-6D28D9?style=flat-square) - json2dir in C#, .NET 8 Native AOT. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-apl](https://github.com/json2dir-guru/json2dir-apl) ![APL](https://img.shields.io/badge/-APL-BE185D?style=flat-square) - json2dir in APL, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-arnoldc](https://github.com/json2dir-guru/json2dir-arnoldc) ![ArnoldC](https://img.shields.io/badge/-ArnoldC-6D28D9?style=flat-square) - json2dir in ArnoldC, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-asm](https://github.com/json2dir-guru/json2dir-asm) ![x86-64 assembly](https://img.shields.io/badge/-x86--64%20assembly-374151?style=flat-square) - json2dir in x86-64 assembly (JWasm). Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-awk](https://github.com/json2dir-guru/json2dir-awk) ![AWK](https://img.shields.io/badge/-AWK-5D4F85?style=flat-square) - json2dir in AWK, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-bash](https://github.com/json2dir-guru/json2dir-bash) ![Bash](https://img.shields.io/badge/-Bash-B91C1C?style=flat-square) - json2dir in Bash, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-basic](https://github.com/json2dir-guru/json2dir-basic) ![FreeBASIC](https://img.shields.io/badge/-FreeBASIC-B91C1C?style=flat-square) - json2dir in BASIC (FreeBASIC). Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-bat](https://github.com/json2dir-guru/json2dir-bat) ![Batch](https://img.shields.io/badge/-Batch-6D28D9?style=flat-square) - json2dir in cmd.exe batch. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-bcpl](https://github.com/json2dir-guru/json2dir-bcpl) ![BCPL](https://img.shields.io/badge/-BCPL-B91C1C?style=flat-square) - json2dir in BCPL, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-befunge](https://github.com/json2dir-guru/json2dir-befunge) ![Befunge-98](https://img.shields.io/badge/-Befunge--98-C2410C?style=flat-square) - json2dir in Befunge-98, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-bqn](https://github.com/json2dir-guru/json2dir-bqn) ![BQN](https://img.shields.io/badge/-BQN-0E7490?style=flat-square) - json2dir in BQN. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-braincopter](https://github.com/json2dir-guru/json2dir-braincopter) ![Braincopter](https://img.shields.io/badge/-Braincopter-374151?style=flat-square) - json2dir in Braincopter, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-brainfuck](https://github.com/json2dir-guru/json2dir-brainfuck) ![Brainfuck](https://img.shields.io/badge/-Brainfuck-5D4F85?style=flat-square) - json2dir in Brainfuck, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-brainloller](https://github.com/json2dir-guru/json2dir-brainloller) ![Brainloller](https://img.shields.io/badge/-Brainloller-C2410C?style=flat-square) - json2dir in Brainloller, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-c17](https://github.com/json2dir-guru/json2dir-c17) ![C17](https://img.shields.io/badge/-C17-0E7490?style=flat-square) - json2dir in C17. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-c23](https://github.com/json2dir-guru/json2dir-c23) ![C23](https://img.shields.io/badge/-C23-BE185D?style=flat-square) - json2dir in C23. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-c89](https://github.com/json2dir-guru/json2dir-c89) ![C89](https://img.shields.io/badge/-C89-5D4F85?style=flat-square) - json2dir in ANSI C (C89). Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-cforall](https://github.com/json2dir-guru/json2dir-cforall) ![Cforall](https://img.shields.io/badge/-Cforall-6D28D9?style=flat-square) - json2dir in Cforall. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-checkedc](https://github.com/json2dir-guru/json2dir-checkedc) ![Checked C](https://img.shields.io/badge/-Checked%20C-C2410C?style=flat-square) - json2dir in Checked C. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-chef](https://github.com/json2dir-guru/json2dir-chef) ![Chef](https://img.shields.io/badge/-Chef-A16207?style=flat-square) - json2dir in Chef, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-chez](https://github.com/json2dir-guru/json2dir-chez) ![Chez Scheme](https://img.shields.io/badge/-Chez%20Scheme-1B4F72?style=flat-square) - json2dir in Chez Scheme. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-cil](https://github.com/json2dir-guru/json2dir-cil) ![CIL](https://img.shields.io/badge/-CIL-374151?style=flat-square) - json2dir in hand-written CIL (ilasm). Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-cilk](https://github.com/json2dir-guru/json2dir-cilk) ![Cilk](https://img.shields.io/badge/-Cilk-BE185D?style=flat-square) - json2dir in Cilk (OpenCilk). Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-clojure](https://github.com/json2dir-guru/json2dir-clojure) ![Clojure](https://img.shields.io/badge/-Clojure-C2410C?style=flat-square) - json2dir in Clojure. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-cmake](https://github.com/json2dir-guru/json2dir-cmake) ![CMake](https://img.shields.io/badge/-CMake-1D4ED8?style=flat-square) - json2dir in CMake script. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-cobol](https://github.com/json2dir-guru/json2dir-cobol) ![COBOL](https://img.shields.io/badge/-COBOL-1B4F72?style=flat-square) - json2dir in COBOL. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-commonlisp](https://github.com/json2dir-guru/json2dir-commonlisp) ![Common Lisp](https://img.shields.io/badge/-Common%20Lisp-374151?style=flat-square) - json2dir in Common Lisp. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-compcert](https://github.com/json2dir-guru/json2dir-compcert) ![C (CompCert)](https://img.shields.io/badge/-C%20%28CompCert%29-A16207?style=flat-square) - json2dir in C, compiled with CompCert. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-cow](https://github.com/json2dir-guru/json2dir-cow) ![COW](https://img.shields.io/badge/-COW-A16207?style=flat-square) - json2dir in COW, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-cpp](https://github.com/json2dir-guru/json2dir-cpp) ![C++](https://img.shields.io/badge/-C%2B%2B-5D4F85?style=flat-square) - json2dir in C++. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-crystal](https://github.com/json2dir-guru/json2dir-crystal) ![Crystal](https://img.shields.io/badge/-Crystal-B91C1C?style=flat-square) - json2dir in Crystal. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-d](https://github.com/json2dir-guru/json2dir-d) ![D](https://img.shields.io/badge/-D-1D4ED8?style=flat-square) - json2dir in D. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-dafny](https://github.com/json2dir-guru/json2dir-dafny) ![Dafny](https://img.shields.io/badge/-Dafny-BE185D?style=flat-square) - json2dir in Dafny. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-dart](https://github.com/json2dir-guru/json2dir-dart) ![Dart](https://img.shields.io/badge/-Dart-1D4ED8?style=flat-square) - json2dir in Dart. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-eiffel](https://github.com/json2dir-guru/json2dir-eiffel) ![Eiffel](https://img.shields.io/badge/-Eiffel-047857?style=flat-square) - json2dir in Eiffel. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-elisp](https://github.com/json2dir-guru/json2dir-elisp) ![Emacs Lisp](https://img.shields.io/badge/-Emacs%20Lisp-A16207?style=flat-square) - json2dir in Emacs Lisp. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-elixir](https://github.com/json2dir-guru/json2dir-elixir) ![Elixir](https://img.shields.io/badge/-Elixir-0E7490?style=flat-square) - json2dir in Elixir. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-emojicode](https://github.com/json2dir-guru/json2dir-emojicode) ![Emojicode](https://img.shields.io/badge/-Emojicode-374151?style=flat-square) - json2dir in Emojicode. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-erlang](https://github.com/json2dir-guru/json2dir-erlang) ![Erlang](https://img.shields.io/badge/-Erlang-1B4F72?style=flat-square) - json2dir in Erlang. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-false](https://github.com/json2dir-guru/json2dir-false) ![FALSE](https://img.shields.io/badge/-FALSE-0F766E?style=flat-square) - json2dir in FALSE, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-fennel](https://github.com/json2dir-guru/json2dir-fennel) ![Fennel](https://img.shields.io/badge/-Fennel-047857?style=flat-square) - json2dir in Fennel. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-fish](https://github.com/json2dir-guru/json2dir-fish) ![><> (Fish)](https://img.shields.io/badge/-%3E%3C%3E%20%28Fish%29-1D4ED8?style=flat-square) - json2dir in >&lt;> (Fish), with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-forth](https://github.com/json2dir-guru/json2dir-forth) ![Forth](https://img.shields.io/badge/-Forth-A16207?style=flat-square) - json2dir in Forth. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-fortran](https://github.com/json2dir-guru/json2dir-fortran) ![Fortran](https://img.shields.io/badge/-Fortran-BE185D?style=flat-square) - json2dir in Fortran. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-fractran](https://github.com/json2dir-guru/json2dir-fractran) ![Fractran](https://img.shields.io/badge/-Fractran-1B4F72?style=flat-square) - json2dir in Fractran, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-freepascal](https://github.com/json2dir-guru/json2dir-freepascal) ![Free Pascal](https://img.shields.io/badge/-Free%20Pascal-1B4F72?style=flat-square) - json2dir in Free Pascal. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-fsharp](https://github.com/json2dir-guru/json2dir-fsharp) ![F#](https://img.shields.io/badge/-F%23-047857?style=flat-square) - json2dir in F#. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-gleam](https://github.com/json2dir-guru/json2dir-gleam) ![Gleam](https://img.shields.io/badge/-Gleam-BE185D?style=flat-square) - json2dir in Gleam. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-gnuc](https://github.com/json2dir-guru/json2dir-gnuc) ![GNU C](https://img.shields.io/badge/-GNU%20C-374151?style=flat-square) - json2dir in GNU C. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-go](https://github.com/json2dir-guru/json2dir-go) ![Go](https://img.shields.io/badge/-Go-374151?style=flat-square) - json2dir in Go. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-groovy](https://github.com/json2dir-guru/json2dir-groovy) ![Groovy](https://img.shields.io/badge/-Groovy-0E7490?style=flat-square) - json2dir in Groovy. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-hare](https://github.com/json2dir-guru/json2dir-hare) ![Hare](https://img.shields.io/badge/-Hare-C2410C?style=flat-square) - json2dir in Hare. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-haskell](https://github.com/json2dir-guru/json2dir-haskell) ![Haskell](https://img.shields.io/badge/-Haskell-0E7490?style=flat-square) - json2dir in Haskell. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-hexagony](https://github.com/json2dir-guru/json2dir-hexagony) ![Hexagony](https://img.shields.io/badge/-Hexagony-5D4F85?style=flat-square) - json2dir in Hexagony, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-holyc](https://github.com/json2dir-guru/json2dir-holyc) ![HolyC](https://img.shields.io/badge/-HolyC-1D4ED8?style=flat-square) - json2dir in HolyC. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-idris2](https://github.com/json2dir-guru/json2dir-idris2) ![Idris 2](https://img.shields.io/badge/-Idris%202-1D4ED8?style=flat-square) - json2dir in Idris 2. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-intercal](https://github.com/json2dir-guru/json2dir-intercal) ![INTERCAL](https://img.shields.io/badge/-INTERCAL-C2410C?style=flat-square) - json2dir in INTERCAL, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-j](https://github.com/json2dir-guru/json2dir-j) ![J](https://img.shields.io/badge/-J-BE185D?style=flat-square) - json2dir in J. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-janet](https://github.com/json2dir-guru/json2dir-janet) ![Janet](https://img.shields.io/badge/-Janet-6D28D9?style=flat-square) - json2dir in Janet. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-java](https://github.com/json2dir-guru/json2dir-java) ![Java](https://img.shields.io/badge/-Java-B91C1C?style=flat-square) - json2dir in Java. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-jq](https://github.com/json2dir-guru/json2dir-jq) ![jq](https://img.shields.io/badge/-jq-A16207?style=flat-square) - json2dir in jq, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-js](https://github.com/json2dir-guru/json2dir-js) ![JavaScript](https://img.shields.io/badge/-JavaScript-1B4F72?style=flat-square) - json2dir in plain JavaScript. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-jscript](https://github.com/json2dir-guru/json2dir-jscript) ![JScript](https://img.shields.io/badge/-JScript-B91C1C?style=flat-square) - json2dir in JScript (Wine). Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-jsonnet](https://github.com/json2dir-guru/json2dir-jsonnet) ![Jsonnet](https://img.shields.io/badge/-Jsonnet-0F766E?style=flat-square) - json2dir in Jsonnet, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-jsonscript](https://github.com/json2dir-guru/json2dir-jsonscript) ![JSONScript](https://img.shields.io/badge/-JSONScript-1B4F72?style=flat-square) - json2dir in JSONScript. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-julia](https://github.com/json2dir-guru/json2dir-julia) ![Julia](https://img.shields.io/badge/-Julia-0F766E?style=flat-square) - json2dir in Julia. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-k](https://github.com/json2dir-guru/json2dir-k) ![K](https://img.shields.io/badge/-K-1D4ED8?style=flat-square) - json2dir in K, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-koka](https://github.com/json2dir-guru/json2dir-koka) ![Koka](https://img.shields.io/badge/-Koka-5D4F85?style=flat-square) - json2dir in Koka. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-kotlin](https://github.com/json2dir-guru/json2dir-kotlin) ![Kotlin](https://img.shields.io/badge/-Kotlin-0F766E?style=flat-square) - json2dir in Kotlin. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-kr](https://github.com/json2dir-guru/json2dir-kr) ![K&R C](https://img.shields.io/badge/-K%26R%20C-BE185D?style=flat-square) - json2dir in K&R C. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-ksh](https://github.com/json2dir-guru/json2dir-ksh) ![ksh93](https://img.shields.io/badge/-ksh93-374151?style=flat-square) - json2dir in ksh93. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-logo](https://github.com/json2dir-guru/json2dir-logo) ![Logo](https://img.shields.io/badge/-Logo-5D4F85?style=flat-square) - json2dir in Logo, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-lolcode](https://github.com/json2dir-guru/json2dir-lolcode) ![LOLCODE](https://img.shields.io/badge/-LOLCODE-BE185D?style=flat-square) - json2dir in LOLCODE, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-lua](https://github.com/json2dir-guru/json2dir-lua) ![Lua](https://img.shields.io/badge/-Lua-1B4F72?style=flat-square) - json2dir in Lua 5.4, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-luajit](https://github.com/json2dir-guru/json2dir-luajit) ![LuaJIT](https://img.shields.io/badge/-LuaJIT-374151?style=flat-square) - json2dir in LuaJIT. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-luatex](https://github.com/json2dir-guru/json2dir-luatex) ![LuaTeX](https://img.shields.io/badge/-LuaTeX-C2410C?style=flat-square) - json2dir in LuaTeX, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-malbolge](https://github.com/json2dir-guru/json2dir-malbolge) ![Malbolge Unshackled](https://img.shields.io/badge/-Malbolge%20Unshackled-374151?style=flat-square) - json2dir in Malbolge Unshackled, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-mercury](https://github.com/json2dir-guru/json2dir-mercury) ![Mercury](https://img.shields.io/badge/-Mercury-1B4F72?style=flat-square) - json2dir in Mercury. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-modula2](https://github.com/json2dir-guru/json2dir-modula2) ![Modula-2](https://img.shields.io/badge/-Modula--2-6D28D9?style=flat-square) - json2dir in Modula-2. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-mojo](https://github.com/json2dir-guru/json2dir-mojo) ![Mojo](https://img.shields.io/badge/-Mojo-374151?style=flat-square) - json2dir in Mojo. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-neovim](https://github.com/json2dir-guru/json2dir-neovim) ![Neovim Lua](https://img.shields.io/badge/-Neovim%20Lua-A16207?style=flat-square) - json2dir in Neovim Lua. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-nim](https://github.com/json2dir-guru/json2dir-nim) ![Nim](https://img.shields.io/badge/-Nim-6D28D9?style=flat-square) - json2dir in Nim. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-njs](https://github.com/json2dir-guru/json2dir-njs) ![nginx njs](https://img.shields.io/badge/-nginx%20njs-0F766E?style=flat-square) - json2dir in nginx njs + WebDAV. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-objc](https://github.com/json2dir-guru/json2dir-objc) ![Objective-C](https://img.shields.io/badge/-Objective--C-BE185D?style=flat-square) - json2dir in Objective-C. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-ocaml](https://github.com/json2dir-guru/json2dir-ocaml) ![OCaml](https://img.shields.io/badge/-OCaml-374151?style=flat-square) - json2dir in OCaml. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-octave](https://github.com/json2dir-guru/json2dir-octave) ![MATLAB/Octave](https://img.shields.io/badge/-MATLAB%2FOctave-0F766E?style=flat-square) - json2dir in MATLAB/Octave. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-octave-pure](https://github.com/json2dir-guru/json2dir-octave-pure) ![MATLAB/Octave](https://img.shields.io/badge/-MATLAB%2FOctave-0F766E?style=flat-square) - json2dir in MATLAB/Octave, without Java. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-odin](https://github.com/json2dir-guru/json2dir-odin) ![Odin](https://img.shields.io/badge/-Odin-5D4F85?style=flat-square) - json2dir in Odin. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-ook](https://github.com/json2dir-guru/json2dir-ook) ![Ook!](https://img.shields.io/badge/-Ook%21-047857?style=flat-square) - json2dir in Ook!, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-perl](https://github.com/json2dir-guru/json2dir-perl) ![Perl](https://img.shields.io/badge/-Perl-6D28D9?style=flat-square) - json2dir in Perl. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-php](https://github.com/json2dir-guru/json2dir-php) ![PHP](https://img.shields.io/badge/-PHP-0F766E?style=flat-square) - json2dir in PHP. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-piet](https://github.com/json2dir-guru/json2dir-piet) ![Piet](https://img.shields.io/badge/-Piet-A16207?style=flat-square) - json2dir in Piet, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-pikachu](https://github.com/json2dir-guru/json2dir-pikachu) ![Pikachu](https://img.shields.io/badge/-Pikachu-5D4F85?style=flat-square) - json2dir in Pikachu, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-pli](https://github.com/json2dir-guru/json2dir-pli) ![PL/I](https://img.shields.io/badge/-PL%2FI-1D4ED8?style=flat-square) - json2dir in PL/I. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-pony](https://github.com/json2dir-guru/json2dir-pony) ![Pony](https://img.shields.io/badge/-Pony-BE185D?style=flat-square) - json2dir in Pony. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-prolog](https://github.com/json2dir-guru/json2dir-prolog) ![Prolog](https://img.shields.io/badge/-Prolog-6D28D9?style=flat-square) - json2dir in Prolog. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-puppet](https://github.com/json2dir-guru/json2dir-puppet) ![Puppet](https://img.shields.io/badge/-Puppet-1B4F72?style=flat-square) - json2dir in Puppet. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-purescript](https://github.com/json2dir-guru/json2dir-purescript) ![PureScript](https://img.shields.io/badge/-PureScript-6D28D9?style=flat-square) - json2dir in PureScript. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-pwsh](https://github.com/json2dir-guru/json2dir-pwsh) ![PowerShell](https://img.shields.io/badge/-PowerShell-374151?style=flat-square) - json2dir in PowerShell. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-python](https://github.com/json2dir-guru/json2dir-python) ![Python](https://img.shields.io/badge/-Python-0F766E?style=flat-square) - json2dir in Python. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-r](https://github.com/json2dir-guru/json2dir-r) ![R](https://img.shields.io/badge/-R-6D28D9?style=flat-square) - json2dir in R. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-racket](https://github.com/json2dir-guru/json2dir-racket) ![Racket](https://img.shields.io/badge/-Racket-C2410C?style=flat-square) - json2dir in Racket. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-raku](https://github.com/json2dir-guru/json2dir-raku) ![Raku](https://img.shields.io/badge/-Raku-6D28D9?style=flat-square) - json2dir in Raku. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-rexx](https://github.com/json2dir-guru/json2dir-rexx) ![REXX](https://img.shields.io/badge/-REXX-1D4ED8?style=flat-square) - json2dir in REXX. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-roc](https://github.com/json2dir-guru/json2dir-roc) ![Roc](https://img.shields.io/badge/-Roc-374151?style=flat-square) - json2dir in Roc. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-rockstar](https://github.com/json2dir-guru/json2dir-rockstar) ![Rockstar](https://img.shields.io/badge/-Rockstar-0E7490?style=flat-square) - json2dir in Rockstar, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-rocq](https://github.com/json2dir-guru/json2dir-rocq) ![Rocq](https://img.shields.io/badge/-Rocq-1B4F72?style=flat-square) - json2dir in Rocq (extracted to OCaml). Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-ruby](https://github.com/json2dir-guru/json2dir-ruby) ![Ruby](https://img.shields.io/badge/-Ruby-1D4ED8?style=flat-square) - json2dir in Ruby. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-scala](https://github.com/json2dir-guru/json2dir-scala) ![Scala](https://img.shields.io/badge/-Scala-374151?style=flat-square) - json2dir in Scala. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-sed](https://github.com/json2dir-guru/json2dir-sed) ![sed](https://img.shields.io/badge/-sed-0E7490?style=flat-square) - json2dir in sed, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-shakespeare](https://github.com/json2dir-guru/json2dir-shakespeare) ![Shakespeare](https://img.shields.io/badge/-Shakespeare-374151?style=flat-square) - json2dir in the Shakespeare Programming Language, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-smalltalk](https://github.com/json2dir-guru/json2dir-smalltalk) ![Smalltalk](https://img.shields.io/badge/-Smalltalk-374151?style=flat-square) - json2dir in Smalltalk. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-sml](https://github.com/json2dir-guru/json2dir-sml) ![Standard ML](https://img.shields.io/badge/-Standard%20ML-B91C1C?style=flat-square) - json2dir in Standard ML. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-snobol4](https://github.com/json2dir-guru/json2dir-snobol4) ![SNOBOL4](https://img.shields.io/badge/-SNOBOL4-B91C1C?style=flat-square) - json2dir in SNOBOL4, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-sqlite](https://github.com/json2dir-guru/json2dir-sqlite) ![SQL](https://img.shields.io/badge/-SQL-1B4F72?style=flat-square) - json2dir in SQL (SQLite). Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-subleq](https://github.com/json2dir-guru/json2dir-subleq) ![Subleq](https://img.shields.io/badge/-Subleq-C2410C?style=flat-square) - json2dir in Subleq, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-swift](https://github.com/json2dir-guru/json2dir-swift) ![Swift](https://img.shields.io/badge/-Swift-6D28D9?style=flat-square) - json2dir in Swift. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-systemverilog](https://github.com/json2dir-guru/json2dir-systemverilog) ![SystemVerilog](https://img.shields.io/badge/-SystemVerilog-1B4F72?style=flat-square) - json2dir in SystemVerilog, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-taxi](https://github.com/json2dir-guru/json2dir-taxi) ![Taxi](https://img.shields.io/badge/-Taxi-0E7490?style=flat-square) - json2dir in Taxi, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-tcl](https://github.com/json2dir-guru/json2dir-tcl) ![Tcl](https://img.shields.io/badge/-Tcl-6D28D9?style=flat-square) - json2dir in Tcl. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-thue](https://github.com/json2dir-guru/json2dir-thue) ![Thue](https://img.shields.io/badge/-Thue-6D28D9?style=flat-square) - json2dir in Thue, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-ts](https://github.com/json2dir-guru/json2dir-ts) ![TypeScript](https://img.shields.io/badge/-TypeScript-0E7490?style=flat-square) - json2dir in TypeScript. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-unicon](https://github.com/json2dir-guru/json2dir-unicon) ![Unicon](https://img.shields.io/badge/-Unicon-0F766E?style=flat-square) - json2dir in Unicon (Icon). Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-unlambda](https://github.com/json2dir-guru/json2dir-unlambda) ![Unlambda](https://img.shields.io/badge/-Unlambda-A16207?style=flat-square) - json2dir in Unlambda, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-v](https://github.com/json2dir-guru/json2dir-v) ![V](https://img.shields.io/badge/-V-A16207?style=flat-square) - json2dir in V. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-vala](https://github.com/json2dir-guru/json2dir-vala) ![Vala](https://img.shields.io/badge/-Vala-1D4ED8?style=flat-square) - json2dir in Vala. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-vbnet](https://github.com/json2dir-guru/json2dir-vbnet) ![VB.NET](https://img.shields.io/badge/-VB.NET-5D4F85?style=flat-square) - json2dir in VB.NET. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-vbs](https://github.com/json2dir-guru/json2dir-vbs) ![VBScript](https://img.shields.io/badge/-VBScript-BE185D?style=flat-square) - json2dir in VBScript (Wine). Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-velato](https://github.com/json2dir-guru/json2dir-velato) ![Velato](https://img.shields.io/badge/-Velato-047857?style=flat-square) - json2dir in Velato, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-vhdl](https://github.com/json2dir-guru/json2dir-vhdl) ![VHDL](https://img.shields.io/badge/-VHDL-0F766E?style=flat-square) - json2dir in VHDL, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-vim](https://github.com/json2dir-guru/json2dir-vim) ![Vim script](https://img.shields.io/badge/-Vim%20script-5D4F85?style=flat-square) - json2dir in Vim script, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-wasm](https://github.com/json2dir-guru/json2dir-wasm) ![WebAssembly](https://img.shields.io/badge/-WebAssembly-A16207?style=flat-square) - json2dir in hand-written WebAssembly (WASI, Bun). Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-whitespace](https://github.com/json2dir-guru/json2dir-whitespace) ![Whitespace](https://img.shields.io/badge/-Whitespace-374151?style=flat-square) - json2dir in Whitespace, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-why3](https://github.com/json2dir-guru/json2dir-why3) ![WhyML](https://img.shields.io/badge/-WhyML-047857?style=flat-square) - json2dir in WhyML (Why3, extracted to OCaml). Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-xslt](https://github.com/json2dir-guru/json2dir-xslt) ![XSLT](https://img.shields.io/badge/-XSLT-6D28D9?style=flat-square) - json2dir in XSLT 3.0, with a shell launcher for the writes. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.
- [json2dir-guru/json2dir-zsh](https://github.com/json2dir-guru/json2dir-zsh) ![zsh](https://img.shields.io/badge/-zsh-374151?style=flat-square) - json2dir in zsh. Part of the [json2dir-guru](https://github.com/json2dir-guru) collection.

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
- [json2dir-guru/json2dir-tester](https://github.com/json2dir-guru/json2dir-tester) ![C#](https://img.shields.io/badge/-C%23-512BD4?style=flat-square&logo=dotnet&logoColor=white) - A C# runner that builds each implementation from source with its own toolchain, feeds every one the same cases and compares the resulting trees. Its cases include this list's conformance suite plus cases collected from other implementations' test suites.

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
| [json2dir-tester](https://github.com/json2dir-guru/json2dir-tester) | C# | runs every implementation | None specified |
| [dir2json](https://github.com/71g3pf4c3/dir2json) | Rust | dir → JSON | GPL-3.0 |
| [json2json](https://github.com/71g3pf4c3/json2json) | Rust | JSON → JSON | GPL-3.0 |
| [dir2dir](https://github.com/71g3pf4c3/dir2dir) | none yet | dir → dir | GPL-3.0 |
| [json2dir-ada](https://github.com/json2dir-guru/json2dir-ada) | Ada | JSON → dir | MIT |
| [json2dir-aheui](https://github.com/json2dir-guru/json2dir-aheui) | Aheui | JSON → dir (launcher) | MIT |
| [json2dir-algol60](https://github.com/json2dir-guru/json2dir-algol60) | ALGOL 60 | JSON → dir (launcher) | MIT |
| [json2dir-algol68](https://github.com/json2dir-guru/json2dir-algol68) | ALGOL 68 | JSON → dir (launcher) | MIT |
| [json2dir-ansible](https://github.com/json2dir-guru/json2dir-ansible) | Ansible | JSON → dir | MIT |
| [json2dir-aot](https://github.com/json2dir-guru/json2dir-aot) | C#, .NET 8 Native AOT | JSON → dir | MIT |
| [json2dir-apl](https://github.com/json2dir-guru/json2dir-apl) | APL | JSON → dir (launcher) | MIT |
| [json2dir-arnoldc](https://github.com/json2dir-guru/json2dir-arnoldc) | ArnoldC | JSON → dir (launcher) | MIT |
| [json2dir-asm](https://github.com/json2dir-guru/json2dir-asm) | x86-64 assembly (JWasm) | JSON → dir | MIT |
| [json2dir-awk](https://github.com/json2dir-guru/json2dir-awk) | AWK | JSON → dir (launcher) | MIT |
| [json2dir-bash](https://github.com/json2dir-guru/json2dir-bash) | Bash | JSON → dir (launcher) | MIT |
| [json2dir-basic](https://github.com/json2dir-guru/json2dir-basic) | BASIC (FreeBASIC) | JSON → dir | MIT |
| [json2dir-bat](https://github.com/json2dir-guru/json2dir-bat) | cmd.exe batch | JSON → dir | MIT |
| [json2dir-bcpl](https://github.com/json2dir-guru/json2dir-bcpl) | BCPL | JSON → dir (launcher) | MIT |
| [json2dir-befunge](https://github.com/json2dir-guru/json2dir-befunge) | Befunge-98 | JSON → dir (launcher) | MIT |
| [json2dir-bqn](https://github.com/json2dir-guru/json2dir-bqn) | BQN | JSON → dir | MIT |
| [json2dir-braincopter](https://github.com/json2dir-guru/json2dir-braincopter) | Braincopter | JSON → dir (launcher) | MIT |
| [json2dir-brainfuck](https://github.com/json2dir-guru/json2dir-brainfuck) | Brainfuck | JSON → dir (launcher) | MIT |
| [json2dir-brainloller](https://github.com/json2dir-guru/json2dir-brainloller) | Brainloller | JSON → dir (launcher) | MIT |
| [json2dir-c17](https://github.com/json2dir-guru/json2dir-c17) | C17 | JSON → dir | MIT |
| [json2dir-c23](https://github.com/json2dir-guru/json2dir-c23) | C23 | JSON → dir | MIT |
| [json2dir-c89](https://github.com/json2dir-guru/json2dir-c89) | ANSI C (C89) | JSON → dir | MIT |
| [json2dir-cforall](https://github.com/json2dir-guru/json2dir-cforall) | Cforall | JSON → dir | MIT |
| [json2dir-checkedc](https://github.com/json2dir-guru/json2dir-checkedc) | Checked C | JSON → dir | MIT |
| [json2dir-chef](https://github.com/json2dir-guru/json2dir-chef) | Chef | JSON → dir (launcher) | MIT |
| [json2dir-chez](https://github.com/json2dir-guru/json2dir-chez) | Chez Scheme | JSON → dir | MIT |
| [json2dir-cil](https://github.com/json2dir-guru/json2dir-cil) | hand-written CIL (ilasm) | JSON → dir | MIT |
| [json2dir-cilk](https://github.com/json2dir-guru/json2dir-cilk) | Cilk (OpenCilk) | JSON → dir | MIT |
| [json2dir-clojure](https://github.com/json2dir-guru/json2dir-clojure) | Clojure | JSON → dir | MIT |
| [json2dir-cmake](https://github.com/json2dir-guru/json2dir-cmake) | CMake script | JSON → dir | MIT |
| [json2dir-cobol](https://github.com/json2dir-guru/json2dir-cobol) | COBOL | JSON → dir | MIT |
| [json2dir-commonlisp](https://github.com/json2dir-guru/json2dir-commonlisp) | Common Lisp | JSON → dir | MIT |
| [json2dir-compcert](https://github.com/json2dir-guru/json2dir-compcert) | C, compiled with CompCert | JSON → dir | MIT |
| [json2dir-cow](https://github.com/json2dir-guru/json2dir-cow) | COW | JSON → dir (launcher) | MIT |
| [json2dir-cpp](https://github.com/json2dir-guru/json2dir-cpp) | C++ | JSON → dir | MIT |
| [json2dir-crystal](https://github.com/json2dir-guru/json2dir-crystal) | Crystal | JSON → dir | MIT |
| [json2dir-d](https://github.com/json2dir-guru/json2dir-d) | D | JSON → dir | MIT |
| [json2dir-dafny](https://github.com/json2dir-guru/json2dir-dafny) | Dafny | JSON → dir | MIT |
| [json2dir-dart](https://github.com/json2dir-guru/json2dir-dart) | Dart | JSON → dir | MIT |
| [json2dir-eiffel](https://github.com/json2dir-guru/json2dir-eiffel) | Eiffel | JSON → dir | MIT |
| [json2dir-elisp](https://github.com/json2dir-guru/json2dir-elisp) | Emacs Lisp | JSON → dir | MIT |
| [json2dir-elixir](https://github.com/json2dir-guru/json2dir-elixir) | Elixir | JSON → dir | MIT |
| [json2dir-emojicode](https://github.com/json2dir-guru/json2dir-emojicode) | Emojicode | JSON → dir | MIT |
| [json2dir-erlang](https://github.com/json2dir-guru/json2dir-erlang) | Erlang | JSON → dir | MIT |
| [json2dir-false](https://github.com/json2dir-guru/json2dir-false) | FALSE | JSON → dir (launcher) | MIT |
| [json2dir-fennel](https://github.com/json2dir-guru/json2dir-fennel) | Fennel | JSON → dir | MIT |
| [json2dir-fish](https://github.com/json2dir-guru/json2dir-fish) | >&lt;> (Fish) | JSON → dir (launcher) | MIT |
| [json2dir-forth](https://github.com/json2dir-guru/json2dir-forth) | Forth | JSON → dir | MIT |
| [json2dir-fortran](https://github.com/json2dir-guru/json2dir-fortran) | Fortran | JSON → dir | MIT |
| [json2dir-fractran](https://github.com/json2dir-guru/json2dir-fractran) | Fractran | JSON → dir (launcher) | MIT |
| [json2dir-freepascal](https://github.com/json2dir-guru/json2dir-freepascal) | Free Pascal | JSON → dir | MIT |
| [json2dir-fsharp](https://github.com/json2dir-guru/json2dir-fsharp) | F# | JSON → dir | MIT |
| [json2dir-gleam](https://github.com/json2dir-guru/json2dir-gleam) | Gleam | JSON → dir | MIT |
| [json2dir-gnuc](https://github.com/json2dir-guru/json2dir-gnuc) | GNU C | JSON → dir | MIT |
| [json2dir-go](https://github.com/json2dir-guru/json2dir-go) | Go | JSON → dir | MIT |
| [json2dir-groovy](https://github.com/json2dir-guru/json2dir-groovy) | Groovy | JSON → dir | MIT |
| [json2dir-hare](https://github.com/json2dir-guru/json2dir-hare) | Hare | JSON → dir | MIT |
| [json2dir-haskell](https://github.com/json2dir-guru/json2dir-haskell) | Haskell | JSON → dir | MIT |
| [json2dir-hexagony](https://github.com/json2dir-guru/json2dir-hexagony) | Hexagony | JSON → dir (launcher) | MIT |
| [json2dir-holyc](https://github.com/json2dir-guru/json2dir-holyc) | HolyC | JSON → dir | MIT |
| [json2dir-idris2](https://github.com/json2dir-guru/json2dir-idris2) | Idris 2 | JSON → dir | MIT |
| [json2dir-intercal](https://github.com/json2dir-guru/json2dir-intercal) | INTERCAL | JSON → dir (launcher) | MIT |
| [json2dir-j](https://github.com/json2dir-guru/json2dir-j) | J | JSON → dir | MIT |
| [json2dir-janet](https://github.com/json2dir-guru/json2dir-janet) | Janet | JSON → dir | MIT |
| [json2dir-java](https://github.com/json2dir-guru/json2dir-java) | Java | JSON → dir | MIT |
| [json2dir-jq](https://github.com/json2dir-guru/json2dir-jq) | jq | JSON → dir (launcher) | MIT |
| [json2dir-js](https://github.com/json2dir-guru/json2dir-js) | plain JavaScript | JSON → dir | MIT |
| [json2dir-jscript](https://github.com/json2dir-guru/json2dir-jscript) | JScript (Wine) | JSON → dir | MIT |
| [json2dir-jsonnet](https://github.com/json2dir-guru/json2dir-jsonnet) | Jsonnet | JSON → dir (launcher) | MIT |
| [json2dir-jsonscript](https://github.com/json2dir-guru/json2dir-jsonscript) | JSONScript | JSON → dir | MIT |
| [json2dir-julia](https://github.com/json2dir-guru/json2dir-julia) | Julia | JSON → dir | MIT |
| [json2dir-k](https://github.com/json2dir-guru/json2dir-k) | K | JSON → dir (launcher) | MIT |
| [json2dir-koka](https://github.com/json2dir-guru/json2dir-koka) | Koka | JSON → dir | MIT |
| [json2dir-kotlin](https://github.com/json2dir-guru/json2dir-kotlin) | Kotlin | JSON → dir | MIT |
| [json2dir-kr](https://github.com/json2dir-guru/json2dir-kr) | K&R C | JSON → dir | MIT |
| [json2dir-ksh](https://github.com/json2dir-guru/json2dir-ksh) | ksh93 | JSON → dir | MIT |
| [json2dir-logo](https://github.com/json2dir-guru/json2dir-logo) | Logo | JSON → dir (launcher) | MIT |
| [json2dir-lolcode](https://github.com/json2dir-guru/json2dir-lolcode) | LOLCODE | JSON → dir (launcher) | MIT |
| [json2dir-lua](https://github.com/json2dir-guru/json2dir-lua) | Lua 5.4 | JSON → dir (launcher) | MIT |
| [json2dir-luajit](https://github.com/json2dir-guru/json2dir-luajit) | LuaJIT | JSON → dir | MIT |
| [json2dir-luatex](https://github.com/json2dir-guru/json2dir-luatex) | LuaTeX | JSON → dir (launcher) | MIT |
| [json2dir-malbolge](https://github.com/json2dir-guru/json2dir-malbolge) | Malbolge Unshackled | JSON → dir (launcher) | MIT |
| [json2dir-mercury](https://github.com/json2dir-guru/json2dir-mercury) | Mercury | JSON → dir | MIT |
| [json2dir-modula2](https://github.com/json2dir-guru/json2dir-modula2) | Modula-2 | JSON → dir | MIT |
| [json2dir-mojo](https://github.com/json2dir-guru/json2dir-mojo) | Mojo | JSON → dir | MIT |
| [json2dir-neovim](https://github.com/json2dir-guru/json2dir-neovim) | Neovim Lua | JSON → dir | MIT |
| [json2dir-nim](https://github.com/json2dir-guru/json2dir-nim) | Nim | JSON → dir | MIT |
| [json2dir-njs](https://github.com/json2dir-guru/json2dir-njs) | nginx njs + WebDAV | JSON → dir | MIT |
| [json2dir-objc](https://github.com/json2dir-guru/json2dir-objc) | Objective-C | JSON → dir | MIT |
| [json2dir-ocaml](https://github.com/json2dir-guru/json2dir-ocaml) | OCaml | JSON → dir | MIT |
| [json2dir-octave](https://github.com/json2dir-guru/json2dir-octave) | MATLAB/Octave | JSON → dir | MIT |
| [json2dir-octave-pure](https://github.com/json2dir-guru/json2dir-octave-pure) | MATLAB/Octave, without Java | JSON → dir | MIT |
| [json2dir-odin](https://github.com/json2dir-guru/json2dir-odin) | Odin | JSON → dir | MIT |
| [json2dir-ook](https://github.com/json2dir-guru/json2dir-ook) | Ook! | JSON → dir (launcher) | MIT |
| [json2dir-perl](https://github.com/json2dir-guru/json2dir-perl) | Perl | JSON → dir | MIT |
| [json2dir-php](https://github.com/json2dir-guru/json2dir-php) | PHP | JSON → dir | MIT |
| [json2dir-piet](https://github.com/json2dir-guru/json2dir-piet) | Piet | JSON → dir (launcher) | MIT |
| [json2dir-pikachu](https://github.com/json2dir-guru/json2dir-pikachu) | Pikachu | JSON → dir (launcher) | MIT |
| [json2dir-pli](https://github.com/json2dir-guru/json2dir-pli) | PL/I | JSON → dir | MIT |
| [json2dir-pony](https://github.com/json2dir-guru/json2dir-pony) | Pony | JSON → dir | MIT |
| [json2dir-prolog](https://github.com/json2dir-guru/json2dir-prolog) | Prolog | JSON → dir | MIT |
| [json2dir-puppet](https://github.com/json2dir-guru/json2dir-puppet) | Puppet | JSON → dir | MIT |
| [json2dir-purescript](https://github.com/json2dir-guru/json2dir-purescript) | PureScript | JSON → dir | MIT |
| [json2dir-pwsh](https://github.com/json2dir-guru/json2dir-pwsh) | PowerShell | JSON → dir | MIT |
| [json2dir-python](https://github.com/json2dir-guru/json2dir-python) | Python | JSON → dir | MIT |
| [json2dir-r](https://github.com/json2dir-guru/json2dir-r) | R | JSON → dir | MIT |
| [json2dir-racket](https://github.com/json2dir-guru/json2dir-racket) | Racket | JSON → dir | MIT |
| [json2dir-raku](https://github.com/json2dir-guru/json2dir-raku) | Raku | JSON → dir | MIT |
| [json2dir-rexx](https://github.com/json2dir-guru/json2dir-rexx) | REXX | JSON → dir | MIT |
| [json2dir-roc](https://github.com/json2dir-guru/json2dir-roc) | Roc | JSON → dir | MIT |
| [json2dir-rockstar](https://github.com/json2dir-guru/json2dir-rockstar) | Rockstar | JSON → dir (launcher) | MIT |
| [json2dir-rocq](https://github.com/json2dir-guru/json2dir-rocq) | Rocq (extracted to OCaml) | JSON → dir | MIT |
| [json2dir-ruby](https://github.com/json2dir-guru/json2dir-ruby) | Ruby | JSON → dir | MIT |
| [json2dir-scala](https://github.com/json2dir-guru/json2dir-scala) | Scala | JSON → dir | MIT |
| [json2dir-sed](https://github.com/json2dir-guru/json2dir-sed) | sed | JSON → dir (launcher) | MIT |
| [json2dir-shakespeare](https://github.com/json2dir-guru/json2dir-shakespeare) | the Shakespeare Programming Language | JSON → dir (launcher) | MIT |
| [json2dir-smalltalk](https://github.com/json2dir-guru/json2dir-smalltalk) | Smalltalk | JSON → dir | MIT |
| [json2dir-sml](https://github.com/json2dir-guru/json2dir-sml) | Standard ML | JSON → dir | MIT |
| [json2dir-snobol4](https://github.com/json2dir-guru/json2dir-snobol4) | SNOBOL4 | JSON → dir (launcher) | MIT |
| [json2dir-sqlite](https://github.com/json2dir-guru/json2dir-sqlite) | SQL (SQLite) | JSON → dir | MIT |
| [json2dir-subleq](https://github.com/json2dir-guru/json2dir-subleq) | Subleq | JSON → dir (launcher) | MIT |
| [json2dir-swift](https://github.com/json2dir-guru/json2dir-swift) | Swift | JSON → dir | MIT |
| [json2dir-systemverilog](https://github.com/json2dir-guru/json2dir-systemverilog) | SystemVerilog | JSON → dir (launcher) | MIT |
| [json2dir-taxi](https://github.com/json2dir-guru/json2dir-taxi) | Taxi | JSON → dir (launcher) | MIT |
| [json2dir-tcl](https://github.com/json2dir-guru/json2dir-tcl) | Tcl | JSON → dir | MIT |
| [json2dir-thue](https://github.com/json2dir-guru/json2dir-thue) | Thue | JSON → dir (launcher) | MIT |
| [json2dir-ts](https://github.com/json2dir-guru/json2dir-ts) | TypeScript | JSON → dir | MIT |
| [json2dir-unicon](https://github.com/json2dir-guru/json2dir-unicon) | Unicon (Icon) | JSON → dir | MIT |
| [json2dir-unlambda](https://github.com/json2dir-guru/json2dir-unlambda) | Unlambda | JSON → dir (launcher) | MIT |
| [json2dir-v](https://github.com/json2dir-guru/json2dir-v) | V | JSON → dir | MIT |
| [json2dir-vala](https://github.com/json2dir-guru/json2dir-vala) | Vala | JSON → dir | MIT |
| [json2dir-vbnet](https://github.com/json2dir-guru/json2dir-vbnet) | VB.NET | JSON → dir | MIT |
| [json2dir-vbs](https://github.com/json2dir-guru/json2dir-vbs) | VBScript (Wine) | JSON → dir | MIT |
| [json2dir-velato](https://github.com/json2dir-guru/json2dir-velato) | Velato | JSON → dir (launcher) | MIT |
| [json2dir-vhdl](https://github.com/json2dir-guru/json2dir-vhdl) | VHDL | JSON → dir (launcher) | MIT |
| [json2dir-vim](https://github.com/json2dir-guru/json2dir-vim) | Vim script | JSON → dir (launcher) | MIT |
| [json2dir-wasm](https://github.com/json2dir-guru/json2dir-wasm) | hand-written WebAssembly (WASI, Bun) | JSON → dir | MIT |
| [json2dir-whitespace](https://github.com/json2dir-guru/json2dir-whitespace) | Whitespace | JSON → dir (launcher) | MIT |
| [json2dir-why3](https://github.com/json2dir-guru/json2dir-why3) | WhyML (Why3, extracted to OCaml) | JSON → dir | MIT |
| [json2dir-xslt](https://github.com/json2dir-guru/json2dir-xslt) | XSLT 3.0 | JSON → dir (launcher) | MIT |
| [json2dir-zsh](https://github.com/json2dir-guru/json2dir-zsh) | zsh | JSON → dir | MIT |

## Wanted

Implementations that have been requested but do not exist yet. Be the first:

- [x] Haskell: [json2dir-hs](https://github.com/KovalevDima/json2dir-hs)
- [x] Nix (pure evaluation, `builtins` only): [json2dir-nix](https://github.com/TheMaxMur/json2dir-nix), with a shell launcher for the writes
- [x] Assembly: [json2dir-asm](https://github.com/json2dir-guru/json2dir-asm)
- [x] JS: [json2dir-js](https://github.com/json2dir-guru/json2dir-js)
- [x] TS: [json2dir-ts](https://github.com/json2dir-guru/json2dir-ts)
- [x] Wasm (Bun): [json2dir-wasm](https://github.com/json2dir-guru/json2dir-wasm)
- [x] jsonscript (Node): [json2dir-jsonscript](https://github.com/json2dir-guru/json2dir-jsonscript)
- [x] Jsonnet (launcher approach): [json2dir-jsonnet](https://github.com/json2dir-guru/json2dir-jsonnet)
- [x] JScript (Wine): [json2dir-jscript](https://github.com/json2dir-guru/json2dir-jscript)
- [x] CMake: [json2dir-cmake](https://github.com/json2dir-guru/json2dir-cmake)
- [x] Lisp (Emacs Lisp): [json2dir-elisp](https://github.com/json2dir-guru/json2dir-elisp)
- [x] LuaJIT: [json2dir-luajit](https://github.com/json2dir-guru/json2dir-luajit)
- [x] Zsh: [json2dir-zsh](https://github.com/json2dir-guru/json2dir-zsh)
- [x] Bat: [json2dir-bat](https://github.com/json2dir-guru/json2dir-bat)
- [x] Pwsh: [json2dir-pwsh](https://github.com/json2dir-guru/json2dir-pwsh)
- [x] Puppet: [json2dir-puppet](https://github.com/json2dir-guru/json2dir-puppet)
- [x] Ansible: [json2dir-ansible](https://github.com/json2dir-guru/json2dir-ansible)
- [x] LuaTeX (launcher approach): [json2dir-luatex](https://github.com/json2dir-guru/json2dir-luatex)
- [x] Vim (launcher approach): [json2dir-vim](https://github.com/json2dir-guru/json2dir-vim)
- [x] Java: [json2dir-java](https://github.com/json2dir-guru/json2dir-java)
- [x] Python: [json2dir-python](https://github.com/json2dir-guru/json2dir-python)
- [x] Ruby: [json2dir-ruby](https://github.com/json2dir-guru/json2dir-ruby)
- [x] PHP: [json2dir-php](https://github.com/json2dir-guru/json2dir-php)
- [x] nginx njs + WebDAV (self recursion with requests): [json2dir-njs](https://github.com/json2dir-guru/json2dir-njs)
- [x] A test harness that checks every implementation against the same fixtures: the [conformance suite](conformance/README.md)

## Contributing

Wrote your own `json2dir`? Run the [conformance suite](conformance/README.md) against it, then open a pull request. Read the [contribution guidelines](CONTRIBUTING.md) first.

---

<div align="center">

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related rights to this work.

</div>
