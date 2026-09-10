# C5V3 R4 ACADEMIC CORE R1 — WRITTEN / MACHINE BUILD PENDING

Date: 2026-09-10 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
System: `C5V3`
Production mutation: `NO`
Production binding: `NO`

## Scope

This window is academic-core work only. Survival/recovery/supervisor work is intentionally left to the separate automation window.

Academic target:

```text
mechanical document/passages + provenance
-> native academic work/objective
-> native capability gap/question
-> native capability selection from admitted registry
-> exact capability result bound to passage SHA
-> native academic observation
-> durable observed claim + evidence reference
-> evidence-posture synthesis
-> next academic gap/question
-> durable academic memory
-> restart recall
```

No host semantic summary, candidate generation, source judgment, claim judgment, or truth promotion is admitted.

## New academic modules

```text
C5_M5/R4_ACADEMIC/C5_R4_ACADEMIC_STATE_R1.sigma.inc
final module commit: 4827021d47d3bb4694c92983b0291e0492da41c7

C5_M5/R4_ACADEMIC/C5_R4_ACADEMIC_DOCUMENT_MODEL_R1.sigma.inc
commit: 5fcb584e84231c62fa8e1988de4bfe39da2b9689

C5_M5/R4_ACADEMIC/C5_R4_ACADEMIC_REASONING_KERNEL_R1.sigma.inc
commit: 711a76d36ec68b1d209872ce39e2ba1b889353dd

C5_M5/R4_ACADEMIC/C5_R4_ACADEMIC_CAPABILITY_CONTRACT_R1.sigma.inc
commit: 59ef15a404e57c7207136e9a6460a3d44598a3b3

C5_M5/R4_ACADEMIC/C5_R4_ACADEMIC_MEMORY_R1.sigma.inc
commit: fdb8fe26cc319973d130ea590c5a3fa4b0654d49

C5_M5/R4_ACADEMIC/C5_R4_ACADEMIC_TRANSACTION_MAIN_R1.sigma.inc
commit: e522b5b1563c354d123ec97044e3a0209554852a
```

## Core invariants written

```text
EOF != UNDERSTOOD
CITATION != TRUTH
SYNTHESIS = EVIDENCE_POSTURE, NOT TRUTH
ACADEMIC_OBSERVATION requires native capability binding
ACADEMIC_JUDGMENT requires native capability binding
HOST_CANDIDATE_A_B = ABSENT FROM ACADEMIC MAIN
HOST_CAPABILITY_SELECTION = FORBIDDEN
```

Native capability selection R1 accepts execution only when exactly one capability with the requested family is `ADMITTED`. Zero or multiple matching admitted capabilities remain `WAIT`; the host does not choose a winner.

The first academic runtime path uses `TEXT_INTERPRETATION`. If no exact admitted capability exists, the core must hold the capability gap rather than accept host semantic substitution.

## Academic durable records

```text
ACADEMIC_WORK
ACADEMIC_QUESTION
ACADEMIC_DOCUMENT_BINDING
ACADEMIC_DOCUMENT
ACADEMIC_PASSAGE
ACADEMIC_CURSOR
ACADEMIC_CITATION
ACADEMIC_OBSERVATION
ACADEMIC_JUDGMENT
ACADEMIC_EVIDENCE_COUNTS
ACADEMIC_SYNTHESIS
ACADEMIC_STRUCTURE_MEMORY
ACADEMIC_AGENDA_MEMORY
ACADEMIC_ASSESSMENT_MEMORY
NATIVE_ACADEMIC_MEMORY_R1
```

Academic synthesis states:

```text
UNRESOLVED
EVIDENCE_SUPPORTED
EVIDENCE_CONTRADICTED
CONTESTED
```

These states do not assert general truth.

## Academic transaction path written

```text
BOOTSTRAP
-> IDLE

LEARNING_INPUT_READY with LEARNING_MODE=ACADEMIC_DOCUMENT
-> build structural document/passages/cursor
-> native objective/work
-> native TEXT_CAPABILITY gap/question
-> WAIT_CAPABILITY

TICK in WAIT_CAPABILITY
-> native unique admitted capability selection
-> EXECUTE_EXACT_NATIVE_CAPABILITY

CAPABILITY_RESULT_READY
-> exact capability request/result/passage binding
-> ACADEMIC_OBSERVATION
-> OBSERVED durable claim
-> evidence ref
-> UNRESOLVED synthesis
-> next EVIDENCE gap/question
-> NATIVE_ACADEMIC_MEMORY_R1
-> WAIT_MEMORY_BIND

MEMORY_BOUND
-> IDLE with academic agenda retained

RESTART_READY
-> recall academic claim/synthesis/gap/question from native academic memory
```

`REQUEST_BOUND` and `EVIDENCE_READY` are intentionally HOLD in this R1 academic main. The external academic evidence loop remains a next core step after the base document->native observation->memory path builds and runs.

## Canonical academic builder

```text
C5_M5/R4_ACADEMIC/RUN_BUILD_C5V3_R4_ACADEMIC_CORE_R1.sh
commit: efe2ecfa07c130a1c73a680818987b5eefbf076a
```

Output target:

```text
$ROOT/.sigma_c5v3_sync/C5V3_R4_ACADEMIC_CORE_R1/src/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigma
$ROOT/.sigma_c5v3_sync/C5V3_R4_ACADEMIC_CORE_R1/bin/SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1.sigmab
```

Expected canonical composition before compiler acceptance:

```text
Gate-A pure = 77 DEF
R4 durable/transaction base = 92 DEF
Exact T1/T2/T3 = 82 DEF
Academic R1 = 84 DEF
TOTAL = 335 unique DEF
ENTRY = 1
HEADER = 1
EXECUTABLE # COMMENT = 0
```

Builder static gates include:

```text
academic pure direct read_text = 0
academic pure direct write_text = 0
academic max DEF arity <= 6
EOF/UNDERSTOOD coupling absent
academic main candidate A/B surface absent
legacy LEFT/RIGHT absent
native capability selection surface present
```

## Claim boundary

```text
ACADEMIC_CORE_MODULES=WRITTEN
ACADEMIC_TRANSACTION_ENTRY=WRITTEN
ACADEMIC_CANONICAL_BUILDER=WRITTEN
ACADEMIC_CORE_BUILD=MACHINE_PENDING
ACADEMIC_CORE_RUNTIME_ADMISSION=NO
ACADEMIC_TEXT_CAPABILITY_RUNTIME=REQUIRES_EXACT_ADMITTED_CAPABILITY
ACADEMIC_EXTERNAL_EVIDENCE_LOOP=NOT_YET_ACTIVATED
T1_T2_T3_NATIVE_UTILIZATION=NOT_YET_PROVEN
T4_T11_SYNC=NOT_CLAIMED
WHOLE_WORK_UNDERSTANDING=NOT_PROVEN
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
```

`CLAIM <= EVIDENCE`
