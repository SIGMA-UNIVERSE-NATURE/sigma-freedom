# SIGMA ONE SIGMA — R18 SPECIAL NOTES

Purpose: separate technical/research notes associated with R18 that must not be confused with canonical continuity claims. GitHub is an archive, not the live OPPO SIGMA HEAD.

## VELA L1 — Experimental Gradient Core Integration Note

Evidence date: 2026-10-11. Basis: user-supplied Termux source inspection and local integration output; not an independent audit.

### Standalone VELA module identity

- File: `SIGMA_VELA_L1_GRADIENT_CORE_R20261011_A.sigma`
- SHA256: `e907d0f641258653026ca1e3328fd092195bcd8c8bcdbc350ac361bb545d04d5`
- Size: 60 lines / 2880 bytes.
- Functions: `VELA1_gradient_chunk`, `VELA1_merge`, `VELA1_finish`.
- Before integration, targeted inspection found no existing `DEF VELA1_` functions in the ARCH8 P0 source.

### Module semantics supported by supplied source

The module is explicitly labeled an experimental additive core with no training, optimizer mutation, checkpoint publication, or activation.

`VELA1_gradient_chunk` requires current/previous gradients with the same shape and computes bounded streaming sums of squared gradient energy and squared gradient change plus element count, with finite-value guards.

`VELA1_merge` adds partial energy, variation, and counts. Its source comment assigns coverage, ordering, parameter identity, gradient identity, and generation validation to the caller.

`VELA1_finish` converts summed values to mean squared gradient/change, updates EMA states q/r using rho, computes instability through `R14_sqrt(r/(q+eps))`, and computes confidence `1/(1+alpha*u)`. It returns q, r, instability, confidence, and count without modifying model or gradient.

### Local ARCH8 P0 integration evidence

Pre-integration ARCH8 P0 source SHA256: `73cbceb2625ef5081c5b3223bf76f8bd8f216266107af74d0a04a52a502bbed3`.

The integration procedure first required both the expected core SHA and expected VELA SHA, and failed closed if a `VELA1_` definition was already present. It then appended the VELA module and recompiled with the existing `sigmac-vkm`.

Reported result: `VELA_LAYER1_CORE=INTEGRATED`.

Post-integration source SHA256: `8d986dfa472c5cf80e7dd143a7cbc80fe1c8afc855d5affa19a8c111749951d1`.
Post-integration bytecode SHA256: `c4688da4102e91cf6cc5d01fa2baa82c5afc0d82faad401ad0d15b65c405764e`.

Post-integration function locations reported:
- `VELA1_gradient_chunk` line 48823
- `VELA1_merge` line 48845
- `VELA1_finish` line 48858

Existing R41 functions remain present, including `R41_cas_range`, `R41_cas_moment_step`, and `R41_embedding_moment_verify`.

### Claim boundary / coder handoff

This note records local source integration only. No VELA entrypoint invocation, behavioral KAT, training use, optimizer mutation, checkpoint publication, Gen2 creation, admission, activation, or cutover is proven by the supplied evidence. Do not treat the post-integration source identity as canonical merely because compilation succeeded.

Anti-rediscovery: later coders should reuse the recorded VELA module identity, semantics, pre/post source hashes, and integration guard. Do not re-search whether `VELA1_` existed in the pre-integration source unless the referenced source identity changes.


## VELA L1 — Native Dispatch Installed + Runtime KAT PASS

Evidence date: 2026-10-11. Basis: user-supplied Termux compile and native runtime KAT output; special R18 research evidence, not an independent audit and not a canonical activation claim.

- VELA_L1_DISPATCH=INSTALLED
- Source SHA256: `7f5f64e62cf1d369c5ec065dc49616ac9f7275360ea6d8849d19e8b2d59f0c2c`
- Bytecode SHA256: `a6643643227bf63b19e5c0a0a222d65265f293c7cb54dbbd6e89de709bbc1ced`
- Compilation with existing `sigmac-vkm`: PASS reported.
- Runtime command: `RBX_VELA_L1_KAT`
- Runtime engine: existing `sigma-vkm`
- VELA_L1_GRADIENT_ENERGY=PASS
- VELA_L1_GRADIENT_VARIATION=PASS
- VELA_L1_CHUNK_MERGE=PASS
- VELA_L1_EMA=PASS
- VELA_L1_CONFIDENCE=PASS
- VELA_LAYER1_KAT=PASS
- SIGMA_VM_EXIT_CODE=0

Continuity interpretation: VELA L1 now has a reported dispatch path and a successful native runtime KAT covering gradient energy, gradient variation, chunk merge, EMA, and confidence behavior. This supersedes the prior special-note state in which no VELA entrypoint invocation or behavioral KAT had yet been proven.

Anti-rediscovery rule: retain this source/bytecode identity and KAT result. Do not repeat the same VELA L1 KAT unless the VELA implementation, dispatch path, relevant runtime identity, or test contract changes, or a new regression is observed.

Claim boundary: runtime KAT PASS does not establish use in ARCH8 training, optimizer mutation, checkpoint publication, Gen2 creation, model-quality improvement, canonical admission, activation, or cutover. VELA remains recorded in SPECIAL R18 NOTES as experimental/research capability evidence until separately authorized and integrated into a qualifying training/control path.


