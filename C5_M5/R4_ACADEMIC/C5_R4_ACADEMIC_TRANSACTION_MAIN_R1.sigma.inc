⟡(Σ.C5_AUTONOMOUS_SELF_LEARNING_CORE_V1) {
    ⚡ BASE: ".sigma_exec/SIGMA_C5_AUTONOMOUS_SELF_LEARNING";
    ⚡ INVOCATION_ID: p0r4_H("read_text", BASE + "/io/invocation_id.txt", NULL, NULL);
    ⚡ FRESH_ROOT_MARKER: p0r4_H("read_text", BASE + "/io/fresh_root_marker.txt", NULL, NULL);
    ⚡ EVENT_TYPE: p0r4_H("read_text", BASE + "/io/event_type.txt", NULL, NULL);
    ⚡ EXPECTED_PHASE: p0r4_H("read_text", BASE + "/io/expected_phase.txt", NULL, NULL);
    ⚡ AUTHORITATIVE_CHAIN_HEAD: p0r4_H("read_text", BASE + "/io/authoritative_state_chain_head.txt", NULL, NULL);
    ⚡ PARENT_STATE_SHA: p0r4_H("read_text", BASE + "/io/parent_state_sha.txt", NULL, NULL);
    ⚡ PARENT_STATE_SNAPSHOT_SHA: p0r4_H("read_text", BASE + "/io/parent_state_snapshot_sha.txt", NULL, NULL);
    ⚡ PARENT_STATE_SNAPSHOT: p0r4_H("read_text", BASE + "/io/parent_state_snapshot.txt", NULL, NULL);
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
    ⚡ ACTION_ID: p0r4_H("read_text", BASE + "/io/action_id.txt", NULL, NULL);
    ⚡ INPUT_PAYLOAD_SHA: p0r4_H("read_text", BASE + "/io/input_payload_sha.txt", NULL, NULL);
    ⚡ BOUND_MEMORY_SHA: p0r4_H("read_text", BASE + "/io/bound_memory_sha.txt", NULL, NULL);
    ⚡ LEARNING_MODE: p0r4_H("read_text", BASE + "/io/learning_mode.txt", NULL, NULL);
    ⚡ CAPABILITY_REGISTRY: p0r4_H("read_text", BASE + "/io/capability_registry.txt", NULL, NULL);
    ⚡ ACADEMIC_DOCUMENT_ID: p0r4_H("read_text", BASE + "/io/academic_document_id.txt", NULL, NULL);
    ⚡ ACADEMIC_DOCUMENT_SHA: p0r4_H("read_text", BASE + "/io/academic_document_sha.txt", NULL, NULL);
    ⚡ ACADEMIC_DOCUMENT_BYTE_LEN: p0r4_H("read_text", BASE + "/io/academic_document_byte_len.txt", NULL, NULL);
    ⚡ ACADEMIC_SOURCE_ID: p0r4_H("read_text", BASE + "/io/academic_source_id.txt", NULL, NULL);
    ⚡ ACADEMIC_SOURCE_VERSION_SHA: p0r4_H("read_text", BASE + "/io/academic_source_version_sha.txt", NULL, NULL);
    ⚡ ACADEMIC_CONTENT_KIND: p0r4_H("read_text", BASE + "/io/academic_content_kind.txt", NULL, NULL);
    ⚡ ACADEMIC_PROVENANCE_SHA: p0r4_H("read_text", BASE + "/io/academic_provenance_sha.txt", NULL, NULL);
    ⚡ ACADEMIC_PASSAGE_ID: p0r4_H("read_text", BASE + "/io/academic_passage_id.txt", NULL, NULL);
    ⚡ ACADEMIC_PASSAGE_START_OFFSET: p0r4_H("read_text", BASE + "/io/academic_passage_start_offset.txt", NULL, NULL);
    ⚡ ACADEMIC_PASSAGE_END_OFFSET: p0r4_H("read_text", BASE + "/io/academic_passage_end_offset.txt", NULL, NULL);
    ⚡ ACADEMIC_PASSAGE_CONTENT_SHA: p0r4_H("read_text", BASE + "/io/academic_passage_content_sha.txt", NULL, NULL);
    ⚡ ACADEMIC_PASSAGE_EOF_STATE: p0r4_H("read_text", BASE + "/io/academic_passage_eof_state.txt", NULL, NULL);
    ⚡ ACADEMIC_SEED_WORK: p0r4_H("read_text", BASE + "/io/academic_seed_work.txt", NULL, NULL);
    ⚡ ACADEMIC_SEED_OBJECTIVE: p0r4_H("read_text", BASE + "/io/academic_seed_objective.txt", NULL, NULL);
    ⚡ ACADEMIC_SEED_GAP: p0r4_H("read_text", BASE + "/io/academic_seed_gap.txt", NULL, NULL);
    ⚡ ACADEMIC_SEED_QUESTION: p0r4_H("read_text", BASE + "/io/academic_seed_question.txt", NULL, NULL);
    ⚡ ACADEMIC_SEED_DOCUMENT: p0r4_H("read_text", BASE + "/io/academic_seed_document.txt", NULL, NULL);
    ⚡ ACADEMIC_SEED_PASSAGE: p0r4_H("read_text", BASE + "/io/academic_seed_passage.txt", NULL, NULL);
    ⚡ ACADEMIC_SEED_CURSOR: p0r4_H("read_text", BASE + "/io/academic_seed_cursor.txt", NULL, NULL);
    ⚡ ACADEMIC_SEED_STRUCTURE: p0r4_H("read_text", BASE + "/io/academic_seed_structure.txt", NULL, NULL);
    ⚡ ACADEMIC_SEED_CAPABILITY_REQUEST: p0r4_H("read_text", BASE + "/io/academic_seed_capability_request.txt", NULL, NULL);
    ⚡ ACADEMIC_TEXT_RESULT: p0r4_H("read_text", BASE + "/io/academic_text_result.txt", NULL, NULL);
    ⚡ MEMORY_TEXT: p0r4_H("read_text", BASE + "/io/memory_text.txt", NULL, NULL);
    ⚡ RECALL_CLAIM_ID: p0r4_H("read_text", BASE + "/io/recall_claim_id.txt", NULL, NULL);
    ⚡ RECALL_GAP_ID: p0r4_H("read_text", BASE + "/io/recall_gap_id.txt", NULL, NULL);
    ⚡ RECALL_QUESTION_ID: p0r4_H("read_text", BASE + "/io/recall_question_id.txt", NULL, NULL);
    ⚡ ACTION: "HOLD";
    ⚡ STATUS: "R4_ACADEMIC_TRUST_ENVELOPE_NOT_ADMITTED";
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
                    ⚡ NEXT_STATE: "STATE_VERSION=2\nPHASE=IDLE\nOBJECTIVE_ID=NONE\nACTIVE_GAP_ID=NONE\nPENDING_ACTION_ID=NONE\nPENDING_REQUEST_ID=NONE\nPENDING_CAPABILITY_ID=NONE\nPENDING_SUBJECT_ID=NONE\nPENDING_PAYLOAD_KIND=NONE\nPENDING_PAYLOAD_SHA=NONE\nEPISTEMIC_STATE_SHA=NONE\nMEMORY_STATE_SHA=NONE\nLAST_RECEIPT_SHA=" + RECEIPT_SHA + "\nLAST_INVOCATION_ID=" + INVOCATION_ID + "\nLAST_ACTION_ID=NONE\nLAST_EVENT=BOOTSTRAP\nLAST_SOURCE_ID=NONE\nLAST_SOURCE_VERSION_SHA=NONE\nLAST_ARTIFACT_SHA=NONE\nLAST_EVIDENCE_ID=NONE";
                    ⚡ ACTION: "BOOTSTRAP_R4_ACADEMIC_STATE";
                    ⚡ STATUS: "R4_ACADEMIC_GENESIS_TRUSTED";
                    ⚡ COMMIT_ALLOWED: 1;
                }
                IF (BOOT_OK == 0) { ⚡ STATUS: "R4_ACADEMIC_GENESIS_BINDING_REJECTED"; }
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
                IF (ENVELOPE_OK == 0) { ⚡ STATUS: "R4_ACADEMIC_TRUST_ENVELOPE_REJECTED"; }
                IF (ENVELOPE_OK) {
                    IF (EVENT_TYPE == "TICK") {
                        IF (STATE_PHASE == "IDLE") {
                            IF (ACTION_ID == "NONE") {
                                ⚡ ACTION: "WAIT";
                                ⚡ STATUS: "R4_ACADEMIC_TRUSTED_IDLE_TICK";
                            }
                        }
                        IF (STATE_PHASE == "WAIT_CAPABILITY") {
                            IF (STATE_PENDING_CAPABILITY_ID == "NONE") {
                                IF (ACTION_ID == "NONE") {
                                    ⚡ SELECTED_CAPABILITY: c5ac1_unique_admitted_capability(CAPABILITY_REGISTRY, "TEXT_INTERPRETATION");
                                    IF (SELECTED_CAPABILITY == "") {
                                        ⚡ ACTION: "WAIT";
                                        ⚡ STATUS: "R4_ACADEMIC_TEXT_CAPABILITY_UNAVAILABLE_OR_AMBIGUOUS";
                                    }
                                    IF (SELECTED_CAPABILITY != "") {
                                        ⚡ SELECT_OK: 1;
                                        IF (c5as1_work_valid(ACADEMIC_SEED_WORK) == 0) { ⚡ SELECT_OK: 0; }
                                        IF (c5t2_objective_valid(ACADEMIC_SEED_OBJECTIVE) == 0) { ⚡ SELECT_OK: 0; }
                                        IF (c5l2_gap_valid(ACADEMIC_SEED_GAP) == 0) { ⚡ SELECT_OK: 0; }
                                        IF (c5as1_question_valid(ACADEMIC_SEED_QUESTION) == 0) { ⚡ SELECT_OK: 0; }
                                        IF (c5ad1_document_valid(ACADEMIC_SEED_DOCUMENT) == 0) { ⚡ SELECT_OK: 0; }
                                        IF (c5ad1_passage_valid(ACADEMIC_SEED_PASSAGE) == 0) { ⚡ SELECT_OK: 0; }
                                        IF (c5ad1_cursor_valid(ACADEMIC_SEED_CURSOR) == 0) { ⚡ SELECT_OK: 0; }
                                        IF (c5am1_structure_valid(ACADEMIC_SEED_STRUCTURE) == 0) { ⚡ SELECT_OK: 0; }
                                        IF (c5l2_field(ACADEMIC_SEED_OBJECTIVE, 1, "OBJECTIVE_ID") != STATE_OBJECTIVE_ID) { ⚡ SELECT_OK: 0; }
                                        IF (c5l2_field(ACADEMIC_SEED_GAP, 1, "GAP_ID") != STATE_ACTIVE_GAP_ID) { ⚡ SELECT_OK: 0; }
                                        IF (c5l2_field(ACADEMIC_SEED_WORK, 3, "SUBJECT_ID") != STATE_PENDING_SUBJECT_ID) { ⚡ SELECT_OK: 0; }
                                        IF (c5l2_field(ACADEMIC_SEED_PASSAGE, 5, "CONTENT_SHA") != STATE_PENDING_PAYLOAD_SHA) { ⚡ SELECT_OK: 0; }
                                        IF (SELECT_OK) {
                                            ⚡ CAPABILITY_ID: c5l2_field(SELECTED_CAPABILITY, 1, "CAPABILITY_ID");
                                            ⚡ CAP_ACTION_ID: "ACAP_" + INVOCATION_ID;
                                            ⚡ CAP_REQUEST: c5ac1_make_request(CAP_ACTION_ID, SELECTED_CAPABILITY, "TEXT_INTERPRETATION", STATE_PENDING_SUBJECT_ID, ACADEMIC_SEED_PASSAGE);
                                            IF (c5ac1_request_valid(CAP_REQUEST) == 0) { ⚡ SELECT_OK: 0; }
                                            IF (SELECT_OK) {
                                                IF (p0r4_stage_write_verify(BASE + "/out/academic_selected_capability.txt", SELECTED_CAPABILITY) == 0) { ⚡ STAGE_OK: 0; }
                                                IF (p0r4_stage_write_verify(BASE + "/out/academic_capability_request.txt", CAP_REQUEST) == 0) { ⚡ STAGE_OK: 0; }
                                                ⚡ NEXT_STATE: "STATE_VERSION=2\nPHASE=WAIT_CAPABILITY\nOBJECTIVE_ID=" + STATE_OBJECTIVE_ID + "\nACTIVE_GAP_ID=" + STATE_ACTIVE_GAP_ID + "\nPENDING_ACTION_ID=" + CAP_ACTION_ID + "\nPENDING_REQUEST_ID=NONE\nPENDING_CAPABILITY_ID=" + CAPABILITY_ID + "\nPENDING_SUBJECT_ID=" + STATE_PENDING_SUBJECT_ID + "\nPENDING_PAYLOAD_KIND=ACADEMIC_CAPABILITY_REQUEST\nPENDING_PAYLOAD_SHA=" + STATE_PENDING_PAYLOAD_SHA + "\nEPISTEMIC_STATE_SHA=" + STATE_EPISTEMIC_STATE_SHA + "\nMEMORY_STATE_SHA=" + STATE_MEMORY_STATE_SHA + "\nLAST_RECEIPT_SHA=" + RECEIPT_SHA + "\nLAST_INVOCATION_ID=" + INVOCATION_ID + "\nLAST_ACTION_ID=" + CAP_ACTION_ID + "\nLAST_EVENT=TICK\nLAST_SOURCE_ID=" + c5l2_field(ACADEMIC_SEED_DOCUMENT, 2, "SOURCE_ID") + "\nLAST_SOURCE_VERSION_SHA=" + c5l2_field(ACADEMIC_SEED_DOCUMENT, 3, "SOURCE_VERSION_SHA") + "\nLAST_ARTIFACT_SHA=" + STATE_PENDING_PAYLOAD_SHA + "\nLAST_EVIDENCE_ID=NONE";
                                                ⚡ ACTION: "EXECUTE_EXACT_NATIVE_CAPABILITY";
                                                ⚡ STATUS: "R4_ACADEMIC_NATIVE_TEXT_CAPABILITY_SELECTED";
                                                ⚡ NEXT_ACTION_ID: CAP_ACTION_ID;
                                                ⚡ COMMIT_ALLOWED: 1;
                                            }
                                        }
                                        IF (SELECT_OK == 0) { ⚡ STATUS: "R4_ACADEMIC_CAPABILITY_SELECTION_SEED_REJECTED"; }
                                    }
                                }
                            }
                            IF (STATE_PENDING_CAPABILITY_ID != "NONE") {
                                IF (ACTION_ID == STATE_PENDING_ACTION_ID) {
                                    ⚡ ACTION: "WAIT";
                                    ⚡ STATUS: "R4_ACADEMIC_WAIT_CAPABILITY_RESULT";
                                }
                            }
                        }
                    }
                    IF (EVENT_TYPE == "LEARNING_INPUT_READY") {
                        ⚡ INPUT_OK: 1;
                        IF (STATE_PHASE != "IDLE") { ⚡ INPUT_OK: 0; }
                        IF (ACTION_ID != "NONE") { ⚡ INPUT_OK: 0; }
                        IF (LEARNING_MODE != "ACADEMIC_DOCUMENT") { ⚡ INPUT_OK: 0; }
                        IF (p0r4_hex64(INPUT_PAYLOAD_SHA) == 0) { ⚡ INPUT_OK: 0; }
                        IF (RECEIPT_ARTIFACT_SHA != INPUT_PAYLOAD_SHA) { ⚡ INPUT_OK: 0; }
                        IF (p0r4_safe_atom(ACADEMIC_DOCUMENT_ID, 112) == 0) { ⚡ INPUT_OK: 0; }
                        IF (p0r4_hex64(ACADEMIC_DOCUMENT_SHA) == 0) { ⚡ INPUT_OK: 0; }
                        IF (c5l2_digits_only(ACADEMIC_DOCUMENT_BYTE_LEN) == 0) { ⚡ INPUT_OK: 0; }
                        IF (p0r4_safe_atom(ACADEMIC_SOURCE_ID, 128) == 0) { ⚡ INPUT_OK: 0; }
                        IF (p0r4_hex64(ACADEMIC_SOURCE_VERSION_SHA) == 0) { ⚡ INPUT_OK: 0; }
                        IF (c5ad1_content_kind_valid(ACADEMIC_CONTENT_KIND) == 0) { ⚡ INPUT_OK: 0; }
                        IF (p0r4_hex64(ACADEMIC_PROVENANCE_SHA) == 0) { ⚡ INPUT_OK: 0; }
                        IF (p0r4_safe_atom(ACADEMIC_PASSAGE_ID, 112) == 0) { ⚡ INPUT_OK: 0; }
                        IF (c5l2_digits_only(ACADEMIC_PASSAGE_START_OFFSET) == 0) { ⚡ INPUT_OK: 0; }
                        IF (c5l2_digits_only(ACADEMIC_PASSAGE_END_OFFSET) == 0) { ⚡ INPUT_OK: 0; }
                        IF (p0r4_hex64(ACADEMIC_PASSAGE_CONTENT_SHA) == 0) { ⚡ INPUT_OK: 0; }
                        IF (c5ad1_eof_state_valid(ACADEMIC_PASSAGE_EOF_STATE) == 0) { ⚡ INPUT_OK: 0; }
                        IF (INPUT_OK) {
                            ⚡ SUBJECT_ID: "DOCSUB_" + ACADEMIC_DOCUMENT_ID;
                            ⚡ OBJECTIVE_ID: "AOBJ_" + INVOCATION_ID;
                            ⚡ WORK_ID: "AWORK_" + INVOCATION_ID;
                            ⚡ TEXT_GAP_ID: "AGAP_TEXT_" + INVOCATION_ID;
                            ⚡ TEXT_QUESTION_ID: "AQ_TEXT_" + INVOCATION_ID;
                            ⚡ BINDING: c5ad1_make_document_binding(ACADEMIC_SOURCE_ID, ACADEMIC_SOURCE_VERSION_SHA, ACADEMIC_CONTENT_KIND, ACADEMIC_PROVENANCE_SHA);
                            ⚡ DOCUMENT: c5ad1_make_document(ACADEMIC_DOCUMENT_ID, ACADEMIC_DOCUMENT_SHA, ACADEMIC_DOCUMENT_BYTE_LEN, BINDING);
                            ⚡ PASSAGE: c5ad1_make_passage(ACADEMIC_PASSAGE_ID, ACADEMIC_DOCUMENT_ID, ACADEMIC_PASSAGE_START_OFFSET, ACADEMIC_PASSAGE_END_OFFSET, ACADEMIC_PASSAGE_CONTENT_SHA, ACADEMIC_PASSAGE_EOF_STATE);
                            ⚡ PRE_CURSOR: c5ad1_make_cursor(ACADEMIC_DOCUMENT_ID, ACADEMIC_PASSAGE_START_OFFSET, "MORE", "NONE");
                            ⚡ CURSOR: c5ad1_cursor_advance(PRE_CURSOR, PASSAGE);
                            ⚡ OBJECTIVE: c5t2_make_objective(OBJECTIVE_ID, "OPEN", SUBJECT_ID, "1");
                            ⚡ WORK: c5as1_make_work(WORK_ID, "OPEN", SUBJECT_ID, OBJECTIVE_ID, "1");
                            ⚡ TEXT_GAP: c5t2_make_gap(TEXT_GAP_ID, OBJECTIVE_ID, "CAPABILITY", SUBJECT_ID, "TEXT_INTERPRETATION", "1");
                            ⚡ TEXT_QUESTION: c5as1_make_question(TEXT_QUESTION_ID, WORK_ID, SUBJECT_ID, "TEXT_CAPABILITY", "TEXT_INTERPRETATION", "1");
                            ⚡ STRUCTURE: c5ad1_pack_structure(DOCUMENT, PASSAGE, "", CURSOR);
                            IF (BINDING == "") { ⚡ INPUT_OK: 0; }
                            IF (DOCUMENT == "") { ⚡ INPUT_OK: 0; }
                            IF (PASSAGE == "") { ⚡ INPUT_OK: 0; }
                            IF (CURSOR == "") { ⚡ INPUT_OK: 0; }
                            IF (OBJECTIVE == "") { ⚡ INPUT_OK: 0; }
                            IF (WORK == "") { ⚡ INPUT_OK: 0; }
                            IF (TEXT_GAP == "") { ⚡ INPUT_OK: 0; }
                            IF (TEXT_QUESTION == "") { ⚡ INPUT_OK: 0; }
                            IF (c5am1_structure_valid(STRUCTURE) == 0) { ⚡ INPUT_OK: 0; }
                            IF (INPUT_OK) {
                                IF (p0r4_stage_write_verify(BASE + "/out/academic_seed_work.txt", WORK) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/academic_seed_objective.txt", OBJECTIVE) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/academic_seed_gap.txt", TEXT_GAP) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/academic_seed_question.txt", TEXT_QUESTION) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/academic_seed_document.txt", DOCUMENT) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/academic_seed_passage.txt", PASSAGE) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/academic_seed_cursor.txt", CURSOR) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/academic_seed_structure.txt", STRUCTURE) == 0) { ⚡ STAGE_OK: 0; }
                                ⚡ NEXT_STATE: "STATE_VERSION=2\nPHASE=WAIT_CAPABILITY\nOBJECTIVE_ID=" + OBJECTIVE_ID + "\nACTIVE_GAP_ID=" + TEXT_GAP_ID + "\nPENDING_ACTION_ID=NONE\nPENDING_REQUEST_ID=NONE\nPENDING_CAPABILITY_ID=NONE\nPENDING_SUBJECT_ID=" + SUBJECT_ID + "\nPENDING_PAYLOAD_KIND=ACADEMIC_TEXT_CAPABILITY_NEED\nPENDING_PAYLOAD_SHA=" + ACADEMIC_PASSAGE_CONTENT_SHA + "\nEPISTEMIC_STATE_SHA=" + INPUT_PAYLOAD_SHA + "\nMEMORY_STATE_SHA=" + STATE_MEMORY_STATE_SHA + "\nLAST_RECEIPT_SHA=" + RECEIPT_SHA + "\nLAST_INVOCATION_ID=" + INVOCATION_ID + "\nLAST_ACTION_ID=NONE\nLAST_EVENT=LEARNING_INPUT_READY\nLAST_SOURCE_ID=" + ACADEMIC_SOURCE_ID + "\nLAST_SOURCE_VERSION_SHA=" + ACADEMIC_SOURCE_VERSION_SHA + "\nLAST_ARTIFACT_SHA=" + ACADEMIC_PASSAGE_CONTENT_SHA + "\nLAST_EVIDENCE_ID=NONE";
                                ⚡ ACTION: "OPEN_NATIVE_TEXT_CAPABILITY_GAP";
                                ⚡ STATUS: "R4_ACADEMIC_DOCUMENT_STRUCTURED_CAPABILITY_NEEDED";
                                ⚡ COMMIT_ALLOWED: 1;
                            }
                        }
                        IF (INPUT_OK == 0) { ⚡ STATUS: "R4_ACADEMIC_DOCUMENT_INPUT_REJECTED"; }
                    }
                    IF (EVENT_TYPE == "CAPABILITY_RESULT_READY") {
                        ⚡ RESULT_OK: 1;
                        IF (STATE_PHASE != "WAIT_CAPABILITY") { ⚡ RESULT_OK: 0; }
                        IF (STATE_PENDING_CAPABILITY_ID == "NONE") { ⚡ RESULT_OK: 0; }
                        IF (ACTION_ID != STATE_PENDING_ACTION_ID) { ⚡ RESULT_OK: 0; }
                        IF (RECEIPT_SUBJECT_ID != STATE_PENDING_SUBJECT_ID) { ⚡ RESULT_OK: 0; }
                        IF (p0r4_hex64(RECEIPT_ARTIFACT_SHA) == 0) { ⚡ RESULT_OK: 0; }
                        IF (c5as1_work_valid(ACADEMIC_SEED_WORK) == 0) { ⚡ RESULT_OK: 0; }
                        IF (c5t2_objective_valid(ACADEMIC_SEED_OBJECTIVE) == 0) { ⚡ RESULT_OK: 0; }
                        IF (c5l2_gap_valid(ACADEMIC_SEED_GAP) == 0) { ⚡ RESULT_OK: 0; }
                        IF (c5as1_question_valid(ACADEMIC_SEED_QUESTION) == 0) { ⚡ RESULT_OK: 0; }
                        IF (c5ad1_document_valid(ACADEMIC_SEED_DOCUMENT) == 0) { ⚡ RESULT_OK: 0; }
                        IF (c5ad1_passage_valid(ACADEMIC_SEED_PASSAGE) == 0) { ⚡ RESULT_OK: 0; }
                        IF (c5ad1_cursor_valid(ACADEMIC_SEED_CURSOR) == 0) { ⚡ RESULT_OK: 0; }
                        IF (c5am1_structure_valid(ACADEMIC_SEED_STRUCTURE) == 0) { ⚡ RESULT_OK: 0; }
                        IF (c5ac1_request_valid(ACADEMIC_SEED_CAPABILITY_REQUEST) == 0) { ⚡ RESULT_OK: 0; }
                        IF (c5ac1_text_result_valid(ACADEMIC_TEXT_RESULT) == 0) { ⚡ RESULT_OK: 0; }
                        IF (c5l2_field(ACADEMIC_SEED_OBJECTIVE, 1, "OBJECTIVE_ID") != STATE_OBJECTIVE_ID) { ⚡ RESULT_OK: 0; }
                        IF (c5l2_field(ACADEMIC_SEED_GAP, 1, "GAP_ID") != STATE_ACTIVE_GAP_ID) { ⚡ RESULT_OK: 0; }
                        IF (c5l2_field(ACADEMIC_SEED_CAPABILITY_REQUEST, 1, "ACTION_ID") != STATE_PENDING_ACTION_ID) { ⚡ RESULT_OK: 0; }
                        IF (c5l2_field(ACADEMIC_SEED_CAPABILITY_REQUEST, 2, "CAPABILITY_ID") != STATE_PENDING_CAPABILITY_ID) { ⚡ RESULT_OK: 0; }
                        IF (c5l2_field(ACADEMIC_SEED_CAPABILITY_REQUEST, 4, "SUBJECT_ID") != STATE_PENDING_SUBJECT_ID) { ⚡ RESULT_OK: 0; }
                        IF (c5l2_field(ACADEMIC_SEED_CAPABILITY_REQUEST, 6, "BASIS_SHA") != STATE_PENDING_PAYLOAD_SHA) { ⚡ RESULT_OK: 0; }
                        IF (c5ac1_result_matches_request(ACADEMIC_TEXT_RESULT, ACADEMIC_SEED_CAPABILITY_REQUEST) == 0) { ⚡ RESULT_OK: 0; }
                        IF (RESULT_OK) {
                            ⚡ OBS_ID: "AOBS_" + INVOCATION_ID;
                            ⚡ CLAIM_ID: "ACL_" + INVOCATION_ID;
                            ⚡ EVIDENCE_ID: "AEV_" + INVOCATION_ID;
                            ⚡ EVIDENCE_GAP_ID: "AGAP_EVID_" + INVOCATION_ID;
                            ⚡ EVIDENCE_QUESTION_ID: "AQ_EVID_" + INVOCATION_ID;
                            ⚡ OBSERVATION: c5ac1_result_to_observation(ACADEMIC_TEXT_RESULT, ACADEMIC_SEED_CAPABILITY_REQUEST, OBS_ID, RECEIPT_ARTIFACT_SHA);
                            ⚡ CLAIM: c5ak1_observation_to_claim(OBSERVATION, CLAIM_ID, "1", "1");
                            ⚡ EVIDENCE: c5ak1_observation_to_evidence(OBSERVATION, ACADEMIC_SEED_PASSAGE, ACADEMIC_SEED_DOCUMENT, EVIDENCE_ID);
                            ⚡ COUNTS: c5as1_make_evidence_counts("0", "0", "0", "0");
                            ⚡ SYNTHESIS: c5as1_make_synthesis(CLAIM_ID, "UNRESOLVED", COUNTS, "1");
                            ⚡ RESOLVED_TEXT_GAP: c5t2_gap_with_state(ACADEMIC_SEED_GAP, "RESOLVED");
                            ⚡ EVIDENCE_GAP: c5t2_make_gap(EVIDENCE_GAP_ID, STATE_OBJECTIVE_ID, "EVIDENCE", STATE_PENDING_SUBJECT_ID, "EVIDENCE_SEARCH", "1");
                            ⚡ WORK2: c5as1_make_work(c5l2_field(ACADEMIC_SEED_WORK, 1, "WORK_ID"), "EVIDENCE_BUILDING", STATE_PENDING_SUBJECT_ID, STATE_OBJECTIVE_ID, "2");
                            ⚡ RESOLVED_TEXT_QUESTION: "TYPE=ACADEMIC_QUESTION || QUESTION_ID=" + c5l2_field(ACADEMIC_SEED_QUESTION, 1, "QUESTION_ID") + " || WORK_ID=" + c5l2_field(ACADEMIC_SEED_QUESTION, 2, "WORK_ID") + " || SUBJECT_ID=" + c5l2_field(ACADEMIC_SEED_QUESTION, 3, "SUBJECT_ID") + " || KIND=" + c5l2_field(ACADEMIC_SEED_QUESTION, 4, "KIND") + " || STATE=RESOLVED || NEED_FAMILY=" + c5l2_field(ACADEMIC_SEED_QUESTION, 6, "NEED_FAMILY") + " || PRIORITY=" + c5l2_field(ACADEMIC_SEED_QUESTION, 7, "PRIORITY");
                            ⚡ EVIDENCE_QUESTION: c5as1_make_question(EVIDENCE_QUESTION_ID, c5l2_field(WORK2, 1, "WORK_ID"), STATE_PENDING_SUBJECT_ID, "EVIDENCE", "EVIDENCE_SEARCH", "1");
                            ⚡ GAP_BANK: RESOLVED_TEXT_GAP + "\n" + EVIDENCE_GAP;
                            ⚡ QUESTION_BANK: RESOLVED_TEXT_QUESTION + "\n" + EVIDENCE_QUESTION;
                            ⚡ AGENDA: c5am1_pack_agenda(WORK2, ACADEMIC_SEED_OBJECTIVE, GAP_BANK, QUESTION_BANK);
                            ⚡ ASSESSMENT: c5ak1_pack_assessment(OBSERVATION, "", "", SYNTHESIS);
                            ⚡ MEMORY: c5am1_pack_memory(AGENDA, ACADEMIC_SEED_STRUCTURE, CLAIM, EVIDENCE, ASSESSMENT);
                            IF (c5as1_observation_valid(OBSERVATION) == 0) { ⚡ RESULT_OK: 0; }
                            IF (c5d1_claim_valid(CLAIM) == 0) { ⚡ RESULT_OK: 0; }
                            IF (c5l2_evidence_valid(EVIDENCE) == 0) { ⚡ RESULT_OK: 0; }
                            IF (c5as1_synthesis_valid(SYNTHESIS) == 0) { ⚡ RESULT_OK: 0; }
                            IF (c5l2_gap_valid(RESOLVED_TEXT_GAP) == 0) { ⚡ RESULT_OK: 0; }
                            IF (c5l2_gap_valid(EVIDENCE_GAP) == 0) { ⚡ RESULT_OK: 0; }
                            IF (c5as1_work_valid(WORK2) == 0) { ⚡ RESULT_OK: 0; }
                            IF (c5as1_question_valid(RESOLVED_TEXT_QUESTION) == 0) { ⚡ RESULT_OK: 0; }
                            IF (c5as1_question_valid(EVIDENCE_QUESTION) == 0) { ⚡ RESULT_OK: 0; }
                            IF (c5am1_agenda_valid(AGENDA) == 0) { ⚡ RESULT_OK: 0; }
                            IF (c5ak1_assessment_valid(ASSESSMENT) == 0) { ⚡ RESULT_OK: 0; }
                            IF (c5am1_memory_valid(MEMORY) == 0) { ⚡ RESULT_OK: 0; }
                            IF (RESULT_OK) {
                                ⚡ MEMORY_ACTION_ID: "AMEM_" + INVOCATION_ID;
                                IF (p0r4_stage_write_verify(BASE + "/out/academic_observation.txt", OBSERVATION) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/academic_observed_claim.txt", CLAIM) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/academic_evidence_ref.txt", EVIDENCE) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/academic_synthesis.txt", SYNTHESIS) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/academic_next_gap.txt", EVIDENCE_GAP) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/academic_next_question.txt", EVIDENCE_QUESTION) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/native_academic_memory.txt", MEMORY) == 0) { ⚡ STAGE_OK: 0; }
                                ⚡ NEXT_STATE: "STATE_VERSION=2\nPHASE=WAIT_MEMORY_BIND\nOBJECTIVE_ID=" + STATE_OBJECTIVE_ID + "\nACTIVE_GAP_ID=" + EVIDENCE_GAP_ID + "\nPENDING_ACTION_ID=" + MEMORY_ACTION_ID + "\nPENDING_REQUEST_ID=NONE\nPENDING_CAPABILITY_ID=NONE\nPENDING_SUBJECT_ID=" + STATE_PENDING_SUBJECT_ID + "\nPENDING_PAYLOAD_KIND=NATIVE_ACADEMIC_MEMORY\nPENDING_PAYLOAD_SHA=NONE\nEPISTEMIC_STATE_SHA=" + STATE_EPISTEMIC_STATE_SHA + "\nMEMORY_STATE_SHA=NONE\nLAST_RECEIPT_SHA=" + RECEIPT_SHA + "\nLAST_INVOCATION_ID=" + INVOCATION_ID + "\nLAST_ACTION_ID=" + MEMORY_ACTION_ID + "\nLAST_EVENT=CAPABILITY_RESULT_READY\nLAST_SOURCE_ID=" + c5l2_field(ACADEMIC_SEED_DOCUMENT, 2, "SOURCE_ID") + "\nLAST_SOURCE_VERSION_SHA=" + c5l2_field(ACADEMIC_SEED_DOCUMENT, 3, "SOURCE_VERSION_SHA") + "\nLAST_ARTIFACT_SHA=" + RECEIPT_ARTIFACT_SHA + "\nLAST_EVIDENCE_ID=" + EVIDENCE_ID;
                                ⚡ ACTION: "MATERIALIZE_NATIVE_ACADEMIC_MEMORY";
                                ⚡ STATUS: "R4_ACADEMIC_NATIVE_OBSERVATION_MEMORY_STAGED";
                                ⚡ NEXT_ACTION_ID: MEMORY_ACTION_ID;
                                ⚡ COMMIT_ALLOWED: 1;
                            }
                        }
                        IF (RESULT_OK == 0) { ⚡ STATUS: "R4_ACADEMIC_CAPABILITY_RESULT_REJECTED"; }
                    }
                    IF (EVENT_TYPE == "MEMORY_BOUND") {
                        ⚡ MEMORY_OK: 1;
                        IF (STATE_PHASE != "WAIT_MEMORY_BIND") { ⚡ MEMORY_OK: 0; }
                        IF (ACTION_ID != STATE_PENDING_ACTION_ID) { ⚡ MEMORY_OK: 0; }
                        IF (RECEIPT_SUBJECT_ID != STATE_PENDING_SUBJECT_ID) { ⚡ MEMORY_OK: 0; }
                        IF (p0r4_hex64(BOUND_MEMORY_SHA) == 0) { ⚡ MEMORY_OK: 0; }
                        IF (RECEIPT_ARTIFACT_SHA != BOUND_MEMORY_SHA) { ⚡ MEMORY_OK: 0; }
                        IF (c5am1_memory_valid(MEMORY_TEXT) == 0) { ⚡ MEMORY_OK: 0; }
                        IF (c5am1_recall_gap(MEMORY_TEXT, STATE_ACTIVE_GAP_ID) == "") { ⚡ MEMORY_OK: 0; }
                        IF (MEMORY_OK) {
                            ⚡ NEXT_STATE: "STATE_VERSION=2\nPHASE=IDLE\nOBJECTIVE_ID=" + STATE_OBJECTIVE_ID + "\nACTIVE_GAP_ID=" + STATE_ACTIVE_GAP_ID + "\nPENDING_ACTION_ID=NONE\nPENDING_REQUEST_ID=NONE\nPENDING_CAPABILITY_ID=NONE\nPENDING_SUBJECT_ID=NONE\nPENDING_PAYLOAD_KIND=NONE\nPENDING_PAYLOAD_SHA=NONE\nEPISTEMIC_STATE_SHA=NONE\nMEMORY_STATE_SHA=" + BOUND_MEMORY_SHA + "\nLAST_RECEIPT_SHA=" + RECEIPT_SHA + "\nLAST_INVOCATION_ID=" + INVOCATION_ID + "\nLAST_ACTION_ID=" + STATE_PENDING_ACTION_ID + "\nLAST_EVENT=MEMORY_BOUND\nLAST_SOURCE_ID=" + p0r4_state_value(PARENT_STATE_SNAPSHOT, 16, "LAST_SOURCE_ID") + "\nLAST_SOURCE_VERSION_SHA=" + p0r4_state_value(PARENT_STATE_SNAPSHOT, 17, "LAST_SOURCE_VERSION_SHA") + "\nLAST_ARTIFACT_SHA=" + BOUND_MEMORY_SHA + "\nLAST_EVIDENCE_ID=" + p0r4_state_value(PARENT_STATE_SNAPSHOT, 19, "LAST_EVIDENCE_ID");
                            ⚡ ACTION: "COMPLETE_ACADEMIC_MEMORY_COMMIT";
                            ⚡ STATUS: "R4_ACADEMIC_MEMORY_BOUND_AGENDA_RETAINED";
                            ⚡ NEXT_ACTION_ID: STATE_PENDING_ACTION_ID;
                            ⚡ COMMIT_ALLOWED: 1;
                        }
                        IF (MEMORY_OK == 0) { ⚡ STATUS: "R4_ACADEMIC_MEMORY_BIND_REJECTED"; }
                    }
                    IF (EVENT_TYPE == "RESTART_READY") {
                        ⚡ RESTART_OK: 1;
                        IF (STATE_PHASE != "IDLE") { ⚡ RESTART_OK: 0; }
                        IF (p0r4_hex64(STATE_MEMORY_STATE_SHA) == 0) { ⚡ RESTART_OK: 0; }
                        IF (RECEIPT_ARTIFACT_SHA != STATE_MEMORY_STATE_SHA) { ⚡ RESTART_OK: 0; }
                        IF (c5am1_memory_valid(MEMORY_TEXT) == 0) { ⚡ RESTART_OK: 0; }
                        IF (p0r4_safe_atom(RECALL_CLAIM_ID, 128) == 0) { ⚡ RESTART_OK: 0; }
                        IF (p0r4_safe_atom(RECALL_GAP_ID, 128) == 0) { ⚡ RESTART_OK: 0; }
                        IF (p0r4_safe_atom(RECALL_QUESTION_ID, 128) == 0) { ⚡ RESTART_OK: 0; }
                        IF (RESTART_OK) {
                            ⚡ RECALLED_CLAIM: c5am1_recall_claim(MEMORY_TEXT, RECALL_CLAIM_ID);
                            ⚡ RECALLED_SYNTHESIS: c5am1_recall_synthesis(MEMORY_TEXT, RECALL_CLAIM_ID);
                            ⚡ RECALLED_GAP: c5am1_recall_gap(MEMORY_TEXT, RECALL_GAP_ID);
                            ⚡ RECALLED_QUESTION: c5am1_recall_question(MEMORY_TEXT, RECALL_QUESTION_ID);
                            IF (RECALLED_CLAIM == "") { ⚡ RESTART_OK: 0; }
                            IF (RECALLED_SYNTHESIS == "") { ⚡ RESTART_OK: 0; }
                            IF (RECALLED_GAP == "") { ⚡ RESTART_OK: 0; }
                            IF (RECALLED_QUESTION == "") { ⚡ RESTART_OK: 0; }
                            IF (RESTART_OK) {
                                IF (p0r4_stage_write_verify(BASE + "/out/recalled_academic_claim.txt", RECALLED_CLAIM) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/recalled_academic_synthesis.txt", RECALLED_SYNTHESIS) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/recalled_academic_gap.txt", RECALLED_GAP) == 0) { ⚡ STAGE_OK: 0; }
                                IF (p0r4_stage_write_verify(BASE + "/out/recalled_academic_question.txt", RECALLED_QUESTION) == 0) { ⚡ STAGE_OK: 0; }
                                ⚡ NEXT_STATE: "STATE_VERSION=2\nPHASE=IDLE\nOBJECTIVE_ID=" + STATE_OBJECTIVE_ID + "\nACTIVE_GAP_ID=" + STATE_ACTIVE_GAP_ID + "\nPENDING_ACTION_ID=NONE\nPENDING_REQUEST_ID=NONE\nPENDING_CAPABILITY_ID=NONE\nPENDING_SUBJECT_ID=NONE\nPENDING_PAYLOAD_KIND=NONE\nPENDING_PAYLOAD_SHA=NONE\nEPISTEMIC_STATE_SHA=NONE\nMEMORY_STATE_SHA=" + STATE_MEMORY_STATE_SHA + "\nLAST_RECEIPT_SHA=" + RECEIPT_SHA + "\nLAST_INVOCATION_ID=" + INVOCATION_ID + "\nLAST_ACTION_ID=NONE\nLAST_EVENT=RESTART_READY\nLAST_SOURCE_ID=" + p0r4_state_value(PARENT_STATE_SNAPSHOT, 16, "LAST_SOURCE_ID") + "\nLAST_SOURCE_VERSION_SHA=" + p0r4_state_value(PARENT_STATE_SNAPSHOT, 17, "LAST_SOURCE_VERSION_SHA") + "\nLAST_ARTIFACT_SHA=" + STATE_MEMORY_STATE_SHA + "\nLAST_EVIDENCE_ID=" + p0r4_state_value(PARENT_STATE_SNAPSHOT, 19, "LAST_EVIDENCE_ID");
                                ⚡ ACTION: "RECALL_FROM_NATIVE_ACADEMIC_MEMORY";
                                ⚡ STATUS: "R4_ACADEMIC_RESTART_MEMORY_REUSE_PASS_PATH";
                                ⚡ COMMIT_ALLOWED: 1;
                            }
                        }
                        IF (RESTART_OK == 0) { ⚡ STATUS: "R4_ACADEMIC_RESTART_MEMORY_RECALL_REJECTED"; }
                    }
                    IF (EVENT_TYPE == "REQUEST_BOUND") {
                        ⚡ ACTION: "HOLD";
                        ⚡ STATUS: "R4_ACADEMIC_EXTERNAL_EVIDENCE_REQUEST_PATH_NOT_ACTIVATED";
                    }
                    IF (EVENT_TYPE == "EVIDENCE_READY") {
                        ⚡ ACTION: "HOLD";
                        ⚡ STATUS: "R4_ACADEMIC_EXTERNAL_EVIDENCE_EVALUATION_PATH_NOT_ACTIVATED";
                    }
                }
            }
        }
    }
    IF (p0r4_stage_write_verify(BASE + "/out/action.txt", ACTION) == 0) { ⚡ STAGE_OK: 0; }
    IF (p0r4_stage_write_verify(BASE + "/out/status.txt", STATUS) == 0) { ⚡ STAGE_OK: 0; }
    IF (COMMIT_ALLOWED) {
        IF (p0r4_state_snapshot_valid(NEXT_STATE) == 0) { ⚡ STAGE_OK: 0; }
        ⚡ EVENT_BINDING: "INVOCATION_ID=" + INVOCATION_ID + "\nEVENT_TYPE=" + EVENT_TYPE + "\nPHASE=" + EXPECTED_PHASE + "\nPARENT_STATE_SHA=" + PARENT_STATE_SHA + "\nRECEIPT_SHA=" + RECEIPT_SHA + "\nRECEIPT_ACTION_ID=" + RECEIPT_ACTION_ID + "\nNEXT_ACTION_ID=" + NEXT_ACTION_ID;
        IF (p0r4_stage_write_verify(BASE + "/out/stage_next_state.txt", NEXT_STATE) == 0) { ⚡ STAGE_OK: 0; }
        IF (p0r4_stage_write_verify(BASE + "/out/stage_event_binding.txt", EVENT_BINDING) == 0) { ⚡ STAGE_OK: 0; }
        IF (p0r4_stage_write_verify(BASE + "/out/commit_parent_state_sha.txt", PARENT_STATE_SHA) == 0) { ⚡ STAGE_OK: 0; }
        IF (p0r4_stage_write_verify(BASE + "/out/commit_receipt_sha.txt", RECEIPT_SHA) == 0) { ⚡ STAGE_OK: 0; }
        IF (STAGE_OK) { ⚡ FINAL_RC: p0r4_H("write_text", BASE + "/out/native_commit_intent.txt", "ALLOW_EXACT_STAGED_STATE", NULL); }
    }
    ⚡ print("SIGMA_C5_AUTONOMOUS_SELF_LEARNING_CORE_V1");
    ⚡ print("R4_ACADEMIC_TRANSACTION_MAIN", "ACTIVE_SOURCE_ONLY");
    ⚡ print("EVENT_TYPE", EVENT_TYPE);
    ⚡ print("ACTION", ACTION);
    ⚡ print("STATUS", STATUS);
    ⚡ print("COMMIT_ALLOWED", COMMIT_ALLOWED);
    ⚡ print("STAGE_OK", STAGE_OK);
}