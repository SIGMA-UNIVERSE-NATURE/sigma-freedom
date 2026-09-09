# SIGMA C5V3 Gate B — R11 HOLD (`SIGMA_MAX_STEPS` not proven) + FIX1 prepared

Updated: 2026-09-09

This checkpoint is a recovery note, **not an admitted PASS**.

## Last admitted checkpoint

R10 remains the latest admitted Gate B test result:

- R10 source SHA256: `7d9e91f9a5a7fa265ca4304084fc48aca105b74ae7ca08662398b535c8d3cd34`
- R10 bytecode SHA256: `c837fcc03f79f64487d9146fc268783c13bf0769352a2068492c1d4374b109c5`
- `R10_OFFLINE_EXPLICIT_DISPATCH_BRIDGE=PASS`
- dormant production `TICK` regression PASS
- live production activation/synchronization remains NO.

## Original R11 result — HOLD

The first R11 activation harness attempted to use `SIGMA_MAX_STEPS` as a VM execution-footprint oracle.

Observed result:

- bundle manifest/syntax/preflight PASS;
- exact R10 source/bytecode locks retained;
- no semantic expected output;
- no core instrumentation;
- no host semantic substitution;
- `HOLD_SIGMA_MAX_STEPS_EFFECT_NOT_PROVEN`;
- `R11_ACTIVATION_DRIVER=FAIL`;
- `RESULT=HOLD`.

Interpretation: the locked VM did not prove support for the assumed runtime step-budget control. This is a harness/oracle incompatibility and does **not** invalidate R10.

Do not claim R11 activation PASS from the original harness.

## R11 FIX1 prepared

FIX1 removes all dependency on `SIGMA_MAX_STEPS`.

It uses the exact frozen R10 source/bytecode with no instrumentation. For every one of the 28 source-derived M5 event literals it compares deterministic runtime observable signatures against dynamically generated non-event counterfactuals.

Observable signature:

- VM return code;
- stdout after normalizing the event input bytes;
- stderr after normalizing the event input bytes;
- filesystem content/existence snapshot after excluding `event.txt` and normalizing event input bytes from file contents.

This specifically prevents a false PASS caused only by `print(EVENT)` or by the changed contents of `event.txt`.

Required FIX1 matrix:

- exact event replay deterministic: `28/28`;
- two distinct dynamic non-event controls normalize to the same signature: `28/28`;
- exact event signature differs from normalized counterfactual signature: `28/28`;
- no core instrumentation;
- no test-oracle contamination;
- no semantic expected answer/query/truth/conflict/status/tool choice;
- artifact hashes frozen;
- synthetic state removed;
- offline only.

Prepared bundle:

`SIGMA_C5V3_OFFLINE_M5_ACTIVATION_R11_FIX1_BUNDLE_20260909.zip`

Bundle SHA256:

`4edbbec6aca141cab6ced4f096c4c5e01ee144172895041a87cad8cb89785dbb`

## Current canonical boundary

`R10=PASS`
`R11_ORIGINAL=HOLD`
`R11_FIX1=PREPARED_NOT_YET_RUN`
`M5_CAPABILITY_ACTIVE_IN_LIVE_PRODUCTION_DISPATCH=NO`
`C5V3_PRODUCTION_CORE_SYNCHRONIZED=NO`
`ONLINE_SYNC_FROM_TEST_WINDOW=NO`
`PRODUCTION_MUTATION_FROM_TEST_WINDOW=NO`
`PRODUCTION_BINDING_FROM_TEST_WINDOW=NO`

`LATEST_GATE_B_SYNC_CHECKPOINT.md` must remain on R10 until R11 FIX1 produces a real PASS.
