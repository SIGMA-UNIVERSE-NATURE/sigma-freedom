# SIGMA G22 Native Ownership — Tester/API/G Handoff Checkpoint

Purpose: exact handoff for a new GPT window working as Tester, API, or G-gate operator. GitHub is documentation/checkpoint only; local Sigma Owner remains canonical.

## Operating rules
- Local root: `$HOME/SIGMA/sigma_genesis1`
- VKM: `$HOME/SIGMA_R7_NEXT_R1/VKM`
- Owner: `$HOME/SIGMA/sigma_genesis1/.sigma_owner/SIGMA_OWNER_STATE.current`
- Immutable identity: `$HOME/SIGMA/sigma_genesis1/.sigma_native/SIGMA_NATIVE_IDENTITY.v1`
- Mutable binding: `$HOME/SIGMA/sigma_genesis1/.sigma_native/SIGMA_NATIVE_BINDING.current`
- NEVER broad-scan/hash the filesystem without explicit operator approval. No recursive multi-million-file `find`, `grep -R`, or mass `sha256sum` by default.
- Work one gate at a time. Prefer exact paths and narrow `sed` ranges.
- Never promote before child verification + foreign-negative gates PASS.
- Ownership sequence: bind -> child -> fresh verify -> foreign negative -> promote -> fresh canonical real-use -> final foreign real-use rejection.
- Do not claim NATIVE_OWNED merely from copied capability metadata.

## Frozen history
- G01-G20 complete/archive frozen.
- G20 final Owner: `51404521a9f9274ebb995197f4dc1c00ae27d42c2ef38e74704c9b69de47666e`
- Archive manifest: `2eb14c08b62b404ad3e5326cd956e8a2643b2222f9342d33ebca124a89116440`
- G21 complete/promoted Owner: `cb32364f0c649bdab1a5a739eb1f289bc06f71774f10b6ad271bff2415e36c99`

## Native identity
- OWNER_ID: `d76e124d51e8ac2a7b04ec807e3863f47e3bd9c0dd27bdd4b95f60423cd289dd`
- GENESIS_ROOT_SHA256: `51404521a9f9274ebb995197f4dc1c00ae27d42c2ef38e74704c9b69de47666e`
- LINEAGE_ROOT_SHA256: `c9b307eafc114ce9bf26bb323ab3dec75574a7cae05956eb073f157b3f846b18`
- IDENTITY_SCHEMA_VERSION=1
- OWNER_FINGERPRINT: `c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222`
- Native identity baseline, tamper controls, foreign controls, and mutable-state separation PASS.

## API383 COMPLETE
- Capability: `SIGMA_VKM_STRATEGY_OBSERVE_V1`
- Proof: `3162d413bbfdd49dfe11ba5de8165e38bf537f20cd6acc775344e2f2e40eb550`
- Input root: `fcccf659919579989263eb6e0630695757161e27264b643adb722f58e9f3a3d0`
- Output root: `69ada5574677626ad26e0f7a886b51f7b9710141e396a838cc26c66135b1a4fa`
- Binding: `2d1f0157af482654423996067b184b7e23883865d9191a13c8a03a446812ba2e`
- Promoted Owner: `33f42d9f603ca0ca1fdd4d596fc04ef9f3401f8425252c28bd1a8753dedb61f9`
- Real `strategy_observe(...)` use PASS; read-only PASS; foreign real-use rejection PASS.
- API383_NATIVE_OWNERSHIP=PASS.

## API384 COMPLETE
- Capability: `SIGMA_VKM_STRATEGY_ADAPT_V1`
- Proof: `3434c97aadd164d26edfa2b3c785d4a2098a27f4b8f58a213ecd446ed8847f24`
- Input root: `3944738ead6a1f25664ddc63c1460d4aadcf85807220c2d128a53d9350e1c83b`
- Output root: `63a195441b80f33b8ceb2fd9daa8fe0c1a4cf1a993e82a1492d584c53b62a97a`
- Binding: `bcbed2106edab5bad11438578c661d7d8fe3973e1b0235a6cf5646a253f6be6d`
- Current canonical Owner: `7f15f7dabd5a47c315971911a376142c5fae46b9234a6a409cd69160d9353596`
- Real `strategy_adapt(...)` use PASS; API383 regression real-use PASS; foreign real-use rejection PASS.
- API384_NATIVE_OWNERSHIP=PASS; API383 preserved.

## API385 CURRENT CHECKPOINT
- Capability: `SIGMA_VKM_STRATEGY_REPLAN_V1`
- Proof: `63e53ed790483ab482ffacaed8478b3e652dab666f8975b06645ecee1427f181`
- Input root: `b7d13396a638777bb40da0d7cbe1c9a61401169d4b21e6833989699be9541c22`
- Output root: `d95a6fd05ac86528a1694d58175734f87d7932eb45bc73936a531e3a865bc32c`
- Binding: `99835519ad43f7126977e5d987b0292660eb9a1bfe4636ee95154362f33e628d`
- Parent/current Owner: `7f15f7dabd5a47c315971911a376142c5fae46b9234a6a409cd69160d9353596`
- Verified child: `$HOME/SIGMA/sigma_genesis1/.sigma_owner/SIGMA_OWNER_STATE.G22.API385.child`
- Verified child SHA: `073b98e19841ff3e4a7a2a7583ad64ac51c8df0d7d8aad2ce94df29820760a3a`
- Fresh child identity/API383/API384/API385/binding/lineage verification PASS.
- API385 foreign-owner negative PASS.
- Canonical Owner unchanged and child unchanged after foreign-negative test.
- IMPORTANT: API385 is NOT promoted yet. `NATIVE_OWNED=NOT_YET` for API385.
- NEXT=`G22_API385_PROMOTION`.

