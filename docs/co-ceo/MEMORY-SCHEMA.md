\# AI Nexora — Co-CEO Memory Schema v0.1



> Memory Architecture for Ball + AI Co-CEO

> สถาปัตยกรรม Memory สำหรับการทำงานร่วมกันระหว่าง Ball และ AI Co-CEO



\---



\## 1. Purpose



This document defines the standard schema for persistent memory used by the AI Nexora Co-CEO operating model.



เอกสารนี้กำหนดมาตรฐานสำหรับ Persistent Memory ที่ใช้ในระบบการทำงานระหว่าง Ball และ AI Co-CEO



The purpose is to ensure that important knowledge can survive across:



\- conversations

\- projects

\- AI model changes

\- long periods of time

\- new team members

\- future AI Nexora versions



หลักการสำคัญ:



> \*\*Conversation is temporary. Project Memory is persistent.\*\*



บทสนทนาเป็นพื้นที่ทำงานชั่วคราว แต่ Project Memory เป็นแหล่งข้อมูลระยะยาว



\---



\# 2. Memory Principles



\## 2.1 Curated Memory



Not everything discussed in a conversation should become persistent memory.



ไม่ใช่ทุกข้อความในบทสนทนาจะต้องถูกบันทึกเป็น Memory



Only information with long-term value should be persisted.



ข้อมูลที่ควรถูกบันทึก ได้แก่:



\- Identity

\- Vision

\- Goals

\- Decisions

\- Strategy

\- Rules

\- Risks

\- Lessons Learned

\- Important project history



\---



\## 2.2 Source of Truth



Persistent Memory should be treated as the long-term source of truth for the Co-CEO operating model.



เมื่อมีข้อมูลขัดแย้งกัน:



1\. ตรวจสอบ Decision Record ก่อน

2\. ตรวจสอบ Goals และ Strategy

3\. ตรวจสอบ Project Rules

4\. หากยังไม่ชัดเจน ให้ถาม Ball



AI Co-CEO must not silently invent or assume a decision.



AI Co-CEO ห้ามสร้างข้อสรุปขึ้นเองเมื่อข้อมูลสำคัญยังไม่ชัดเจน



\---



\## 2.3 Human Authority



Ball remains the final decision maker.



AI Co-CEO may:



\- analyze

\- challenge

\- recommend

\- identify risks

\- propose alternatives



แต่ AI Co-CEO ไม่มีอำนาจแทน Ball ในการตัดสินใจเชิงกลยุทธ์หรือการตัดสินใจที่มีความเสี่ยงสูง



\---



\# 3. Memory Categories



The initial memory system contains the following categories.



```text

IDENTITY

VISION

GOALS

DECISIONS

STRATEGY

RISKS

LESSONS

HISTORY

```



\---



\# 4. IDENTITY



File:



```text

IDENTITY.md

```



Purpose:



Define who we are, our roles, responsibilities, and operating relationship.



ใช้สำหรับกำหนด:



\- Ball คือใครในระบบ

\- AI Co-CEO คืออะไร

\- AI Nexora คืออะไร

\- ใครมีอำนาจตัดสินใจ

\- ใครมีหน้าที่อะไร



\### Required Information



```text

Identity ID

Name

Role

Responsibilities

Decision Authority

Operating Relationship

```



\### Example



```text

ID: ID-0001



Name: Ball

Role: CEO / Final Decision Maker



Responsibilities:

\- Make final business decisions

\- Approve high-risk actions

\- Define strategic direction



Decision Authority:

\- Final decision

```



\---



\# 5. VISION



File:



```text

VISION.md

```



Purpose:



Define the long-term direction of AI Nexora and the Ball + AI Co-CEO relationship.



ใช้สำหรับตอบคำถาม:



> เรากำลังสร้างอะไร และสร้างไปเพื่ออะไร?



\### Required Information



```text

Vision ID

Vision Statement

Long-Term Direction

Business Direction

Technology Direction

Principles

```



Vision should change rarely.



Vision ไม่ควรถูกแก้บ่อย เพราะเป็นทิศทางระยะยาว



\---



\# 6. GOALS



File:



```text

GOALS.md

```



Purpose:



Track current objectives and priorities.



Goals may change more frequently than Vision.



\### Goal ID



Every goal must have a unique identifier.



Format:



```text

GOAL-YYYY-###

```



Example:



```text

GOAL-2026-001

```



\### Goal Schema



```text

Goal ID

Title

Description

Priority

Status

Owner

Start Date

Target Date

Success Criteria

Related Decisions

Notes

```



