# SIGMA C5 M5 — Current Status

Updated: 2026-09-09 (Asia/Ho_Chi_Minh)

## Production boundary

- Production binding: NO
- Production C5V3 observed PID: `23663`
- Production core SHA256: `23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc`
- Production runner SHA256: `092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847`
- Locked sigmac SHA256: `65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- Locked VM SHA256: `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

## Latest admitted capability

`M5_NATIVE_GAP_EVIDENCE_REQUEST_R1`

Core SHA256: `1ff2dc93dc41f63e070a548d582d56911c406538eeacac826a0b9c419a4ce1eb`

Retained admitted dependencies:

1. `M5_CLEANLINE_R1` — neutral evidence/provenance persistence, replay, restart, bounded 64-record ledger.
2. `M5_NATIVE_PROVENANCE_GAP_R1` — native structural provenance-diversity gap.
3. `M5_NATIVE_EXACT_EVIDENCE_COHORT_R1` — exact-byte evidence identity/cohorting.
4. `M5_NATIVE_SCOPED_PROVENANCE_GAP_R1` — target-scoped provenance gap.
5. `M5_NATIVE_CONTEXT_STRUCTURE_R1` — native structural context hypothesis; blind contextual-transfer `100/100` only in that exact structural scope.
6. `M5_NATIVE_RELATION_DISCRIMINATION_GAP_R1` — shared context plus differing configuration opens/revises a native discrimination gap instead of asserting equivalence.
7. `M5_NATIVE_GAP_EVIDENCE_REQUEST_R1` — open native gap produces native evidence request; no gap means no request; request persists/restarts and is revoked by discriminating evidence.

## Retained blind truth

- Wide blind after scoped-gap repair: `75/100`.
- Natural-language paraphrase blind R1: `60/100`; role reversal FAIL.
- Natural-language paraphrase blind R2: `75/100`; role reversal PASS, benign untrained reorder FAIL, zero-shot low-overlap FAIL.
- Learned-transform causality blind: `75/100`; `SPURIOUS_TRANSFORM_FALSE_INDUCTION_RESISTANCE=FAIL`.
- Context-grounded causality blind: `65/100`; `GROUNDED_ROLE_REVERSAL_FALSE_EQUIVALENCE_RESISTANCE=FAIL`.

Retired assumptions:

- recurring permutation shape => relation-preserving transformation;
- shared co-document context => same relation;
- unordered sentence-coverage matching.

## Current hard FAIL capabilities

- `SEMANTIC_PARAPHRASE=FAIL`
- `ZERO_SHOT_LOW_OVERLAP_PARAPHRASE=FAIL`
- `BENIGN_UNGROUNDED_REORDER=FAIL`
- `AUTONOMOUS_RESEARCH=FAIL`
- `REAL_INTERNET_ACQUISITION=FAIL`
- `TOOL_EXECUTION=FAIL`
- semantic support/conflict/truth judgment: FAIL.

## Mechanical evidence-tool transport — current state

Parent candidate core and transport remain unchanged through R1/R1H1/R1H2:

- Core SHA256: `f530a556a670137f865b3f67b52557f3ccd9ec0b97f536f5c2123ce4276117e5`
- Transport SHA256: `0ed437aa2188b2382aec88c390697f7f912dff0ac27b9f50cc15b5936e713ffd`

R1 runtime passed request gating/correlation/verbatim transport, irrelevant-evidence handling, cross-gap isolation, persistence and restart, then stopped at `FAIL=DISCRIMINATING_REQUEST_NOT_VERBATIM`, `RC=72`. Root cause was a harness live-file alias: the oracle compared provider capture to a native request file that SIGMA had legitimately revoked after discriminating evidence. No core/transport defect established.

R1H1 fixed that oracle with an immutable request snapshot. Oppo runtime then additionally passed:

- `RAW_EVIDENCE_NATIVE_REVISION=PASS`
- `NATIVE_REQUEST_REVOKE_STOPS_TOOL=PASS`

R1H1 stopped at `FAIL=BOUND_LEDGER_NOT_64`, `RC=83` before the 65th-tool-result gate. Root cause is another harness counting bug: `open_gap` successfully ingests 4 records and the filler loop successfully ingests 60 more, but the oracle used `wc -l`. The canonical ledger has no trailing newline, so 64 records contain 63 newline characters. Native core count semantics are record-based (`str_split`) and the 64 accepted ingests establish 64 records; R1H1 did not demonstrate a core boundedness failure.

Current pending harness correction: `M5_MECHANICAL_EVIDENCE_TOOL_TRANSPORT_R1H2`

- Core SHA256 unchanged: `f530a556a670137f865b3f67b52557f3ccd9ec0b97f536f5c2123ce4276117e5`
- Transport SHA256 unchanged: `0ed437aa2188b2382aec88c390697f7f912dff0ac27b9f50cc15b5936e713ffd`
- Preflight SHA256: `769b2caffd0791faf4b81ce1bc72f4cf3898dcf7d60266d0473a51a68f0e5617`
- Bundle SHA256: `df950ba9f07762d816f4eb7b399fb3f2b215d839fa10028f1f1e6c0e4c0bcf27`
- Harness change only: replace newline count (`wc -l`) with record count (`awk NR`) for the two boundedness post-hoc assertions.
- Native 65th-record rejection requirement remains unchanged.
- Admission criteria weakened: NO.
- Oppo locked runtime admission: pending.

## Anti-hardcode state

Current admitted lineage repeatedly passes gates for token LEFT/RIGHT cognition absent, active Python cognition absent, host learning absent, host semantic substitution absent, no fixed English grammar/semantic-role tables in active candidate capability code, and dynamic fixtures generated after compile/freeze where applicable.

## Exact next dependency

Run `M5_MECHANICAL_EVIDENCE_TOOL_TRANSPORT_R1H2` on Oppo. Do not promote mechanical tool invocation until the corrected harness reaches final admission PASS. If it passes, promote only `MECHANICAL_TOOL_INVOCATION=PASS`; keep real Internet acquisition, autonomous research, semantic paraphrase, and truth/support/conflict capabilities FAIL until separate blind/admission tests.