## VELA L2 — Core Integrated + Native Dispatch/KAT PASS

Evidence date: 2026-10-11. Basis: user-supplied Termux integration, compile, dispatch, and native runtime KAT output; SPECIAL R18 research evidence, not an independent audit or canonical activation claim.

### Integration and dispatch

- VELA_LAYER2_CORE=INTEGRATED
- Dispatch insertion required exactly one existing `RBX_VELA_L1_KAT` anchor and failed closed otherwise.
- New command installed: `RBX_VELA_L2_KAT` → `VELA2_kat()`.
- VELA_LAYER2_DISPATCH=INSTALLED
- Compilation with existing `sigmac-vkm`: PASS reported.
- Post-L2 source SHA256: `0f8f49c3c4d90a2172e77463ccc7ca73b20631b6612ab831df98c54bb88b2676`
- Post-L2 bytecode SHA256: `4db8c0fc0c5a8038c9fd59b6218c0e815dccdcee14d279d4ab53f62193eed6a8`

### Native runtime KAT

Runtime command: `RBX_VELA_L2_KAT`, executed by the existing `sigma-vkm`.

- VELA2_ADAPTIVE_BETA=PASS
- VELA2_MOMENT_UPDATE=PASS
- VELA2_BIAS_PRODUCTS=PASS
- VELA2_DIRECTION=PASS
- VELA2_ZERO_GRADIENT=PASS
- VELA2_STATE_IMMUTABILITY=PASS
- VELA2_ADAPTATION=PASS
- VELA_LAYER2_KAT=PASS
- SIGMA_VM_EXIT_CODE=0

Continuity interpretation: VELA L2 now has reported local source integration, an explicit native dispatch path, successful compilation, and a native runtime KAT covering adaptive beta behavior, moment update, bias products, direction, zero-gradient behavior, state immutability, and adaptation.

Anti-rediscovery rule: retain this source/bytecode identity, dispatch insertion contract, and L2 KAT result. Do not repeat the same L2 discovery/KAT unless implementation, dispatch, runtime identity, or KAT contract changes, or a regression appears.

Claim boundary: this does not establish VELA L2 use in ARCH8 training, optimizer mutation of the qualifying candidate, checkpoint publication, Gen2 creation, model-quality improvement, canonical admission, activation, or cutover. VELA L2 remains SPECIAL R18 experimental/research evidence until separately bound into and qualified by an authorized training/control path.


## VELA L2 — Multi-Step Native KAT PASS

Evidence date: 2026-10-11. Basis: user-supplied Termux dispatch, compile, and native runtime multi-step KAT output; SPECIAL R18 research evidence, not an independent audit or canonical activation claim.

- VELA2_MULTISTEP_DISPATCH=INSTALLED
- Source SHA256: `d0b39004ad6dcd57216e3f6af7e0e09a5abcc41c1fd3ca3290ed4537051f57d1`
- Bytecode SHA256: `c8be6f907a7169b1a21febe0c2e0613a426a4b1edc194933a06fd8ad71411639`
- Compilation with existing `sigmac-vkm`: PASS reported.
- Runtime command: `RBX_VELA_L2_MULTISTEP_KAT`
- Runtime engine: existing `sigma-vkm`
- VELA2_MULTI_STEP_COUNT=PASS
- VELA2_MULTI_BETA_PRODUCTS=PASS
- VELA2_MULTI_STATE_IMMUTABILITY=PASS
- VELA2_MULTI_NUMERIC=PASS
- VELA2_MULTISTEP_KAT=PASS
- SIGMA_VM_EXIT_CODE=0

Continuity interpretation: VELA L2 now has reported multi-step native validation in addition to the previously recorded single-run L2 KAT. The multi-step evidence covers step progression/count behavior, beta-product behavior, preservation of required state immutability, and numeric checks.

Anti-rediscovery rule: retain this source/bytecode identity and multi-step KAT result. Do not repeat the same multi-step validation unless VELA L2 implementation, dispatch, runtime identity, test contract, or relevant state semantics change, or a regression is observed.

Claim boundary: multi-step KAT PASS does not establish use in ARCH8 candidate training, optimizer mutation of the qualifying model, checkpoint publication, Gen2 creation, model-quality improvement, canonical admission, activation, or cutover. VELA L2 remains SPECIAL R18 experimental/research evidence pending separate authorized integration and qualification.


## VELA L3 — Core Integrated + Native Dispatch/KAT PASS

Evidence date: 2026-10-11. Basis: user-supplied Termux integration, compile, dispatch, and native runtime KAT output; SPECIAL R18 research evidence, not an independent audit or canonical activation claim.

### Integration and dispatch

- VELA_LAYER3_CORE=INTEGRATED
- Dispatch insertion required exactly one existing `RBX_VELA_L2_MULTISTEP_KAT` anchor and failed closed otherwise with `FAILED_GATE=VELA3_DISPATCH_ANCHOR`.
- New command installed: `RBX_VELA_L3_KAT` → `VELA3_kat()`.
- VELA_LAYER3_DISPATCH=INSTALLED
- Compilation with existing `sigmac-vkm`: PASS reported.
- Post-L3 source SHA256: `430010ceb0715d7a6d30e6b11692f6b4006fc2256a323ce367a291e5c20d0bf7`
- Post-L3 bytecode SHA256: `f2f91c0a38da7025d6c78af2255fc8134603f84d3676f98d5f37d2b9121ae248`

