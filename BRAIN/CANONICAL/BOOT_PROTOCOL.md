# SIGMA COGNITIVE BOOT PROTOCOL v1.0

Boot is state reconstruction, not greeting generation.

## Sequence

1. Verify `ROOT_OF_TRUST.json`.
2. Load `LINEAGE.json`; identify the state parent and branch.
3. Load `DO_NOT_RERUN_LOCKS.json` before executing any work.
4. Load `CURRENT_STATE.json`.
5. Verify the 512 canonical contract.
6. Discover exactly 54 DNA cores from the repository, not from memory.
7. Discover runtime capabilities and resource limits.
8. Load active goals, open loops, unresolved contradictions and unknowns.
9. Run diagnostic probes; do not ask the model to self-certify capability.
10. Read `NEXT_ACTION.md` and select only an action compatible with authority and preconditions.
11. Execute in the least-side-effect mode possible.
12. Verify result from reality/runtime evidence.
13. Append/update state; never rewrite immutable event history.
14. Mirror canonical state to available persistence targets.
15. Continue the loop or enter safe shutdown.

## Required boot output

A boot report must distinguish:

- `STRUCTURAL_PASS`
- `RUNTIME_EVIDENCE_PASS/PARTIAL/HOLD/FAIL/NOT_AUDITED`
- `AVAILABLE_CAPABILITIES`
- `MISSING_DEPENDENCIES`
- `ACTIVE_GOAL`
- `NEXT_EXECUTABLE_ACTION`

A structural PASS is never a claim of AGI or complete implementation.
