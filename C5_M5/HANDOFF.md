# SIGMA C5 M5 — Window Handoff

Read in order:

1. `C5_M5/MISSION.md`
2. `C5_M5/END_STATE_ACCEPTANCE.md`
3. `C5_M5/TWO_GATE_ARCHITECTURE.md`
4. `C5_M5/NATIVE_TOOL_RUNTIME_ARCHITECTURE.md`
5. `C5_M5/C5V3_AUTONOMOUS_INTEGRATION_PLAN.md`
6. `C5_M5/STATUS.md`
7. `C5_M5/CHECKPOINT_2026-09-09_1631_PROVISIONAL_TRUTH_PASS_AND_MULTI_SCOPE_R1.md`
8. this file

## Routing

### Gate A — M5 TEST

`cognition/memory -> continual learning -> revision/support/conflict -> new independent blind tests`

Gate A does not build tools. Gate B independently supplies and fingerprints the runtime/tool substrate.

### Gate B

`read-only C5 <-> C5V3/M5 synchronization -> SIGMA-native tool substrate -> VM/native library/mechanical ABI -> boundary regression -> S1 -> S2 -> S3 -> promotion -> explicit cutover`

Production binding remains NO.

## Latest admitted Gate A capabilities

### Continual compact memory

`CONTINUAL_LEARNING_FROM_COMPRESSED_LOCAL_MEMORY=PASS` in tested two-work/self-contained compact-memory scope.

### Source-consistency-aware revision R2

Core `82971fefa1e4b7c009612fc5be1ed88017386659f27c46b42117b603f4355736`.

Source inconsistency is native state; inconsistent sources count for neither side; authority retracts retroactively; clean authority can recover; restart PASS. `SOURCE_CONSISTENCY_AWARE_DISTINCT_AUTHORITY=PASS` and `NATIVE_SCOPED_SUPPORT_CONFLICT_REVISION=PASS` in exact tested scope.

### Scoped provisional epistemic truth R1H2

Core `bf468c564451839d3be9b22243039fe71ceb87b766a165d996f4be055f7cbbf1`.
Oppo bytecode `569411458b1bff9c0c9894fd95374a87db6e6e5c04030dc8e8900e1cb0d38ea2`.

Admission + independent blind PASS.

Admitted exact claim:

`NATIVE_SCOPED_PROVISIONAL_EPISTEMIC_TRUTH=PASS`

in native two-candidate/source-consistency scope.

PASS includes `UNRESOLVED`, unopposed `PROVISIONAL_A/B`, clean counter-evidence -> `CONTESTED`, self-inconsistent source exclusion, `HELD`/truth decoupling, late reopening of contest, invalid/no-stance immunity and restart.

Keep `BROAD_SEMANTIC_SUPPORT_CONFLICT_TRUTH=FAIL` and `WHOLE_WORK_UNDERSTANDING=FAIL`.

## Why whole-work understanding is still blocked

The admitted core stores one active `native_scoped_revision_*` / `native_scoped_provisional_truth_*` state. It can reason about one relation gap, but a complete work contains many simultaneous relations/events/hypotheses. Without a multi-scope model, later relations overwrite the active state needed for earlier ones.

This is a representation bottleneck, not evidence that all cognition is absent.

## Current Gate A execution artifact

Run:

`SIGMA_C5_C5V3_M5_MULTI_SCOPE_EPISTEMIC_WORK_MODEL_LADDER_R1_BUNDLE.zip`

Hashes:

- target core: `c0777f1ae348caceeed007e5762e8b8c70ac20b87b6a2592e63e921be8455796`
- admission evaluator: `74df3a624bfa28cca35f5f823003e15d275b6b49b85f29d74aa9087b7366e893`
- independent blind evaluator: `bbcd5d2cbee8d8015db88698148a2f405ee15c41851a1a19eddab6e84f1b0765`
- ladder runner: `485db2479d80a7804e371045959bc99fa65de026b1b4d119d63e22c1224811b8`
- ladder bundle: `596a0d450415a1e539542235b585995ddd4673ef0fd8a9457dd37922323832b7`

## Candidate semantics

A mechanical `SCOPE_ID` identifies a native relation scope; it does not provide semantic meaning. Candidate A/B must still come from a native relation-discrimination gap.