### Native runtime KAT

Runtime command: `RBX_VELA_L3_KAT`, executed by the existing `sigma-vkm`.

- VELA3_STABLE_NORM=PASS
- VELA3_CHUNK_MERGE=PASS
- VELA3_TRUST_CONTROL=PASS
- VELA3_ZERO_DIRECTION=PASS
- VELA_LAYER3_KAT=PASS
- SIGMA_VM_EXIT_CODE=0

Continuity interpretation: VELA L3 now has reported local source integration, fail-closed dispatch installation, successful compilation, and native runtime KAT coverage for stable norm, chunk merge, trust control, and zero-direction behavior.

Anti-rediscovery rule: retain this source/bytecode identity, dispatch anchor contract, and L3 KAT result. Do not repeat the same L3 discovery/KAT unless implementation, dispatch, runtime identity, test contract, or relevant semantics change, or a regression appears.

Claim boundary: this does not establish VELA L3 use in ARCH8 candidate training, optimizer mutation of the qualifying model, checkpoint publication, Gen2 creation, model-quality improvement, canonical admission, activation, or cutover. VELA L3 remains SPECIAL R18 experimental/research evidence until separately bound into and qualified by an authorized training/control path.


## VELA Unified Shadow — Core Integrated + Native KAT PASS

Evidence date: 2026-10-11. Basis: user-supplied Termux integration, compile, dispatch, and native runtime KAT output; SPECIAL R18 research evidence, not an independent audit or canonical activation claim.

### Integration and dispatch

- VELA_UNIFIED_SHADOW_CORE=INTEGRATED
- Dispatch insertion required exactly one existing `RBX_VELA_L3_KAT` anchor and failed closed otherwise with `FAILED_GATE=VELA4_DISPATCH_ANCHOR`.
- New command installed: `RBX_VELA_UNIFIED_KAT` → `VELA4_kat()`.
- VELA_UNIFIED_DISPATCH=INSTALLED
- Compilation with existing `sigmac-vkm`: PASS reported.
- Post-integration source SHA256: `9e281d7fac3279bb91706fab05486a16528b8cf943cd365cce54a7c857f6f0b3`
- Post-integration bytecode SHA256: `9d9e8a01832eac8005b81014266378f7c062845ca406f718f3127ef34d3b396c`

### Native unified-shadow KAT

Runtime command: `RBX_VELA_UNIFIED_KAT`, executed by the existing `sigma-vkm`.

- VELA4_GRADIENT_INTELLIGENCE=PASS
- VELA4_ADAPTIVE_MOMENTS=PASS
- VELA4_GEOMETRIC_TRUST=PASS
- VELA4_INPUT_IMMUTABILITY=PASS
- VELA_UNIFIED_SHADOW_KAT=PASS
- SIGMA_VM_EXIT_CODE=0

Continuity interpretation: the reported VELA unified shadow layer now combines and validates gradient-intelligence, adaptive-moment, geometric-trust, and input-immutability behavior through a native KAT on the existing SIGMA VM.

Anti-rediscovery rule: retain this source/bytecode identity, dispatch-anchor contract, and unified-shadow KAT result. Do not repeat the same discovery/KAT unless the unified implementation, dispatch path, runtime identity, KAT contract, or relevant semantics change, or a regression appears.

Claim boundary: `VELA_UNIFIED_SHADOW_KAT=PASS` establishes the reported shadow KAT only. It does not establish use in ARCH8 candidate training, optimizer mutation of the qualifying candidate, checkpoint publication, Gen2 creation, model-quality improvement, canonical admission, activation, or cutover. VELA unified remains SPECIAL R18 experimental/research evidence pending separate authorized integration and qualification.


## VELA Layer 4 Selector — Native KAT + Candidate/CAS Contract Inspection

Evidence date: 2026-10-11. Basis: user-supplied Termux compile/runtime output and source inspection; SPECIAL R18 research evidence, not an independent audit or canonical activation claim.

### Selector dispatch and native KAT

- VELA_LAYER4_DISPATCH=INSTALLED
- Source SHA256: `0391497f1236151b303fa71a259945c3fbee7021bfa74721a72d995918d67d32`
- Bytecode SHA256: `a7c0b46b001bb6b4831cfeafc024561c0046221774c2a40628d404e7c2d4554a`
- Compilation with existing `sigmac-vkm`: PASS reported.
- Runtime command: `RBX_VELA_L4_SELECTOR_KAT`
- VELA5_CANDIDATE_RECORD=PASS
- VELA5_SCORE_SELECTION=PASS
- VELA5_RISK_GATE=PASS
- VELA5_HOLD_GATE=PASS
- VELA_LAYER4_SELECTOR_KAT=PASS
- SIGMA_VM_EXIT_CODE=0

### Existing CAS/page and reference primitives

