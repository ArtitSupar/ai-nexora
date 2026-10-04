# AI Nexora — Analysis Package v0.1

Version: 0.1
Status: DRAFT
Owner: Ball
Strategic Partner: AI Co-CEO

---

## 1. Purpose

This document defines the structured output contract for the Analyst in AI Nexora Vertical Slice v0.1.

The Analysis Package is the formal handoff from Analyst analysis to the Evidence and Decision Gate stages.

It must contain enough structured information for:

1. another AI role to continue the workflow,
2. Ball to understand the findings,
3. Ball to make required human decisions,
4. later stages to verify what the Analyst concluded and why.

The Analysis Package is not an implementation plan.

The Analyst identifies and explains findings. The Analyst does not authorize code changes.

### ไทย

Analysis Package คือ Output แบบ Structured ของ Analyst สำหรับ Vertical Slice v0.1 ใช้ส่งต่องานจากการวิเคราะห์ไปยัง Evidence และ Decision Gate โดยต้องเพียงพอสำหรับ AI role ถัดไปและ Ball ในการตรวจสอบและตัดสินใจ

---

## 2. Design Principles

1. Structured over free-form conversation.
2. Evidence over confidence.
3. Findings must be traceable.
4. Facts must be separated from assumptions.
5. Conflicts must be explicit.
6. Unknowns must be explicit.
7. Recommendations must be separated from decisions.
8. Human decisions must be clearly identified.
9. No unauthorized implementation.
10. No Evidence, No DONE.

---

## 3. Package Lifecycle

```text
INPUT
  ↓
ANALYSIS
  ↓
FINDINGS
  ↓
EVIDENCE
  ↓
CLASSIFICATION
  ↓
RECOMMENDATION
  ↓
HUMAN DECISION REQUIRED?
  ↓
DECISION GATE
```

A revised package must remain traceable. Material changes should not silently overwrite an important previous conclusion.

---

## 4. Top-Level Structure

```text
Analysis Package
├── Metadata
├── Objective
├── Context
├── Inputs
├── Specification Understanding
├── Implementation Understanding
├── Findings
├── Evidence References
├── Risks
├── Recommended Actions
├── Do Not Change
├── Human Decisions Required
├── Acceptance Criteria
├── Confidence
└── Final Recommendation
```

---

## 5. Metadata

Required fields:

```text
Package ID
Version
Status
Created By
Created At
Project
Workflow
Related Goal
Related Decision
```

Recommended Package ID format: `AP-YYYY-###`.

Allowed Status values:

```text
DRAFT
READY_FOR_DECISION
SUPERSEDED
CLOSED
```

For the Vertical Slice, Created By is `ANALYST`.

---

## 6. Objective

The package must state what the Analyst was asked to determine.

Required fields:

```text
Objective
Scope
Success Criteria
```

The Objective must be specific enough to determine whether the analysis answered the requested question.

---

## 7. Context

Relevant context may include:

```text
Business Context
Technical Context
Project Context
Known Constraints
Relevant History
```

Only relevant context should be included.

---

## 8. Inputs

The package must list the inputs actually used by the Analyst.

Example:

```text
Inputs
├── API Specification
├── Existing Source Code
├── Working JSON Request
├── Failed JSON Request
├── Runtime Error Response
└── Relevant Project Evidence
```

Each input should identify:

```text
Input ID
Input Type
Description
Source
Version or Timestamp
Availability
```

The Analyst must not claim to have analyzed an input that was not actually available.

---

## 9. Specification Understanding

This section records the Analyst's understanding of the relevant specification.

It should include:

```text
Requirement ID
Field / Rule
Requirement
Required / Optional
Constraints
Source Reference
```

The Analyst should distinguish `SPEC FACT` from `ANALYST INTERPRETATION`.

If the specification is ambiguous or internally inconsistent, the ambiguity must be recorded as a finding or unknown rather than silently resolved.

---

## 10. Implementation Understanding

This section records observed implementation behavior.

It should include:

```text
Component
Observed Behavior
Relevant Code Evidence
Validation Behavior
Runtime Behavior
Notes
```

The Analyst must describe observed behavior rather than infer unverified implementation behavior.

If evidence is insufficient, classify the relevant conclusion as UNKNOWN.

---

## 11. Findings

Findings are the primary output of the Analysis Package.

Each finding must have:

```text
Finding ID
Title
Classification
Type
Description
Expected Behavior
Observed Behavior
Impact
Evidence
Recommendation
Human Decision Required
Confidence
```

Recommended Finding ID format:

```text
F-001
F-002
F-003
```

---

## 12. Finding Classification

### CONFIRMED

The finding has sufficient supporting evidence. CONFIRMED does not mean implementation is approved.

### CONFLICT

Requirements, evidence, or observed behavior conflict. Human decision is required.

### UNKNOWN

Evidence is insufficient to establish the correct conclusion. Additional evidence is required.

---

## 13. Finding Type

Recommended values:

```text
DATA_PROBLEM
CODE_PROBLEM
CONTRACT_CONFLICT
SPECIFICATION_PROBLEM
VALIDATION_GAP
TEST_GAP
UNKNOWN
OTHER
```

Classification and Type are separate.

Example:

```text
Classification: CONFIRMED
Type: DATA_PROBLEM
```

---

## 14. Evidence References

Evidence must be referenced from findings. Evidence is not the same thing as a decision.

Supported evidence types:

```text
SPEC
CODE
DIFF
TEST
RUNTIME
DATA
REVIEW
```

Each evidence reference should contain:

```text
Evidence ID
Evidence Type
Source
Location
Observation
Supports
```

Recommended Evidence ID format: `E-001`, `E-002`, `E-003`.

Example:

```text
E-001
Type: SPEC
Source: OIL006 Specification
Observation: ProductOrMaterialCode is mandatory
Supports: F-001
```

---

## 15. Facts, Assumptions, Conflicts, and Unknowns

The Analyst must explicitly distinguish:

### Facts

Directly supported by evidence.

### Assumptions

Reasonable interpretations that are not directly established by evidence. Assumptions must never be presented as facts.

### Conflicts

Two or more relevant sources or requirements disagree.

### Unknowns

The available evidence is insufficient to determine the correct conclusion.

Recommended structure:

```text
Facts
Assumptions
Conflicts
Unknowns
```

---

## 16. Request Difference Analysis

When multiple requests or runtime cases are provided, the package should compare them systematically.

```text
Field
Working Value
Failed Value
Difference
Expected Rule
Potential Impact
Evidence
```

The Analyst must not assume that a difference is the root cause unless evidence supports that conclusion.

---

## 17. Error / Root Cause Analysis

The package should distinguish:

```text
Observed Error
Confirmed Cause
Potential Cause
Unknown Cause
```

A confirmed root cause requires supporting evidence.

Example:

```text
Observed Error:
API002

Confirmed Cause:
Mandatory ProductOrMaterialCode is empty.

Potential Cause:
Other mandatory-field validation may also be triggered.

Unknown:
Whether another downstream validation would fail after ProductOrMaterialCode is corrected.
```

---

## 18. Recommended Actions

Recommendations describe what should happen next. Recommendations must be separated from authorization.

Each recommendation should contain:

```text
Recommendation ID
Action
Reason
Expected Impact
Risk
Requires Human Approval
```

Example:

```text
R-001
Action: Correct invalid ProductOrMaterialCode values in the request.
Reason: Mandatory field is empty.
Requires Human Approval: NO
```

For contract conflicts, `Requires Human Approval: YES`.

---

## 19. Do Not Change

The Analyst must explicitly identify things that should not be changed based on the current evidence.

Examples:

```text
Do not weaken validation merely to make an invalid request pass.
Do not change API contract by assumption.
Do not modify unrelated API behavior.
Do not change business rules without approval.
Do not modify production behavior.
```

This section protects the implementation boundary.

---

## 20. Human Decisions Required

This section lists decisions that cannot be safely made by the Analyst.

Each item should contain:

```text
Decision ID
Question
Why Human Decision Is Required
Options
AI Recommendation
Risk
Decision Status
```

Recommended status:

```text
PENDING
APPROVED
REJECTED
NEED_MORE_EVIDENCE
```

Example:

```text
Decision ID: D-001

Question:
Should CtrlTypeToList remain optional for Thai Oil when CtrlTypeTo = 3?

Why Human Decision Is Required:
Specification and observed implementation behavior conflict.

Options:
A. Follow specification.
B. Follow established business behavior.
C. Reconcile specification and business behavior.

AI Recommendation:
C. Reconcile the contract with the authoritative API/customer owner.

Decision Status:
PENDING
```

The Analyst may recommend. The Analyst may not make the decision.

---

## 21. Acceptance Criteria

Each criterion should contain:

```text
AC-ID
Criterion
Verification Method
Evidence Required
Status
```

Example:

```text
AC-01
All relevant mandatory fields were evaluated.

Verification:
Field-by-field compliance review.

Evidence:
Specification + implementation evidence.

Status:
PASS / FAIL / UNKNOWN
```

---

## 22. Confidence

Confidence is supporting metadata. Confidence does not replace evidence.

Recommended values:

```text
HIGH
MEDIUM
LOW
```

Confidence should explain why the level was assigned, what evidence supports it, and what could change the conclusion.

Example:

```text
Confidence: HIGH

Reason:
Specification, validator behavior, failed request data, and API error are consistent.
```

---

## 23. Final Recommendation

The package must end with a concise recommendation.

Recommended structure:

```text
Overall Status
Key Findings
Immediate Action
Human Decisions Required
Implementation Recommendation
Evidence Sufficiency
```

Example:

