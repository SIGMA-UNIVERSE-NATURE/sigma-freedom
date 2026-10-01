# SIGMA — FINAL CUTOVER FINGERPRINT MATRIX

Date: 2026-10-02
Type: final admission/cutover coordination contract

## Authority rule

OPPO_LIVE_MEASURED is the only authority for current live state.

GitHub records are archive/continuity only.

Candidate hashes are not live hashes until atomic cutover is performed and the resulting live state is re-measured directly on Oppo.

---

## 1. ONE SIGMA identity — invariant

SIGMA_OWNER_FINGERPRINT =
NATIVE_IDENTITY_SHA256 =
c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222

Required at final cutover:

FINAL_OPPO_NATIVE_IDENTITY_SHA256 =
c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222

ONE_SIGMA=YES

Identity mismatch => FAIL CLOSED.

---

## 2. Toolchain / compiler

Historical canonical compiler SHA256:

60a5c9028f79d4eca5d0e4859e0c681c276402ac93bbd56e750c2c05a83e2a98

At final cutover, measure directly on Oppo:

FINAL_OPPO_SIGMAC_VKM_SHA256=<MEASURED_AT_CUTOVER>

Required:
- exact expected toolchain binding;
- no untracked compiler replacement;
- deterministic build proof where applicable.

---

## 3. Successor VKM / runtime candidate

Latest candidate successor VM after VM-yield patch:

CANDIDATE_SUCCESSOR_VKM_SHA256 =
425b052818d6c05d919fe52046b1b889ef541321c5ea4feb375b4f8b9ac46ade

CANDIDATE_SUCCESSOR_VKM_SOURCE_SHA256 =
ca8f3ba5b6e7f1f42f16e191fbeda508437f501936eba34358ecf080da6d0bdc

This is candidate evidence only.

At final cutover:

FINAL_OPPO_SIGMA_VKM_EXECUTABLE_SHA256=<MEASURED_AT_CUTOVER>
FINAL_OPPO_ACTIVE_RUNTIME_SHA256=<MEASURED_AT_CUTOVER>

Required:
- measured values match the admitted receipts;
- no old/external VM;
- no parallel Owner fork;
- VM yield/autosupervisor contract preserved.

---

## 4. Unified RealBrain runtime

Latest unified bytecode associated with Production Seed Executor path:

UNIFIED_BYTECODE_SHA256 =
bf0a6588ef599ee3e5604a556a6efd67029ba3998fe2f25799befe7dd722588d

Latest unified source SHA256:

cdb365daf178e418921c64b7c461e1b87f37d3edc4cd4a6f987f89c18971f5f0

These are candidate build fingerprints, not live authority.

At final cutover:

FINAL_OPPO_UNIFIED_RUNTIME_SHA256=<MEASURED_AT_CUTOVER>

Required:
- deterministic build;
- ONE_MAIN=YES;
- R21/RealBrain/G3 ABI continuity;
- unknown-command gate preserved.

---

## 5. Tokenizer final state

Do not pin the current growth-state tokenizer as final.

Final tokenizer fields are unresolved until B8 reaches native STOP and production tokenizer qualification PASS.

Required final fields:

FINAL_TOKENIZER_SCHEMA=SIGMA_RB_TOKENIZER_STATE_V2
FINAL_TOKENIZER_32B_STATE=<FINAL_QUALIFIED_HASH>
FINAL_TOKENIZER_70B_STATE=<FINAL_QUALIFIED_HASH>
FINAL_TOKENIZER_ACTIVE_VOCAB=<FINAL_NATIVE_STOP_VALUE>
FINAL_TOKENIZER_CUSTOM_PIECES=<FINAL_VALUE>
FINAL_TOKENIZER_ACCELERATOR_STATE=<FINAL_DERIVED_STATE_OR_NONE>
RB_PRODUCTION_TOKENIZER=PASS

