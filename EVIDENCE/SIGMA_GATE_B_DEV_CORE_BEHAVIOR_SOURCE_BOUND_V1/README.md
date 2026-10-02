# SIGMA Gate B DEV/CORE/behavior — source-bound Tiny proof harness V1

This harness implements the next evidence step after Gate A without creating training examples, semantic answers, semantic scores, final/reserve artifacts, admission, cutover, server seed, or live mutation.

## Evidence bindings

The contract is pinned to:

- Gate A checkpoint `2475befc0261217fea910284b1035fcbfeda0627` (`GATE_A_TINY_DATA_DRIVEN_PASS`, `TRAIN_IMPROVES_DATA_PRESENT`, next action Gate B Tiny proofs).
- Behavioral evaluator checkpoint `289f597188e6028988ed972842dca9e262ef6edb` (Module97 behavioral-gate binding, Module98 transformer-owned semantic examination, six capabilities, `OPPO_REAL_LEARNING_PROOF=PENDING_SOURCE_BOUND_EXAM`).
- Unified candidate checkpoint `f98a8d7285be1296bc3d523d2b970f3721128e52`, which records Module99 as `99_rb_source_bound_semantic_adapter.sigma` and pins the unified source/bytecode used by the Gate A proof directory.

Gate B does not re-run TRAIN: TRAIN evidence is inherited only through the pinned Gate A evidence/model-pair binding. The eight Gate B proof units cover DEV, CORE, and the six behavioral capabilities.

The native policy semantics are fixed at the contract level but their concrete runtime tokens must be sourced from active Module97/98/99:

- DEV: candidate gain on the source-bound DEV workset;
- CORE: candidate no-regression on the source-bound CORE workset;
- BEHAVIOR: all-correct plus no-regression on the source-bound capability exam.

The required behavioral capabilities are exactly:

`referent_identity`, `relation_support`, `contradiction`, `scope_compatibility`, `evidence_support`, `cross_document_support`.

## Workset contract

There are exactly eight proof units: DEV, CORE, and one BEHAVIOR unit for each required capability. Every workset must bind a three-link provenance chain by SHA-256:

1. `source_root_manifest_path`: JSON schema `SIGMA_GATE_B_SOURCE_ROOT_MANIFEST_V1` with a non-empty `roots` array; every root entry contains an absolute `path` and SHA-256, and the validator re-hashes each root file.
2. `input_path`: the exact runtime input actually consumed by the bound native entrypoint.
3. `workset_manifest_path`: JSON schema `SIGMA_GATE_B_WORKSET_MANIFEST_V1` containing the exact `role`, `capability`, `source_root_manifest_sha256`, and `input_sha256`.

The harness does not generate any of these artifacts. Missing files, null hashes, hash mismatches, broken provenance links, missing role/capability provenance, or non-absolute paths are `BLOCKED_SAFE`.

## Runtime/source contract

A runnable manifest must bind all of the following before execution:

- active Module97 source with checkpoint SHA-256 `90baaf...`;
- active `98_rb_behavioral_semantic_eval.sigma` with checkpoint SHA-256 `75abe2...`;
- active `99_rb_source_bound_semantic_adapter.sigma` with an Oppo-measured SHA-256;
- unified source SHA-256 `93a9eb...`;
- unified bytecode SHA-256 `b7fa47...`;
- exact VM executable path + Oppo-measured SHA-256;
- ONE SIGMA identity `c8ccb7...`;
- Gate A rbseed/builder evidence hashes;
- a source-bound model-pair receipt containing baseline/candidate refs and fingerprints.

Each of the eight invocations must name a `binding_source` (Module97/98/99), an exact native entrypoint token, an exact native policy token, an exact native ACCEPT token, and an exact native REJECT token. The validator requires all four tokens to exist literally in the selected source file. The invocation must call the bound VM directly (`shell=False`), include the bound unified bytecode, and pass the exact workset and baseline/candidate refs. No host-side semantic answer or score is computed.

## Proof acceptance contract

The runner accepts one proof only when all of these are true:

- the bound process exits with RC 0;
- the source-bound native policy token and native ACCEPT token are present;
- the source-bound native REJECT token is absent;
- stdout binds the exact workset SHA-256, baseline/candidate refs and fingerprints, and ONE SIGMA identity;
- stdout asserts `LIVE_MUTATION=NO`, `SERVER_SEED=NO`, `ADMISSION=NO`, `CUTOVER=NO`;
- behavioral proofs additionally assert `TRANSFORMER_DOES_SEMANTIC_EXAM=YES` and `GROUNDING_ANSWERS_FOR_MODEL=NO` and name the exact capability;
- every bound input/source/runtime file remains byte-identical after the invocation.

The final Gate B result is `ACCEPT` only if all eight native proof units satisfy the contract. This is a Tiny source-bound evidence result only; it is not production readiness, R22 READY, final/reserve qualification, admission, or cutover.

## Oppo usage

Copy `PREREQUISITES.template.json` to a separate measured manifest. Fill only values directly measured/inspected on the active Oppo source/runtime. Set `binding_state` to `BOUND_BY_OPPO_MEASUREMENT` only after every required path/hash/entrypoint/decision token is bound.

Validate first:

```sh
python3 validate_gate_b.py \
  --contract GATE_B_CONTRACT.json \
  --manifest /absolute/path/to/measured_gate_b_manifest.json \
  --json-out /absolute/non-live/proof/prerequisite_validation.json
```

Run only if validation returns `READY`:

```sh
python3 run_gate_b.py \
  --contract GATE_B_CONTRACT.json \
  --manifest /absolute/path/to/measured_gate_b_manifest.json \
  --output-dir /absolute/non-live/proof/gate_b_run
```

The provided template is intentionally `UNBOUND`; running the validator against it must fail closed. No proof has been executed merely by installing this harness.
