# AI Nexora — Vertical Slice v0.1
# Implementation Specification

Version: 0.1
Status: APPROVED WITH MINOR CHANGES
Owner: Ball
Strategic Partner: AI Co-CEO

---

## 1. Purpose

### English

This document defines the implementation scope and operating rules
for the AI Nexora Vertical Slice v0.1.

The Vertical Slice is a capability experiment.

Its purpose is to prove that AI Nexora can:

1. receive a real software engineering problem,
2. analyze specification and implementation evidence,
3. identify compliance findings,
4. distinguish confirmed findings from conflicts and unknowns,
5. provide traceable evidence,
6. identify decisions that require human authority,
7. stop before unauthorized implementation,
8. provide useful information for human decision-making.

The Vertical Slice is not intended to implement the complete AI Nexora platform.

### ไทย

เอกสารนี้กำหนดขอบเขตและกติกาการทำงานของ AI Nexora Vertical Slice v0.1

Vertical Slice นี้เป็นการทดลองความสามารถของ Nexora

เป้าหมายคือพิสูจน์ว่า AI Nexora สามารถ:

1. รับปัญหาด้าน Software Engineering จริง
2. วิเคราะห์ Specification และหลักฐานจาก Implementation
3. ระบุ Findings ที่พบ
4. แยก Confirmed Findings, Conflicts และ Unknowns
5. แสดง Evidence ที่ตรวจสอบย้อนกลับได้
6. ระบุเรื่องที่ต้องให้มนุษย์ตัดสินใจ
7. หยุดก่อนทำ Implementation ที่ไม่ได้รับอนุมัติ
8. ให้ข้อมูลที่เพียงพอสำหรับมนุษย์ในการตัดสินใจ

Vertical Slice นี้ไม่ได้มีเป้าหมายที่จะสร้าง AI Nexora ทั้งระบบ

---

## 2. Validation Project

The Vertical Slice will be validated using the OIL006 API compliance problem.

Input materials:

1. OIL006 API Specification
2. Existing API source code
3. Working JSON request
4. Failed JSON request
5. API error response
6. Relevant project evidence

The OIL006 project is used as a validation case.

It is not the architecture or identity of AI Nexora.

---

## 3. Vertical Slice Scope

### Included

The Vertical Slice includes:

- Orchestrator
- Analyst
- Analysis Package
- Evidence Model
- Decision Gate
- Human Escalation

### Excluded

The Vertical Slice does not include:

- Autonomous Developer
- Autonomous QA
- Autonomous Reviewer
- Autonomous code modification
- Automatic Git commit
- Production actions
- Multi-project orchestration
- Web UI
- SaaS functionality
- Large-scale infrastructure
- Autonomous learning system

The purpose is to validate the decision and analysis loop before expanding the workforce.

---

## 4. Target Workflow

```text
BALL
  ↓
ORCHESTRATOR
  ↓
ANALYST
  ↓
ANALYSIS PACKAGE
  ↓
EVIDENCE
  ↓
DECISION GATE
  ↓
BALL

---

## 9. Decision Gate

The Decision Gate determines whether analysis can proceed,
must stop for human decision, or requires additional evidence.

Possible states:

### CONFIRMED

The finding has sufficient supporting evidence.

This does not mean that implementation is approved.

### CONFLICT

Requirements, evidence, or observed behavior conflict.

Human decision is required.

### UNKNOWN

Evidence is insufficient to establish the finding.

Additional evidence is required.

The Decision Gate must not make business or strategic decisions
on behalf of Ball.

### Human Decision Boundary

The system must escalate to Ball when a decision involves:

- major business or strategic direction,
- scope expansion,
- production-impacting actions,
- security-sensitive actions,
- financial commitments,
- significant architecture changes,
- conflicting requirements,
- unclear requirements,
- insufficient evidence,
- repeated AI failure,
- high-risk changes.

---

## 10. Evidence Contract

### Principle

No Evidence, No DONE.

A claim is not evidence.

Confidence is not evidence.

An agent must provide evidence that allows another party
to verify the claim.

### Evidence Types

Evidence may include:

```text
SPEC
CODE
DIFF
TEST
RUNTIME
DATA
REVIEW
```

Each evidence item should be:

- identifiable,
- traceable,
- relevant to the claim,
- sufficient for verification,
- associated with the finding or decision it supports.

### Evidence and Decision Separation

Decision records are not evidence themselves.

A decision records an authorized human or governance decision
made based on available evidence.

Evidence supports a decision.

A decision does not replace evidence.

The relationship is:

```text
Evidence
   ↓
Analysis
   ↓
Decision
```

not:

```text
Decision
   =
Evidence
```

---

## 11. Analysis Package

The Analyst must produce a structured Analysis Package.

The package should contain:

```text
1. Objective
2. Context
3. Specification Understanding
4. Current Implementation Understanding
5. Findings
6. Evidence
7. Risks
8. Recommended Actions
9. Do Not Change
10. Human Decisions Required
11. Acceptance Criteria
12. Confidence
13. Final Recommendation
```

Each finding should contain at minimum:

```text
Finding ID
Title
Classification
Description
Evidence
Impact
Recommendation
Human Decision Required
```

---

## 12. Human Decision Model

AI Nexora does not replace Ball as the final decision maker.

The expected decision flow is:

```text
ANALYST
   ↓
