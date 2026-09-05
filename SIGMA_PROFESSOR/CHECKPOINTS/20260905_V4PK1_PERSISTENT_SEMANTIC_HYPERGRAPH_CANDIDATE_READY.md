# V4-PK1 PERSISTENT SEMANTIC HYPERGRAPH — CANDIDATE + PREFLIGHT READY

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

## Status

```text
LEVEL=1
PROGRAM=V4_PERSISTENT_KNOWLEDGE
STAGE=V4-PK1
CAPABILITY=PERSISTENT_SEMANTIC_HYPERGRAPH_SUBSTRATE
SOURCE_CANDIDATE_READY=YES
PREFLIGHT_RUNNER_READY=YES
LOCKED_SIGMAC_COMPILE=NOT_RUN
LOCKED_VM_RUNTIME=NOT_RUN
ADMISSION=NOT_RUN
PRODUCTION_BINDING=NO
```

This checkpoint is source/runner readiness only. It is not runtime capability evidence.

## Governing toolchain directive

Path:
`SIGMA_PROFESSOR/DIRECTIVES/SIGMA_LEVEL1_V4_PERSISTENT_KNOWLEDGE_TOOLCHAIN_V1.md`

Creation commit:
`88b29b08ca230147dbf1b9830d6fa52d5a03aa0e`

Required order:

```text
V4-PK1 Persistent Semantic Hypergraph
-> V4-PK2 Weight / Evidence
-> V4-PK3 Multi-hop Reasoning
-> V4-PK4 Controlled Inference
-> V4-PK5 Cognitive VM Bridge
-> V4-PK6 Verified Evolution
```

V5 external acquisition remains gated behind sufficient Level 1 admission.

## Native source candidate

Path:
`SIGMA_PROFESSOR/artifacts/SIGMA_V4_PERSISTENT_SEMANTIC_HYPERGRAPH_V4PK1.sigma`

Creation commit:
`defea6639e58dc5b2a5e9ed0431a8d56a73bd8c5`

Canonical repository Git blob:
`02246026c041c140cf3410590693795205031c65`

Source SHA256:
`NOT_YET_CANONICALLY_OBSERVED_ON_TERMUX`

Target native behavior:

- bounded 2..4-member hyperedge representation;
- opaque relation/member runtime tokens;
- evidence identity and provenance identity retained on each hyperedge;
- integer basis-point weight and uncertainty fields with native syntax/range validation;
- immutable edge identity in the tested state namespace;
- exact-edge replay idempotency;
- conflicting reuse of an edge ID refused;
- persistent store validation before mutation;
- native write/readback equality check;
- persistent prior state affects a later fresh-VM invocation;
- native incident-edge and incident-weight aggregation for the input anchor;
- bounded maximum of 64 retained hyperedges in this candidate.

Claim boundary:

```text
SEMANTIC_UNDERSTANDING=NOT_PROVEN
MULTI_HOP_REASONING=NOT_EXECUTED
CONTROLLED_INFERENCE=NOT_EXECUTED
CRASH_CONSISTENT_HYPERGRAPH_WRITE=NOT_PROVEN
GENERAL_KNOWLEDGE_PROMOTION=NOT_PROVEN
```

The word `Semantic` denotes the intended representation layer. Relation labels remain opaque tokens in V4-PK1; label storage alone is not evidence of semantic understanding.

## Mechanical admission runner

Path:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V4PK1_PERSISTENT_SEMANTIC_HYPERGRAPH_PREFLIGHT.sh`

Creation commit:
`f908dc5bcebb36c94caa9812c0163acbb518a690`

Canonical repository Git blob:
`b6e12e8fa6f48e8417766054e5409a58a3c5a922`

Runner SHA256:
`NOT_YET_CANONICALLY_OBSERVED_ON_TERMUX`

The runner gates the locked compiler/VM identities, gates the source by canonical Git blob, prints the source SHA256 observed on Termux, compiles once, runs fresh VM processes against shadow state, and leaves production V2.4 untouched.

## Planned dynamic/negative runtime cases

The runner is designed to exercise:

1. valid 3-ary hyperedge commit;
2. exact replay in a fresh VM with no duplicate mutation;
3. same edge ID with changed fingerprint refused;
4. second valid 2-ary hyperedge using persisted prior state;
5. one-member invalid shape refused;
6. duplicate hyperedge member refused;
7. weight above 10000 basis points refused;
8. uncertainty above 10000 basis points refused;
9. unsafe field separator token refused;
10. host-injected malformed persistent-store record refused without further mutation;
11. source/bytecode immutability check;
12. bounded step-limit transcript check;
13. production V2.4 PID unchanged when it was running before the test.

Fixture values are fixed test inputs only. The host does not generate graph policy, choose hyperedges for SIGMA, score evidence, infer relations, promote knowledge or make semantic decisions.

## Host-substitution boundary

```text
HOST_HYPEREDGE_ADMISSION_DECISION=NO
HOST_WEIGHT_DECISION=NO
HOST_EVIDENCE_DECISION=NO
HOST_SEMANTIC_INTERPRETATION=NO
HOST_LEARNING=NO
HOST_POST_VM_TEST_ORACLE_ONLY=YES
PYTHON_USED=NO
```

Shell responsibilities are limited to identity gates, shadow fixture setup, exact-byte fault injection, locked compiler/VM invocation, hashing and post-VM assertions.

## Locked runtime expected by runner

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

## Admission rule

Do not unlock V4-PK2 as an admitted dependency merely because these files exist.

Required next evidence:

```text
CANONICAL REPO SOURCE
-> TERMUX SOURCE SHA256 OBSERVATION
-> LOCKED SIGMAC COMPILE
-> LOCKED VM DYNAMIC/NEGATIVE RUN
-> RESTART/PERSISTENCE CHARACTERIZATION
-> HOST SUBSTITUTION AUDIT
-> BOUNDEDNESS CHECK
-> CLAIM-SCOPE REVIEW
-> PASS OR FAIL
```

Until a runtime transcript is observed:

```text
PERSISTENT_SEMANTIC_HYPERGRAPH=NOT_PROVEN
V4_PK1_ADMISSION=NOT_RUN
V4_PK2_ADMISSION_UNLOCKED=NO
```