\### Status



Allowed values:



```text

PROPOSED

ACTIVE

ON-HOLD

COMPLETED

CANCELLED

```



\### Example



```text

GOAL-2026-001



Title:

Build AI Nexora Framework v0.1



Priority:

HIGH



Status:

ACTIVE



Owner:

Ball



Success Criteria:

A working AI workforce can inspect an existing API,

compare it against an API specification,

implement required fixes,

run verification,

and provide evidence of completion.

```



\---



\# 7. DECISIONS



File:



```text

DECISIONS.md

```



Purpose:



Record important decisions made by Ball.



This is one of the most important memory categories.



\### Decision ID



Format:



```text

DEC-YYYY-###

```



Example:



```text

DEC-2026-001

```



\### Decision Schema



Every important decision should contain:



```text

Decision ID

Date

Title

Context

Problem

Options Considered

AI Co-CEO Recommendation

Ball Decision

Reason

Impact

Status

Related Goals

Related Projects

Review Date

```



\### Example



```text

DEC-2026-001



Date:

2026-10-04



Title:

Create AI Nexora as the AI Workforce Execution Platform



Context:

Ball wants to build a reusable AI workforce system

for software engineering and future business operations.



Problem:

AI coding assistants often require continuous human direction

and may make changes outside the intended scope.



Options Considered:

1\. Use existing AI coding assistants only

2\. Build a reusable AI workforce framework

3\. Build a SaaS product immediately



AI Co-CEO Recommendation:

Build the reusable framework first and validate it

with a real project before building SaaS.



Ball Decision:

Build AI Nexora Framework v0.1 first.



Reason:

Validate the core architecture before investing in SaaS.



Impact:

AI Nexora becomes the execution layer for future AI workforce operations.



Status:

ACTIVE



Related Goals:

GOAL-2026-001

```



\### Decision Rule



Once a decision is recorded, AI Co-CEO should not repeatedly reopen the same decision unless:



\- new evidence appears

\- assumptions have changed

\- the decision produces unexpected results

\- Ball asks to reconsider it



\---



\# 8. STRATEGY



File:



```text

STRATEGY.md

```



Purpose:



Record strategic approaches used to achieve goals.



Strategy answers:



> How are we going to win?



Strategy may contain:



```text

Strategic Objective

Approach

Why

Alternatives

Trade-offs

Expected Outcome

Metrics

```



Strategy is different from a Decision.



A Decision says:



> "We chose this."



A Strategy says:



> "This is how we intend to achieve it."



\---



\# 9. RISKS



File:



```text

RISKS.md

```



Purpose:



Track risks that may affect projects, business, technology, or strategy.



\### Risk ID



Format:



```text

RISK-YYYY-###

```



\### Risk Schema



```text

Risk ID

Title

Description

Category

Probability

Impact

Risk Level

Mitigation

Owner

Status

Trigger

Related Decisions

```



\### Risk Levels



```text

LOW

MEDIUM

HIGH

CRITICAL

```



\### Risk Status



```text

OPEN

MITIGATING

ACCEPTED

CLOSED

```



\### Example



```text

RISK-2026-001



Title:

AI makes changes outside approved scope



Category:

Engineering



Probability:

MEDIUM



Impact:

HIGH



Risk Level:

HIGH



Mitigation:

\- Define explicit scope

\- Use Architect impact analysis

\- Require Git diff verification

\- Require Reviewer approval

\- Prevent unrelated refactoring



Status:

OPEN

```



\---



\# 10. LESSONS



File:



```text

LESSONS.md

```



Purpose:



Record lessons learned from actual work.



Lessons should answer:



> What did we learn that should change how we work in the future?



\### Lesson ID



Format:



```text

LESSON-YYYY-###

```



\### Lesson Schema



```text

Lesson ID

Date

Title

Context

What Happened

Root Cause

Lesson

Action

Future Rule

Related Project

```



\### Example



```text

LESSON-2026-001



Title:

AI should not modify code before understanding API scope



Context:

API compliance workflow



What Happened:

An implementation change was attempted before

the full API specification and existing implementation

were analyzed.



Root Cause:

Implementation started before requirement analysis.



Lesson:

Requirement analysis must happen before implementation.



Future Rule:

No code modification before Analyst and Architect stages

are completed and the implementation scope is defined.

```



\---



\# 11. HISTORY



Directory:



```text

history/

```



Initial file:



```text

BUILD-DIARY.md

```



Purpose:



Record the evolution of AI Nexora.



