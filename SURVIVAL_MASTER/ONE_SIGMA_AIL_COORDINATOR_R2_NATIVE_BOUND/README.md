# ONE SIGMA.AIL Brain Coordinator R2 — Native-bound

R2 corrects the R1 boundary: it does **not** create a second canonical brain HEAD or second runtime writer lock.

Canonical runtime authority is the already-promoted Oppo `.sigma_ail` surface:

- `.sigma_ail/BRAIN_HEAD` — symlink alias to active R3 state `HEAD`.
- `.sigma_ail/WRITER.lock` — symlink alias to the active R3 native writer lock.
- `.sigma_ail/MODEL_GENERATION` — roadmap model generation maintained by accepted SIGMA-native generation transitions.

The coordinator only owns registration, one coordination lease, per-operation authorization, admission receipt binding, worker status, and completed-receipt acceptance. The native R3 transaction advances the runtime HEAD while holding the native writer lock. `complete` accepts a result only when the reported `NEW_HEAD` already equals the live Oppo `.sigma_ail/BRAIN_HEAD`.

Required invariants:

- `ONE_SIGMA_AIL=YES`
- `ONE_WRITER=YES`
- `UNREGISTERED_WRITER=REJECT`
- `STALE_HEAD_WRITER=REJECT`
- `CONFLICTING_LEASE=REJECT`
- `HOST_COGNITION=NO`
- `NO_STATE_FORK=MANDATORY`

Activation sequence: `verify-runtime` -> `attach <receipt>` -> register admission evidence -> workers use `register` + `authorize` + native task + `complete`.

R2 refuses to operate if R1 parallel canonical state exists under `.sigma_ail/coordination/CANONICAL`.
