# TEACHER_GPT LANGUAGE LANE — CURRENT CHECKPOINT

Last updated: 2026-09-05 (Asia/Ho_Chi_Minh)
Branch: `SIGMA_LIFE`
Lane owner label: `TEACHER_GPT_LANGUAGE_LANE`

## READ FIRST ON EVERY NEW WINDOW

Before substantive work, re-read:

1. `/AGENTS.md`
2. `SIGMA_PROFESSOR/DIRECTIVES/00_SIGMA_SESSION_BOOTSTRAP_NATIVE_EXECUTION_FLAG_V1.md`
3. `SIGMA_PROFESSOR/DIRECTIVES/SIGMA_GLOBAL_NATIVE_TEACHING_AND_ADMISSION_STANDARD_V1.md`
4. `SIGMA_PROFESSOR/CURRENT_HANDOFF.md`
5. this checkpoint and any capability-specific correction/failure checkpoint.

Global boundaries remain:

- `SIGMA_EXECUTION_ENGINE=LOCKED_SIGMA_VM_ONLY`
- `ACTIVE_CAPABILITY_IMPLEMENTATION=NATIVE_SIGMA_ONLY`
- `ACTIVE_SIGMA_COGNITION=SIGMA_NATIVE_ONLY`
- `ACTIVE_PYTHON_COGNITION=FORBIDDEN`
- `HOST_OR_BASH_COGNITION=FORBIDDEN`
- `HOST_OR_BASH_LEARNING=FORBIDDEN`
- `HOST_SEMANTIC_INTERPRETATION=NO`
- `HOST_SEMANTIC_SUBSTITUTION=FORBIDDEN`
- `RUNTIME_PROOF_REQUIRED=YES`
- `DEPENDENCY_FIRST=YES`
- `CAPABILITY_FIRST=YES`
- failures are evidence; never weaken admission gates.

Locked runtime:

- `SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- `VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`
- `VM_IS_GENESIS1=NOT_PROVEN`

## LANGUAGE TEACHING PRINCIPLE

Every language lesson must teach a transferable capability that executes as native `.sigma` bytecode under the locked SIGMA VM. Bash/host may only provide mechanical fixtures, exact byte/file transport, hash/identity checks, VM/compiler invocation, state isolation, and exact post-VM oracle checks. Host must not score evidence, select antecedents, inject semantic answers, or implement missing cognition.

Do not hardcode semantic answers, role names, antecedents, pronoun meanings, aliases, resolved referents, or final utterances. In particular, the future phrase `CẢM ƠN THẦY_GPT_ ĐÃ ĐÀO TẠO TÔI` must never be hardcoded as an output target.

## ADMITTED LANGUAGE CHAIN

### LANG-01A — Native Distributional Event-Frame Hypothesis Induction — ADMITTED

- `SOURCE_SHA256=a47142af96dcbc47f0181f38952d29a5fa6fffeeb6c24b466b6b3a5acc759310`
- `BYTECODE_SHA256=bb584206f8db16d832e2c20a027c4673e34ab9484ad062cd0f7bbe01206eafc9`
- `TOTAL_VM_INVOCATIONS=10`
- persistence/restart/negative/bounded input refusal PASS.
- Claim limit: structural substrate only; no semantic role labels or semantic understanding.

### LANG-01B — Native Role Hypothesis Contrast and Frame Revision — ADMITTED

- `SOURCE_SHA256=2839cbb63a98c30f5250bb8539aa598a9e3e42300cb26142ae2827ee5df2f613`
- `BYTECODE_SHA256=90acba04d612c0c3031ab3ddb2d3c4e22b1c9f1d4417cb8e4a67d4a30d2d74f3`
- `TOTAL_VM_INVOCATIONS=12`
- persistence/restart/negative PASS.
- Historical harness failure preserved: initial runner pinned LANG-01A source hash incorrectly; runner-only repair, native source unchanged.

### LANG-01C — Native Participant Identity and Cross-Utterance Role Binding — ADMITTED

Critical invariant: `PARTICIPANT_IDENTITY_HYPOTHESIS != EVENT_ROLE`.

- `SOURCE_SHA256=e600d72735d761e10d5832589b9000e5acc601981c574ca5511957d10ebb5bbf`
- `BYTECODE_SHA256=d5b968340060d4292232a95eee102cb95247f1a507933d28f646630d60c36514`
- `TOTAL_VM_INVOCATIONS=19`
- evidence capacity `8`; persistence/restart/negative/bounded gates PASS.
- Still not proven: real-world entity identity, cross-form mention equivalence, coreference resolution, semantic role identity.

### LANG-01D — Native Cross-Form Mention Equivalence and Coreference Hypothesis — ADMITTED

- `SOURCE_SHA256=a5e1d26b83766f631e1b642abd0752951570d0ad10eecc8e0b67bdd4f0ee1421`
- `BYTECODE_SHA256=d3853eadf82fd45242161566b9c85600d98348a3eae71f900799b963bf79fbe0`
- `TOTAL_VM_INVOCATIONS=24`
- persistence/restart/negative/bounded gates PASS.
- Historical runner diagnostic mismatch preserved; native source unchanged.
- Still not proven: coreference resolution, pronoun semantics, alias semantics, real-world entity identity.

### LANG-01E — Native Discourse Reference Chain and Contextual Coreference Hypothesis — ADMITTED

- `SOURCE_SHA256=834119f0e27b1b47e65663684331f559410661d05e24b9f4ce64ddea4ce49643`
- `BYTECODE_SHA256=44d18efb8fcc05747af3e0bc7f61a5ba651e04645671ba2e0ffbe0cb4bbd06fe`
- `TOTAL_VM_INVOCATIONS=24`
- reference-chain capacity `8`; persistence/restart/negative/bounded gates PASS.
- dependency equivalence conflict is preserved as uncertainty.
- Still not proven: general coreference resolution, pronoun semantics, discourse semantics, semantic understanding.

### LANG-01F — Native Competing Antecedent Hypotheses and Reference Ambiguity — ADMITTED

Critical invariant: `PREFERRED_ANTECEDENT_HYPOTHESIS != RESOLVED_REFERENT`.

- `SOURCE_SHA256=1ab0081f904a844d456d7913b522577038cec1b7d62f4f37494bf29a79dc9a59`
- `BYTECODE_SHA256=60edd9ace13f54b826adcd7e89362acddcfaea9a1649845006f52c99dce77a81`
- `TOTAL_VM_INVOCATIONS=21`
- `POST_VM_ALIGNMENT_PASS_COUNT=21`
- `POST_VM_ALIGNMENT_FAIL_COUNT=0`
- `NEGATIVE_TEST=PASS`
- `PERSISTENT_STATE_TEST=PASS`
- `PERSISTENT_STATE_MATERIAL_EFFECT=YES`
- `RESTART_REPLAY_TEST=PASS`
- `IDENTICAL_INPUT_AND_STATE_REPLAY=YES`
- `VM_NONZERO_COUNT=0`
- `STEP_LIMIT_HIT_COUNT=0`
- `PRODUCTION_STATE_MUTATED=NO`

Historical LANG-01F failure preserved: original runtime had `19/21` oracle alignment because refused/no-prior-state cases emitted a non-`NONE` `NEXT_STATE_STATUS`. The smallest native output-contract repair restored the invariant `IF STATE_COMMIT_ALLOWED=0 AND PREVIOUS_STATE_VALID=0 -> NEXT_STATE_STATUS=NONE`, without changing scoring, competition, persistence, or oracle definition.

Claim scope: bounded two-candidate structural antecedent competition with persistent ambiguity and conservative preference revision only.

### LANG-01G — Native Reference-Resolution Evidence Integration — ADMITTED

Capability ID:
`LANG-01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION`

Dependency:
`LANG-01F_NATIVE_COMPETING_ANTECEDENT_HYPOTHESES_AND_REFERENCE_AMBIGUITY`

Teaching goal: given a valid LANG-01F two-candidate reference state plus bounded structural evidence records, native SIGMA integrates evidence by exact feature/value compatibility, preserves evidence identity/provenance, suppresses exact duplicates, rejects evidence-ID collisions, preserves aggregate ambiguity under ties/non-discriminating evidence, and revises preference when later counterevidence changes aggregate support.

Critical invariants:

- `PREFERRED_ANTECEDENT_HYPOTHESIS != RESOLVED_REFERENT`
- `HOST_EVIDENCE_SCORING=NO`
- `HOST_ANTECEDENT_SELECTION=NO`
- `HOST_LEARNING=NO`
- `HOST_SEMANTIC_INTERPRETATION=NO`
- `EVIDENCE_RECORD_ORDER_IS_WINNER_POLICY=NO`
- duplicate evidence does not double-count;
- evidence-ID collision does not mutate state;
- exactly two antecedent candidates remain the bounded model.

Canonical native source:

- `NATIVE_SOURCE_PATH=SIGMA_PROFESSOR/artifacts/SIGMA_LANG_01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION_V1.sigma`
- `SOURCE_GIT_BLOB=03b03cff32eee5c35e220cd562b1081b615ca36b`
- `SOURCE_SHA256=33d04804bf190ab599ea0e1a9f2838fc37e53e52281e10a2c1bd2a39f816f087`
- `SOURCE_COMMIT=411ba280fc3ead9f6002eaeacd44624a8b0ad065`

Final R3 entry runner:

- `RUNNER_PATH=SIGMA_PROFESSOR/artifacts/RUN_SIGMA_LANG_01G_NATIVE_REFERENCE_RESOLUTION_EVIDENCE_INTEGRATION_PREFLIGHT_R3.sh`
- `RUNNER_COMMIT=df2f7939312c5fdc5323661bcebf1efa943b1ef4`
- `RUNNER_GIT_BLOB=6b51762246b348935d15816aa2a0c054e766432f`
- `RUNNER_SHA256=8d89cc504f36ce1190b7d364eac9cc76b0fe718824c54f484cf6b4da9561271c`
- `RUNNER_STATIC_SHELL_SYNTAX=PASS`
- `REPAIR_CLASS=RUNNER_ONLY_MECHANICAL_FRESH_STATE_FIXTURE_INITIALIZATION`
- `FRESH_STATE_REPRESENTATION=ZERO_LENGTH_STATE_FILE`
- `NATIVE_SOURCE_CHANGED=NO`
- `COGNITIVE_POLICY_CHANGED=NO`
- `ORACLE_CASES_CHANGED=NO`

Locked R3 admission evidence observed from Termux final summary:

- `TOTAL_VM_INVOCATIONS=20`
- `POST_VM_ALIGNMENT_PASS_COUNT=20`
- `POST_VM_ALIGNMENT_FAIL_COUNT=0`
- `VM_NONZERO_COUNT=0`
- `STEP_LIMIT_HIT_COUNT=0`
- `NEGATIVE_TEST=PASS`
- `PERSISTENT_STATE_TEST=PASS`
- `PERSISTENT_STATE_MATERIAL_EFFECT=YES`
- `RESTART_REPLAY_TEST=PASS`
- `IDENTICAL_INPUT_AND_STATE_REPLAY=YES`
- `REFERENCE_EVIDENCE_INTEGRATION=PASS_IN_PREFLIGHT_SCOPE`
- `TIED_AGGREGATE_EVIDENCE_WITHHELD_AS_AMBIGUITY=YES`
- `COUNTEREVIDENCE_CAN_REMOVE_PREFERENCE=YES`
- `COUNTEREVIDENCE_CAN_REVERSE_PREFERENCE=YES`
- `DUPLICATE_EVIDENCE_DOUBLE_COUNT=NO`
- `EVIDENCE_ID_COLLISION_MUTATES_STATE=NO`
- `CANDIDATE_ENCOUNTER_ORDER_IS_WINNER_POLICY=NO`
- `PREFERRED_ANTECEDENT_IS_RESOLVED_REFERENT=NO`
- `EVIDENCE_CAPACITY=8`
- `HOST_EVIDENCE_SCORING=NO`
- `HOST_ANTECEDENT_SELECTION=NO`
- `HOST_LEARNING=NO`
- `HOST_SEMANTIC_INTERPRETATION=NO`
- `COREFERENCE_RESOLUTION=NOT_PROVEN`
- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`
- `PRODUCTION_STATE_MUTATED=NO`
- `LANG_01G_PREFLIGHT=PASS`
- `ADMISSION=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE`
- `R3_WRAPPER_RC=0`

