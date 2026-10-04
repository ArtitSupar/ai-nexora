import json
from dataclasses import asdict

from agents.analyst import Analyst
from agents.architect import Architect


class Orchestrator:

    def __init__(self):
        self.analyst = Analyst()
        self.architect = Architect()

    def run(self, task):
        analysis = self.analyst.analyze(task)
        architecture = self.architect.design(analysis)

        unresolved_unknowns = any(
            finding.classification == "UNKNOWN"
            for finding in analysis.findings
        )

        unresolved_conflicts = any(
            finding.classification == "CONFLICT"
            for finding in analysis.findings
        )

        decision_required = bool(
            analysis.human_decisions_required
            or unresolved_unknowns
            or unresolved_conflicts
        )

        done = not decision_required

        return {
            "project_id": task["project_id"],
            "task_id": task["task_id"],
            "workflow": [
                "ORCHESTRATOR",
                "ANALYST",
                "ANALYSIS_PACKAGE",
                "ARCHITECT",
                "ARCHITECTURE_PACKAGE",
                "HUMAN_DECISION",
            ],
            "analysis_package": asdict(analysis),
            "architecture_package": asdict(architecture),
            "status": (
                "READY_FOR_HUMAN_DECISION"
                if decision_required
                else "READY_FOR_NEXT_STAGE"
            ),
            "decision_required": decision_required,
            "done": done,
            "evidence_rule": "No Evidence, No DONE.",
        }


def run_file(path):
    with open(path, "r", encoding="utf-8-sig") as f:
        task = json.load(f)

    return Orchestrator().run(task)
