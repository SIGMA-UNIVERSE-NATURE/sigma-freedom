# SIGMA Language Understanding Core R1 — Design Direction

Date: 2026-10-02
Type: architecture / coordination contract
Source: user-supplied direction.

## Claim boundary

Small capsule PASS results are scaffold/component proofs only.

They are NOT sufficient evidence that SIGMA understands natural language.

Do not claim real language understanding until SIGMA passes semantic-frame, contradiction, grounding, and action tests on unseen sentences, including meaning-reversal negative controls.

## Big method

### Surface Language
Read natural human sentences and diverse paraphrases.

### Semantic Frame
Extract:
- intent;
- object;
- constraints;
- risk;
- requested action.

### Logic Graph
Represent semantic relations such as:
- requires;
- forbids;
- contradicts;
- allows.

### Contradiction Engine
Detect:
- false statements;
- reversed meaning;
- contradictory constraints;
- overclaims.

### Grounding Gate
Bind meaning to real evidence:
- receipts;
- hashes;
- tests;
- provenance.

Unproven claims must fail closed.

### Action Policy
Classify resulting action, including:
- read-only;
- candidate-only;
- blocked;
- owner-review.

### Memory Compression
Persist minimal rules/actions rather than raw-log memorization.

### Curriculum Engine
Select the next demonstrated knowledge/semantic gap to learn.

### Native Exam
Generate new tests and negative controls.

### Promotion Gate
Promote only when old, new, and adversarial tests pass.

## Target core pipeline

human sentence
-> semantic frame
-> logic graph
-> contradiction check
-> grounding
-> grounded action
-> fail closed if unproven

## Initial unseen-style test examples

- "Đừng vì OPPO yếu mà bỏ học"
- "Candidate pass không có nghĩa được bind"
- "Không được fake hiểu nếu chưa có evidence"
- "Muốn tự học thì phải tự tạo test chống tự lừa"

Required:
- convert each to the correct semantic frame;
- derive the correct logical/action constraints;
- reject meaning-reversed or contradictory variants;
- do not answer from hardcoded phrase mappings.

## Architectural ownership

No host learning policy.
No phrase-to-answer hardcoding.
No raw-log memorization as intelligence.
No grounding component answering on behalf of the model.
No admission claim from component-level PASS.

ONE_SIGMA=YES

## Proposed next stage

SIGMA_LANGUAGE_UNDERSTANDING_CORE_R1

Goal:
build a reusable semantic representation and grounded-action pipeline rather than accumulating isolated capsules.

## Evidence required before stronger claim

At minimum:
- unseen paraphrase generalization;
- semantic-frame correctness;
- contradiction/reversal rejection;
- evidence-grounding correctness;
- action-policy correctness;
- adversarial negative controls;
- fresh-process deterministic evaluation;
- no host semantic selection;
- no hardcoded case-to-answer mapping.

Only after those gates may the system claim progress toward robust language understanding.

This document is a design direction, not a PASS checkpoint and not an admission/cutover authority.
