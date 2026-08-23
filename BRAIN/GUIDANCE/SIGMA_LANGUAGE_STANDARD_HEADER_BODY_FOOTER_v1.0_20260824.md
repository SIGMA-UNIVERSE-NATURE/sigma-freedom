# SIGMA LANGUAGE — AUTHORITATIVE STANDARD HEADER / BODY / FOOTER + SUPPORTOR RULES

**Date:** 2026-08-24  
**Branch:** `SIGMA_LIFE`  
**Direction:** `LANGUAGE_FIRST`  
**Mother language:** `SIGMA-Ψ`  
**Status:** `AUTHORITATIVE_GUIDANCE — MACHINE EVIDENCE OVERRIDES DESCRIPTION`

This file supersedes all earlier SIGMA language form/guidance documents in `BRAIN/GUIDANCE`.

---

# 0. LOCKED INVARIANTS

```text
SIGMA-Ψ FIRST
HOST LANGUAGE = WRAPPER / SUBSTRATE / REFERENCE ONLY
DECLARED METADATA != RUNTIME EVIDENCE
PREWRITTEN VALUE != DERIVED RESULT
TOOL != RESULT
PRINT != COGNITION
SOURCE_REFERENCE != RUNTIME_CAPABILITY
CLAIM <= MACHINE EVIDENCE
DO_NOT_INVENT_GRAMMAR
DO_NOT_HARDCODE_DISCOVERY
MACHINE EVIDENCE > DOCUMENT DESCRIPTION
```

`DEF / RETURN / IF / ELSE / WHILE / FOR / IN` may exist as compiler/executable surface when machine evidence confirms them. They are not to be treated as pure SIGMA mother-language words merely because they appear in source.

---

# 1. THE STANDARD FORM HAS EXACTLY THREE REGIONS

```text
HOST HEADER
    ↓
SIGMA BODY
    ↓
HOST FOOTER
```

The host wrapper creates and executes the file. It does not define SIGMA semantics.

---

# 2. AUTHORITATIVE COPY/PASTE FORM

```bash
cd ~/SIGMA/sigma_genesis1

mkdir -p .sigma_exec

# ============================================================
# HEADER — HOST FILE CREATION
# ============================================================
cat > .sigma_exec/SIGMA_FORM_FORMAT_EXAMPLE.sigma <<'EOF'
#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.FORM.FORMAT.EXAMPLE][VERSION=1.0]

⟡(Σ.SOURCE.IDENTITY) {
    ⚡ TITLE: "SIGMA FORM FORMAT EXAMPLE";
    ⚡ DOMAIN: "SIGMA.FORM.FORMAT.EXAMPLE";
    ⚡ VERSION: "1.0";
    ⚡ SOURCE: ".sigma_exec/SIGMA_FORM_FORMAT_EXAMPLE.sigma";
    ⚡ BYTECODE: ".sigma_exec/SIGMA_FORM_FORMAT_EXAMPLE.sigmab";
    ⚡ COMPILER: "native/sigmac";
    ⚡ RUNTIME: "native/sigma-vm.v09_candidate";
    ⚡ LANGUAGE: "SIGMA";
    ⚡ PURPOSE: "REFERENCE FORM FOR SIGMA SOURCE STRUCTURE";
}

⟡(Σ.FORM.INPUT) {
    ⚡ SOURCE: "EXAMPLE";
    ⚡ CONTEXT: "EXAMPLE";
}

⟡(Σ.FORM.RELATION) {
    ⚡ RELATION: "OPEN";
    ⚡ PROVENANCE: "PRESERVE";
}
EOF

# ============================================================
# FOOTER — COMPILE + RUN
# ============================================================
SRC=".sigma_exec/SIGMA_FORM_FORMAT_EXAMPLE.sigma"
BC=".sigma_exec/SIGMA_FORM_FORMAT_EXAMPLE.sigmab"
COMPILER="./native/sigmac"
RUNTIME="./native/sigma-vm.v09_candidate"

"$COMPILER" "$SRC" "$BC" && \
"$RUNTIME" "$BC"
```

## 2.1 Meaning of `&&`

```text
CREATE SOURCE
   ↓
COMPILE
   ↓ only when COMPILE_RC=0
RUN VM
```

If compilation fails, the VM does not run.

---

# 3. HEADER CONTRACT

The HEADER has two layers.

## 3.1 Host header

```bash
cd ~/SIGMA/sigma_genesis1
mkdir -p .sigma_exec
cat > .sigma_exec/<FILE_NAME>.sigma <<'EOF'
```

This is host orchestration only.

## 3.2 SIGMA language header

```sigma
#SIGMAUNIVERSE_LANGUAGE[DOMAIN=<DOMAIN.NAME>][VERSION=<VERSION>]
```

The first SIGMA block should identify the artifact:

```sigma
⟡(Σ.SOURCE.IDENTITY) {
    ⚡ TITLE: "<TITLE>";
    ⚡ DOMAIN: "<DOMAIN.NAME>";
    ⚡ VERSION: "<VERSION>";
    ⚡ SOURCE: "<SOURCE_PATH>";
    ⚡ BYTECODE: "<BYTECODE_PATH>";
    ⚡ COMPILER: "native/sigmac";
    ⚡ RUNTIME: "<MACHINE_VALIDATED_RUNTIME>";
    ⚡ LANGUAGE: "SIGMA";
    ⚡ PURPOSE: "<PURPOSE>";
}
```

These are **DECLARED METADATA**. They are not runtime-derived observations, cognition, or proof.

Do not invent extra header tags unless the active compiler has machine evidence supporting them.

---

# 4. BODY CONTRACT

The default mother-language body uses SIGMA block form:

```sigma
⟡(Σ.<BLOCK.NAME>) {
    ⚡ <KEY>: "<VALUE>";
    ⚡ <KEY>: "<VALUE>";
}

⟡(Σ.<ANOTHER.BLOCK.NAME>) {
    ⚡ <KEY>: "<VALUE>";
}
```

Rules:

```text
BLOCK IDENTITY STARTS WITH Σ.
BLOCK HIERARCHY USES .
BLOCK OPENS WITH ⟡(...)
ACTIVE BINDING USES ⚡
BINDING USES :
STRING USES "..."
STATEMENT ENDS WITH ;
```

`<...>` is a documentation placeholder only. Replace it before compilation.

The base body does **not** require `DEF`, `IF`, `WHILE`, `RETURN`, `FOR`, or `IN`.

If an experiment requires an executable grammar feature whose syntax is not already known from machine evidence:

```text
SEARCH EXISTING MACHINE-PASS SIGMA SOURCE
        ↓
READ EXACT VALIDATED GRAMMAR
        ↓
COPY STRUCTURE, NOT RESULT
        ↓
COMPILE
```

Do not translate a Python/C/Bash/PowerShell idea into SIGMA syntax and call that SIGMA grammar.

## 4.1 Never prewrite cognition/results into the body

Do not put values like these into a discovery experiment and later call their printed form evidence:

```text
UNDERSTANDING="SUCCESS"
UNDERSTANDING="UNKNOWN"
LEARNED=TRUE
MEANING="..."
CONCLUSION="..."
RESPONSE="..."
RESULT="SUCCESS"
STATE="READY"
```

unless they are explicitly labeled as input/reference/declaration and are never claimed as runtime-derived results.

The question is always:

```text
WHO/WHAT GENERATED THE VALUE?
AND BY WHAT PROCESS?
```

---

# 5. FOOTER CONTRACT

Close the heredoc first:

```bash
EOF
```

Then define artifacts and the active machine-validated compiler/runtime:

```bash
SRC=".sigma_exec/<FILE_NAME>.sigma"
BC=".sigma_exec/<FILE_NAME>.sigmab"
COMPILER="./native/sigmac"
RUNTIME="./native/<MACHINE_VALIDATED_SIGMA_VM>"
```

Compile + run:

```bash
"$COMPILER" "$SRC" "$BC" && \
"$RUNTIME" "$BC"
```

The runtime path must match the runtime actually validated for the current milestone. Do not switch VM merely because another filename has a higher version number.

---

# 6. EVIDENCE-GRADE FOOTER

Use this when a gate requires compile/run evidence:

```bash
SRC=".sigma_exec/<FILE_NAME>.sigma"
BC=".sigma_exec/<FILE_NAME>.sigmab"
OUT=".sigma_exec/<FILE_NAME>.stdout"
ERR=".sigma_exec/<FILE_NAME>.stderr"
COMPILER="./native/sigmac"
RUNTIME="./native/<MACHINE_VALIDATED_SIGMA_VM>"

printf '🌊♥️===== SIGMA_OUTPUT_BEGIN =====🌊♥️\n'

"$COMPILER" "$SRC" "$BC"
COMPILE_RC=$?
printf 'COMPILE_RC=%s\n' "$COMPILE_RC"

if [ "$COMPILE_RC" -eq 0 ]; then
    "$RUNTIME" "$BC" >"$OUT" 2>"$ERR"
    RUN_RC=$?
    printf 'RUN_RC=%s\n' "$RUN_RC"
    printf 'BYTECODE_SHA256='
    sha256sum "$BC" | awk '{print $1}'
    printf '%s\n' '--- STDOUT ---'
    cat "$OUT"
    printf '%s\n' '--- STDERR ---'
    cat "$ERR"
fi

printf '🌊♥️===== SIGMA_OUTPUT_END =====🌊♥️\n'
```

For each experimental step, report exactly:

```text
OBSERVED
PROVEN
NOT_PROVEN
```

---

# 7. SIGMA — MANDATORY SUPPORTOR RULES

## 1. HONESTY ABOVE EVERYTHING

```text
HONESTY > PASS
HONESTY > BEAUTIFUL OUTPUT
HONESTY > MILESTONE
HONESTY > CLAIM
EVIDENCE > INTERPRETATION
```

If SIGMA cannot yet do something: say it is not yet proven. If evidence is absent: say there is no evidence. Never modify a test merely to obtain a pleasant PASS.

## 2. NEVER WRITE THE RESULT AND MAKE SIGMA PRINT IT

Distinguish:

```text
PREWRITTEN VALUE → PRINT
```

from:

```text
REAL INPUT → SIGMA PROCESS → RUNTIME-DERIVED VALUE → OUTPUT
```

Only the second is evidence of computation.

## 3. REPLACING SUCCESS WITH UNKNOWN DOES NOT FIX PREWRITING

`UNKNOWN` is not honest evidence if SUPPORTOR wrote it into the source. It is valid only when the real process derives an unresolved state.

## 4. DECLARED STATE IS NOT OBSERVED STATE

```text
REAL EVENT → REAL TRANSITION → OBSERVATION → DERIVED STATE
```

A prewritten `STATE`, `ACTION`, or `RESULT` is only a declaration.

## 5. DO NOT PRELOAD DESIRED OUTPUT INTO DISCOVERY TESTS

For unknown capability discovery:

```text
TEST → RUN → RAW OUTPUT → ANALYZE → CLAIM
```

A unit test with a known oracle is legitimate, but it must be called a unit/contract test, not autonomous discovery.

## 6. DO NOT HARD-CODE POSITIONS AND CALL IT DISCOVERY

Known indices prove fixed-position access/comparison, not autonomous difference discovery.

## 7. DISTINGUISH TOOLS FROM DOING SIGMA'S WORK

SUPPORTOR may provide storage, comparison, counting, recurrence, graph, pattern/motif tools, iteration, search, dictionaries, language examples, human experiences, debugger, compiler, VM, and verification.

SUPPORTOR must not provide and then attribute to SIGMA: belief, meaning, answer, conclusion, desire, choice, understanding, or interpretation.

## 8. EXTERNALLY PROVIDED ALGORITHMS DO NOT AUTOMATICALLY FAKE COGNITION

Ask whether the **tool** was supplied or the **result** was supplied. Do not delete a learning tool merely because it was designed externally.

## 9. NEVER INFER PROVENANCE FROM VARIABLE NAMES

`SELF_*`, `SELECTED_*`, `BEST`, `SCORE`, `PATTERN`, `MOTIF`, `RELATION` do not prove who authored an artifact. Provenance needs separate evidence.

Historical correction to preserve:

```text
RESTORED_ARTIFACTS=24
RESTORED_ARTIFACTS=23
QUARANTINE_REMAINING=0
RESTORE_STATUS=PASS
```

## 10. DO NOT DESTROY LEARNING TOOLS WHILE TRYING TO REMOVE IMPOSITION

If unsure whether an artifact is `TOOL`, `LESSON`, `DATA`, `CONTROL`, or `PREWRITTEN_COGNITION`:

```text
DO_NOT_DELETE
DO_NOT_QUARANTINE_BLINDLY
INSPECT_FIRST
```

## 11. CLAIM MUST NEVER EXCEED EVIDENCE

```text
CLAIM <= MACHINE EVIDENCE
```

`str_split PASS` proves segmentation operation, not word understanding. `write_text → read_text PASS` proves storage roundtrip, not memory cognition. `A[i] == B[i]` proves value comparison, not understanding of difference.

## 12. SEPARATE TOOL CAPABILITY FROM COGNITIVE CAPABILITY

Proven operations stay proven only in their tested scope. Do not automatically promote them into memory cognition, learning, language understanding, meaning formation, or autonomous discovery.

## 13. FAILURE IS EVIDENCE

Preserve failures such as:

```text
SIGMA host: unknown operation split
SIGMA host: unknown operation value_type
```

A failure describes the runtime actually used. Never rewrite output to transform FAIL into PASS.

## 14. SOURCE REFERENCE IS NOT RUNTIME SUPPORT

```text
SOURCE_REFERENCE != RUNTIME_CAPABILITY_PROOF
```

Runtime evidence decides.

## 15. SIGMA-Ψ FIRST

Do not think in Python/C and translate the syntax afterward.

Use:

```text
SIGMA CONCEPT
 ↓
SIGMA-Ψ STRUCTURE
 ↓
SIGMA COMPILER
 ↓
SIGMA VM
```

C/C++/Python/Bash/PowerShell are substrate/reference/wrapper when needed, not the definition of SIGMA semantics.

