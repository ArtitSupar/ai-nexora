from contracts.models import ArchitecturePackage, ArchitectureOption


class Architect:

    def design(self, analysis):
        impact = []
        conflicts = []

        for finding in analysis.findings:

            if finding.classification == "CONFLICT":
                conflicts.append(finding)

                impact.append(
                    f"{finding.finding_id}: confirmed conflict requires "
                    "human decision before implementation."
                )

            elif finding.classification == "UNKNOWN":
                impact.append(
                    f"{finding.finding_id}: insufficient evidence; "
                    "implementation must not be authorized yet."
                )

        options = []

        if conflicts:
            conflict = conflicts[0]

            options = [
                ArchitectureOption(
                    option_id=f"{conflict.finding_id}-A",
                    title="Align implementation to the current specification",
                    description=(
                        "Treat the specification as authoritative and update "
                        "the implementation/example/client behavior accordingly."
                    ),
                    risks=[
                        "Existing clients or examples may become incompatible."
                    ],
                ),
                ArchitectureOption(
                    option_id=f"{conflict.finding_id}-B",
                    title="Clarify and revise the contract",
                    description=(
                        "Confirm the intended business rule and revise the "
                        "specification/example so the contract is unambiguous "
                        "before implementation."
                    ),
                    risks=[
                        "Implementation may be delayed until the requirement "
                        "is clarified."
                    ],
                ),
            ]

        if not options:
            options = [
                ArchitectureOption(
                    option_id="GENERAL-A",
                    title="Proceed after evidence review",
                    description=(
                        "Proceed only when all required evidence and acceptance "
                        "criteria are satisfied."
                    ),
                    risks=["Insufficient evidence may remain undetected."],
                ),
                ArchitectureOption(
                    option_id="GENERAL-B",
                    title="Collect additional evidence first",
                    description=(
                        "Pause implementation and collect the missing evidence "
                        "before authorizing changes."
                    ),
                    risks=["Delivery may be delayed."],
                ),
            ]

        if conflicts:
            recommendation = (
                "Resolve the confirmed contract conflict before implementation. "
                "Clarifying the contract is preferred when the intended business "
                "rule is not independently established."
            )
        else:
            recommendation = (
                "Collect sufficient evidence before authorizing implementation."
            )

        return ArchitecturePackage(
            package_id=f"{analysis.project_id}-ARCHITECTURE-v0.1",
            source_analysis_package=analysis.package_id,
            impact=impact,
            options=options,
            recommendation=recommendation,
            human_decisions_required=analysis.human_decisions_required,
        )
