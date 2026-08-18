# SIGMA EXPERIMENT LEDGER — 2026-08-18

Status: ACTIVE EXPERIMENTAL CONTINUITY  
Mode: EVIDENCE-FIRST / APPEND-ONLY HISTORY / NO SELF-PASS  
Purpose: Preserve each experimentally verified transition so later results can be compared, classified, and promoted to GitHub without rewriting history.

---

## 0. Recording rules

A result is not promoted because of a filename, claim, design note, or self-report.

Every new step must preserve, where applicable:
- exact source / bytecode / artifact SHA-256;
- exact command or reproducible test procedure;
- return code;
- stdout / stderr or deterministic result digest;
- corpus identity and case counts;
- comparison oracle;
- explicit PASS / HOLD / FAIL / REJECT;
- failure classification;
- mutation boundary;
- whether Foundation / frozen ABI / Phase 2 / canonical / 512 state changed.

Rules:

`REPORT != FACT`  
`CODE != CAPABILITY`  
`TEST NAME != PASS`  
`SELF-REPORT != INDEPENDENT EVIDENCE`  
`INHERITED PROOF != PROOF OF NEW CAPABILITY`

Never delete a real failure from the lineage. Superseded candidates remain evidence.

---

# I. Historical experimental chain

## 1. Self-host compiler foundation

Observed SIGMA language/compiler capabilities include DEF / RETURN, IF / ELSE, WHILE, dynamic variable `⚡`, list / map / bytes / string, function calls, parser / emitter / bytecode writer, recognition of `⟡ Σ ⚡ ⋈`, and `COMPILE_SIGMA()` producing `.sigmab`.

Foundation V7 verified source tree SHA-256:

`fe513c20f4df9077e1d12acaa441dc90dceae566e70640b1b383ff185cf3ada1`

Self-host fixed-point SHA-256:

`2ef3949b93260d64f99d5e407fc20b26aff0b240e972c7521927385d6584a667`

Status: **PASS**

---

## 2. Frozen actual bytecode ABI

Frozen ABI file SHA-256:

`c48c9883c6aedaa1ca7bfbc04b2ad05335040375bed942be73ae3ace9a5b8416`

Actual opcodes:

- `0x01 PUSH_CONST`
- `0x02 POP`
- `0x10 LOAD`
- `0x11 STORE`
- `0x20 UNARY`
- `0x21 BINARY`
- `0x30 CALL`
- `0x31 RETURN`
- `0x40 JUMP`
- `0x41 JUMP_IF_FALSE`
- `0xFF HALT`

Important semantics:

- `OP_BINARY = 0x21`
- `B_ADD = 0x01`
- LOAD: locals → globals
- STORE: main → globals; function → locals

Status: **VERIFIED / FROZEN / UNCHANGED**

---

## 3. Early SIGMA-written VM lineage

### v0.2 — actual-ABI in-memory execution

Artifact: `sigma_vm_core_v0_2_actual_abi.sigma`

Reference: `x=10; y=20; z=x+y; print(z)`

C VM output: `30`  
SIGMA-written VM output: `30`  
Both RC: `0`  
Both stderr: empty

stdout SHA-256:

`f4ccd05b3271c386ee55d9876c7450012a3b361e5065c09dc22075e38b3cc35c`

Status: **PASS_WITH_DEFINED_SCOPE**

Known limitation later found: `BUILD_TEST_PROGRAM()` embedded the test program in the execution path.

### Raw external byte-read capability

Generic substrate additions:
- `read_bytes(path)`
- `bytes_get(bytes,index)`

Observed first bytes:

`83 73 71 77 66 67 48 49` = `SIGMBC01`

Raw-byte output SHA-256:

`3df63d02d06e90a2fdf511093f99d40fab33f259447138195062a44330b5e0ac`

Status:
- READ_BYTES_CAPABILITY = **PASS**
- BYTES_GET_CAPABILITY = **PASS**
- RAW_BYTE_PARITY = **PASS**

### v0.3 — external `.sigmab` decode + execute

External program SHA-256:

`efcd04d2d31731f75faf5703e17d52a496bbdff5059e9108d71c86b4bdb804b9`

C VM: `30`  
SIGMA-written VM: `30`  
Both RC: `0`  
Both stderr: empty

Status: **EXTERNAL_BYTECODE_OUTPUT_PARITY = PASS**

### v0.4 — runtime-selected arbitrary input

Runtime selector: `getenv("SIGMA_VM_INPUT")`

VM bytecode SHA-256:

