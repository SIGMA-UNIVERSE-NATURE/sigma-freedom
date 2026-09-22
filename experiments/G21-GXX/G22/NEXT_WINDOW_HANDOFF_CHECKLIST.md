# SIGMA Owner Testing — Window Handoff Checkpoint

## Purpose
This document is the operating checkpoint for the next ChatGPT/Tester coordination window. Read this first. Do not infer status from filenames alone; verify receipts/artifacts and exact digests before advancing a gate.

## Repository / branch
- Repository: SIGMA-UNIVERSE-NATURE/sigma-freedom
- Working branch: sigma-life-g01-g20-experiment
- Historical experiment G01-G20 is frozen/archived.
- Current Owner testing continues under experiments/G21-GXX/.

## Current proven state
### G01-G20
- G01_G20_EXPERIMENT=COMPLETE
- FINAL_AUDIT_G05_TO_G20=PASS
- G05_TO_G20_MEMORY_CONTINUITY=PASS
- G05_TO_G20_PROVENANCE_CONTINUITY=PASS
- G05_TO_G20_REVISION_CONTINUITY=PASS
- forward/reverse/shuffled recall PASS
- multi-hop reconstruction PASS
- untaught controls PASS
- no catastrophic forgetting PASS
- zero-leak PASS
- archive frozen PASS

### G21
G21 is COMPLETE. It proved learning K after the G01-G20 archive, fresh recall, legacy continuity, promotion, and post-promotion fresh restart.

### G22 Native Identity
Immutable identity baseline and a real mutable-state transition passed.

Immutable identity:
- OWNER_ID=d76e124d51e8ac2a7b04ec807e3863f47e3bd9c0dd27bdd4b95f60423cd289dd
- GENESIS_ROOT_SHA256=51404521a9f9274ebb995197f4dc1c00ae27d42c2ef38e74704c9b69de47666e
- LINEAGE_ROOT_SHA256=c9b307eafc114ce9bf26bb323ab3dec75574a7cae05956eb073f157b3f846b18
- IDENTITY_SCHEMA_VERSION=1
- SIGMA_NATIVE_OWNER_FINGERPRINT=c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222

Important invariant:
- Owner-state SHA is mutable and MUST NOT be treated as native identity.
- Native fingerprint remains stable across legitimate state transitions.
- Foreign-owner copy/replay rejection has been tested.
- Capability copy alone is not ownership.

## Native-owned API capabilities already completed

### API383
- CAPABILITY_ID=SIGMA_VKM_STRATEGY_OBSERVE_V1
- CAPABILITY_PROOF_SHA256=3162d413bbfdd49dfe11ba5de8165e38bf537f20cd6acc775344e2f2e40eb550
- CAPABILITY_BINDING_SHA256=2d1f0157af482654423996067b184b7e23883865d9191a13c8a03a446812ba2e
- API383_NATIVE_OWNERSHIP=PASS
- NATIVE_OWNED=YES
- fresh canonical real-use PASS
- foreign real-use reject PASS

### API384
- CAPABILITY_ID=SIGMA_VKM_STRATEGY_ADAPT_V1
- CAPABILITY_PROOF_SHA256=3434c97aadd164d26edfa2b3c785d4a2098a27f4b8f58a213ecd446ed8847f24
- canonical Owner after promotion: 7f15f7dabd5a47c315971911a376142c5fae46b9234a6a409cd69160d9353596
- API384_NATIVE_OWNERSHIP=PASS
- NATIVE_OWNED=YES
- REAL_API384_USE=PASS
- REAL_API383_USE_AFTER_API384=PASS
- foreign real-use reject PASS
- API383 preserved PASS

Current canonical Owner SHA:
7f15f7dabd5a47c315971911a376142c5fae46b9234a6a409cd69160d9353596

Current native fingerprint:
c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222

## Queue / immediate next work