The inspected source shows `I_page` stores text bytes with `U_store(BASE,...)` and requires a non-null handle. `I_readpage` restores through `U_restore(BASE,h)` and requires a non-null result. `I_row` validates row width and kind after restore.

`I_ref(s)` accepts `NONE` or a hex string. This is a syntactic/reference-shape predicate in the supplied excerpt; this note does not treat it as proof that a referenced object exists or is semantically valid.

### VELA candidate record contract

The supplied `VELA5_candidate(id,model_ref,optimizer_ref,evidence_ref,loss,risk,cost)`:
- requires model, optimizer, and evidence refs to satisfy `I_ref`;
- requires loss/risk/cost to be finite and non-negative;
- returns a list containing id, the three refs, the three metrics, and the literal string `VERIFIED`.

Claim discipline: the literal `VERIFIED` field is part of the candidate-record construction shown here. By itself it is not evidence of external attestation, evidence-object validation, checkpoint qualification, or canonical verification.

### Existing evidence/receipt surface

Targeted source inspection found multiple existing evidence/receipt functions across the source, including grounding evidence functions, transaction/contract receipts, SPIA evidence paths, ARCH8 KAT persistence receipt, and R35 receipt. Their mere existence does not prove that VELA Layer 4 currently binds its `evidence_ref` through any specific one of those mechanisms.

Continuity decision: retain the selector KAT and candidate/CAS contract inspection so later coders do not repeat this discovery. The next evidence-binding work, if pursued, must demonstrate the exact semantics and validation path for VELA candidate `evidence_ref` rather than inferring it from `I_ref` or the literal `VERIFIED` marker.

Claim boundary: selector KAT PASS does not establish ARCH8 training integration, optimizer mutation, checkpoint publication, Gen2 creation, model-quality improvement, canonical admission, activation, or cutover. This remains SPECIAL R18 experimental/research evidence.


## VELA Numeric/Evidence Contracts + Existing ARCH8 Restore/Evaluation Surface

Evidence date: 2026-10-11. Basis: user-supplied Termux native KAT output and source inspection; SPECIAL R18 research evidence, not an independent audit or canonical activation claim.

### VELA numeric contract KAT

- VELA7_DECIMAL_SYNTAX=PASS
- VELA7_EXPONENT_SYNTAX=PASS
- VELA7_INVALID_REJECTION=PASS
- VELA7_METRIC_VALIDATION=PASS
- VELA_NUMERIC_CONTRACT_KAT=PASS
- SIGMA_VM_EXIT_CODE=0

### VELA evidence integrity KAT

- VELA6_REF_VALIDATION=PASS
- VELA6_NONE_REJECTION=PASS
- VELA6_NULL_REJECTION=PASS
- VELA6_EVIDENCE_INTEGRITY_KAT=PASS
- SIGMA_VM_EXIT_CODE=0
- VELA_NUMERIC_EVIDENCE_REGRESSION=PASS

These KATs supersede the earlier special-note uncertainty about whether VELA evidence refs had any validation beyond the previously inspected generic `I_ref` candidate-record check, but only to the extent covered by these reported VELA6 tests. Exact evidence-object semantic/attestation binding is not inferred beyond the KAT names/results supplied.

### Existing ARCH8 model/optimizer restore surface

Source inspection confirms `RBARCH8_restore` validates model/profile/manifest binding and parameter count, then restores every model tensor via the existing reference-manifest lookup.

`RBARCH8_model_load` constructs the model from the recorded profile, restores it, and binds the model ref.

`RBARCH8_opt_state_list_new` creates one AdamW state per model parameter and assigns `round_key=i+1`.

`RBARCH8_opt_state_consistent` requires all optimizer states to share the same step, beta1_power, and beta2_power.

`RBARCH8_opt_restore` validates profile and OPT_M/OPT_V manifest binding/counts, restores each M/V tensor, restores scalar step/beta powers into every state, and requires final optimizer-state consistency.

`RBARCH8_opt_step_all` requires a valid model and consistent states, finite positive learning rate and finite gradient scale, matching model/gradient/state counts, scales each gradient to F32, and applies `RB_adamw_step(...,0.9,0.999,lr,1e-8,0.0)` to every parameter before rechecking state consistency.

### Existing loss/evaluation surface

`RBQ_model_loss` restores a model by ref, runs the existing raw forward path, requires finite loss, and returns it.

`RBVE_eval_begin` binds parent and child profiles and requires child generation = parent generation + 1 before creating behavior-evaluation accumulation state.

`RBVE_eval_final` requires completed count/cursor conditions and computes parent mean, child mean, and `gain=child_mean-parent_mean` before producing the behavior report.

### Current inspected source identity

Current reported ARCH8 P0 source SHA256: `1c6c23083cde9951c1d19509d812961a65f1d5f8b587a179b8977df02915fe03`.

### Coder handoff / claim boundary

Retain these VELA numeric/evidence KAT results and existing ARCH8 restore/evaluation primitives; do not rediscover them broadly. Do not infer that VELA is wired into `RBARCH8_opt_step_all`, checkpoint restore, model loss, or RBVE evaluation merely because those functions coexist in the source. Such integration requires an explicit call path plus runtime evidence.

