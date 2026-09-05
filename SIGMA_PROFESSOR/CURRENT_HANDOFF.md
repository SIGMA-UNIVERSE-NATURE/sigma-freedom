# CURRENT HANDOFF — SIGMA_PROFESSOR

Last updated: 2026-09-05 (Asia/Ho_Chi_Minh)

## REPOSITORY-WIDE BOOTSTRAP STOP-GATE

**Before any SIGMA work, every window/session/agent MUST read:**

1. `/AGENTS.md`
2. `SIGMA_PROFESSOR/DIRECTIVES/00_SIGMA_SESSION_BOOTSTRAP_NATIVE_EXECUTION_FLAG_V1.md`
3. `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`
4. this `CURRENT_HANDOFF.md`
5. latest relevant checkpoint

Bootstrap commits installed:

- native-execution directive: `a6a6856a4b233ef47378096f5909b9b084de9485`
- root `AGENTS.md`: `c737721739e9e2fa368bac05fcf592f5146fd1b2`
- `SIGMA_PROFESSOR/README.md` bootstrap update: `209f4c1192417937ed2c2e0974dfb99b3de2d4e2`
- handoff STOP-GATE install: `5cef391ad4d2514c624b5f76c68826d495aeadb3`
- immutable bootstrap checkpoint: `1d12c5e7176a7d703156ccef53573ece87a03ce2`

### Non-negotiable execution boundary

- `SIGMA_EXECUTION_ENGINE=LOCKED_SIGMA_VM_ONLY`
- `ACTIVE_CAPABILITY_IMPLEMENTATION=NATIVE_SIGMA_ONLY`
- `ACTIVE_COGNITION_NATIVE_SIGMA_ONLY=YES`
- `HOST_OR_BASH_AS_SIGMA_EXECUTION_ENGINE=FORBIDDEN`
- `HOST_OR_BASH_COGNITION=FORBIDDEN`
- `HOST_OR_BASH_LEARNING=FORBIDDEN`
- `HOST_OR_BASH_SEMANTIC_INTERPRETATION=FORBIDDEN`
- `HOST_OR_BASH_STAGE_DECISION=FORBIDDEN`
- `HOST_OR_BASH_WORK_SELECTION=FORBIDDEN`
- `HOST_OR_BASH_REVISIT_PRIORITY=FORBIDDEN`
- `HOST_OR_BASH_TRUTH_DECISION=FORBIDDEN`
- `HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN`

Bash/host is **not SIGMA**. It MUST NOT implement or substitute any SIGMA cognitive capability. It may only be an external mechanically transparent harness: invoke locked compiler/VM, move exact bytes/files, print/compare hashes and return codes, create isolated fixtures/fault injections, supervise processes/transport bytes, or dispatch an **exact event/stage already emitted by native SIGMA** without choosing or rewriting it.

- `BASH_MAY_LAUNCH_SIGMA=YES`
- `BASH_MAY_IMPLEMENT_SIGMA_CAPABILITY=NO`
- `HOST_MAY_DISPATCH_EXACT_NATIVE_EVENT=MECHANICAL_ONLY`
- `HOST_MAY_CHOOSE_EVENT_OR_STAGE=NO`

If an old artifact conflicts with this bootstrap flag, treat the old artifact as historical evidence/provenance only. Never weaken this STOP-GATE to preserve old behavior.

## Global invariants

- active cognition = native `.sigma` only;
- `HOST_LEARNING=NO`;
- `HOST_SEMANTIC_INTERPRETATION=NO`;
- `HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN`;
- `ANTI_HARDCODE=ADMISSION_CONTROL_NOT_TOOL_REMOVAL`;
- `DO_NOT_LOAD_RESULTS=YES`;
- `LOAD_CAPABILITIES=YES`;
- runtime proof required;
- failures are evidence; never weaken admission gates;
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`;
- `SEMANTIC_TRUTH_VALIDATION=NOT_PROVEN`;
- `GENERAL_AUTONOMOUS_REASONING=NOT_PROVEN`;
- `GENERAL_AUTONOMOUS_MATHEMATICAL_RESEARCH=NOT_PROVEN`.

## Locked runtime

SIGMAC SHA256:
`65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`

VM v09 candidate SHA256:
`029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

`VM_IS_GENESIS1=NOT_PROVEN`.

