# 2026-09-09 15:27 +07 — Epistemic Stress R1 and Source-Consistency R2

## Parent admitted capability retained

`M5_NATIVE_SCOPED_REVISION_SUPPORT_CONFLICT_R1`

- Core SHA256: `460461d6273145fcedcf20e2c75b97e718ff61a6afa8f71dc8d0812f739f850e`.
- Oppo bytecode: `e4a3e18029e93a4f97c4808fcda5518a89fa925d7c160471f83cb4635f28ee2a`.
- Original admission + blind remain PASS in their exact native two-candidate/provenance scope.
- `NATIVE_SCOPED_SUPPORT_CONFLICT_REVISION=PASS` remains historically valid.

## New independent epistemic stress

Target core unchanged: `460461d6273145fcedcf20e2c75b97e718ff61a6afa8f71dc8d0812f739f850e`.

Runtime results:

- `BLIND_BALANCED_EVIDENCE_REMAINS_UNFORMED=PASS`.
- `BLIND_SELF_CONTRADICTING_SOURCE_ALONE_DOES_NOT_FORM_HYPOTHESIS=PASS`.
- `BLIND_SELF_CONTRADICTING_SOURCE_EXCLUDED_FROM_DISTINCT_AUTHORITY=FAIL`.
- observed held after self-conflicting source X plus one clean B source: `B`.
- observed epistemic state: `SUPPORTED`.
- work-scope isolation regression PASS.
- protocol-injection regression PASS.
- `TOTAL_SCORE=65/100`.
- `SOURCE_CONSISTENCY_AWARE_DISTINCT_AUTHORITY=FAIL`.
- evaluator execution PASS, `RC=0`.
- production mutation NO.

Diagnosis: R1 counts distinct SOURCE_ID independently on candidate A and candidate B. A source that supplies evidence for both candidates can therefore contribute authority to both sides. This is a cognition defect exposed by a stronger blind, not a harness failure and not a retroactive invalidation of the narrower R1 claim.

## R2 prepared

Candidate: `M5_NATIVE_SOURCE_CONSISTENCY_AWARE_SCOPED_REVISION_R2`.

R2 native behavior:

- recompute per-source stance from the full revision ledger: `A`, `B`, `INCONSISTENT`, `NONE`;
- persist native source-consistency state;
- `INCONSISTENT` sources contribute authority to neither candidate;
- recompute authority retroactively after every evidence record;
- if a source that helped form a held hypothesis later becomes inconsistent and remaining consistent support drops below threshold, retract the held hypothesis;
- later clean independent sources can recover/form a hypothesis.

Frozen static hashes:

- Core SHA256: `82971fefa1e4b7c009612fc5be1ed88017386659f27c46b42117b603f4355736`.
- Admission evaluator SHA256: `337bb3d1852abf9a93f6dcc918b36f9cac960b4bf693c151c27284cb9011234a`.
- Independent blind evaluator SHA256: `ae8d0c7a024359c54a9d2014cdc5e764e3563e3e699f7b5f91eb1abe2ea4b8e8`.
- Ladder runner SHA256: `37985b838255e73ab54788ffa12c240e57a182d24fc648ce4bc09af0f819f9c0`.
- Ladder bundle SHA256: `2b928b54117bb694d2fabea9c26edfb82f0c85458c7d12b950f456f41483ad99`.

Static validation: candidate/blind target core byte-identical; shell syntax PASS; manifests PASS; ZIP integrity PASS; no production paths in core; forbidden LEFT/RIGHT/previous-next/grammar-role markers absent.

## Claim rule

R2 is pending runtime admission/blind. Even on PASS, only source-consistency-aware scoped support/conflict/revision may advance. `BROAD_SEMANTIC_SUPPORT_CONFLICT_TRUTH=FAIL` remains until separate learned-incompatibility/provisional-truth blinds pass.