No ARCH8 training integration, qualifying optimizer mutation, Gen2 checkpoint, model-quality improvement, canonical admission, activation, or cutover is established by this block. GitHub SPECIAL R18 remains a research/experimental archive, not the live OPPO SIGMA HEAD.


## VELA9 PEG — Local ARCH8 Source Replacement Record

Evidence date: 2026-10-11. Basis: user-supplied Termux file-identity, compile, backup/copy/compare/move output; SPECIAL R18 research evidence, not an independent audit or production/canonical activation claim.

### Input identities

- VELA9 SIGMA source: `SIGMA_CORE_VELA9_PEG_R20261011_B.sigma`
- VELA9 SIGMA source SHA256: `64afacbcb659e6df557903c407be368447b6f8ec17994b3f3ad007ba4975879d`
- VELA9 VKM meter C source: `SIGMA_VKM_VELA9_METER_R20261011_B.c`
- VKM meter C SHA256: `c4b1fadbfd50f7a5817cc10ca0299b80cc6fc1c80cac27c590462ff1a8850559`

### Compile and local replacement procedure

The VELA9 SIGMA source was successfully compiled with the existing `sigmac-vkm` into `SIGMA_CORE_VELA9_PEG_R20261011_B.sigmab` according to the supplied output.

The local file `/sdcard/Download/SIGMA_ARCH8_P0_SHAPE_FIXED.sigma` was handled as follows:
1. copied with metadata preservation to `SIGMA_ARCH8_P0_SHAPE_FIXED.sigma.backup_pre_vela9`;
2. VELA9 source copied to a `.vela9_pending` path;
3. pending copy compared byte-for-byte with the VELA9 source using `cmp -s`;
4. pending file moved over the local ARCH8 P0 source path with `mv -f`.

Reported marker: `SIGMA_CANONICAL_SOURCE=VELA9`.

Post-replacement SHA256 of the local `SIGMA_ARCH8_P0_SHAPE_FIXED.sigma` path: `64afacbcb659e6df557903c407be368447b6f8ec17994b3f3ad007ba4975879d`, matching the supplied VELA9 source identity.

### Claim discipline / coder handoff

This record establishes the reported replacement of the local /sdcard ARCH8 P0 source file and matching content identity. The marker `SIGMA_CANONICAL_SOURCE=VELA9` is recorded as command output only.

It does NOT by itself establish mutation of the live ONE SIGMA canonical HEAD, owner state, native binding, production runtime selector, admission state, or production activation. No such live-state readback was supplied in this block.

The C file `SIGMA_VKM_VELA9_METER_R20261011_B.c` is identity-recorded only. This block does not establish that it was compiled into, linked into, or used by the existing `sigma-vkm` binary.

Anti-rediscovery: later coders should treat SHA256 `64afacbcb659e6df557903c407be368447b6f8ec17994b3f3ad007ba4975879d` as the reported current content identity of the local ARCH8 P0 source path after this VELA9 replacement, and preserve the `.backup_pre_vela9` recovery fact. Any stronger canonical/VM integration claim requires separate runtime/binary/live-state evidence.


## VELA9 — Test VM Build, Resource Governor KAT, and L1–L8 Regression PASS

Evidence date: 2026-10-11. Basis: user-supplied Termux build/runtime/regression output; SPECIAL R18 research evidence, not an independent audit or canonical VM activation claim.

### VELA9 source and build environment

- Local ARCH8/VELA9 source path reports SHA256 `64afacbcb659e6df557903c407be368447b6f8ec17994b3f3ad007ba4975879d` at the start of this evidence block.
- VELA9 meter C source: `SIGMA_VKM_VELA9_METER_R20261011_B.c`
- Meter C SHA256: `c4b1fadbfd50f7a5817cc10ca0299b80cc6fc1c80cac27c590462ff1a8850559`
- Available build tools reported: Termux `cc`, `clang`, and `gcc`.
- Existing canonical-path executable `$HOME/SIGMA_R7_NEXT_R1/VKM/sigma-vkm` was inspected but not replaced in this block.
- Meter C dependencies include libc/system headers plus curl and OpenSSL headers.
- Existing VKM tree also contains previously existing integration shell scripts; their presence is recorded only and does not prove they were used for this VELA9 build.

### Dedicated VELA9 test VM build

The meter C source identity was fail-closed checked against the expected SHA before build.

Reported build command used `clang -O2 -std=c11` with `-lm -lcurl -lcrypto -lssl` and produced:
`$HOME/SIGMA_R7_NEXT_R1/VKM/sigma-vkm-vela9-test`.

- Test VM SHA256: `ed2849dc666ab80cf44e29a7178affc95c02ed051168494d9575d4a60ca5ff7d`
- VELA9_VKM_BUILD=PASS

This supersedes the earlier special-note boundary that the VELA9 C meter had identity evidence only: it is now reported compiled into a dedicated test VM binary. It does NOT establish replacement or mutation of the existing canonical `sigma-vkm`.

### VELA9 resource governor KAT

Using `sigma-vkm-vela9-test` with the VELA9 bytecode and execution context `SIGMA_MAX_STEPS=2000000000`:

