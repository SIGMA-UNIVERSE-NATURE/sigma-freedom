# R3 FIX1 P0 trust/state substrate.
# Development module. Final composition keeps the historical C5 header/entry.
# Semantic authority remains native. Mechanical host may hash/copy/atomically commit,
# but may not create beliefs, goals, source choices, or capability choices.

DEF p0_present(value) {
    IF (value == "") { RETURN 0; }
    IF (value == "NONE") { RETURN 0; }
    RETURN 1;
}

DEF p0_digits_only(value) {
    IF (value == "") { RETURN 0; }
    ⚡ REST: value;
    ⚡ REST: H("str_replace", REST, "0", "");
    ⚡ REST: H("str_replace", REST, "1", "");
    ⚡ REST: H("str_replace", REST, "2", "");
    ⚡ REST: H("str_replace", REST, "3", "");
    ⚡ REST: H("str_replace", REST, "4", "");
    ⚡ REST: H("str_replace", REST, "5", "");
    ⚡ REST: H("str_replace", REST, "6", "");
    ⚡ REST: H("str_replace", REST, "7", "");
    ⚡ REST: H("str_replace", REST, "8", "");
    ⚡ REST: H("str_replace", REST, "9", "");
    IF (REST == "") { RETURN 1; }
    RETURN 0;
}

DEF p0_hex64(value) {
    IF (H("str_len", value, NULL, NULL) != 64) { RETURN 0; }
    ⚡ REST: H("str_lower", value, NULL, NULL);
    ⚡ REST: H("str_replace", REST, "0", "");
    ⚡ REST: H("str_replace", REST, "1", "");
    ⚡ REST: H("str_replace", REST, "2", "");
    ⚡ REST: H("str_replace", REST, "3", "");
    ⚡ REST: H("str_replace", REST, "4", "");
    ⚡ REST: H("str_replace", REST, "5", "");
    ⚡ REST: H("str_replace", REST, "6", "");
    ⚡ REST: H("str_replace", REST, "7", "");
    ⚡ REST: H("str_replace", REST, "8", "");
    ⚡ REST: H("str_replace", REST, "9", "");
    ⚡ REST: H("str_replace", REST, "a", "");
    ⚡ REST: H("str_replace", REST, "b", "");
    ⚡ REST: H("str_replace", REST, "c", "");
    ⚡ REST: H("str_replace", REST, "d", "");
    ⚡ REST: H("str_replace", REST, "e", "");
    ⚡ REST: H("str_replace", REST, "f", "");
    IF (REST == "") { RETURN 1; }
    RETURN 0;
}

DEF p0_safe_atom(value, max_len) {
    IF (value == "") { RETURN 0; }
    ⚡ N: H("str_len", value, NULL, NULL);
    IF (max_len < N) { RETURN 0; }

    ⚡ X: H("str_replace", value, "\n", "");
    IF (X != value) { RETURN 0; }
    ⚡ X: H("str_replace", value, "\r", "");
    IF (X != value) { RETURN 0; }
    ⚡ X: H("str_replace", value, "\t", "");
    IF (X != value) { RETURN 0; }
    ⚡ X: H("str_replace", value, "=", "");
    IF (X != value) { RETURN 0; }
    ⚡ X: H("str_replace", value, " || ", "");
    IF (X != value) { RETURN 0; }
    RETURN 1;
}

DEF p0_none_or_atom(value, max_len) {
    IF (value == "NONE") { RETURN 1; }
    RETURN p0_safe_atom(value, max_len);
}

DEF p0_none_or_hex64(value) {
    IF (value == "NONE") { RETURN 1; }
    RETURN p0_hex64(value);
}

DEF p0_none_or_digits(value) {
    IF (value == "NONE") { RETURN 1; }
    RETURN p0_digits_only(value);
}

DEF p0_exact_field(line, key) {
    ⚡ PARTS: H("str_split", line, "=", NULL);
    ⚡ N: H("list_len", PARTS, NULL, NULL);
    IF (N != 2) { RETURN ""; }
    ⚡ K: H("list_get", PARTS, 0, NULL);
    IF (K != key) { RETURN ""; }
    RETURN H("list_get", PARTS, 1, NULL);
}

DEF p0_state_value(snapshot, index, key) {
    ⚡ LINES: H("str_split", snapshot, "\n", NULL);
    ⚡ N: H("list_len", LINES, NULL, NULL);
    IF (N != 20) { RETURN ""; }
    ⚡ LINE: H("list_get", LINES, index, NULL);
    RETURN p0_exact_field(LINE, key);
}

