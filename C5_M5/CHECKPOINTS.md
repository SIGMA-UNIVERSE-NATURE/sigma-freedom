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
- Production binding: NO

## 2026-09-09 — Native Exact Evidence Cohort R1

- Admission: PASS
- Capability: exact-byte evidence identity/cohort
- Core SHA256: `b8a925822aee50533b882ab5e0ea678280c4ff29676483dd9c7e9a7831da8c46`
- Production binding: NO

## 2026-09-09 — Wide Blind R1

- Score: `65/100`
- Structural native: `45/45`
- Anti-hardcode: `20/20`
- Cognitive transfer: `0/35`
- `TARGET_SCOPED_GAP_ISOLATION=FAIL`
- `SEMANTIC_PARAPHRASE_TRANSFER=FAIL`
- `CONFLICT_AWARENESS=FAIL`
- `AUTONOMOUS_RESEARCH_GOAL_FORMATION=FAIL`

## 2026-09-09 — Native Scoped Provenance Gap R1

- Admission: PASS
- Core SHA256: `12def2b5c1b9fa6c76614c9409ed8090fab669bd6266de6a34638c7dccf67e07`
- Fixed target-scoped gap isolation.

## 2026-09-09 — Wide Blind R2

- Score: `75/100`
- Structural native: `45/45`
- Anti-hardcode: `20/20`
- Cognitive transfer: `10/35`
- `TARGET_SCOPED_GAP_ISOLATION=PASS`
- `SEMANTIC_PARAPHRASE_TRANSFER=FAIL`
- `CONFLICT_AWARENESS=FAIL`
- `AUTONOMOUS_RESEARCH_GOAL_FORMATION=FAIL`

## 2026-09-09 — Native Context Structure R1

- Admission: PASS
- Core SHA256: `049aedb09a0a5ca4719ee004114269fa091a0b62df8673f1a17b48f7c25bb161`
- Blind contextual transfer: `100/100` in exact tested structural scope.
- Natural-language paraphrase score unchanged.

## 2026-09-09 — Native Contextual Paraphrase R1

- Admission: PASS in capability-local tests.
- Core SHA256: `68cd597e1ba1c3273ff21f65995080fcfdac1fbc6ca36865d86e24ee4d5702fb`
- Independent NL blind R1 later scored `60/100`.
- Role reversal failed; semantic paraphrase claim rejected.

## 2026-09-09 — Native Relational Sequence R1

- Admission: PASS
- Core SHA256: `08a1f6c5d5968b24b2c6528184c2fb09ebefb1a327662d0bda4036776302f1ba`
- Independent NL blind R2: `75/100`.
- Role reversal repaired to PASS.
- Benign untrained reorder: FAIL.
- Zero-shot low-overlap paraphrase: FAIL.

## 2026-09-09 — Native Learned Sequence Transform R1

- Admission: PASS
- Core SHA256: `8a10df7f94bc0e9ce1d4ab62d0d6667eb10785c7ea8cc623b40374ddc342aa37`
- Blind learned-transform causality: `75/100`.
- `SPURIOUS_TRANSFORM_FALSE_INDUCTION_RESISTANCE=FAIL`.
- Promotion status: RETIRED.
- Retired assumption: recurring permutation shape implies relation-preserving transform.

## 2026-09-09 — Native Context-Grounded Sequence R1

- Admission: PASS
- Core SHA256: `e3fcdb9999c501ab7696457691edc4923d187e397486f506d30ad7c70cca0f11`
- Blind context-grounded causality: `65/100`.
- `GROUNDED_ROLE_REVERSAL_FALSE_EQUIVALENCE_RESISTANCE=FAIL`.
- Promotion status: RETIRED.
- Retired assumption: shared co-document context implies same relation.

## 2026-09-09 — Native Relation Discrimination Gap R1

- Admission: PASS
- Core SHA256: `2bbeafc1fdf7297884109efd12570de6e300e990f489bb3e0904847f4d307a91`
- Shared-context false equivalence resistance: PASS.
- Relation-discrimination gap opening: PASS.
- Dynamic distinguishing-evidence revision: PASS.
- Semantic paraphrase: FAIL.

## 2026-09-09 — Native Gap Evidence Request R1

- Admission: PASS
- Core SHA256: `1ff2dc93dc41f63e070a548d582d56911c406538eeacac826a0b9c419a4ce1eb`
- No gap -> no evidence request: PASS.
- Native open gap -> native evidence request: PASS.
- Request depends on dynamic gap: PASS.
- Cross-gap isolation: PASS.
- Persistence/fresh restart: PASS.
- Discriminating evidence revokes request: PASS.
- Host learning/query generation/tool selection for active decision: NO.
- Semantic paraphrase: FAIL.
- Zero-shot low-overlap paraphrase: FAIL.
- Autonomous research: FAIL.
- Tool execution: FAIL.
- Production binding: NO.

## 2026-09-09 — Mechanical Evidence Tool Transport R1 runtime attempt

- Core SHA256: `f530a556a670137f865b3f67b52557f3ccd9ec0b97f536f5c2123ce4276117e5`
- Transport SHA256: `0ed437aa2188b2382aec88c390697f7f912dff0ac27b9f50cc15b5936e713ffd`
- Runtime passed through request gating, request correlation, verbatim transport, irrelevant-evidence native handling, cross-gap isolation, persistence and restart.
- Stopped at `FAIL=DISCRIMINATING_REQUEST_NOT_VERBATIM`, `RC=72`.
- Failure class: HARNESS BUG.
- Root cause: preflight compared provider capture to the live native request output after discriminating evidence had correctly caused native SIGMA to revoke/clear that request.
- No core or transport defect established by this failure.
- Capability remains not admitted.

## 2026-09-09 — Mechanical Evidence Tool Transport R1H1 prepared

- Harness-only correction; runtime pending.
- Core SHA256 unchanged: `f530a556a670137f865b3f67b52557f3ccd9ec0b97f536f5c2123ce4276117e5`
- Transport SHA256 unchanged: `0ed437aa2188b2382aec88c390697f7f912dff0ac27b9f50cc15b5936e713ffd`
- Preflight SHA256: `f52f0c584e9edafa55eb2598bd4591b9a0d506df4c510eb054abb8b83bc2e00c`
- Bundle SHA256: `5fa18729eb97473884da3ece2c8b5584da86e6e89155a6d812c123f2c41a2b25`
- Fix: freeze immutable native-request snapshot before provider invocation; post-consumption verbatim checks compare against the snapshot rather than a live output that may be legitimately revoked.
- Test criteria weakened: NO.
- Production binding: NO.

### Next checkpoint target

Run R1H1 Oppo admission. If it passes, promote only `MECHANICAL_TOOL_INVOCATION=PASS`; keep real Internet acquisition, autonomous research, semantic paraphrase and semantic truth/support/conflict FAIL until separate tests.