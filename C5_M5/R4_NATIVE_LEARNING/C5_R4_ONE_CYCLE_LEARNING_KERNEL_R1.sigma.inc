# C5V3 R4 one-cycle native learning kernel R1.
# Depends on R4 R2 state/transitions + Gate-A R2 adapter + exact Gate-A pure cognition DEFs.
# Pure learning transitions only. No direct I/O, transport, persistence, host semantic selection, or capability choice.

DEF c5c2_relation_seed_valid(objective, gap, claim_a, claim_b) {
    IF (c5t2_objective_valid(objective) == 0) { RETURN 0; }
    IF (c5l2_gap_valid(gap) == 0) { RETURN 0; }
    IF (c5l2_claim_valid(claim_a) == 0) { RETURN 0; }
    IF (c5l2_claim_valid(claim_b) == 0) { RETURN 0; }
    ⚡ OID: c5l2_field(objective, 1, "OBJECTIVE_ID");
    ⚡ OSUB: c5l2_field(objective, 3, "SUBJECT_ID");
    ⚡ GOID: c5l2_field(gap, 2, "OBJECTIVE_ID");
    ⚡ GSUB: c5l2_field(gap, 4, "SUBJECT_ID");
    ⚡ ASUB: c5l2_field(claim_a, 2, "SUBJECT_ID");
    ⚡ BSUB: c5l2_field(claim_b, 2, "SUBJECT_ID");
    IF (OID != GOID) { RETURN 0; }
    IF (OSUB != GSUB) { RETURN 0; }
    IF (ASUB != GSUB) { RETURN 0; }
    IF (BSUB != GSUB) { RETURN 0; }
    RETURN 1;
}

DEF c5c2_relation_request_payload(ledger, candidate_a, candidate_b, gap) {
    IF (c5l2_gap_valid(gap) == 0) { RETURN ""; }
    ⚡ STATE: c5l2_field(gap, 5, "STATE");
    IF (STATE != "OPEN") { RETURN ""; }
    RETURN c5a2_relation_request_payload(ledger, candidate_a, candidate_b);
}

DEF c5c2_make_bound_request(request_id, gap, payload_sha) {
    RETURN c5t2_make_request(request_id, gap, payload_sha);
}

DEF c5c2_make_evidence_ref(evidence_id, source_id, source_version_sha, artifact_sha, subject_id) {
    RETURN c5t2_make_evidence(evidence_id, source_id, source_version_sha, artifact_sha, subject_id);
}

DEF c5c2_make_claim_evaluation(eval_id, claim, evidence, source_stance, claim_side, basis_sha) {
    IF (c5l2_claim_valid(claim) == 0) { RETURN ""; }
    IF (c5l2_evidence_valid(evidence) == 0) { RETURN ""; }
    ⚡ CLAIM_ID: c5l2_field(claim, 1, "CLAIM_ID");
    ⚡ EVIDENCE_ID: c5l2_field(evidence, 1, "EVIDENCE_ID");
    ⚡ SOURCE_ID: c5l2_field(evidence, 2, "SOURCE_ID");
    ⚡ STANCE: c5a2_evaluation_stance_for_claim(source_stance, claim_side);
    RETURN c5t2_make_evaluation(eval_id, CLAIM_ID, EVIDENCE_ID, SOURCE_ID, STANCE, basis_sha);
}

DEF c5c2_revise_claim_from_truth(claim, truth_state, claim_side, uncertainty, new_revision) {
    IF (c5l2_claim_valid(claim) == 0) { RETURN ""; }
    ⚡ NEXT_CLASS: c5a2_seed_epistemic_class(truth_state, claim_side);
    RETURN c5l2_claim_revision_record(claim, NEXT_CLASS, uncertainty, new_revision);
}

DEF c5c2_open_conflict_gap(relation_gap, truth_state, conflict_gap_id, priority) {
    IF (c5l2_gap_valid(relation_gap) == 0) { RETURN ""; }
    IF (c5a2_conflict_gap_signal(truth_state) == 0) { RETURN ""; }
    ⚡ OBJECTIVE_ID: c5l2_field(relation_gap, 2, "OBJECTIVE_ID");
    ⚡ SUBJECT_ID: c5l2_field(relation_gap, 4, "SUBJECT_ID");
    RETURN c5t2_make_gap(conflict_gap_id, OBJECTIVE_ID, "CONFLICT", SUBJECT_ID, "EVIDENCE_SEARCH", priority);
}

DEF c5c2_pack_memory(work_id, claim_bank, gap_bank, evidence_ref_bank, revision) {
    RETURN c5l2_memory_pack(work_id, claim_bank, gap_bank, evidence_ref_bank, revision);
}

DEF c5c2_restart_recall_claim(memory, claim_id) {
    RETURN c5t2_memory_recall_claim(memory, claim_id);
}

DEF c5c2_restart_recall_gap(memory, gap_id) {
    RETURN c5t2_memory_recall_gap(memory, gap_id);
}