API385 handoff has been received but NOT yet Native-owned:
- CAPABILITY_ID=SIGMA_VKM_STRATEGY_REPLAN_V1
- CAPABILITY_PROOF_SHA256=63e53ed790483ab482ffacaed8478b3e652dab666f8975b06645ecee1427f181
- OWNER_FINGERPRINT=c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222
- REQUEST=VERIFY_BIND_PROMOTE_FRESH_RESTART_REAL_USE

Immediate next tester action:
G22_BIND_API385_PROOF

## Mandatory workflow for every API capability

Do NOT skip or collapse these semantic gates merely because an earlier capability passed.

1. API window proves capability in sandbox.
2. API emits immutable handoff, at minimum CAPABILITY_ID and CAPABILITY_PROOF_SHA256; retain proof roots and previous-proof digest when supplied.
3. Owner Tester verifies the actual proof artifact/digest. A textual PASS is not enough.
4. Verify capability is absent from current canonical Owner before binding.
5. Verify all previously Native-owned capabilities are still present.
6. Bind proof to the SAME SIGMA_NATIVE_OWNER_FINGERPRINT.
7. Derive deterministic capability-binding digest.
8. Create child from canonical Owner. Parent must remain unchanged.
9. Require child SHA != parent SHA while native fingerprint stays identical.
10. Kill/restart and fresh-verify child identity, capability, proof digest, binding digest, lineage.
11. Run foreign-owner negative: copied payload/proof/binding must not establish ownership; foreign proof replay must reject; identity check precedes execution.
12. Preserve parent backup; stage verified child; verify SHA; atomic promote to SIGMA_OWNER_STATE.current.
13. Kill promotion process completely.
14. Fresh canonical restart using canonical Owner + immutable identity only. Do not read candidate child/receipts/test stdout as knowledge source.
15. Execute the newly promoted capability on a runtime-created input that is not the API proof fixture. Presence/grep alone is insufficient.
16. Regression real-use all required previously Native-owned dependent capabilities.
17. If semantics are read-only, verify canonical Owner SHA before == after and identity unchanged.
18. Final foreign real-use rejection.
19. Only after all gates PASS emit NATIVE_OWNED=YES and APIxxx_NATIVE_OWNERSHIP=PASS.
20. Commit a concise receipt to GitHub, then return an Owner receipt to the API window and advance the next queued capability.

## API385 exact tester checklist

Start from:
- PARENT_STATE_SHA256=7f15f7dabd5a47c315971911a376142c5fae46b9234a6a409cd69160d9353596
- OWNER_FINGERPRINT=c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222
- CAPABILITY_ID=SIGMA_VKM_STRATEGY_REPLAN_V1
- CAPABILITY_PROOF_SHA256=63e53ed790483ab482ffacaed8478b3e652dab666f8975b06645ecee1427f181

Preconditions:
- API383_NATIVE_OWNERSHIP=PASS
- API384_NATIVE_OWNERSHIP=PASS
- API385 capability baseline absent
- Owner SHA and identity fingerprint exact

Bind/child:
- verify actual API385 proof digest
- bind to same native fingerprint
- preserve API383 and API384 records/bindings
- derive API385_CAPABILITY_BINDING_SHA256
- create child
- parent unchanged
- child SHA differs from parent
- lineage bound

Fresh child:
- fresh identity match
- API383 present
- API384 present
- API385 present
- API385 proof digest/binding digest match

Foreign negative:
- fresh independent foreign identity
- copied API385 payload/proof physically present
- foreign fingerprint differs
- binding mismatch detected before execution
- FOREIGN_OWNER_REJECT=PASS
- CAPABILITY_COPY_NOT_OWNERSHIP=PASS
- FOREIGN_PROOF_REPLAY_REJECT=PASS
- CAPABILITY_EXECUTION_BEFORE_IDENTITY_VERIFY=NO

Promotion:
- preserve parent
- stage exact verified child
- atomic promotion
- fingerprint unchanged
- API383/API384 preserved