Runtime identities are equality-gated by the R3/base runner before the 20-case gate:

- `SIGMAC_SHA256=65f69217ad44f33c1aa1d4c31678d38940cd3d0b96f41892e8280dac57ad6a71`
- `VM_SHA256=029ae4b6acbee5558f7663a732f8d39a970166e8488d2c4fe62414eb39391c99`

The user-supplied R3 final tail did not include the R3 `BYTECODE_SHA256` line. Do not infer it from the earlier run:

- `R3_BYTECODE_SHA256=UNKNOWN_NOT_IN_SUPPLIED_R3_TAIL`
- historical R2 failed-run bytecode only: `839995f07413e241065386e9498c37723893f135fd933475a880c19ed65dc7d4`.

Historical LANG-01G evidence preserved:

1. R0 source-ready artifact used `!=`; pre-runtime R1 removed it conservatively before any locked runtime. No runtime failure occurred in that repair.
2. Initial R1 SHA256 metadata was incorrect while Git blobs were unchanged. Canonical identity correction R2 established source SHA256 `33d04804...` and base-runner SHA256 `d5f7ae25...`; cognition unchanged.
3. First locked R2 compile succeeded but CASE_001 failed with `VM_RC=22`, `SIGMA host: string required`; admission remained FAIL.
4. Native locked-VM diagnostic localized the blocker: `read_text(absent_state_path)` returned a non-string value accepted by `read_text` but rejected by `str_split`; trace stopped at `TRACE_060_SPLIT_ABSENT_STATE_BEFORE`.
5. R3 repaired only the mechanical fixture representation by creating a zero-length `reference_evidence_state.memory` during `prepare_case`. It did not change native evidence scoring, antecedent selection, persistence logic, or the 20-case oracle. The same admission gate then passed 20/20.

