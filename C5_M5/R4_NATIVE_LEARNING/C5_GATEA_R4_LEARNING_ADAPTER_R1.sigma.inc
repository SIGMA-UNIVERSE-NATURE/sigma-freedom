# C5V3 Gate-A -> R4 native learning adapter R1.
# Narrow adapter only. Depends on:
# - exact Gate-A pure cognition DEFs from bf468c... (append_line excluded)
# - C5_NATIVE_LEARNING_STATE_R1.sigma.inc
# - C5_NATIVE_LEARNING_TRANSITIONS_R1.sigma.inc
# No direct I/O. No host semantic authority. No broad truth claim.

DEF c5a_relation_gap_signal(ledger, candidate_a, candidate_b) {
    RETURN relation_discrimination_gap_signal(ledger, candidate_a, candidate_b);
}

DEF c5a_relation_request_payload(ledger, candidate_a, candidate_b) {
    IF (relation_discrimination_gap_signal(ledger, candidate_a, candidate_b) == 0) { RETURN ""; }
    RETURN build_native_gap_evidence_request(candidate_a, candidate_b);
}

DEF c5a_revision_source_stance(neutral_ledger, revision_ledger, candidate_a, candidate_b, source_id) {
    RETURN revision_source_stance(neutral_ledger, revision_ledger, candidate_a, candidate_b, source_id);
}

DEF c5a_revision_authority_count(neutral_ledger, revision_ledger, candidate_a, candidate_b, target_side) {
    IF (target_side != "A") {
        IF (target_side != "B") { RETURN 0; }
    }
    RETURN revision_consistent_distinct_source_count(neutral_ledger, revision_ledger, candidate_a, candidate_b, target_side);
}

DEF c5a_revision_truth_state(neutral_ledger, revision_ledger, candidate_a, candidate_b) {
    ⚡ A: revision_consistent_distinct_source_count(neutral_ledger, revision_ledger, candidate_a, candidate_b, "A");
    ⚡ B: revision_consistent_distinct_source_count(neutral_ledger, revision_ledger, candidate_a, candidate_b, "B");
    RETURN derive_scoped_provisional_truth_state(A, B);
}

DEF c5a_revision_incompatibility_state(neutral_ledger, revision_ledger, candidate_a, candidate_b) {
    ⚡ A: revision_consistent_distinct_source_count(neutral_ledger, revision_ledger, candidate_a, candidate_b, "A");
    ⚡ B: revision_consistent_distinct_source_count(neutral_ledger, revision_ledger, candidate_a, candidate_b, "B");
    RETURN derive_scoped_competing_incompatibility_state(A, B);
}

DEF c5a_revision_source_consistency(neutral_ledger, revision_ledger, candidate_a, candidate_b) {
    RETURN build_revision_source_consistency_state(neutral_ledger, revision_ledger, candidate_a, candidate_b);
}

DEF c5a_revision_snapshot(work_id, neutral_ledger, revision_ledger, candidate_a, candidate_b) {
    ⚡ A: revision_consistent_distinct_source_count(neutral_ledger, revision_ledger, candidate_a, candidate_b, "A");
    ⚡ B: revision_consistent_distinct_source_count(neutral_ledger, revision_ledger, candidate_a, candidate_b, "B");
    ⚡ TRUTH: derive_scoped_provisional_truth_state(A, B);
    ⚡ CONFLICT: derive_scoped_competing_incompatibility_state(A, B);
    ⚡ CONSISTENCY: build_revision_source_consistency_state(neutral_ledger, revision_ledger, candidate_a, candidate_b);
    RETURN "TYPE=GATEA_RELATION_REVISION_POSTURE || WORK_ID=" + work_id + " || TRUTH_STATE=" + TRUTH + " || INCOMPATIBILITY_STATE=" + CONFLICT + " || AUTHORITY_A=" + A + " || AUTHORITY_B=" + B + "\nSOURCE_CONSISTENCY_BEGIN\n" + CONSISTENCY + "\nSOURCE_CONSISTENCY_END";
}

DEF c5a_evaluation_stance_for_claim(source_stance, claim_side) {
    IF (claim_side != "A") {
        IF (claim_side != "B") { RETURN "NEUTRAL"; }
    }
    IF (source_stance == claim_side) { RETURN "SUPPORT"; }
    RETURN "NEUTRAL";
}

DEF c5a_conflict_gap_signal(truth_state) {
    IF (truth_state == "CONTESTED") { RETURN 1; }
    RETURN 0;
}

DEF c5a_provisional_side(truth_state) {
    IF (truth_state == "PROVISIONAL_A") { RETURN "A"; }
    IF (truth_state == "PROVISIONAL_B") { RETURN "B"; }
    RETURN "NONE";
}

DEF c5a_seed_epistemic_class(truth_state, claim_side) {
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
