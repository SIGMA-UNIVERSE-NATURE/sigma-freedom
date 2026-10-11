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


## VELA12 — Local ARCH8 Source Promotion

Evidence date: 2026-10-11. Basis: user-supplied Termux backup, pending-copy comparison, promotion, and SHA256 readback; SPECIAL R18 evidence, not an independent audit or ONE SIGMA canonical activation claim.

### Reported source promotion

Before replacement, the existing local ARCH8 source was preserved with `cp -p` to the caller-selected backup path.

The VELA12 source was then copied to a pending path, byte-compared with `cmp -s`, moved with `mv -f` over the local `SIGMA_ARCH8_P0_SHAPE_FIXED.sigma` path, and checked against the expected VELA12 SHA256.

Post-promotion local source SHA256:
`3255b41d8771494d8061071d2e129ffee59241e1a81cce4d25d1ebeb95e71f92`.

Reported markers:
- `SIGMA_CANONICAL_SOURCE=VELA12`
- `VELA12_SOURCE_PROMOTION=PASS`

### Continuity interpretation

This supersedes the previously recorded VELA10 local-source identity for the `/sdcard/Download/SIGMA_ARCH8_P0_SHAPE_FIXED.sigma` path. The reported current local source identity is now VELA12 SHA `3255b41d...`, with a pre-promotion backup reported as created.

Anti-rediscovery: do not repeat the VELA12 local-source promotion or rediscover its resulting SHA unless the local source identity changes or recovery is required.

### Claim boundary

The word `CANONICAL` in the emitted marker is archived as local command output. This evidence does not by itself prove mutation of `.sigma_ail/SIGMA_HEAD`, owner state, native binding, production runtime selector, SIA bindings, admission, activation, or cutover.

The previously recorded VELA12 proof gaps also remain unless separately resolved: independent execution proof and cost-bound proof were reported NOT_IMPLEMENTED.


## VELA13 — Cost Registry KAT + Marker-Checked Backward Compatibility

Evidence date: 2026-10-11. Basis: user-supplied Termux compile/runtime and marker-checked regression output; SPECIAL R18 research evidence, not an independent audit or canonical activation claim.

### VELA13 cost-registry identity and KAT

- Source: `SIGMA_CORE_VELA13_COST_REGISTRY_R20261011_F.sigma`
- Source SHA256: `d3d1e71e0350887925f0f63bfa0a95abec873b0b3cc3bc0271eb1ebe27df3146`
- Bytecode SHA256: `ba8894e86abd8309220cd614ba232dde539e81601de7ef4c0308607e38bb42f5`
- Compilation with existing `sigmac-vkm`: PASS reported.
- Runtime: `$VKM/SIGMA-Vkm-VELA`
- Command: `RBX_VELA13_KAT`
- VELA13_MEASURED_HOLD=PASS
- VELA13_CALIBRATED_HOLD=PASS
- VELA13_IDENTITY_REJECTION=PASS
- VELA13_NO_SELF_CERTIFICATION=PASS
- VELA13_REGISTRY_KAT=PASS
- SIGMA_VM_EXIT_CODE=0
- VELA13_COST_PROOF=NOT_IMPLEMENTED

### Marker-checked backward compatibility

Using VELA13 bytecode on `SIGMA-Vkm-VELA`, regression executed VELA8, VELA9, VELA10, VELA11, and VELA12 commands. The harness failed closed on nonzero runtime status and separately required the expected exact PASS marker for each command.

Required/observed markers:
- `VELA8_VALIDATION_ENGINE_KAT=PASS`
- `VELA9_GOVERNOR_KAT=PASS`
- `VELA10_PLANNER_KAT=PASS`
- `VELA11_CURSOR_KAT=PASS`
- `VELA12_CAS_RECEIPT_KAT=PASS`

Reported aggregate: `VELA13_BACKWARD_COMPATIBILITY=PASS`.

This is stronger than exit-code-only compatibility evidence because the harness also checks the expected semantic KAT marker for each covered command.

### Remaining boundaries

Historical subordinate output still reports:
- VELA11_COST_PROOF=NOT_IMPLEMENTED
- VELA12_INDEPENDENT_EXECUTION_PROOF=NOT_IMPLEMENTED
- VELA12_COST_BOUND_PROOF=NOT_IMPLEMENTED