Admission transcripts must visibly print and equality-gate both identities.

## Production V2.4

Keep V2.4 running unchanged unless it emits a real VM failure.

Source SHA256:
`6c3764dd9903ab6c9bc1ffe755d4d2784e3a5fe4a4594d969e70bcfe3afb54c2`

`PRODUCTION_V2_4_KEEP_RUNNING=YES`

`UPGRADE_V2_4_IN_PLACE=NO`

## Admitted continual-learning chain

- V2.5B.2 frozen 56-document survey — PASS `dca66b408fba5c21d081983d6ba15ca510e63c2c`.
- V2.6/V2.6F persisted bounded traversal — PASS `81c8c72e66c30292e17c567d8c3824490dc00e7a`, `97b2e047211d6606b0772daf451b6a9c16359946`.
- V2.7/P.1 structural grouping — PASS `3c98031845c42792c3bd58ba049e13013c60160b`.
- V2.8P.1 structural curriculum priority — PASS `5e375d2ffa210852a042d833f061b6cc6c969ecf`.
- V2.8R.1 real-survey native selection — PASS `ce7650b46026b6f4dc553618b198f48d1f1692d3`.
- V2.8D.1 selected work deep re-learn — PASS `a0b3dce9b784ef36e552f377ab2c808e7d80e9d9`.
- V2.9R.1A structural revalidation — PASS `b9dc75e37cf7a72e9851c0ccabd1b53a72c3d235`.
- V2.10R.1 lifecycle — PASS `220fa78bce0d9873533cb8acce102fc411107924`.
- V2.11R.1 revisit execution/archive re-entry — PASS `aa1bec9344510d95dbbee9312076df7ad9975256`.
- V2.12R.1 cycle event controller — PASS `cf08b2faa4c17eb9bfa7a9c6870ea6a9e2138982`.
- V2.13R.1 generation-aware revalidation/lifecycle — PASS `d464511977c85853d05c09419f3102d0fd0db88f`.
- V2.14R.1 generation-aware closed-loop transition — PASS `40408a72286efe677d3cdf472c3d8f59b4bac457`.
- V2.15R.1 first -> second real-work transition — PASS `fd6f8019af60758c2575589a2af1016f8cff2fc1`.
- V2.16R.1 second real-work complete cycle — PASS `04d786edfe832ef501949549d0560e70c8d8b27f`.
- V2.17R.1 real multi-document cycle promotion — PASS `1897b22984ecd095b0475041e9ea0ececf794e2f`.
- V2.18R.1 shadow starvation audit — PASS / production promotion blocked `1e07738afce2bd5f111eb7861ebcdcdf3ab4472c`.
- V2.19R.1 native revisit fairness queue — PASS `e44e84a37168cc193721d80a68cb58f331378280`.
- V2.20R.1 fairness shadow integration — PASS `596a9620a7046d431f89ed5006332c1e1cfa4415`.
- V2.21R.1 long-horizon shadow stability/recovery — PASS `cc2decc32d7aed2c5348333d9857623936a25b09`.
- V2.22R.1 crash-consistent transaction journal — PASS `8b0a2e97e7918e2d99894fb6255192cd190524f2`.

## Key admitted claims

`MULTI_DOCUMENT_AUTONOMOUS_CYCLE=PROVEN_IN_BOUNDED_REAL_CORPUS_SECOND_THIRD_WORK_SCOPE`

`NATIVE_REVISIT_FAIRNESS_QUEUE=PROVEN_IN_BOUNDED_TESTED_SCOPE`

`REAL_SHADOW_ANTI_STARVATION_INTEGRATION=PROVEN_IN_FIRST_SECOND_THIRD_WORK_SCOPE`

`LONG_HORIZON_SHADOW_STABILITY=PROVEN_IN_SIX_BOUNDARY_FOUR_REAL_WORK_SCOPE`

`CRASH_CONSISTENT_JOURNAL_RECOVERY=PROVEN_UNDER_INJECTED_TRUNCATED_TAIL_FAULTS`

## V2.22 admitted runtime evidence

Native source:
`SIGMA_PROFESSOR/artifacts/SIGMA_CRASH_CONSISTENT_TRANSACTION_JOURNAL_V2_22R1.sigma`