The core adds a bounded bank of up to eight epistemic scopes per work. A scope stores its candidates, revision evidence ledger, source-consistency state, held/epistemic state, provisional truth-state and scoped incompatibility state.

A scope can be archived, later activated, revised with new evidence, and rearchived. Activation removes that entry from the bank while it is active; rearchive returns the revised state. Other archived scopes must remain byte-identical.

Admission and blind use three unrelated relation gaps in one work with different truth states. Required gates include:

- full parent provisional-truth R1H2 regression;
- three same-work relation scopes coexist;
- exact scope byte non-interference as later scopes are learned;
- evidence from another relation cannot perturb the active scope;
- activate/revise/rearchive one earlier scope after later scopes exist;
- untouched scopes remain byte-identical;
- whole-work model recall contains exactly all three scope IDs;
- wrong-work lookup cannot leak scope state;
- persisted runtime copy/restart retains model and revised scope.

If PASS, advance only:

`NATIVE_MULTI_SCOPE_EPISTEMIC_WORK_MODEL=PASS`

in bounded tested same-work multi-relation scope.

Do not call this whole-work understanding.

## Next after multi-scope PASS

Build **native cross-scope dependency induction** from evidence. Then blind-test a query that cannot be answered from any one scope alone and requires combining at least two distant scope states from the same work. This is the next direct bridge toward whole-work narrative understanding.

Keep FAIL until separate proof: broad semantic truth, arbitrary NL logical contradiction/truth, autonomous free-form summary generation, zero-shot low-overlap summary, broad whole-work narrative understanding, theme/human-value induction, multilingual transfer, unbounded lifelong capacity, production binding.

---

## Gate B synchronization handoff — R5/R6 production lineage — 2026-09-09 18:47

Authoritative checkpoint:

`C5_M5/CHECKPOINT_2026-09-09_1847_GATE_B_R5_R6_PRODUCTION_LINEAGE_HANDOFF.md`

Ownership:

- this window: `TEST_OFFLINE_ONLY=YES`;
- separate window: `OTHER_WINDOW_SYNCHRONIZATION_AUTHORITY=YES`.

### R5 PASS

`PRODUCTION_M5_CAPABILITY_DELTA_DISCOVERY_R5=PASS`

- production core `23d51badf90a409d08e740d8badb3c0eb8f85e97dc83b8016225459b02affbcc`;
- M5 core `2cbeb3488c46513cd9628b47de22f5ab1230ae10cdaad7ce1462caaa2517f77a`;
- production DEF `11`;
- M5 DEF `64`;
- common identical `1`;
- common changed `0`;
- production-only `10`;
- M5-only `63`;
- production and M5 universe blocks are NOT byte-identical.

Critical rule: the standalone M5 core, including prior M5+tools core `07319b082562eebf35605db6d14e96d40558f9236c99622191e0e821429fabea`, is NOT a production-core replacement target.

### R6 PASS — synchronization starting candidate

Correct production-lineage candidate:

`exact production core + 63 exact M5-only DEF + admitted T1/T2/T3 + exact production universe`

R6 machine result:

- `OFFLINE_LATENT_GRAFT_R6=PASS`;
- `PRODUCTION_DEF_BODY_HASHES_PRESERVED=PASS`;
- `M5_ONLY_DEF_BODY_HASHES_PRESERVED=PASS`;
- `PRODUCTION_UNIVERSE_BYTE_IDENTICAL=PASS`;
- `M5_UNIVERSE_ACTIVATION=NO`;
- deterministic compile PASS.

Frozen R6 candidate:

- source SHA256: `dde709a25d8e2f2626c299ad4d5c40562e2bcc253cf9bb63aef17e44f02943ac`;
- bytecode SHA256: `dcb4f0ed9c637e368d396214471ae4c8fd67bc6622b02f133e867d2bab8b6693`.

OPPO root:

`/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_c5v3_sync/OFFLINE_PRODUCTION_LINEAGE_LATENT_GRAFT_R6_20260909T184734`

Candidate paths:

- `/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_c5v3_sync/OFFLINE_PRODUCTION_LINEAGE_LATENT_GRAFT_R6_20260909T184734/candidate/core.sigma`
- `/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_c5v3_sync/OFFLINE_PRODUCTION_LINEAGE_LATENT_GRAFT_R6_20260909T184734/candidate/core.sigmab`