VELA13 itself reports `VELA13_COST_PROOF=NOT_IMPLEMENTED`. Therefore the cost registry KAT demonstrates registry/hold/identity/no-self-certification behavior, not a completed cost proof.

Continuity decision: retain VELA13 KAT and marker-checked V8–V12 compatibility. Do not repeat these unchanged regressions for the same source/bytecode/VM identities unless a relevant identity changes or regression appears.

Claim boundary: no cost proof, independent execution proof, qualifying ARCH8 training, Gen2 checkpoint, ONE SIGMA binding activation, admission, or cutover is established by this evidence.


## VELA13 — Local ARCH8 Source Promotion Readback

Evidence date: 2026-10-11. Basis: user-supplied Termux expected-SHA check and local source readback; SPECIAL R18 evidence, not an independent audit or ONE SIGMA canonical activation claim.

- The local `SIGMA_ARCH8_P0_SHAPE_FIXED.sigma` path passed the expected-new SHA check.
- Post-promotion SHA256: `d3d1e71e0350887925f0f63bfa0a95abec873b0b3cc3bc0271eb1ebe27df3146`.
- Reported markers:
  - `SIGMA_CANONICAL_SOURCE=VELA13`
  - `VELA13_SOURCE_PROMOTION=PASS`

Continuity interpretation: VELA13 SHA `d3d1e71e...` supersedes the previously recorded VELA12 SHA as the reported current content identity of the local `/sdcard/Download/SIGMA_ARCH8_P0_SHAPE_FIXED.sigma` path.

Anti-rediscovery: do not repeat VELA13 local-source promotion/readback unless the local source identity changes or recovery is required.

Claim boundary: the emitted `SIGMA_CANONICAL_SOURCE=VELA13` marker is archived as local command output. This block does not prove mutation of ONE SIGMA HEAD, owner state, native binding, production runtime selector, SIA bindings, admission, activation, or cutover. The previously recorded VELA13 cost-proof gap remains unresolved unless separately proven.


## VELA14 — Structural Bound KAT + V8–V13 Marker-Checked Compatibility

Evidence date: 2026-10-11. Basis: user-supplied Termux native KAT and marker-checked regression output; SPECIAL R18 research evidence, not an independent audit or canonical activation claim.

### VELA14 structural-bound identity and KAT

- Source: `SIGMA_CORE_VELA14_STRUCTURAL_BOUND_R20261011_G.sigma`
- Source SHA256: `45238d7645345669377120fa5fa7c9978115fc124caf38e9dd75696bddf45b81`
- Bytecode SHA256: `91cdca54a334d01b7c0975648ec127f235aa55c4bdee54a7fed8988873c552fe`
- Runtime: `$VKM/SIGMA-Vkm-VELA`
- VELA14_AFFINE_STRUCTURAL_BOUND=PASS
- VELA14_IDENTITY_AND_DOMAIN=PASS
- VELA14_OVERBUDGET_HOLD=PASS
- VELA14_VM_ADMISSION_FAIL_CLOSED=PASS
- VELA14_STRUCTURAL_KAT=PASS
- SIGMA_VM_EXIT_CODE=0
- VELA14_VM_BYTECODE_PROOF=NOT_IMPLEMENTED

### Marker-checked backward compatibility

Using VELA14 bytecode on `SIGMA-Vkm-VELA`, the fail-closed harness executed VELA8 through VELA13 and required each exact expected semantic PASS marker in addition to successful process execution:

- `VELA8_VALIDATION_ENGINE_KAT=PASS`
- `VELA9_GOVERNOR_KAT=PASS`
- `VELA10_PLANNER_KAT=PASS`
- `VELA11_CURSOR_KAT=PASS`
- `VELA12_CAS_RECEIPT_KAT=PASS`
- `VELA13_REGISTRY_KAT=PASS`

Reported aggregate: `VELA14_BACKWARD_COMPATIBILITY=PASS`.

### Proof-gap continuity