- VELA9_RESOURCE_METER=PASS
- VELA9_UNPROVEN_BOUND_HOLD=PASS
- VELA9_OVERBUDGET_HOLD=PASS
- VELA9_GOVERNOR_KAT=PASS
- SIGMA_VM_EXIT_CODE=0
- VELA9_RUNTIME_KAT=EXIT_SUCCESS

The max-step value is recorded as execution context; it is not treated as a canonical VKM configuration change.

### Regression on the VELA9 test VM

The same dedicated test VM then reported exit-code 0 and PASS for:
- `RBX_VELA_L1_KAT`: energy, variation, chunk merge, EMA, confidence.
- `RBX_VELA_L2_KAT`: adaptive beta, moment update, bias products, direction, zero-gradient, state immutability, adaptation.
- `RBX_VELA_L2_MULTISTEP_KAT`: step count, beta products, state immutability, numeric.
- `RBX_VELA_L3_KAT`: stable norm, chunk merge, trust control, zero direction.
- `RBX_VELA_UNIFIED_KAT`: gradient intelligence, adaptive moments, geometric trust, input immutability.
- `RBX_VELA_L4_SELECTOR_KAT`: candidate record, score selection, risk gate, hold gate.
- `RBX_VELA_EVIDENCE_KAT`: ref validation, NONE rejection, NULL rejection, evidence integrity.
- `RBX_VELA_NUMERIC_KAT`: decimal syntax, exponent syntax, invalid rejection, metric validation.
- `RBX_VELA8_KAT`: ARCH8 forward, cross entropy, numeric integrity, validation engine.

Reported aggregate marker: `VELA9_REGRESSION=EXIT_SUCCESS`.

### Continuity interpretation and anti-rediscovery

VELA9 now has evidence of a separately compiled test VM containing the supplied meter C implementation, a passing resource-governor KAT, and successful regression of the reported VELA L1–L8 KAT suite on that test VM.

Later coders should not rediscover whether the meter C can compile or whether these unchanged KATs pass on test binary SHA `ed2849dc...` unless source/binary/test identities change or a regression occurs.

### Claim boundary

This block does NOT establish that `sigma-vkm-vela9-test` replaced the existing `sigma-vkm`, nor that the canonical VKM binary, ONE SIGMA owner/native binding, production runtime selector, or canonical HEAD was mutated. It also does not establish qualifying ARCH8 training, Gen2 checkpoint creation, admission, activation, or cutover. Any promotion from test VM to canonical VKM requires separate authority, exact binary/prestate binding, regression/rollback controls, and post-mutation readback evidence.


## VELA9 — Test VM Renamed to SIGMA-Vkm-VELA

Evidence date: 2026-10-11. Basis: user-supplied Termux rename and SHA256 readback; SPECIAL R18 research evidence, not an independent audit or canonical VKM promotion claim.

- The previously qualified VELA9 test VM binary was moved/renamed to:
  `$HOME/SIGMA_R7_NEXT_R1/VKM/SIGMA-Vkm-VELA`
- Permissions were set to mode 700.
- Post-rename SHA256: `ed2849dc666ab80cf44e29a7178affc95c02ed051168494d9575d4a60ca5ff7d`
- The post-rename SHA was explicitly compared with the expected binary identity.
- SIGMA_VKM_VELA_RENAME=PASS

Continuity interpretation: binary content identity is unchanged from the previously recorded `sigma-vkm-vela9-test` test VM; only the reported filesystem name/path changed to `SIGMA-Vkm-VELA`.

Anti-rediscovery rule: later coders should treat `SIGMA-Vkm-VELA` SHA256 `ed2849dc...` as the renamed VELA9-qualified test binary and should not rebuild/requalify it solely because of the rename.

Claim boundary: this rename is not evidence that the existing canonical executable `$HOME/SIGMA_R7_NEXT_R1/VKM/sigma-vkm` was replaced, redirected, or mutated. It does not establish ONE SIGMA native-binding change, production runtime selection, canonical activation, admission, or cutover. Promotion requires separate authority and live-state readback.


## VELA9 — Post-Rename Direct Runtime Governor KAT

Evidence date: 2026-10-11. Basis: user-supplied Termux SHA readback and direct runtime output; SPECIAL R18 research evidence, not an independent audit or canonical VKM promotion claim.

- Runtime path: `$HOME/SIGMA_R7_NEXT_R1/VKM/SIGMA-Vkm-VELA`
- SHA256 readback: `ed2849dc666ab80cf44e29a7178affc95c02ed051168494d9575d4a60ca5ff7d`
- SHA matched the expected qualified VELA9 test-VM identity.
- Prior rename marker remained `SIGMA_VKM_VELA_RENAME=PASS`.
- Bytecode invoked: `SIGMA_CORE_VELA9_PEG_R20261011_B.sigmab`
- Command: `RBX_VELA9_KAT`
- VELA9_RESOURCE_METER=PASS
- VELA9_UNPROVEN_BOUND_HOLD=PASS
- VELA9_OVERBUDGET_HOLD=PASS
- VELA9_GOVERNOR_KAT=PASS