DEF p0_phase_valid(value) {
    IF (value == "GENESIS") { RETURN 1; }
    IF (value == "IDLE") { RETURN 1; }
    IF (value == "COGNITION_READY") { RETURN 1; }
    IF (value == "WAIT_SEGMENT") { RETURN 1; }
    IF (value == "WAIT_FETCH") { RETURN 1; }
    IF (value == "WAIT_EVIDENCE") { RETURN 1; }
    IF (value == "WAIT_CAPABILITY") { RETURN 1; }
    IF (value == "STAGED_COMMIT") { RETURN 1; }
    RETURN 0;
}

DEF p0_event_valid(value) {
    IF (value == "BOOTSTRAP") { RETURN 1; }
    IF (value == "TICK") { RETURN 1; }
    IF (value == "COGNITION_INPUT_READY") { RETURN 1; }
    IF (value == "SEGMENT_READY") { RETURN 1; }
    IF (value == "FETCH_READY") { RETURN 1; }
    IF (value == "EVIDENCE_LOOKUP_READY") { RETURN 1; }
    IF (value == "CAPABILITY_RESULT_READY") { RETURN 1; }
    RETURN 0;
}

DEF p0_receipt_kind_valid(value) {
    IF (value == "GENESIS") { RETURN 1; }
    IF (value == "TICK") { RETURN 1; }
    IF (value == "COGNITION_INPUT") { RETURN 1; }
    IF (value == "SEGMENT") { RETURN 1; }
    IF (value == "FETCH") { RETURN 1; }
    IF (value == "EVIDENCE_LOOKUP") { RETURN 1; }
    IF (value == "CAPABILITY_RESULT") { RETURN 1; }
    RETURN 0;
}

DEF p0_state_snapshot_valid(snapshot) {
    ⚡ N: H("str_len", snapshot, NULL, NULL);
    IF (4096 < N) { RETURN 0; }

    ⚡ VERSION: p0_state_value(snapshot, 0, "STATE_VERSION");
    ⚡ PHASE: p0_state_value(snapshot, 1, "PHASE");
    ⚡ OBJECTIVE_ID: p0_state_value(snapshot, 2, "OBJECTIVE_ID");
    ⚡ PENDING_ACTION_ID: p0_state_value(snapshot, 3, "PENDING_ACTION_ID");
    ⚡ PENDING_REQUEST_ID: p0_state_value(snapshot, 4, "PENDING_REQUEST_ID");
    ⚡ PENDING_CAPABILITY_ID: p0_state_value(snapshot, 5, "PENDING_CAPABILITY_ID");
    ⚡ PENDING_CANDIDATE_SET_SHA: p0_state_value(snapshot, 6, "PENDING_CANDIDATE_SET_SHA");
    ⚡ PENDING_CANDIDATE_COUNT: p0_state_value(snapshot, 7, "PENDING_CANDIDATE_COUNT");
    ⚡ PENDING_ENTRY_ID: p0_state_value(snapshot, 8, "PENDING_ENTRY_ID");
    ⚡ PENDING_SOURCE_ID: p0_state_value(snapshot, 9, "PENDING_SOURCE_ID");
    ⚡ PENDING_SOURCE_VERSION_SHA: p0_state_value(snapshot, 10, "PENDING_SOURCE_VERSION_SHA");
    ⚡ PENDING_OFFSET: p0_state_value(snapshot, 11, "PENDING_OFFSET");
    ⚡ PENDING_PAYLOAD_KIND: p0_state_value(snapshot, 12, "PENDING_PAYLOAD_KIND");
    ⚡ PENDING_PAYLOAD_SHA: p0_state_value(snapshot, 13, "PENDING_PAYLOAD_SHA");
    ⚡ EPISTEMIC_STATE_SHA: p0_state_value(snapshot, 14, "EPISTEMIC_STATE_SHA");
    ⚡ MEMORY_STATE_SHA: p0_state_value(snapshot, 15, "MEMORY_STATE_SHA");
    ⚡ LAST_RECEIPT_SHA: p0_state_value(snapshot, 16, "LAST_RECEIPT_SHA");
    ⚡ LAST_INVOCATION_ID: p0_state_value(snapshot, 17, "LAST_INVOCATION_ID");
    ⚡ LAST_ACTION_ID: p0_state_value(snapshot, 18, "LAST_ACTION_ID");
    ⚡ LAST_EVENT: p0_state_value(snapshot, 19, "LAST_EVENT");

    IF (VERSION != "1") { RETURN 0; }
    IF (p0_phase_valid(PHASE) == 0) { RETURN 0; }
    IF (p0_none_or_atom(OBJECTIVE_ID, 128) == 0) { RETURN 0; }
    IF (p0_none_or_atom(PENDING_ACTION_ID, 128) == 0) { RETURN 0; }
    IF (p0_none_or_atom(PENDING_REQUEST_ID, 128) == 0) { RETURN 0; }
    IF (p0_none_or_atom(PENDING_CAPABILITY_ID, 128) == 0) { RETURN 0; }
    IF (p0_none_or_hex64(PENDING_CANDIDATE_SET_SHA) == 0) { RETURN 0; }
    IF (p0_none_or_digits(PENDING_CANDIDATE_COUNT) == 0) { RETURN 0; }
    IF (p0_none_or_atom(PENDING_ENTRY_ID, 128) == 0) { RETURN 0; }
    IF (p0_none_or_atom(PENDING_SOURCE_ID, 128) == 0) { RETURN 0; }
    IF (p0_none_or_hex64(PENDING_SOURCE_VERSION_SHA) == 0) { RETURN 0; }
    IF (p0_none_or_digits(PENDING_OFFSET) == 0) { RETURN 0; }
    IF (p0_none_or_atom(PENDING_PAYLOAD_KIND, 64) == 0) { RETURN 0; }
    IF (p0_none_or_hex64(PENDING_PAYLOAD_SHA) == 0) { RETURN 0; }
    IF (p0_none_or_hex64(EPISTEMIC_STATE_SHA) == 0) { RETURN 0; }
    IF (p0_none_or_hex64(MEMORY_STATE_SHA) == 0) { RETURN 0; }
    IF (p0_none_or_hex64(LAST_RECEIPT_SHA) == 0) { RETURN 0; }
    IF (p0_none_or_atom(LAST_INVOCATION_ID, 128) == 0) { RETURN 0; }
    IF (p0_none_or_atom(LAST_ACTION_ID, 128) == 0) { RETURN 0; }
    IF (LAST_EVENT != "NONE") {
        IF (p0_event_valid(LAST_EVENT) == 0) { RETURN 0; }
    }

    RETURN 1;
}

