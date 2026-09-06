# DIRECTOR-B1.1-INTEGRATION-AUDIT — Execution Window

## Window state

`ACTIVE`

Execution branch:

`hka-tree/director-b1-1-integration-audit`

Control-plane branch:

`hka-tree/curriculum-master`

Activation base:

`b7eaae3ed59aa4c9ea8f65580895735252523746`

## Scope

Audit the effective B1.1 curriculum formed by the Director-accepted C01-C10 authoring chain plus every effective foundational overlay and supersession record at `FOUNDATIONAL_GAP_COUNT = 0`.

The execution window must independently verify stable IDs, semantic closure, ownership/duplicate integrity, prerequisites, locked-scope isolation, zero-gap preservation, scope-map alignment, stage boundary, and accepted-history integrity.

## Locked controls

- Canonical Knowledge Tree: `fc799bf1104ab6352710e1801777a971b5179995`
- B1 architecture: `265bb584b5d7e36e11091289d58558408880118c`
- Immutable B1 scope-map blob: `bedef47958a728e3f0d56d412f7bdea3ec465856`
- Stage: `CURRICULUM`
- B1.2: `LOCKED_PENDING_B1_1_INTEGRATION_AND_SENTINEL`
- `ACADEMIC_LOCKED`: false / gated
- Later pipeline stages: gated
- C10 worker submission state remains `PARTIAL_NOT_PASS_CANDIDATE`

## Terminal rule

The strongest allowed integration result is:

`DIRECTOR_INTEGRATION_PASS_PENDING_FRESH_SENTINEL`

That result does not unlock B1.2. The mandatory next gate is a fresh `DIRECTOR-BACKUP-S01 TREE_ALIGNMENT_PASS` against the post-integration durable state.

## Execution policy

Small certain defects may be repaired at their true owner with append-only or explicit supersession semantics. Any repair that can alter foundational coverage requires revalidation of the affected foundational requirement before retaining `FOUNDATIONAL_GAP_COUNT = 0`.