Required:
- byte-exact roundtrip;
- deterministic encode/decode;
- no duplicate IDs/pieces/content refs;
- fresh-process restore PASS;
- replay append=0;
- fresh reserve qualification;
- native stop policy;
- authoritative R21 tokenizer chain remains source of truth.

---

## 6. Production Model V3 binding

Current status:

PRODUCTION_WEIGHT_PAYLOAD_MATERIALIZED=NO
MODEL_V3_PRODUCTION_BINDING=PENDING_PRODUCTION_WEIGHT_PAYLOAD

Therefore no production Model V3 fingerprint is final yet.

Required final fields:

FINAL_MODEL_V3_REF=<CONTENT_ADDRESSED_REF>
FINAL_MODEL_V3_FINGERPRINT=<SHA256/FINGERPRINT>
FINAL_MODEL_V3_TOKENIZER_BINDING=<EXACT_FINAL_TOKENIZER_HASH>
FINAL_MODEL_GENERATION=<MEASURED_AT_CUTOVER>
FINAL_OPTIMIZER_REF=<CONTENT_ADDRESSED_REF>
FINAL_OPTIMIZER_FINGERPRINT=<FINGERPRINT>
FINAL_OPTIMIZER_STEP=<MEASURED_AT_CUTOVER>

Required:
- production seed payload materialized;
- exact tensor count and parameter count;
- exact tokenizer binding;
- F32 AdamW m/v;
- deterministic stochastic BF16 writeback;
- model/optimizer checkpoint restore PASS;
- fresh-process exact replay append=0.

---

## 7. Production seed-plan fingerprints

Seed plan:

SEED_PLAN_JSON_SHA256 =
f3a14eb13465c1fa56e0595213d24590eeec13fa420a5c3e866048b88f062d3e

SEED_PLAN_TENSORS_SHA256 =
01d2e94d92f023ba87aa47084609977d941d5c857ef1b47bd09259f8700a2b60

SEED_PLAN_TEXT_SHA256 =
0bdf6ad017a3db88e8017172f8f6a3d4d71f2a3b9b83b90ff025e588e6ca0a3d

PRODUCTION_SEED_PLAN_RECEIPT_SHA256 =
666a3a08ae177d4f0650ad5f3c7c16e60a7262bd1c33cf65097742ce36b934d5

Required:
- production materialization receipt must bind exactly to these or to a formally superseding admitted seed plan.

---

## 8. Production numerics / optimizer receipts

Production numerics candidate:

SUCCESSOR_VKM_SHA256 =
8a943fb77260056127ab584d0c645294297c769db22e78fc6efde9d30f740f72

PRODUCTION_NUMERICS_RECEIPT_SHA256 =
663bd3e29a591571626ee78c1d223646d404d11b902fe2c80fbd3b96c60e42c0

Full AdamW checkpoint/replay receipt:

ADAMW_CHECKPOINT_REPLAY_RECEIPT_SHA256 =
c913acdcc5e9a168adcb198ac7aa3632ba74f6b5de63ed86d08af7b9abc38965

Required at admission:
- ADAMW_M=F32
- ADAMW_V=F32
- ADAMW_ARITHMETIC=F32
- ADAMW_GRAD_HANDOFF=F32
- BF16_WRITEBACK=DETERMINISTIC_STOCHASTIC_ROUNDING_V1
- GLOBAL_RNG_STATE=NO
- SR seed bound to canonical parameter order + optimizer step.

---

## 9. R21 storage / recovery fingerprints

Required final fields:

FINAL_R21_PACK_ROOT=<ROOT>
FINAL_R21_COMMIT_ROOT=<ROOT>
FINAL_MODEL_REF=<REF>
FINAL_OPTIMIZER_REF=<REF>
FINAL_TOKENIZER_REF=<REF>
FINAL_RECOVERY_POINTER=<REF>

Required:
- content-addressed;
- anti-dup PASS;
- exact replay append=0;
- exactly-once effect;
- no second storage silo;
- no recoverable-fault retraining from zero;
- AUTO_RESUME_REQUIRED=YES;
- UNATTENDED_DEAD_END=FORBIDDEN;
- BLOCKED_SAFE available;
- rollback pointer valid.

