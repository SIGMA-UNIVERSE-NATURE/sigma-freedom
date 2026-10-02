# SIGMA Gate B DEV/CORE/Behavior — Source-Bound Proof Contract V1

Date: 2026-10-03
Type: DEV/CORE/behavior Tiny proof harness contract
Scope: source-bound, read-only proof orchestration only

## Evidence anchors

- Gate A anchor: `2475befc0261217fea910284b1035fcbfeda0627`
  - `GATE_A_TINY_DATA_DRIVEN_PASS`
  - `TRAIN_IMPROVES_DATA_PRESENT`
  - next action: `BUILD_GATE_B_DEV_CORE_BEHAVIOR_TINY_PROOFS`
- Behavioral evaluator anchor: `289f597188e6028988ed972842dca9e262ef6edb`
  - transformer-owned semantic exam
  - grounding does not answer for the model
  - six-capability behavioral gate required
  - `OPPO_REAL_LEARNING_PROOF=PENDING_SOURCE_BOUND_EXAM`
- Current `SIGMA_LIFE` observed while building this harness: `a789793f43513f62ca6806ad46bf27ca3fce02d9`
  - use the existing R57 child model/state
  - do not retrain
  - do not create a new proposal
  - proceed to Gate B DEV/CORE/behavior evaluation

This contract does not reinterpret any prior checkpoint as Gate B PASS.

## Non-negotiable boundary

The harness is verifier/orchestrator only. It must not provide semantic answers, gold labels, semantic scores, or substitute host judgments for the model/evaluator.

Always keep:

- `LIVE_MUTATION=NO`
- `SERVER_SEED=NO`
- `ADMISSION=NO`
- `CUTOVER=NO`
- `FINAL=NO`
- `RESERVE=NO`
- `RETRAIN=NO`
- `NEW_PROPOSAL=NO`
- `HOST_SEMANTIC_ANSWER=NO`
- `HOST_SEMANTIC_SCORE=NO`

The only acceptable semantic decisions are fields emitted by the source-bound native evaluator receipt.

## Exact prerequisite contract

The JSON prerequisite manifest is authoritative for this harness. Every required file must be a non-empty regular file and must match its SHA-256 exactly.

### Runtime/source bindings

Required:

1. exact Sigma VM path and SHA-256;
2. exact unified source path/hash from the current evidence lineage;
3. exact unified bytecode path/hash;
4. exact Module97 source path with the evaluator-bound hash from the behavioral checkpoint;
5. exact Module98 behavioral semantic evaluator path/hash;
6. exact Module99 source-bound semantic adapter path/hash.

Known hashes are pinned where repository evidence provides them. Unknown current values remain `null` and therefore block execution.

The runtime action identifier must occur literally in the bound Module97/98/99 source text. The harness will not accept an unbound command name.

### TRAIN/DEV source split

Gate B DEV is not valid unless the TRAIN source and DEV workset are different artifacts and a source-bound split receipt proves the DEV set is held out.

Required split receipt schema:

`SIGMA_GATE_B_TRAIN_DEV_SPLIT_RECEIPT_V1`

Required fields:

- `source_bound=true`
- `disjoint=true`
- `host_semantic_selection=false`
- exact `train_sha256`
- exact `dev_sha256`
- exact `builder_source_sha256`

The split builder source itself must be path/hash bound.

### DEV workset

Required bindings:

- DEV workset path/hash;
- DEV provenance path/hash;
- TRAIN source path/hash and provenance path/hash;
- split receipt above.

The harness does not inspect or author semantic answers. The native receipt must say DEV is source-bound, held out, and PASS.

### CORE workset

Required bindings:

- CORE workset path/hash;
- CORE provenance path/hash.

The native receipt must say CORE is source-bound, has no regression under the evaluator's own policy, and PASS. The host does not calculate the semantic score.

### Behavior worksets

Exactly six behavior entries are required. Each entry must bind:

- capability ID;
- workset path/hash;
- provenance path/hash.

Capability IDs are not invented in this repository harness. Each ID must be present in the bound Module97/98/99 source text. Missing or duplicate capability IDs fail closed.

The native receipt must contain exactly six capability results matching the manifest IDs and workset hashes, with each result emitted as PASS by the native evaluator.

## Native input contract

After all prerequisites validate, the harness writes a generated input document containing only:

- run ID;
- ONE SIGMA identity;
- existing parent/child model and optimizer references;
- existing R57 TX/state references;
- bound source/runtime hashes;
- bound TRAIN/DEV/CORE/behavior workset paths/hashes;
- source-bound split receipt binding;
- policy flags;
- requested native runtime action;
- `SIGMA_MAX_STEPS=10000000`.

It contains no semantic answers and no host-authored scores.

## Native output receipt contract

Required schema:

`SIGMA_GATE_B_DEV_CORE_BEHAVIOR_NATIVE_RECEIPT_V1`

The receipt must echo the exact run ID, child model, parent model, TXID, TX receipt, R57 state hash, source hashes, workset hashes, and split receipt hash.

Required ownership fields:

- `transformer_does_semantic_exam=true`
- `grounding_answers_for_model=false`
- `host_semantic_answer=false`
- `host_semantic_score=false`

Required proof scope:

- `proof_scope=TINY`

Required gate results:

- DEV: `source_bound=true`, `held_out=true`, `decision=PASS`
- CORE: `source_bound=true`, `no_regression=true`, `decision=PASS`
- behavior: `source_bound=true`, `capability_count=6`, `decision=PASS`
- each of six capability results: exact capability ID, exact workset hash, `decision=PASS`
- aggregate: `gate_b_decision=PASS`

Required policy fields all remain false for live mutation, server seed, admission, cutover, final, reserve, retrain, new proposal, host semantic answer, and host semantic score.

The harness validates this receipt but does not produce the semantic decisions itself.

## Fail-closed stop conditions

Return `HOLD` and do not run the native proof if any of the following is true:

- VM path/hash is not bound;
- any pinned source/hash mismatches;
- Module97 path is not bound;
- Module99 hash is not bound;
- runtime action is not source-bound;
- runtime argv is not bound to exact VM + bytecode + input + output + action;
- TRAIN/DEV split builder or receipt is missing;
- DEV/CORE source/provenance is missing;
- six capability IDs cannot be sourced from active evaluator/adapter source;
- any behavior workset/provenance is missing;
- any bound source/workset changes during the run;
- runtime exits nonzero;
- native receipt is missing, stale, schema-invalid, hash-mismatched, or non-PASS;
- any prohibited mutation/admission/cutover/final/reserve flag is asserted.

## Current status of this repository change

Harness: implemented.

Validator: implemented.

Prerequisite manifest: implemented and intentionally incomplete where current Oppo runtime/workset evidence is unavailable to GitHub.

Gate B proof execution: not claimed.

Gate B PASS: not claimed.

Next action on Oppo: bind the exact missing prerequisite fields from active source/runtime/worksets, then run the harness unchanged. If those bindings cannot be established, remain at `HOLD`.