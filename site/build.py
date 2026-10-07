#!/usr/bin/env python3
"""Build the website from the repository's Markdown documents with pandoc.

Usage: python3 site/build.py [OUTPUT_DIRECTORY]   (default: _site)
"""

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"

# (source, output, page id, title, description)
PAGES = [
    ("README.md", "index.html", "home", "Awesome json2dir",
     "A curated list of json2dir implementations, ports, rewrites and heresies."),
    ("spec/rfc-json2dir.md", "rfc.html", "rfc", "RFC J2D-1: The json2dir Directory Tree Format",
     "The specification of the json2dir format: conversion scheme, processing model and security rules."),
    ("conformance/README.md", "conformance.html", "conformance", "json2dir Conformance Suite",
     "A language-agnostic test suite for json2dir implementations."),
    ("results/README.md", "results.html", "results", "json2dir Test Results",
     "Every buildable json2dir implementation run against the same black-box cases."),
    ("MANIFESTO.md", "manifesto.html", "manifesto", "The json2dir Manifesto",
     "A tree is a value. Write it down."),
    ("CONTRIBUTING.md", "contributing.html", "contributing", "Contributing to awesome-json2dir",
     "How to add an implementation or change the specification."),
]


def build_page(source: str, output: Path, page: str, title: str, description: str) -> None:
    subprocess.run(
        [
            "pandoc",
            str(ROOT / source),
            "--from=gfm",
            "--to=html5",
            "--standalone",
            f"--template={SITE / 'template.html'}",
            f"--lua-filter={SITE / 'links.lua'}",
            f"--metadata=pagetitle:{title}",
            f"--metadata=description:{description}",
            f"--metadata=source:{source}",
            f"--metadata=page:{page}",
            f"--metadata=nav_{page}:true",
            f"--output={output}",
        ],
        check=True,
    )


def main() -> int:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "_site"
    out.mkdir(parents=True, exist_ok=True)
    for source, name, page, title, description in PAGES:
        build_page(source, out / name, page, title, description)
        print(f"{source} -> {out / name}")
    shutil.copyfile(SITE / "style.css", out / "style.css")
    shutil.copyfile(SITE / "results.js", out / "results.js")
    shutil.copyfile(ROOT / "results" / "results.json", out / "results.json")
    for name in ("benchmarks.js", "benchmarks.css"):
        shutil.copyfile(SITE / name, out / name)
    for name in ("benchmarks.json", "benchmark-samples.json"):
        shutil.copyfile(ROOT / "results" / name, out / name)
    (out / ".nojekyll").touch()
    return 0


if __name__ == "__main__":
    sys.exit(main())
