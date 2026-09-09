# SIGMA C5 M5 — Current Status

Updated: 2026-09-09 (Asia/Ho_Chi_Minh)

## Current production boundary

- Production binding: NO
- Production C5V3 observed PID during latest admission: `23663`
- Production core SHA256: `23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc`
- Production runner SHA256: `092c6ad96823ba578ba5a8e22fe5f9d45a80c9ae4cc380b7296a5da3ec6a8847`
- Locked sigmac SHA256: `65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- Locked VM SHA256: `029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

## Admitted M5 lineage retained as valid dependencies

1. `M5_CLEANLINE_R1`
   - Native neutral evidence/provenance persistence.
   - Dynamic unseen input, idempotent replay, explicit-boundary persistence, restart recall, bounded 64-record ledger.

2. `M5_NATIVE_PROVENANCE_GAP_R1`
   - Native structural provenance-diversity gap over the ledger.

3. `M5_NATIVE_EXACT_EVIDENCE_COHORT_R1`
   - Native exact-byte evidence identity/cohorting.

4. `M5_NATIVE_SCOPED_PROVENANCE_GAP_R1`
   - Gap scoped to the exact target-evidence cohort.
   - Fixed the earlier blind failure where unrelated evidence could close the wrong gap.

5. `M5_NATIVE_CONTEXT_STRUCTURE_R1`
   - Native unordered co-document context-structure hypothesis over opaque atoms.
   - Independent blind contextual-transfer audit: `100/100` in that exact structural scope.

6. `M5_NATIVE_RELATION_DISCRIMINATION_GAP_R1`
   - Shared context plus differing whole-sequence configuration does not permit equivalence.
   - Native relation-discrimination gap opens and revises when distinguishing evidence arrives.

7. `M5_NATIVE_GAP_EVIDENCE_REQUEST_R1`
   - Core SHA256: `1ff2dc93dc41f63e070a548d582d56911c406538eeacac826a0b9c419a4ce1eb`
   - No gap -> no request.
   - Open native relation-discrimination gap -> native evidence request.
   - Request depends on the dynamic gap, is isolated across gaps, persists/restarts, and is revoked by discriminating evidence.
   - Host gap creation/query generation/tool selection for active decision: NO.

## Important blind results retained without inflation

- Wide blind after scoped-gap repair: `75/100`.
- Context-structure transfer blind: `100/100` **only in its exact structural context-transfer scope**.
- Natural-language paraphrase blind R1: `60/100` on the contextual-paraphrase parent.
  - Zero-shot low-overlap paraphrase: FAIL.
  - Role-reversal rejection: FAIL.
- Natural-language paraphrase blind R2: `75/100` on relational-sequence core.
  - Role-reversal rejection: PASS.
  - Benign untrained reorder: FAIL.
  - Zero-shot low-overlap paraphrase: FAIL.
- Learned-transform causality blind: `75/100`.
  - `SPURIOUS_TRANSFORM_FALSE_INDUCTION_RESISTANCE=FAIL`.
- Context-grounded causality blind: `65/100`.
  - `GROUNDED_ROLE_REVERSAL_FALSE_EQUIVALENCE_RESISTANCE=FAIL`.

## Retired assumptions / non-promotable parents

- `recurring permutation shape => relation-preserving transformation` is RETIRED.
- `shared co-document context => same relation` is RETIRED.
- `M5_NATIVE_LEARNED_SEQUENCE_TRANSFORM_R1` is not promotion-eligible because blind causality exposed false induction.
- `M5_NATIVE_CONTEXT_GROUNDED_SEQUENCE_R1` is not promotion-eligible because blind causality exposed grounded role-reversal false equivalence.
- Earlier unordered sentence-coverage matching is superseded and must not return.

## Current FAIL capabilities

These remain FAIL and must not be described as achieved:

- `SEMANTIC_PARAPHRASE=FAIL`
- `ZERO_SHOT_LOW_OVERLAP_PARAPHRASE=FAIL`
- `BENIGN_UNGROUNDED_REORDER=FAIL`
- `AUTONOMOUS_RESEARCH=FAIL`
- `TOOL_EXECUTION=FAIL`
- semantic support/conflict/truth judgment is not an admitted capability; any future test for it must produce direct PASS/FAIL rather than semantic inflation from structure.

## Anti-hardcode state of current M5 lineage

Current admitted lineage has repeatedly passed gates for:

- token LEFT/RIGHT cognition absent;
- active Python cognition absent;
- host learning absent;
- host semantic substitution absent;
- no fixed English grammar/semantic-role tables in active candidate capability code;
- dynamic fixtures materialized only after compile/freeze in admission/blind tests where applicable.

## Exact next dependency

Build and test **mechanical evidence-tool transport**:

`native gap -> native evidence request -> host transports request only -> external/raw evidence -> native SIGMA ingestion/revision`

Host must not create the gap, research goal, semantic query interpretation, belief, answer, support/conflict decision, or final statement.

Before promotion of tool transport, add a blind gate proving that host transport cannot make SIGMA succeed when the native request is absent or malformed.