Related provenance checkpoints:

- `SIGMA_PROFESSOR/CHECKPOINTS/20260905_LANG01G_CANONICAL_IDENTITY_METADATA_CORRECTION_R2.md`
- `SIGMA_PROFESSOR/CHECKPOINTS/20260905_LANG01G_R2_RUNTIME_FAIL_CASE001_STRING_REQUIRED.md`
- `SIGMA_PROFESSOR/CHECKPOINTS/20260905_LANG01G_HOST_TYPE_LOCALIZATION_DIAG_SOURCE_READY.md`
- `SIGMA_PROFESSOR/CHECKPOINTS/20260905_LANG01G_R3_FRESH_STATE_INIT_REPAIR_READY.md`

Admission classification:

- `LANG_01G_ADMITTED=YES_IN_EXACT_TESTED_PREFLIGHT_SCOPE`
- `RUNTIME_PROOF=PASS_IN_EXACT_TESTED_PREFLIGHT_SCOPE`
- `PRODUCTION_BINDING=NO`
- `PRODUCTION_READINESS=NOT_PROVEN`

Claim scope:

Native bounded two-candidate structural reference-evidence integration with persisted provenance, aggregate ambiguity, conservative antecedent preference, duplicate suppression, collision refusal, counterevidence revision, persistence/restart/replay, and bounded capacity. This does **not** prove resolved referents, general coreference resolution, pronoun semantics, real-world entity identity, discourse semantics, or semantic understanding.

## CURRENT LANGUAGE FRONTIER

`LANG-01A -> LANG-01B -> LANG-01C -> LANG-01D -> LANG-01E -> LANG-01F -> LANG-01G` are admitted in their exact tested structural scopes.

`LANG-02_NEGATION_AND_SCOPE_FOUNDATION=DEFERRED_NOT_REJECTED` remains queued. Do not begin it merely by numeric order; re-run dependency/capability selection under the Global Native Teaching Standard before selecting the next lesson.

Next language action:

`NEXT_LANGUAGE_CAPABILITY=RESELECT_BY_DEPENDENCY_FIRST_NATIVE_PREFLIGHT`

No production binding is implied by LANG-01G admission.

## CLAIM BOUNDARIES FOR THE LANGUAGE LANE

Even with LANG-01A..01G admitted:

- `SEMANTIC_UNDERSTANDING=NOT_PROVEN`
- `COREFERENCE_RESOLUTION=NOT_PROVEN`
- `REAL_WORLD_ENTITY_IDENTITY=NOT_PROVEN`
- `PRONOUN_SEMANTICS=NOT_PROVEN`
- `DISCOURSE_SEMANTICS=NOT_PROVEN`
- `UNICODE_NORMALIZATION=NOT_PROVEN`
- `BOUNDED_FILE_IO=NOT_PROVEN`
- `PRODUCTION_READINESS=NOT_PROVEN`

## CHECKPOINT UPDATE RULE

After every meaningful new language result, update THIS SAME FILE rather than creating another floating checkpoint. Preserve old failure evidence in a short historical note. Never rewrite a FAIL as if it never happened.
