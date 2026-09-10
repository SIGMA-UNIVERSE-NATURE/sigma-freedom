# C5V3 R4 durable academic memory model R1.
# Pure memory packing/validation/recall. Preserves objective, gaps, questions, structure, claims, evidence and native assessments.

DEF c5am1_agenda_valid(memory) {
    IF (memory == "") { RETURN 0; }
    IF (49152 < H("str_len", memory, NULL, NULL)) { RETURN 0; }
    ⚡ PREFIX: H("str_split", memory, "TYPE=ACADEMIC_AGENDA_MEMORY\n", NULL);
    IF (H("list_len", PREFIX, NULL, NULL) != 2) { RETURN 0; }
    IF (H("list_get", PREFIX, 0, NULL) != "") { RETURN 0; }
    ⚡ WORK: c5ak1_memory_section(memory, "WORK_BEGIN\n", "\nWORK_END");
    ⚡ OBJECTIVE: c5ak1_memory_section(memory, "OBJECTIVE_BEGIN\n", "\nOBJECTIVE_END");
    ⚡ GAPS: c5ak1_memory_section(memory, "GAPS_BEGIN\n", "\nGAPS_END");
    ⚡ QUESTIONS: c5ak1_memory_section(memory, "QUESTIONS_BEGIN\n", "\nQUESTIONS_END");
    IF (c5as1_work_valid(WORK) == 0) { RETURN 0; }
    IF (c5t2_objective_valid(OBJECTIVE) == 0) { RETURN 0; }
    IF (c5l2_field(WORK, 4, "OBJECTIVE_ID") != c5l2_field(OBJECTIVE, 1, "OBJECTIVE_ID")) { RETURN 0; }
    IF (c5l2_gap_bank_valid(GAPS) == 0) { RETURN 0; }
    IF (c5as1_question_bank_valid(QUESTIONS) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5am1_pack_agenda(work, objective, gap_bank, question_bank) {
    IF (c5as1_work_valid(work) == 0) { RETURN ""; }
    IF (c5t2_objective_valid(objective) == 0) { RETURN ""; }
    IF (c5l2_field(work, 4, "OBJECTIVE_ID") != c5l2_field(objective, 1, "OBJECTIVE_ID")) { RETURN ""; }
    IF (c5l2_gap_bank_valid(gap_bank) == 0) { RETURN ""; }
    IF (c5as1_question_bank_valid(question_bank) == 0) { RETURN ""; }
    IF (16384 < H("str_len", gap_bank, NULL, NULL)) { RETURN ""; }
    IF (16384 < H("str_len", question_bank, NULL, NULL)) { RETURN ""; }
    ⚡ OUT: "TYPE=ACADEMIC_AGENDA_MEMORY\nWORK_BEGIN\n" + work + "\nWORK_END\nOBJECTIVE_BEGIN\n" + objective + "\nOBJECTIVE_END\nGAPS_BEGIN\n" + gap_bank + "\nGAPS_END\nQUESTIONS_BEGIN\n" + question_bank + "\nQUESTIONS_END";
    IF (49152 < H("str_len", OUT, NULL, NULL)) { RETURN ""; }
    RETURN OUT;
}

DEF c5am1_structure_valid(memory) {
    IF (memory == "") { RETURN 0; }
    IF (65536 < H("str_len", memory, NULL, NULL)) { RETURN 0; }
    ⚡ PREFIX: H("str_split", memory, "TYPE=ACADEMIC_STRUCTURE_MEMORY\n", NULL);
    IF (H("list_len", PREFIX, NULL, NULL) != 2) { RETURN 0; }
    IF (H("list_get", PREFIX, 0, NULL) != "") { RETURN 0; }
    RETURN c5ad1_structure_memory_valid(memory);
}

DEF c5am1_memory_valid(memory) {
    IF (memory == "") { RETURN 0; }
    IF (196608 < H("str_len", memory, NULL, NULL)) { RETURN 0; }
    ⚡ PREFIX: H("str_split", memory, "TYPE=NATIVE_ACADEMIC_MEMORY_R1\n", NULL);
    IF (H("list_len", PREFIX, NULL, NULL) != 2) { RETURN 0; }
    IF (H("list_get", PREFIX, 0, NULL) != "") { RETURN 0; }
    ⚡ AGENDA: c5ak1_memory_section(memory, "AGENDA_BEGIN\n", "\nAGENDA_END");
    ⚡ STRUCTURE: c5ak1_memory_section(memory, "STRUCTURE_BEGIN\n", "\nSTRUCTURE_END");
    ⚡ CLAIMS: c5ak1_memory_section(memory, "CLAIMS_BEGIN\n", "\nCLAIMS_END");
    ⚡ EVIDENCE: c5ak1_memory_section(memory, "EVIDENCE_REFS_BEGIN\n", "\nEVIDENCE_REFS_END");
    ⚡ ASSESSMENT: c5ak1_memory_section(memory, "ASSESSMENT_BEGIN\n", "\nASSESSMENT_END");
    IF (c5am1_agenda_valid(AGENDA) == 0) { RETURN 0; }
    IF (c5am1_structure_valid(STRUCTURE) == 0) { RETURN 0; }
    IF (c5d1_claim_bank_valid(CLAIMS) == 0) { RETURN 0; }
    IF (c5l2_evidence_ref_bank_valid(EVIDENCE) == 0) { RETURN 0; }
    IF (c5ak1_assessment_valid(ASSESSMENT) == 0) { RETURN 0; }
    RETURN 1;
}

DEF c5am1_pack_memory(agenda, structure, claim_bank, evidence_bank, assessment) {
    IF (c5am1_agenda_valid(agenda) == 0) { RETURN ""; }
    IF (c5am1_structure_valid(structure) == 0) { RETURN ""; }
    IF (c5d1_claim_bank_valid(claim_bank) == 0) { RETURN ""; }
    IF (c5l2_evidence_ref_bank_valid(evidence_bank) == 0) { RETURN ""; }
    IF (c5ak1_assessment_valid(assessment) == 0) { RETURN ""; }
    IF (24576 < H("str_len", claim_bank, NULL, NULL)) { RETURN ""; }
    IF (32768 < H("str_len", evidence_bank, NULL, NULL)) { RETURN ""; }
    ⚡ OUT: "TYPE=NATIVE_ACADEMIC_MEMORY_R1\nAGENDA_BEGIN\n" + agenda + "\nAGENDA_END\nSTRUCTURE_BEGIN\n" + structure + "\nSTRUCTURE_END\nCLAIMS_BEGIN\n" + claim_bank + "\nCLAIMS_END\nEVIDENCE_REFS_BEGIN\n" + evidence_bank + "\nEVIDENCE_REFS_END\nASSESSMENT_BEGIN\n" + assessment + "\nASSESSMENT_END";
    IF (196608 < H("str_len", OUT, NULL, NULL)) { RETURN ""; }
    RETURN OUT;
}

DEF c5am1_recall_work(memory) {
    IF (c5am1_memory_valid(memory) == 0) { RETURN ""; }
    ⚡ AGENDA: c5ak1_memory_section(memory, "AGENDA_BEGIN\n", "\nAGENDA_END");
    RETURN c5ak1_memory_section(AGENDA, "WORK_BEGIN\n", "\nWORK_END");
}

DEF c5am1_recall_objective(memory) {
    IF (c5am1_memory_valid(memory) == 0) { RETURN ""; }
    ⚡ AGENDA: c5ak1_memory_section(memory, "AGENDA_BEGIN\n", "\nAGENDA_END");
    RETURN c5ak1_memory_section(AGENDA, "OBJECTIVE_BEGIN\n", "\nOBJECTIVE_END");
}

DEF c5am1_recall_gap(memory, gap_id) {
    IF (c5am1_memory_valid(memory) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(gap_id, 128) == 0) { RETURN ""; }
    ⚡ AGENDA: c5ak1_memory_section(memory, "AGENDA_BEGIN\n", "\nAGENDA_END");
    ⚡ GAPS: c5ak1_memory_section(AGENDA, "GAPS_BEGIN\n", "\nGAPS_END");
    ⚡ GAP: c5l2_bank_find_at(GAPS, 1, "GAP_ID", gap_id);
    IF (c5l2_gap_valid(GAP) == 0) { RETURN ""; }
    RETURN GAP;
}

DEF c5am1_recall_question(memory, question_id) {
    IF (c5am1_memory_valid(memory) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(question_id, 128) == 0) { RETURN ""; }
    ⚡ AGENDA: c5ak1_memory_section(memory, "AGENDA_BEGIN\n", "\nAGENDA_END");
    ⚡ QUESTIONS: c5ak1_memory_section(AGENDA, "QUESTIONS_BEGIN\n", "\nQUESTIONS_END");
    ⚡ QUESTION: c5l2_bank_find_at(QUESTIONS, 1, "QUESTION_ID", question_id);
    IF (c5as1_question_valid(QUESTION) == 0) { RETURN ""; }
    RETURN QUESTION;
}

DEF c5am1_recall_claim(memory, claim_id) {
    IF (c5am1_memory_valid(memory) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(claim_id, 128) == 0) { RETURN ""; }
    ⚡ CLAIMS: c5ak1_memory_section(memory, "CLAIMS_BEGIN\n", "\nCLAIMS_END");
    ⚡ CLAIM: c5l2_bank_find_at(CLAIMS, 1, "CLAIM_ID", claim_id);
    IF (c5d1_claim_valid(CLAIM) == 0) { RETURN ""; }
    RETURN CLAIM;
}

DEF c5am1_recall_synthesis(memory, claim_id) {
    IF (c5am1_memory_valid(memory) == 0) { RETURN ""; }
    IF (c5l2_safe_atom(claim_id, 128) == 0) { RETURN ""; }
    ⚡ ASSESSMENT: c5ak1_memory_section(memory, "ASSESSMENT_BEGIN\n", "\nASSESSMENT_END");
    ⚡ SYNTHESES: c5t2_memory_section(ASSESSMENT, "SYNTHESES_BEGIN\n", "\nSYNTHESES_END");
    ⚡ SYNTHESIS: c5l2_bank_find_at(SYNTHESES, 1, "CLAIM_ID", claim_id);
    IF (c5as1_synthesis_valid(SYNTHESIS) == 0) { RETURN ""; }
    RETURN SYNTHESIS;
}
