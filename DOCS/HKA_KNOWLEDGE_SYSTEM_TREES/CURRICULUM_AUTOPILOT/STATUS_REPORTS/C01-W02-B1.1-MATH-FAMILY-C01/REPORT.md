# C01-W02-B1.1-MATH-FAMILY-C01 — Durable Status Report

Status: `CHECKPOINTED`  
Stage: `CURRICULUM`  
Scope: `B1.1-C01 — Logic, tập hợp và chứng minh`  
Execution branch: `hka-tree/c01-w02-math-c01`

## Repair academic closure checkpoint

Director-reopened repair has completed the academic/source work and is checkpointed at `CP05-REPAIR-ACADEMIC-CLOSURE`, commit `40023f836059a7ae5a9edefa2806ffdb04edbb72`. The repaired academic record commit is `24f26793d923dd55e87839331994c45489109d88`.

Current repaired counts: 8 nodes, 38 claims, 8 sources, 32 learning objectives, 32 claim-to-objective closure records, 10 cross-links, and 8 sequence-intent records.

## Five Director repairs

1. Propositional syntax/WFF closure: repaired with sourced N001 claims.
2. Axiomatic set existence/Separation closure: repaired with sourced N003 claims; the audit also added the minimum `∈` versus `⊆` closure needed by D1.
3. Decidability distinction: repaired at N008 while explicitly leaving machines, Church–Turing, automata, complexity and detailed computability in `B1.5-C02`.
4. Open Logic source identity: active provenance is now deterministic `HKA-SRC-73f520eedb8e`, pinned to exact upstream commit `OpenLogicProject/OpenLogic@1e960beff9ed7835bf3e3f1335e21af3439cd107`. The two moving OLP sources remain historical only and have zero active claim/node references.
5. 32/32 LO support audit: `CLAIM_TO_LEARNING_OBJECTIVE_CLOSURE.jsonl` contains exactly one record per objective; every record has `SUPPORTED_BY_CLAIMS=true` and `requires_unlocked_scope_claims=false`. B1.5 references appear only as boundary references where R04 matters.

The independent closure audit also found and repaired minimum factual gaps for first-order term/formula syntax, equivalence-relation/function-property definitions, and mechanized proof versus program-verification ownership. These are closure claims, not new scope expansion.

## R04 and stage boundary

`B1.5-C02` retains detailed computability/formal-language/automata ownership and `B1.5-C04` retains program verification/formal methods. Existing `OVERLAP_REVIEW` cross-links remain unchanged and do not transfer primary ownership.

No B1.1-C02, Lesson Registry, image prompt/image, R2, delivery, website, or `ACADEMIC_LOCKED` artifact has been authored.

## Remaining work

Re-read the current control-plane, run the final committed pre-PASS audit against all original and Director-added gates, write `CP06-REPAIR-PRE-PASS-AUDIT`, then finalize `RESULT.json`, `STATUS.json`, `REPORT.md` and `HANDOFF.md` only if every gate remains PASS.

C02 remains locked until an independent Director accepts the repaired C01 result.
