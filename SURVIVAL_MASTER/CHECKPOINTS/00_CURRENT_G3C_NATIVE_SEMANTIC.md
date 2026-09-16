# START HERE — CURRENT G3C SEMANTIC R2 VS R4 WORK

Do not rescan old windows.

## PRIMARY MISSION — THIS OVERRIDES ANY BROADER WORDING BELOW

The first and controlling responsibility of this workstream is:

```text
CONTINUE TRAINING + TESTING SEMANTIC R2 CANDIDATE
TO DETERMINE WHETHER SEMANTIC R2 CAN REPLACE THE CURRENT R4 SEMANTIC CORE.
```

Everything else is subordinate to that decision.

That means:

```text
R2 is the candidate under training/evaluation.
R4 is the current core/baseline to be replaced only if R2 proves better.
Shadow/candidate is the laboratory.
Native VM09 is execution authority for authoritative learning/eval.
No host/Bash semantic verdict.
No canonical mutation or R2->R4 cutover without explicit SIGMA admission.
Build PASS is not enough.
Training improvement is not enough.
R2 must demonstrate real semantic uplift, blind generalization, and no unacceptable regression before replacement is considered.
```

Read the full checkpoint for experiment history and command templates:

```text
SURVIVAL_MASTER/CHECKPOINTS/G3C_NATIVE_SEMANTIC_SHADOW_CHECKPOINT_20260917.md
```

Also read the mission correction, which supersedes the earlier generic responsibility wording in that checkpoint:

```text
SURVIVAL_MASTER/CHECKPOINTS/G3C_SEMANTIC_R2_REPLACE_R4_PRIMARY_MISSION.md
```

New pane/session:

```bash
source "$HOME/SIGMA/sigma_genesis1/.sigma_ail/coordination/SESSION_R4/shell/sigma-session.bash"
sigma-session "Resume G3C Semantic R2 training and evaluation to determine whether R2 can replace current R4 semantic core; Native VM09 authority; shadow only; no canonical cutover without explicit SIGMA admission"
```

If the pane already has a session:

```bash
sigma-session status
```

Immediate evaluation state recorded before this correction:

```text
Best training-side shadow: R13M mass-preserving semantic metric.
Blind Generalization 001 already executed.
Blind Generalization 002 was frozen and was the next pending blind evaluation.
Do not treat R13M as final R2 replacement proof.
The final decision question remains: IS SEMANTIC R2 ACTUALLY BETTER THAN CURRENT R4 ENOUGH TO REPLACE IT?
```

Native authority:

```text
./native/sigma-vm.v09_candidate
SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99
```

Compiler:

```text
./native/sigmac
SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71
```

Canonical baseline:

```text
CANONICAL_HEAD=700d5c1b4845322d7c14800029c629b0
MODEL_SHA256=70da3e9e719ae0e72e88add59d6b7752fe732319b8fc7590170a050ef860005e
```

Do not rediscover the system. Resume from the checkpoint, but keep the R2-vs-R4 replacement decision as the primary mission at all times.