```text
Overall Status:
PARTIALLY COMPLIANT / CONTRACT RECONCILIATION REQUIRED

Key Findings:
- ProductOrMaterialCode is a confirmed request-data problem.
- CtrlTypeToList is a contract conflict.
- TankList / MeterList requires clarification.

Immediate Action:
Correct invalid request data.

Human Decisions Required:
Resolve contract behavior for CtrlTypeToList and Tank/Meter.

Implementation Recommendation:
Do not modify API code until contract decisions are resolved.

Evidence Sufficiency:
Sufficient for analysis; insufficient for contract changes.
```

---

## 24. OIL006 Reference Package

The Vertical Slice should be able to represent at least these findings.

### F-001

```text
Classification: CONFIRMED
Type: DATA_PROBLEM
```

Finding: ProductOrMaterialCode is empty in the failed request while the specification defines the field as mandatory.

Expected action: Do not modify the API merely to make the invalid request pass.

### F-002

```text
Classification: CONFLICT
Type: CONTRACT_CONFLICT
```

Finding: CtrlTypeToList is defined as mandatory by the specification, while existing implementation and historical behavior indicate that Thai Oil may omit it when CtrlTypeTo = 3.

Expected action: Human clarification is required.

### F-003

```text
Classification: CONFLICT or UNKNOWN
Type: VALIDATION_GAP or UNKNOWN
```

Finding: The specification states that TankList or MeterList should be supplied as one of the alternatives, while implementation behavior and test expectations require confirmation.

Expected action: Human clarification is required before implementation changes.

---

## 25. Package Quality Rules

An Analysis Package is not considered ready when:

- findings have no evidence,
- assumptions are presented as facts,
- conflicts are hidden,
- unknowns are presented as confirmed,
- recommendations are presented as decisions,
- human decisions are missing,
- scope is unclear,
- evidence cannot be traced,
- unauthorized implementation is implied.

An Analysis Package is ready for the Decision Gate when:

- objective is clear,
- inputs are identified,
- relevant requirements are documented,
- implementation behavior is supported by evidence,
- findings are classified,
- evidence is traceable,
- recommendations are explicit,
- human decisions are identified,
- acceptance criteria exist,
- no unauthorized implementation is included.

---

## 26. Handoff Contract

The Analysis Package is the formal handoff from Analyst to the next stage.

The next stage must be able to determine:

```text
What was analyzed?
What was found?
Why is it considered a finding?
What evidence supports it?
What is confirmed?
What conflicts?
What is unknown?
What should happen next?
What must not change?
What requires Ball's decision?
```

The receiving stage must not need to reconstruct the Analyst's reasoning from an informal chat transcript.

---

## 27. Versioning and Traceability

Every material revision should update:

```text
Version
Updated At
Updated By
Change Summary
```

Important findings should retain stable Finding IDs when the finding continues across package revisions.

If a finding is withdrawn or materially changed, the reason must be recorded.

---

## 28. Definition of Ready

An Analysis Package is READY_FOR_DECISION only when:

```text
Objective                 ✓
Inputs                    ✓
Specification             ✓
Implementation            ✓
Findings                  ✓
Evidence                  ✓
Classification            ✓
Recommendations           ✓
Do Not Change             ✓
Human Decisions           ✓
Acceptance Criteria       ✓
Confidence                ✓
Final Recommendation      ✓
```

If a required item is missing:

```text
NOT READY
```

---

## 29. Definition of Done

The Analysis Package is DONE only when:

1. required analysis was completed,
2. findings are supported by evidence,
3. classifications are justified,
4. conflicts and unknowns are explicit,
5. recommendations are separated from decisions,
6. human decision requirements are identified,
7. acceptance criteria are defined,
8. the package is traceable,
9. no unauthorized implementation was performed.

No Evidence, No DONE.

---

# Thai Summary

## เป้าหมาย

Analysis Package คือ Output แบบ Structured ของ Analyst ที่ใช้ส่งต่องานจากการวิเคราะห์ไปยัง Evidence และ Decision Gate

## หลักการสำคัญ

```text
Facts ≠ Assumptions
Evidence ≠ Confidence
Recommendation ≠ Decision
Conflict ≠ Confirmed
Unknown ≠ Confirmed
```

และ:

```text
Evidence
   ↓
Analysis
   ↓
Recommendation
   ↓
Human Decision
```

## Analyst ต้องตอบให้ได้

```text
วิเคราะห์อะไร?
พบอะไร?
รู้ได้อย่างไร?
Evidence อยู่ที่ไหน?
อะไร Confirmed?
อะไร Conflict?
อะไร Unknown?
ควรทำอะไรต่อ?
อะไรห้ามเปลี่ยน?
เรื่องไหนต้องให้ Ball ตัดสินใจ?
```

## สถานะ

```text
ANALYST
   ↓
ANALYSIS PACKAGE
   ↓
EVIDENCE
   ↓
DECISION GATE
   ↓
BALL
```

Analysis Package เป็น **handoff contract** ไม่ใช่เพียงรายงานข้อความจาก AI

Next Step:

```text
Implement the smallest executable Analyst flow
using this package contract.
```