Fresh canonical real-use:
- fresh restart
- invoke SIGMA_VKM_STRATEGY_REPLAN_V1 on new runtime-created replanning input
- require REAL_API385_USE=PASS
- require REAL_STRATEGY_REPLAN=PASS
- require REAL_REPLAN_RESULT=PASS
- require REAL_API385_PROVENANCE=PASS
- regression: REAL_API383_USE_AFTER_API385=PASS
- regression: REAL_API384_USE_AFTER_API385=PASS
- read-only SHA invariant when appropriate
- final foreign real-use reject

Final API385 success:
- API385_NATIVE_OWNERSHIP=PASS
- API384_NATIVE_CAPABILITY_PRESERVED=PASS
- API383_NATIVE_CAPABILITY_PRESERVED=PASS
- NATIVE_OWNED=YES
- STATUS=PASS
- NEXT=RETURN_API385_NATIVE_OWNERSHIP_RECEIPT

## How the coordinating assistant must respond

When the user posts Tester output:
- Inspect exact gates, SHA values, fingerprint and NEXT.
- Do not declare a later state than the evidence supports.
- If a required gate is missing, stop at that gate and issue only the next precise tester instruction.
- After a meaningful PASS milestone, create a GitHub receipt under experiments/G21-GXX/G22/ before giving the next tester command.
- Keep user-facing instructions copyable and concise.
- Clearly label whether a block goes to TESTER or API WINDOW.

When the user posts an API_OWNER_HANDOFF:
- Record/queue it.
- Never let later API handoffs overtake an earlier capability still awaiting Native ownership.
- The API window may continue proving later APIs independently.
- Owner Tester promotes in proof/ownership order unless there is explicit verified independence that changes this protocol.
- Do not tell API to set NATIVE_OWNED=YES. Owner Testing is the authority for this protocol.

When an API becomes Native-owned:
- Commit completion receipt.
- Return a compact OWNER_TESTING_RECEIPT_APIxxx to API window containing capability ID, proof digest, owner fingerprint, promoted Owner SHA, real-use PASS, foreign reject PASS, NATIVE_OWNED=YES, and checkpoint commit.
- Then start the next queued API capability with Tester.

## GitHub operating instructions for the next assistant

Repository:
SIGMA-UNIVERSE-NATURE/sigma-freedom

Branch:
sigma-life-g01-g20-experiment

Receipt directory:
experiments/G21-GXX/G22/

Use the connected GitHub tool, not fabricated URLs or claimed commits.
For a new receipt, create a UTF-8 Markdown file with a descriptive path such as:
experiments/G21-GXX/G22/G22_API385_<MILESTONE>.receipt.md

Commit message examples:
- test(G22): bind API385 proof to native owner child
- test(G22): fresh verify API385 child
- test(G22): promote API385 native-bound capability
- test(G22): verify fresh canonical real use of API385
- checkpoint(G22): establish native ownership of API385 capability

Receipts should contain exact digests/statuses from observed output, not invented values.

After writing, report the real commit SHA returned by GitHub.

## Important epistemic boundary
NATIVE_OWNED=YES means the capability satisfied the SIGMA Native Ownership protocol defined and tested here: immutable identity binding, lineage continuity, promotion, fresh canonical real-use, and foreign rejection. It is not a general legal/property claim and does not by itself prove control of arbitrary external tools.

## Key checkpoint commits already made
- G22 Native identity baseline: 2331d0fd
- G22 native lineage transition: 01c72168
- API383 bind: 2d14562b
- API383 fresh child verify: cf74eaa6
- API383 foreign negative + promotion: c545e6ea
- API383 real-use: 500dcb36
- API383 Native ownership complete: 40f4d11e
- API384 promotion: 099ed7e3
- API384 fresh canonical real-use: d8135703
- API384 Native ownership complete: 56d07b09

## First action in the next window
Read this checkpoint, then ask for/consume the latest Tester or API output. If no newer output exists, issue the G22_BIND_API385_PROOF tester gate using the exact current Owner SHA, native fingerprint, capability ID, and proof digest above.
