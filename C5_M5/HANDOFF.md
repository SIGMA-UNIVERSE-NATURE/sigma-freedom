# SIGMA C5 M5 — Window Handoff

Read in order:

1. `C5_M5/MISSION.md`
2. `C5_M5/END_STATE_ACCEPTANCE.md`
3. `C5_M5/TWO_GATE_ARCHITECTURE.md`
4. `C5_M5/NATIVE_TOOL_RUNTIME_ARCHITECTURE.md`
5. `C5_M5/C5V3_AUTONOMOUS_INTEGRATION_PLAN.md`
6. `C5_M5/STATUS.md`
7. `C5_M5/CHECKPOINTS.md`
8. this file

## Authoritative routing

### Gate A — M5 TEST

`cognition/memory -> continual learning -> revision/support/conflict -> new independent blind tests`

### Gate B — C5 <-> C5V3/M5 synchronization/tool substrate

`read-only synchronization -> SIGMA-native tool substrate -> VM/native library/mechanical ABI -> boundary regression -> S1 -> S2 -> S3 -> promotion -> explicit cutover`

The gates may run in parallel. Gate B operational success cannot waive a Gate A cognition FAIL.

## Latest admitted Gate A core

`M5_NATIVE_CONTINUAL_COMPACT_WORK_MEMORY_R1`

Core SHA256:

`69ec3e26ef857976c257724fa5691210bf2fe1ad3695e085dcd2a2bc9fa0db47`

Oppo bytecode SHA256:

`642b5902dc55944a764704c56b806bc711b570b002cf5628e501bb3b1cacd59b`

R1H1 admission + independent blind both PASS, `RC=0`.

Admitted exact scope:

- Work A archived as detached self-contained compact local memory;
- learning Work B does not change Work A recall bytes;
- exact archived Work A bank block is byte-for-byte unchanged after Work B;
- A and B remain separately semantically queryable;
- A/B cross-work leakage rejected;
- role reversal rejected;
- bank smaller than raw works;
- raw A/B whole spans excluded;
- raw source A not restored during Work B;
- multi-work restart PASS;
- `CONTINUAL_LEARNING_FROM_COMPRESSED_LOCAL_MEMORY=PASS` only in tested two-work/self-contained compact-memory scope.

Production binding remains NO.

## Current Gate A execution artifact

Run:

`SIGMA_C5_C5V3_M5_SCOPED_REVISION_SUPPORT_CONFLICT_LADDER_R1_BUNDLE.zip`

Hashes:

- target core: `460461d6273145fcedcf20e2c75b97e718ff61a6afa8f71dc8d0812f739f850e`
- admission evaluator: `9896de1de21157b255c88c8f01107ab03eb16a3b677f8a6d898857fcbbb582b4`
- independent blind evaluator: `661b69a3944f40a28dc6a0b309a162480859308673ff7227d12d76741ef526d4`
- ladder runner: `b698df3d83367a70dae1146b426e7ca8f394fe885b3588bd2f50cad7200e8a59`
- ladder bundle: `209c5221eac20a3fb5376ed11b9139f3d1116affe4b5efc6a749782f5395b4a1`

## Candidate semantics

Revision scope is legal only when SIGMA already has an open native relation-discrimination gap. Candidate A/B are copied from that gap; Host does not create a support/conflict stance or held belief.

New raw evidence is natively classified as matching A, matching B, ambiguous, or no stance. Within this exact two-candidate discrimination scope:

- evidence on the held candidate = scoped support;
- evidence on the competing candidate = scoped conflict;
- evidence on neither candidate = no stance, not conflict;
- same-source duplicates do not increase authority;
- revision occurs only when distinct-source support for the competitor reaches the threshold and strictly exceeds held-side support.

Admission additionally rejects opening a revision scope without a native gap.

Independent blind uses a different randomized gap layout and tests replay idempotence, evidence-ID conflict rejection, irrelevant/no-stance input, protocol injection, work-scope mismatch, same-source conflict, tie non-revision, A->B revision, B->A revision and restart.

## Claim rule if PASS

Advance only:

`NATIVE_SCOPED_SUPPORT_CONFLICT_REVISION=PASS`

in the native-gap/provenance scope.

Keep FAIL:

- `BROAD_SEMANTIC_SUPPORT_CONFLICT_TRUTH`
- arbitrary natural-language logical contradiction/truth
- autonomous free-form summary generation
- zero-shot low-overlap summary
- broad whole-work understanding
- theme/human-value induction
- multilingual transfer
- unbounded lifelong capacity
- production binding.

## After PASS

Next Gate A step: internalize the revised hypothesis into compact/archived memory and test later revision after raw working evidence is removed. Only then broaden incompatibility/truth semantics with separate blind tests.

Gate B remains independent and may continue synchronization/tool substrate/VM/native library/S1-S3 while production stays read-only until the shared convergence gate and explicit cutover authorization.