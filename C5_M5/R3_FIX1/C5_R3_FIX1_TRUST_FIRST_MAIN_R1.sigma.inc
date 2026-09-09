⟡(Σ.C5_AUTONOMOUS_SELF_LEARNING_CORE_V1) {
    ⚡ BASE: ".sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING";

    # Fresh invocation envelope. The mechanical runner must create BASE inside a
    # fresh per-invocation root and pre-bound every input file before VM start.
    ⚡ INVOCATION_ID: H("read_text", BASE + "/io/invocation_id.txt", NULL, NULL);
    ⚡ FRESH_ROOT_MARKER: H("read_text", BASE + "/io/fresh_root_marker.txt", NULL, NULL);
    ⚡ EVENT_TYPE: H("read_text", BASE + "/io/event_type.txt", NULL, NULL);
    ⚡ EXPECTED_PHASE: H("read_text", BASE + "/io/expected_phase.txt", NULL, NULL);

    ⚡ AUTHORITATIVE_CHAIN_HEAD: H("read_text", BASE + "/io/authoritative_state_chain_head.txt", NULL, NULL);
    ⚡ PARENT_STATE_SHA: H("read_text", BASE + "/io/parent_state_sha.txt", NULL, NULL);
    ⚡ PARENT_STATE_SNAPSHOT_SHA: H("read_text", BASE + "/io/parent_state_snapshot_sha.txt", NULL, NULL);
    ⚡ PARENT_STATE_SNAPSHOT: H("read_text", BASE + "/io/parent_state_snapshot.txt", NULL, NULL);

    # Canonical mechanical receipt fields.
    ⚡ RECEIPT_SHA: H("read_text", BASE + "/io/receipt_sha.txt", NULL, NULL);
    ⚡ RECEIPT_KIND: H("read_text", BASE + "/io/receipt_kind.txt", NULL, NULL);
    ⚡ RECEIPT_INVOCATION_ID: H("read_text", BASE + "/io/receipt_invocation_id.txt", NULL, NULL);
    ⚡ RECEIPT_EVENT_TYPE: H("read_text", BASE + "/io/receipt_event_type.txt", NULL, NULL);
    ⚡ RECEIPT_PHASE: H("read_text", BASE + "/io/receipt_phase.txt", NULL, NULL);
    ⚡ RECEIPT_PARENT_STATE_SHA: H("read_text", BASE + "/io/receipt_parent_state_sha.txt", NULL, NULL);
    ⚡ RECEIPT_ACTION_ID: H("read_text", BASE + "/io/receipt_action_id.txt", NULL, NULL);
    ⚡ RECEIPT_ARTIFACT_SHA: H("read_text", BASE + "/io/receipt_artifact_sha.txt", NULL, NULL);
    ⚡ RECEIPT_SUBJECT_ID: H("read_text", BASE + "/io/receipt_subject_id.txt", NULL, NULL);
    ⚡ RECEIPT_REQUEST_ID: H("read_text", BASE + "/io/receipt_request_id.txt", NULL, NULL);
    ⚡ RECEIPT_CAPABILITY_ID: H("read_text", BASE + "/io/receipt_capability_id.txt", NULL, NULL);
    ⚡ RECEIPT_CANDIDATE_SET_SHA: H("read_text", BASE + "/io/receipt_candidate_set_sha.txt", NULL, NULL);
    ⚡ RECEIPT_CANDIDATE_COUNT: H("read_text", BASE + "/io/receipt_candidate_count.txt", NULL, NULL);
    ⚡ RECEIPT_SOURCE_ID: H("read_text", BASE + "/io/receipt_source_id.txt", NULL, NULL);
    ⚡ RECEIPT_SOURCE_VERSION_SHA: H("read_text", BASE + "/io/receipt_source_version_sha.txt", NULL, NULL);
    ⚡ RECEIPT_OFFSET: H("read_text", BASE + "/io/receipt_offset.txt", NULL, NULL);

    # Event payload binding. The payload bytes themselves may be in a separate
    # bounded artifact; this core consumes only the authoritative reference here.
    ⚡ PAYLOAD_KIND: H("read_text", BASE + "/io/payload_kind.txt", NULL, NULL);
    ⚡ PAYLOAD_SHA: H("read_text", BASE + "/io/payload_sha.txt", NULL, NULL);
    ⚡ ACTION_ID: H("read_text", BASE + "/io/action_id.txt", NULL, NULL);

    # Segment/fetch/evidence/capability subject fields.
    ⚡ ENTRY_ID: H("read_text", BASE + "/io/entry_id.txt", NULL, NULL);
    ⚡ SOURCE_ID: H("read_text", BASE + "/io/source_id.txt", NULL, NULL);
    ⚡ SOURCE_VERSION_SHA: H("read_text", BASE + "/io/source_version_sha.txt", NULL, NULL);
    ⚡ EXPECTED_OFFSET: H("read_text", BASE + "/io/expected_offset.txt", NULL, NULL);
    ⚡ REQUEST_ID: H("read_text", BASE + "/io/request_id.txt", NULL, NULL);
    ⚡ CAPABILITY_ID: H("read_text", BASE + "/io/capability_id.txt", NULL, NULL);
    ⚡ CANDIDATE_SET_SHA: H("read_text", BASE + "/io/candidate_set_sha.txt", NULL, NULL);
    ⚡ CANDIDATE_COUNT: H("read_text", BASE + "/io/candidate_count.txt", NULL, NULL);

    ⚡ ACTION: "HOLD";
    ⚡ STATUS: "TRUST_ENVELOPE_NOT_ADMITTED";
    ⚡ COMMIT_ALLOWED: 0;
    ⚡ NEXT_STATE: "";
    ⚡ EVENT_BINDING: "";
    ⚡ PAYLOAD_REF: "";

    # Never trust a reused invocation root.
    IF (p0_safe_atom(INVOCATION_ID, 128) == 0) {
        ⚡ STATUS: "INVALID_INVOCATION_ID";
    }

    IF (p0_safe_atom(INVOCATION_ID, 128)) {
        IF (FRESH_ROOT_MARKER != INVOCATION_ID) {
            ⚡ STATUS: "FRESH_ROOT_BINDING_FAILED";
        }

        IF (FRESH_ROOT_MARKER == INVOCATION_ID) {
            IF (p0_event_valid(EVENT_TYPE) == 0) {
                ⚡ STATUS: "INVALID_EVENT_TYPE";
            }

            # Genesis is the only event without an existing SHA256 state head.
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
                IF (p0_hex64(RECEIPT_SHA) == 0) { ⚡ BOOT_OK: 0; }

                IF (BOOT_OK) {
                    ⚡ NEXT_STATE:
                        "STATE_VERSION=1\n"
                        + "PHASE=IDLE\n"
                        + "OBJECTIVE_ID=NONE\n"
                        + "PENDING_ACTION_ID=NONE\n"
                        + "PENDING_REQUEST_ID=NONE\n"
                        + "PENDING_CAPABILITY_ID=NONE\n"
                        + "PENDING_CANDIDATE_SET_SHA=NONE\n"
                        + "PENDING_CANDIDATE_COUNT=NONE\n"
                        + "PENDING_ENTRY_ID=NONE\n"
                        + "PENDING_SOURCE_ID=NONE\n"
                        + "PENDING_SOURCE_VERSION_SHA=NONE\n"
                        + "PENDING_OFFSET=NONE\n"
                        + "PENDING_PAYLOAD_KIND=NONE\n"
                        + "PENDING_PAYLOAD_SHA=NONE\n"
                        + "EPISTEMIC_STATE_SHA=NONE\n"
                        + "MEMORY_STATE_SHA=NONE\n"
                        + "LAST_RECEIPT_SHA=" + RECEIPT_SHA + "\n"
                        + "LAST_INVOCATION_ID=" + INVOCATION_ID + "\n"
                        + "LAST_ACTION_ID=NONE\n"
                        + "LAST_EVENT=BOOTSTRAP";

                    ⚡ EVENT_BINDING:
                        "INVOCATION_ID=" + INVOCATION_ID
                        + "\nEVENT_TYPE=BOOTSTRAP"
                        + "\nPHASE=GENESIS"
                        + "\nPARENT_STATE_SHA=GENESIS"
                        + "\nRECEIPT_SHA=" + RECEIPT_SHA;

                    ⚡ PAYLOAD_REF: "PAYLOAD_KIND=NONE\nPAYLOAD_SHA=NONE";
                    ⚡ ACTION: "STAGE_GENESIS_STATE";
                    ⚡ STATUS: "GENESIS_TRANSITION_TRUSTED";
                    ⚡ COMMIT_ALLOWED: 1;
                }

                IF (BOOT_OK == 0) {
                    ⚡ STATUS: "GENESIS_BINDING_REJECTED";
                }
            }

            IF (EVENT_TYPE != "BOOTSTRAP") {
                ⚡ ENVELOPE_OK: 1;

                IF (p0_hex64(AUTHORITATIVE_CHAIN_HEAD) == 0) { ⚡ ENVELOPE_OK: 0; }
                IF (p0_hex64(PARENT_STATE_SHA) == 0) { ⚡ ENVELOPE_OK: 0; }
                IF (p0_hex64(PARENT_STATE_SNAPSHOT_SHA) == 0) { ⚡ ENVELOPE_OK: 0; }
                IF (PARENT_STATE_SHA != AUTHORITATIVE_CHAIN_HEAD) { ⚡ ENVELOPE_OK: 0; }
                IF (PARENT_STATE_SNAPSHOT_SHA != PARENT_STATE_SHA) { ⚡ ENVELOPE_OK: 0; }
                IF (p0_state_snapshot_valid(PARENT_STATE_SNAPSHOT) == 0) { ⚡ ENVELOPE_OK: 0; }
                IF (p0_hex64(RECEIPT_SHA) == 0) { ⚡ ENVELOPE_OK: 0; }
                IF (p0_event_receipt_kind_matches(EVENT_TYPE, RECEIPT_KIND) == 0) { ⚡ ENVELOPE_OK: 0; }

                ⚡ STATE_PHASE: p0_state_value(PARENT_STATE_SNAPSHOT, 1, "PHASE");
                ⚡ STATE_OBJECTIVE_ID: p0_state_value(PARENT_STATE_SNAPSHOT, 2, "OBJECTIVE_ID");
                ⚡ STATE_PENDING_ACTION_ID: p0_state_value(PARENT_STATE_SNAPSHOT, 3, "PENDING_ACTION_ID");
                ⚡ STATE_PENDING_REQUEST_ID: p0_state_value(PARENT_STATE_SNAPSHOT, 4, "PENDING_REQUEST_ID");
                ⚡ STATE_PENDING_CAPABILITY_ID: p0_state_value(PARENT_STATE_SNAPSHOT, 5, "PENDING_CAPABILITY_ID");
                ⚡ STATE_PENDING_CANDIDATE_SET_SHA: p0_state_value(PARENT_STATE_SNAPSHOT, 6, "PENDING_CANDIDATE_SET_SHA");
                ⚡ STATE_PENDING_CANDIDATE_COUNT: p0_state_value(PARENT_STATE_SNAPSHOT, 7, "PENDING_CANDIDATE_COUNT");
                ⚡ STATE_PENDING_ENTRY_ID: p0_state_value(PARENT_STATE_SNAPSHOT, 8, "PENDING_ENTRY_ID");
                ⚡ STATE_PENDING_SOURCE_ID: p0_state_value(PARENT_STATE_SNAPSHOT, 9, "PENDING_SOURCE_ID");
                ⚡ STATE_PENDING_SOURCE_VERSION_SHA: p0_state_value(PARENT_STATE_SNAPSHOT, 10, "PENDING_SOURCE_VERSION_SHA");
                ⚡ STATE_PENDING_OFFSET: p0_state_value(PARENT_STATE_SNAPSHOT, 11, "PENDING_OFFSET");
                ⚡ STATE_EPISTEMIC_STATE_SHA: p0_state_value(PARENT_STATE_SNAPSHOT, 14, "EPISTEMIC_STATE_SHA");
                ⚡ STATE_MEMORY_STATE_SHA: p0_state_value(PARENT_STATE_SNAPSHOT, 15, "MEMORY_STATE_SHA");

                IF (EXPECTED_PHASE != STATE_PHASE) { ⚡ ENVELOPE_OK: 0; }

                IF (p0_receipt_envelope_shape_valid(
                    INVOCATION_ID,
                    EVENT_TYPE,
                    EXPECTED_PHASE,
                    PARENT_STATE_SHA,
                    ACTION_ID,
                    RECEIPT_KIND
                ) == 0) {
                    ⚡ ENVELOPE_OK: 0;
                }
                IF (RECEIPT_INVOCATION_ID != INVOCATION_ID) { ⚡ ENVELOPE_OK: 0; }
                IF (RECEIPT_EVENT_TYPE != EVENT_TYPE) { ⚡ ENVELOPE_OK: 0; }
                IF (RECEIPT_PHASE != EXPECTED_PHASE) { ⚡ ENVELOPE_OK: 0; }
                IF (RECEIPT_PARENT_STATE_SHA != PARENT_STATE_SHA) { ⚡ ENVELOPE_OK: 0; }
                IF (RECEIPT_ACTION_ID != ACTION_ID) { ⚡ ENVELOPE_OK: 0; }

                IF (ENVELOPE_OK == 0) {
                    ⚡ STATUS: "TRUST_ENVELOPE_REJECTED";
                }

                IF (ENVELOPE_OK) {
                    # TICK is a trusted no-op and never advances the state chain.
                    IF (EVENT_TYPE == "TICK") {
                        IF (STATE_PHASE != "IDLE") {
                            ⚡ STATUS: "TICK_WRONG_PHASE";
                        }
                        IF (STATE_PHASE == "IDLE") {
                            IF (ACTION_ID != "NONE") {
                                ⚡ STATUS: "TICK_ACTION_ID_MUST_BE_NONE";
                            }
                            IF (ACTION_ID == "NONE") {
                                ⚡ ACTION: "WAIT";
                                ⚡ STATUS: "TRUSTED_IDLE_TICK";
                            }
                        }
                    }

                    IF (EVENT_TYPE == "COGNITION_INPUT_READY") {
                        ⚡ KIND_OK: 1;
                        IF (STATE_PHASE != "IDLE") { ⚡ KIND_OK: 0; }
                        IF (ACTION_ID != "NONE") { ⚡ KIND_OK: 0; }
                        IF (p0_safe_atom(PAYLOAD_KIND, 64) == 0) { ⚡ KIND_OK: 0; }
                        IF (p0_hex64(PAYLOAD_SHA) == 0) { ⚡ KIND_OK: 0; }
                        IF (RECEIPT_ARTIFACT_SHA != PAYLOAD_SHA) { ⚡ KIND_OK: 0; }

                        IF (KIND_OK) {
                            ⚡ NEXT_STATE:
                                "STATE_VERSION=1\n"
                                + "PHASE=COGNITION_READY\n"
                                + "OBJECTIVE_ID=" + STATE_OBJECTIVE_ID + "\n"
                                + "PENDING_ACTION_ID=NONE\n"
                                + "PENDING_REQUEST_ID=NONE\n"
                                + "PENDING_CAPABILITY_ID=NONE\n"
                                + "PENDING_CANDIDATE_SET_SHA=NONE\n"
                                + "PENDING_CANDIDATE_COUNT=NONE\n"
                                + "PENDING_ENTRY_ID=NONE\n"
                                + "PENDING_SOURCE_ID=NONE\n"
                                + "PENDING_SOURCE_VERSION_SHA=NONE\n"
                                + "PENDING_OFFSET=NONE\n"
                                + "PENDING_PAYLOAD_KIND=" + PAYLOAD_KIND + "\n"
                                + "PENDING_PAYLOAD_SHA=" + PAYLOAD_SHA + "\n"
                                + "EPISTEMIC_STATE_SHA=" + STATE_EPISTEMIC_STATE_SHA + "\n"
                                + "MEMORY_STATE_SHA=" + STATE_MEMORY_STATE_SHA + "\n"
                                + "LAST_RECEIPT_SHA=" + RECEIPT_SHA + "\n"
                                + "LAST_INVOCATION_ID=" + INVOCATION_ID + "\n"
                                + "LAST_ACTION_ID=NONE\n"
                                + "LAST_EVENT=COGNITION_INPUT_READY";
                            ⚡ ACTION: "STAGE_TRUSTED_COGNITION_INPUT";
                            ⚡ STATUS: "COGNITION_INPUT_BOUND_TO_STATE";
                            ⚡ COMMIT_ALLOWED: 1;
                        }
                        IF (KIND_OK == 0) { ⚡ STATUS: "COGNITION_INPUT_BINDING_REJECTED"; }
                    }

                    IF (EVENT_TYPE == "SEGMENT_READY") {
                        ⚡ KIND_OK: 1;
                        IF (STATE_PHASE != "WAIT_SEGMENT") { ⚡ KIND_OK: 0; }
                        IF (STATE_PENDING_ACTION_ID != ACTION_ID) { ⚡ KIND_OK: 0; }
                        IF (STATE_PENDING_ENTRY_ID != ENTRY_ID) { ⚡ KIND_OK: 0; }
                        IF (STATE_PENDING_SOURCE_ID != SOURCE_ID) { ⚡ KIND_OK: 0; }
                        IF (STATE_PENDING_SOURCE_VERSION_SHA != SOURCE_VERSION_SHA) { ⚡ KIND_OK: 0; }
                        IF (STATE_PENDING_OFFSET != EXPECTED_OFFSET) { ⚡ KIND_OK: 0; }
                        IF (RECEIPT_SUBJECT_ID != ENTRY_ID) { ⚡ KIND_OK: 0; }
                        IF (RECEIPT_SOURCE_ID != SOURCE_ID) { ⚡ KIND_OK: 0; }
                        IF (RECEIPT_SOURCE_VERSION_SHA != SOURCE_VERSION_SHA) { ⚡ KIND_OK: 0; }
                        IF (RECEIPT_OFFSET != EXPECTED_OFFSET) { ⚡ KIND_OK: 0; }
                        IF (p0_safe_atom(PAYLOAD_KIND, 64) == 0) { ⚡ KIND_OK: 0; }
                        IF (p0_hex64(PAYLOAD_SHA) == 0) { ⚡ KIND_OK: 0; }
                        IF (RECEIPT_ARTIFACT_SHA != PAYLOAD_SHA) { ⚡ KIND_OK: 0; }

                        IF (KIND_OK) {
                            ⚡ NEXT_STATE:
                                "STATE_VERSION=1\n"
                                + "PHASE=COGNITION_READY\n"
                                + "OBJECTIVE_ID=" + STATE_OBJECTIVE_ID + "\n"
                                + "PENDING_ACTION_ID=NONE\n"
                                + "PENDING_REQUEST_ID=NONE\n"
                                + "PENDING_CAPABILITY_ID=NONE\n"
                                + "PENDING_CANDIDATE_SET_SHA=NONE\n"
                                + "PENDING_CANDIDATE_COUNT=NONE\n"
                                + "PENDING_ENTRY_ID=NONE\n"
                                + "PENDING_SOURCE_ID=NONE\n"
                                + "PENDING_SOURCE_VERSION_SHA=NONE\n"
                                + "PENDING_OFFSET=NONE\n"
                                + "PENDING_PAYLOAD_KIND=" + PAYLOAD_KIND + "\n"
                                + "PENDING_PAYLOAD_SHA=" + PAYLOAD_SHA + "\n"
                                + "EPISTEMIC_STATE_SHA=" + STATE_EPISTEMIC_STATE_SHA + "\n"
                                + "MEMORY_STATE_SHA=" + STATE_MEMORY_STATE_SHA + "\n"
                                + "LAST_RECEIPT_SHA=" + RECEIPT_SHA + "\n"
                                + "LAST_INVOCATION_ID=" + INVOCATION_ID + "\n"
                                + "LAST_ACTION_ID=" + ACTION_ID + "\n"
                                + "LAST_EVENT=SEGMENT_READY";
                            ⚡ ACTION: "STAGE_TRUSTED_SEGMENT";
                            ⚡ STATUS: "SEGMENT_RECEIPT_BOUND_TO_PENDING_STATE";
                            ⚡ COMMIT_ALLOWED: 1;
                        }
                        IF (KIND_OK == 0) { ⚡ STATUS: "SEGMENT_BINDING_REJECTED"; }
                    }

                    IF (EVENT_TYPE == "FETCH_READY") {
                        ⚡ KIND_OK: 1;
                        IF (STATE_PHASE != "WAIT_FETCH") { ⚡ KIND_OK: 0; }
                        IF (STATE_PENDING_ACTION_ID != ACTION_ID) { ⚡ KIND_OK: 0; }
                        IF (STATE_PENDING_REQUEST_ID != REQUEST_ID) { ⚡ KIND_OK: 0; }
                        IF (RECEIPT_REQUEST_ID != REQUEST_ID) { ⚡ KIND_OK: 0; }
                        IF (p0_safe_atom(PAYLOAD_KIND, 64) == 0) { ⚡ KIND_OK: 0; }
                        IF (p0_hex64(PAYLOAD_SHA) == 0) { ⚡ KIND_OK: 0; }
                        IF (RECEIPT_ARTIFACT_SHA != PAYLOAD_SHA) { ⚡ KIND_OK: 0; }

                        IF (KIND_OK) {
                            ⚡ NEXT_STATE:
                                "STATE_VERSION=1\n"
                                + "PHASE=COGNITION_READY\n"
                                + "OBJECTIVE_ID=" + STATE_OBJECTIVE_ID + "\n"
                                + "PENDING_ACTION_ID=NONE\n"
                                + "PENDING_REQUEST_ID=NONE\n"
                                + "PENDING_CAPABILITY_ID=NONE\n"
                                + "PENDING_CANDIDATE_SET_SHA=NONE\n"
                                + "PENDING_CANDIDATE_COUNT=NONE\n"
                                + "PENDING_ENTRY_ID=NONE\n"
                                + "PENDING_SOURCE_ID=NONE\n"
                                + "PENDING_SOURCE_VERSION_SHA=NONE\n"
                                + "PENDING_OFFSET=NONE\n"
                                + "PENDING_PAYLOAD_KIND=" + PAYLOAD_KIND + "\n"
                                + "PENDING_PAYLOAD_SHA=" + PAYLOAD_SHA + "\n"
                                + "EPISTEMIC_STATE_SHA=" + STATE_EPISTEMIC_STATE_SHA + "\n"
                                + "MEMORY_STATE_SHA=" + STATE_MEMORY_STATE_SHA + "\n"
                                + "LAST_RECEIPT_SHA=" + RECEIPT_SHA + "\n"
                                + "LAST_INVOCATION_ID=" + INVOCATION_ID + "\n"
                                + "LAST_ACTION_ID=" + ACTION_ID + "\n"
                                + "LAST_EVENT=FETCH_READY";
                            ⚡ ACTION: "STAGE_TRUSTED_FETCH_RESULT";
                            ⚡ STATUS: "FETCH_RECEIPT_BOUND_TO_NATIVE_REQUEST";
                            ⚡ COMMIT_ALLOWED: 1;
                        }
                        IF (KIND_OK == 0) { ⚡ STATUS: "FETCH_BINDING_REJECTED"; }
                    }

                    IF (EVENT_TYPE == "EVIDENCE_LOOKUP_READY") {
                        ⚡ KIND_OK: 1;
                        IF (STATE_PHASE != "WAIT_EVIDENCE") { ⚡ KIND_OK: 0; }
                        IF (STATE_PENDING_ACTION_ID != ACTION_ID) { ⚡ KIND_OK: 0; }
                        IF (STATE_PENDING_CANDIDATE_SET_SHA != CANDIDATE_SET_SHA) { ⚡ KIND_OK: 0; }
                        IF (STATE_PENDING_CANDIDATE_COUNT != CANDIDATE_COUNT) { ⚡ KIND_OK: 0; }
                        IF (RECEIPT_CANDIDATE_SET_SHA != CANDIDATE_SET_SHA) { ⚡ KIND_OK: 0; }
                        IF (RECEIPT_CANDIDATE_COUNT != CANDIDATE_COUNT) { ⚡ KIND_OK: 0; }
                        IF (p0_hex64(CANDIDATE_SET_SHA) == 0) { ⚡ KIND_OK: 0; }
                        IF (p0_digits_only(CANDIDATE_COUNT) == 0) { ⚡ KIND_OK: 0; }
                        IF (p0_safe_atom(PAYLOAD_KIND, 64) == 0) { ⚡ KIND_OK: 0; }
                        IF (p0_hex64(PAYLOAD_SHA) == 0) { ⚡ KIND_OK: 0; }
                        IF (RECEIPT_ARTIFACT_SHA != PAYLOAD_SHA) { ⚡ KIND_OK: 0; }

                        IF (KIND_OK) {
                            ⚡ NEXT_STATE:
                                "STATE_VERSION=1\n"
                                + "PHASE=COGNITION_READY\n"
                                + "OBJECTIVE_ID=" + STATE_OBJECTIVE_ID + "\n"
                                + "PENDING_ACTION_ID=NONE\n"
                                + "PENDING_REQUEST_ID=NONE\n"
                                + "PENDING_CAPABILITY_ID=NONE\n"
                                + "PENDING_CANDIDATE_SET_SHA=NONE\n"
                                + "PENDING_CANDIDATE_COUNT=NONE\n"
                                + "PENDING_ENTRY_ID=NONE\n"
                                + "PENDING_SOURCE_ID=NONE\n"
                                + "PENDING_SOURCE_VERSION_SHA=NONE\n"
                                + "PENDING_OFFSET=NONE\n"
                                + "PENDING_PAYLOAD_KIND=" + PAYLOAD_KIND + "\n"
                                + "PENDING_PAYLOAD_SHA=" + PAYLOAD_SHA + "\n"
                                + "EPISTEMIC_STATE_SHA=" + STATE_EPISTEMIC_STATE_SHA + "\n"
                                + "MEMORY_STATE_SHA=" + STATE_MEMORY_STATE_SHA + "\n"
                                + "LAST_RECEIPT_SHA=" + RECEIPT_SHA + "\n"
                                + "LAST_INVOCATION_ID=" + INVOCATION_ID + "\n"
                                + "LAST_ACTION_ID=" + ACTION_ID + "\n"
                                + "LAST_EVENT=EVIDENCE_LOOKUP_READY";
                            ⚡ ACTION: "STAGE_TRUSTED_EVIDENCE_LOOKUP_RESULT";
                            ⚡ STATUS: "EVIDENCE_RESPONSE_BOUND_TO_EXACT_CANDIDATE_SET";
                            ⚡ COMMIT_ALLOWED: 1;
                        }
                        IF (KIND_OK == 0) { ⚡ STATUS: "EVIDENCE_LOOKUP_BINDING_REJECTED"; }
                    }

                    IF (EVENT_TYPE == "CAPABILITY_RESULT_READY") {
                        ⚡ KIND_OK: 1;
                        IF (STATE_PHASE != "WAIT_CAPABILITY") { ⚡ KIND_OK: 0; }
                        IF (STATE_PENDING_ACTION_ID != ACTION_ID) { ⚡ KIND_OK: 0; }
                        IF (STATE_PENDING_CAPABILITY_ID != CAPABILITY_ID) { ⚡ KIND_OK: 0; }
                        IF (RECEIPT_CAPABILITY_ID != CAPABILITY_ID) { ⚡ KIND_OK: 0; }
                        IF (p0_safe_atom(CAPABILITY_ID, 128) == 0) { ⚡ KIND_OK: 0; }
                        IF (p0_safe_atom(PAYLOAD_KIND, 64) == 0) { ⚡ KIND_OK: 0; }
                        IF (p0_hex64(PAYLOAD_SHA) == 0) { ⚡ KIND_OK: 0; }
                        IF (RECEIPT_ARTIFACT_SHA != PAYLOAD_SHA) { ⚡ KIND_OK: 0; }

                        IF (KIND_OK) {
                            ⚡ NEXT_STATE:
                                "STATE_VERSION=1\n"
                                + "PHASE=COGNITION_READY\n"
                                + "OBJECTIVE_ID=" + STATE_OBJECTIVE_ID + "\n"
                                + "PENDING_ACTION_ID=NONE\n"
                                + "PENDING_REQUEST_ID=NONE\n"
                                + "PENDING_CAPABILITY_ID=NONE\n"
                                + "PENDING_CANDIDATE_SET_SHA=NONE\n"
                                + "PENDING_CANDIDATE_COUNT=NONE\n"
                                + "PENDING_ENTRY_ID=NONE\n"
                                + "PENDING_SOURCE_ID=NONE\n"
                                + "PENDING_SOURCE_VERSION_SHA=NONE\n"
                                + "PENDING_OFFSET=NONE\n"
                                + "PENDING_PAYLOAD_KIND=" + PAYLOAD_KIND + "\n"
                                + "PENDING_PAYLOAD_SHA=" + PAYLOAD_SHA + "\n"
                                + "EPISTEMIC_STATE_SHA=" + STATE_EPISTEMIC_STATE_SHA + "\n"
                                + "MEMORY_STATE_SHA=" + STATE_MEMORY_STATE_SHA + "\n"
                                + "LAST_RECEIPT_SHA=" + RECEIPT_SHA + "\n"
                                + "LAST_INVOCATION_ID=" + INVOCATION_ID + "\n"
                                + "LAST_ACTION_ID=" + ACTION_ID + "\n"
                                + "LAST_EVENT=CAPABILITY_RESULT_READY";
                            ⚡ ACTION: "STAGE_TRUSTED_CAPABILITY_RESULT";
                            ⚡ STATUS: "CAPABILITY_RESULT_BOUND_TO_NATIVE_PENDING_ACTION";
                            ⚡ COMMIT_ALLOWED: 1;
                        }
                        IF (KIND_OK == 0) { ⚡ STATUS: "CAPABILITY_RESULT_BINDING_REJECTED"; }
                    }

                    IF (COMMIT_ALLOWED) {
                        ⚡ EVENT_BINDING:
                            "INVOCATION_ID=" + INVOCATION_ID
                            + "\nEVENT_TYPE=" + EVENT_TYPE
                            + "\nPHASE=" + EXPECTED_PHASE
                            + "\nPARENT_STATE_SHA=" + PARENT_STATE_SHA
                            + "\nACTION_ID=" + ACTION_ID
                            + "\nRECEIPT_SHA=" + RECEIPT_SHA
                            + "\nRECEIPT_KIND=" + RECEIPT_KIND;

                        ⚡ PAYLOAD_REF:
                            "PAYLOAD_KIND=" + PAYLOAD_KIND
                            + "\nPAYLOAD_SHA=" + PAYLOAD_SHA;
                    }
                }
            }
        }
    }

    # No persistent-state mutation exists in this core. It writes only into the
    # fresh invocation out/ surface. Mechanical commit is a later atomic step.
    ⚡ STAGE_OK: 1;

    IF (p0_stage_write_verify(BASE + "/out/action.txt", ACTION) == 0) {
        ⚡ STAGE_OK: 0;
    }
    IF (p0_stage_write_verify(BASE + "/out/status.txt", STATUS) == 0) {
        ⚡ STAGE_OK: 0;
    }

    IF (COMMIT_ALLOWED) {
        IF (p0_state_snapshot_valid(NEXT_STATE) == 0) {
            ⚡ STAGE_OK: 0;
        }

        IF (p0_stage_write_verify(BASE + "/out/stage_next_state.txt", NEXT_STATE) == 0) {
            ⚡ STAGE_OK: 0;
        }
        IF (p0_stage_write_verify(BASE + "/out/stage_event_binding.txt", EVENT_BINDING) == 0) {
            ⚡ STAGE_OK: 0;
        }
        IF (p0_stage_write_verify(BASE + "/out/stage_payload_ref.txt", PAYLOAD_REF) == 0) {
            ⚡ STAGE_OK: 0;
        }
        IF (p0_stage_write_verify(BASE + "/out/commit_parent_state_sha.txt", PARENT_STATE_SHA) == 0) {
            ⚡ STAGE_OK: 0;
        }
        IF (p0_stage_write_verify(BASE + "/out/commit_receipt_sha.txt", RECEIPT_SHA) == 0) {
            ⚡ STAGE_OK: 0;
        }

        # Positive permission is the final authoritative file write.
        IF (STAGE_OK) {
            ⚡ FINAL_RC: H("write_text", BASE + "/out/native_commit_intent.txt", "ALLOW_EXACT_STAGED_STATE", NULL);
        }
    }

    ⚡ print("SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1");
    ⚡ print("R3_FIX1_P0_TRUST_STATE", "ACTIVE");
    ⚡ print("EVENT_TYPE", EVENT_TYPE);
    ⚡ print("ACTION", ACTION);
    ⚡ print("STATUS", STATUS);
    ⚡ print("COMMIT_ALLOWED", COMMIT_ALLOWED);
    ⚡ print("STAGE_OK", STAGE_OK);
}
