⟡(Σ.C5_AUTONOMOUS_SELF_LEARNING_CORE_V1) {
    ⚡ BASE: ".sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING";

    # Fresh invocation + authoritative state-chain envelope.
    ⚡ INVOCATION_ID: p0r4_H("read_text", BASE + "/io/invocation_id.txt", NULL, NULL);
    ⚡ FRESH_ROOT_MARKER: p0r4_H("read_text", BASE + "/io/fresh_root_marker.txt", NULL, NULL);
    ⚡ EVENT_TYPE: p0r4_H("read_text", BASE + "/io/event_type.txt", NULL, NULL);
    ⚡ EXPECTED_PHASE: p0r4_H("read_text", BASE + "/io/expected_phase.txt", NULL, NULL);
    ⚡ AUTHORITATIVE_CHAIN_HEAD: p0r4_H("read_text", BASE + "/io/authoritative_state_chain_head.txt", NULL, NULL);
    ⚡ PARENT_STATE_SHA: p0r4_H("read_text", BASE + "/io/parent_state_sha.txt", NULL, NULL);
    ⚡ PARENT_STATE_SNAPSHOT_SHA: p0r4_H("read_text", BASE + "/io/parent_state_snapshot_sha.txt", NULL, NULL);
    ⚡ PARENT_STATE_SNAPSHOT: p0r4_H("read_text", BASE + "/io/parent_state_snapshot.txt", NULL, NULL);

    # Canonical mechanical receipt fields. The runner owns hashing/serialization only.
    ⚡ RECEIPT_SHA: p0r4_H("read_text", BASE + "/io/receipt_sha.txt", NULL, NULL);
    ⚡ RECEIPT_KIND: p0r4_H("read_text", BASE + "/io/receipt_kind.txt", NULL, NULL);
    ⚡ RECEIPT_INVOCATION_ID: p0r4_H("read_text", BASE + "/io/receipt_invocation_id.txt", NULL, NULL);
    ⚡ RECEIPT_EVENT_TYPE: p0r4_H("read_text", BASE + "/io/receipt_event_type.txt", NULL, NULL);
    ⚡ RECEIPT_PHASE: p0r4_H("read_text", BASE + "/io/receipt_phase.txt", NULL, NULL);
    ⚡ RECEIPT_PARENT_STATE_SHA: p0r4_H("read_text", BASE + "/io/receipt_parent_state_sha.txt", NULL, NULL);
    ⚡ RECEIPT_ACTION_ID: p0r4_H("read_text", BASE + "/io/receipt_action_id.txt", NULL, NULL);
    ⚡ RECEIPT_ARTIFACT_SHA: p0r4_H("read_text", BASE + "/io/receipt_artifact_sha.txt", NULL, NULL);
    ⚡ RECEIPT_SUBJECT_ID: p0r4_H("read_text", BASE + "/io/receipt_subject_id.txt", NULL, NULL);
    ⚡ RECEIPT_REQUEST_ID: p0r4_H("read_text", BASE + "/io/receipt_request_id.txt", NULL, NULL);
    ⚡ RECEIPT_SOURCE_ID: p0r4_H("read_text", BASE + "/io/receipt_source_id.txt", NULL, NULL);
    ⚡ RECEIPT_SOURCE_VERSION_SHA: p0r4_H("read_text", BASE + "/io/receipt_source_version_sha.txt", NULL, NULL);
    ⚡ RECEIPT_EVIDENCE_ID: p0r4_H("read_text", BASE + "/io/receipt_evidence_id.txt", NULL, NULL);
    ⚡ RECEIPT_REQUEST_ARTIFACT_SHA: p0r4_H("read_text", BASE + "/io/receipt_request_artifact_sha.txt", NULL, NULL);
    ⚡ RECEIPT_EPISTEMIC_STATE_SHA: p0r4_H("read_text", BASE + "/io/receipt_epistemic_state_sha.txt", NULL, NULL);

    # Event-side mechanical identifiers/attestations.
    ⚡ ACTION_ID: p0r4_H("read_text", BASE + "/io/action_id.txt", NULL, NULL);
    ⚡ INPUT_PAYLOAD_SHA: p0r4_H("read_text", BASE + "/io/input_payload_sha.txt", NULL, NULL);
    ⚡ BOUND_REQUEST_ARTIFACT_SHA: p0r4_H("read_text", BASE + "/io/bound_request_artifact_sha.txt", NULL, NULL);
    ⚡ BOUND_EPISTEMIC_STATE_SHA: p0r4_H("read_text", BASE + "/io/bound_epistemic_state_sha.txt", NULL, NULL);
    ⚡ BOUND_MEMORY_SHA: p0r4_H("read_text", BASE + "/io/bound_memory_sha.txt", NULL, NULL);

    # Learning input. These bytes are evidence/problem input; semantic decisions remain native below.
    ⚡ SUBJECT_ID: p0r4_H("read_text", BASE + "/io/subject_id.txt", NULL, NULL);
    ⚡ CANDIDATE_A: p0r4_H("read_text", BASE + "/io/candidate_a.txt", NULL, NULL);
    ⚡ CANDIDATE_B: p0r4_H("read_text", BASE + "/io/candidate_b.txt", NULL, NULL);
    ⚡ NEUTRAL_LEDGER: p0r4_H("read_text", BASE + "/io/neutral_ledger.txt", NULL, NULL);
    ⚡ REVISION_LEDGER: p0r4_H("read_text", BASE + "/io/revision_ledger.txt", NULL, NULL);

    # Exact native records replayed from the immutable epistemic seed artifact.
    ⚡ SEED_OBJECTIVE: p0r4_H("read_text", BASE + "/io/seed_objective.txt", NULL, NULL);
    ⚡ SEED_GAP: p0r4_H("read_text", BASE + "/io/seed_gap.txt", NULL, NULL);
    ⚡ SEED_CLAIM_A: p0r4_H("read_text", BASE + "/io/seed_claim_a.txt", NULL, NULL);
    ⚡ SEED_CLAIM_B: p0r4_H("read_text", BASE + "/io/seed_claim_b.txt", NULL, NULL);

    # Restart-only memory input. Source text is not required on this path.
    ⚡ MEMORY_TEXT: p0r4_H("read_text", BASE + "/io/memory_text.txt", NULL, NULL);
    ⚡ RECALL_CLAIM_ID: p0r4_H("read_text", BASE + "/io/recall_claim_id.txt", NULL, NULL);
    ⚡ RECALL_GAP_ID: p0r4_H("read_text", BASE + "/io/recall_gap_id.txt", NULL, NULL);

    ⚡ ACTION: "HOLD";
    ⚡ STATUS: "R4_TRUST_ENVELOPE_NOT_ADMITTED";
    ⚡ NEXT_STATE: "";
    ⚡ EVENT_BINDING: "";
    ⚡ COMMIT_ALLOWED: 0;
    ⚡ STAGE_OK: 1;
    ⚡ NEXT_ACTION_ID: "NONE";

    IF (p0r4_safe_atom(INVOCATION_ID, 96) == 0) { ⚡ STATUS: "INVALID_INVOCATION_ID"; }

    IF (p0r4_safe_atom(INVOCATION_ID, 96)) {
        IF (FRESH_ROOT_MARKER != INVOCATION_ID) { ⚡ STATUS: "FRESH_ROOT_BINDING_FAILED"; }

        IF (FRESH_ROOT_MARKER == INVOCATION_ID) {
            IF (p0r4_event_valid(EVENT_TYPE) == 0) { ⚡ STATUS: "INVALID_EVENT_TYPE"; }

            IF (EVENT_TYPE == "BOOTSTRAP") {
                ⚡ BOOT_OK: 1;
                IF (EXPECTED_PHASE != "GENESIS") { ⚡ BOOT_OK: 0; }
                IF (AUTHORITATIVE_CHAIN_HEAD != "GENESIS") { ⚡ BOOT_OK: 0; }
                IF (PARENT_STATE_SHA != "GENESIS") { ⚡ BOOT_OK: 0; }
                IF (PARENT_STATE_SNAPSHOT_SHA != "GENESIS") { ⚡ BOOT_OK: 0; }
                IF (PARENT_STATE_SNAPSHOT != "") { ⚡ BOOT_OK: 0; }
                IF (RECEIPT_KIND != "GENESIS") { ⚡ BOOT_OK: 0; }
                IF (RECEIPT_INVOCATION_ID != INVOCATION_ID) { ⚡ BOOT_OK: 0; }
                IF (RECEIPT_EVENT_TYPE != "BOOTSTRAP") { ⚡ BOOT_OK: 0; }
                IF (RECEIPT_PHASE != "GENESIS") { ⚡ BOOT_OK: 0; }
                IF (RECEIPT_PARENT_STATE_SHA != "GENESIS") { ⚡ BOOT_OK: 0; }
                IF (RECEIPT_ACTION_ID != "NONE") { ⚡ BOOT_OK: 0; }
                IF (p0r4_hex64(RECEIPT_SHA) == 0) { ⚡ BOOT_OK: 0; }

                IF (BOOT_OK) {
                    ⚡ NEXT_STATE:
                        "STATE_VERSION=2\n"
                        + "PHASE=IDLE\n"
                        + "OBJECTIVE_ID=NONE\n"
                        + "ACTIVE_GAP_ID=NONE\n"
                        + "PENDING_ACTION_ID=NONE\n"
                        + "PENDING_REQUEST_ID=NONE\n"
                        + "PENDING_CAPABILITY_ID=NONE\n"
                        + "PENDING_SUBJECT_ID=NONE\n"
                        + "PENDING_PAYLOAD_KIND=NONE\n"
                        + "PENDING_PAYLOAD_SHA=NONE\n"
                        + "EPISTEMIC_STATE_SHA=NONE\n"
                        + "MEMORY_STATE_SHA=NONE\n"
                        + "LAST_RECEIPT_SHA=" + RECEIPT_SHA + "\n"
                        + "LAST_INVOCATION_ID=" + INVOCATION_ID + "\n"
                        + "LAST_ACTION_ID=NONE\n"
                        + "LAST_EVENT=BOOTSTRAP\n"
                        + "LAST_SOURCE_ID=NONE\n"
                        + "LAST_SOURCE_VERSION_SHA=NONE\n"
                        + "LAST_ARTIFACT_SHA=NONE\n"
                        + "LAST_EVIDENCE_ID=NONE";
                    ⚡ ACTION: "BOOTSTRAP_R4_STATE";
                    ⚡ STATUS: "R4_GENESIS_TRUSTED";
                    ⚡ NEXT_ACTION_ID: "NONE";
                    ⚡ COMMIT_ALLOWED: 1;
                }
                IF (BOOT_OK == 0) { ⚡ STATUS: "R4_GENESIS_BINDING_REJECTED"; }
            }

            IF (EVENT_TYPE != "BOOTSTRAP") {
                ⚡ ENVELOPE_OK: 1;
                IF (p0r4_hex64(AUTHORITATIVE_CHAIN_HEAD) == 0) { ⚡ ENVELOPE_OK: 0; }
                IF (p0r4_hex64(PARENT_STATE_SHA) == 0) { ⚡ ENVELOPE_OK: 0; }
                IF (p0r4_hex64(PARENT_STATE_SNAPSHOT_SHA) == 0) { ⚡ ENVELOPE_OK: 0; }
                IF (PARENT_STATE_SHA != AUTHORITATIVE_CHAIN_HEAD) { ⚡ ENVELOPE_OK: 0; }
                IF (PARENT_STATE_SNAPSHOT_SHA != PARENT_STATE_SHA) { ⚡ ENVELOPE_OK: 0; }
                IF (p0r4_state_snapshot_valid(PARENT_STATE_SNAPSHOT) == 0) { ⚡ ENVELOPE_OK: 0; }
                IF (p0r4_hex64(RECEIPT_SHA) == 0) { ⚡ ENVELOPE_OK: 0; }
                IF (p0r4_event_receipt_kind_matches(EVENT_TYPE, RECEIPT_KIND) == 0) { ⚡ ENVELOPE_OK: 0; }
                IF (RECEIPT_INVOCATION_ID != INVOCATION_ID) { ⚡ ENVELOPE_OK: 0; }
                IF (RECEIPT_EVENT_TYPE != EVENT_TYPE) { ⚡ ENVELOPE_OK: 0; }
                IF (RECEIPT_PHASE != EXPECTED_PHASE) { ⚡ ENVELOPE_OK: 0; }
                IF (RECEIPT_PARENT_STATE_SHA != PARENT_STATE_SHA) { ⚡ ENVELOPE_OK: 0; }
                IF (RECEIPT_ACTION_ID != ACTION_ID) { ⚡ ENVELOPE_OK: 0; }

                ⚡ STATE_PHASE: p0r4_state_value(PARENT_STATE_SNAPSHOT, 1, "PHASE");
                ⚡ STATE_OBJECTIVE_ID: p0r4_state_value(PARENT_STATE_SNAPSHOT, 2, "OBJECTIVE_ID");
                ⚡ STATE_ACTIVE_GAP_ID: p0r4_state_value(PARENT_STATE_SNAPSHOT, 3, "ACTIVE_GAP_ID");
                ⚡ STATE_PENDING_ACTION_ID: p0r4_state_value(PARENT_STATE_SNAPSHOT, 4, "PENDING_ACTION_ID");
                ⚡ STATE_PENDING_REQUEST_ID: p0r4_state_value(PARENT_STATE_SNAPSHOT, 5, "PENDING_REQUEST_ID");
                ⚡ STATE_PENDING_CAPABILITY_ID: p0r4_state_value(PARENT_STATE_SNAPSHOT, 6, "PENDING_CAPABILITY_ID");
                ⚡ STATE_PENDING_SUBJECT_ID: p0r4_state_value(PARENT_STATE_SNAPSHOT, 7, "PENDING_SUBJECT_ID");
                ⚡ STATE_PENDING_PAYLOAD_KIND: p0r4_state_value(PARENT_STATE_SNAPSHOT, 8, "PENDING_PAYLOAD_KIND");
                ⚡ STATE_PENDING_PAYLOAD_SHA: p0r4_state_value(PARENT_STATE_SNAPSHOT, 9, "PENDING_PAYLOAD_SHA");
                ⚡ STATE_EPISTEMIC_STATE_SHA: p0r4_state_value(PARENT_STATE_SNAPSHOT, 10, "EPISTEMIC_STATE_SHA");
                ⚡ STATE_MEMORY_STATE_SHA: p0r4_state_value(PARENT_STATE_SNAPSHOT, 11, "MEMORY_STATE_SHA");

                IF (EXPECTED_PHASE != STATE_PHASE) { ⚡ ENVELOPE_OK: 0; }
                IF (ENVELOPE_OK == 0) { ⚡ STATUS: "R4_TRUST_ENVELOPE_REJECTED"; }

                IF (ENVELOPE_OK) {
                    IF (EVENT_TYPE == "TICK") {
                        IF (STATE_PHASE == "IDLE") {
                            IF (ACTION_ID == "NONE") {
                                ⚡ ACTION: "WAIT";
                                ⚡ STATUS: "R4_TRUSTED_IDLE_TICK";
                            }
                        }
                    }

                    IF (EVENT_TYPE == "LEARNING_INPUT_READY") {
                        ⚡ INPUT_OK: 1;
                        IF (STATE_PHASE != "IDLE") { ⚡ INPUT_OK: 0; }
                        IF (ACTION_ID != "NONE") { ⚡ INPUT_OK: 0; }
                        IF (p0r4_hex64(INPUT_PAYLOAD_SHA) == 0) { ⚡ INPUT_OK: 0; }
                        IF (RECEIPT_ARTIFACT_SHA != INPUT_PAYLOAD_SHA) { ⚡ INPUT_OK: 0; }
                        IF (p0r4_safe_atom(SUBJECT_ID, 128) == 0) { ⚡ INPUT_OK: 0; }

                        IF (INPUT_OK) {
                            ⚡ GAP_SIGNAL: c5a3_relation_gap_signal(NEUTRAL_LEDGER, CANDIDATE_A, CANDIDATE_B);
                            IF (GAP_SIGNAL == 0) {
                                ⚡ ACTION: "NO_NATIVE_RELATION_GAP";
                                ⚡ STATUS: "R4_INPUT_ACCEPTED_NO_RELATION_GAP";
                            }

                            IF (GAP_SIGNAL) {
                                ⚡ NATIVE_OBJECTIVE_ID: "OBJ_" + INVOCATION_ID;
                                ⚡ NATIVE_WORK_ID: NATIVE_OBJECTIVE_ID;
                                ⚡ NATIVE_GAP_ID: "GAP_" + INVOCATION_ID;
                                ⚡ NATIVE_CLAIM_A_ID: "CLAIM_A_" + INVOCATION_ID;
                                ⚡ NATIVE_CLAIM_B_ID: "CLAIM_B_" + INVOCATION_ID;
                                ⚡ NATIVE_ACTION_ID: "ACT_" + INVOCATION_ID;
                                ⚡ NATIVE_REQUEST_ID: "REQ_" + INVOCATION_ID;
                                ⚡ NATIVE_OBJECTIVE: c5t2_make_objective(NATIVE_OBJECTIVE_ID, "OPEN", SUBJECT_ID, "1");
                                ⚡ NATIVE_CLAIM_A: c5d1_make_claim(NATIVE_CLAIM_A_ID, SUBJECT_ID, CANDIDATE_A, "UNRESOLVED", "1", "1");
                                ⚡ NATIVE_CLAIM_B: c5d1_make_claim(NATIVE_CLAIM_B_ID, SUBJECT_ID, CANDIDATE_B, "UNRESOLVED", "1", "1");
                                ⚡ NATIVE_GAP: c5t2_make_gap(NATIVE_GAP_ID, NATIVE_OBJECTIVE_ID, "EVIDENCE", SUBJECT_ID, "EVIDENCE_SEARCH", "1");
                                ⚡ NATIVE_REQUEST_PAYLOAD: c5c4_relation_request_payload(NEUTRAL_LEDGER, CANDIDATE_A, CANDIDATE_B, NATIVE_GAP);
                                ⚡ SEED_VALID: c5c4_relation_seed_valid(NATIVE_OBJECTIVE, NATIVE_GAP, NATIVE_CLAIM_A, NATIVE_CLAIM_B, CANDIDATE_A, CANDIDATE_B);

                                IF (SEED_VALID == 0) { ⚡ INPUT_OK: 0; }
                                IF (NATIVE_REQUEST_PAYLOAD == "") { ⚡ INPUT_OK: 0; }

                                IF (INPUT_OK) {
                                    ⚡ SEED_SNAPSHOT:
                                        "TYPE=R4_RELATION_SEED_SNAPSHOT\n"
                                        + "WORK_ID=" + NATIVE_WORK_ID + "\n"
                                        + "SUBJECT_ID=" + SUBJECT_ID + "\n"
                                        + "OBJECTIVE=" + NATIVE_OBJECTIVE + "\n"
                                        + "GAP=" + NATIVE_GAP + "\n"
                                        + "CLAIM_A=" + NATIVE_CLAIM_A + "\n"
                                        + "CLAIM_B=" + NATIVE_CLAIM_B + "\n"
                                        + "CANDIDATE_A=" + CANDIDATE_A + "\n"
                                        + "CANDIDATE_B=" + CANDIDATE_B + "\n"
                                        + "NEUTRAL_LEDGER_BEGIN\n" + NEUTRAL_LEDGER + "\nNEUTRAL_LEDGER_END";

                                    IF (p0r4_stage_write_verify(BASE + "/out/native_work_id.txt", NATIVE_WORK_ID) == 0) { ⚡ STAGE_OK: 0; }
                                    IF (p0r4_stage_write_verify(BASE + "/out/native_objective.txt", NATIVE_OBJECTIVE) == 0) { ⚡ STAGE_OK: 0; }
                                    IF (p0r4_stage_write_verify(BASE + "/out/native_gap.txt", NATIVE_GAP) == 0) { ⚡ STAGE_OK: 0; }
                                    IF (p0r4_stage_write_verify(BASE + "/out/native_claim_a.txt", NATIVE_CLAIM_A) == 0) { ⚡ STAGE_OK: 0; }
                                    IF (p0r4_stage_write_verify(BASE + "/out/native_claim_b.txt", NATIVE_CLAIM_B) == 0) { ⚡ STAGE_OK: 0; }
                                    IF (p0r4_stage_write_verify(BASE + "/out/native_request_payload.txt", NATIVE_REQUEST_PAYLOAD) == 0) { ⚡ STAGE_OK: 0; }
                                    IF (p0r4_stage_write_verify(BASE + "/out/native_epistemic_seed.txt", SEED_SNAPSHOT) == 0) { ⚡ STAGE_OK: 0; }

                                    ⚡ NEXT_STATE:
                                        "STATE_VERSION=2\n"
                                        + "PHASE=WAIT_REQUEST_BIND\n"
                                        + "OBJECTIVE_ID=" + NATIVE_OBJECTIVE_ID + "\n"
                                        + "ACTIVE_GAP_ID=" + NATIVE_GAP_ID + "\n"
                                        + "PENDING_ACTION_ID=" + NATIVE_ACTION_ID + "\n"
                                        + "PENDING_REQUEST_ID=" + NATIVE_REQUEST_ID + "\n"
                                        + "PENDING_CAPABILITY_ID=NONE\n"
                                        + "PENDING_SUBJECT_ID=" + SUBJECT_ID + "\n"
                                        + "PENDING_PAYLOAD_KIND=NATIVE_EVIDENCE_REQUEST\n"
                                        + "PENDING_PAYLOAD_SHA=NONE\n"
                                        + "EPISTEMIC_STATE_SHA=NONE\n"
                                        + "MEMORY_STATE_SHA=" + STATE_MEMORY_STATE_SHA + "\n"
                                        + "LAST_RECEIPT_SHA=" + RECEIPT_SHA + "\n"
                                        + "LAST_INVOCATION_ID=" + INVOCATION_ID + "\n"
                                        + "LAST_ACTION_ID=" + NATIVE_ACTION_ID + "\n"
                                        + "LAST_EVENT=LEARNING_INPUT_READY\n"
                                        + "LAST_SOURCE_ID=NONE\n"
                                        + "LAST_SOURCE_VERSION_SHA=NONE\n"
                                        + "LAST_ARTIFACT_SHA=" + INPUT_PAYLOAD_SHA + "\n"
                                        + "LAST_EVIDENCE_ID=NONE";
                                    ⚡ ACTION: "MATERIALIZE_NATIVE_REQUEST";
                                    ⚡ STATUS: "R4_NATIVE_GAP_AND_REQUEST_CREATED";
                                    ⚡ NEXT_ACTION_ID: NATIVE_ACTION_ID;
                                    ⚡ COMMIT_ALLOWED: 1;
                                }
                            }
                        }
                        IF (INPUT_OK == 0) { ⚡ STATUS: "R4_LEARNING_INPUT_REJECTED"; }
                    }

                    IF (EVENT_TYPE == "REQUEST_BOUND") {
                        ⚡ BIND_OK: 1;
                        IF (STATE_PHASE != "WAIT_REQUEST_BIND") { ⚡ BIND_OK: 0; }
                        IF (ACTION_ID != STATE_PENDING_ACTION_ID) { ⚡ BIND_OK: 0; }
                        IF (RECEIPT_REQUEST_ID != STATE_PENDING_REQUEST_ID) { ⚡ BIND_OK: 0; }
                        IF (RECEIPT_SUBJECT_ID != STATE_PENDING_SUBJECT_ID) { ⚡ BIND_OK: 0; }
                        IF (p0r4_hex64(BOUND_REQUEST_ARTIFACT_SHA) == 0) { ⚡ BIND_OK: 0; }
                        IF (p0r4_hex64(BOUND_EPISTEMIC_STATE_SHA) == 0) { ⚡ BIND_OK: 0; }
                        IF (RECEIPT_ARTIFACT_SHA != BOUND_REQUEST_ARTIFACT_SHA) { ⚡ BIND_OK: 0; }
                        IF (RECEIPT_REQUEST_ARTIFACT_SHA != BOUND_REQUEST_ARTIFACT_SHA) { ⚡ BIND_OK: 0; }
                        IF (RECEIPT_EPISTEMIC_STATE_SHA != BOUND_EPISTEMIC_STATE_SHA) { ⚡ BIND_OK: 0; }

                        IF (BIND_OK) {
                            ⚡ NEXT_STATE:
                                "STATE_VERSION=2\n"
                                + "PHASE=WAIT_EVIDENCE\n"
                                + "OBJECTIVE_ID=" + STATE_OBJECTIVE_ID + "\n"
                                + "ACTIVE_GAP_ID=" + STATE_ACTIVE_GAP_ID + "\n"
                                + "PENDING_ACTION_ID=" + STATE_PENDING_ACTION_ID + "\n"
                                + "PENDING_REQUEST_ID=" + STATE_PENDING_REQUEST_ID + "\n"
                                + "PENDING_CAPABILITY_ID=NONE\n"
                                + "PENDING_SUBJECT_ID=" + STATE_PENDING_SUBJECT_ID + "\n"
                                + "PENDING_PAYLOAD_KIND=NATIVE_EVIDENCE_REQUEST\n"
                                + "PENDING_PAYLOAD_SHA=" + BOUND_REQUEST_ARTIFACT_SHA + "\n"
                                + "EPISTEMIC_STATE_SHA=" + BOUND_EPISTEMIC_STATE_SHA + "\n"
                                + "MEMORY_STATE_SHA=" + STATE_MEMORY_STATE_SHA + "\n"
                                + "LAST_RECEIPT_SHA=" + RECEIPT_SHA + "\n"
                                + "LAST_INVOCATION_ID=" + INVOCATION_ID + "\n"
                                + "LAST_ACTION_ID=" + STATE_PENDING_ACTION_ID + "\n"
                                + "LAST_EVENT=REQUEST_BOUND\n"
                                + "LAST_SOURCE_ID=NONE\n"
                                + "LAST_SOURCE_VERSION_SHA=NONE\n"
                                + "LAST_ARTIFACT_SHA=" + BOUND_REQUEST_ARTIFACT_SHA + "\n"
                                + "LAST_EVIDENCE_ID=NONE";
                            ⚡ ACTION: "TRANSPORT_EXACT_NATIVE_REQUEST";
                            ⚡ STATUS: "R4_NATIVE_REQUEST_BOUND_FOR_TRANSPORT";
                            ⚡ NEXT_ACTION_ID: STATE_PENDING_ACTION_ID;
                            ⚡ COMMIT_ALLOWED: 1;
                        }
                        IF (BIND_OK == 0) { ⚡ STATUS: "R4_REQUEST_BIND_REJECTED"; }
                    }

                    IF (EVENT_TYPE == "EVIDENCE_READY") {
                        ⚡ EVIDENCE_OK: 1;
                        IF (STATE_PHASE != "WAIT_EVIDENCE") { ⚡ EVIDENCE_OK: 0; }
                        IF (ACTION_ID != STATE_PENDING_ACTION_ID) { ⚡ EVIDENCE_OK: 0; }
                        IF (RECEIPT_REQUEST_ID != STATE_PENDING_REQUEST_ID) { ⚡ EVIDENCE_OK: 0; }
                        IF (RECEIPT_SUBJECT_ID != STATE_PENDING_SUBJECT_ID) { ⚡ EVIDENCE_OK: 0; }
                        IF (RECEIPT_REQUEST_ARTIFACT_SHA != STATE_PENDING_PAYLOAD_SHA) { ⚡ EVIDENCE_OK: 0; }
                        IF (RECEIPT_EPISTEMIC_STATE_SHA != STATE_EPISTEMIC_STATE_SHA) { ⚡ EVIDENCE_OK: 0; }
                        IF (p0r4_safe_atom(RECEIPT_SOURCE_ID, 128) == 0) { ⚡ EVIDENCE_OK: 0; }
                        IF (p0r4_hex64(RECEIPT_SOURCE_VERSION_SHA) == 0) { ⚡ EVIDENCE_OK: 0; }
                        IF (p0r4_hex64(RECEIPT_ARTIFACT_SHA) == 0) { ⚡ EVIDENCE_OK: 0; }
                        IF (p0r4_safe_atom(RECEIPT_EVIDENCE_ID, 128) == 0) { ⚡ EVIDENCE_OK: 0; }
                        IF (c5c4_relation_seed_valid(SEED_OBJECTIVE, SEED_GAP, SEED_CLAIM_A, SEED_CLAIM_B, CANDIDATE_A, CANDIDATE_B) == 0) { ⚡ EVIDENCE_OK: 0; }
                        IF (c5l2_field(SEED_OBJECTIVE, 1, "OBJECTIVE_ID") != STATE_OBJECTIVE_ID) { ⚡ EVIDENCE_OK: 0; }
                        IF (c5l2_field(SEED_GAP, 1, "GAP_ID") != STATE_ACTIVE_GAP_ID) { ⚡ EVIDENCE_OK: 0; }
                        IF (c5l2_field(SEED_GAP, 4, "SUBJECT_ID") != STATE_PENDING_SUBJECT_ID) { ⚡ EVIDENCE_OK: 0; }

                        IF (EVIDENCE_OK) {
                            ⚡ STANCE_RECORD: c5a3_make_source_stance_record(NEUTRAL_LEDGER, REVISION_LEDGER, CANDIDATE_A, CANDIDATE_B, RECEIPT_SOURCE_ID);
                            ⚡ EVIDENCE_REF: c5c4_make_evidence_ref(RECEIPT_EVIDENCE_ID, RECEIPT_SOURCE_ID, RECEIPT_SOURCE_VERSION_SHA, RECEIPT_ARTIFACT_SHA, STATE_PENDING_SUBJECT_ID);
                            ⚡ EVAL_A: c5c4_make_claim_evaluation("EVAL_A_" + INVOCATION_ID, SEED_CLAIM_A, EVIDENCE_REF, STANCE_RECORD, "A", RECEIPT_ARTIFACT_SHA);
                            ⚡ EVAL_B: c5c4_make_claim_evaluation("EVAL_B_" + INVOCATION_ID, SEED_CLAIM_B, EVIDENCE_REF, STANCE_RECORD, "B", RECEIPT_ARTIFACT_SHA);
                            ⚡ POSTURE: c5a3_make_truth_posture(NEUTRAL_LEDGER, REVISION_LEDGER, CANDIDATE_A, CANDIDATE_B);
                            ⚡ REVISED_A: c5c4_revise_claim_from_posture(SEED_CLAIM_A, POSTURE, "A", "1", "2");
                            ⚡ REVISED_B: c5c4_revise_claim_from_posture(SEED_CLAIM_B, POSTURE, "B", "1", "2");
                            ⚡ CONFLICT_GAP: c5c4_open_conflict_gap(SEED_GAP, POSTURE, "CONFLICT_" + INVOCATION_ID, "1");
                            ⚡ TRUTH_STATE: c5l2_field(POSTURE, 1, "TRUTH_STATE");
                            ⚡ NEXT_RELATION_GAP: SEED_GAP;
                            ⚡ NEXT_ACTIVE_GAP_ID: STATE_ACTIVE_GAP_ID;

                            IF (TRUTH_STATE == "PROVISIONAL_A") { ⚡ NEXT_RELATION_GAP: c5t2_gap_with_state(SEED_GAP, "RESOLVED"); }
                            IF (TRUTH_STATE == "PROVISIONAL_B") { ⚡ NEXT_RELATION_GAP: c5t2_gap_with_state(SEED_GAP, "RESOLVED"); }
                            IF (TRUTH_STATE == "CONTESTED") {
                                ⚡ NEXT_RELATION_GAP: c5t2_gap_with_state(SEED_GAP, "HELD");
                                IF (CONFLICT_GAP != "") { ⚡ NEXT_ACTIVE_GAP_ID: c5l2_field(CONFLICT_GAP, 1, "GAP_ID"); }
                            }

                            ⚡ CLAIM_BANK: REVISED_A + "\n" + REVISED_B;
                            ⚡ GAP_BANK: NEXT_RELATION_GAP;
                            IF (CONFLICT_GAP != "") { ⚡ GAP_BANK: GAP_BANK + "\n" + CONFLICT_GAP; }
                            ⚡ EVIDENCE_REF_BANK: EVIDENCE_REF;
                            ⚡ EVALUATION_BANK: EVAL_A + "\n" + EVAL_B;
                            ⚡ MEMORY: c5c4_pack_memory(STATE_OBJECTIVE_ID, CLAIM_BANK, GAP_BANK, EVIDENCE_REF_BANK, EVALUATION_BANK, "2");

                            IF (STANCE_RECORD == "") { ⚡ EVIDENCE_OK: 0; }
                            IF (EVIDENCE_REF == "") { ⚡ EVIDENCE_OK: 0; }
                            IF (EVAL_A == "") { ⚡ EVIDENCE_OK: 0; }
                            IF (EVAL_B == "") { ⚡ EVIDENCE_OK: 0; }
                            IF (POSTURE == "") { ⚡ EVIDENCE_OK: 0; }
                            IF (REVISED_A == "") { ⚡ EVIDENCE_OK: 0; }
                            IF (REVISED_B == "") { ⚡ EVIDENCE_OK: 0; }
                            IF (MEMORY == "") { ⚡ EVIDENCE_OK: 0; }

                            IF (EVIDENCE_OK) {
                                ⚡ MEMORY_ACTION_ID: "MEM_" + INVOCATION_ID;
                                IF (p0r4_stage_write_verify(BASE + "/out/source_stance.txt", STANCE_RECORD) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/evidence_ref.txt", EVIDENCE_REF) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/evaluation_a.txt", EVAL_A) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/evaluation_b.txt", EVAL_B) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/truth_posture.txt", POSTURE) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/revised_claim_a.txt", REVISED_A) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/revised_claim_b.txt", REVISED_B) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/next_relation_gap.txt", NEXT_RELATION_GAP) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/conflict_gap.txt", CONFLICT_GAP) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/native_compact_memory.txt", MEMORY) == 0) { ⚡ STAGE_OK: 0; }

                                ⚡ NEXT_STATE:
                                    "STATE_VERSION=2\n"
                                    + "PHASE=WAIT_MEMORY_BIND\n"
                                    + "OBJECTIVE_ID=" + STATE_OBJECTIVE_ID + "\n"
                                    + "ACTIVE_GAP_ID=" + NEXT_ACTIVE_GAP_ID + "\n"
                                    + "PENDING_ACTION_ID=" + MEMORY_ACTION_ID + "\n"
                                    + "PENDING_REQUEST_ID=NONE\n"
                                    + "PENDING_CAPABILITY_ID=NONE\n"
                                    + "PENDING_SUBJECT_ID=" + STATE_PENDING_SUBJECT_ID + "\n"
                                    + "PENDING_PAYLOAD_KIND=NATIVE_COMPACT_MEMORY\n"
                                    + "PENDING_PAYLOAD_SHA=NONE\n"
                                    + "EPISTEMIC_STATE_SHA=" + STATE_EPISTEMIC_STATE_SHA + "\n"
                                    + "MEMORY_STATE_SHA=NONE\n"
                                    + "LAST_RECEIPT_SHA=" + RECEIPT_SHA + "\n"
                                    + "LAST_INVOCATION_ID=" + INVOCATION_ID + "\n"
                                    + "LAST_ACTION_ID=" + MEMORY_ACTION_ID + "\n"
                                    + "LAST_EVENT=EVIDENCE_READY\n"
                                    + "LAST_SOURCE_ID=" + RECEIPT_SOURCE_ID + "\n"
                                    + "LAST_SOURCE_VERSION_SHA=" + RECEIPT_SOURCE_VERSION_SHA + "\n"
                                    + "LAST_ARTIFACT_SHA=" + RECEIPT_ARTIFACT_SHA + "\n"
                                    + "LAST_EVIDENCE_ID=" + RECEIPT_EVIDENCE_ID;
                                ⚡ ACTION: "MATERIALIZE_NATIVE_MEMORY";
                                ⚡ STATUS: "R4_EVIDENCE_EVALUATED_AND_MEMORY_STAGED";
                                ⚡ NEXT_ACTION_ID: MEMORY_ACTION_ID;
                                ⚡ COMMIT_ALLOWED: 1;
                            }
                        }
                        IF (EVIDENCE_OK == 0) { ⚡ STATUS: "R4_EVIDENCE_BINDING_OR_EVALUATION_REJECTED"; }
                    }

                    IF (EVENT_TYPE == "MEMORY_BOUND") {
                        ⚡ MEMORY_OK: 1;
                        IF (STATE_PHASE != "WAIT_MEMORY_BIND") { ⚡ MEMORY_OK: 0; }
                        IF (ACTION_ID != STATE_PENDING_ACTION_ID) { ⚡ MEMORY_OK: 0; }
                        IF (RECEIPT_SUBJECT_ID != STATE_PENDING_SUBJECT_ID) { ⚡ MEMORY_OK: 0; }
                        IF (p0r4_hex64(BOUND_MEMORY_SHA) == 0) { ⚡ MEMORY_OK: 0; }
                        IF (RECEIPT_ARTIFACT_SHA != BOUND_MEMORY_SHA) { ⚡ MEMORY_OK: 0; }

                        IF (MEMORY_OK) {
                            ⚡ NEXT_STATE:
                                "STATE_VERSION=2\n"
                                + "PHASE=IDLE\n"
                                + "OBJECTIVE_ID=" + STATE_OBJECTIVE_ID + "\n"
                                + "ACTIVE_GAP_ID=" + STATE_ACTIVE_GAP_ID + "\n"
                                + "PENDING_ACTION_ID=NONE\n"
                                + "PENDING_REQUEST_ID=NONE\n"
                                + "PENDING_CAPABILITY_ID=NONE\n"
                                + "PENDING_SUBJECT_ID=NONE\n"
                                + "PENDING_PAYLOAD_KIND=NONE\n"
                                + "PENDING_PAYLOAD_SHA=NONE\n"
                                + "EPISTEMIC_STATE_SHA=NONE\n"
                                + "MEMORY_STATE_SHA=" + BOUND_MEMORY_SHA + "\n"
                                + "LAST_RECEIPT_SHA=" + RECEIPT_SHA + "\n"
                                + "LAST_INVOCATION_ID=" + INVOCATION_ID + "\n"
                                + "LAST_ACTION_ID=" + STATE_PENDING_ACTION_ID + "\n"
                                + "LAST_EVENT=MEMORY_BOUND\n"
                                + "LAST_SOURCE_ID=" + p0r4_state_value(PARENT_STATE_SNAPSHOT, 16, "LAST_SOURCE_ID") + "\n"
                                + "LAST_SOURCE_VERSION_SHA=" + p0r4_state_value(PARENT_STATE_SNAPSHOT, 17, "LAST_SOURCE_VERSION_SHA") + "\n"
                                + "LAST_ARTIFACT_SHA=" + BOUND_MEMORY_SHA + "\n"
                                + "LAST_EVIDENCE_ID=" + p0r4_state_value(PARENT_STATE_SNAPSHOT, 19, "LAST_EVIDENCE_ID");
                            IF (p0r4_stage_write_verify(BASE + "/out/source_release.txt", "ALLOW_SOURCE_RELEASE_AFTER_MEMORY_COMMIT") == 0) { ⚡ STAGE_OK: 0; }
                            ⚡ ACTION: "COMPLETE_LEARNING_CYCLE";
                            ⚡ STATUS: "R4_MEMORY_BOUND_SOURCE_RELEASE_ALLOWED";
                            ⚡ NEXT_ACTION_ID: STATE_PENDING_ACTION_ID;
                            ⚡ COMMIT_ALLOWED: 1;
                        }
                        IF (MEMORY_OK == 0) { ⚡ STATUS: "R4_MEMORY_BIND_REJECTED"; }
                    }

                    IF (EVENT_TYPE == "RESTART_READY") {
                        ⚡ RESTART_OK: 1;
                        IF (STATE_PHASE != "IDLE") { ⚡ RESTART_OK: 0; }
                        IF (p0r4_hex64(STATE_MEMORY_STATE_SHA) == 0) { ⚡ RESTART_OK: 0; }
                        IF (RECEIPT_ARTIFACT_SHA != STATE_MEMORY_STATE_SHA) { ⚡ RESTART_OK: 0; }
                        IF (p0r4_safe_atom(RECALL_CLAIM_ID, 128) == 0) { ⚡ RESTART_OK: 0; }
                        IF (p0r4_safe_atom(RECALL_GAP_ID, 128) == 0) { ⚡ RESTART_OK: 0; }

                        IF (RESTART_OK) {
                            ⚡ RECALLED_CLAIM: c5c4_restart_recall_claim(MEMORY_TEXT, RECALL_CLAIM_ID);
                            ⚡ RECALLED_GAP: c5c4_restart_recall_gap(MEMORY_TEXT, RECALL_GAP_ID);
                            ⚡ RECALLED_EVALUATIONS: c5c4_restart_recall_evaluations(MEMORY_TEXT, RECALL_CLAIM_ID);
                            ⚡ RECALLED_EVIDENCE_POSTURE: c5c4_restart_evidence_posture(MEMORY_TEXT, RECALL_CLAIM_ID);
                            IF (RECALLED_CLAIM == "") { ⚡ RESTART_OK: 0; }
                            IF (RECALLED_GAP == "") { ⚡ RESTART_OK: 0; }
                            IF (RECALLED_EVALUATIONS == "") { ⚡ RESTART_OK: 0; }
                            IF (RESTART_OK) {
                                IF (p0r4_stage_write_verify(BASE + "/out/recalled_claim.txt", RECALLED_CLAIM) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/recalled_gap.txt", RECALLED_GAP) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/recalled_evaluations.txt", RECALLED_EVALUATIONS) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/recalled_evidence_posture.txt", RECALLED_EVIDENCE_POSTURE) == 0) { ⚡ STAGE_OK: 0; }
                                ⚡ NEXT_STATE:
                                    "STATE_VERSION=2\n"
                                    + "PHASE=IDLE\n"
                                    + "OBJECTIVE_ID=" + STATE_OBJECTIVE_ID + "\n"
                                    + "ACTIVE_GAP_ID=" + STATE_ACTIVE_GAP_ID + "\n"
                                    + "PENDING_ACTION_ID=NONE\n"
                                    + "PENDING_REQUEST_ID=NONE\n"
                                    + "PENDING_CAPABILITY_ID=NONE\n"
                                    + "PENDING_SUBJECT_ID=NONE\n"
                                    + "PENDING_PAYLOAD_KIND=NONE\n"
                                    + "PENDING_PAYLOAD_SHA=NONE\n"
                                    + "EPISTEMIC_STATE_SHA=NONE\n"
                                    + "MEMORY_STATE_SHA=" + STATE_MEMORY_STATE_SHA + "\n"
                                    + "LAST_RECEIPT_SHA=" + RECEIPT_SHA + "\n"
                                    + "LAST_INVOCATION_ID=" + INVOCATION_ID + "\n"
                                    + "LAST_ACTION_ID=NONE\n"
                                    + "LAST_EVENT=RESTART_READY\n"
                                    + "LAST_SOURCE_ID=" + p0r4_state_value(PARENT_STATE_SNAPSHOT, 16, "LAST_SOURCE_ID") + "\n"
                                    + "LAST_SOURCE_VERSION_SHA=" + p0r4_state_value(PARENT_STATE_SNAPSHOT, 17, "LAST_SOURCE_VERSION_SHA") + "\n"
                                    + "LAST_ARTIFACT_SHA=" + STATE_MEMORY_STATE_SHA + "\n"
                                    + "LAST_EVIDENCE_ID=" + p0r4_state_value(PARENT_STATE_SNAPSHOT, 19, "LAST_EVIDENCE_ID");
                                ⚡ ACTION: "RECALL_FROM_NATIVE_MEMORY";
                                ⚡ STATUS: "R4_RESTART_MEMORY_REUSE_PASS_PATH";
                                ⚡ NEXT_ACTION_ID: "NONE";
                                ⚡ COMMIT_ALLOWED: 1;
                            }
                        }
                        IF (RESTART_OK == 0) { ⚡ STATUS: "R4_RESTART_MEMORY_RECALL_REJECTED"; }
                    }

                    IF (EVENT_TYPE == "CAPABILITY_RESULT_READY") {
                        ⚡ ACTION: "HOLD";
                        ⚡ STATUS: "R4_CAPABILITY_RESULT_PATH_PRESENT_NOT_ACTIVATED";
                    }
                }
            }
        }
    }

    # Stage status/action for every invocation. No persistent write occurs here.
    IF (p0r4_stage_write_verify(BASE + "/out/action.txt", ACTION) == 0) { ⚡ STAGE_OK: 0; }
    IF (p0r4_stage_write_verify(BASE + "/out/status.txt", STATUS) == 0) { ⚡ STAGE_OK: 0; }

    IF (COMMIT_ALLOWED) {
        IF (p0r4_state_snapshot_valid(NEXT_STATE) == 0) { ⚡ STAGE_OK: 0; }
        ⚡ EVENT_BINDING:
            "INVOCATION_ID=" + INVOCATION_ID
            + "\nEVENT_TYPE=" + EVENT_TYPE
            + "\nPHASE=" + EXPECTED_PHASE
            + "\nPARENT_STATE_SHA=" + PARENT_STATE_SHA
            + "\nRECEIPT_SHA=" + RECEIPT_SHA
            + "\nRECEIPT_ACTION_ID=" + RECEIPT_ACTION_ID
            + "\nNEXT_ACTION_ID=" + NEXT_ACTION_ID;
        IF (p0r4_stage_write_verify(BASE + "/out/stage_next_state.txt", NEXT_STATE) == 0) { ⚡ STAGE_OK: 0; }
        IF (p0r4_stage_write_verify(BASE + "/out/stage_event_binding.txt", EVENT_BINDING) == 0) { ⚡ STAGE_OK: 0; }
        IF (p0r4_stage_write_verify(BASE + "/out/commit_parent_state_sha.txt", PARENT_STATE_SHA) == 0) { ⚡ STAGE_OK: 0; }
        IF (p0r4_stage_write_verify(BASE + "/out/commit_receipt_sha.txt", RECEIPT_SHA) == 0) { ⚡ STAGE_OK: 0; }
        IF (STAGE_OK) {
            ⚡ FINAL_RC: p0r4_H("write_text", BASE + "/out/native_commit_intent.txt", "ALLOW_EXACT_STAGED_STATE", NULL);
        }
    }

    ⚡ print("SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1");
    ⚡ print("R4_NATIVE_LEARNING_TRANSACTION_MAIN", "ACTIVE_SOURCE_ONLY");
    ⚡ print("EVENT_TYPE", EVENT_TYPE);
    ⚡ print("ACTION", ACTION);
    ⚡ print("STATUS", STATUS);
    ⚡ print("COMMIT_ALLOWED", COMMIT_ALLOWED);
    ⚡ print("STAGE_OK", STAGE_OK);
}
