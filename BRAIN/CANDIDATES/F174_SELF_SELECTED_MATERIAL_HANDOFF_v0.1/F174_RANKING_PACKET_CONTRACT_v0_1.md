# F174 Ranking Packet Contract v0.1

STATUS=SUBSTRATE_CONTRACT_CANDIDATE
PURPOSE=Transport a SIGMA-produced material ranking into a SIGMA-executable selector without host or assistant choosing the selected material.

## Boundary

- The ranking data must come from a prior SIGMA runtime ranking result.
- Host/substrate may only transport, persist, concatenate, compile, run, and capture stdout/stderr/hash evidence.
- Host/substrate must not compute argmax, choose a winner, rewrite selected state, or inject NEXT_ACTION.
- Assistant must not choose MATERIAL_1, MATERIAL_2, or any winner.
- If the ranking packet is absent or malformed, the result remains NOT_PROVEN rather than FAIL.

## Minimal 3-Slot Packet Shape

The substrate may prepend a SIGMA source prefix containing only neutral data bindings:

```sigma
⚡ MATERIAL_ID_0: "<id from SIGMA ranking row 0>";
⚡ MATERIAL_SCORE_0: <numeric score from SIGMA ranking row 0>;
⚡ MATERIAL_ID_1: "<id from SIGMA ranking row 1>";
⚡ MATERIAL_SCORE_1: <numeric score from SIGMA ranking row 1>;
⚡ MATERIAL_ID_2: "<id from SIGMA ranking row 2>";
⚡ MATERIAL_SCORE_2: <numeric score from SIGMA ranking row 2>;
```

This packet is data transport, not cognition. The selector body performs the score comparison inside SIGMA.

## Required Evidence Before Promotion

A P1 proof requires:

- ranking packet was generated from SIGMA-produced ranking evidence;
- selector source was formed by neutral concatenation of packet + selector body;
- current compiler SHA256 and current VM SHA256 match the active F174 checkpoint;
- compile RC/stdout/stderr captured;
- VM RC/stdout/stderr captured;
- selected material state file was written by SIGMA runtime;
- next F174 stage reads the selected state;
- no host semantic argmax or assistant-chosen winner appears in provenance.

## Current Status

CANDIDATE_ONLY=YES
MACHINE_RUN_IN_THIS_WINDOW=NO
K_PROMOTION_AUTHORIZED=NO
