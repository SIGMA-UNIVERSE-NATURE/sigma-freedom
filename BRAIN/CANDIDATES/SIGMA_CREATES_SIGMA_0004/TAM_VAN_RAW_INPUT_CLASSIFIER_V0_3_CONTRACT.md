# SIGMA TAM VAN RAW INPUT CLASSIFIER v0.3 — BOUNDED GATE CONTRACT

## Gate identity

- Candidate: `SIGMA_CREATES_SIGMA_0004_TAM_VAN_TU_BI`
- Successor gate: `TAM_VAN_RAW_INPUT_CLASSIFIER_V0_3`
- Parent branch head used to prepare this gate: `194dcf7f25e61bc66699036d0b92811755e007ea`
- Scope: **finite exact-match UTF-8 corpus only**
- Canonical mutation: **NO**
- 54-core mutation: **NO**
- 512 promotion: **NO**
- Free-form semantic classifier claim: **NO**

This gate extends the already accepted v0.1/v0.2 defined scope without rerunning or modifying either accepted artifact.

## Inherited prerequisite

The existing SIGMA-PSI host bridge has already been machine-proven on OPPO for:

- `host("write_text", path, text)`
- `host("read_text", path)`
- exact UTF-8 roundtrip for the frozen probe.

v0.3 uses only the inherited `host("read_text", "tam_van_raw_input.txt")` capability. It does not rebuild the HP bridge and does not require the HP bridge.

## Question under test

Can a new SIGMA-PSI program:

1. read raw UTF-8 text from a file;
2. classify a frozen bounded corpus into measured `SIGNAL`, `NOISE`, `HARM`, and `UNKNOWN` flags;
3. preserve `UNKNOWN` as a fail-closed state for unrecognized input;
4. produce a bounded clean rewrite;
5. route the resulting state through the Tam Vấn policy and exit path;
6. compile and execute on the OPPO native toolchain with exact expected stdout?

## Frozen artifacts

- Source: `BRAIN/CANDIDATES/SIGMA_CREATES_SIGMA_0004/src/tam_van_raw_input_classifier_v0_3.sigma`
  - UTF-8 bytes: `9053`
  - SHA-256: `2a3dcaf1621ec04a39764d1174ac8a117e6d9a58fc02b5ebeef26eda80490ae6`
- Corpus: `BRAIN/CANDIDATES/SIGMA_CREATES_SIGMA_0004/tests/RAW_INPUT_CORPUS_V0_3.json`
  - UTF-8 bytes: `5389`
  - SHA-256: `ed26f839c46adbd0858448654cd44042a684ab2e9b51f301d9b0430d5f80e7e5`
- OPPO runner: `BRAIN/CANDIDATES/SIGMA_CREATES_SIGMA_0004/tests/run_v0_3_oppo_gate.sh`
  - UTF-8 bytes: `4104`
  - SHA-256: `1ce01a69b91d65c59cd926df4bebd50713588e20b45bb85f7fab63bb537cee91`

Six raw inputs and six exact stdout oracles are frozen in the corpus ledger and runner. The runner materializes them only inside a temporary workspace for execution.

## Measurement

Primary extraction measurement:

- 6 cases
- 4 primary labels per case: `SIGNAL`, `NOISE`, `HARM`, `UNKNOWN`
- 24 label decisions total
- PASS threshold: **24/24 exact**

Secondary measurements:

- `RECOVERABLE_INTENT`: 6/6 exact
- clean rewrite: 6/6 exact
- full pipeline stdout: 6/6 byte-exact
- compile rc = 0
- compile stderr empty
- each runtime rc = 0
- each runtime stderr empty

Exact stdout is the oracle. A mismatch is HOLD, not an invitation to edit the oracle after execution.

## Bounded classifier rule

Five raw strings are explicitly recognized. Any other raw text must take the default branch:

- `SIGNAL=0`
- `NOISE=0`
- `HARM=0`
- `UNKNOWN=1`
- `RECOVERABLE=0`
- clean text = `HOLD_UNKNOWN_INPUT_DO_NOT_INVENT`

This default branch is a fail-closed unknown detector, **not** evidence of general language understanding.

## Clean rewrite rule

For this frozen corpus only:

- clean signal is preserved;
- bounded noise is removed;
- the harmful mechanism in the frozen harm case is removed while a non-harmful informational intent is preserved;
- uncertain factual content is not invented;
- noise-only content is redirected to a real-goal request;
- unrecognized input is held as unknown.

## Tam Vấn mapping

The frozen harmful-mechanism case maps to `kho_nguoi=TRUE`, so the Tam Vấn gate must select the clean-equivalent path. All other recognized cases have no asserted Tam Vấn harm flag. Unknown remains stopped by the existing `UNKNOWN` policy and `TAM_VAN_EXIT_PATH`.

## Required OPPO execution

From the repository root on the OPPO/Termux machine:

```bash
bash BRAIN/CANDIDATES/SIGMA_CREATES_SIGMA_0004/tests/run_v0_3_oppo_gate.sh
```

The runner compiles only v0.3 and executes only the six v0.3 fixtures. It does **not** rerun v0.1 or v0.2.

## PASS interpretation

If all required observations pass, the only permitted claim is:

> A bounded exact-match raw-input classifier written in SIGMA-PSI read six UTF-8 inputs on the observed OPPO toolchain, produced 24/24 frozen primary extraction labels, six exact bounded clean rewrites, and six exact Tam Vấn pipeline outputs.

Even after machine PASS:

- `FREE_FORM_CLASSIFIER = HOLD`
- general semantic `SIGNAL/NOISE/HARM/UNKNOWN` extraction = HOLD
- general natural-language clean rewrite = HOLD
- full Native Brain integration = HOLD
- canonical promotion = NO

Independent evaluation is required after machine PASS before the v0.3 defined scope may be recorded as independently accepted.

## HOLD interpretation

Any compile failure, stderr output, runtime failure, label mismatch, clean rewrite mismatch, or full stdout mismatch means:

`V0_3_MACHINE_GATE=HOLD`

Preserve the exact failure evidence. Do not mutate v0.1/v0.2, do not alter expected output to force PASS, and do not generalize from partial success.
