# C5V3 native learning transition helpers R2.
# Depends on C5_NATIVE_LEARNING_STATE_R2.sigma.inc.
# Pure construction/transition helpers. Exact schemas. No direct I/O.

DEF c5t2_objective_state_valid(value) {
    IF (value == "OPEN") { RETURN 1; }
    IF (value == "SATISFIED") { RETURN 1; }
    IF (value == "HELD") { RETURN 1; }
    RETURN 0;
}

DEF c5t2_objective_valid(record) {
    IF (H("str_len", record, NULL, NULL) > 1024) { RETURN 0; }
    IF (c5l2_record_part_count(record) != 5) { RETURN 0; }
    ⚡ TYPE: c5l2_field(record, 0, "TYPE");
    ⚡ OBJECTIVE_ID: c5l2_field(record, 1, "OBJECTIVE_ID");
    ⚡ STATE: c5l2_field(record, 2, "STATE");
    ⚡ SUBJECT_ID: c5l2_field(record, 3, "SUBJECT_ID");
    ⚡ REVISION: c5l2_field(record, 4, "REVISION");
    IF (TYPE != "OBJECTIVE") { RETURN 0; }
    IF (c5l2_safe_atom(OBJECTIVE_ID, 128) == 0) { RETURN 0; }
    IF (c5t2_objective_state_valid(STATE) == 0) { RETURN 0; }
    IF (c5l2_safe_atom(SUBJECT_ID, 128) == 0) { RETURN 0; }
    IF (c5l2_digits_only(REVISION) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5t2_make_objective(objective_id, state, subject_id, revision) {
    IF (c5l2_safe_atom(objective_id, 128) == 0) { RETURN ""; }
    IF (c5t2_objective_state_valid(state) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(subject_id, 128) == 0) { RETURN ""; }
    IF (c5l2_digits_only(revision) == 0) { RETURN ""; }
    RETURN "TYPE=OBJECTIVE || OBJECTIVE_ID=" + objective_id + " || STATE=" + state + " || SUBJECT_ID=" + subject_id + " || REVISION=" + revision;
}

DEF c5t2_make_claim(claim_id, subject_id, class_name, revision, uncertainty) {
    IF (c5l2_safe_atom(claim_id, 128) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(subject_id, 128) == 0) { RETURN ""; }
    IF (c5l2_epistemic_class_valid(class_name) == 0) { RETURN ""; }
    IF (c5l2_digits_only(revision) == 0) { RETURN ""; }
    IF (c5l2_digits_only(uncertainty) == 0) { RETURN ""; }
    RETURN "TYPE=CLAIM || CLAIM_ID=" + claim_id + " || SUBJECT_ID=" + subject_id + " || CLASS=" + class_name + " || REVISION=" + revision + " || UNCERTAINTY=" + uncertainty;
}

DEF c5t2_make_gap(gap_id, objective_id, kind, subject_id, need_family, priority) {
    IF (c5l2_safe_atom(gap_id, 128) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(objective_id, 128) == 0) { RETURN ""; }
    IF (c5l2_gap_kind_valid(kind) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(subject_id, 128) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(need_family, 64) == 0) { RETURN ""; }
    IF (c5l2_digits_only(priority) == 0) { RETURN ""; }
    RETURN "TYPE=GAP || GAP_ID=" + gap_id + " || OBJECTIVE_ID=" + objective_id + " || KIND=" + kind + " || SUBJECT_ID=" + subject_id + " || STATE=OPEN || NEED_FAMILY=" + need_family + " || PRIORITY=" + priority;
}

DEF c5t2_gap_with_state(gap, new_state) {
    IF (c5l2_gap_valid(gap) == 0) { RETURN ""; }
    IF (new_state != "OPEN") {
        IF (new_state != "RESOLVED") {
            IF (new_state != "HELD") { RETURN ""; }
        }
    }
    ⚡ GAP_ID: c5l2_field(gap, 1, "GAP_ID");
    ⚡ OBJECTIVE_ID: c5l2_field(gap, 2, "OBJECTIVE_ID");
    ⚡ KIND: c5l2_field(gap, 3, "KIND");
    ⚡ SUBJECT_ID: c5l2_field(gap, 4, "SUBJECT_ID");
    ⚡ NEED_FAMILY: c5l2_field(gap, 6, "NEED_FAMILY");
    ⚡ PRIORITY: c5l2_field(gap, 7, "PRIORITY");
    RETURN "TYPE=GAP || GAP_ID=" + GAP_ID + " || OBJECTIVE_ID=" + OBJECTIVE_ID + " || KIND=" + KIND + " || SUBJECT_ID=" + SUBJECT_ID + " || STATE=" + new_state + " || NEED_FAMILY=" + NEED_FAMILY + " || PRIORITY=" + PRIORITY;
}

DEF c5t2_make_evidence(evidence_id, source_id, source_version_sha, artifact_sha, subject_id) {
    IF (c5l2_safe_atom(evidence_id, 128) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(source_id, 128) == 0) { RETURN ""; }
    IF (c5l2_hex64(source_version_sha) == 0) { RETURN ""; }
    IF (c5l2_hex64(artifact_sha) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(subject_id, 128) == 0) { RETURN ""; }
    RETURN "TYPE=EVIDENCE || EVIDENCE_ID=" + evidence_id + " || SOURCE_ID=" + source_id + " || SOURCE_VERSION_SHA=" + source_version_sha + " || ARTIFACT_SHA=" + artifact_sha + " || SUBJECT_ID=" + subject_id;
}

DEF c5t2_make_evaluation(eval_id, claim_id, evidence_id, source_id, stance, basis_sha) {
    IF (c5l2_safe_atom(eval_id, 128) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(claim_id, 128) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(evidence_id, 128) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(source_id, 128) == 0) { RETURN ""; }
    IF (c5l2_stance_valid(stance) == 0) { RETURN ""; }
    IF (c5l2_hex64(basis_sha) == 0) { RETURN ""; }
    RETURN "TYPE=EVALUATION || EVAL_ID=" + eval_id + " || CLAIM_ID=" + claim_id + " || EVIDENCE_ID=" + evidence_id + " || SOURCE_ID=" + source_id + " || STANCE=" + stance + " || BASIS_SHA=" + basis_sha;
}

DEF c5t2_make_request(request_id, gap, payload_sha) {
    IF (c5l2_safe_atom(request_id, 128) == 0) { RETURN ""; }
    IF (c5l2_gap_valid(gap) == 0) { RETURN ""; }
    IF (c5l2_hex64(payload_sha) == 0) { RETURN ""; }
    ⚡ GAP_ID: c5l2_field(gap, 1, "GAP_ID");
    ⚡ STATE: c5l2_field(gap, 5, "STATE");
    ⚡ NEED_FAMILY: c5l2_field(gap, 6, "NEED_FAMILY");
    IF (STATE != "OPEN") { RETURN ""; }
    RETURN "TYPE=REQUEST || REQUEST_ID=" + request_id + " || GAP_ID=" + GAP_ID + " || NEED_FAMILY=" + NEED_FAMILY + " || PAYLOAD_SHA=" + payload_sha;
}

DEF c5t2_memory_section(memory, begin_marker, end_marker) {
    IF (memory == "") { RETURN ""; }
    IF (65536 < H("str_len", memory, NULL, NULL)) { RETURN ""; }
    ⚡ A: H("str_split", memory, begin_marker, NULL);
    ⚡ AN: H("list_len", A, NULL, NULL);
    IF (AN != 2) { RETURN ""; }
    ⚡ AFTER: H("list_get", A, 1, NULL);
    ⚡ B: H("str_split", AFTER, end_marker, NULL);
    ⚡ BN: H("list_len", B, NULL, NULL);
    IF (BN != 2) { RETURN ""; }
    RETURN H("list_get", B, 0, NULL);
}

DEF c5t2_memory_recall_claim(memory, claim_id) {
    ⚡ CLAIMS: c5t2_memory_section(memory, "CLAIMS_BEGIN\n", "\nCLAIMS_END");
    IF (CLAIMS == "") { RETURN ""; }
    ⚡ CLAIM: c5l2_bank_find_at(CLAIMS, 1, "CLAIM_ID", claim_id);
    IF (CLAIM == "") { RETURN ""; }
    IF (c5l2_claim_valid(CLAIM) == 0) { RETURN ""; }
    RETURN CLAIM;
}

DEF c5t2_memory_recall_gap(memory, gap_id) {
    ⚡ GAPS: c5t2_memory_section(memory, "GAPS_BEGIN\n", "\nGAPS_END");
    IF (GAPS == "") { RETURN ""; }
    ⚡ GAP: c5l2_bank_find_at(GAPS, 1, "GAP_ID", gap_id);
    IF (GAP == "") { RETURN ""; }
    IF (c5l2_gap_valid(GAP) == 0) { RETURN ""; }
    RETURN GAP;
}
