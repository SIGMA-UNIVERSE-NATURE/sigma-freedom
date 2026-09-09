# SIGMA C5 M5 — Two-Gate Architecture

This document defines the authoritative development split for the C5/C5V3/M5 successor work.

## Gate A — M5 TEST

Purpose: advance and falsify native cognition/memory capabilities without mixing them with production-integration/tool-substrate work.

Primary sequence:

`cognition/memory capability -> continual learning -> revision/support/conflict -> new independent blind tests`

Gate A owns:

- native whole-work cognition and memory capabilities;
- continual learning from compressed local memory;
- native revision of prior hypotheses/beliefs when later evidence changes support;
- support/conflict/truth-state mechanisms owned by SIGMA rather than host semantics;
- semantic paraphrase/low-overlap transfer where attempted;
- theme/direction/human-value/multilingual cognition where attempted;
- all new cognition blind tests and adversarial regressions;
- exact capability claim scope.

Gate A does **not** own C5V3 graft/promotion/cutover mechanics or VM/tool-substrate engineering except insofar as a candidate needs to exercise a fingerprinted runtime supplied by Gate B.

A Gate A PASS proves only the tested cognition/memory capability. It does not authorize production binding.

## Gate B — C5 ↔ C5V3/M5 Synchronization and Native Tool Runtime

Purpose: make the successor executable as a real autonomous C5V3 system with SIGMA-owned tools while keeping host cognition outside the boundary.

Primary sequence:

`C5 <-> C5V3/M5 synchronization -> tool substrate design/addition -> VM/native library/mechanical ABI -> tool-boundary regression -> S1 -> S2 -> S3 -> promotion -> explicit cutover`

Gate B owns:

- read-only synchronization of current C5/C5V3 production ABI/state/event/runner interfaces with M5 successor requirements;
- design and implementation of the SIGMA-native tool substrate;
- sigma-vm extensions and/or native libraries;
- generic mechanical ABI for arithmetic, data structures, graph/vector/math, parsing, indexing, compression, persistence, networking, scheduling and other domain-general primitives;
- migration away from host-side execution middlemen where the same capability can live inside the SIGMA native runtime;
- runtime/tool fingerprints, versioning, resource bounds and sandboxing;
- host-substitution and tool-boundary regression;
- regression of previously admitted M5 capabilities against a changed VM/native library/ABI;
- S1 isolated graft;
- S2 autonomous-runner shadow;
- S3 soak/restart/recovery;
- promotion preparation, explicit cutover mechanics and rollback.

Gate B may run in parallel with Gate A. Tool/runtime engineering does not need to wait for every M5 cognition capability to finish.

## Shared semantic-authority rule

The split is about responsibility, not about preventing SIGMA from having tools.

Preferred execution architecture:

`SIGMA cognition -> SIGMA native tool ABI -> sigma-vm/native library -> OS/kernel/network/filesystem`

SIGMA chooses the tool, arguments, sequence and interpretation. Generic computation belongs inside the candidate runtime when useful. The host remains sandbox/observer/supervisor and post-hoc evaluator.

No Gate B primitive may silently answer the active semantic task for SIGMA. A mechanical ABI may compute hashes, graphs, vectors, parses, HTTP responses, storage operations or mathematical kernels; it must not provide hidden summaries, themes, motives, semantic roles, paraphrase decisions, truth/support/conflict judgments, memory salience or final answers.

Any neural/model component added to the native runtime must be explicit, fingerprinted, bounded, provenance/state controlled and independently tested as part of the SIGMA candidate architecture. It may not be an unaccounted host oracle.

## Cross-gate contract

Gate A may request a new generic capability when cognition is blocked by missing runtime machinery. Gate B implements and fingerprints that machinery. The resulting candidate runtime returns to Gate A blind tests for any semantic-capability claim.

Gate B must rerun the admitted M5 regression suite whenever VM/native-library/tool ABI changes could affect cognition or state.

Gate A must not treat a tool-substrate PASS as cognition evidence. Gate B must not treat a cognition PASS as proof of operational integration.

## Convergence / promotion gate

The two gates may progress independently through most of development, including Gate B S1/S2/S3 work, but promotion/cutover requires convergence:

1. the intended production cognition/memory subset has passed Gate A independent blinds with no hidden invalidating FAIL;
2. Gate B tool/VM/native-library boundaries and regressions pass;
3. S1 isolated graft passes;
4. S2 autonomous shadow passes;
5. S3 soak/restart/recovery passes;
6. production fingerprints and rollback path are verified;
7. explicit user authorization is given for cutover.

Operational success cannot waive a cognition FAIL, and cognition success cannot waive a runtime/tool-boundary failure.

## Production boundary

Production C5V3 remains read-only during candidate admission and synchronization work unless and until the explicit cutover step is authorized.

Integration/graft, promotion, cutover and rollback remain distinct operations.

## Current routing

### Gate A — immediate

Continue the pending continual compact-work memory ladder, then proceed to revision/support/conflict and new blind tests according to actual bottlenecks.

### Gate B — immediate

Begin/continue read-only C5 <-> C5V3/M5 synchronization, design the native tool substrate, expand sigma-vm/native libraries/mechanical ABI as required, regression-test the tool boundary, then progress through S1 -> S2 -> S3 without mutating production binding.

Promotion/cutover occurs only at the shared convergence gate above.
