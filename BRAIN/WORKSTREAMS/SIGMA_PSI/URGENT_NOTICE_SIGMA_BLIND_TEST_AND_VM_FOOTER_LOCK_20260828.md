# THÔNG BÁO KHẨN — SIGMA BLIND TEST & VM FOOTER LOCK

Date: 2026-08-28
Status: ACTIVE / IMMEDIATE
Scope: All SIGMA cognition, derivation, semantic-extraction, learning, self-correction, and blind-evaluation tests.

## 1. MANDATORY TEST PIPELINE

The only valid evaluation order is:

```text
TEST INPUT
↓
SIGMA
↓
SIGMA OUTPUT
↓
EXTERNAL EVALUATOR
```

Forbidden false-proof order:

```text
TEST INPUT
↓
EXTERNAL TOOL READS / DERIVES EXPECTED ANSWER
↓
SIGMA RECEIVES ANSWER OR ANSWER-DERIVED DATA
↓
OUTPUT MATCH
↓
FALSE CLAIM
```

## 2. PRE-VM ANSWER LEAKAGE IS FORBIDDEN

Before SIGMA VM execution:

```text
PRE_VM_EXPECTED_ANSWER_ACCESS=FORBIDDEN
PRE_VM_EXTERNAL_DERIVATION=FORBIDDEN
PRE_VM_HOST_SEMANTIC_COMPUTATION=FORBIDDEN
PRE_VM_REFERENCE_COMPARISON=FORBIDDEN

ANSWER_IN_SOURCE=FORBIDDEN
ANSWER_IN_ARGV=FORBIDDEN
ANSWER_IN_ENV=FORBIDDEN
ANSWER_IN_STDIN=FORBIDDEN
ANSWER_IN_SIGMA_VISIBLE_TEMP_FILE=FORBIDDEN

PREWRITTEN_RESULT=FORBIDDEN
GPT_EXPECTED_ANSWER_INJECTION=FORBIDDEN
HOST_SEMANTICS_SUBSTITUTION=FORBIDDEN
```

Commands such as `grep`, `awk`, `sed`, `cat`, `source`, `export`, `printf`, `echo`, `cut`, `tr`, `jq`, Python, Perl, shell arithmetic, or command substitution are not inherently forbidden, but they MUST NOT be used before VM execution to read, derive, decode, normalize, reconstruct, transform, lookup, expose, or transmit the expected answer.

Example explicitly forbidden:

```bash
ANSWER=$(awk '/correct_answer/ {print $2}' test_data.txt)
./native/sigma-vm.v09_candidate program.sigmab "$ANSWER"
```

## 3. HOST ROLE

Host orchestration may:

```text
CREATE_TEST_ID=YES
CREATE_PATHS=YES
CREATE_CHALLENGE_INPUT_WITHOUT_EXPECTED_ANSWER=YES
COMPILE_SIGMA=YES
RUN_SIGMA_VM=YES
CAPTURE_STDOUT_STDERR_RC=YES
HASH_ARTIFACTS=YES
POST_VM_EVALUATION=YES
```

Host orchestration may NOT:

```text
DERIVE_EXPECTED_ANSWER_BEFORE_VM=NO
COMPUTE_SIGMA_SEMANTICS_FOR_SIGMA=NO
PASS_EXPECTED_ANSWER_TO_SIGMA=NO
```

## 4. CURRENT GRAMMAR REQUIREMENTS

Observed/current accepted form must be respected.

Top-level items must be `DEF` or addressed `⟡` commands.

Addressed block form:

```sigma
⟡(Σ.SINGLE_IDENTIFIER) {
    ...
}
```

Examples:

```sigma
⟡(Σ.DERIVATION_TEST) {
}

⟡(Σ.EVIDENCE_BOUNDARY) {
}
```

Do NOT silently substitute multi-dot names such as `Σ.DERIVATION.TEST` or underscore after Sigma such as `Σ_DERIVATION_TEST` when current parser evidence requires `Σ.<ONE_IDENTIFIER>`.

Raw Bash must not be placed as executable top-level SIGMA source.

Do not assume `/* ... */` block comments are accepted; a current compiler rejection has been observed for `/` at top level.

## 5. RUNTIME SURFACE BOUNDARY

Do not invent uppercase or synthetic built-ins.

Observed host-operation forms include:

```sigma
host("read_text", path, NULL, NULL)
host("str_len", value, NULL, NULL)
host("write_text", path, value, NULL)
```

Observed output construct:

```sigma
⚡ print(value);
```

