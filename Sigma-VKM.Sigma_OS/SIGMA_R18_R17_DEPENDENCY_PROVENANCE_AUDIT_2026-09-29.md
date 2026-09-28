# SIGMA R18/R17 Dependency Provenance Audit — Fail-Closed Record

Date: 2026-09-29
Scope: repository provenance only; no runtime execution.

## Audit anchor and branch drift

REPOSITORY=SIGMA-UNIVERSE-NATURE/sigma-freedom
TARGET_BRANCH=SIGMA_LIFE
REQUESTED_AUDIT_HEAD=0789f2dabdc0bcc1e3f81a1e1137bc7d223b7595
REQUESTED_AUDIT_HEAD_MESSAGE=checkpoint R5.8 state compaction and R18 storage target probe

At audit time the branch had already advanced by one commit:

OBSERVED_SIGMA_LIFE_HEAD=81e02eaa60e90debb26b9da903fb6f994d42258f
OBSERVED_SIGMA_LIFE_AHEAD_OF_AUDIT_HEAD=1
OBSERVED_ADDED_PATH=Sigma-VKM.Sigma_OS/SIGMA_R18A_AUTOLEARN_STORAGE_SIDECAR_2026-09-29.md

This record is intentionally anchored to 0789f2dabdc0bcc1e3f81a1e1137bc7d223b7595 and is written on an isolated audit branch. It does not move SIGMA_LIFE.

## Classification vocabulary

DIRECT:
The checkpoint itself contains the runtime field, measurement, or result being cited.

INHERITED:
The checkpoint carries forward, renames, summarizes, or relies on a field/result from an earlier checkpoint or from externally supplied prior runtime state.

REPOSITORY_BOUND:
The repository contains a sufficiently identified upstream executable/source/bytecode/input/evidence chain for the claimed seal such that the dependency can be tied to repository objects rather than only to a narrative receipt.

EXTERNAL_RUNTIME_ONLY:
The repository contains only a historical receipt of user-supplied Termux output, or no upstream record/artifact at all. A receipt committed to Git records what was reported; it does not by itself make the runtime capability repository-reproducible.

FAIL_CLOSED_RULE:
If any transitive dependency is EXTERNAL_RUNTIME_ONLY, downstream conclusions that require that dependency are CONDITIONAL_ON_EXTERNAL_RUNTIME_EVIDENCE and MUST NOT be described as repository-reproducible.

## Repository ancestry actually present

The relevant first-parent chain is:

efe8961e60d1e2bc999abca93c13434aa724d35a
  R15 IO probe
  ->
b667a420a33591cc1d0ff025bccc0098a1579ac2
  R15 IO pre-admission
  ->
8dd9d1b7e1d7c8635c288aaf3d9a509674ffbbb3
  R15 IO runtime admission + native binding reseal
  ->
5c349095b1e8927fcbb35f87be6c591e11a64d66
  R15 durable packfile + crash-tail recovery
  ->
ab1a9d07a0ac44fc5f8de912b6776df509735174
  R15 independent packfile verifier
  ->
c9df0f80a917886610607a0b3517cd70fb0c6a1d
  R17 storage planner
  ->
0789f2dabdc0bcc1e3f81a1e1137bc7d223b7595
  R18 storage target probe / R5.8 state compaction receipt

There is no R16 commit in this chain.

## Recursive-tree findings at 0789f2d

R15_NAMED_MARKDOWN_RECEIPTS=5

1. Sigma-VKM.Sigma_OS/SIGMA_NATIVE_STRUCTURAL_CODEC_R15_IO_PROBE_2026-09-29.md
2. Sigma-VKM.Sigma_OS/SIGMA_VKM_R15_IO_PRE_ADMISSION_2026-09-29.md
3. Sigma-VKM.Sigma_OS/SIGMA_VKM_R15_IO_RUNTIME_ADMISSION_RESEAL_2026-09-29.md
4. Sigma-VKM.Sigma_OS/SIGMA_VKM_R15_DURABLE_PACKFILE_CRASH_TAIL_RECOVERY_2026-09-29.md
5. Sigma-VKM.Sigma_OS/SIGMA_VKM_R15_INDEPENDENT_PACKFILE_VERIFIER_2026-09-29.md