Continuity interpretation: the renamed `SIGMA-Vkm-VELA` binary is now reported to execute the VELA9 governor KAT successfully from its new path, preserving both binary identity and the previously qualified governor behavior after rename.

Anti-rediscovery rule: do not repeat rename/path qualification for binary SHA `ed2849dc...` unless the binary/path identity changes or a regression appears.

Claim boundary: this is post-rename runtime qualification of the VELA test binary only. It does not establish replacement or redirection of canonical `sigma-vkm`, ONE SIGMA native-binding mutation, production runtime selection, admission, activation, or cutover.


## VELA9 — Default sigma-vkm Filesystem Promotion Readback

Evidence date: 2026-10-11. Basis: user-supplied Termux prepare/promote/readback output; SPECIAL R18 evidence, not an independent audit and not yet a complete ONE SIGMA canonical handoff proof.

### Reported default-runtime replacement

The qualified VELA binary was copied to `$VKM/sigma-vkm.pending`, mode 700 was applied, and the pending copy was byte-compared with the VELA binary before promotion.

The pending binary was then moved with `mv -f` onto the default executable path `$VKM/sigma-vkm`.

Post-move readback:
- `$VKM/sigma-vkm` SHA256 = `ed2849dc666ab80cf44e29a7178affc95c02ed051168494d9575d4a60ca5ff7d`
- `$VKM/SIGMA-Vkm-VELA` SHA256 = `ed2849dc666ab80cf44e29a7178affc95c02ed051168494d9575d4a60ca5ff7d`
- byte comparison between the two paths succeeded.
- Reported marker: `SIGMA_VKM_VELA_DEFAULT_RUNTIME=PASS`.

Continuity interpretation: unlike the earlier test-only/rename evidence, this block reports an actual filesystem replacement of the default `sigma-vkm` executable path with the previously qualified VELA binary identity `ed2849dc...`, followed by matching SHA and byte-level readback.

### Claim boundary / required handoff evidence

This block proves only the supplied filesystem-path replacement/readback. It does not by itself prove a complete authorized ONE SIGMA production handoff.

No evidence in this block establishes:
- pre/post `.sigma_owner/SIGMA_OWNER_STATE.current` binding;
- pre/post `.sigma_native/SIGMA_NATIVE_BINDING.current` binding;
- production runtime-selector or launcher/watchdog consumption of the new VM identity;
- watchdog restart/postcondition health;
- transaction/authority receipt for this VM promotion;
- rollback artifact/path and tested rollback;
- canonical SIGMA HEAD mutation or preservation readback;
- admission/activation/cutover state.

Therefore `SIGMA_VKM_VELA_DEFAULT_RUNTIME=PASS` is archived as a default-path filesystem promotion marker, not yet as a complete canonical production activation verdict.

Anti-rediscovery: later coders should not re-prove that default `sigma-vkm` and `SIGMA-Vkm-VELA` matched SHA `ed2849dc...` immediately after this reported promotion. Next verification should focus on authority/binding/runtime-consumption/postcondition/rollback evidence.


## VELA10 Planner — KAT, Backward Compatibility, and Local Source Promotion

Evidence date: 2026-10-11. Basis: user-supplied Termux compile/runtime/backward-compatibility and source-promotion output; SPECIAL R18 research evidence, not an independent audit or canonical ONE SIGMA activation claim.

### VELA10 planner identity and KAT

- VELA10 source: `SIGMA_CORE_VELA10_PLANNER_R20261011_C.sigma`
- Source SHA256: `9551d033f84a23166e3e52ad85666a606c1607a31eb6992bc1f359d946021e8a`
- Bytecode SHA256: `93534c7561b225ba9d6373fb776ec90d2e0bff0d7e6a2415e8388f7fe380853c`
- Source identity was fail-closed checked before compilation.
- Compilation with existing `sigmac-vkm`: PASS reported.
- Runtime used `$VKM/SIGMA-Vkm-VELA`.
- Command: `RBX_VELA10_KAT`.
- VELA10_UNPROVEN_HOLD=PASS
- VELA10_COMPLETE_CURSOR=PASS
- VELA10_BOUNDED_PLAN=PASS
- VELA10_BUDGET_HOLD=PASS
- VELA10_PLANNER_KAT=PASS
- SIGMA_VM_EXIT_CODE=0

### Backward compatibility on VELA VM

Using the VELA10 bytecode on `SIGMA-Vkm-VELA`, the supplied regression reran:
- `RBX_VELA9_KAT`: resource meter, unproven-bound HOLD, overbudget HOLD, governor KAT all PASS.
- `RBX_VELA8_KAT`: ARCH8 forward, cross entropy, numeric integrity, validation-engine KAT all PASS.

Reported aggregate marker: `VELA10_BACKWARD_COMPATIBILITY=PASS`.

This is backward-compatibility evidence for the reported VELA8/VELA9 KAT surfaces only; it is not a complete regression of every SIGMA/SIA capability.

### Local ARCH8 source promotion VELA9 → VELA10

Precondition identities were explicitly checked:
- old local ARCH8 source expected SHA: `64afacbcb659e6df557903c407be368447b6f8ec17994b3f3ad007ba4975879d`
- new VELA10 source expected SHA: `9551d033f84a23166e3e52ad85666a606c1607a31eb6992bc1f359d946021e8a`

