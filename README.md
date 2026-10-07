<div align="center">

# Awesome json2dir [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**A curated list of implementations, ports, rewrites and heresies of [`json2dir`](https://github.com/alurm/json2dir).**

*One JSON object in. One directory tree out. Many languages, many opinions.*

**[Website](https://kitsunoff.github.io/awesome-json2dir/) · [RFC J2D-1](spec/rfc-json2dir.md) · [Conformance suite](conformance/README.md) · [Manifesto](MANIFESTO.md)**

[![Projects](https://img.shields.io/badge/projects-167-blueviolet?style=flat-square)](#contents)
[![Languages](https://img.shields.io/badge/languages-Rust%20%C2%B7%20Zig%20%C2%B7%20C%23%20%C2%B7%20Scheme%20%C2%B7%20Go%20%C2%B7%20MSBuild%20%C2%B7%20Nix%20%C2%B7%20Lean%20%C2%B7%20LLVM%20IR%20%C2%B7%20F%2A%20%C2%B7%20Agda%20%C2%B7%20ATS%20%C2%B7%20Brainfuck%20%C2%B7%20bimbo--lang%20%C2%B7%20Haskell%20%C2%B7%20Typst%20%C2%B7%20Python%20%C2%B7%20Shell%20%C2%B7%20%2B%20141%20via%20json2dir--guru-orange?style=flat-square)](#ports-and-rewrites)
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
- [json2dir-guru: 141 languages](#json2dir-guru-141-languages)
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

## json2dir-guru: 141 languages

[json2dir-guru](https://github.com/json2dir-guru) ports json2dir to 141 languages and stacks, one repository each, all MIT. Languages that cannot write files use a small shell launcher in the style of json2dir-nix; those are marked *launcher*. Every port is run against the same cases by [json2dir-tester](https://github.com/json2dir-guru/json2dir-tester), including this list's [conformance suite](conformance/README.md).

- [json2dir-ada](https://github.com/json2dir-guru/json2dir-ada) - Ada.
- [json2dir-aheui](https://github.com/json2dir-guru/json2dir-aheui) - Aheui, *launcher*.
- [json2dir-algol60](https://github.com/json2dir-guru/json2dir-algol60) - ALGOL 60, *launcher*.
- [json2dir-algol68](https://github.com/json2dir-guru/json2dir-algol68) - ALGOL 68, *launcher*.
- [json2dir-ansible](https://github.com/json2dir-guru/json2dir-ansible) - Ansible.
- [json2dir-aot](https://github.com/json2dir-guru/json2dir-aot) - C#, .NET 8 Native AOT.
- [json2dir-apl](https://github.com/json2dir-guru/json2dir-apl) - APL, *launcher*.
- [json2dir-arnoldc](https://github.com/json2dir-guru/json2dir-arnoldc) - ArnoldC, *launcher*.
- [json2dir-asm](https://github.com/json2dir-guru/json2dir-asm) - x86-64 assembly (JWasm).
- [json2dir-awk](https://github.com/json2dir-guru/json2dir-awk) - AWK, *launcher*.
- [json2dir-bash](https://github.com/json2dir-guru/json2dir-bash) - Bash, *launcher*.
- [json2dir-basic](https://github.com/json2dir-guru/json2dir-basic) - BASIC (FreeBASIC).
- [json2dir-bat](https://github.com/json2dir-guru/json2dir-bat) - cmd.exe batch.
- [json2dir-bcpl](https://github.com/json2dir-guru/json2dir-bcpl) - BCPL, *launcher*.
- [json2dir-befunge](https://github.com/json2dir-guru/json2dir-befunge) - Befunge-98, *launcher*.
- [json2dir-bqn](https://github.com/json2dir-guru/json2dir-bqn) - BQN.
- [json2dir-braincopter](https://github.com/json2dir-guru/json2dir-braincopter) - Braincopter, *launcher*.
- [json2dir-brainfuck](https://github.com/json2dir-guru/json2dir-brainfuck) - Brainfuck, *launcher*.
- [json2dir-brainloller](https://github.com/json2dir-guru/json2dir-brainloller) - Brainloller, *launcher*.
- [json2dir-c17](https://github.com/json2dir-guru/json2dir-c17) - C17.
- [json2dir-c23](https://github.com/json2dir-guru/json2dir-c23) - C23.
- [json2dir-c89](https://github.com/json2dir-guru/json2dir-c89) - ANSI C (C89).
- [json2dir-cforall](https://github.com/json2dir-guru/json2dir-cforall) - Cforall.
- [json2dir-checkedc](https://github.com/json2dir-guru/json2dir-checkedc) - Checked C.
- [json2dir-chef](https://github.com/json2dir-guru/json2dir-chef) - Chef, *launcher*.
- [json2dir-chez](https://github.com/json2dir-guru/json2dir-chez) - Chez Scheme.
- [json2dir-cil](https://github.com/json2dir-guru/json2dir-cil) - hand-written CIL (ilasm).
- [json2dir-cilk](https://github.com/json2dir-guru/json2dir-cilk) - Cilk (OpenCilk).
- [json2dir-clojure](https://github.com/json2dir-guru/json2dir-clojure) - Clojure.
- [json2dir-cmake](https://github.com/json2dir-guru/json2dir-cmake) - CMake script.
- [json2dir-cobol](https://github.com/json2dir-guru/json2dir-cobol) - COBOL.
- [json2dir-commonlisp](https://github.com/json2dir-guru/json2dir-commonlisp) - Common Lisp.
- [json2dir-compcert](https://github.com/json2dir-guru/json2dir-compcert) - C, compiled with CompCert.
- [json2dir-cow](https://github.com/json2dir-guru/json2dir-cow) - COW, *launcher*.
- [json2dir-cpp](https://github.com/json2dir-guru/json2dir-cpp) - C++.
- [json2dir-crystal](https://github.com/json2dir-guru/json2dir-crystal) - Crystal.
- [json2dir-d](https://github.com/json2dir-guru/json2dir-d) - D.
- [json2dir-dafny](https://github.com/json2dir-guru/json2dir-dafny) - Dafny.
- [json2dir-dart](https://github.com/json2dir-guru/json2dir-dart) - Dart.
- [json2dir-eiffel](https://github.com/json2dir-guru/json2dir-eiffel) - Eiffel.
- [json2dir-elisp](https://github.com/json2dir-guru/json2dir-elisp) - Emacs Lisp.
- [json2dir-elixir](https://github.com/json2dir-guru/json2dir-elixir) - Elixir.
- [json2dir-emojicode](https://github.com/json2dir-guru/json2dir-emojicode) - Emojicode.
- [json2dir-erlang](https://github.com/json2dir-guru/json2dir-erlang) - Erlang.
- [json2dir-false](https://github.com/json2dir-guru/json2dir-false) - FALSE, *launcher*.
- [json2dir-fennel](https://github.com/json2dir-guru/json2dir-fennel) - Fennel.
- [json2dir-fish](https://github.com/json2dir-guru/json2dir-fish) - >&lt;> (Fish), *launcher*.
- [json2dir-forth](https://github.com/json2dir-guru/json2dir-forth) - Forth.
- [json2dir-fortran](https://github.com/json2dir-guru/json2dir-fortran) - Fortran.
- [json2dir-fractran](https://github.com/json2dir-guru/json2dir-fractran) - Fractran, *launcher*.
- [json2dir-freepascal](https://github.com/json2dir-guru/json2dir-freepascal) - Free Pascal.
- [json2dir-fsharp](https://github.com/json2dir-guru/json2dir-fsharp) - F#.
- [json2dir-gleam](https://github.com/json2dir-guru/json2dir-gleam) - Gleam.
- [json2dir-gnuc](https://github.com/json2dir-guru/json2dir-gnuc) - GNU C.
- [json2dir-go](https://github.com/json2dir-guru/json2dir-go) - Go.
- [json2dir-groovy](https://github.com/json2dir-guru/json2dir-groovy) - Groovy.
- [json2dir-hare](https://github.com/json2dir-guru/json2dir-hare) - Hare.
- [json2dir-haskell](https://github.com/json2dir-guru/json2dir-haskell) - Haskell.
- [json2dir-hexagony](https://github.com/json2dir-guru/json2dir-hexagony) - Hexagony, *launcher*.
- [json2dir-holyc](https://github.com/json2dir-guru/json2dir-holyc) - HolyC.
- [json2dir-idris2](https://github.com/json2dir-guru/json2dir-idris2) - Idris 2.
- [json2dir-intercal](https://github.com/json2dir-guru/json2dir-intercal) - INTERCAL, *launcher*.
- [json2dir-j](https://github.com/json2dir-guru/json2dir-j) - J.
- [json2dir-janet](https://github.com/json2dir-guru/json2dir-janet) - Janet.
- [json2dir-java](https://github.com/json2dir-guru/json2dir-java) - Java.
- [json2dir-jq](https://github.com/json2dir-guru/json2dir-jq) - jq, *launcher*.
- [json2dir-js](https://github.com/json2dir-guru/json2dir-js) - plain JavaScript.
- [json2dir-jscript](https://github.com/json2dir-guru/json2dir-jscript) - JScript (Wine).
- [json2dir-jsonnet](https://github.com/json2dir-guru/json2dir-jsonnet) - Jsonnet, *launcher*.
- [json2dir-jsonscript](https://github.com/json2dir-guru/json2dir-jsonscript) - JSONScript.
- [json2dir-julia](https://github.com/json2dir-guru/json2dir-julia) - Julia.
- [json2dir-k](https://github.com/json2dir-guru/json2dir-k) - K, *launcher*.
- [json2dir-koka](https://github.com/json2dir-guru/json2dir-koka) - Koka.
- [json2dir-kotlin](https://github.com/json2dir-guru/json2dir-kotlin) - Kotlin.
- [json2dir-kr](https://github.com/json2dir-guru/json2dir-kr) - K&R C.
- [json2dir-ksh](https://github.com/json2dir-guru/json2dir-ksh) - ksh93.
- [json2dir-logo](https://github.com/json2dir-guru/json2dir-logo) - Logo, *launcher*.
- [json2dir-lolcode](https://github.com/json2dir-guru/json2dir-lolcode) - LOLCODE, *launcher*.
- [json2dir-lua](https://github.com/json2dir-guru/json2dir-lua) - Lua 5.4, *launcher*.
- [json2dir-luajit](https://github.com/json2dir-guru/json2dir-luajit) - LuaJIT.
- [json2dir-luatex](https://github.com/json2dir-guru/json2dir-luatex) - LuaTeX, *launcher*.
- [json2dir-malbolge](https://github.com/json2dir-guru/json2dir-malbolge) - Malbolge Unshackled, *launcher*.
- [json2dir-mercury](https://github.com/json2dir-guru/json2dir-mercury) - Mercury.
- [json2dir-modula2](https://github.com/json2dir-guru/json2dir-modula2) - Modula-2.
- [json2dir-mojo](https://github.com/json2dir-guru/json2dir-mojo) - Mojo.
- [json2dir-neovim](https://github.com/json2dir-guru/json2dir-neovim) - Neovim Lua.
- [json2dir-nim](https://github.com/json2dir-guru/json2dir-nim) - Nim.
- [json2dir-njs](https://github.com/json2dir-guru/json2dir-njs) - nginx njs + WebDAV.
- [json2dir-objc](https://github.com/json2dir-guru/json2dir-objc) - Objective-C.
- [json2dir-ocaml](https://github.com/json2dir-guru/json2dir-ocaml) - OCaml.
- [json2dir-octave](https://github.com/json2dir-guru/json2dir-octave) - MATLAB/Octave.
- [json2dir-octave-pure](https://github.com/json2dir-guru/json2dir-octave-pure) - MATLAB/Octave, without Java.
- [json2dir-odin](https://github.com/json2dir-guru/json2dir-odin) - Odin.
- [json2dir-ook](https://github.com/json2dir-guru/json2dir-ook) - Ook!, *launcher*.
- [json2dir-perl](https://github.com/json2dir-guru/json2dir-perl) - Perl.
- [json2dir-php](https://github.com/json2dir-guru/json2dir-php) - PHP.
- [json2dir-piet](https://github.com/json2dir-guru/json2dir-piet) - Piet, *launcher*.
- [json2dir-pikachu](https://github.com/json2dir-guru/json2dir-pikachu) - Pikachu, *launcher*.
- [json2dir-pli](https://github.com/json2dir-guru/json2dir-pli) - PL/I.
- [json2dir-pony](https://github.com/json2dir-guru/json2dir-pony) - Pony.
- [json2dir-prolog](https://github.com/json2dir-guru/json2dir-prolog) - Prolog.
- [json2dir-puppet](https://github.com/json2dir-guru/json2dir-puppet) - Puppet.
- [json2dir-purescript](https://github.com/json2dir-guru/json2dir-purescript) - PureScript.
- [json2dir-pwsh](https://github.com/json2dir-guru/json2dir-pwsh) - PowerShell.
- [json2dir-python](https://github.com/json2dir-guru/json2dir-python) - Python.
- [json2dir-r](https://github.com/json2dir-guru/json2dir-r) - R.
- [json2dir-racket](https://github.com/json2dir-guru/json2dir-racket) - Racket.
- [json2dir-raku](https://github.com/json2dir-guru/json2dir-raku) - Raku.
- [json2dir-rexx](https://github.com/json2dir-guru/json2dir-rexx) - REXX.
- [json2dir-roc](https://github.com/json2dir-guru/json2dir-roc) - Roc.
- [json2dir-rockstar](https://github.com/json2dir-guru/json2dir-rockstar) - Rockstar, *launcher*.
- [json2dir-rocq](https://github.com/json2dir-guru/json2dir-rocq) - Rocq (extracted to OCaml).
- [json2dir-ruby](https://github.com/json2dir-guru/json2dir-ruby) - Ruby.
- [json2dir-scala](https://github.com/json2dir-guru/json2dir-scala) - Scala.
- [json2dir-sed](https://github.com/json2dir-guru/json2dir-sed) - sed, *launcher*.
- [json2dir-shakespeare](https://github.com/json2dir-guru/json2dir-shakespeare) - the Shakespeare Programming Language, *launcher*.
- [json2dir-smalltalk](https://github.com/json2dir-guru/json2dir-smalltalk) - Smalltalk.
- [json2dir-sml](https://github.com/json2dir-guru/json2dir-sml) - Standard ML.
- [json2dir-snobol4](https://github.com/json2dir-guru/json2dir-snobol4) - SNOBOL4, *launcher*.
- [json2dir-sqlite](https://github.com/json2dir-guru/json2dir-sqlite) - SQL (SQLite).
- [json2dir-subleq](https://github.com/json2dir-guru/json2dir-subleq) - Subleq, *launcher*.
- [json2dir-swift](https://github.com/json2dir-guru/json2dir-swift) - Swift.
- [json2dir-systemverilog](https://github.com/json2dir-guru/json2dir-systemverilog) - SystemVerilog, *launcher*.
- [json2dir-taxi](https://github.com/json2dir-guru/json2dir-taxi) - Taxi, *launcher*.
- [json2dir-tcl](https://github.com/json2dir-guru/json2dir-tcl) - Tcl.
- [json2dir-thue](https://github.com/json2dir-guru/json2dir-thue) - Thue, *launcher*.
- [json2dir-ts](https://github.com/json2dir-guru/json2dir-ts) - TypeScript.
- [json2dir-unicon](https://github.com/json2dir-guru/json2dir-unicon) - Unicon (Icon).
- [json2dir-unlambda](https://github.com/json2dir-guru/json2dir-unlambda) - Unlambda, *launcher*.
- [json2dir-v](https://github.com/json2dir-guru/json2dir-v) - V.
- [json2dir-vala](https://github.com/json2dir-guru/json2dir-vala) - Vala.
- [json2dir-vbnet](https://github.com/json2dir-guru/json2dir-vbnet) - VB.NET.
- [json2dir-vbs](https://github.com/json2dir-guru/json2dir-vbs) - VBScript (Wine).
- [json2dir-velato](https://github.com/json2dir-guru/json2dir-velato) - Velato, *launcher*.
- [json2dir-vhdl](https://github.com/json2dir-guru/json2dir-vhdl) - VHDL, *launcher*.
- [json2dir-vim](https://github.com/json2dir-guru/json2dir-vim) - Vim script, *launcher*.
- [json2dir-wasm](https://github.com/json2dir-guru/json2dir-wasm) - hand-written WebAssembly (WASI, Bun).
- [json2dir-whitespace](https://github.com/json2dir-guru/json2dir-whitespace) - Whitespace, *launcher*.
- [json2dir-why3](https://github.com/json2dir-guru/json2dir-why3) - WhyML (Why3, extracted to OCaml).
- [json2dir-xslt](https://github.com/json2dir-guru/json2dir-xslt) - XSLT 3.0, *launcher*.
- [json2dir-zsh](https://github.com/json2dir-guru/json2dir-zsh) - zsh.

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