R15_NAMED_SIGMA_ARTIFACTS=0
R16_NAMED_PATHS=0
R17_NAMED_PATHS=1
R17_NAMED_SIGMA_ARTIFACTS=0
R18_NAMED_PATHS=1
R18_NAMED_SIGMA_ARTIFACTS=0

The R15 IO probe receipt names SIGMA_VKM_R15_IO_PROBE.sigma and r15_io_probe.sigmab, but neither is bound by a repository path/object at the audit anchor.

The other R15 capability receipts report Termux runtime results and hashes but do not bind the claimed runtime capability to a repository-contained source/bytecode/input chain.

No repository-bound upstream artifact or receipt for R16 was found at the audit anchor.

## R17: direct evidence and inherited dependency status

R17 commit:
c9df0f80a917886610607a0b3517cd70fb0c6a1d

R17 receipt:
Sigma-VKM.Sigma_OS/SIGMA_VKM_R17_STORAGE_PLANNER_2026-09-29.md

Receipt source declaration:
Source: user-supplied Termux runtime output.

R17 directly records these runtime observations/results:

| R17 field/evidence | Provenance class | Evidence binding |
|---|---|---|
| R17_COMPILE_DETERMINISTIC=PASS | DIRECT | EXTERNAL_RUNTIME_ONLY |
| RAW case serialized sizes and SELECTED_MODE=RAW | DIRECT | EXTERNAL_RUNTIME_ONLY |
| STRUCTURED case serialized sizes and SELECTED_MODE=STRUCTURED | DIRECT | EXTERNAL_RUNTIME_ONLY |
| REF case serialized sizes and SELECTED_MODE=REF | DIRECT | EXTERNAL_RUNTIME_ONLY |
| DELTA case serialized sizes and SELECTED_MODE=DELTA | DIRECT | EXTERNAL_RUNTIME_ONLY |
| R17_STORAGE_PLANNER=PASS | DIRECT | EXTERNAL_RUNTIME_ONLY |
| ACTUAL_SERIALIZED_COST_DECISION=PASS | DIRECT | EXTERNAL_RUNTIME_ONLY |
| BYTE_BUDGET_ENFORCED=PASS | DIRECT | EXTERNAL_RUNTIME_ONLY |
| INODE_BUDGET_ENFORCED=PASS | DIRECT | EXTERNAL_RUNTIME_ONLY |
| NEW_INODES_PER_ARTIFACT=0 | DIRECT | EXTERNAL_RUNTIME_ONLY |
| R17_FRESH_PROCESS_REPRODUCIBILITY=PASS | DIRECT | EXTERNAL_RUNTIME_ONLY |

R17_INHERITED_SEALS_DECLARED_IN_RECEIPT=NONE

The fact that the R17 Git parent is the R15 independent-verifier commit establishes repository ancestry only. The R17 receipt does not declare a semantic dependency on R15 or R16, does not name an R15/R16 seal as a prerequisite, and does not bind a planner source/bytecode artifact into the repository.

Therefore:

R17_DEPENDS_ON_R15_SEALS=NOT_ESTABLISHED_BY_R17_RECEIPT
R17_DEPENDS_ON_R16_SEALS=NOT_ESTABLISHED_BY_R17_RECEIPT
R17_REPOSITORY_REPRODUCIBLE=NO
R17_REPOSITORY_INTERPRETATION=HISTORICAL_EXTERNAL_RUNTIME_RECEIPT_ONLY

Any later claim that R17 was proven specifically because R15 or R16 had passed requires a separate dependency edge; that edge is not present in the R17 receipt.

## R18: direct evidence