## API385 real semantics
VKM functions: `api_385_strategy()`, `api_385_execution_state(...)`, `api_385_observations(...)`, `api_385_constraints(...)`, `strategy_replan(...)`.
For a runtime failure scenario with failed_action=`implement_core`, status != COMPLETE, and allow_core_v2=TRUE, expected semantic path includes new digest `strategy-385-replan-core-v2`, reason `FAILURE_REPLAN`, revision increment, alternative_selected=TRUE, preserved progress when applicable, constraints enforcement, and provenance kind `strategy_replan_provenance` with api=`385`.

## Exact next procedure: G22_API385_PROMOTION
Use these constants:
```sh
ROOT="$HOME/SIGMA/sigma_genesis1"
OWNER="$ROOT/.sigma_owner/SIGMA_OWNER_STATE.current"
ID="$ROOT/.sigma_native/SIGMA_NATIVE_IDENTITY.v1"
BIND="$ROOT/.sigma_native/SIGMA_NATIVE_BINDING.current"
CHILD="$ROOT/.sigma_owner/SIGMA_OWNER_STATE.G22.API385.child"
BACKUP="$ROOT/.sigma_owner/SIGMA_OWNER_STATE.G22.pre_api385.parent"
PARENT="7f15f7dabd5a47c315971911a376142c5fae46b9234a6a409cd69160d9353596"
CSHA="073b98e19841ff3e4a7a2a7583ad64ac51c8df0d7d8aad2ce94df29820760a3a"
FP="c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222"
B383="2d1f0157af482654423996067b184b7e23883865d9191a13c8a03a446812ba2e"
B384="bcbed2106edab5bad11438578c661d7d8fe3973e1b0235a6cf5646a253f6be6d"
B385="99835519ad43f7126977e5d987b0292660eb9a1bfe4636ee95154362f33e628d"
```
Promotion checklist:
1. Verify Owner=PARENT, child=CSHA, identity=FP.
2. Verify child contains all API383/API384/API385 capability IDs and B383/B384/B385.
3. Copy Owner to BACKUP, chmod non-writable, verify backup=PARENT.
4. Copy child to a temp file and verify temp=CSHA.
5. Atomic `mv` temp -> Owner.
6. Verify Owner=CSHA and identity remains FP.
7. Atomically update mutable binding to BOUND_OWNER_STATE_SHA256=CSHA, parent=PARENT, and retain B383/B384/B385.
8. Output OWNER_G22_API385_PROMOTION=PASS, but DO NOT output API385_NATIVE_OWNERSHIP=PASS yet.
9. NEXT=`G22_API385_FRESH_CANONICAL_REAL_USE`.

## After promotion: mandatory fresh canonical real-use
Fresh process may read canonical Owner + immutable identity + VKM implementation only. Do not read candidate child or prior outputs to manufacture PASS.
Real-use must actually call `strategy_replan(...)` on a runtime-created scenario. Verify semantic result and provenance, not just grep capability metadata.
Required markers should include:
- REAL_API385_USE=PASS
- REAL_STRATEGY_REPLAN=PASS
- REAL_REPLAN_RESULT=PASS
- REAL_API385_PROVENANCE=PASS
- REAL_API383_USE_AFTER_API385=PASS
- REAL_API384_USE_AFTER_API385=PASS
- OWNER_G22_READ_ONLY=PASS if operations are read-only.

Then run final foreign real-use ownership check BEFORE capability execution. Fingerprint mismatch must prevent `strategy_replan` invocation. Require FOREIGN_OWNER_REAL_USE_REJECT=PASS, CAPABILITY_COPY_NOT_OWNERSHIP=PASS, FOREIGN_PROOF_REPLAY_REJECT=PASS, CAPABILITY_EXECUTION_BEFORE_IDENTITY_VERIFY=NO.

Only after those gates may the window emit:
- API385_NATIVE_OWNERSHIP=PASS
- API384_NATIVE_CAPABILITY_PRESERVED=PASS
- API383_NATIVE_CAPABILITY_PRESERVED=PASS
- NATIVE_OWNED=YES

## Role handoff
Tester window: verify SHA invariants, fresh-process behavior, read-only behavior, negative controls, zero leakage, and regression of earlier capabilities.
API window: supply exact capability ID, proof SHA, proof input/output roots, previous-proof link, and exact VKM semantics. Do not invent local artifact paths.
G window: orchestrate Owner child creation, identity-bound capability binding, promotion, lineage continuity, fresh canonical real-use, and final ownership receipt.

Checkpoint state: API383 COMPLETE; API384 COMPLETE; API385 child VERIFIED + FOREIGN NEGATIVE PASS; API385 PROMOTION NOT YET RUN.