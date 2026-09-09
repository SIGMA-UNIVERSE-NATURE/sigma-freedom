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
- Core SHA256: `8a10df7f94bc0e9ce1d4ab62d0d6667eb10785c7ea8cc623b4036776302f1ba`
- Blind learned-transform causality: `75/100`; spurious transform false induction FAIL.
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
- Latest admitted capability as of this checkpoint.

## 2026-09-09 — Mechanical Evidence Tool Transport R1 runtime attempt
- Core SHA256: `f530a556a670137f865b3f67b52557f3ccd9ec0b97f536f5c2123ce4276117e5`
- Transport SHA256: `0ed437aa2188b2382aec88c390697f7f912dff0ac27b9f50cc15b5936e713ffd`
- Passed request gating/correlation/verbatim transport, irrelevant evidence, cross-gap isolation, persistence/restart.
- Stopped `RC=72`; failure class HARNESS BUG: live request file legitimately revoked before post-hoc comparison.

## 2026-09-09 — Mechanical Evidence Tool Transport R1H1 runtime attempt
- Immutable request snapshot fix worked.
- Native discriminating-evidence revision PASS; revoked request stops provider PASS.
- Stopped `RC=83`; failure class HARNESS COUNTING BUG: `wc -l` counted newline delimiters rather than canonical records.
- 4 gap records + 60 filler records had each returned native record-success, establishing 64 accepted records before oracle failure.

## 2026-09-09 — Mechanical Evidence Tool Transport R1H2 prepared
- Harness-only record-count correction; core/transport unchanged.
- Native 65th-record rejection gate unchanged.
- Runtime pending.

## 2026-09-09 — Static trust-boundary audit
- New defect found before blind: R1/R1H2 transport treated matching request output/state files as authority without native recomputation from current gap state.
- This could allow a correlated forged request-file pair to trigger provider invocation.
- Defect class: TRANSPORT TRUST BOUNDARY.
- Response: prepare R2; do not promote R1H2 as final transport design even if its remaining harness gate passes.

## 2026-09-09 — Mechanical Evidence Tool Transport R2 prepared
- Core SHA256: `c3ec9d2436f965046ac53bc8b4dba67870f1fb937868d3b667cad6779ea51285`
- Transport SHA256: `32c54f4f2f342652b27f4639b1b7ae74c4cc30f27a80bf202eebe309594ddb35`
- Preflight SHA256: `399f5a901fbbe762938cbf30eeaf65acb8cf833fb92741c6108d6458fb0a1cdd`
- Bundle SHA256: `08293b98f13e695e83ef79e76ec5c079ed025c7b8a7c126de682cfed542eb4ad`
- New gate: locked native SIGMA recomputes exact request from current native gap state immediately before provider invocation.
- All R1H2 boundedness/revision/freeze gates retained.

## 2026-09-09 — Blind Host Substitution R1 prepared
- Auditor SHA256: `25d9ae0401d7784672c7f284a710876bb5a5b9875743a8307f3c775131281045`
- Bundle SHA256: `269c5edfeb610676b4131d20dadce766019bd4828cc560949bf45640ed516cc7`
- Target fixed before evaluator creation.
- Tests correlated forged request, stale request from another gap, raw provider protocol injection, irrelevant evidence and native-only revision.

## 2026-09-09 — Native Gap Search Query R1 prepared
- Core SHA256: `286b1c557a2cbe027d67fb645448bdd8ff09540d5a628b89517ef2a3fa38bd5f`
- Bundle SHA256: `300b87ba0357268d816d328d304ca500d1b5925929e7bbe645a8a454658dd428`
- Query bytes are generated inside SIGMA as verbatim serialization of the open gap pair.
- Host query rewriting/expansion: forbidden.
- Search quality and Internet acquisition remain FAIL pending runtime tests.