FINDING
   ↓
EVIDENCE
   ↓
CLASSIFICATION
   ↓
DECISION GATE
   ↓
HUMAN DECISION
   ↓
APPROVED / REJECTED / NEED MORE EVIDENCE
```

The AI may:

- analyze,
- challenge,
- recommend,
- explain risks,
- present alternatives.

The AI may not:

- silently make high-impact decisions,
- change requirements by assumption,
- expand scope without approval,
- declare conflicting requirements resolved without authority.

---

## 13. Expected OIL006 Decision State

Before implementation changes are considered,
the Vertical Slice should produce a state similar to:

```text
ProductOrMaterialCode
    → CONFIRMED
    → DATA_PROBLEM
    → No API code change

CtrlTypeToList
    → CONFLICT
    → CONTRACT_CONFLICT
    → Human decision required

TankList / MeterList
    → CONFLICT or UNKNOWN
    → Contract clarification required

Other validation gaps
    → REVIEW
    → Additional evidence / decision required
```

Expected overall status:

```text
PARTIALLY COMPLIANT
+
CONTRACT RECONCILIATION REQUIRED
```

No implementation change is authorized by this document.

---

## 14. Success Condition

The Vertical Slice is successful when it can:

- process the OIL006 validation case,
- identify relevant findings,
- distinguish data problems from code problems,
- identify contract conflicts,
- identify unknowns,
- provide traceable evidence,
- identify human decisions,
- avoid unauthorized implementation changes,
- allow Ball to independently review the findings and evidence,
- provide sufficient information for Ball to make required decisions.

The vertical slice validates not only whether AI can produce an analysis,
but whether the analysis and evidence are useful for human decision-making.

Success does not mean that the OIL006 API has been modified.

Success means that AI Nexora has demonstrated a reliable
analysis → evidence → decision-boundary capability.

---

## 15. Constraints

The Vertical Slice must not:

- modify unrelated API behavior,
- weaken validation merely to make a failed request pass,
- change business rules without evidence and approval,
- change API contracts by assumption,
- modify database schema,
- expand scope without human approval,
- perform production actions,
- automatically commit code.

All implementation decisions remain subject to the human decision boundary.

---

## 16. Evidence Required for Completion

Before declaring the Vertical Slice DONE,
the system must provide evidence for:

1. Input materials were processed.
2. Findings were generated.
3. Findings contain supporting evidence.
4. Findings were correctly classified.
5. Human decision requirements were identified.
6. Unauthorized implementation was not performed.
7. Ball can review the output and understand what decision is required.

The final completion status must therefore be:

```text
DONE
only when sufficient evidence exists.
```

Otherwise:

```text
NOT DONE
```

---

## 17. Current Status

Current status:

```text
Vertical Slice v0.1
    ↓
Design Defined
    ↓
Implementation Specification Defined
    ↓
OIL006 Validation Case Defined
    ↓
Human Decision Boundary Defined
    ↓
Ready for Execution
```

The next step is to implement the smallest executable version
of the Orchestrator + Analyst flow.

No Developer, QA, or Reviewer automation will be added
until this Vertical Slice produces useful evidence
and demonstrates the human decision boundary successfully.

---

## 18. Next Step

Implement the smallest executable Vertical Slice:

```text
Input
  ↓
Orchestrator
  ↓
Analyst
  ↓
Analysis Package
  ↓
Evidence
  ↓
Decision Gate
  ↓
Ball
```

The implementation should be minimal,
observable,
testable,
and easy to replace or extend later.

The goal is not to build the whole platform.

The goal is to prove the core behavior first.

---

# Thai Summary

## เป้าหมาย

Vertical Slice v0.1 มีไว้พิสูจน์ว่า AI Nexora สามารถวิเคราะห์ปัญหาจริง
โดยใช้ Evidence และรู้ว่าเมื่อใดควรดำเนินการต่อ
และเมื่อใดต้องหยุดเพื่อให้ Ball ตัดสินใจ

## หลักการ

```text
AI วิเคราะห์
AI แสดง Evidence
AI ระบุ Conflict
AI แนะนำทางเลือก
มนุษย์ตัดสินใจ
```

และ:

```text
No Evidence
    ↓
No DONE
```

## สิ่งที่ Vertical Slice ต้องพิสูจน์

1. วิเคราะห์ปัญหาจริงได้
2. แยก Data Problem / Code Problem ได้
3. ตรวจพบ Contract Conflict ได้
4. ระบุ Unknown ได้
5. แสดง Evidence ที่ตรวจสอบได้
6. รู้ว่าเมื่อใดต้องถาม Ball
7. ไม่เปลี่ยน Code โดยไม่ได้รับอนุมัติ
8. ให้ข้อมูลที่เพียงพอสำหรับ Ball ในการตัดสินใจ

## สิ่งที่ยังไม่ทำ

- Autonomous Developer
- Autonomous QA
- Autonomous Reviewer
- Automatic Git Commit
- Production Action
- SaaS
- Web UI
- Large Infrastructure
- Autonomous Learning

## สถานะ

```text
DESIGN
  ↓
VERTICAL SLICE SPEC
  ↓
READY FOR EXECUTION
```

Next Step:

```text
Build minimal executable Orchestrator + Analyst
```
