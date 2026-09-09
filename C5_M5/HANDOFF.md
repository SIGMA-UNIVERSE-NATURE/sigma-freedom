# SIGMA C5 M5 — Window Handoff

Read in order:

1. `C5_M5/MISSION.md`
2. `C5_M5/END_STATE_ACCEPTANCE.md`
3. `C5_M5/C5V3_AUTONOMOUS_INTEGRATION_PLAN.md`
4. `C5_M5/STATUS.md`
5. `C5_M5/CHECKPOINTS.md`
6. `C5_M5/WHOLE_WORK_R1_FAILURE_AND_R1H1.md`
7. this file

## Current admitted chain

Mechanical transport R2 PASS; corrected blind host-substitution PASS; native gap search-query PASS; real Internet search-discovery PASS; real Internet full-source stream PASS.

Production binding remains NO.

## Latest failure

Whole-Work Ladder R1 Stage A reached native recurrence and recurrent unit signatures, then failed:

`FAIL=FINALIZE_VM`, `RC=35`.

Root cause is a runtime serialization defect, not a semantic blind result: the core directly concatenated integer whole-work counts into persistent text on the first exercised FINALIZE path. Native count gates remain valid.

## Exact next execution artifact

Run:

`SIGMA_C5_C5V3_M5_WHOLE_WORK_LADDER_R1H1_BUNDLE.zip`

Hashes:

- Whole-work R1H1 core: `a9549a65e3e7229a5ab74e27c0a26514415f3f7a117930d6e52bfbd93b562195`
- Admission preflight: `bda40ee9ae3ec8a799a34dc53cfbe7234745243a9d8a6c6bd35b3195bc79e289`
- Independent blind auditor: `0b1b105a9902e0fddc6b8ed090e098c7674ea52d5a949f4ddab6c1812107017f`
- Ladder runner: `f6431921da6c69055f52293e979ff9216830e6f0d7dda33fcd45e518941db7ff`
- Ladder bundle: `bb384565fa79294a8ec4ab853ec03dde69350111669627db2c9ab63caa4fc935`

R1H1 changes only the FINALIZE text serialization: integer unit/signature counts are still native gates but are no longer concatenated directly into text state.

The independent blind keeps the same semantic challenges: source removal, distant recurrent recall, role reversal, high-frequency background suppression, once-only event-detail retention, direct whole-work summary and restart. A summary-scorer harness bug was corrected so the summary result is snapshotted before a later recall can overwrite the action output.

## Interpretation rule

A passing Stage A only proves source-independent structural whole-work memory in its exact scope. It does not prove narrative understanding.

If blind `UNIQUE_EVENT_DETAIL_RETENTION=FAIL`, the next core must learn/preserve novelty or salience without host-provided importance labels.

If blind `EVIDENCE_BACKED_WHOLE_WORK_SUMMARY=FAIL`, keep it FAIL; do not add host/extractive summary generation.

## Hard FAILs retained

- autonomous research;
- whole-work narrative understanding;
- evidence-backed whole-work summary;
- theme/direction/human-value induction;
- multilingual narrative transfer;
- semantic compression after source removal;
- continual learning from compressed local memory;
- semantic paraphrase/zero-shot low-overlap/benign ungrounded reorder;
- semantic support/conflict/truth judgment.

## Later C5V3 route

Only after the required cognition/memory subset passes:

`read-only ABI/state synchronization -> isolated successor graft -> autonomous-runner shadow -> soak/restart/recovery -> promotion -> explicit user-authorized cutover -> rollback retained`.

Never hot-patch production during candidate admission.