The supplied subordinate outputs continue to expose historical unresolved items:
- VELA11_COST_PROOF=NOT_IMPLEMENTED
- VELA12_INDEPENDENT_EXECUTION_PROOF=NOT_IMPLEMENTED
- VELA12_COST_BOUND_PROOF=NOT_IMPLEMENTED
- VELA13_COST_PROOF=NOT_IMPLEMENTED

VELA14 additionally reports `VELA14_VM_BYTECODE_PROOF=NOT_IMPLEMENTED`.

Therefore the structural KAT and fail-closed VM-admission behavior do not constitute a bytecode proof, cost proof, or independent-execution proof.

### Anti-rediscovery / claim boundary

Retain the VELA14 source/bytecode identities, structural KAT, and marker-checked V8–V13 compatibility result. Do not repeat unchanged regressions for these identities absent a regression or changed contract.

No VM bytecode proof, qualifying ARCH8 training, Gen2 checkpoint, ONE SIGMA binding activation, admission, or cutover is established by this evidence. VELA14 remains SPECIAL R18 qualification evidence.


## VELA14 — Local ARCH8 Source Promotion Readback

Evidence date: 2026-10-11. Basis: user-supplied Termux atomic-move and SHA256 readback; SPECIAL R18 evidence, not an independent audit or ONE SIGMA canonical activation claim.

- Pending VELA14 source was moved with `mv -f` over the local ARCH8 P0 source path.
- Expected-new SHA check passed.
- Current reported local `SIGMA_ARCH8_P0_SHAPE_FIXED.sigma` SHA256: `45238d7645345669377120fa5fa7c9978115fc124caf38e9dd75696bddf45b81`.
- Reported markers: `SIGMA_CANONICAL_SOURCE=VELA14`, `VELA14_SOURCE_PROMOTION=PASS`.

Continuity interpretation: VELA14 SHA `45238d76...` supersedes VELA13 as the reported current local ARCH8 P0 source identity.

Claim boundary: local source promotion is not itself ONE SIGMA admission/activation/cutover. The recorded VELA14 VM-bytecode proof gap and prior unresolved cost/independent-execution proof gaps remain unless separately resolved.


## VELA15 — Bytecode Header ABI Qualification

Evidence date: 2026-10-11. Basis: user-supplied Termux native KAT and direct bytecode-header inspection; SPECIAL R18 qualification evidence, not an independent audit or complete VM-bytecode proof.

### Header KAT

- VELA15_ABI_HEADER=PASS
- VELA15_MAGIC_VERSION_REJECTION=PASS
- VELA15_ENDIAN_DECODER=PASS
- VELA15_RANGE_INPUT_GATES=PASS
- VELA15_HEADER_KAT=PASS
- SIGMA_VM_EXIT_CODE=0
- VELA15_RUNTIME_EXIT=PASS
- VELA15_FULL_PARSER=NOT_IMPLEMENTED
- VELA15_VM_COST_PROOF=NOT_IMPLEMENTED

### Runtime and real-bytecode binding

The runtime binary `$VKM/SIGMA-Vkm-VELA` was explicitly checked against expected SHA256:
`ed2849dc666ab80cf44e29a7178affc95c02ed051168494d9575d4a60ca5ff7d`.

Inspected bytecode:
`SIGMA_CORE_VELA15_HEADER_R20261011_H_FIX1.sigmab`

- size: 868667 bytes
- first 16 decimal bytes reported: `83 73 71 77 66 67 48 49 1 0 0 0 202 28 0 0`
- first 8 bytes decoded/checked as magic `SIGMBC01`
- VELA15_REAL_BYTECODE_MAGIC=PASS
- bytecode SHA256: `6982d1c2b99f651de2883dbeeba59113ee001f1ca81ea4aa679e8763ebee5d18`

### Continuity interpretation

VELA15 provides reported evidence that the header-level ABI contract and rejection/range/endian checks pass, and independently confirms the expected magic on an actual compiled VELA15 bytecode artifact while bound to the qualified VELA VM identity.

This advances the previously recorded VELA14 `VM_BYTECODE_PROOF=NOT_IMPLEMENTED` gap only at header/ABI level. It does not constitute a full bytecode parser/proof.

### Remaining gates / anti-rediscovery

Do not repeat header magic/ABI discovery for unchanged VM and bytecode identities. The explicit remaining VELA15 gates are:
- `VELA15_FULL_PARSER=NOT_IMPLEMENTED`
- `VELA15_VM_COST_PROOF=NOT_IMPLEMENTED`

