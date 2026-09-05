# C01-W02-B1.1-MATH-FAMILY-C05 — Durable Status Report

Status: `CHECKPOINTED`
Stage: `CURRICULUM`
Scope: `B1.1-C05 — Giải tích và biến đổi liên tục`
Execution branch: `hka-tree/c01-w02-math-c05`

## Definitely finished

- Bootstrap/scope lock is durable at CP03.
- Academic Block A T01–T05 is durable at CP04 commit `669ea1a9094e67ae07142825b636024dcfdd9f35`.
- Block A contains 5 nodes, 43 claims, 1 immutable-edition source, 20 D1–D4 objectives, 20 closure rows, 8 ownership/cross-link records and 5 sequence-intent records.
- The Block A directory and the committed NODES/CLAIMS blobs were read back from GitHub.
- Ownership boundaries T01/T02, T03/T06, T04/T07 and T05/T10 are explicitly recorded. C04 was not opened; its identifiers appear only as locked non-support boundaries supplied by the contract/amendment.

## Known nonterminal reconciliation

Claim `HKA-B1-1-C05-N004-C010` (integration by parts) is committed and used in the N004 D3 objective/closure, but the current N004 `claim_ids` and duplicate fingerprint still end at C009. This exact metadata repair is recorded in CP04 and must be made in the full NODES rewrite before the academic-closure checkpoint.

## Not finished

T06–T10, final source set, T07/T09 and T08/T10 overlap dispositions, complete-file read-back, full audits, RESULT/HANDOFF and terminal worker status remain outstanding.

## Locked decisions

- Continue the same branch; do not re-author T01–T05 from scratch.
- Do not open or author C04.
- Do not use claims from C04/C06/C07/C09/C10 or other locked scopes as support.
- No artifact after `CURRICULUM` is authorized.

## Next action

Extend the committed seven academic files with T06–T10, repair the recorded N004 claim-list metadata, then checkpoint complete academic closure and begin committed-file audits.
