# C5V3 Autonomous Integration Plan

This document is authoritative for connecting the M5 successor candidate back into the automatic C5V3 program. It does not authorize production cutover by itself.

## Goal

After the required M5 capability and blind gates are complete, integrate the successor into the existing C5V3 autonomous loop without reintroducing legacy LEFT/RIGHT cognition, host semantic substitution, English grammar hardcoding, or source-hoarding.

Target automatic loop:

`native state -> native gap -> native evidence/search request -> mechanical host transport -> raw Internet source/provenance -> native ingest -> native whole-work reasoning -> native bounded semantic compression -> local persistence -> restart -> continued learning`

## Integration phases

### S0 — Read-only synchronization

- Freeze and fingerprint production core, runner, ingress, supervisor, sigmac and VM.
- Audit the real C5V3 event/input/output/state ABI.
- Map candidate events/state namespaces onto the automatic runner without changing production.
- Production remains read-only and active.

### S1 — Isolated graft

- Build a new C5V3 successor candidate containing only admitted M5 capabilities and any later whole-work/memory capabilities that passed their own gates.
- Use isolated runtime/state/store paths.
- Compile with locked sigmac and run with locked VM.
- Re-run all admitted regression and anti-hardcode gates.
- No production binding.

### S2 — Autonomous-runner shadow

- Run the candidate under a copy of the C5V3 autonomous orchestration path.
- Feed the same class of incoming work/events without allowing candidate writes to production state.
- Tool/network calls must originate only from native candidate requests.
- Compare stability, boundedness, restart/recovery and request isolation; do not require cognitive outputs to mimic legacy C5V3.

### S3 — Soak and recovery

- Long-running automatic loop over multiple sources/works.
- Repeated restart/recovery tests.
- State integrity, bounded memory, source deletion after admitted compression, provenance retention and continual-learning tests.
- Network/tool failures must not corrupt native memory or cause host fallback cognition.
- Maintain rollback-ready old production artifacts.

### S4 — Promotion gate

Promotion requires the production subset defined in `END_STATE_ACCEPTANCE.md` plus operational stability. At minimum, no known blind failure that invalidates the intended production claim may be hidden or waived.

Promotion is not cutover.

### S5 — Explicit cutover

Only after explicit user authorization:

- stop or drain old automatic runner in a controlled manner;
- bind the promoted successor runner/core/state paths;
- verify exact hashes and first-run health;
- retain rollback path to the old C5V3.

### S6 — Rollback

If the promoted successor violates state integrity, boundedness, tool boundary, recovery or accepted cognition behavior, restore the old C5V3 production binding without rewriting historical evidence.

## What must never happen during integration

- No hot-patching the live production core during admission.
- No copying candidate test state into production as if it were learned knowledge.
- No host-generated query, summary, belief, theme, value, support/conflict/truth decision or memory selection.
- No reintroduction of token LEFT/RIGHT, adjacency-as-meaning or fixed lexical/grammar tables.
- No calling structural correlation `understanding` merely because orchestration runs automatically.

## Current synchronization status

As of 2026-09-09, production binding remains NO. Mechanical tool transport R2 has returned runtime Stage-1 RC=0 on Oppo; independent blind host-substitution is being corrected after an evaluator fixture-ID bug. Real Internet, whole-work understanding, semantic compression, multilingual narrative transfer and continual compressed-memory learning still require their own gates before final production claims.
