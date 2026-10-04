from contracts.models import AnalysisPackage, Finding


class Analyst:

    def analyze(self, task):
        findings = [
            Finding(
                finding_id=item["finding_id"],
                classification=item["classification"],
                finding_type=item["finding_type"],
                summary=item["summary"],
                evidence=item.get("evidence", []),
                confidence=item.get("confidence", "MEDIUM"),
            )
            for item in task.get("findings", [])
        ]

        decisions = [
            item["decision"]
            for item in task.get("human_decisions_required", [])
        ]

        return AnalysisPackage(
            package_id=f'{task["project_id"]}-ANALYSIS-v0.1',
            project_id=task["project_id"],
            objective=task["objective"],
            findings=findings,
            human_decisions_required=decisions,
        )
