from dataclasses import dataclass
from typing import List


@dataclass
class Finding:
    finding_id: str
    classification: str
    finding_type: str
    summary: str
    evidence: List[str]
    confidence: str = "MEDIUM"


@dataclass
class AnalysisPackage:
    package_id: str
    project_id: str
    objective: str
    findings: List[Finding]
    human_decisions_required: List[str]


@dataclass
class ArchitectureOption:
    option_id: str
    title: str
    description: str
    risks: List[str]


@dataclass
class ArchitecturePackage:
    package_id: str
    source_analysis_package: str
    impact: List[str]
    options: List[ArchitectureOption]
    recommendation: str
    human_decisions_required: List[str]