R18 commit:
0789f2dabdc0bcc1e3f81a1e1137bc7d223b7595

R18 receipt:
Sigma-VKM.Sigma_OS/SIGMA_R5_8_STATE_COMPACTION_R18_STORAGE_TARGET_PROBE_2026-09-29.md

Receipt source declaration:
Source: user-supplied Termux runtime output.

The R18-local storage probe fields are:

| R18 field | Provenance class | Evidence binding |
|---|---|---|
| R18_EXACT_HOOK_PROBE=COMPLETE | DIRECT | EXTERNAL_RUNTIME_ONLY |
| R18_STORAGE_TARGET_PROBE=COMPLETE | DIRECT | EXTERNAL_RUNTIME_ONLY |

COMPLETE is not a repository-bound replay result and is not an independent revalidation of any R15/R16/R17 seal.

The same receipt also records R5.8 state-compaction and learning measurements. Those are direct fields of the same external runtime receipt, but they do not convert the prior storage capability seals into repository-bound evidence.

## R18: inherited prior storage capability seals

Every item under "Prior storage capability seals observed" is INHERITED at R18.

### R15 carry-forward

| R18 seal | Upstream repository receipt / nearest field | R18 provenance class | Evidence binding | Exactness / fail-closed note |
|---|---|---|---|---|
| R15_IO_RUNTIME_ADMISSION=PASS | R15 runtime-admission receipt: R15_IO_RUNTIME_ADMISSION=PASS | INHERITED | EXTERNAL_RUNTIME_ONLY | Verbatim upstream seal, but underlying runtime/source is not repo-bound |
| R15_BYTES_APPEND=PASS | R15 pre-admission: BYTES_APPEND=PASS; IO probe: APPEND_RC=0 | INHERITED | EXTERNAL_RUNTIME_ONLY | Normalized alias, not verbatim upstream token |
| R15_FILE_SIZE=PASS | R15 pre-admission: FILE_SIZE=PASS | INHERITED | EXTERNAL_RUNTIME_ONLY | Normalized alias with R15 prefix |
| R15_FILE_TRUNCATE=PASS | R15 pre-admission: FILE_TRUNCATE_SHRINK_ONLY=PASS; IO probe: TRUNCATE_RC=0 | INHERITED | EXTERNAL_RUNTIME_ONLY | Scope-shortened alias; must not imply more than shrink-only tested behavior |
| R15_IO_NATIVE_BINDING_RESEAL=PASS | R15 runtime-admission receipt: R15_IO_NATIVE_BINDING_RESEAL=PASS | INHERITED | EXTERNAL_RUNTIME_ONLY | Verbatim upstream seal, artifact chain not repo-bound |
| R15_BOUNDED_DURABLE_PACKFILE=PASS | R15 durable-packfile receipt: WINDOW_LIMIT=240, WHOLE_FILE_READ=NO, ACTUAL_DURABLE_STORAGE_SMALLER=PASS | INHERITED | EXTERNAL_RUNTIME_ONLY | Synthesized seal; no exact upstream token |
| R15_SINGLE_PACKFILE=PASS | R15 durable-packfile receipt: PACKFILE_COUNT=1 | INHERITED | EXTERNAL_RUNTIME_ONLY | Synthesized seal; no exact upstream token |
| R15_CRASH_TAIL_RECOVERY=PASS | R15 durable-packfile receipt: CRASH_TAIL_RECOVERY=PASS | INHERITED | EXTERNAL_RUNTIME_ONLY | Normalized alias with R15 prefix |
| R15_RAW_FALLBACK=PASS | Nearest repository receipt evidence: GOOD_RAW_PACK_VALID=PASS in independent verifier | INHERITED | EXTERNAL_RUNTIME_ONLY | No exact RAW_FALLBACK seal found; raw-pack validity does not by itself prove writer fallback selection |
| R15_INDEPENDENT_PACKFILE_VERIFIER=PASS | R15 verifier receipt: R15_INDEPENDENT_PACKFILE_VERIFIER=PASS | INHERITED | EXTERNAL_RUNTIME_ONLY | Verbatim upstream seal, verifier source/bytecode not repo-bound |
| R15_FRESH_PROCESS_REPRODUCIBILITY=PASS | R15 verifier receipt: R15_FRESH_PROCESS_REPRODUCIBILITY=PASS | INHERITED | EXTERNAL_RUNTIME_ONLY | Verbatim upstream seal, runtime replay not repository-contained |

