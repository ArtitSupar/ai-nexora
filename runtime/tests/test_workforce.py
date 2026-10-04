import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OIL006 = ROOT / "examples" / "oil006" / "input.json"
PROJECT_B = ROOT / "examples" / "project-b" / "input.json"


def run_cli(input_file):
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "runtime.cli",
            str(input_file),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )

    return json.loads(result.stdout)


class WorkforceTests(unittest.TestCase):

    def test_oil006_runs(self):
        data = run_cli(OIL006)

        self.assertEqual(data["project_id"], "OIL006")
        self.assertEqual(data["status"], "READY_FOR_HUMAN_DECISION")
        self.assertTrue(data["decision_required"])
        self.assertFalse(data["done"])

    def test_oil006_preserves_evidence_classification(self):
        data = run_cli(OIL006)

        findings = {
            item["finding_id"]: item["classification"]
            for item in data["analysis_package"]["findings"]
        }

        self.assertEqual(findings["F-001"], "UNKNOWN")
        self.assertEqual(findings["F-002"], "CONFLICT")
        self.assertEqual(findings["F-003"], "UNKNOWN")

    def test_oil006_has_multiple_architecture_options(self):
        data = run_cli(OIL006)

        options = data["architecture_package"]["options"]

        self.assertGreaterEqual(len(options), 2)
        self.assertEqual(options[0]["option_id"], "F-002-A")
        self.assertEqual(options[1]["option_id"], "F-002-B")

    def test_traceability(self):
        data = run_cli(OIL006)

        self.assertEqual(
            data["architecture_package"]["source_analysis_package"],
            data["analysis_package"]["package_id"],
        )

    def test_project_b_works_without_oil006_logic(self):
        data = run_cli(PROJECT_B)

        self.assertEqual(data["project_id"], "PROJECT-B")
        self.assertEqual(data["status"], "READY_FOR_HUMAN_DECISION")
        self.assertTrue(data["decision_required"])
        self.assertFalse(data["done"])

        options = data["architecture_package"]["options"]

        self.assertGreaterEqual(len(options), 2)

    def test_evidence_rule_is_enforced(self):
        data = run_cli(PROJECT_B)

        self.assertEqual(
            data["evidence_rule"],
            "No Evidence, No DONE.",
        )

        self.assertFalse(data["done"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
