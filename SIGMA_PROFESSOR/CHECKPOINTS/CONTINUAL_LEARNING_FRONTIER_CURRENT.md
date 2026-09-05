# CONTINUAL-LEARNING FRONTIER — CURRENT

Updated: 2026-09-05 (Asia/Ho_Chi_Minh)

Repository STOP-GATE applies. Read `/AGENTS.md` and `00_SIGMA_SESSION_BOOTSTRAP_NATIVE_EXECUTION_FLAG_V1.md` first.

## Last admitted milestone

V2.22R.1 crash-consistent transaction journal — PASS.

Checkpoint:
`8b0a2e97e7918e2d99894fb6255192cd190524f2`

Admitted claim:
`CRASH_CONSISTENT_JOURNAL_RECOVERY=PROVEN_UNDER_INJECTED_TRUNCATED_TAIL_FAULTS`

Still:
`MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`
`PHYSICAL_FILESYSTEM_ATOMICITY=NOT_CLAIMED`
`PRODUCTION_PROMOTION_ALLOWED=NO`

## Current candidate

V2.23R.1 — journal-wrapped real shadow scheduled intent.

Canonical runner:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V223R1_JOURNAL_WRAPPED_REAL_SHADOW_SCHEDULED_INTENT_PREFLIGHT.sh`

Canonical Git blob SHA:
`c4d2c9790d505041ee71cfaafaf77365af790865`

README correction commit:
`445b9dfc7d36bde14428c04be9a60af482bbfd16`

Source-ready checkpoint:
`20ecf519d3b011f7837495da3e68371f8c248097`

Canonical-identity correction checkpoint:
`228988ca333f821cb3e8a7842bb5946f8ebd58ff`

The earlier local candidate SHA256 is NONCANONICAL. Before runtime admission, Termux must verify the Git blob identity, then print `sha256sum` for the canonical repository file. That observed SHA256 becomes canonical only after runtime evidence.

## V2.23 required runtime behavior

- real native defer intent committed/recovered through V2.22;
- direct fairness scheduled file cleared before continued dispatch;
- real second work cycle replay;
- real resume intent subjected to torn PREPARE fault;
- native recovery preserves last fully committed defer event;
- retry commits/recover exact resume event;
- recovered event drives native revisit executor byte-for-byte;
- real re-defer intent subjected to torn COMMIT fault;
- native recovery preserves last fully committed resume event;
- retry commits/recover exact re-defer event;
- real third work selected;
- production V2.4 same PID before/after;
- shadow namespace isolated.

Host/Bash may inject fault bytes mechanically only. Native V2.22 decides recovery validity.

## Next after V2.23 PASS

Checkpoint V2.23, then build production-state migration + rollback admission. Do not upgrade V2.4 in place.