A complete VM-bytecode proof must go beyond the 16-byte/header evidence and validate the relevant bytecode structure/ranges/instructions or other exact parser contract, fail closed on malformed artifacts, and bind the resulting proof to the exact bytecode and VM identities.

Claim boundary: no full VM-bytecode proof, VM cost proof, qualifying ARCH8 Gen2 checkpoint, ONE SIGMA admission, activation, or cutover is established by this evidence.


## VELA15 — Real Bytecode Header Runtime KAT

Evidence date: 2026-10-11. Basis: user-supplied Termux source integration/compile and native runtime output; SPECIAL R18 qualification evidence, not an independent audit or complete bytecode proof.

### Real-header runtime path

- VELA15_REAL_HEADER_DISPATCH=INSTALLED
- Source: `SIGMA_CORE_VELA15_REAL_HEADER_R20261011_I.sigma`
- Source SHA256: `feb0f0f0ecc547df6f41449ab4650c726f3594a7680e0776c2d3091e7a1f0b71`
- Bytecode SHA256: `007d5e0259f59199f554b59400ca9ae631029cd6cabc07090584dcbaebc3e552`
- Compilation with existing `sigmac-vkm`: PASS reported.
- Runtime: `$VKM/SIGMA-Vkm-VELA`
- Command: `RBX_VELA15_REAL_HEADER_KAT`

The runtime fixture path was explicitly set to the previously inspected real bytecode:
`/sdcard/Download/SIGMA_CORE_VELA15_HEADER_R20261011_H_FIX1.sigmab`.

### Native real-file results

- VELA15_REAL_FILE_READ=PASS
- VELA15_REAL_MAGIC=PASS
- VELA15_REAL_ABI_VERSION=PASS
- VELA15_REAL_CONSTANT_COUNT=7370
- VELA15_REAL_HEADER_KAT=PASS
- SIGMA_VM_EXIT_CODE=0

### Continuity interpretation

This strengthens the prior VELA15 header evidence: validation is now reported through a SIGMA native runtime command that reads the real bytecode fixture rather than relying only on external shell header inspection. The runtime successfully reads the file, validates magic and ABI version, and extracts a constant-count value of 7370 from the real artifact.

Anti-rediscovery: retain this runtime real-header result for the recorded source/bytecode/runtime fixture identities. Do not repeat it unless one of those identities or the header contract changes, or a regression appears.

### Claim boundary

This remains header-level/runtime-fixture qualification. Reading a constant count does not by itself prove that all 7370 constants, section boundaries, instruction stream, operand ranges, control-flow targets, or other bytecode structures have been fully parsed and validated.

Accordingly the previously recorded `VELA15_FULL_PARSER=NOT_IMPLEMENTED` and `VELA15_VM_COST_PROOF=NOT_IMPLEMENTED` gaps are not considered resolved by this evidence. No full VM-bytecode proof, ONE SIGMA admission, activation, or cutover is established.


## VELA15K — Full Constant-Pool Segmented Scan Complete

Evidence date: 2026-10-11. Basis: user-supplied VELA15K segmented runtime scan output; SPECIAL R18 qualification evidence, not an independent audit or complete whole-bytecode proof.

### Full constant-pool scan result

The reported VELA15K scanner advanced monotonically through the real bytecode constant pool in bounded segments. Each reported segment returned `VELA15K_SEGMENT=PASS` and advanced `VELA15K_NEXT_INDEX`.

Final reported state:
- VELA15K_SEGMENTS=231
- VELA15K_CONSTANTS=7370
- VELA15K_SYMBOL_TABLE_OFFSET=197703
- final index=7370
- final offset=197703

The final partial segment advanced from index 7360 to the declared constant count 7370. This matches the previously reported real-header `VELA15_REAL_CONSTANT_COUNT=7370`.

### Continuity interpretation

This materially strengthens VELA15 parser evidence: the constant-pool portion of the real bytecode is now reported scanned completely, not merely counted from its header. The bounded scan reaches exactly the declared 7370 constants and yields the next structural boundary at symbol-table offset 197703.