Source SHA256:
`643c6f534777193951d772e9653463b5d97ceebb7c35f14b21390a3308ef4c64`

Runner:
`SIGMA_PROFESSOR/artifacts/RUN_SIGMA_V222R1_CRASH_CONSISTENT_TRANSACTION_JOURNAL_PREFLIGHT.sh`

Runner SHA256:
`6038ba6d2a6d4a16cc67c98386227c130fdc2f659c6dd850457b5c0ce4a4be9e`

PASS gates:

- PREPARE_ONLY is not visible as committed;
- prepared transaction resumes to COMMIT after restart;
- torn PREPARE tail ignored + retry recovers;
- torn COMMIT tail ignored + retry recovers;
- garbage tail ignored;
- conflicting valid PREPARE payloads block that transaction;
- fresh-VM idempotent commit;
- deterministic journal replay;
- invalid delimiter refusal;
- journal bound refusal;
- `HOST_TRANSACTION_DECISION=NO`;
- `HOST_RECOVERY_DECISION=NO`;
- `HOST_LEARNING=NO`.

The user-provided final runtime tail did not include the V2.22 bytecode SHA line. Do not invent it.

## Durability claim boundary

V2.22 proves crash-consistent native journal recovery under the injected truncated-tail model. It does **not** prove physical filesystem atomicity.

Keep locked:

- `MID_APPEND_CRASH_ATOMICITY=NOT_PROVEN`
- `PHYSICAL_FILESYSTEM_ATOMICITY=NOT_CLAIMED`
- `BOUNDED_FILE_IO=NOT_PROVEN`

## Promotion status

`PRODUCTION_PROMOTION_ALLOWED=NO`

The next blocker is integration: real shadow scheduled intent has not yet been wrapped by the admitted V2.22 journal under injected torn PREPARE/COMMIT faults.

## Current frontier — journal-wrapped real shadow scheduled intent

Next gate must integrate V2.22 with the real fairness/scheduler chain without moving any cognition to Bash/host.

Required behavior:

1. native fairness/controller produces an exact scheduled event;
2. that exact event becomes the V2.22 transaction payload without reinterpretation;
3. native V2.22 writes/recover-validates the event transaction;
4. inject torn PREPARE and torn COMMIT faults around a real shadow defer/resume intent;
5. fresh recovery must expose only the last fully committed exact native event;
6. retry must commit/recover the intended event exactly;
7. mechanical dispatcher may launch only the exact event recovered by native SIGMA;
8. production V2.4 remains running and shadow state remains isolated.

No host/Bash selection, recovery decision, stage decision, fairness decision, work selection, or learning is permitted.

## TEACHER_GPT language lane pointer

Dedicated living checkpoint:
`SIGMA_PROFESSOR/CHECKPOINTS/TEACHER_GPT_LANGUAGE_LANE_CURRENT.md`

Current admitted language chain:
`LANG-01A -> LANG-01B -> LANG-01C -> LANG-01D -> LANG-01E -> LANG-01F`

Current language status:

- `LANG-01A..LANG-01F=ADMITTED_IN_EXACT_TESTED_STRUCTURAL_SCOPES`;
- latest LANG-01F source SHA256 `1ab0081f904a844d456d7913b522577038cec1b7d62f4f37494bf29a79dc9a59`;
- latest LANG-01F bytecode SHA256 `60edd9ace13f54b826adcd7e89362acddcfaea9a1649845006f52c99dce77a81`;
- LANG-01F final runtime: `21/21` post-VM alignment PASS;
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`;
- `COREFERENCE_RESOLUTION=NOT_PROVEN`;
- next language capability intentionally `NOT_YET_LOCKED`; re-read dedicated checkpoint + latest canon before choosing the next language capability.

This lane does not change the continual-learning production-promotion status.

## NEXT ACTION

1. Re-read `/AGENTS.md` and bootstrap directive before implementation.
2. Keep V2.4 running unchanged.
3. Build the next native-first admission gate wrapping real shadow scheduled intent in V2.22 transaction journal.
4. Fault injection may be mechanical only; native SIGMA must decide validity/recovery.
5. Preserve exact runtime identities, VM_RC, journal hashes, recovered exact events, and shadow/production isolation evidence.
6. If any gate fails, preserve failure evidence and repair only the narrow native capability/integration issue.
