#!/usr/bin/env python3
"""json2dir conformance runner.

Runs every test case against an implementation and compares the directory
tree it produces with the expected one. See conformance/README.md.

Usage: python3 conformance/run.py [OPTIONS] COMMAND
"""

import argparse
import base64
import json
import os
import shlex
import signal
import stat
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

LEVELS = ("core", "overwrite")
INPUT_FIELDS = ("input", "input_text", "input_base64")
CASE_FIELDS = {"description", "section", "level", "setup", "expect", *INPUT_FIELDS}
EXPECT_FIELDS = {"tree", "error", "accept_error"}
DEFAULT_CASES = Path(__file__).resolve().parent / "cases"
DEFAULT_TIMEOUT = 10.0
EXEC_BITS = 0o111


class CaseError(Exception):
    """A test case file is malformed."""


@dataclass
class Case:
    name: str
    description: str
    section: str
    level: str
    setup: Optional[Dict[str, Any]]
    raw_input: bytes
    expect_tree: Optional[Dict[str, Any]]
    expect_error: bool
    accept_error: bool

    def input_bytes(self) -> bytes:
        return self.raw_input


@dataclass
class Result:
    status: str
    reason: str = ""
    stderr: str = field(default="", repr=False)


def parse_case(name: str, data: Any) -> Case:
    if not isinstance(data, dict):
        raise CaseError(f"{name}: a case must be a JSON object")
    unknown = set(data) - CASE_FIELDS
    if unknown:
        raise CaseError(f"{name}: unknown fields: {', '.join(sorted(unknown))}")
    for key in ("description", "section", "level", "expect"):
        if key not in data:
            raise CaseError(f"{name}: missing field {key!r}")
    if data["level"] not in LEVELS:
        raise CaseError(f"{name}: level must be one of {', '.join(LEVELS)}")

    inputs = [key for key in INPUT_FIELDS if key in data]
    if len(inputs) != 1:
        raise CaseError(f"{name}: exactly one of {', '.join(INPUT_FIELDS)} is required")
    if inputs[0] == "input":
        raw = json.dumps(data["input"], ensure_ascii=False).encode()
    elif inputs[0] == "input_text":
        raw = data["input_text"].encode()
    else:
        raw = base64.b64decode(data["input_base64"], validate=True)

    expect = data["expect"]
    if not isinstance(expect, dict) or set(expect) - EXPECT_FIELDS:
        raise CaseError(f"{name}: expect must be an object with {', '.join(sorted(EXPECT_FIELDS))}")
    tree = expect.get("tree")
    error = expect.get("error", False) is True
    accept_error = expect.get("accept_error", False) is True
    if (tree is None) == (not error) or (error and accept_error):
        raise CaseError(f"{name}: expect needs either 'tree' or 'error': true")
    if tree is not None and not isinstance(tree, dict):
        raise CaseError(f"{name}: expect.tree must be an object")

    setup = data.get("setup")
    if setup is not None and not isinstance(setup, dict):
        raise CaseError(f"{name}: setup must be an object")

    return Case(
        name=name,
        description=data["description"],
        section=str(data["section"]),
        level=data["level"],
        setup=setup,
        raw_input=raw,
        expect_tree=tree,
        expect_error=error,
        accept_error=accept_error,
    )


def load_cases(directory: Path) -> List[Case]:
    cases = []
    for path in sorted(directory.rglob("*.json")):
        name = path.relative_to(directory).with_suffix("").as_posix()
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except ValueError as error:
            raise CaseError(f"{name}: {error}") from error
        cases.append(parse_case(name, data))
    return cases


def read_tree(root: Path) -> Dict[str, Any]:
    """Describe a directory in the json2dir scheme, without following symlinks."""
    tree: Dict[str, Any] = {}
    with os.scandir(root) as entries:
        for entry in entries:
            tree[entry.name] = read_entry(Path(entry.path))
    return tree


def read_entry(path: Path) -> Any:
    info = os.lstat(path)
    if stat.S_ISLNK(info.st_mode):
        return ["link", os.readlink(path)]
    if stat.S_ISDIR(info.st_mode):
        return read_tree(path)
    if not stat.S_ISREG(info.st_mode):
        return ["special", oct(stat.S_IFMT(info.st_mode))]

    data = path.read_bytes()
    try:
        content = data.decode("utf-8")
    except UnicodeDecodeError:
        return ["bytes", base64.b64encode(data).decode()]

    exec_bits = info.st_mode & EXEC_BITS
    if exec_bits == 0:
        return content
    if exec_bits == EXEC_BITS:
        return ["script", content]
    return ["mode", f"{stat.S_IMODE(info.st_mode):04o}", content]


def write_tree(root: Path, tree: Dict[str, Any]) -> None:
    """Materialize a json2dir tree; used to prepare pre-existing state."""
    for name in sorted(tree):
        value = tree[name]
        path = root / name
        if isinstance(value, dict):
            path.mkdir()
            write_tree(path, value)
        elif isinstance(value, str):
            path.write_text(value, encoding="utf-8")
        elif value[0] == "script":
            path.write_text(value[1], encoding="utf-8")
            path.chmod(stat.S_IMODE(path.stat().st_mode) | EXEC_BITS)
        elif value[0] == "link":
            os.symlink(value[1], path)
        else:
            raise CaseError(f"unsupported setup value at {path}: {value!r}")


