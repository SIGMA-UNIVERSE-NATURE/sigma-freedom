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

The test window continues separately with offline R7 production-runner ABI regression. Any superseding failure/candidate must be published as a new checkpoint, never silently relabeled.