For the constant-pool objective, earlier header-only uncertainty is superseded by this full segmented scan.

### Anti-rediscovery / remaining parser scope

Do not repeat the 231-segment / 7370-constant scan for the same real-bytecode identity unless the parser contract or artifact identity changes or a regression appears.

However, `VELA15_FULL_PARSER` is not promoted to PASS from this evidence alone. A whole-bytecode parser/proof still needs evidence for the remaining applicable structures after offset 197703, including the symbol table and any instruction/code sections, operand/range constraints, section boundaries, and control-flow targets required by the actual SIGMBC01 format.

Likewise, `VELA15_VM_COST_PROOF=NOT_IMPLEMENTED` remains unresolved unless separately proven.

Claim boundary: constant-pool full scan complete does not itself establish complete VM-bytecode proof, VM cost proof, ONE SIGMA admission, activation, or cutover.


## VELA15K — Symbol Table Header Discovery

Evidence date: 2026-10-11. Basis: user-supplied real-bytecode identity/header inspection output; SPECIAL R18 qualification evidence, not an independent audit or complete parser proof.

Following the previously completed 7370-constant scan ending at symbol-table offset 197703:

- BYTECODE_SHA=PASS
- Symbol-table header bytes reported: `37 14 0 0`
- Decoded/reported SYMBOL_COUNT=3621
- Real bytecode file size=868667 bytes
- Fixture: `SIGMA_CORE_VELA15_HEADER_R20261011_H_FIX1.sigmab`

Continuity interpretation: the parser investigation has reached the symbol-table structure after the fully scanned constant pool and has identified a declared symbol count of 3621.

Anti-rediscovery: retain symbol-table start offset 197703 and declared count 3621 for the same bytecode identity. Do not repeat header discovery unless the bytecode/parser contract changes.

Claim boundary: this is symbol-table header/count discovery only. It does not establish that all 3621 symbol records have been parsed, that their offsets/ranges/references are valid, or that subsequent code/instruction/control-flow sections are valid. Therefore whole-bytecode `FULL_PARSER=PASS` and VM cost proof remain unproven.


## VELA15K — First Symbol Record Inspection

Evidence date: 2026-10-11. Basis: user-supplied direct inspection of the real VELA15 bytecode fixture; SPECIAL R18 parser evidence, not an independent audit or full symbol-table proof.

Following the previously recorded symbol-table boundary/count discovery:

- BYTECODE_IDENTITY=PASS
- First symbol length bytes: `3 0 0 0`
- Reported first symbol payload begins with the three-byte text `U_H`.
- The displayed following bytes include subsequent length-prefixed-looking text such as `op`, `a`, `b`, `c`, and `R14_bytes_new`.
- Real fixture size remains 868667 bytes.

Continuity interpretation: direct inspection is consistent with the first symbol having declared length 3 and payload `U_H`. This provides a concrete first-record fixture for development of the bounded 3621-symbol scanner.

Claim discipline: the surrounding bytes are retained as observational evidence only. This note does not infer the complete symbol-record schema, alignment rules, or subsequent section boundary from a single sample.

Anti-rediscovery: later parser work should reuse symbol-table start offset 197703, declared symbol count 3621, and the first-record fixture (length 3, payload `U_H`) rather than rediscovering them.

Claim boundary: full symbol-table scan, reference/range validation, subsequent bytecode sections, whole-bytecode FULL_PARSER, and VM cost proof remain unproven.


## VELA15-L — Symbol Chunk/Cursor Runtime KAT

Evidence date: 2026-10-11. Basis: user-supplied Termux compile/runtime output; SPECIAL R18 parser qualification evidence, not an independent audit or full symbol-table scan proof.

### Identity and compile

- Source: `SIGMA_CORE_VELA15_SYMBOL_R20261011_L.sigma`
- Source SHA256: `ded17adda9688f0fa170d1d0973d52c69f9dbc44c970881ff6bc6daa5c288e24`
- Bytecode SHA256: `a756af30d6fb8dcecd02fa9b293d0103e2965e67530a4921b306c75a31ba5ef3`
- VELA15L_COMPILE=PASS

### Native runtime KAT

