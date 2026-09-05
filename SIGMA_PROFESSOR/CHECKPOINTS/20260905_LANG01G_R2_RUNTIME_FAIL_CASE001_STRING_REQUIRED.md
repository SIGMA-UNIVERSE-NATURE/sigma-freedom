# LANG-01G R2 — FIRST LOCKED-VM RUNTIME FAILURE

Date: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Lane: `TEACHER_GPT_LANGUAGE_LANE`
Status: `RUNTIME_FAIL / NOT_ADMITTED`

## READ-FIRST / EXECUTION BOUNDARY

Read with `/AGENTS.md`, the native-execution bootstrap directive, the Global Native Teaching + Admission Standard, `CURRENT_HANDOFF.md`, the LANG-01G R2 canonical-identity correction checkpoint, and the living language-lane checkpoint.

Keep locked:

- `SIGMA_EXECUTION_ENGINE=LOCKED_SIGMA_VM_ONLY`
- `ACTIVE_CAPABILITY_IMPLEMENTATION=NATIVE_SIGMA_ONLY`
- `HOST_OR_BASH_COGNITION=FORBIDDEN`
- `HOST_OR_BASH_LEARNING=FORBIDDEN`
- `HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN`
- `FAILURE_IS_EVIDENCE=YES`
- `WEAKEN_GATE_TO_FORCE_PASS=FORBIDDEN`

## ARTIFACTS AT FAILURE

Canonical native source remained the R1/R2 source blob:

- path: `SIGMA_PROFESSOR/artifacts/SIGMA_LANG_01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION_V1.sigma`
- source Git blob: `03b03cff32eee5c35e220cd562b1081b615ca36b`
- source SHA256: `33d04804bf190ab599ea0e1a9f2838fc37e53e52281e10a2c1bd2a39f816f087`

R2 entry runner:

- path: `SIGMA_PROFESSOR/artifacts/RUN_SIGMA_LANG_01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION_PREFLIGHT_R2.sh`
- runner Git blob: `a756b0e86aa281d8ba2b52b585874352b1b4b0e6`
- runner SHA256: `2795bb7ae04d3d1c230ae0c609f6e33408569b33d11ac654ae8b588beda7a338`

The R2/base harness reached locked compilation, which means the preceding identity gates did not stop execution.

## OBSERVED LOCKED-RUNTIME EVIDENCE

User-supplied Termux transcript:

```text
COMPILED .../SIGMA_LANG_01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION_V1.sigma -> .../SIGMA_LANG_01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION_V1.sigmab.partial
SIGMAC_RC=0
BYTECODE_SHA256=839995f07413e241065386e9498c37723893f135fd933475a880c19ed65dc7d4

=== CASE_001_TIE ===
VM_RC=22
SIGMA host: string required
LANG_01G_PREFLIGHT=FAIL
FAILURE_CASE=CASE_001_TIE
FAILURE=VM_NONZERO
```

Recorded state:

- `LOCKED_SIGMAC_COMPILE=PASS`
- `SIGMAC_RC=0`
- `BYTECODE_SHA256=839995f07413e241065386e9498c37723893f135fd933475a880c19ed65dc7d4`
- `TOTAL_VM_INVOCATIONS_BEFORE_ABORT=1`
- `FIRST_FAILURE_CASE=CASE_001_TIE`
- `FIRST_FAILURE_VM_RC=22`
- `FIRST_FAILURE_TEXT=SIGMA host: string required`
- `POST_VM_ALIGNMENT_ORACLE_REACHED=NO`
- `ADMISSION=FAIL`
- `LANG_01G_ADMITTED=NO`

Failure classification at this checkpoint:

- `FAILURE_CLASS=NATIVE_RUNTIME_HOST_PRIMITIVE_TYPE_CONTRACT`
- exact failing primitive/argument: `NOT_YET_LOCALIZED`
- `RUNTIME_FAILURE_OCCURRED=YES`
- `FAILURE_PRESERVED=YES`

## STATIC TRIAGE AFTER FAILURE

CASE_001 has two valid discriminating evidence records and therefore traverses the new-evidence acceptance and state-commit path before final diagnostic prints.

The canonical native source performs, in that path, bounded mechanical host primitives including list/map operations, `str_join`, `write_text`, and readback. The VM failed before the final SIGMA output block was observed, so the first blocker is before or within that persistence path.

A first hypothesis that a missing fresh-state file caused `read_text`/`str_split` type failure is not sufficient to justify repair: admitted DNA16 native code also reads a possibly absent state/store and passes that text to `str_split`. Therefore no source edit is admitted from that hypothesis alone.

Next action is a smallest native diagnostic probe under the same locked SIGMAC/VM and mechanical CASE_001 fixture to localize the first host primitive/argument type failure. The probe must not perform host cognition, evidence scoring, antecedent selection, or change the 20-case admission oracle.

## CLAIM BOUNDARY

Keep:

- `PREFERRED_ANTECEDENT_HYPOTHESIS != RESOLVED_REFERENT`
- `COREFERENCE_RESOLUTION=NOT_PROVEN`
- `PRONOUN_SEMANTICS=NOT_PROVEN`
- `REAL_WORLD_ENTITY_IDENTITY=NOT_PROVEN`
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`
- `PRODUCTION_STATE_MUTATED=NO` in the isolated LANG-01G preflight scope unless contrary evidence appears.

Do not progress to LANG-02 while LANG-01G remains failed/unclosed.