DEF p0_receipt_envelope_shape_valid(
    invocation_id,
    event_type,
    expected_phase,
    parent_state_sha,
    action_id,
    receipt_kind
) {
    IF (p0_safe_atom(invocation_id, 128) == 0) { RETURN 0; }
    IF (p0_event_valid(event_type) == 0) { RETURN 0; }
    IF (p0_phase_valid(expected_phase) == 0) { RETURN 0; }
    IF (p0_hex64(parent_state_sha) == 0) { RETURN 0; }
    IF (p0_none_or_atom(action_id, 128) == 0) { RETURN 0; }
    IF (p0_receipt_kind_valid(receipt_kind) == 0) { RETURN 0; }
    RETURN 1;
}

DEF p0_stage_write_verify(path, value) {
    ⚡ RC: H("write_text", path, value, NULL);
    ⚡ BACK: H("read_text", path, NULL, NULL);
    IF (BACK != value) { RETURN 0; }
    RETURN 1;
}

DEF p0_event_receipt_kind_matches(event_type, receipt_kind) {
    IF (event_type == "BOOTSTRAP") {
        IF (receipt_kind == "GENESIS") { RETURN 1; }
        RETURN 0;
    }
    IF (event_type == "TICK") {
        IF (receipt_kind == "TICK") { RETURN 1; }
        RETURN 0;
    }
    IF (event_type == "COGNITION_INPUT_READY") {
        IF (receipt_kind == "COGNITION_INPUT") { RETURN 1; }
        RETURN 0;
    }
    IF (event_type == "SEGMENT_READY") {
        IF (receipt_kind == "SEGMENT") { RETURN 1; }
        RETURN 0;
    }
    IF (event_type == "FETCH_READY") {
        IF (receipt_kind == "FETCH") { RETURN 1; }
        RETURN 0;
    }
    IF (event_type == "EVIDENCE_LOOKUP_READY") {
        IF (receipt_kind == "EVIDENCE_LOOKUP") { RETURN 1; }
        RETURN 0;
    }
    IF (event_type == "CAPABILITY_RESULT_READY") {
        IF (receipt_kind == "CAPABILITY_RESULT") { RETURN 1; }
        RETURN 0;
    }
    RETURN 0;
}

DEF p0_zero_state() {
    RETURN
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
        + "LAST_RECEIPT_SHA=NONE\n"
        + "LAST_INVOCATION_ID=NONE\n"
        + "LAST_ACTION_ID=NONE\n"
        + "LAST_EVENT=NONE";
}