- VELA15L_SYMBOL_CHUNK=PASS
- VELA15L_SYMBOL_CURSOR=PASS
- VELA15L_SYMBOL_KAT=PASS
- SIGMA_VM_EXIT_CODE=0

### Continuity interpretation

VELA15-L establishes reported runtime qualification of the symbol-table chunk and cursor primitives needed for bounded symbol scanning. This follows the previously recorded real-bytecode symbol-table boundary at offset 197703, declared symbol count 3621, and first-record fixture with length 3 / payload `U_H`.

Anti-rediscovery: retain the VELA15-L source/bytecode identities and chunk/cursor KAT result. Do not repeat this primitive KAT for unchanged identities absent a regression.

### Claim boundary

This evidence does not state that all 3621 symbol records were traversed. Therefore `FULL_SYMBOL_TABLE_SCAN=PASS` is not claimed. Whole-bytecode `FULL_PARSER=PASS`, subsequent section validation, and VM cost proof remain unresolved until separately evidenced.


## VELA15M — Full Symbol-Table Segmented Scan PASS

Evidence date: 2026-10-11. Basis: user-supplied VELA15M bounded segmented scan output; SPECIAL R18 parser qualification evidence, not an independent audit or complete whole-bytecode proof.

### Full symbol-table scan

The VELA15M scanner advanced monotonically through the declared symbol table in bounded segments. Each reported segment returned `VELA15M_SEGMENT=PASS`.

Final reported state:
- VELA15M_SEGMENTS=114
- VELA15M_SYMBOLS=3621
- VELA15M_FUNCTION_TABLE_OFFSET=254941
- final symbol index=3621
- final offset=254941
- VELA15M_FULL_SYMBOL_SCAN=PASS

The final partial segment advanced from index 3616 to the declared symbol count 3621. This exactly matches the previously discovered `SYMBOL_COUNT=3621`.

### Parser continuity

For the same real-bytecode investigation, the reported structural chain is now:

`header/magic/ABI PASS → CONSTANT_COUNT=7370 → full constant scan 7370/7370 → SYMBOL_TABLE_OFFSET=197703 → SYMBOL_COUNT=3621 → full symbol scan 3621/3621 → FUNCTION_TABLE_OFFSET=254941`.

This supersedes the prior state in which only symbol chunk/cursor primitives and the first symbol record had been qualified.

### Anti-rediscovery / remaining parser scope

Do not repeat the 114-segment / 3621-symbol scan for unchanged bytecode/parser identities unless a regression or format change appears.

Whole-bytecode `FULL_PARSER=PASS` is still not claimed from this block alone. Parser work must continue from function-table offset 254941 and validate the remaining applicable function/code/instruction structures, section boundaries, operand/range constraints, control-flow targets, and exact end-of-file/format invariants required by SIGMBC01.

`VELA15_VM_COST_PROOF` also remains unresolved unless separately proven.

Claim boundary: full symbol-table scan PASS does not itself establish complete VM-bytecode proof, VM cost proof, ONE SIGMA admission, activation, or cutover.


## VELA15M — Function Table Header Discovery

Evidence date: 2026-10-11. Basis: user-supplied direct inspection of the real VELA15 bytecode fixture; SPECIAL R18 parser evidence, not an independent audit or full function-table proof.

Following the previously completed symbol scan ending at `FUNCTION_TABLE_OFFSET=254941`:

- BYTECODE_IDENTITY=PASS
- Function-table header bytes: `23 6 0 0`
- Decoded/reported FUNCTION_COUNT=1559
- First function metadata bytes: `0 0 0 0 4 0 1 0 0 0 2 0 0 0 3 0`
- Real bytecode size remains 868667 bytes.

### Continuity interpretation

The parser investigation has now reached the function-table structure after completing 7370/7370 constants and 3621/3621 symbols. The function table declares 1559 entries, and a concrete 16-byte first-function metadata fixture has been captured.

### Claim discipline / anti-rediscovery

Retain function-table start offset 254941, declared function count 1559, and the first 16 metadata bytes for subsequent bounded parser work. Do not infer field meanings, widths beyond what is directly observed, code offsets, argument counts, or control-flow semantics from this single metadata sample without additional format/runtime evidence.