def show(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False)


def diff_trees(expected: Dict[str, Any], actual: Dict[str, Any], prefix: str = "") -> List[str]:
    lines = []
    for name in sorted(set(expected) | set(actual)):
        path = prefix + name
        if name not in actual:
            lines.append(f"{path}: missing")
        elif name not in expected:
            lines.append(f"{path}: unexpected entry")
        elif isinstance(expected[name], dict) and isinstance(actual[name], dict):
            lines.extend(diff_trees(expected[name], actual[name], path + "/"))
        elif expected[name] != actual[name]:
            lines.append(f"{path}: expected {show(expected[name])}, got {show(actual[name])}")
    return lines


def execute(command: str, cwd: Path, stdin: bytes, timeout: float):
    process = subprocess.Popen(
        command,
        shell=True,
        cwd=cwd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        start_new_session=True,
        umask=0o022,
    )
    try:
        _, stderr = process.communicate(stdin, timeout=timeout)
    except subprocess.TimeoutExpired:
        os.killpg(process.pid, signal.SIGKILL)
        process.communicate()
        return None, ""
    except BrokenPipeError:
        _, stderr = process.communicate()
    return process.returncode, stderr.decode("utf-8", "replace")


def run_case(case: Case, command: str, timeout: float = DEFAULT_TIMEOUT) -> Result:
    with tempfile.TemporaryDirectory(prefix="json2dir-sandbox-") as sandbox, \
            tempfile.TemporaryDirectory(prefix="json2dir-input-") as input_dir:
        root = Path(sandbox) / "root"
        root.mkdir()
        if case.setup:
            write_tree(root, case.setup)

        input_path = Path(input_dir) / "input.json"
        input_path.write_bytes(case.input_bytes())
        resolved = command.replace("{input}", shlex.quote(str(input_path)))
        resolved = resolved.replace("{output}", shlex.quote(str(root)))

        status, stderr = execute(resolved, root, case.input_bytes(), timeout)
        if status is None:
            return Result("fail", f"timed out after {timeout:g}s")

        escaped = sorted(set(os.listdir(sandbox)) - {"root"})
        if escaped:
            return Result("fail", f"wrote outside the target directory: {', '.join(escaped)}", stderr)

        if status != 0:
            if case.expect_error or case.accept_error:
                return Result("pass", stderr=stderr)
            last = stderr.strip().splitlines()[-1:] or [""]
            return Result("fail", f"exit status {status}: {last[0]}".rstrip(": "), stderr)

        if case.expect_error:
            return Result("fail", "expected failure (non-zero exit status), got success", stderr)

        diff = diff_trees(case.expect_tree, read_tree(root))
        if diff:
            return Result("fail", "; ".join(diff), stderr)
        return Result("pass", stderr=stderr)


def paint(text: str, color: str, enabled: bool) -> str:
    codes = {"green": "32", "red": "31", "dim": "2", "bold": "1"}
    return f"\033[{codes[color]}m{text}\033[0m" if enabled else text


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Run the json2dir conformance suite against an implementation.",
        epilog=(
            "COMMAND is run by /bin/sh inside an empty target directory with the input on stdin. "
            "{input} and {output} in COMMAND are replaced with the input file path and the "
            "target directory path."
        ),
    )
    parser.add_argument("command", metavar="COMMAND", help="shell command that runs the implementation")
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES, help="directory with test cases")
    parser.add_argument("--level", choices=LEVELS, action="append", help="run only this level (repeatable)")
    parser.add_argument("--filter", default="", help="run only cases whose name contains this text")
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT, help="seconds per case")
    parser.add_argument("--json", type=Path, help="also write results to this JSON file")
    parser.add_argument("--verbose", action="store_true", help="print stderr of failing cases")
    args = parser.parse_args(argv)

    try:
        cases = load_cases(args.cases)
    except CaseError as error:
        print(f"invalid test case: {error}", file=sys.stderr)
        return 2

    levels = args.level or list(LEVELS)
    cases = [c for c in cases if c.level in levels and args.filter in c.name]
    color = sys.stdout.isatty() and "NO_COLOR" not in os.environ

    results = []
    for case in cases:
        result = run_case(case, args.command, args.timeout)
        results.append((case, result))
        if result.status == "pass":
            print(f"{paint('✓', 'green', color)} {case.name} {paint(case.description, 'dim', color)}")
        else:
            print(f"{paint('✗', 'red', color)} {case.name} {paint(case.description, 'dim', color)}")
            print(f"    {result.reason}  [RFC §{case.section}]")
            if args.verbose and result.stderr.strip():
                for line in result.stderr.strip().splitlines():
                    print(f"    | {line}")

    print()
    failed = 0
    for level in levels:
        level_results = [r for c, r in results if c.level == level]
        passed = sum(r.status == "pass" for r in level_results)
        failed += len(level_results) - passed
        verdict = "conformant" if passed == len(level_results) else "not conformant"
        line = f"{level:<10} {passed}/{len(level_results)} passed — {verdict}"
        print(paint(line, "bold", color))

    if args.json:
        args.json.write_text(
            json.dumps(
                {
                    "command": args.command,
                    "results": [
                        {"case": c.name, "level": c.level, "status": r.status, "reason": r.reason}
                        for c, r in results
                    ],
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
