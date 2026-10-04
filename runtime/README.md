# AI Nexora — Runnable Workforce MVP

## Current workflow

Project Input
    ↓
Orchestrator
    ↓
Analyst
    ↓
Analysis Package
    ↓
Architect
    ↓
Architecture Package
    ↓
Human Decision

## Design boundary

The Workforce core does not contain OIL006-specific findings.

Projects provide their own input.

Current pilot projects:
- OIL006
- PROJECT-B

## Current guarantees

- Evidence classification is preserved.
- UNKNOWN blocks implementation authorization.
- CONFLICT blocks implementation authorization.
- Architect produces multiple options.
- Human decision remains explicit.
- DONE is not declared while unresolved decisions/evidence exist.
- No source-code modification is performed.
- No Git commit is performed automatically.
- No production action is performed.
