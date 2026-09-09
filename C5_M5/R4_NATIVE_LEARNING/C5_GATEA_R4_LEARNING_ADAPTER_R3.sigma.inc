# C5V3 Gate-A -> R4 native learning adapter R3.
# Supersedes adapter R2 before runtime admission.
# Narrow adapter only. Exact Gate-A source semantics remain authoritative in tested scope.
# No direct I/O. No host semantic authority. No broad truth claim.

DEF c5a3_relation_gap_signal(ledger, candidate_a, candidate_b) {
    RETURN relation_discrimination_gap_signal(ledger, candidate_a, candidate_b);
}

DEF c5a3_relation_request_payload(ledger, candidate_a, candidate_b) {
    IF (relation_discrimination_gap_signal(ledger, candidate_a, candidate_b) == 0) { RETURN ""; }
    RETURN build_native_gap_evidence_request(candidate_a, candidate_b);
}

DEF c5a3_revision_source_stance(neutral_ledger, revision_ledger, candidate_a, candidate_b, source_id) {
    RETURN revision_source_stance(neutral_ledger, revision_ledger, candidate_a, candidate_b, source_id);
}

DEF c5a3_revision_authority_count(neutral_ledger, revision_ledger, candidate_a, candidate_b, target_side) {
    IF (target_side != "A") {
        IF (target_side != "B") { RETURN 0; }
    }
    RETURN revision_consistent_distinct_source_count(neutral_ledger, revision_ledger, candidate_a, candidate_b, target_side);
}

DEF c5a3_revision_truth_state(neutral_ledger, revision_ledger, candidate_a, candidate_b) {
    ⚡ A: revision_consistent_distinct_source_count(neutral_ledger, revision_ledger, candidate_a, candidate_b, "A");
    ⚡ B: revision_consistent_distinct_source_count(neutral_ledger, revision_ledger, candidate_a, candidate_b, "B");
    RETURN derive_scoped_provisional_truth_state(A, B);
}

DEF c5a3_revision_incompatibility_state(neutral_ledger, revision_ledger, candidate_a, candidate_b) {
    ⚡ A: revision_consistent_distinct_source_count(neutral_ledger, revision_ledger, candidate_a, candidate_b, "A");
    ⚡ B: revision_consistent_distinct_source_count(neutral_ledger, revision_ledger, candidate_a, candidate_b, "B");
    RETURN derive_scoped_competing_incompatibility_state(A, B);
}

DEF c5a3_revision_source_consistency(neutral_ledger, revision_ledger, candidate_a, candidate_b) {
    RETURN build_revision_source_consistency_state(neutral_ledger, revision_ledger, candidate_a, candidate_b);
}

DEF c5a3_source_stance_valid(value) {
    IF (value == "A") { RETURN 1; }
    IF (value == "B") { RETURN 1; }
    IF (value == "INCONSISTENT") { RETURN 1; }
    IF (value == "NONE") { RETURN 1; }
    RETURN 0;
}

DEF c5a3_make_source_stance_record(neutral_ledger, revision_ledger, candidate_a, candidate_b, source_id) {
    IF (c5l2_safe_atom(source_id, 128) == 0) { RETURN ""; }
    ⚡ STANCE: revision_source_stance(neutral_ledger, revision_ledger, candidate_a, candidate_b, source_id);
    IF (c5a3_source_stance_valid(STANCE) == 0) { RETURN ""; }
    RETURN "TYPE=GATEA_SOURCE_STANCE || SOURCE_ID=" + source_id + " || STANCE=" + STANCE;
}