Whole-bytecode `FULL_PARSER=PASS` is not yet claimed. The next parser stage must traverse/validate all 1559 function records and establish the next section boundary, then validate any remaining code/instruction/operand/control-flow/end-of-file invariants required by SIGMBC01.

`VELA15_VM_COST_PROOF` also remains unresolved unless separately proven.


## VELA15 — First Function Instruction-Stream Discovery

Evidence date: 2026-10-11. Basis: user-supplied direct inspection of the real VELA15 bytecode fixture; SPECIAL R18 parser evidence, not an independent audit or full function/code proof.

Following the previously recorded function-table declaration of 1559 functions:

- Additional reported first-function metadata/value sequence: `1 2 3 4`.
- FIRST FUNCTION INSTRUCTION COUNT=1169.
- First 32 reported instruction bytes:
  `10 01 00 00 00 01 00 00 00 00 21 10 41 07 00 00 00 30 05 00 00 00 00 00 31 40 07 00 00 00 10 01`.

### Continuity interpretation

The parser investigation has progressed from the function-table header/first metadata fixture into the first function's instruction stream and has identified a declared instruction count of 1169 for that function.

### Claim discipline / anti-rediscovery

Retain the reported instruction count and first 32 instruction bytes as a concrete fixture for function/code parser development. The sequence `1 2 3 4` is retained as observed output only because the supplied excerpt does not identify its field names or semantics.

Do not infer opcode meanings, instruction widths, operand types, branch targets, stack effects, or control-flow semantics solely from these bytes.

This block does not establish traversal of all 1169 instructions in function 0 or all 1559 functions. Whole-bytecode `FULL_PARSER=PASS`, instruction/control-flow validation, and VM cost proof remain unresolved until separately evidenced.


## VELA Activation — Gate A1 Prestate/Recovery Identity PASS

Evidence date: 2026-10-11. Basis: user-supplied Termux Gate A1 output; SPECIAL R18 activation-preparation evidence, not an independent audit or activation verdict.

### Gate A1 result

- Recovery/prestate report SHA256: `297d041aff02416a6a8a9f39e9e45c19ede66b351b8e688dae6e4a560ca51c22`
- Recovery report path: `$HOME/SIGMA/sigma_genesis1/VELA_ACTIVATION_RECOVERY/prestate_20261011_073712.txt`
- SIGMA_CORE_IDENTITY=PASS
- SIGMA_VELA_VM_IDENTITY=PASS
- SIGMA_PRESTATE_REPORT=CREATED
- GATE A1 COMPLETE

### Continuity interpretation

Gate A1 establishes the reported creation of a recovery/prestate artifact while successfully checking the expected SIGMA core and VELA VM identities. This is activation-preparation evidence and provides a concrete pre-mutation recovery reference for later gates.

Anti-rediscovery: retain the report path and SHA256 above. Later activation work should bind subsequent authority/transaction evidence to this exact prestate rather than reconstructing it from memory.

### Claim boundary

Gate A1 does not by itself establish Admission, native-binding mutation, runtime-selector consumption, Activation, or Cutover. The contents of the prestate report were not supplied in this block, so this note does not infer which individual owner/native/head/watchdog fields it contains. Subsequent gates should explicitly bind the activation transaction to this prestate SHA and verify required postconditions/rollback.


## VELA Activation — Gate B4 SIA capability_invoke Host ABI Discovery

Evidence date: 2026-10-11. Basis: user-supplied Termux SIA consumer/host-source discovery output; SPECIAL R18 activation/architecture evidence, not an independent audit or activation verdict.

### Canonical SIA consumer R3 invocation surface

The current SIA canonical consumer R3 source was resolved through `canonical_consumer_R3.current` and inspected. It invokes the following through the host operation `capability_invoke`:

- D18 / OBSERVE
- DNA-20 / ASSESS
- DNA-39 / SELECT
- DNA-42 / SCHEDULE
- DNA-49 / ROUTE
- MEMORY_LINEAGE_R1 / VERIFY
- API410_FINAL_LANGUAGE_UNDERSTANDING / UNDERSTAND

The consumer validates returned result structure through `VALID_D18` and `VALID_ALL`. It emits `CANONICAL_RESULT_CONSUMPTION=PASS` and `CORE_A_DECISION=CAPABILITY_RESULTS_ACCEPTED` only when all seven checks pass; otherwise it emits `CANONICAL_RESULT_CONSUMPTION=HOLD`.