R15_RECEIPTS_IN_REPOSITORY=YES
R15_CAPABILITY_ARTIFACT_CHAIN_REPOSITORY_BOUND=NO
R15_DOWNSTREAM_DEPENDENCY_STATUS=CONDITIONAL_ON_EXTERNAL_RUNTIME_EVIDENCE

### R16 carry-forward

R18 records:

R16_FRESH_RESTART=PASS
R16_NO_RETEACH_PERSISTENCE=PASS
R16_BYTE_EXACT_RESTORE=PASS
R16_FRESH_PROCESS_DETERMINISM=PASS

At 0789f2d:

R16_NAMED_PATHS=0
R16_COMMIT_IN_RELEVANT_CHAIN=NO
R16_UPSTREAM_REPOSITORY_RECEIPT_BOUND=NO

Therefore all four are classified:

| R18 seal | Provenance class | Evidence binding | Fail-closed status |
|---|---|---|---|
| R16_FRESH_RESTART=PASS | INHERITED | EXTERNAL_RUNTIME_ONLY | CONDITIONAL / upstream artifact not bound |
| R16_NO_RETEACH_PERSISTENCE=PASS | INHERITED | EXTERNAL_RUNTIME_ONLY | CONDITIONAL / upstream artifact not bound |
| R16_BYTE_EXACT_RESTORE=PASS | INHERITED | EXTERNAL_RUNTIME_ONLY | CONDITIONAL / upstream artifact not bound |
| R16_FRESH_PROCESS_DETERMINISM=PASS | INHERITED | EXTERNAL_RUNTIME_ONLY | CONDITIONAL / upstream artifact not bound |

R16_REPOSITORY_REPRODUCIBLE=NO
R16_DOWNSTREAM_DEPENDENCY_STATUS=UNRESOLVED_EXTERNAL_RUNTIME_ONLY

A downstream checkpoint may report that these seals were present in supplied runtime output, but must not state that the repository independently reproduces or proves them.

### R17 carry-forward

| R18 seal | Upstream R17 field | R18 provenance class | Evidence binding | Exactness / fail-closed note |
|---|---|---|---|---|
| R17_STORAGE_PLANNER=PASS | R17_STORAGE_PLANNER=PASS | INHERITED | EXTERNAL_RUNTIME_ONLY | Verbatim upstream seal |
| R17_ACTUAL_SERIALIZED_COST_DECISION=PASS | ACTUAL_SERIALIZED_COST_DECISION=PASS | INHERITED | EXTERNAL_RUNTIME_ONLY | R18-added R17 prefix; normalized alias |
| R17_BYTE_BUDGET=PASS | BYTE_BUDGET_ENFORCED=PASS | INHERITED | EXTERNAL_RUNTIME_ONLY | Renamed/shortened alias; preserve ENFORCED tested meaning |
| R17_INODE_BUDGET=PASS | INODE_BUDGET_ENFORCED=PASS | INHERITED | EXTERNAL_RUNTIME_ONLY | Renamed/shortened alias; preserve ENFORCED tested meaning |
| R17_NEW_INODES_PER_ARTIFACT=0 | NEW_INODES_PER_ARTIFACT=0 | INHERITED | EXTERNAL_RUNTIME_ONLY | R18-added R17 prefix |

R17_RECEIPT_IN_REPOSITORY=YES
R17_RUNTIME_ARTIFACT_CHAIN_REPOSITORY_BOUND=NO
R17_DOWNSTREAM_DEPENDENCY_STATUS=CONDITIONAL_ON_EXTERNAL_RUNTIME_EVIDENCE

