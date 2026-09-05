# V2.20R.1 Fairness Shadow-Production Integration — SOURCE READY

Date: 2026-09-05 (Asia/Ho_Chi_Minh)

V2.19 native fairness has passed admission. This checkpoint records the next integration candidate only; V2.20 runtime admission is NOT yet proven.

Runner:
`RUN_SIGMA_V220R1_FAIRNESS_SHADOW_PRODUCTION_INTEGRATION_PREFLIGHT.sh`

Runner SHA256:
`43554f0b4f1adf7bd203f1233df51917b00c9c5f474364bf3d217d92c5682fdf`

Static:
- `bash -n` RC = 0.

Integration contract:
1. reproduce the real first-work starvation path in an isolated shadow BRAIN;
2. V2.19 must persist exact `first::|||::EXECUTE_REVISIT` as pending and schedule `SELECT_NEXT_WORK`;
3. a fresh host process must recover the persisted scheduled event before dispatch;
4. native selector must select the real second work;
5. second work must complete its admitted real `REOBSERVED -> ARCHIVE_FOR_NOW` cycle;
6. on the second work scheduling turn, V2.19 must resume the exact pending first-work `|||::EXECUTE_REVISIT`;
7. a fresh host process must again recover that persisted resumed event before execution;
8. resumed generation `|||` must execute to completion with exact cycle identity preserved;
9. if first remains unresolved and generates `||||::EXECUTE_REVISIT`, V2.19 must defer it again;
10. selector must then advance to the real third work;
11. production V2.4 must remain running with the same runner PID throughout;
12. shadow mutable state must remain under the separate V2.20 BRAIN namespace.

Expected bounded claim only after runtime PASS:
`REAL_SHADOW_ANTI_STARVATION_INTEGRATION=PROVEN_IN_FIRST_SECOND_THIRD_WORK_SCOPE`

Production promotion remains forbidden after V2.20 alone. Remaining blockers include long-horizon shadow stability and mid-write crash atomicity.

Global limits remain:
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`
- `BOUNDED_FILE_IO=NOT_PROVEN`
- `MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`
- keep production V2.4 running unchanged.