The old local source was preserved as `SIGMA_ARCH8_P0_SHAPE_FIXED.sigma.backup_pre_vela10`.

The VELA10 source was copied to a pending path, byte-compared with the source, then moved over `SIGMA_ARCH8_P0_SHAPE_FIXED.sigma`.

Post-promotion readback SHA256 of the local ARCH8 P0 source path:
`9551d033f84a23166e3e52ad85666a606c1607a31eb6992bc1f359d946021e8a`.

Reported markers:
- `SIGMA_CANONICAL_SOURCE=VELA10`
- `VELA10_SOURCE_PROMOTION=PASS`

### Continuity / anti-rediscovery

Treat SHA `9551d033...` as the reported current local `/sdcard/Download/SIGMA_ARCH8_P0_SHAPE_FIXED.sigma` content identity after this VELA10 promotion, with the VELA9 source preserved at the reported backup path. Do not repeat VELA10 planner or VELA8/V9 compatibility KATs for unchanged source/bytecode/VM identities unless a regression appears.

### Claim boundary

The `SIGMA_CANONICAL_SOURCE=VELA10` marker records local source-promotion output. It does not by itself establish mutation of ONE SIGMA canonical HEAD, owner state, native binding, production runtime selector, SIA capability bindings, admission, activation, or cutover.

Likewise, `VELA10_BACKWARD_COMPATIBILITY=PASS` covers only the explicitly rerun VELA8 and VELA9 KATs. Existing SIA/other SIGMA capabilities still require their own VM-identity compatibility/rebinding evidence where applicable.


## VELA11/VELA12 — Cursor and CAS Receipt Qualification

Evidence date: 2026-10-11. Basis: user-supplied Termux native KAT and backward-compatibility output; SPECIAL R18 research evidence, not an independent audit or canonical activation claim.

### VELA11 cursor evidence

- Source SHA256: `8759365be69db94c36c9a0be2d2990a80f9c0d8685b404d82d49ed9172dfa429`
- Bytecode SHA256: `b2c4b1dd40b8df61d5bae9515831e51e6637399406a70401e07a7120d0532f7e`
- VELA11_CURSOR_ADVANCE=PASS
- VELA11_STATE_IMMUTABILITY=PASS
- VELA11_UNPROVEN_HOLD=PASS
- VELA11_CURSOR_KAT=PASS
- SIGMA_VM_EXIT_CODE=0
- VELA11_CAS_RECEIPT_RUNTIME=NOT_TESTED
- VELA11_COST_PROOF=NOT_IMPLEMENTED

### VELA12 CAS receipt identity and KAT

- Source: `SIGMA_CORE_VELA12_CAS_RECEIPT_R20261011_E.sigma`
- Source SHA256: `3255b41d8771494d8061071d2e129ffee59241e1a81cce4d25d1ebeb95e71f92`
- Bytecode SHA256: `27afcb1322640287a4b29c7bf07c32bfd1094cdb64f16410390d4f899b525893`
- Source identity was fail-closed checked before compilation.
- Runtime used `$VKM/SIGMA-Vkm-VELA`.
- Command: `RBX_VELA12_KAT`.
- VELA12_CAS_RESTORE=PASS
- VELA12_IDENTITY_BINDING=PASS
- VELA12_MISMATCH_REJECTION=PASS
- VELA12_CURSOR_CHAIN=PASS
- VELA12_CAS_RECEIPT_KAT=PASS
- SIGMA_VM_EXIT_CODE=0
- VELA12_INDEPENDENT_EXECUTION_PROOF=NOT_IMPLEMENTED
- VELA12_COST_BOUND_PROOF=NOT_IMPLEMENTED

### VELA12 backward compatibility

Using VELA12 bytecode on `SIGMA-Vkm-VELA`, the reported regression returned exit code 0 for:
- VELA9 governor KAT
- VELA10 planner KAT
- VELA11 cursor KAT
- VELA8 validation-engine KAT

Reported aggregate marker: `VELA12_BACKWARD_COMPATIBILITY=PASS`.

This compatibility claim is limited to the explicitly rerun VELA8–VELA11 KAT surfaces.

### Continuity / anti-rediscovery

VELA12 supersedes the VELA11 state in which CAS-receipt runtime behavior was not tested, to the extent covered by VELA12's CAS restore, identity binding, mismatch rejection, cursor chain, and CAS receipt KAT. Do not rerun unchanged VELA11/12 KATs for the recorded source/bytecode/VM identities absent a regression or changed contract.

### Remaining proof boundaries

The supplied evidence explicitly leaves:
- `VELA12_INDEPENDENT_EXECUTION_PROOF=NOT_IMPLEMENTED`
- `VELA12_COST_BOUND_PROOF=NOT_IMPLEMENTED`

Therefore VELA12 is not yet evidence of independent execution proof or a proved cost bound. It also does not by itself establish qualifying ARCH8 training, Gen2 checkpoint creation, ONE SIGMA native-binding activation, admission, or cutover. Those claims require separate evidence.
