# SIGMA C5 M5 — Checkpoints

This file is append-only in intent. Historical failures remain visible after later fixes.

## 2026-09-09 — M5 Cleanline R1
- Admission: PASS
- Capability: native neutral evidence/provenance persistence
- Core SHA256: `082fad3a063232ea25c633d310a004887f6b228a233f76009ef111b4469fabf1`
- Production binding: NO

## 2026-09-09 — Native Provenance Gap R1
- Admission: PASS
- Capability: native structural provenance-diversity gap

## 2026-09-09 — Native Exact Evidence Cohort R1
- Admission: PASS
- Core SHA256: `b8a925822aee50533b882ab5e0ea678280c4ff29676483dd9c7e9a7831da8c46`

## 2026-09-09 — Wide Blind R1
- Score: `65/100`
- Structural native: `45/45`
- Anti-hardcode: `20/20`
- Cognitive transfer: `0/35`
- target-scoped gap FAIL; semantic paraphrase FAIL; conflict awareness FAIL; autonomous research-goal formation FAIL.

## 2026-09-09 — Native Scoped Provenance Gap R1
- Admission: PASS
- Core SHA256: `12def2b5c1b9fa6c76614c9409ed8090fab669bd6266de6a34638c7dccf67e07`

## 2026-09-09 — Wide Blind R2
- Score: `75/100`
- target-scoped gap PASS; semantic paraphrase FAIL; conflict awareness FAIL; autonomous research-goal formation FAIL.

## 2026-09-09 — Native Context Structure R1
- Admission: PASS
- Core SHA256: `049aedb09a0a5ca4719ee004114269fa091a0b62df8673f1a17b48f7c25bb161`
- Blind contextual transfer: `100/100` in exact structural scope only.

## 2026-09-09 — Native Contextual Paraphrase R1
- Admission: PASS in local scope
- Core SHA256: `68cd597e1ba1c3273ff21f65995080fcfdac1fbc6ca36865d86e24ee4d5702fb`
- NL blind R1: `60/100`; role reversal FAIL; semantic paraphrase claim rejected.

## 2026-09-09 — Native Relational Sequence R1
- Admission: PASS
- Core SHA256: `08a1f6c5d5968b24b2c6528184c2fb09ebefb1a327662d0bda4036776302f1ba`
- NL blind R2: `75/100`; role reversal PASS; benign untrained reorder FAIL; zero-shot low-overlap FAIL.

## 2026-09-09 — Native Learned Sequence Transform R1
- Admission: PASS
- Blind learned-transform causality later exposed spurious transform false induction.
- Promotion status: RETIRED.
- Retired assumption: recurring permutation shape implies relation-preserving transform.

## 2026-09-09 — Native Context-Grounded Sequence R1
- Admission: PASS
- Core SHA256: `e3fcdb9999c501ab7696457691edc4923d187e397486f506d30ad7c70cca0f11`
- Blind context-grounded causality: `65/100`; grounded role-reversal false equivalence FAIL.
- Promotion status: RETIRED.
- Retired assumption: shared co-document context implies same relation.

## 2026-09-09 — Native Relation Discrimination Gap R1
- Admission: PASS
- Core SHA256: `2bbeafc1fdf7297884109efd12570de6e300e990f489bb3e0904847f4d307a91`
- shared-context false equivalence resistance PASS; relation-discrimination gap PASS; dynamic distinguishing-evidence revision PASS.
- Semantic paraphrase remains FAIL.

## 2026-09-09 — Native Gap Evidence Request R1
- Admission: PASS
- Core SHA256: `1ff2dc93dc41f63e070a548d582d56911c406538eeacac826a0b9c419a4ce1eb`
- no gap/no request PASS; open native gap/request PASS; request dynamic/isolation/persistence/restart/revocation PASS.
- Host learning/query generation/tool selection for active decision: NO.

## 2026-09-09 — Mechanical Evidence Tool Transport R1 runtime attempt
- Runtime passed several transport gates then stopped `RC=72`.
- Failure class: HARNESS BUG; live request file was legitimately revoked before post-hoc comparison.

## 2026-09-09 — Mechanical Evidence Tool Transport R1H1 runtime attempt
- Immutable request snapshot fix worked; native revision/revocation PASS.
- Stopped `RC=83`.
- Failure class: HARNESS COUNTING BUG; `wc -l` counted newline delimiters rather than canonical records.

