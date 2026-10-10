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