The consumer also explicitly reports:
- TRAINING_EXECUTED=NO
- SECOND_SIGMA=NO

### Host implementation / socket discovery

Targeted source discovery for `capability_invoke` found a C implementation surface at:

`$ROOT/.sigma_ail/SIA_CORE_A/runtime/7a696d39a5854ddd32a44e18dc6fd5465de3b6a135b55830f1c07d973fb27a5c/sigma_vkm.c`

The same source was also the reported hit for `SIA_SOCKET_PATH`.

Within the searched SIA source inventory, this `sigma_vkm.c` was the reported C/H implementation file.

### Architectural interpretation

This evidence supports the concrete execution boundary:

`SIA canonical consumer (.sigma) → host("capability_invoke", ...) → SIA runtime host implementation (sigma_vkm.c) → capability dispatch/result → consumer validation`.

It also demonstrates a fail-closed consumer decision at the result-consumption layer: any failed capability result validation prevents aggregate canonical result consumption PASS.

This is useful for VELA activation because VM migration/rebinding must preserve this `capability_invoke` ABI and the SIA runtime/socket contract rather than rewriting capability semantics merely to accommodate a new VM identity.

### Claim boundary / next activation evidence

Gate B4 is discovery/contract evidence. It does not yet prove that the newly promoted VELA default VM is the runtime process actually serving the SIA `capability_invoke` host implementation, nor that all seven capabilities have been rerun successfully through that runtime after VM migration.

The next relevant qualification should bind:
1. exact VELA VM SHA;
2. exact SIA runtime `sigma_vkm.c`/built-runtime identity;
3. socket/runtime endpoint;
4. canonical consumer R3 identity;
5. native execution of all seven capability invocations;
6. aggregate `CANONICAL_RESULT_CONSUMPTION=PASS`;
7. owner/native-binding prestate and poststate.

GATE B4 COMPLETE is recorded as host-ABI discovery complete, not Admission or Activation.


## VELA Evolution E7.4 — Tensor Adapter Real-Runtime KAT PASS

Evidence date: 2026-10-11. Basis: user-supplied Termux dispatch/compile/native-runtime output; SPECIAL R18 VELA Evolution qualification evidence, not an independent audit or activation verdict.

### E7.4 build and dispatch

- E7_DISPATCH_INSTALLED=PASS
- Source: `$HOME/SIGMA/sigma_genesis1/VELA_EVOLUTION_R1/SIGMA_CORE_VELA_E7_KAT_R2.sigma`
- Bytecode: `$HOME/SIGMA/sigma_genesis1/VELA_EVOLUTION_R1/SIGMA_CORE_VELA_E7_KAT_R2.sigmab`
- E7_COMPILE=PASS
- Source SHA256: `70b63042b8dec41f0f2199745fecfd45bda8cbd41292102acf256d6f5d71014e`
- Bytecode SHA256: `a4f430169bb9e90231ec7d8e9b614adcb446856f59f16bafe2df30e18c082022`

### Real-runtime KAT

- VELA_E7_F32_ROUNDTRIP=PASS
- VELA_E7_BF16_ROUNDTRIP=PASS
- VELA_E7_SOURCE_IMMUTABILITY=PASS
- VELA_E7_TENSOR_ADAPTER_KAT=PASS
- SIGMA_VM_EXIT_CODE=0
- E7_RUNTIME_GATE=PASS
- E7.4 COMPLETE

### Continuity interpretation

E7.4 establishes reported real-runtime qualification of the VELA tensor-adapter surface for F32 and BF16 roundtrip behavior while preserving source immutability. Dispatch installation and compiled source/bytecode identities are retained for later evolution and compatibility work.

Anti-rediscovery: do not repeat this exact E7 tensor-adapter KAT for unchanged source/bytecode/runtime contracts unless a regression or identity change occurs.

### Claim boundary

E7_RUNTIME_GATE=PASS is an Evolution R1 component qualification result. This evidence does not by itself establish SIA compatibility, VELA Admission, native-binding activation, canonical runtime consumption, or Cutover. Those require their separate activation-chain evidence.