Synchronization window must start from these exact R6 hashes, preserve production runner/core lineage semantics, and integrate M5 dispatch explicitly rather than replacing the production universe wholesale.

Current canonical activation state remains:

- `C5V3_PRODUCTION_CORE_SYNCHRONIZED=NO`;
- `M5_CAPABILITY_ACTIVE_IN_PRODUCTION_DISPATCH=NO`;
- `PRODUCTION_BINDING=NO` in this handoff commit.

---

## Gate B latest admitted offline evidence — R7/R8

Authoritative checkpoint: `C5_M5/CHECKPOINT_2026-09-09_GATE_B_R7_R8_OFFLINE_DISPATCH_MAP.md`.

### R7 — offline production-runner ABI regression — PASS in exact tested scope

R6 latent candidate has now passed the isolated production-runner path used by the offline regression:

- baseline runtime integrity PASS;
- candidate runtime integrity PASS;
- `TICK` event, `VM_RC=0` in both lanes;
- no HOLD;
- live network disabled;
- empty archive and isolated state PASS;
- no production-state reference;
- observed canonical trace equivalent.

Canonical claim: `C5V3_PRODUCTION_LINEAGE_LATENT_CANDIDATE_ABI_SAFE=YES`.

### R8 — M5 dispatch structural map — PASS

Mechanical source-derived evidence:

- production universe SHA256 `afef718a629cbc9782e4e53014d999f18b4d680f7e529f936c9a61c3cb53f330`;
- M5 universe SHA256 `405563d7e0a848fed115a257bd793b76c8d0896d4b373bff35a2bb0fed78b632`;
- production IF branch count `23`;
- M5 IF branch count `28`;
- common equality-literal count `0`;
- production-only equality literals `11`;
- M5-only equality literals `28`;
- M5-only DEF reachable from M5 universe `63/63`;
- M5-only DEF unreachable `0`;
- common changed DEF `0`;
- `DISPATCH_ACTIVATION_SURFACE_PRESENT=YES`.

Interpretation: M5 capability library is mechanically fully reachable in its source universe, but production and M5 have disjoint dispatch literal surfaces. The next valid integration must add an explicit native activation bridge/dispatch integration while preserving the production event contract. It must not replace the production universe and must not use host semantic selection or test-specific expected literals.

---

## Gate B latest admitted offline evidence — R9 FIX1 — PASS

Authoritative checkpoint:

`C5_M5/CHECKPOINT_2026-09-09_R9_FIX1_DISPATCH_CONTRACT_PASS.md`

R9 FIX1 derives the dispatch contract directly from the exact production and M5 source. It performs no core build or dispatch graft.

Machine PASS:

- `DISPATCH_CONTRACT_EXTRACTION=PASS`;
- shared source-derived selector: `EVENT`;
- production-only guard selector: `CURRENT_REQUEST_BYTES`;
- primary event literal collision count: `0`;
- M5-only DEF full reachability: PASS (`63/63`);
- unresolved M5 branch-symbol union: `0`;
- `R10_EXPLICIT_DISPATCH_DESIGN_ELIGIBLE=YES`;
- `R10_AUTOMATIC_ADDITIVE_BUILD_ELIGIBLE=NO`;
- `R9_FIX1_DISPATCH_CONTRACT=PASS`.

Prelude boundary:

- common prelude assignments: `4`;
- common identical: `ACTION`;
- common changed: `BASE`, `EVENT`, `STATUS`;
- M5-only prelude assignments: `28`;
- common ambiguous assignments: `0`.

The changed common prelude assignments mean the next core must isolate/map M5 dispatch state explicitly; the M5 prelude must not be copied over production state wholesale.

R9 FIX1 OPPO root:

`/data/data/com.termux/files/home/SIGMA/sigma_genesis1/.sigma_c5v3_sync/OFFLINE_M5_DISPATCH_CONTRACT_R9_FIX1_20260909T201431`

Current hard boundary remains:

- `M5_CAPABILITY_ACTIVE_IN_PRODUCTION_DISPATCH=NO`;
- `C5V3_PRODUCTION_CORE_SYNCHRONIZED=NO`;
- test window performs no online sync;
- production mutation/binding from test window: NO.