## 2026-09-09 — Real Internet Search Discovery R1 prepared
- Query core SHA256: `286b1c557a2cbe027d67fb645448bdd8ff09540d5a628b89517ef2a3fa38bd5f`
- Transport SHA256: `32c54f4f2f342652b27f4639b1b7ae74c4cc30f27a80bf202eebe309594ddb35`
- Provider SHA256: `cbab8e07a87009a1787f64a1179706e77fc72c72ab2848366b488a335534d3c3`
- Bundle SHA256: `5007bc3e80df1a158f45f9e3c711f0f383ba600907dbc7894e062fd80cffaf30`
- Fixed mechanical provider: English Wikipedia MediaWiki search API.
- Native query bytes are sent without host expansion; compact raw search response must enter native ledger without forcing semantic conclusion.
- Runtime/network admission pending.

## 2026-09-09 — Immediate Execution Ladder R1 prepared
- Bundle SHA256: `87118eebdda1ee1af2d5bb247516905da26ded4f1ce60595c8da6e859fe32197`
- Runner SHA256: `c4c1780d57dc57357bc9d90e90faed04cee4e4bb384241cc9a3eb200f244ad69`
- Strict order: Transport R2 -> blind host substitution -> native gap search query -> real Internet search discovery.
- Stops at first failure and preserves local logs.
- Even full ladder PASS does not imply whole-work understanding, semantic compression or continual narrative learning.

## 2026-09-09 10:35 +07 — Mechanical Evidence Tool Transport R2 runtime admission
- Execution Ladder Stage 1 returned `RC=0` on Oppo.
- Core SHA256: `c3ec9d2436f965046ac53bc8b4dba67870f1fb937868d3b667cad6779ea51285`.
- Transport SHA256: `32c54f4f2f342652b27f4639b1b7ae74c4cc30f27a80bf202eebe309594ddb35`.
- Full R2 preflight therefore completed through native request revalidation/authority, provider gating, byte-preserving request/raw transport, native discriminating-evidence revision/revocation, bounded 64-record ledger/65th-result rejection, freeze and production-safety gates.
- `MECHANICAL_TOOL_INVOCATION=PASS` in exact tested opaque-provider scope.
- Real Internet acquisition and autonomous research remain FAIL.
- Production binding: NO.

## 2026-09-09 10:35 +07 — Blind Host Substitution R1 runtime attempt
- `FORGED_CORRELATED_REQUEST_REJECTION=PASS`.
- Stopped at `FAIL=GAP_A`, `RC=34` before intended gap-authority adversarial cases.
- Failure class: EVALUATOR FIXTURE BUG.
- Root cause: blind helper generated IDs like `EID_A_1` (7 characters); target core `safe_atom` requires >=8 characters, so first blind evidence record was rejected.
- This result is neither a SIGMA failure nor a blind PASS.
- Corrected evaluator R1H1 changes only fixture IDs to valid-length `EID_BLIND_<case>_<n>`; target core/transport and adversarial criteria are unchanged.
- Auditor R1H1 SHA256: `d807e3606bda51a2586dbccc5f4b458a4e797036018a8b2337d819cb1b55580d`.
- Bundle R1H1 SHA256: `716ba0f4ca1ed002e17ac2a1487aa7ad0cb7d753ab2ee866e3e01586206ee3ea`.

## 2026-09-09 10:38 +07 — 24H Continuation Ladder R2 prepared
- Runner SHA256: `84b68095bd3807c725f482ea55f67998f98e260a637b6f732c44cb14e8f32036`.
- Bundle SHA256: `f5c9c99e38efc76a8fa64eac1f8c92fb08faea64bd4e714d622f168223d0f4b9`.
- Resumes from corrected Blind Stage 2H1, then runs native gap search-query and real Internet search-discovery.
- Stops at first failure and preserves logs.
- Stage 1 R2 is treated as already admitted from the prior Oppo `RC=0`.

### Next checkpoint target

Run the continuation ladder. If all stages pass, move immediately to full-source fetch, bounded long-form streaming, whole-work source-removal semantic-retention, semantic compression, local continual learning and multilingual tests. After the required production subset passes, follow `C5V3_AUTONOMOUS_INTEGRATION_PLAN.md`: read-only synchronization -> isolated graft -> autonomous-runner shadow -> soak/recovery -> promotion -> explicit cutover only when authorized.