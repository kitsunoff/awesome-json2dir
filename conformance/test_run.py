"""Tests for the json2dir conformance runner.

Run with: python3 -m unittest discover --start-directory conformance
"""

import base64
import json
import os
import shlex
import stat
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import run  # noqa: E402

PYTHON = shlex.quote(sys.executable)
MODEL = f"{PYTHON} {shlex.quote(str(HERE / 'selftest' / 'model.py'))}"


def fake_impl(body: str) -> str:
    """Return a shell command running a small Python program as an implementation."""
    return f"{PYTHON} -c {shlex.quote(body)}"


def make_case(**fields) -> run.Case:
    data = {"description": "test case", "section": "1", "level": "core"}
    data.update(fields)
    return run.parse_case("test", data)


class ReadTreeTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_empty_directory(self):
        self.assertEqual(run.read_tree(self.root), {})

    def test_regular_file_and_nested_directory(self):
        (self.root / "f").write_text("content")
        (self.root / "d" / "e").mkdir(parents=True)
        self.assertEqual(run.read_tree(self.root), {"f": "content", "d": {"e": {}}})

    def test_script_has_all_execute_bits(self):
        script = self.root / "s"
        script.write_text("#!/bin/sh\n")
        script.chmod(0o755)
        self.assertEqual(run.read_tree(self.root), {"s": ["script", "#!/bin/sh\n"]})

    def test_partial_execute_bits_are_reported(self):
        script = self.root / "s"
        script.write_text("x")
        script.chmod(0o744)
        self.assertEqual(run.read_tree(self.root), {"s": ["mode", "0744", "x"]})

    def test_symlink_is_not_followed(self):
        (self.root / "t").write_text("x")
        os.symlink("t", self.root / "l")
        os.symlink("/nonexistent/target", self.root / "dangling")
        self.assertEqual(
            run.read_tree(self.root),
            {"t": "x", "l": ["link", "t"], "dangling": ["link", "/nonexistent/target"]},
        )

    def test_symlink_to_directory_is_not_descended(self):
        (self.root / "d").mkdir()
        os.symlink("d", self.root / "l")
        self.assertEqual(run.read_tree(self.root), {"d": {}, "l": ["link", "d"]})

    def test_non_utf8_file_is_reported_as_bytes(self):
        (self.root / "b").write_bytes(b"\xff\x00")
        self.assertEqual(
            run.read_tree(self.root),
            {"b": ["bytes", base64.b64encode(b"\xff\x00").decode()]},
        )


class WriteTreeTest(unittest.TestCase):
    def test_round_trip(self):
        tree = {
            "f": "content",
            "empty": "",
            "d": {"sub": {"deep": "x"}, "e": {}},
            "s": ["script", "#!/bin/sh\necho hi\n"],
            "l": ["link", "d/sub"],
            "dangling": ["link", "../nowhere"],
        }
        with tempfile.TemporaryDirectory() as tmp:
            run.write_tree(Path(tmp), tree)
            self.assertEqual(run.read_tree(Path(tmp)), tree)

    def test_regular_file_is_not_executable(self):
        with tempfile.TemporaryDirectory() as tmp:
            run.write_tree(Path(tmp), {"f": "x"})
            mode = os.stat(Path(tmp) / "f").st_mode
            self.assertEqual(stat.S_IMODE(mode) & 0o111, 0)


class DiffTreesTest(unittest.TestCase):
    def test_equal_trees_have_no_diff(self):
        self.assertEqual(run.diff_trees({"a": {"b": "x"}}, {"a": {"b": "x"}}), [])

    def test_reports_missing_extra_and_changed_paths(self):
        diff = run.diff_trees(
            {"missing": "x", "changed": "old", "d": {"inner": "x"}},
            {"extra": "y", "changed": "new", "d": {"inner": ["link", "x"]}},
        )
        self.assertEqual(
            diff,
            [
                'changed: expected "old", got "new"',
                'd/inner: expected "x", got ["link", "x"]',
                "extra: unexpected entry",
                "missing: missing",
            ],
        )


