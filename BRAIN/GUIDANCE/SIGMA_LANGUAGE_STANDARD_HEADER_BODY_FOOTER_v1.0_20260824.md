# SIGMA LANGUAGE — STANDARD HEADER / BODY / FOOTER v1.0

**Date:** 2026-08-24  
**Branch:** `SIGMA_LIFE`  
**Direction:** `LANGUAGE_FIRST`  
**Mother language:** `SIGMA-Ψ`  
**Status:** `STANDARD_FORM_CANDIDATE — MUST BE MACHINE-VALIDATED ON ACTIVE COMPILER/RUNTIME`

## 0. Invariants

```text
SIGMA-Ψ FIRST
HOST LANGUAGE = WRAPPER / SUBSTRATE / REFERENCE ONLY
DECLARED METADATA != RUNTIME EVIDENCE
PREWRITTEN VALUE != DERIVED RESULT
DEF / IF / WHILE / RETURN != PURE_MOTHER_LANGUAGE_BY_DEFAULT
MACHINE EVIDENCE > DOCUMENT DESCRIPTION
```

This form has exactly three regions:

```text
HOST HEADER
    ↓
SIGMA BODY
    ↓
HOST FOOTER
```

The host wrapper creates and executes the file. It does not define SIGMA semantics.

---

# 1. STANDARD MASTER FORM

```bash
cd ~/SIGMA/sigma_genesis1

mkdir -p .sigma_exec

# ============================================================
# HEADER — HOST FILE CREATION + SIGMA LANGUAGE HEADER
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

# ============================================================
# BODY — PURE SIGMA BLOCK STRUCTURE
# ============================================================
⟡(Σ.FORM.INPUT) {
    ⚡ SOURCE: "EXAMPLE";
    ⚡ CONTEXT: "EXAMPLE";
}

⟡(Σ.FORM.RELATION) {
    ⚡ RELATION: "OPEN";
    ⚡ PROVENANCE: "PRESERVE";
}

# ============================================================
# END OF SIGMA SOURCE
# ============================================================
EOF

# ============================================================
# FOOTER — COMPILE + RUN
# ============================================================
SRC=".sigma_exec/SIGMA_FORM_FORMAT_EXAMPLE.sigma"
BC=".sigma_exec/SIGMA_FORM_FORMAT_EXAMPLE.sigmab"

./native/sigmac "$SRC" "$BC" && \
./native/sigma-vm.v09_candidate "$BC"
```

---

# 2. HEADER CONTRACT

The HEADER has two layers.

## 2.1 Host header

```bash
cd ~/SIGMA/sigma_genesis1
mkdir -p .sigma_exec
cat > .sigma_exec/<FILE_NAME>.sigma <<'EOF'
```

This is a host execution wrapper only.

## 2.2 SIGMA file header

```sigma
#SIGMAUNIVERSE_LANGUAGE[DOMAIN=<DOMAIN.NAME>][VERSION=<VERSION>]
```

Then one metadata block:

```sigma
⟡(Σ.SOURCE.IDENTITY) {
    ⚡ TITLE: "<TITLE>";
    ⚡ DOMAIN: "<DOMAIN.NAME>";
    ⚡ VERSION: "<VERSION>";
    ⚡ SOURCE: "<SOURCE_PATH>";
    ⚡ BYTECODE: "<BYTECODE_PATH>";
    ⚡ COMPILER: "native/sigmac";
    ⚡ RUNTIME: "native/sigma-vm.v09_candidate";
    ⚡ LANGUAGE: "SIGMA";
    ⚡ PURPOSE: "<PURPOSE>";
}
```

These fields are declared metadata. They are not runtime-derived evidence.

---

# 3. BODY CONTRACT

The default mother-language body uses SIGMA blocks:

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

Placeholders `<...>` are documentation placeholders only. They must be replaced before compilation.

The base form does not require `DEF`, `IF`, `WHILE`, `RETURN`, `FOR`, or `IN`. If a capability needs executable compiler surface syntax, first find an existing machine-PASS SIGMA source and inherit its exact grammar.

Do not write precomputed cognition into the body:

```text
UNDERSTANDING="SUCCESS"
UNDERSTANDING="UNKNOWN"
LEARNED=TRUE
MEANING="..."
CONCLUSION="..."
RESULT="SUCCESS"
```

unless the field is explicitly declared as input/reference metadata rather than a derived result.

---

# 4. FOOTER CONTRACT

Close the heredoc first:

```bash
EOF
```

Then define execution artifacts:

```bash
SRC=".sigma_exec/<FILE_NAME>.sigma"
BC=".sigma_exec/<FILE_NAME>.sigmab"
```

Compile and run:

```bash
./native/sigmac "$SRC" "$BC" && \
./native/sigma-vm.v09_candidate "$BC"
```

`&&` means the VM runs only if compilation succeeds.

For evidence-grade execution, use:

```bash
OUT=".sigma_exec/<FILE_NAME>.stdout"
ERR=".sigma_exec/<FILE_NAME>.stderr"

./native/sigmac "$SRC" "$BC"
COMPILE_RC=$?
printf 'COMPILE_RC=%s\n' "$COMPILE_RC"

if [ "$COMPILE_RC" -eq 0 ]; then
    ./native/sigma-vm.v09_candidate "$BC" >"$OUT" 2>"$ERR"
    RUN_RC=$?
    printf 'RUN_RC=%s\n' "$RUN_RC"
    printf 'BYTECODE_SHA256='
    sha256sum "$BC" | awk '{print $1}'
    printf '%s\n' '--- STDOUT ---'
    cat "$OUT"
    printf '%s\n' '--- STDERR ---'
    cat "$ERR"
fi
```

---

# 5. CLAIM RULE

After execution, report only:

```text
OBSERVED
PROVEN
NOT_PROVEN
```

Never infer cognition from formatting or output alone.

```text
DECLARATION != OBSERVATION
PRINT != COGNITION
SOURCE_REFERENCE != RUNTIME_CAPABILITY
CLAIM <= MACHINE_EVIDENCE
```

---

# 6. CANONICAL SHAPE

```text
HOST HEADER
    cd
    mkdir
    cat > ... <<'EOF'
        ↓
SIGMA HEADER
    #SIGMAUNIVERSE_LANGUAGE
    Σ.SOURCE.IDENTITY
        ↓
SIGMA BODY
    ⟡(Σ....) {
        ⚡ ...: ...;
    }
        ↓
HOST FOOTER
    EOF
    sigmac
    sigma-vm
    evidence capture
```

This is the standard structural form. Machine evidence from the active compiler/runtime remains authoritative over this document.
