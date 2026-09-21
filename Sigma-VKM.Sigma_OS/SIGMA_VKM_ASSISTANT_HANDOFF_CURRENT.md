# SIGMA-VKM Assistant Handoff — Current

## Purpose
This file is the continuity checkpoint for a new ChatGPT window/context. Read this before continuing SIGMA-VKM public API work.

## Repository
- Repository: SIGMA-UNIVERSE-NATURE/sigma-freedom
- Branch: SIGMA_LIFE
- Evidence directory: Sigma-VKM.Sigma_OS/

## Current verified position
- Legacy public API lock: 300/300
- Extended target: APIs 301–500 (200 APIs)
- Extended proven: 20/200
- Total proven: 320/500
- Last proven API: 320 — Regression Gate
- Group 301–310 Experiment & Reproducibility: PROVEN
- Group 311–320 Evaluation & Benchmark: PROVEN
- Current next API: 321 — Incremental Update
- API 321 specification has been sent to the user but no execution result has yet been received at this checkpoint.

## Locked legacy phase
The 1–300 phase has a FINAL PROVEN LOCK. New APIs must not retroactively redefine the meaning of the locked 300 APIs. Every new API requires:
- SIGMA_VKM_API_<N>_REGRESSION_300_LOCK=PASS
- regression of the immediately preceding API
- no increment of TOTAL_API_PROVEN unless the new API genuinely passes its gate.

## Required workflow for every user result
1. Inspect the pasted Termux output.
2. Do NOT infer PASS merely from individual PASS lines.
3. Require successful process exit (normally RC1/RC2/RC3=0 for hardened proof), zero FAIL, required previous-API regression, legacy 300-lock regression, and deterministic output SHA when specified.
4. If any required gate fails, record a HOLD artifact on GitHub and do NOT increment the API counter or send the next API as implementable work. Give only the exact fix gate.
5. If complete, FIRST save the proof artifact to GitHub under Sigma-VKM.Sigma_OS/.
6. Confirm the GitHub commit to the user.
7. ONLY AFTER GitHub save, issue the concise specification for the next API.
8. Never count hardening as an additional API.
9. Preserve counters exactly:
   LEGACY_API_LOCK=300/300
   EXTENDED_API_PROVEN=(N-300)/200
   TOTAL_API_PROVEN=N/500
10. Prefer Sigma-level implementation. Kernel/C may provide primitives only where Sigma cannot compose the primitive itself. Do not move semantic decisions into the host merely to make tests pass.

## Evidence convention
PASS filename:
SIGMA_VKM_PUBLIC_API_<N>_<NAME>_HARDENED_THREE_RUNS_PASS.txt

HOLD filename:
SIGMA_VKM_PUBLIC_API_<N>_<NAME>_HOLD_<BLOCKER>.txt

Evidence should include:
- acceptance checks
- RC values
- PASS/FAIL counts
- previous API regression results
- 300-lock regression
- all run SHA256 values
- STATUS/DONE/NEXT
- exact counters

## Current API 321 specification
PUBLIC API:
incremental_update(learning_state, evidence)

GOAL:
Update real learning/knowledge state using new evidence without rebuilding the entire state.

OUTPUT:
previous_revision
new_revision
accepted_evidence
state_delta
update_digest
provenance

INVARIANTS:
- valid update increments revision exactly once
- accepted evidence creates a real semantic state delta
- duplicate evidence is not learned twice
- rejected evidence causes no state mutation
- prior knowledge remains present unless explicit revision semantics say otherwise
- independent learning states remain isolated
- provenance links before-state -> evidence -> after-state
- same state + same evidence is deterministic

REQUIRED TESTS:
SIGMA_VKM_API_321_UPDATE_ACCEPT=PASS
SIGMA_VKM_API_321_REVISION_INCREMENT=PASS
SIGMA_VKM_API_321_STATE_DELTA=PASS
SIGMA_VKM_API_321_DUPLICATE_NO_DOUBLE_LEARN=PASS
SIGMA_VKM_API_321_REJECT_NO_MUTATION=PASS
SIGMA_VKM_API_321_PRIOR_KNOWLEDGE_PRESERVED=PASS
SIGMA_VKM_API_321_STATE_ISOLATION=PASS
SIGMA_VKM_API_321_DETERMINISTIC_UPDATE=PASS
SIGMA_VKM_API_321_INVALID_REJECT=PASS
SIGMA_VKM_API_321_PROVENANCE=PASS
SIGMA_VKM_API_321_REGRESSION_300_LOCK=PASS
SIGMA_VKM_API_320_REGRESSION=PASS

PROOF:
3 runs
RC1=RC2=RC3=0
zero FAIL
deterministic output SHA
API320 regression PASS in all runs
legacy 300-lock PASS

AFTER PASS:
LEGACY_API_LOCK=300/300
EXTENDED_API_PROVEN=21/200
TOTAL_API_PROVEN=321/500
DONE=SIGMA_VKM_PUBLIC_API_321_INCREMENTAL_UPDATE_HARDENED_THREE_RUNS_PASS
NEXT=SIGMA_VKM_PUBLIC_API_322_LEARNING_CHECKPOINT

IMPORTANT:
API 321 must produce a real knowledge/state delta. Merely incrementing revision/counters without changing the represented learned state is not sufficient.

## Planned direction
321–330 is Persistent / Incremental Learning. Do not treat API-level PASS as proof that Sigma Owner possesses/uses all capabilities. Owner capability integration requires a separate later gate demonstrating discover -> authorize -> invoke -> compose -> persist -> process restart -> recall/continue, including deny/revocation and real unseen workloads.

## Last GitHub checkpoint before this handoff
API 320 Regression Gate hardened proof commit:
b20f3ea0b943f29c485b1721c9d2189b150cb202