class ParseCaseTest(unittest.TestCase):
    def test_valid_case(self):
        case = make_case(input={}, expect={"tree": {}})
        self.assertEqual(case.input_bytes(), b"{}")
        self.assertEqual(case.expect_tree, {})
        self.assertFalse(case.expect_error)

    def test_input_text_is_used_verbatim(self):
        case = make_case(input_text='{"a":"1","a":"2"}', expect={"error": True})
        self.assertEqual(case.input_bytes(), b'{"a":"1","a":"2"}')

    def test_input_base64_is_decoded(self):
        case = make_case(input_base64="/w==", expect={"error": True})
        self.assertEqual(case.input_bytes(), b"\xff")

    def test_input_value_keeps_non_ascii_as_utf8(self):
        case = make_case(input={"ф": "🦀"}, expect={"tree": {"ф": "🦀"}})
        self.assertEqual(case.input_bytes(), '{"ф": "🦀"}'.encode())

    def test_rejects_multiple_inputs(self):
        with self.assertRaises(run.CaseError):
            make_case(input={}, input_text="{}", expect={"tree": {}})

    def test_rejects_missing_input(self):
        with self.assertRaises(run.CaseError):
            make_case(expect={"tree": {}})

    def test_rejects_unknown_level(self):
        with self.assertRaises(run.CaseError):
            make_case(level="extra", input={}, expect={"tree": {}})

    def test_rejects_expectation_without_tree_or_error(self):
        with self.assertRaises(run.CaseError):
            make_case(input={}, expect={})

    def test_rejects_unknown_fields(self):
        with self.assertRaises(run.CaseError):
            make_case(input={}, expect={"tree": {}}, typo=True)


class RunCaseTest(unittest.TestCase):
    def test_pass_when_tree_matches(self):
        case = make_case(input={"f": "x"}, expect={"tree": {"f": "x"}})
        impl = fake_impl("open('f', 'w').write('x')")
        self.assertEqual(run.run_case(case, impl).status, "pass")

    def test_fail_when_tree_differs(self):
        case = make_case(input={"f": "x"}, expect={"tree": {"f": "x"}})
        result = run.run_case(case, fake_impl("pass"))
        self.assertEqual(result.status, "fail")
        self.assertIn("f: missing", result.reason)

    def test_fail_on_nonzero_exit_when_tree_expected(self):
        case = make_case(input={}, expect={"tree": {}})
        result = run.run_case(case, fake_impl("raise SystemExit(1)"))
        self.assertEqual(result.status, "fail")
        self.assertIn("exit status 1", result.reason)

    def test_pass_on_nonzero_exit_when_error_expected(self):
        case = make_case(input_text="nope", expect={"error": True})
        self.assertEqual(run.run_case(case, fake_impl("raise SystemExit(1)")).status, "pass")

    def test_fail_on_zero_exit_when_error_expected(self):
        case = make_case(input_text="nope", expect={"error": True})
        result = run.run_case(case, fake_impl("pass"))
        self.assertEqual(result.status, "fail")
        self.assertIn("expected failure", result.reason)

    def test_accept_error_allows_either_outcome(self):
        case = make_case(input={}, expect={"tree": {"a": "x"}, "accept_error": True})
        self.assertEqual(run.run_case(case, fake_impl("raise SystemExit(1)")).status, "pass")
        self.assertEqual(run.run_case(case, fake_impl("open('a', 'w').write('x')")).status, "pass")
        self.assertEqual(run.run_case(case, fake_impl("pass")).status, "fail")

    def test_fail_when_writing_outside_root(self):
        case = make_case(input_text="nope", expect={"error": True})
        result = run.run_case(case, fake_impl("open('../escaped', 'w').write('x'); raise SystemExit(1)"))
        self.assertEqual(result.status, "fail")
        self.assertIn("outside the target directory", result.reason)

    def test_setup_tree_is_created_before_run(self):
        case = make_case(setup={"old": "x"}, input={}, expect={"tree": {"old": "x"}})
        self.assertEqual(run.run_case(case, fake_impl("pass")).status, "pass")

    def test_stdin_receives_input(self):
        case = make_case(input={"f": "x"}, expect={"tree": {"f": '{"f": "x"}'}})
        impl = fake_impl("import sys; open('f', 'w').write(sys.stdin.read())")
        self.assertEqual(run.run_case(case, impl).status, "pass")

    def test_input_and_output_placeholders(self):
        case = make_case(input={"f": "x"}, expect={"tree": {"f": '{"f": "x"}'}})
        body = "import sys; open(sys.argv[2] + '/f', 'w').write(open(sys.argv[1]).read())"
        impl = fake_impl(body) + " {input} {output}"
        self.assertEqual(run.run_case(case, impl).status, "pass")

    def test_timeout_is_a_failure(self):
        case = make_case(input={}, expect={"tree": {}})
        result = run.run_case(case, fake_impl("import time; time.sleep(5)"), timeout=0.5)
        self.assertEqual(result.status, "fail")
        self.assertIn("timed out", result.reason)


class SuiteTest(unittest.TestCase):
    """The bundled cases must be valid and pass against the Python model."""

    def test_all_cases_load(self):
        cases = run.load_cases(HERE / "cases")
        self.assertGreater(len(cases), 40)
        self.assertEqual(len({c.name for c in cases}), len(cases))

    def test_model_passes_every_case(self):
        failures = [
            f"{case.name}: {result.reason}"
            for case in run.load_cases(HERE / "cases")
            for result in [run.run_case(case, MODEL)]
            if result.status != "pass"
        ]
        self.assertEqual(failures, [])


if __name__ == "__main__":
    unittest.main()
