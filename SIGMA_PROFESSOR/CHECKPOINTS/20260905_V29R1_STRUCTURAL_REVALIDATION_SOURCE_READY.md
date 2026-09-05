# V2.9R.1 STRUCTURAL REVALIDATION — SOURCE READY

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`

Dependency satisfied:
V2.8D.1 real selected-work deep re-learn PASS checkpoint commit:
`a0b3dce9b784ef36e552f377ab2c808e7d80e9d9`

## Candidate identities

Native source:
`SIGMA_PROFESSOR/artifacts/SIGMA_DEEP_RELEARN_STRUCTURAL_REVALIDATION_V2_9R1.sigma`

Source SHA256:
`94b12091d0d0727f23f57b298ee9ed71d11a2085571273496138990ca56f920b`

Source commit:
`36cb16d33eeb08d048c182499d4fc1e1a1ad0c53`

Runner:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V29R1_DEEP_RELEARN_STRUCTURAL_REVALIDATION_PREFLIGHT.sh`

Runner SHA256:
`c87fdcd46587b3e0200eed4be1f631ee5c2d5b270c1ef2a10141bd94e1ad4ce7`

Runner commit:
`be85ac96d98ece276295601c82a094ead19d88b4`

README commit:
`89d9cd584e9b65a052c55cd7af6b97ea73defa27`

## Static admission evidence

- `H_CALL_ARITY_AUDIT=PASS`
- `NATIVE_NOT_EQUAL_DEPENDENCY=NONE`
- `STR_STARTS_DEPENDENCY=NONE`
- `DIRECT_STR_DEPENDENCY=NONE`
- runner `bash -n` RC `0`

## Intended real positive evidence

Selected real work:
`0ac783c25e93ee81fe130c55026323e74191fc82a7782974ed64614aed66485b`

V2.5 baseline anchor:
`in => the`

Admitted V2.8D.1 deep segment anchors:

- segment 0: `in => the`
- segment 1: `As => disagreements`

Expected structural revalidation result:
`REOBSERVED`

This means only that the previous structural baseline anchor is observed again as a committed deep segment best anchor. It is not semantic truth validation.

## Important terminal-state handling

The V2.8D.1 admission runner intentionally ended with a synthetic over-limit evidence fixture. V2.9R.1 therefore must not consume the terminal D1 evidence file as if it were real deep evidence.

The V2.9R.1 runner:

1. mechanically preserves the terminal D1 QA state as reference;
2. re-runs exact admitted V2.8R.1 to regenerate real selected work;
3. re-runs exact admitted V2.8D.1 to regenerate real two-segment evidence;
4. requires regenerated real evidence SHA256 `9f2964422fdc34a1b3909a67900ef7902b719974b44081b14002c6b4f32ad28a` before revalidation.

## Admission gates prepared

- real positive `REOBSERVED`;
- fresh VM persistent revalidation-state reuse without duplicate append;
- deterministic revalidation replay;
- completed negative counterexample -> `NOT_REOBSERVED`;
- incomplete deep re-learn -> `PENDING`, no revalidation mutation;
- partial/uncommitted matching evidence ignored;
- state/evidence/survey over-budget refusal;
- real survey/document/deep evidence immutability.

## Current truth

- `COMPILE_PASS=NOT_PROVEN`
- `RUNTIME_PASS=NOT_PROVEN`
- `BYTECODE_SHA256=UNKNOWN`
- `ADMISSION=NOT_PROVEN`
- `STRUCTURAL_REVALIDATION_ONLY=YES`
- `SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN`
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`
- `BOUNDED_FILE_IO=NOT_PROVEN`
- `MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`

Next action:
run exact V2.9R.1 source + runner on the locked compiler/VM and preserve all runtime evidence.