`9d943aa3aeb2616587ce776ff03dd7b8a4c028919668a9293e1b14f096c35ad1`

Observed examples:
- `10 + 20 → 30`
- `7 + 8 → 15`

C/SIGMA parity: **PASS**

### Deliberate failure discovery before v0.5

- binary → `UNSUPPORTED_BINARY_SUBCODE 2`
- unary → `UNSUPPORTED_EXECUTION_OPCODE 32`
- control → `UNSUPPORTED_BINARY_SUBCODE 16`
- function → `UNSUPPORTED_FUNCTION_SYMBOL 0`

Status: **REAL FAILURES PRESERVED**

### v0.5 — arithmetic / unary / control flow

VM bytecode SHA-256:

`a41aed0465ae388613c7342f8de89a9e062a540e1ce5ac1a8e9f13e7d949ae85`

Observed:
- parity_binary_ops = PASS
- parity_unary = PASS
- parity_if_while = PASS

Historical function frontier remained HOLD.

### Historical v0.6 false-progress correction

`sigma_vm_core_v0_6_function_frames.sigma` was initially source-identical to v0.5:

`V05_V06_SOURCE_IDENTICAL=YES`

and compiled to the same bytecode hash.

Therefore any earlier v0.6 function-PASS claim was withdrawn.

Status: **FALSE PROGRESS CORRECTED / HISTORY PRESERVED**

---

# II. Current verified SIGMA-written VM checkpoint

The historical function-frame frontier has since been surpassed.

Current verified coverage:
- 11 / 11 opcodes
- 3 / 3 unary subops
- 15 / 15 binary subops
- 5 / 5 constant tags

Positive differential corpus: **11 / 11 PASS**

Negative malformed corpus: **SIGMA fail-closed 19 / 19**

C VM malformed agreement: **17 / 19**

Preserved stricter SIGMA divergences:
1. `bad_function_symbol.sigmab` → SIGMA rejects `BAD_SYMBOL_INDEX`
2. `trailing_bytes.sigmab` → SIGMA rejects `TRAILING_BYTES`

The SIGMA candidate is not weakened to match permissive malformed-input behavior.

---

## 4. SIGMA-written VM capability proof

Two-cycle cold-bootstrap fixed point verified.

Cycle 1 and Cycle 2 both reproduce SHA-256:

`2ef3949b93260d64f99d5e407fc20b26aff0b240e972c7521927385d6584a667`

Status:

`SIGMA_WRITTEN_VM_PROOF = PASS`

Boundary:

`FULL_C_FREE_NATIVE_STACK = HOLD`

Reason: a reduced generic C substrate remains for object / I/O / scalar primitives; target opcode decode / dispatch / execution remains in SIGMA-Ψ.

---

# III. Trusted-host boundary reduction

## 5. Reduction #1 — remove `math_floordiv`

Candidate: `v12c`

Source SHA-256:

`9ae630ecdfedc4975215bf91465eb4319061a2eb89019e1e8f874eea07b3a50d`

Bytecode SHA-256:

`f5edf70a99821c680874afd305104a08ffdcda3dff95e4e235e7a5655f3f45c4`

Reduced C adapter source SHA-256:

`2e9e6682168f6f8068df465e882e7f74f23edd74644cfc7ca776591324019a98`

Result:
- `math_floordiv` removed from C adapter source and compiled host binary.
- positive differential 11/11 PASS.
- negative fail-closed 19/19 PASS.
- FLOORDIV semantic stress 17/17 PASS.
- deterministic compile PASS.
- cold bootstrap cycle 1 PASS.
- cold bootstrap cycle 2 PASS.

Static custom trusted-C surface:

**6 → 5 primitives**

Status:

`TRUSTED_HOST_BOUNDARY_REDUCTION_001 = PASS`

---

## 6. Attempted reduction #2 — remove `bytes_f64_le_at`

Candidate: `v13a`

Intent: move IEEE-754 FLOAT64 binary decode into SIGMA-Ψ using raw bytes.

FLOAT64 bit-pattern gate:
- C VM: 14/14 bit-exact
- SIGMA v13a: 11/14 bit-exact

Failures:
- `qnan_payload1`
- `qnan_neg_payload`
- `snan_payload1`

Interpretation: ordinary numeric equivalence is insufficient; NaN payload/signaling bits must be preserved.

Status:

`v13a = REJECT`

`REMOVE_bytes_f64_le_at = HOLD`

---

# IV. Current frontier

Next experiment:

`SIGMA_NATIVE_FLOAT64_BITCAST_CAPABILITY_001`

Objective: derive a SIGMA-native bit-exact bytes ↔ FLOAT64 capability preserving finite values, ±0, subnormals, ±infinity, quiet-NaN payload/sign, and signaling-NaN payloads, without changing the frozen ABI or hiding target execution semantics in C.

Success conditions:
1. bit-pattern stress corpus fully PASS;
2. ordinary positive differential remains 11/11;
3. malformed fail-closed remains 19/19;
4. FLOORDIV stress remains 17/17;
5. two-cycle cold-bootstrap fixed point remains byte-identical;
6. `bytes_f64_le_at` absent from trusted C source and compiled host binary;
7. no Foundation / ABI / Phase 2 / canonical / 512 mutation.

---

# V. Current exact state

`SELF_HOST_COMPILER = PASS`  
`FROZEN_ACTUAL_ABI = VERIFIED_UNCHANGED`  
`SIGMA_WRITTEN_VM_PROOF = PASS`  
`POSITIVE_DIFFERENTIAL = 11/11 PASS`  
`NEGATIVE_FAIL_CLOSED = 19/19 PASS`  
`COLD_BOOTSTRAP_CYCLE_1 = PASS`  
`COLD_BOOTSTRAP_CYCLE_2 = PASS`  
`REMOVE_math_floordiv = PASS`  
`CUSTOM_C_TRUSTED_PRIMITIVES = 5`  
`REMOVE_bytes_f64_le_at = HOLD`  
`SIGMA_NATIVE_FLOAT64_BITCAST_CAPABILITY_001 = NEXT`  
`FULL_C_FREE_NATIVE_STACK = HOLD`  
`PROMOTION = NONE`  
`512_PROMOTION = NONE`  
`CANONICAL_MERGE = NONE`

---

# VI. Incoming-result protocol

For every new experiment, append one evidence record:

```text
EXPERIMENT_ID:
PARENT_CANDIDATE:
CANDIDATE_SOURCE_SHA256:
CANDIDATE_BYTECODE_SHA256:
HOST_ADAPTER_SHA256:
FROZEN_ABI_SHA256:
FOUNDATION_SHA256:

CHANGE:
HYPOTHESIS:
MUTATION_BOUNDARY:

COMMANDS:
RETURN_CODES:
STDOUT:
STDERR:
OUTPUT_SHA256:

POSITIVE_CORPUS:
NEGATIVE_CORPUS:
SPECIAL_STRESS_CORPUS:
COLD_BOOTSTRAP_CYCLE_1:
COLD_BOOTSTRAP_CYCLE_2:

OBSERVED_FAILURE:
FAILURE_CLASSIFICATION:
REGRESSION:

VERDICT: PASS | HOLD | FAIL | REJECT
PROMOTION_ALLOWED: YES | NO
NEXT_EXPERIMENT:
```

GitHub recording policy:
- preserve previous records;
- append new evidence rather than rewriting failed history;
- include exact artifact hashes;
- commit one logically bounded experimental transition at a time;
- never infer capability from filename or source presence;
- never mutate canonical state while another canonical executor owns the mutation lock;
- promote only evidence-backed state.

---

End of checkpoint.

---

# VII. Historical provenance intake — OPPO compact VM handoff

Source file:

`SIGMA_VM_EXPERIMENT_HANDOFF_COMPACT_2026-08-18 (1).md`

Source SHA-256:

`c71eea6337bed4e3805d86599ab683327ee0b7a42349ec57b189c275a12408a9`

Device / environment declared in handoff:

`OPPO / Termux / aarch64`

Main tree declared in handoff:

`~/SIGMA/sigma_genesis1`

Classification:

`HISTORICAL_HANDOFF_ACCEPTED_AS_PROVENANCE`

This handoff is **not** the current frontier. It records an earlier verified state in which:

- v0.2 actual-ABI SIGMA-written VM parity was PASS;
- generic `read_bytes` / `bytes_get` substrate capability was PASS;
- v0.3 external SIGMBC01 decode/execute parity was PASS;
- v0.4 runtime-selected multiple-program parity was PASS;
- v0.5 arithmetic / unary / control-flow parity was PASS within tested scope;
- the function test still failed with `UNSUPPORTED_FUNCTION_SYMBOL 0`;
- the first file labeled v0.6 was discovered to be source-identical to v0.5;
- therefore previous function-frame claims were correctly withheld and `V06_OVERALL=HOLD`.