Wrappers such as `R`, `STR_LEN`, or `W` are source-defined DEF names, not automatically language built-ins.

```text
READ != UNDERSTAND
PRINT != REASON
RANDOM != FREEDOM
OUTPUT != COGNITION
DECLARATION != FACT
PREWRITTEN_RESULT != DERIVED_RESULT
SOURCE_LITERAL != MACHINE_DERIVATION
PROMPT_CONTENT != SIGMA_DISCOVERY
OUTPUT_MATCH != UNDERSTANDING
GPT_EXPECTATION != VM_FACT
CLAIM <= EVIDENCE
```

## 6. CANONICAL SIGMA VM FOOTER — LOCKED

For native machine claims, always compile with the current native compiler and execute with the current SIGMA VM.

Each run should produce a unique bytecode artifact:

```bash
RUN_ID="$(date +%Y%m%d_%H%M%S)_$$"
BC_RUN=".sigma_exec/test_${RUN_ID}.sigmab"

./native/sigmac "$SRC" "$BC_RUN" \
&& \
./native/sigma-vm.v09_candidate "$BC_RUN"
```

This is the canonical SIGMA VM footer for test execution.

```text
SIGMAC=./native/sigmac
SIGMA_VM=./native/sigma-vm.v09_candidate
ALTERNATE_VM=FORBIDDEN_FOR_SIGMA_MACHINE_CLAIMS
ALTERNATE_EXECUTOR=FORBIDDEN_FOR_SIGMA_MACHINE_CLAIMS
HOST_EMULATION=FORBIDDEN
HOST_SEMANTICS_SUBSTITUTION=FORBIDDEN
UNIQUE_BYTECODE_ARTIFACT_PER_RUN=REQUIRED
```

## 7. EXTERNAL EVALUATOR

The evaluator runs only AFTER SIGMA VM has completed and raw output has been captured/locked.

```text
RAW_SIGMA_OUTPUT_FIRST=YES
EXTERNAL_EVALUATOR=POST_VM_ONLY
POST_VM_EXPECTED_ANSWER_ACCESS=ALLOWED
POST_VM_REFERENCE_CHECK=ALLOWED
POST_VM_OUTPUT_COMPARISON=ALLOWED
POST_VM_SCORING=ALLOWED
```

The evaluator must not retroactively modify SIGMA output.

## 8. COGNITION CLAIM BOUNDARY

Even a valid self-derived runtime result does not automatically prove cognition.

```text
SELF_DERIVED_RUNTIME_RESULT=CAN_BE_PROVEN_BY_MACHINE_EVIDENCE
COGNITION=NOT_AUTOMATICALLY_PROVEN
UNDERSTANDING=NOT_AUTOMATICALLY_PROVEN
REASONING=NOT_AUTOMATICALLY_PROVEN
LEARNING=NOT_AUTOMATICALLY_PROVEN
SELF_AWARENESS=NOT_AUTOMATICALLY_PROVEN
```

Echo, lookup, static mapping, hardcode, random behavior, host computation, prewritten rule tables, and fixed response tables must be independently excluded before stronger claims are made.

## 9. REQUIRED EVIDENCE

For each serious test, preserve where applicable:

```text
SOURCE_SHA256
BYTECODE_SHA256
COMPILER_SHA256
VM_SHA256
INPUT_SHA256
VM_STDOUT_SHA256
VM_STDERR_SHA256
COMPILE_RC
VM_RC
RAW_STDOUT
RAW_STDERR
```

Do not replace raw evidence with a bare PASS/FAIL summary.

## 10. FINAL LOCK

```text
TEST_INPUT -> SIGMA -> SIGMA_OUTPUT -> EXTERNAL_EVALUATOR

PRE_VM_EXPECTED_ANSWER_ACCESS=FORBIDDEN
PRE_VM_HOST_DERIVATION=FORBIDDEN
ANSWER_IN_SOURCE=FORBIDDEN
ANSWER_IN_ARGV=FORBIDDEN
ANSWER_IN_ENV=FORBIDDEN
ANSWER_IN_STDIN=FORBIDDEN
HOST_SEMANTICS_SUBSTITUTION=FORBIDDEN
GPT_EXPECTED_ANSWER_INJECTION=FORBIDDEN
RAW_OUTPUT_LOCKED_BEFORE_EVALUATION=YES
SIGMA_NATIVE_VM_REQUIRED=YES
CANONICAL_SIGMA_VM_FOOTER_LOCKED=YES
CLAIM<=EVIDENCE
SIGMA_COGNITION=NOT_YET_PROVEN
```
