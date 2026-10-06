# The json2dir Manifesto

*A tree is a value. Write it down.*

---

## I. Every directory is already a JSON object

A directory maps names to things. So does a JSON object. A file holds text. So does a JSON string. The correspondence was always there; json2dir only refuses to pretend otherwise.

We do not need a template engine, an archive format, or a twelve-step bootstrap script to describe a tree of files. We need one value that a human can read and a machine can produce.

## II. One value, one tree

A json2dir document is a single object. It does not include other files, import modules, expand variables, or run hooks. What you read is what you get.

Composition belongs to the tools that generate the document: Nix, jq, Jsonnet, CUE, Dhall, a shell script, a language model with a strict schema. json2dir is the last step, and the last step should be boring.

## III. Four shapes are enough

```text
{ }                  a directory
"text"               a file
["link", target]     a symbolic link
["script", text]     an executable
```

Every feature added to the format is a feature every implementation must carry forever. Four shapes cover dotfiles, fixtures, skeletons and configuration trees. When they do not, the answer is a different tool, not a fifth shape.

## IV. Refuse loudly

A number is not a file. `..` is not a name. A slash is not a directory. An unknown array is not a guess.

When a document is wrong, a json2dir implementation stops and says so. Silent coercion is how a typo becomes `rm -rf` in somebody's home directory.

## V. Never follow a link you did not make

The target directory belongs to someone. A symbolic link already sitting in it is a question, not an invitation. Replace it; never write through it.

Security is not a footnote in the README. It is [Section 5.3 of the RFC](spec/rfc-json2dir.md#53-symbolic-links-are-not-followed), and it has tests.

## VI. The specification is the product

An idea that has only one implementation is an implementation detail. json2dir now has more ports than features, in Rust, Zig, Scheme, C#, MSBuild and Go, plus one that asks a language model nicely.

That is only useful if they agree. [RFC J2D-1](spec/rfc-json2dir.md) says what agreement means. The [conformance suite](conformance/README.md) checks it. Implementations compete on speed, safety and style, never on what a document means.

## VII. Rewrite it in your language

Rewriting json2dir is the best way to learn a language's file system API, its JSON story, and its error handling in one evening. It is small enough to finish and sharp enough to get wrong.

So write one. Run the suite. Send a pull request. Haskell, Nix and assembly are still [wanted](README.md#wanted).

## VIII. Or argue against it

`json2json` exists because someone disagreed hard enough to write code. `dir2dir` is still at the manifesto stage, and we know how that feels. Disagreement with tests attached is a contribution. Disagreement without them is a comment.

---

*Signed by everyone who ever typed `cat tree.json | json2dir` and watched it just work.*
