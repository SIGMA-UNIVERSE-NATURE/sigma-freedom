# SIGMA PROGRAMMER ABI CATALOG — 25 PRACTICAL ABIs — 2026-09-19

ROLE=PROGRAMMER_ABI_CATALOG
REPOSITORY=SIGMA-UNIVERSE-NATURE/sigma-freedom
BRANCH=SIGMA_LIFE
AUDIT_DATE=2026-09-19
AUDIT_SOURCE_HEAD_BEFORE_CATALOG=566475df2e8cb73a956666b3743b5fa273cc7e9e
CLAIM_POLICY=CLAIM<=EVIDENCE

## 0. Important correction: 25 is a programmer subset, not the total ABI count

The current source-level host ABI inventory reports:

```text
HOST_OP_COUNT=93
```

Therefore:

```text
TOTAL_SIGMA_HOST_ABI_SOURCE_OPS=93
THIS_CATALOG_SIZE=25
THIS_CATALOG_IS_PRACTICAL_PROGRAMMER_SUBSET=YES
TOTAL_ABI_EQUALS_25=NO
```

Authoritative source inventory:

- [SIGMA HOST ABI INVENTORY — 2026-09-04 V1](https://github.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/blob/SIGMA_LIFE/SIGMA_PROFESSOR/DESIGN/HOST_ABI_INVENTORY_20260904_V1.md)
- Blob: `73aceec927ee3a8762ecbfc97bdd11f594a3cfe2`
- Create commit: `fc4b63f092ac43697a4cf7b2623892097e4ade56`
- Follow-up handoff commit recording the 93-op milestone: `105cb9135b9184ccd77fbcf57308a888e80f4682`

Presence in `sigma_vm.c` is source evidence. It is not automatically proof that the currently locked VM binary accepts the operation or that its exact argument/return semantics are characterized.

## 1. Locked programming convention

The native SIGMA sources repeatedly use this host-call wrapper:

```sigma
DEF H(op, a, b, c) {
    RETURN host(op, a, b, c);
}
```

Programming rule:

```text
USE_PROVEN_CALL_SHAPE_WHEN_AVAILABLE=YES
DO_NOT_GUESS_ARGUMENT_MEANING=YES
DO_NOT_INFER_SOURCE_PRESENCE_AS_LOCKED_RUNTIME_SUPPORT=YES
HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN
HOST_COGNITION=NO
```

Locked toolchain identities used by the admitted learning/runtime lane:

```text
SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
SIGMA_VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

## 2. Evidence grades

```text
A = DIRECT_OR_RECORDED_RUNTIME_PROOF
    Direct locked-runtime PASS or explicitly recorded verified capability.

B = RUNTIME_EXERCISED_IN_PASSING_NATIVE_PROGRAM
    Exact call shape appears in a native source whose tested execution completed PASS in the cited scope.
    This does not automatically freeze every edge case or universal semantic detail.

C = SOURCE_PRESENT_ONLY
    Operation exists in the inspected sigma_vm.c source inventory, but exact current locked-runtime
    availability/signature/return semantics are not proven by the cited evidence.
```

## 3. Practical programmer subset — 25 host ABIs

| # | ABI op | Proven call shape / use | Grade | Safe programmer claim |
|---:|---|---|---|---|
| 1 | `input` | `H("input", "", NULL, NULL)` | A | Interactive input capability is recorded as verified in its tested scope. |
| 2 | `read_text` | `H("read_text", path, NULL, NULL)` | A | Text-file read is verified. Current admitted long-document programs still read whole files; bounded file I/O is not proven. |
| 3 | `write_text` | `H("write_text", path, content, NULL)` | A | Text write is verified. Crash-safe/atomic replacement semantics are not proven. |
| 4 | `append_text` | `H("append_text", path, content, NULL)` | B | Exercised in admitted survey/deep-relearn persistence paths; mid-append crash atomicity remains not proven. |
| 5 | `file_exists` | `H("file_exists", path, NULL, NULL)` | A | Explicit locked-VM runtime PASS in V2.8D.1 selected-work resolution. |
| 6 | `listdir` | `H("listdir", dir, NULL, NULL)` | B | Exercised in the 56-document full-corpus survey PASS. |
| 7 | `time_now` | `H("time_now", NULL, NULL, NULL)` | A | Locked-VM execution proven in tested clock scope. |
| 8 | `time_sleep` | `H("time_sleep", seconds, NULL, NULL)` | A | Locked-VM 2-second minimum progress execution proven in tested scope. |
| 9 | `str_split` | `H("str_split", text, separator, NULL)` | A | Recorded verified capability and heavily exercised by native learners. |
| 10 | `str_join` | `H("str_join", list, separator, NULL)` | B | Exercised by V2.4 production native learning source in a passing fetch->learn cycle. |
| 11 | `str_ends` | `H("str_ends", text, suffix, NULL)` | B | Exercised by V2.5B.2 document survey in admitted 56-document scope. |
| 12 | `str_replace` | `H("str_replace", text, old, new)` | B | Exercised by admitted survey/deep-relearn native sources. |
| 13 | `list_new` | `H("list_new", NULL, NULL, NULL)` | B | Exercised by production/native learning and survey programs. |
| 14 | `list_len` | `H("list_len", list, NULL, NULL)` | A | Recorded verified capability. |
| 15 | `list_get` | `H("list_get", list, index, NULL)` | A | Recorded verified capability. |
| 16 | `list_push` | `H("list_push", list, value, NULL)` | B | Exercised by passing native learning/survey programs. |
| 17 | `list_sort` | `H("list_sort", list, NULL, NULL)` | B | Exercised by V2.5B.2; deterministic sorted-snapshot behavior is observed in that scope. Universal stability/order semantics are not fully characterized. |
| 18 | `map_new` | `H("map_new", NULL, NULL, NULL)` | B | Exercised by admitted survey/deep-relearn relation counting. |
| 19 | `map_has` | `H("map_has", map, key, NULL)` | B | Exercised by admitted survey/deep-relearn relation counting. |
| 20 | `map_get` | `H("map_get", map, key, NULL)` | B | Exercised by admitted survey/deep-relearn relation counting. |
| 21 | `map_set` | `H("map_set", map, key, value)` | B | Exercised by admitted survey/deep-relearn relation counting. |
| 22 | `read_bytes` | exact argument semantics: `NOT_PROVEN_CURRENT_LOCKED_RUNTIME` | C | Present in source inventory only. Whether offset/count bounded reads exist is explicitly unresolved. |
| 23 | `json_decode` | exact current locked-runtime signature/behavior: `NOT_PROVEN` | C | Present in source inventory only; JSON-family runtime support must be tested per locked VM epoch. |
| 24 | `crypto_digest` | exact algorithms/arguments/output encoding: `NOT_PROVEN` | C | Present in source inventory only. Do not assume SHA-256 call form or hex/raw return format. |
| 25 | `net_fetch` | exact request/response/scheme/limit semantics: `NOT_PROVEN` | C | Present in source inventory only. Do not assume direct locked-VM network ABI without a dedicated runtime receipt. |

## 4. Evidence for ABI 1–3, 9, 14–15

Current verified-capability note:

- [SIGMA CURRENT VERIFIED CAPABILITIES — 21](https://github.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/blob/SIGMA_LIFE/BRAIN/WORKSTREAMS/SIGMA_PSI/SIGMA_CURRENT_VERIFIED_CAPABILITIES_21_20260826.md)
- Blob: `9db81dd6f9abf07fdfab854e4c1fcd0b12b47c74`

It explicitly records:

```text
INPUT
STORAGE_WRITE
STORAGE_READ
STORAGE_ROUNDTRIP
STR_SPLIT
LIST_LEN
LIST_GET
```

as already proven in their cited test scopes.

Exact storage/input source:

- [SIGMA_SHELL_STORAGE_ROUNDTRIP.sigma](https://github.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/blob/SIGMA_LIFE/BRAIN/EXTRA%20BRAIN_OPPO_24826/.sigma_exec/SIGMA_SHELL_STORAGE_ROUNDTRIP.sigma)
- Blob: `b4139e00b58b73196fdacf5804e52889c0daa55a`

Exact list/split examples:

- [SIGMA_SHELL_SEGMENT_COMPARE.sigma](https://github.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/blob/SIGMA_LIFE/BRAIN/EXTRA%20BRAIN_OPPO_24826/.sigma_exec/SIGMA_SHELL_SEGMENT_COMPARE.sigma)
- Blob: `f58bc7531c862078bf9feb89a2096fcc19cec074`
- [SIGMA_SHELL_SEGMENT_VALUE_COMPARE.sigma](https://github.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/blob/SIGMA_LIFE/BRAIN/EXTRA%20BRAIN_OPPO_24826/.sigma_exec/SIGMA_SHELL_SEGMENT_VALUE_COMPARE.sigma)
- Blob: `e71cdb3c6eca9f0586138bd2a81b0e11c6646e78`

## 5. Evidence for ABI 4–6, 11–13, 16–21

### V2.5B.2 full-corpus survey

Native source:

- [SIGMA_DOCUMENT_SURVEY_V2_5B_2.sigma](https://github.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/blob/SIGMA_LIFE/SIGMA_PROFESSOR/artifacts/SIGMA_DOCUMENT_SURVEY_V2_5B_2.sigma)
- Blob: `613877a2a5d85393a8c6a5c5a8cb9be637c0d24f`

Runtime result:

- [V2.5B.2 FULL-CORPUS DOCUMENT SURVEY — PASS](https://github.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/blob/SIGMA_LIFE/SIGMA_PROFESSOR/CHECKPOINTS/20260905_V25B2_FULL_CORPUS_SURVEY_PASS.md)
- Blob: `6fbbfd64e53306ae03b540846fc4f4d413a88fca`

Observed scope includes:

```text
SNAPSHOT_DOCUMENT_COUNT=56
COMMITTED_SURVEY_COUNT=56
VM_RC=0
NATIVE_STRUCTURAL_FULL_CORPUS_SURVEY=PROVEN_FOR_FROZEN_56_DOCUMENT_SNAPSHOT
PERSISTENT_SURVEY_RESUME_ACROSS_RUNNER_INVOCATIONS=PROVEN_IN_TESTED_SCOPE
HOST_DOCUMENT_SELECTION=NO
HOST_LEARNING=NO
BOUNDED_FILE_IO=NOT_PROVEN
```

The source exercises `listdir`, `list_sort`, `read_text`, `str_split`, `list_len`, `list_get`,
`str_ends`, `str_replace`, `map_new`, `map_has`, `map_get`, `map_set`, `list_new`,
`list_push`, `time_now`, and `append_text` in the admitted program.

### V2.8D.1 selected-work deep re-learn

Native source:

- [SIGMA_SELECTED_WORK_DEEP_RELEARN_V2_8D1.sigma](https://github.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/blob/SIGMA_LIFE/SIGMA_PROFESSOR/artifacts/SIGMA_SELECTED_WORK_DEEP_RELEARN_V2_8D1.sigma)
- Blob: `711d67ba970f877e1e7d87705dfad9a069691ed2`

Runtime result:

- [V2.8D.1 REAL SELECTED WORK -> DEEP RE-LEARN — PASS](https://github.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/blob/SIGMA_LIFE/SIGMA_PROFESSOR/CHECKPOINTS/20260905_V28D1_REAL_SELECTED_WORK_DEEP_RELEARN_PASS.md)
- Blob: `c320098e5cd2d65a740c7d1a57c55ac6fc9b730e`

Explicitly observed:

```text
FILE_EXISTS_LOCKED_VM_RUNTIME=PASS
EVIDENCE_APPEND_RC=0
CURSOR_APPEND_RC=0
DETERMINISTIC_DEEP_EVIDENCE_REPLAY=PASS
MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN
```

## 6. Evidence for ABI 7–8

Native source:

- [SIGMA_V4_NATIVE_SLEEP_CLOCK_PROBE_V4C3T1R3.sigma](https://github.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/blob/SIGMA_LIFE/SIGMA_PROFESSOR/artifacts/SIGMA_V4_NATIVE_SLEEP_CLOCK_PROBE_V4C3T1R3.sigma)
- Blob: `5fe99ed5f0017209676babe7319479c38b14d05d`

Locked-runtime result:

- [V4-C3 T1 R3 — NATIVE SLEEP CLOCK PREFLIGHT PASS](https://github.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/blob/SIGMA_LIFE/SIGMA_PROFESSOR/CHECKPOINTS/20260905_V4C3T1R3_NATIVE_SLEEP_CLOCK_PREFLIGHT_PASS.md)
- Blob: `f90d88a5916165ec23b140856e503212ae4b8b0b`

Exact admitted scope:

```text
LOCKED_SIGMAC_EXECUTION=PASS
LOCKED_VM_EXECUTION=PASS
NATIVE_TIME_NOW_EXECUTION=PASS_IN_SINGLE_INVOCATION_SCOPE
NATIVE_TIME_SLEEP_EXECUTION=PASS_IN_TWO_SECOND_MINIMUM_PROGRESS_SCOPE
VM_RC=0
HOST_TIME_DECISION=NO
HOST_SLEEP=NO
```

## 7. Evidence for ABI 10 and core learning-file patterns

Native V2.4 source:

- [SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sigma](https://github.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/blob/SIGMA_LIFE/SIGMA_PROFESSOR/artifacts/SIGMA_CONTINUOUS_NATIVE_SELF_DIRECTED_V2_4.sigma)
- Blob: `070c81cec4a9be1b2c1b5216d498b514618db87a`

Runtime result:

- [V2.4 PRODUCTION NATIVE FETCH -> LEARN CYCLE PASS](https://github.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/blob/SIGMA_LIFE/SIGMA_PROFESSOR/CHECKPOINTS/20260904_V24_PRODUCTION_NATIVE_FETCH_LEARN_CYCLE_PASS.md)
- Blob: `16d4db7dc7401fc43ca6534e9f3090f146d343c4`

This source shows exact call shapes for `str_join` and the core `read_text/str_split/list_len/list_get/list_new/list_push/write_text` pattern.

## 8. Source-only ABI warning for 22–25

The 93-op source inventory contains:

```text
read_bytes
json_decode
crypto_digest
net_fetch
```

but does not by itself prove exact current locked-runtime semantics.

A concrete version-scope warning already exists:

- [V4-C3 T1 R2 — runtime failure: json_encode unknown](https://github.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/blob/SIGMA_LIFE/SIGMA_PROFESSOR/CHECKPOINTS/20260905_V4C3T1R2_RUNTIME_FAIL_JSON_ENCODE_UNKNOWN.md)
- Blob: `42b3b698f394f6a8b175fa3393822d36425b5364`

Observed on the locked VM in that scope:

```text
SIGMA host: unknown operation json_encode
JSON_ENCODE_AVAILABLE_IN_LOCKED_VM=NO_IN_OBSERVED_SCOPE
```

Therefore programmer windows MUST NOT infer current locked-binary support from source inventory alone.

Required before relying on ABI 22–25:

```text
LOCKED_SIGMAC_HASH_MATCH
LOCKED_VM_HASH_MATCH
EXACT_CALL_SIGNATURE_TEST
POSITIVE_RUNTIME_RECEIPT
NEGATIVE_ARGUMENT_CASE
RETURN_TYPE_OR_ENCODING_CHARACTERIZATION
```

Specific unresolved items from the host inventory:

```text
read_bytes: offset/count bounded-read semantics unknown
json_decode: current locked-runtime availability and exact behavior unknown
crypto_digest: supported algorithms, argument signature, output encoding unknown
net_fetch: schemes, redirects, request/response representation, limits, raw-byte behavior unknown
```

## 9. Native program/file ABIs — separate layer from host(op,...)

These are NOT counted in the 25 host-op subset.

Latest G3B printable ABI evidence:

- [G3B Native Planner / Selector / Summarizer Printable ABI Evidence](https://github.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/blob/SIGMA_LIFE/BRAIN/EVIDENCE/G6/G6_G3B_NATIVE_PLANNER_SELECTOR_SUMMARIZER_PRINTABLE_ABI_20260918.md)
- Blob: `fc59964daba33e3b85bde78c7fdf0a354e82a1f3`

### G3B planner

```text
planner.sigmab SHA256=405dcc52a69844f14dff657dd61b90cc1dba3a3ac1a30def7d5e3e6fd1345127

.sigma_exec/G3B_PLANNER
/input/task.txt
/input/capabilities.txt
/output/status.txt
/output/capability_id.txt
/output/endpoint.txt
/output/discovery_kind.txt
/output/discovery_value.txt
G3B_NATIVE_PLANNER_STATUS
```

### G3B selector

```text
selector.sigmab SHA256=b94dbcb2b02caec47499c086c6398b1b0c0a79c0b887317b52b14bf5b06dc698

.sigma_exec/G3B_SELECTOR
/input/candidates.txt
/state/seen_ids.txt
/output/status.txt
/output/page_id.txt
/output/title.txt
G3B_NATIVE_SELECTOR_STATUS
```

### G3B summarizer

```text
summarizer.sigmab SHA256=65c0e617bec58de5c28379ba513145b6bdcff74cd89899af9fd9056002613987

/input/story.txt
/output/status.txt
/output/summary.txt
/output/summary_mode.txt
G3B_NATIVE_SUMMARIZER_STATUS
```

Boundary:

```text
G3B_PLANNER_RUNTIME=NOT_PROVEN
G3B_SELECTOR_RUNTIME=NOT_PROVEN
G3B_SUMMARIZER_RUNTIME=NOT_PROVEN
```

These are static/printable compiled-artifact interfaces until an exact VM execution receipt binds them.

Latest separate runtime control-plane evidence for native fact-gap/query/source selection:

- [Native Fact-Gap Query Evolution R3F1 FIX2K](https://github.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/blob/SIGMA_LIFE/BRAIN/EVIDENCE/G6/G6_NATIVE_FACT_GAP_QUERY_EVOLUTION_R3F1_FIX2K_20260918.md)
- Blob: `dd13c6e3be534148be3f69bc5d10dd79d9a76899`

This proves native topic/query origination and native source-selector plane only in its exact observed scope; it does not upgrade the three G3B static artifacts to runtime-proven.

## 10. Bytecode ABI — separate serialization/compiler/VM layer

Programmer windows should not confuse `host(op,...)` names with numeric bytecode opcodes.

Authoritative bounded freeze:

- [WINDOW C — SIGMA BYTECODE ABI FREEZE RESULT](https://github.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/blob/SIGMA_LIFE/BRAIN/WORKSTREAMS/SIGMA_PSI/WINDOW_C_BYTECODE_ABI_FREEZE_RESULT_20260826.md)
- Blob: `e683fc134743c1b1fc5f45f04a1a5da3dd8801d1`

Field ledger:

- [WINDOW_C_ABI_FIELD_LEDGER_20260826.tsv](https://github.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/blob/SIGMA_LIFE/BRAIN/EVIDENCE/SIGMA_PSI/WINDOW_C_BYTECODE_ABI/WINDOW_C_ABI_FIELD_LEDGER_20260826.tsv)
- Blob: `3526092a181b55719959ac46b1a047de6f0646e7`

Window C reviewed:

```text
ABI_FIELD_QUESTIONS=61
PURE_BYTE_EXACT_OBSERVATIONS=2
SOURCE_CORRELATED_FIELDS_WITH_BYTE_EVIDENCE=37
UNRESOLVED_FIELDS=22
VM_RUNTIME_LOCALIZED_EXACT_ABI_FIELDS=0
```

Selected exact/source-correlated shapes include:

```text
file prefix: SIGMBC01
constant-count-shaped u32 LE at offsets 12..15
constant-correlated tags: 0x00, 0x02, 0x04
name-table u32 counts/lengths/indices
function record:
  u32 function-name index
  u16 parameter count
  parameter_count * u32 parameter-name index
  u32 instruction count
  instruction bytes

0x01 PUSH_CONST_CORRELATED + u32 constant index
0x02 POP_OR_DISCARD_RESULT_CORRELATED
0x10 LOAD_CORRELATED + u32 name index
0x11 STORE_CORRELATED + u32 name index
0x21 BINARY_CORRELATED + u8 sub-op
0x30 CALL_CORRELATED + u32 callee-name index + u16 argc
0x31 RETURN_CORRELATED
0x40 JUMP_BACKEDGE_CORRELATED + u32 target
0x41 JUMP_IF_FALSE_CORRELATED + u32 target
0xFF HALT_OR_TERMINATOR_CORRELATED

binary sub-op source correlations:
0x01 -> +
0x12 -> <
```

Critical boundary:

```text
SOURCE_CORRELATED_BYTE != VM_RUNTIME_OPCODE_SEMANTICS
STACK_EFFECTS=NOT_PROVEN
EXHAUSTIVE_OPCODE_INVENTORY=NOT_PROVEN
UNIVERSAL_JUMP_TARGET_RULE=NOT_PROVEN
EXACT_RUNTIME_HALT_SEMANTICS=NOT_PROVEN
```

Use the compiler. Do not hand-author new bytecode by extrapolating these numbers.

Historical WS06 audit for background:

- [WS06_BYTECODE_ABI_COMPILER_VM_RESULT.md](https://github.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/blob/SIGMA_LIFE/BRAIN/WORKSTREAMS/SIGMA_PSI/WS06_BYTECODE_ABI_COMPILER_VM_RESULT.md)
- Blob: `683278bd5e868502bdcfc326aa16215930b73151`

Window C is the later bounded bytecode-ABI freeze and should control over older broad formulations.

## 11. Recommended read order for a programming window

```text
1. BRAIN/00_READ_FIRST_SIGMA_DIRECTION.md
2. BRAIN/ABI/SIGMA_PROGRAMMER_ABI_CATALOG_25_20260919.md
3. SIGMA_PROFESSOR/DESIGN/HOST_ABI_INVENTORY_20260904_V1.md
4. exact source example for every ABI you will call
5. exact runtime PASS/receipt for every ABI whose availability matters
6. WINDOW_C bytecode ABI freeze only if touching compiler/bytecode/VM representation
7. G3B printable ABI evidence only if implementing planner/selector/summarizer file contracts
```

## 12. Programmer rules

```text
ANTI_HARDCODE=MANDATORY
HOST_COGNITION=NO
HOST_LEARNING_SUBSTITUTION=NO
HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN
CLAIM<=EVIDENCE

SOURCE_PRESENT != CURRENT_LOCKED_RUNTIME_SUPPORTED
PASSING_PROGRAM != UNIVERSAL_ABI_SEMANTICS
PRINTABLE_TOKEN != RUNTIME_VALUE
SOURCE_CORRELATED_OPCODE != VM_RUNTIME_OPCODE
OLD_PASS != PERMANENT_DESIGN
CAPABILITY_SET != FIXED
```

For new code, prefer Grade A/B ABIs in this catalog. For Grade C operations, add an isolated locked-runtime characterization gate before depending on them.
