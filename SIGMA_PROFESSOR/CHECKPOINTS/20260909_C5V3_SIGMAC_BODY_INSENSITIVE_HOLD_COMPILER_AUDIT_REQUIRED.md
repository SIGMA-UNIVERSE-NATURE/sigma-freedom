# C5V3 SIGMAC body-insensitive compiler HOLD

Date: 2026-09-09 +07
Branch: `SIGMA_LIFE`

## Exact diagnostic evidence

Locked compiler:

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
```

Distinct sources:

```text
R2_SOURCE_SHA256=d7d1153fd6979dff7d119bb5e8187f045b9f8af62e51065cccf95265478fc3a0
R2_SOURCE_BYTES=50488
R2_MAIN_SHA256=4ae00a417b8b07f4a256bb97464f1469d7fcd3382e4651e51050366a0bc5dc6a

R3_FIX1_SOURCE_SHA256=152f5b90033e3ee7a67c8847d95cb6eb6b17ab1f659f079a9533b749e8d0b7d8
R3_FIX1_SOURCE_BYTES=115807
R3_FIX1_MAIN_SHA256=591361ea4de8f7c496fb95c09ab12eb76f9999d5c631ab1ada922e3b07ccea1e
R2_R3_SOURCE_BYTE_IDENTICAL=NO
```

Fresh compile behavior:

```text
R2_FRESH_COMPILE_RC=0
R2_FRESH_COMPILE_BYTES=29
R2_FRESH_COMPILE_SHA256=ae220dac7d620cb7a791e047b66101ff8aa570a91da5c02db853f0b50786501a

R3_FIX1_FRESH_COMPILE_RC=0
R3_FIX1_FRESH_COMPILE_BYTES=29
R3_FIX1_FRESH_COMPILE_SHA256=ae220dac7d620cb7a791e047b66101ff8aa570a91da5c02db853f0b50786501a

R2_R3_FRESH_BYTECODE_BYTE_IDENTICAL=YES
```

Observable active-main counterfactual:

```text
COUNTERFACTUAL_TARGET_COUNT=1
R3_COUNTERFACTUAL_COMPILE_RC=0
R3_COUNTERFACTUAL_COMPILE_BYTES=29
R3_COUNTERFACTUAL_COMPILE_SHA256=ae220dac7d620cb7a791e047b66101ff8aa570a91da5c02db853f0b50786501a
R3_COUNTERFACTUAL_BYTECODE_CHANGED=NO
```

Negative parser control:

```text
NEGATIVE_CONTROL=REMOVE_FINAL_MAIN_BRACE
R3_NEGATIVE_UNBALANCED_COMPILE_RC=0
R3_NEGATIVE_UNBALANCED_REJECTED=NO
R3_NEGATIVE_UNBALANCED_BYTECODE_SHA256=ae220dac7d620cb7a791e047b66101ff8aa570a91da5c02db853f0b50786501a
```

## Classification

```text
SIGMAC_RC0_MEANS_SEMANTIC_COMPILE=NO
SIGMAC_BODY_SENSITIVITY=FAIL
SIGMAC_MAIN_LITERAL_SENSITIVITY=FAIL
SIGMAC_NEGATIVE_SYNTAX_REJECTION=FAIL
CURRENT_29_BYTE_OUTPUT_SEMANTIC_BYTECODE_IDENTITY=NOT_ADMITTED
R3_FIX1_RUNTIME_ADMISSION=NO
RESULT=HOLD_COMPILER_OUTPUT_INSENSITIVE_TO_SOURCE_BODY
```

The present evidence is consistent with a stub/header/container emitter or another compiler path that does not parse/encode the SIGMA program body. The exact implementation is not yet established.

## DEF-count diagnostic correction

The diagnostic printed `R2_DEF_COUNT=0` and `R3_FIX1_DEF_COUNT=0` because its Python regex used an over-escaped whitespace token (`r'^DEF\\s+'`). Those zero counts are a diagnostic-script bug and do not contradict the earlier deterministic R3 construction result `R3_FIX1_DEF_COUNT=176`.

## Consequences for prior claims

Historical `sigmac RC=0` / 29-byte file freezes are not sufficient evidence of executable semantic compilation.

Do not automatically erase prior runtime/counterfactual capability PASS results: their actual execution path must be re-audited. If the VM or harness consumed source or another artifact directly, some behavioral evidence may remain valid. If the 29-byte artifact was assumed to carry the program body, that assumption is now unproven.

## Repository audit

`SIGMA_LIFE` does not expose a `native/` compiler/VM source tree or bytecode specification. `CORE/` contains only small SIGMA identity/principles source files. The locked compiler and VM are therefore machine-local artifacts on Oppo for this audit.

## Next dependency

```text
exact local sigmac/VM binary conformance probe
-> dump exact 29-byte output
-> compile empty/plain/header-only/broken controls
-> export exact sigmac + VM + manifest for binary audit
-> determine real VM input contract / bytecode format
-> repair or replace compiler path
-> compiler negative/counterfactual conformance admission
-> only then resume R3 FIX1 executable admission
```

Production remains unchanged.

```text
VM_EXECUTION=NO
PRODUCTION_BINDING=NO
PRODUCTION_MUTATION=NO
CLAIM_LEQ_EVIDENCE=MANDATORY
```
