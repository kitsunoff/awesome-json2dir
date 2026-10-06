#!/usr/bin/env python3
"""Executable model of the reference json2dir, used to self-test the suite.

It mirrors alurm/json2dir src/main.rs step by step: read stdin, parse the
whole document, then walk members in byte order, unlinking whatever
non-directory entry is in the way before creating each one.

One deliberate difference: names that contain "/" are always rejected.
The reference accepts trailing separators, which RFC J2D-1 leaves optional.

It is not a recommended implementation: it exists so the conformance cases
can be checked without building the reference.
"""

import json
import os
import stat
import sys


class Failure(Exception):
    pass


def reject_constant(name):
    raise ValueError(f"{name} is not valid JSON")


def parse(data: bytes):
    text = data.decode("utf-8")
    document = json.loads(text, parse_constant=reject_constant)
    # Python accepts lone surrogate escapes; JSON text in UTF-8 cannot carry them.
    json.dumps(document, ensure_ascii=False).encode("utf-8")
    return document


def check_name(name: str) -> None:
    if name in ("", ".", "..") or "/" in name or "\0" in name:
        raise Failure(f"invalid name {name!r}")


def materialize(directory: dict) -> None:
    for name in sorted(directory):
        value = directory[name]
        check_name(name)
        try:
            os.unlink(name)
        except OSError:
            pass

        if isinstance(value, dict):
            try:
                os.mkdir(name)
            except FileExistsError:
                pass
            os.chdir(name)
            materialize(value)
            os.chdir("..")
        elif isinstance(value, str):
            with open(name, "wb") as file:
                file.write(value.encode("utf-8"))
        elif (
            isinstance(value, list)
            and len(value) == 2
            and all(isinstance(part, str) for part in value)
            and value[0] in ("link", "script")
        ):
            kind, payload = value
            if kind == "link":
                os.symlink(payload, name)
            else:
                with open(name, "wb") as file:
                    file.write(payload.encode("utf-8"))
                mode = stat.S_IMODE(os.stat(name).st_mode)
                os.chmod(name, mode | 0o111)
        else:
            raise Failure(f"invalid value at {name!r}")


def main() -> int:
    if len(sys.argv) != 1:
        print("Usage: model.py < file.json", file=sys.stderr)
        return 1
    try:
        document = parse(sys.stdin.buffer.read())
        if not isinstance(document, dict):
            raise Failure("expected provided JSON to be an object")
        materialize(document)
    except (Failure, ValueError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
