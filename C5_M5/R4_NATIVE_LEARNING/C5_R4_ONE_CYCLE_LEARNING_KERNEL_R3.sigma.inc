# C5V3 R4 one-cycle native learning kernel R3.
# Uses durable claims + evaluation-retaining memory. Depends on R4 R2, Adapter R3, Durable Model R1.
# Pure learning transitions only. No direct I/O, transport, persistence, host semantic selection, or capability choice.

DEF c5c4_relation_seed_valid(objective, gap, claim_a, claim_b, candidate_a, candidate_b) {
    IF (c5t2_objective_valid(objective) == 0) { RETURN 0; }
    IF (c5l2_gap_valid(gap) == 0) { RETURN 0; }
    IF (c5d1_claim_valid(claim_a) == 0) { RETURN 0; }
    IF (c5d1_claim_valid(claim_b) == 0) { RETURN 0; }
    ⚡ OID: c5l2_field(objective, 1, "OBJECTIVE_ID");
    ⚡ OSUB: c5l2_field(objective, 3, "SUBJECT_ID");
    ⚡ GOID: c5l2_field(gap, 2, "OBJECTIVE_ID");
    ⚡ GSUB: c5l2_field(gap, 4, "SUBJECT_ID");
    ⚡ ASUB: c5l2_field(claim_a, 2, "SUBJECT_ID");
    ⚡ BSUB: c5l2_field(claim_b, 2, "SUBJECT_ID");
    ⚡ ACONTENT: c5l2_field(claim_a, 3, "CONTENT");
    ⚡ BCONTENT: c5l2_field(claim_b, 3, "CONTENT");
    IF (OID != GOID) { RETURN 0; }
    IF (OSUB != GSUB) { RETURN 0; }
    IF (ASUB != GSUB) { RETURN 0; }
    IF (BSUB != GSUB) { RETURN 0; }
    IF (ACONTENT != candidate_a) { RETURN 0; }
    IF (BCONTENT != candidate_b) { RETURN 0; }
    RETURN 1;
}

DEF c5c4_relation_request_payload(ledger, candidate_a, candidate_b, gap) {
    IF (c5l2_gap_valid(gap) == 0) { RETURN ""; }
    IF (c5l2_field(gap, 5, "STATE") != "OPEN") { RETURN ""; }
    RETURN c5a3_relation_request_payload(ledger, candidate_a, candidate_b);
}

DEF c5c4_make_bound_request(request_id, gap, payload_sha) {
    RETURN c5t2_make_request(request_id, gap, payload_sha);
}

DEF c5c4_make_evidence_ref(evidence_id, source_id, source_version_sha, artifact_sha, subject_id) {
    RETURN c5t2_make_evidence(evidence_id, source_id, source_version_sha, artifact_sha, subject_id);
}

DEF c5c4_make_claim_evaluation(eval_id, claim, evidence, stance_record, claim_side, basis_sha) {
    IF (c5d1_claim_valid(claim) == 0) { RETURN ""; }
    IF (c5l2_evidence_valid(evidence) == 0) { RETURN ""; }
    IF (c5a3_source_stance_record_valid(stance_record) == 0) { RETURN ""; }
    IF (claim_side != "A") { IF (claim_side != "B") { RETURN ""; } }
    ⚡ CLAIM_ID: c5l2_field(claim, 1, "CLAIM_ID");
    ⚡ CLAIM_SUBJECT: c5l2_field(claim, 2, "SUBJECT_ID");
    ⚡ EVIDENCE_ID: c5l2_field(evidence, 1, "EVIDENCE_ID");
    ⚡ SOURCE_ID: c5l2_field(evidence, 2, "SOURCE_ID");
    ⚡ EVIDENCE_SUBJECT: c5l2_field(evidence, 5, "SUBJECT_ID");
    ⚡ STANCE_SOURCE_ID: c5l2_field(stance_record, 1, "SOURCE_ID");
    ⚡ SOURCE_STANCE: c5l2_field(stance_record, 2, "STANCE");
    IF (CLAIM_SUBJECT != EVIDENCE_SUBJECT) { RETURN ""; }
    IF (SOURCE_ID != STANCE_SOURCE_ID) { RETURN ""; }
    ⚡ STANCE: c5a3_evaluation_stance_for_claim(SOURCE_STANCE, claim_side);
    RETURN c5t2_make_evaluation(eval_id, CLAIM_ID, EVIDENCE_ID, SOURCE_ID, STANCE, basis_sha);
}

DEF c5c4_revise_claim_from_posture(claim, posture_record, claim_side, uncertainty, new_revision) {
    IF (c5d1_claim_valid(claim) == 0) { RETURN ""; }
    IF (c5a3_truth_posture_valid(posture_record) == 0) { RETURN ""; }
    IF (claim_side != "A") { IF (claim_side != "B") { RETURN ""; } }
    ⚡ TRUTH: c5l2_field(posture_record, 1, "TRUTH_STATE");
    ⚡ NEXT_CLASS: c5a3_seed_epistemic_class(TRUTH, claim_side);
    RETURN c5d1_claim_revision_record(claim, NEXT_CLASS, uncertainty, new_revision);
}

DEF c5c4_open_conflict_gap(relation_gap, posture_record, conflict_gap_id, priority) {
    IF (c5l2_gap_valid(relation_gap) == 0) { RETURN ""; }
    IF (c5a3_truth_posture_valid(posture_record) == 0) { RETURN ""; }
    ⚡ TRUTH: c5l2_field(posture_record, 1, "TRUTH_STATE");
    IF (c5a3_conflict_gap_signal(TRUTH) == 0) { RETURN ""; }
    ⚡ OBJECTIVE_ID: c5l2_field(relation_gap, 2, "OBJECTIVE_ID");
    ⚡ SUBJECT_ID: c5l2_field(relation_gap, 4, "SUBJECT_ID");
    RETURN c5t2_make_gap(conflict_gap_id, OBJECTIVE_ID, "CONFLICT", SUBJECT_ID, "EVIDENCE_SEARCH", priority);
}

DEF c5c4_pack_memory(work_id, claim_bank, gap_bank, evidence_ref_bank, evaluation_bank, revision) {
    RETURN c5d1_memory_pack(work_id, claim_bank, gap_bank, evidence_ref_bank, evaluation_bank, revision);
}

DEF c5c4_restart_recall_claim(memory, claim_id) {
    RETURN c5d1_memory_recall_claim(memory, claim_id);
}

DEF c5c4_restart_recall_gap(memory, gap_id) {
    RETURN c5t2_memory_recall_gap(memory, gap_id);
}

DEF c5c4_restart_recall_evaluations(memory, claim_id) {
    RETURN c5d1_memory_recall_evaluations(memory, claim_id);
}

DEF c5c4_restart_evidence_posture(memory, claim_id) {
    RETURN c5d1_memory_evidence_posture(memory, claim_id);
}
