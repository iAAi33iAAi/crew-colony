"""Contract tests for the current Crew Colony repository scaffold.

These checks validate repository contents and truthful status labeling only.
They do not test an executable multi-agent runtime or production conformance.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CrewColonyScaffoldContractTests(unittest.TestCase):
    def test_current_scaffold_files_are_present(self) -> None:
        for relative in ("README.md", "LICENSE", "src/__init__.py", "tests/__init__.py"):
            with self.subTest(path=relative):
                self.assertTrue((ROOT / relative).is_file(), f"missing scaffold artifact: {relative}")

    def test_readme_truthfully_discloses_missing_runtime(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        self.assertIn("multi-agent colony concept and repository scaffold", readme)
        self.assertIn("scaffold / documentation state", readme)
        self.assertIn("executable crew_colony.py runtime", readme)
        self.assertIn("not currently present", readme)
        self.assertIn("does not contain the previously claimed 7-agent implementation or 21-test suite", readme)
        self.assertIn("not evidence of an implemented geometric runtime", readme)

    def test_documented_manna_allocation_sums_to_one_hundred(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        values = {
            name: int(value)
            for name, value in re.findall(
                r"^-\s*(Human|Vault|Architect):\s*(\d+)%\s*$",
                readme,
                re.MULTILINE,
            )
        }
        self.assertEqual(values, {"Human": 84, "Vault": 15, "Architect": 1})
        self.assertEqual(sum(values.values()), 100)

    def test_no_runtime_or_test_suite_is_claimed_by_the_package_files(self) -> None:
        self.assertFalse((ROOT / "src" / "crew_colony.py").exists())
        readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        self.assertIn("until corresponding code and ci evidence exist", readme)

    def test_suite_identifies_itself_as_a_scaffold_contract(self) -> None:
        source = Path(__file__).read_text(encoding="utf-8")
        self.assertIn("Contract tests for the current Crew Colony repository scaffold", source)
        self.assertIn("They do not test an executable multi-agent runtime", source)


if __name__ == "__main__":
    unittest.main()