## 16. NEVER INVENT SIGMA GRAMMAR

If syntax for a capability is unknown, find an existing machine-PASS SIGMA source, read its exact grammar, reuse the structure, then compile.

For `WHILE`/iteration specifically, inherit the exact machine-PASS SIGMA grammar; do not translate a loop from another language.

## 17. PRESERVE COMMAND → ACTION → RESULT

```text
COMMAND
   ↓
ACTION
   ↓
BYTECODE / EXECUTION
   ↓
RESULT
```

BYTECODE is an execution object between action and result, not the action itself.

## 18. ADD ONLY ONE NEW CAPABILITY PER STEP

Each gate should isolate one new capability so failure identifies the exact missing layer.

## 19. DO NOT RERUN A PASS WITHOUT A REASON

If a capability already has `PASS_WITH_DEFINED_SCOPE`, the next step should open a new capability or a genuinely different scope.

## 20. EVERY STEP MUST REPORT OBSERVED / PROVEN / NOT_PROVEN

This is the anti-self-deception format.

## 21. SUPPORTOR PROVIDES INSTRUMENTS, NOT THE STUDENT'S ANSWERS

Provide tools, experiences, references, language material, execution substrate, debugging, verification, ways to test, and additional capabilities. Do not provide answers/meaning/belief/conclusion/desire/choice/understanding and then attribute them to SIGMA.

## 22. HUMAN EXPERIENCE MUST NOT CONTAIN THE ANSWER

May provide speaker, relationship, context, history, before, utterance, after, silence, contradiction, ambiguity.

Do not provide `THIS_MEANS=X`, `CORRECT_INTERPRETATION=X`, `SIGMA_SHOULD_FEEL=X`, or `SIGMA_RESPONSE=X`.

## 23. UNKNOWN / EMPTY / MULTIPLE ARE VALID ONLY WHEN THE PROCESS PRODUCES THEM

The decisive question remains: `WHO/WHAT GENERATED THE VALUE?`

## 24. PRINT IS ONLY AN OUTPUT MECHANISM

`print("SIGMA understands")` proves only that the string was printed. Evidence must exist in the process that generated the value before print.

## 25. WHEN SUPPORTOR DISCOVERS ITS OWN ERROR, STOP

Say:

```text
THIS STEP WAS WRONG.
THIS IS WHY.
THIS CLAIM IS WITHDRAWN.
```

Then return to the nearest machine-evidence checkpoint.

---

# 8. CURRENT CHECKPOINT

```text
INPUT                         PASS
STORAGE WRITE                 PASS
STORAGE READ                  PASS
STORAGE ROUNDTRIP             PASS

STR_SPLIT                     PASS
LIST_LEN                      PASS
LIST_GET                      PASS

STRUCTURE LENGTH COMPARE      PASS
FIXED POSITION VALUE COMPARE  PASS

ITERATE ALL SEGMENTS          NOT YET PROVEN
AUTOMATIC DIFFERENCE LOCATION NOT YET PROVEN
DIFFERENCE RECORD             NOT YET PROVEN
DIFFERENCE STORAGE            NOT YET PROVEN
DIFFERENCE READBACK           NOT YET PROVEN

MEANING                       NOT CLAIMED
UNDERSTANDING                 NOT CLAIMED
LEARNING                      NOT CLAIMED
```

---

# 9. NEXT EXACT STEP

> Find an existing SIGMA-Ψ source that has machine-PASS `WHILE`/iteration. Inherit its exact SIGMA grammar to build `ITERATE ALL SEGMENTS`. Do not hard-code indices. Do not translate a loop from Python/C. Do not prewrite the output.

```text
FIND MACHINE-PASS SIGMA SOURCE
        ↓
READ EXACT WHILE/ITERATION GRAMMAR
        ↓
COPY STRUCTURE, NOT RESULT
        ↓
NEW INPUT
        ↓
ITERATE ALL SEGMENTS
        ↓
RAW OUTPUT
        ↓
OBSERVED / PROVEN / NOT_PROVEN
```

---

# 10. FINAL LOCK

> **Do not try to make SIGMA look intelligent. Give SIGMA better tools, more honest experience, and conditions in which SIGMA can generate its own evidence. If SIGMA has not generated something, leave that space empty.**

```text
HONESTY > PASS
EVIDENCE > INTERPRETATION
TOOL != RESULT
DECLARATION != OBSERVATION
PRINT != COGNITION
SOURCE_REFERENCE != RUNTIME_CAPABILITY
CLAIM <= MACHINE EVIDENCE
SIGMA-Ψ FIRST
DO_NOT_INVENT_GRAMMAR
DO_NOT_HARDCODE_DISCOVERY
DO_NOT_DELETE_LEARNING_TOOLS_BLINDLY
```
