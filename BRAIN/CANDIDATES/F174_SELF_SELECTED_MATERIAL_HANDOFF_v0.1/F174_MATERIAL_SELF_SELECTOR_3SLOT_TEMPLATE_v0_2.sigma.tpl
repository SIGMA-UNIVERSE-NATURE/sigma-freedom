#SIGMAUNIVERSE_LANGUAGE[DOMAIN=SIGMA.F174.MATERIAL.HANDOFF][VERSION=P1.CANDIDATE.0.2]

DEF host_call(op, a, b, c) {
    RETURN host(op, a, b, c);
}

DEF save(path, content) {
    RETURN host_call("write_text", path, content, NULL);
}

DEF join(xs, delim) {
    RETURN host_call("str_join", xs, delim, NULL);
}

DEF list_create() {
    RETURN host_call("list_new", NULL, NULL, NULL);
}

DEF list_add(xs, item) {
    RETURN host_call("list_push", xs, item, NULL);
}

DEF select_id2(id0, score0, id1, score1) {
    IF (score0 < score1) {
        RETURN id1;
    }
    RETURN id0;
}

DEF select_score2(score0, score1) {
    IF (score0 < score1) {
        RETURN score1;
    }
    RETURN score0;
}

⟡(Σ.F174_MATERIAL_SELF_SELECTION) {
__SIGMA_PACKET_BINDINGS__
    ⚡ TARGET_FILE: ".sigma_exec/F174_SELECTED_MATERIAL_STATE_v0_1.txt";

    ⚡ BEST_ID_01: select_id2(MATERIAL_ID_0, MATERIAL_SCORE_0, MATERIAL_ID_1, MATERIAL_SCORE_1);
    ⚡ BEST_SCORE_01: select_score2(MATERIAL_SCORE_0, MATERIAL_SCORE_1);

    ⚡ SELECTED_ID: select_id2(BEST_ID_01, BEST_SCORE_01, MATERIAL_ID_2, MATERIAL_SCORE_2);
    ⚡ SELECTED_SCORE: select_score2(BEST_SCORE_01, MATERIAL_SCORE_2);

    ⚡ OUT: list_create();
    ⚡ list_add(OUT, "F174_SELECTED_MATERIAL_STATE_V0_1");
    ⚡ list_add(OUT, "SELECTED_ID");
    ⚡ list_add(OUT, SELECTED_ID);
    ⚡ list_add(OUT, "SELECTED_SCORE");
    ⚡ list_add(OUT, SELECTED_SCORE);
    ⚡ list_add(OUT, "SELECTION_AUTHORITY");
    ⚡ list_add(OUT, "SIGMA_PSI");
    ⚡ list_add(OUT, "HOST_ARGMAX_USED");
    ⚡ list_add(OUT, "NO");
    ⚡ list_add(OUT, "ASSISTANT_WINNER_USED");
    ⚡ list_add(OUT, "NO");

    ⚡ SERIALIZED: join(OUT, " | ");
    ⚡ save(TARGET_FILE, SERIALIZED);

    ⚡ print("F174_SELECTED_MATERIAL_STATE_WRITTEN");
    ⚡ print(TARGET_FILE);
}