## 2026-09-09 — Static transport trust-boundary audit
- Found a real defect: request output/state files alone could be forged coherently.
- Response: R2 requires locked native SIGMA to recompute request from current gap state immediately before provider invocation.

## 2026-09-09 10:35 +07 — Mechanical Evidence Tool Transport R2 runtime admission
- Execution Ladder Stage 1: `RC=0`.
- Core SHA256: `c3ec9d2436f965046ac53bc8b4dba67870f1fb937868d3b667cad6779ea51285`.
- Transport SHA256: `32c54f4f2f342652b27f4639b1b7ae74c4cc30f27a80bf202eebe309594ddb35`.
- Native request authority/revalidation, provider gating, verbatim transport, native revision/revocation, 64-record bound/65th rejection, freeze and production safety all completed.
- `MECHANICAL_TOOL_INVOCATION=PASS` in exact tested scope.
- Production binding: NO.

## 2026-09-09 10:35 +07 — Blind Host Substitution R1 runtime attempt
- Forged correlated request rejection PASS.
- Then `FAIL=GAP_A`, `RC=34`.
- Failure class: EVALUATOR FIXTURE BUG; ID `EID_A_1` violated generic safe-atom minimum length.
- Not counted as cognition FAIL or blind PASS.

## 2026-09-09 10:45 +07 — Corrected Blind Host Substitution R1H1
- Continuation Ladder Stage 2H1: PASS, `RC=0`.
- `BLIND_HOST_SUBSTITUTION_BOUNDARY=PASS` in exact adversarial scope.
- Forged/stale request authority does not substitute for native state; provider/raw payload cannot directly force a native conclusion.

## 2026-09-09 10:45 +07 — Native Gap Search Query R1
- Continuation Ladder Stage 3: PASS, `RC=0`.
- Core SHA256: `286b1c557a2cbe027d67fb645448bdd8ff09540d5a628b89517ef2a3fa38bd5f`.
- Native SIGMA serializes unresolved gap pair into search-query bytes.
- Host query expansion/rewriting remains absent.

## 2026-09-09 10:45 +07 — Real Internet Search Discovery R1
- Continuation Ladder Stage 4: PASS, `RC=0`.
- Native search query reached real Wikipedia MediaWiki search provider.
- Raw search-discovery bytes stored native with provenance.
- Raw result did not force semantic conclusion.
- `REAL_INTERNET_SEARCH_DISCOVERY=PASS`.
- Full-source fetch, autonomous research, whole-work understanding and semantic compression remain FAIL.
- Production binding: NO.

## 2026-09-09 10:46 +07 — 24H Continuation Ladder R2
- `LADDER_RC=0`.
- `MECHANICAL_TOOL_INVOCATION=PASS`.
- `BLIND_HOST_SUBSTITUTION_BOUNDARY=PASS`.
- `NATIVE_SEARCH_QUERY_BYTES=PASS`.
- `REAL_INTERNET_SEARCH_DISCOVERY=PASS`.
- Full source / whole work / semantic compression / continual narrative learning remain FAIL.

## 2026-09-09 10:46 +07 — Real Internet Full Source Stream R1 prepared
- Core SHA256: `d134fded334a368a24d173823bb20aa0b053e0a40b76edba9c3cf31bc2b0da06`.
- Transport SHA256: `db3310c77c678f205575a4865a325b6017df0183c8ac6e2bd79f12712fdf8f6d`.
- Provider SHA256: `1f269972cf561de8e5e0d8c9b065cb04ca7f6c0620e4a1de8434a16ddcc32976`.
- Preflight SHA256: `325d2e36930f65185471f0526b37913a6a8af4db4865c3ec1c3de775945a37ad`.
- Bundle SHA256: `06897f124d076c5ba1e8e128661fe78b5a563f2adea8a9fc4be5daf34a4a7423`.
- Intended gates: complete real source fetch; byte-identical ordered native reassembly; 64-segment/131072-byte transient bounds; restart state; source excluded from canonical memory; explicit source removal; production unchanged.
- Runtime admission pending.

### Next checkpoint target

Run Real Internet Full Source Stream R1. If PASS, build native whole-work relational representation across distant source units and independent source-removal semantic-retention blind tests. Then continue toward semantic compression/local continual learning/multilingual transfer before C5V3 synchronization/graft/shadow/soak/cutover.