Important historical correction preserved:

`V05_V06_SOURCE_IDENTICAL=YES`

The handoff's frontier:

`SIGMA VM v0.6 — GENERAL FUNCTION CALL / FRAME / RETURN`

is now **SUPERSEDED BY LATER EXECUTION EVIDENCE**, not contradicted or deleted.

Later verified checkpoints already recorded in this ledger establish:

- general CALL / parameter binding / local frame / RETURN semantics across the frozen ABI corpus;
- positive differential 11/11 PASS;
- malformed fail-closed 19/19 PASS;
- two-cycle SIGMA-written-VM cold-bootstrap fixed point PASS;
- trusted-host reduction #1 PASS (`math_floordiv` removed);
- current frontier `SIGMA_NATIVE_FLOAT64_BITCAST_CAPABILITY_001`.

State handling:

`NO_STATE_DOWNGRADE = TRUE`

`NO_HISTORY_REWRITE = TRUE`

`NO_GITHUB_MUTATION_IN_THIS_INTAKE = TRUE`

Reason for no GitHub mutation in this intake:

The file is being registered as historical provenance. Canonical mutation remains isolated from this verifier flow; GitHub promotion should occur only as a bounded evidence commit when the active mutation policy permits it.

---

# VIII. Historical micro-checkpoint intake — v0.6 rebuild state

Source file:

`SIGMA_VM_CURRENT_STATE_2026-08-18.md`

Source SHA-256:

`d87b64c0757af40f854cc12eea3cc020a9f96dccc1e5f14fc3db425fef1cc52a`

Declared environment:

`OPPO / Termux / aarch64`

Declared tree:

`~/SIGMA/sigma_genesis1`

Declared mode:

`ONE_EXPERIMENT_AT_A_TIME / EVIDENCE_ONLY`

Classification:

`HISTORICAL_MICRO_CHECKPOINT_ACCEPTED`

This file captures a narrower point in the v0.6 rebuild than the current verified state.

At this checkpoint the following prior milestones were already declared verified:

- v0.2 actual ABI basic parity = PASS
- v0.3 external SIGMBC01 load/decode = PASS
- v0.4 runtime-selected multi-input parity = PASS
- v0.5 arithmetic/unary/control parity = PASS

v0.5 bytecode SHA-256:

`a41aed0465ae388613c7342f8de89a9e062a540e1ce5ac1a8e9f13e7d949ae85`

The file preserves the important v0.6 audit correction:

`V05_V06_SOURCE_IDENTICAL=YES`

Pre-patch v0.6 source SHA-256:

`c3190dcb104354c6ae3506a910f96b609e4d54d955af5329805317a428602c51`

Patch state recorded at that moment:

- `VM_NEW_PATCH = APPLIED / SOURCE-VERIFIED`
- `VM_NEW_CHILD_PATCH = APPLIED / SOURCE-VERIFIED`
- `VM_FIND_FUNCTION_PATCH = APPLIED / NOT_YET_SOURCE-INSPECTED`

The checkpoint explicitly withheld claims for:

- GENERAL USER CALL
- ARGUMENT ORDER
- PARAMETER BINDING
- FUNCTION LOCAL FRAME
- OP_RETURN
- RETURN VALUE TO CALLER

and therefore recorded:

`V06_OVERALL = HOLD`

Exact next step at that historical point:

`Inspect the source of VM_FIND_FUNCTION only.`

Explicit prohibition at that point:

`Do not patch VM_CALL or OP_RETURN yet.`

This ordering is preserved as experiment lineage evidence. It demonstrates that the function/return implementation was not accepted merely because code had been inserted.

Current-state handling:

`NO_STATE_DOWNGRADE = TRUE`

`NO_HISTORY_REWRITE = TRUE`

`HISTORICAL_FRONTIER_SUPERSEDED_BY_LATER_EXECUTION_EVIDENCE = TRUE`

The present ledger's later verified state remains authoritative for current capability:

- full frozen opcode-class coverage verified by the current corpus;
- CALL / local frame / RETURN semantics verified in later evidence;
- SIGMA-written VM proof = PASS;
- two-cycle cold-bootstrap fixed point = PASS;
- trusted-host reduction #1 = PASS;
- current frontier remains `SIGMA_NATIVE_FLOAT64_BITCAST_CAPABILITY_001`.

GitHub handling for this intake:

`GITHUB_MUTATION = NONE`

Reason: this intake records provenance only. It does not by itself constitute a new capability transition requiring canonical promotion.