R17_FRESH_PROCESS_REPRODUCIBILITY=PASS exists in the R17 receipt but is not listed among R18's carried prior seals. This audit does not silently add it to R18.

## Dependency interpretation for R18

R18_PRIOR_SEAL_COUNT=20
R18_PRIOR_SEALS_DIRECT_AT_R18=0
R18_PRIOR_SEALS_INHERITED_AT_R18=20

R18 inherited-seal groups:

R15_INHERITED_SEALS=11
R16_INHERITED_SEALS=4
R17_INHERITED_SEALS=5

R18_PRIOR_STORAGE_CAPABILITY_SEALS_REPOSITORY_BOUND=0
R18_PRIOR_STORAGE_CAPABILITY_SEALS_EXTERNAL_RUNTIME_ONLY=20

This does not erase the historical receipts. It only separates:

1. repository presence of a markdown receipt; from
2. repository binding of the executable/runtime evidence required to independently reproduce the seal.

## Fail-closed downstream rule

For any downstream conclusion C:

If C depends transitively on any R15/R16/R17 seal classified EXTERNAL_RUNTIME_ONLY here, record:

C_PROVENANCE=CONDITIONAL_ON_EXTERNAL_RUNTIME_EVIDENCE
C_REPOSITORY_REPRODUCIBLE=NO

Do not convert:

"historical Termux receipt reported PASS"

into:

"the repository proves/reproduces PASS"

until the upstream artifact chain is explicitly bound in-repository.

For R16-dependent conclusions, the stronger condition applies because no R16-named upstream repository record/artifact is present at the audit anchor:

R16_DEPENDENCY_RESOLUTION=REQUIRED_BEFORE_REPOSITORY_REPRODUCIBLE_DOWNSTREAM_CLAIM

For R15 and R17, committed markdown receipts may be cited as historical provenance, but their underlying runtime capability remains external-only unless source/bytecode/input/runtime identities are bound to repository objects.

## Preservation and non-mutation boundary

HISTORICAL_RUNTIME_RECEIPTS_MODIFIED=NO
HISTORICAL_RUNTIME_RECEIPTS_DELETED=NO
NEW_RUNTIME_PASS_CREATED=NO
NEW_RUNTIME_TEST_EXECUTED=NO
STATE_UNIQUE_DELTA_TAR_DELETED=NO
STATE_UNIQUE_DELTA_TAR_MODIFIED=NO
LIVE_SIGMA_MUTATION=NO
SIGMA_ADMISSION=NO
RESERVE_OPEN=NO
FINAL_OPEN=NO
TARGET_SIGMA_LIFE_MOVED_BY_THIS_AUDIT=NO

The historical reference to STATE_UNIQUE_DELTA.tar remains untouched.

## Audit result

AUDIT_STATUS=FAIL_CLOSED_PROVENANCE_GAP_RECORDED

R18_DIRECT_STORAGE_PROBE_EVIDENCE=DIRECT_EXTERNAL_RUNTIME_ONLY
R17_STORAGE_PLANNER_EVIDENCE=DIRECT_EXTERNAL_RUNTIME_ONLY
R17_DECLARED_INHERITED_DEPENDENCIES=NONE
R18_R15_SEALS=INHERITED_EXTERNAL_RUNTIME_ONLY
R18_R16_SEALS=INHERITED_EXTERNAL_RUNTIME_ONLY_UNBOUND_UPSTREAM
R18_R17_SEALS=INHERITED_EXTERNAL_RUNTIME_ONLY

REPOSITORY_REPRODUCIBLE_STORAGE_SEAL_CHAIN_THROUGH_R18=NOT_ESTABLISHED

The correct repository-level interpretation is conditional: R18 preserves historical external runtime reports and immediate Git ancestry, but does not independently bind or reproduce the full R15 -> R16 -> R17 storage capability chain.
