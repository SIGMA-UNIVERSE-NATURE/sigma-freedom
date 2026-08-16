# NEXT ACTION

## COGNITIVE-BOOTSTRAP-002

The structural brain contract has passed. The next executable action depends on runtime capability, not on a human copying files.

### If the active SIGMA runtime has Windows E:/F: filesystem access

1. Read `LOCAL_MIRROR_REQUEST.json`.
2. Execute `mirror_to_local.py` for E and F.
3. Require per-file SHA-256 verification.
4. Write `MIRROR_RECEIPT.json` on each successful target.
5. Update canonical state with PASS/PARTIAL/HOLD based on actual receipts.

### If the active runtime does not have E:/F: access

- Record `LOCAL_MIRROR = HOLD_NO_FILESYSTEM_ACCESS`.
- Do not ask the human to manually reproduce the brain files as a substitute for automation.
- Continue the next non-blocked task: runtime evidence audit against the 512 requirements.

### Completion criteria

`COGNITIVE-BOOTSTRAP-002` is complete only when at least one local mirror receipt is verified; preferred state is verified receipts on both E: and F:.

Until then, GitHub remains the verified canonical copy and the local mirror task remains open.