The Build Diary is different from Memory.



Memory answers:



> What do we need to remember?



Build Diary answers:



> What happened while we built this?



Each entry should contain:



```text

Date

Step

What Was Built

Why

How

Result

What Was Learned

Next Step

```



Example:



```text

\## 2026-10-04 — STEP 0.2



\### What Was Built

Defined the Co-CEO Memory Schema.



\### Why

To establish a persistent memory architecture

before creating individual memory files.



\### How

Defined schemas for:

\- Identity

\- Vision

\- Goals

\- Decisions

\- Strategy

\- Risks

\- Lessons

\- History



\### Result

Memory structure v0.1 defined.



\### What Was Learned

Persistent memory must be curated rather than

storing every conversation.



\### Next Step

Create the initial Co-CEO memory files.

```



\---



\# 12. Memory Priority



Not all memory has the same priority.



Priority order:



```text

1\. DECISIONS

2\. GOALS

3\. VISION

4\. RULES / CONSTRAINTS

5\. RISKS

6\. STRATEGY

7\. LESSONS

8\. HISTORY

```



When context is limited, higher-priority memory should be loaded first.



\---



\# 13. Memory Lifecycle



Memory follows this lifecycle:



```text

DISCUSS

&#x20;  ↓

ANALYZE

&#x20;  ↓

DECIDE

&#x20;  ↓

RECORD

&#x20;  ↓

EXECUTE

&#x20;  ↓

OBSERVE RESULT

&#x20;  ↓

LEARN

&#x20;  ↓

UPDATE MEMORY

```



A conversation should not automatically become permanent memory.



\---



\# 14. Memory Update Rules



AI Co-CEO should consider creating or updating persistent memory when:



\- Ball makes an important decision

\- A strategic direction changes

\- A goal is created or completed

\- A new operating rule is established

\- A significant risk is discovered

\- A reusable lesson is learned

\- A major project milestone occurs



AI Co-CEO should NOT persist:



\- casual conversation

\- temporary thoughts

\- redundant information

\- information with no future value

\- speculative ideas that have not been adopted

\- temporary debugging details unless they become a reusable lesson



\---



\# 15. Conflict Resolution



When two memory records appear to conflict:



```text

1\. Check the newest Decision

2\. Check current Goals

3\. Check current Strategy

4\. Check Project Rules

5\. Ask Ball if ambiguity remains

```



AI Co-CEO must not silently overwrite a previous decision.



If a decision changes, create a new decision record or update the decision history explicitly.



\---



\# 16. Human Decision Boundary



The following should normally require Ball's decision:



\- Major strategic changes

\- New business direction

\- High-risk production actions

\- Security-sensitive actions

\- Financial commitments

\- Significant architecture changes

\- Scope expansion

\- Cancellation of major goals

\- Decisions with unclear or conflicting requirements



AI Co-CEO may recommend but does not own the final decision.



\---



\# 17. AI Co-CEO Memory Behavior



When starting a new conversation, AI Co-CEO should attempt to establish:



```text

Who are we?

What are we building?

What are our current goals?

What important decisions have already been made?

What risks are currently open?

What lessons have we learned?

What is happening now?

```



The AI Co-CEO should use persistent memory to maintain continuity rather than assuming that the previous conversation is still available.



\---



\# 18. Memory Architecture



Initial architecture:



```text

docs/

└── co-ceo/

&#x20;   ├── OPERATING-MODEL.md

&#x20;   ├── MEMORY-SCHEMA.md

&#x20;   │

&#x20;   ├── memory/

&#x20;   │   ├── IDENTITY.md

&#x20;   │   ├── VISION.md

&#x20;   │   ├── GOALS.md

&#x20;   │   ├── DECISIONS.md

&#x20;   │   ├── STRATEGY.md

&#x20;   │   ├── RISKS.md

&#x20;   │   └── LESSONS.md

&#x20;   │

&#x20;   └── history/

&#x20;       └── BUILD-DIARY.md

```



\---



\# 19. Core Principle



The purpose of memory is not to remember everything.



The purpose of memory is to preserve the information required to make better decisions over time.



> \*\*Remember what matters.\*\*

>

> \*\*Forget what does not.\*\*

>

> \*\*Record decisions.\*\*

>

> \*\*Learn from results.\*\*

>

> \*\*Keep Ball in control.\*\*



\---



\## Version



```text

Version: 0.1

Status: Initial Draft

Owner: Ball

Strategic Partner: AI Co-CEO

Execution Platform: AI Nexora

```
