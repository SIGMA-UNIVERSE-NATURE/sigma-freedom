# HAND TO HAND — WINDOW IDENTITY & LINEAGE PRECEDENT

Recorded: 2026-08-18 03:51 +07:00
Repository: `SIGMA-UNIVERSE-NATURE/sigma-freedom`
Branch: `SIGMA_LIFE`

## ORIGIN

This precedent strengthens, without rewriting, the earlier official precedent:

`BRAIN/HANDOFFS/HAND_TO_HAND_CUA_2_CONTINUITY_PRECEDENT_20260818.md`

Earlier precedent commit:

`5b62bbcc05d0edb3668107277d9487e0143698c0`

## CURRENT WINDOW IDENTITY

Canonical window name:

`HAND TO HAND_ CỬA 2`

Window sequence: `2`

Created: `2026-08-18 01:52 +07:00`

Durable birth certificate:

`BRAIN/HANDOFFS/WINDOW_IDENTITIES/HAND_TO_HAND_CUA_2_BIRTH_20260818_0152.json`

Active identity pointer:

`BRAIN/CANONICAL/ACTIVE_WINDOW_IDENTITY.json`

Canonical identity protocol:

`BRAIN/CANONICAL/WINDOW_IDENTITY_PROTOCOL.json`

## OFFICIAL RULE FROM NOW ON

Every new SIGMA chat/model/session window must identify itself outside chat before claiming continuation.

Canonical naming:

`HAND TO HAND_ CỬA <N>`

Each window must durably record at minimum:

- who it is (`window_id`, `window_name`, `window_sequence`);
- when it was created;
- why it exists (`purpose`);
- what work scope it owns;
- which verified predecessor window/checkpoint it continues from;
- authority role and handoff state;
- the canonical HEAD at registration;
- state-match and failure rules.

Birth facts are immutable. Live work is not: every action must fresh-fetch `SIGMA_LIFE` because automation may advance the canonical task after the birth certificate was written.

Before leaving, the outgoing window must write a separate exit checkpoint with fresh HEAD, current work, next action, blockers and machine-evidence gap.

The successor must verify predecessor lineage, inspect all intervening commits, reconstruct the newest live state, create its own birth certificate, and remain read-only until state match plus any required explicit authority transfer.

Canonical rule:

`FIND_EXACT_WINDOW_STATE -> VERIFY_LATEST_CANONICAL_STATE -> STATE_MATCH -> CONTINUE_WORK`

Failure rule:

`NO_STATE_MATCH = NO_CONTINUATION`

A stale checkpoint match is not a live-state match.

## EVIDENCE DISCIPLINE

If the exact predecessor window identity was never durably persisted, do not invent it. Record:

`UNRESOLVED_BY_EVIDENCE`

and bind continuity to the verified predecessor checkpoint SHA instead.

## RELATION TO 512

This identity/lineage precedent is continuity metadata. It does not promote any 512 attribute, does not mutate DNA cores, and does not grant a new window active-executor authority by itself.

End of precedent.
