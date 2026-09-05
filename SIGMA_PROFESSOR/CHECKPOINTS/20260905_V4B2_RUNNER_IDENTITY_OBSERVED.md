# V4-B2 runner identity observed on Termux

Date: 2026-09-05 (Asia/Ho_Chi_Minh)

User installation evidence:

- `REMOTE_SIGMA_LIFE=d939e52b664b9dedfdd30e614661a8a71f8be392`
- runner Git blob expected/actual: `6ea6a0269bcbe00ca44238a66c60c61d9b603e65`
- `V4B2_RUNNER_INSTALL=PASS`
- canonical Termux-observed runner SHA256: `a0edc04b61fa6ba308f7e69b78a0ea9516bbd90a8e684c91e56029cec4a2365a`

Classification:

- runner bytes identity: PASS
- runner SHA256 identity: observed and pinned
- V4-B2 runtime: NOT YET RUN at this checkpoint
- production V2.4 state: untouched by this installation step

Next action:

Run `SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V4B2_REAL_V24_RC9_HELD_CONTEXT_REPLAY_PREFLIGHT.sh` as a separate process (not sourced). Preserve all five real-context replay outcomes and production V2.4 PID before/after.