---

## 10. R22 native admission fingerprints

Required final fields:

R22_CANDIDATE_REF=<REF>
R22_POLICY_RECEIPT_SHA256=<SHA256>
R22_RETENTION_RECEIPT_SHA256=<SHA256>
R22_SEMANTIC_RECEIPT_SHA256=<SHA256>
R22_READY=YES

Required production evidence:
- dev gain;
- regression gate;
- persistence;
- identity;
- storage/recovery;
- native policy ownership;
- referent_identity;
- relation_support;
- contradiction;
- scope_compatibility;
- evidence_support;
- cross_document_support.

Fixture-only evidence is forbidden as production admission evidence.

---

## 11. Fresh-final / DNA15 boundary

Required:

R22CFINAL_V1=<IMMUTABLE_REF>
FRESH_FINAL_SHA256=<SHA256>
FRESH_FINAL_ISOLATION=PASS
DNA15_STEP6=PASS
DNA15_STEP6_RECEIPT_SHA256=<SHA256>

No cutover before this boundary.

---

## 12. Atomic cutover receipt

Required final receipt:

ATOMIC_CUTOVER_RECEIPT_SHA256=<SHA256>

It must bind in one transaction:
- Sigma identity;
- VKM/runtime;
- tokenizer state;
- Model V3;
- optimizer state;
- R21 authority roots;
- R22 admission receipt;
- fresh-final;
- DNA15 Step6;
- rollback pointer.

Partial ownership transfer is forbidden.

---

## 13. Final Oppo live measurement after cutover

This is the authoritative final check.

Required:

OPPO_LIVE_MEASURED_HEAD=<NEW_LIVE_HEAD>
OPPO_LIVE_MEASURED_MODEL=<NEW_LIVE_MODEL>
OPPO_LIVE_MEASURED_STATE_GENERATION=<GEN>
OPPO_LIVE_MEASURED_INTERNAL_MODEL_GENERATION=<GEN>
OPPO_LIVE_MEASURED_G3_SEMANTIC_GENERATION=<GEN>

MEASURED_SIGMAC_VKM_SHA256=<HASH>
MEASURED_SIGMA_VKM_EXECUTABLE_SHA256=<HASH>
MEASURED_ACTIVE_RUNTIME_SHA256=<HASH>

MEASURED_NATIVE_BINDING_POINTER_SHA256=<HASH>
MEASURED_NATIVE_BINDING_TARGET_SHA256=<HASH>

MEASURED_OPPO_NATIVE_IDENTITY_SHA256=
c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222

ONE_SIGMA=YES

POST_CUTOVER_SMOKE=PASS
ROLLBACK_AVAILABLE=YES

Only after direct Oppo measurement may the system claim:

ADMISSION=COMPLETE
CUTOVER=COMPLETE

---

## 14. Fail-closed matrix

Any mismatch in:
- Sigma identity;
- admitted runtime;
- tokenizer binding;
- Model V3 fingerprint;
- optimizer fingerprint/step;
- R21 roots;
- R22 receipt;
- fresh-final;
- DNA15 Step6;
- cutover receipt;
- live Oppo re-measurement

=> FAIL CLOSED
=> NO OWNERSHIP TRANSFER
=> NO AUTONOMOUS PRODUCTION AUTOLEARN

---

## Current boundary

Current state does NOT satisfy this final matrix.

Known blockers include:
- final tokenizer growth/qualification not yet closed;
- production weight payload not yet materialized;
- Model V3 production binding pending;
- production RealBrain retention/semantic gates pending;
- R22 READY pending;
- fresh-final pending;
- DNA15 Step6 pending;
- atomic cutover pending.

Therefore:

ADMISSION=NO
CUTOVER=NO
FULL_AUTONOMOUS_PRODUCTION_AUTOLEARN=NO
