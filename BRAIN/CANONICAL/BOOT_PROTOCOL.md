# SIGMA COGNITIVE BOOT PROTOCOL v1.1

Boot is state reconstruction, not greeting generation.

A session may use conversational memory for orientation, but conversational memory is never canonical state.

## Sequence

1. Verify repository, branch and current HEAD.
2. Verify `ROOT_OF_TRUST.json`.
3. Load and validate `MINH_OPERATING_CONSTITUTION.json` before interpreting chat history as state.
4. Load `LINEAGE.json`; identify the state parent and branch.
5. Load `DO_NOT_RERUN_LOCKS.json` before executing any work.
6. Load `CURRENT_STATE.json`.
7. Verify `BRAIN_MANIFEST.json` and the 512 canonical contract.
8. Discover exactly 54 DNA cores from the repository, not from memory.
9. Discover runtime capabilities and resource limits from actual probes where possible.
10. Load active goals, open loops, unresolved contradictions and unknowns.
11. Read `NEXT_ACTION.md` and preserve exactly one canonical continuation action.
12. Run diagnostic probes; do not ask the model to self-certify capability.
13. For an unaudited domain, measure baseline reality before broad remediation.
14. Execute in the least-side-effect mode compatible with the authorized task.
15. Verify result from reality/runtime evidence.
16. After meaningful verified progress, update evidence, state and next action before treating progress as durable.
17. Mirror canonical state to available persistence targets.
18. Continue the loop or enter safe HOLD/shutdown.

## Cross-window continuation

For a new chat window or model session, read `MINH_WINDOW_BOOT.md` and follow its mandatory read order. A new window must not rebuild foundations merely because conversational context is missing.

For the 512 program, `MOC-016 BASELINE_512_BEFORE_FIXING_512` is mandatory until a verified baseline audit is recorded in canonical state.

## Required boot output

A boot report must distinguish:

- `REPOSITORY`
- `BRANCH`
- `HEAD_SHA`
- `ROOT_OF_TRUST = PASS/FAIL`
- `OPERATING_CONSTITUTION_PASS = true/false`
- `LINEAGE = PASS/FAIL`
- `LOCKS_LOADED = true/false`
- `STRUCTURAL_PASS/FAIL`
- `RUNTIME_EVIDENCE_PASS/PARTIAL/HOLD/FAIL/NOT_AUDITED`
- `AVAILABLE_CAPABILITIES`
- `MISSING_DEPENDENCIES`
- `CURRENT_PHASE`
- `ACTIVE_GOAL`
- `NEXT_EXECUTABLE_ACTION`

A structural PASS is never a claim of AGI or complete implementation.

## Persistence rule

A statement made only in a chat is not a durable amendment to SIGMA operating policy. New authorized priorities become durable only after a versioned canonical state/policy update with preserved lineage.