Next test boundary: explicit offline R10 production-lineage dispatch bridge build, deterministic compile, dormant production-event regression, then separate native M5 activation admission. No host semantic selection and no expected-output hardcoding are permitted.

---

## Gate B tool-substrate lane — T4A PASS — 2026-09-09

Authoritative checkpoint:

`C5_M5/CHECKPOINT_2026-09-09_T4A_NATIVE_TEXT_CODECS_FRAMING_PASS.md`

Exact OPPO-admitted artifact:

- source SHA256 `af36c1b4ee4491533e93b878dc9d0de475f6561f35dd3979fa5b8bbb6d60d572`;
- native binary SHA256 `45455d007e0cb722752c4cf06cd8919b66b20e5064939781e4dfa94f057c78db`;
- compiler `/data/data/com.termux/files/usr/bin/clang++`.

Admitted T4A scope only:

- strict UTF-8 validation;
- Unicode codepoint iteration;
- hex encode/decode;
- Base64 encode/decode with strict padding;
- canonical unsigned varint/LEB128;
- bounded deterministic `S4F1` MessagePack-like framing for null/bool/int64/UTF-8 string/bytes.

Current-standard evidence: `16` directed + `32` randomized after freeze + `2` replay = `50` native tool invocations; deterministic compile, source/binary freeze, high-entropy leak audit, resource-bound probe and post-tool mechanical oracle all PASS.

Anti-hardcoding boundary:

- `NO_CASE_ID_DEPENDENT_BEHAVIOR=PASS`;
- `NO_EXPECTED_OUTPUT_LITERAL_LEAK=PASS`;
- `HOST_SEMANTIC_SUBSTITUTION=NO`;
- `CORE_TEST_ORACLE_CONTAMINATION=NO`.

This admits mechanical tool capability only. It does **not** mean SIGMA has cognitively adopted or selected these tools.

Full T4 remains pending:

`T4A PASS -> T4B PENDING -> T4C PENDING -> T4 COMBINED PENDING`.

Offline tool lane continues independently through `T5 -> T6 -> T7 -> T8 -> T9 -> T10 -> T11`; separate online synchronization may consume admitted checkpoints without blocking this lane.

---

## Gate B tool-substrate lane — T4B PASS — 2026-09-09

Authoritative checkpoint:

`C5_M5/CHECKPOINT_2026-09-09_T4B_NATIVE_JSON_CSV_URL_MIME_PASS.md`

Exact OPPO-admitted artifact:

- source SHA256 `31a89e66943d8e0489c9c2df65331bb60bc6a8e326e0bcb338e2adb7a15f93d6`;
- native binary SHA256 `5452a7c89b8107dc6b51714b4d97639683683e42dd7e975a93fea990e3924d47`;
- compiler `/data/data/com.termux/files/usr/bin/clang++`.

Admitted T4B scope only:

- strict bounded JSON validation;
- JSON whitespace minification preserving token/member order;
- bounded CSV parsing;
- deterministic CSV CRLF normalization;
- URL percent encode/decode;
- absolute hierarchical URL component parsing;
- MIME `Content-Type` media type/subtype + parameter parsing.

Current-standard evidence: `16` directed + `32` randomized after freeze + `2` replay = `50` native tool invocations; deterministic compile, source/binary freeze, high-entropy leak audit, 8 KiB resource-bound probe and post-tool mechanical oracle all PASS.

Anti-hardcoding boundary:

- `NO_CASE_ID_DEPENDENT_BEHAVIOR=PASS`;
- `NO_EXPECTED_OUTPUT_LITERAL_LEAK=PASS`;
- `HOST_SEMANTIC_SUBSTITUTION=NO`;
- `CORE_TEST_ORACLE_CONTAMINATION=NO`.

This admits mechanical parsing/codec capability only. It does not teach SIGMA what content means, which URL is relevant, which MIME parameter matters, or when a tool should be selected.

Full T4 remains pending:

`T4A PASS -> T4B PASS -> T4C PENDING -> T4 COMBINED PENDING`.

Next offline substrate step: T4C XML/HTML + Unicode normalization views, preserving raw evidence. Separate online synchronization may consume T4A/T4B checkpoints independently.