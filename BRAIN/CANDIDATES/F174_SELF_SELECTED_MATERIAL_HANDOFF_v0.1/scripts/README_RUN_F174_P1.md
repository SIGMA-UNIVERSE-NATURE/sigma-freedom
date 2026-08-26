# Run F174 P1 Material Handoff 3-Slot Script

This script is a bounded OPPO/Termux runner for the F174 P1 candidate.

It does not choose the selected material in Bash. It only reads a SIGMA-produced ranking TSV, copies the first 3 valid material_id/score rows into neutral SIGMA bindings, renders selector source, compiles/runs selector, compiles/runs readback, and stores RC/stdout/stderr/hash evidence.

Command from ~/SIGMA/sigma_genesis1:

    git pull
    bash BRAIN/CANDIDATES/F174_SELF_SELECTED_MATERIAL_HANDOFF_v0.1/scripts/run_f174_p1_material_handoff_3slot.sh .sigma_tmp/<SIGMA-produced-ranking>.raw.tsv

Input TSV must contain at least 3 valid rows:

    material_id<TAB>score
    material_id<TAB>score
    material_id<TAB>score

Header rows or rows with nonnumeric field 2 are skipped.

Evidence output:

- .sigma_tmp/F174_P1_MATERIAL_HANDOFF/<RUN_ID>/
- .sigma_audit/F174_P1_MATERIAL_HANDOFF/<RUN_ID>/
- .sigma_exec/F174_SELECTED_MATERIAL_STATE_v0_1.txt

Do not promote P1 only because this script exits 0. Review evidence for no host argmax, no assistant winner, selector compile RC=0, selector VM RC=0, selected state exists, readback compile RC=0, readback VM RC=0, and next real F174 stage consumption.
