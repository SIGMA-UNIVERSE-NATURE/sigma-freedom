# LANG-01G R3 — FRESH-STATE INITIALIZATION REPAIR READY

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Lane: `TEACHER_GPT_LANGUAGE_LANE`
Status: `R3_RUNNER_REPAIR_READY / LOCKED_RUNTIME_RERUN_NOT_YET_OBSERVED / NOT_ADMITTED`

## PREDECESSOR FAILURE

Preserve as immutable evidence:

- checkpoint: `SIGMA_PROFESSOR/CHECKPOINTS/20260905_LANG01G_R2_RUNTIME_FAIL_CASE001_STRING_REQUIRED.md`
- locked compilation: `SIGMAC_RC=0`
- failed bytecode SHA256: `839995f07413e241065386e9498c37723893f135fd933475a880c19ed65dc7d4`
- first VM case: `CASE_001_TIE`
- `VM_RC=22`
- failure text: `SIGMA host: string required`
- `LANG_01G_ADMITTED=NO`

## LOCKED-VM DIAGNOSTIC EVIDENCE

Diagnostic source/runner were explicitly diagnostic-only and did not alter the canonical LANG-01G source or admission oracle.

Observed identities:

- `SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- `VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`
- diagnostic source Git blob: `53ca847aa3eebe77e18c404e8dad8b717c9234cb`
- diagnostic source SHA256: `0a5ad75113ffc0550d13aa85c08e4f364af8d32c63528fbbc89bce827abeed64`
- diagnostic bytecode SHA256: `536133240cc94741033e8d6ec737a233d6adf14d4140441e71758f1abb164aa1`
- diagnostic VM RC: `22`

Observed ordered trace tail:

```text
TRACE_050_READ_ABSENT_STATE_BEFORE
TRACE_051_READ_ABSENT_STATE_AFTER
TRACE_060_SPLIT_ABSENT_STATE_BEFORE
SIGMA host: string required
```

`TRACE_061_SPLIT_ABSENT_STATE_AFTER` was not observed.

Therefore the first localized blocker is:

- `read_text(absent_state_path)` returns without VM failure;
- its returned value is not acceptable to locked-VM `str_split` as a string;
- the VM type failure occurs at `str_split` of the absent-state read result.

This supersedes the earlier unproven hypothesis that the blocker might occur later in map/persistence operations.

## ROOT CAUSE IN CURRENT HARNESS SCOPE

The canonical base admission runner `prepare_case` mechanically creates the input directory and state directory, but does not create `reference_evidence_state.memory` before the first VM invocation. The canonical native source models fresh state as an empty string using `STATE_EMPTY = exact(STATE_TEXT, "")`; on an absent path the locked VM does not provide a string suitable for `str_split`.

The repair is therefore constrained to fixture initialization rather than cognition:

- create the fresh state file as a zero-length file before each newly prepared case;
- do not change native evidence scoring;
- do not change candidate comparison;
- do not change persistence semantics after the file exists;
- do not change any of the 20 admission oracle cases;
- do not reinterpret the R2 failure as PASS.

## R3 RUNNER-ONLY REPAIR

New entry runner:

`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_LANG_01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION_PREFLIGHT_R3.sh`

Identity:

- commit: `df2f7939312c5fdc5323661bcebf1efa943b1ef4`
- Git blob: `6b51762246b348935d15816aa2a0c054e766432f`
- SHA256: `8d89cc504f36ce1190b7d364eac9cc76b0fe718824c54f484cf6b4da9561271c`
- static shell syntax: `PASS`

R3 verifies the unchanged base runner and canonical native source identities, mechanically patches the stale source pin, and inserts exactly one fresh-state initialization line into the sandbox copy of `prepare_case`:

```sh
: > "$STATE_FILE"
```

Repair classification:

- `REPAIR_CLASS=RUNNER_ONLY_MECHANICAL_FRESH_STATE_FIXTURE_INITIALIZATION`
- `FRESH_STATE_REPRESENTATION=ZERO_LENGTH_STATE_FILE`
- `NATIVE_SOURCE_CHANGED=NO`
- `COGNITIVE_POLICY_CHANGED=NO`
- `ORACLE_CASES_CHANGED=NO`
- `HOST_COGNITION=NO`
- `HOST_EVIDENCE_SCORING=NO`
- `HOST_ANTECEDENT_SELECTION=NO`

## CURRENT ADMISSION STATE

Until a locked Termux R3 transcript is observed:

- canonical source remains unchanged;
- prior failed bytecode remains failure evidence;
- `R3_LOCKED_SIGMAC_COMPILE=NOT_RUN_FROM_THIS_WINDOW`
- `R3_TOTAL_VM_INVOCATIONS=0_OBSERVED_FROM_THIS_WINDOW`
- `R3_ADMISSION=NOT_RUN_FROM_THIS_WINDOW`
- `LANG_01G_ADMITTED=NO`

The next admissible action is to execute R3 under the same locked SIGMAC/VM and apply the same 20-case admission gate. Any new first failure must be preserved and classified before another repair.

## CLAIM BOUNDARY

Keep locked:

- `PREFERRED_ANTECEDENT_HYPOTHESIS != RESOLVED_REFERENT`
- `COREFERENCE_RESOLUTION=NOT_PROVEN`
- `PRONOUN_SEMANTICS=NOT_PROVEN`
- `REAL_WORLD_ENTITY_IDENTITY=NOT_PROVEN`
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`
- do not progress to LANG-02 while LANG-01G remains unclosed.