DEF c5a3_source_stance_record_valid(record) {
    IF (H("str_len", record, NULL, NULL) > 512) { RETURN 0; }
    IF (c5l2_record_part_count(record) != 3) { RETURN 0; }
    ⚡ TYPE: c5l2_field(record, 0, "TYPE");
    ⚡ SOURCE_ID: c5l2_field(record, 1, "SOURCE_ID");
    ⚡ STANCE: c5l2_field(record, 2, "STANCE");
    IF (TYPE != "GATEA_SOURCE_STANCE") { RETURN 0; }
    IF (c5l2_safe_atom(SOURCE_ID, 128) == 0) { RETURN 0; }
    IF (c5a3_source_stance_valid(STANCE) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5a3_make_truth_posture(neutral_ledger, revision_ledger, candidate_a, candidate_b) {
    ⚡ A: revision_consistent_distinct_source_count(neutral_ledger, revision_ledger, candidate_a, candidate_b, "A");
    ⚡ B: revision_consistent_distinct_source_count(neutral_ledger, revision_ledger, candidate_a, candidate_b, "B");
    ⚡ TRUTH: derive_scoped_provisional_truth_state(A, B);
    ⚡ CONFLICT: derive_scoped_competing_incompatibility_state(A, B);
    RETURN "TYPE=GATEA_TRUTH_POSTURE || TRUTH_STATE=" + TRUTH + " || INCOMPATIBILITY_STATE=" + CONFLICT + " || AUTHORITY_A=" + A + " || AUTHORITY_B=" + B;
}

DEF c5a3_truth_posture_valid(record) {
    IF (H("str_len", record, NULL, NULL) > 1024) { RETURN 0; }
    IF (c5l2_record_part_count(record) != 5) { RETURN 0; }
    ⚡ TYPE: c5l2_field(record, 0, "TYPE");
    ⚡ TRUTH: c5l2_field(record, 1, "TRUTH_STATE");
    ⚡ CONFLICT: c5l2_field(record, 2, "INCOMPATIBILITY_STATE");
    ⚡ A: c5l2_field(record, 3, "AUTHORITY_A");
    ⚡ B: c5l2_field(record, 4, "AUTHORITY_B");
    IF (TYPE != "GATEA_TRUTH_POSTURE") { RETURN 0; }
    IF (c5l2_digits_only(A) == 0) { RETURN 0; }
    IF (c5l2_digits_only(B) == 0) { RETURN 0; }
    IF (TRUTH != "UNRESOLVED") {
        IF (TRUTH != "PROVISIONAL_A") {
            IF (TRUTH != "PROVISIONAL_B") {
                IF (TRUTH != "CONTESTED") { RETURN 0; }
            }
        }
    }
    IF (c5l2_safe_atom(CONFLICT, 128) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5a3_evaluation_stance_for_claim(source_stance, claim_side) {
    IF (claim_side != "A") {
        IF (claim_side != "B") { RETURN "NEUTRAL"; }
    }
    IF (source_stance == claim_side) { RETURN "SUPPORT"; }
    IF (source_stance == "A") { RETURN "CONTRARY"; }
    IF (source_stance == "B") { RETURN "CONTRARY"; }
    RETURN "NEUTRAL";
}

DEF c5a3_conflict_gap_signal(truth_state) {
    IF (truth_state == "CONTESTED") { RETURN 1; }
    RETURN 0;
}

DEF c5a3_provisional_side(truth_state) {
    IF (truth_state == "PROVISIONAL_A") { RETURN "A"; }
    IF (truth_state == "PROVISIONAL_B") { RETURN "B"; }
    RETURN "NONE";
}

DEF c5a3_seed_epistemic_class(truth_state, claim_side) {
    IF (claim_side != "A") {
        IF (claim_side != "B") { RETURN "UNRESOLVED"; }
    }
    IF (truth_state == "PROVISIONAL_A") {
        IF (claim_side == "A") { RETURN "HYPOTHESIS"; }
        RETURN "UNRESOLVED";
    }
    IF (truth_state == "PROVISIONAL_B") {
        IF (claim_side == "B") { RETURN "HYPOTHESIS"; }
        RETURN "UNRESOLVED";
    }
    IF (truth_state == "CONTESTED") { RETURN "HYPOTHESIS"; }
    RETURN "UNRESOLVED";
}
