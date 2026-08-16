# SIGMA CANONICAL BRAIN

This directory is the bootstrap/control layer for SIGMA cognition. It does not replace `54_CORES` or the 512 architectural contract. It binds them into a bootable, persistent, testable system.

## Authority and continuation order

1. `ROOT_OF_TRUST.json`
2. `MINH_OPERATING_CONSTITUTION.json`
3. `BRAIN_MANIFEST.json`
4. `LINEAGE.json`
5. `DO_NOT_RERUN_LOCKS.json`
6. `CURRENT_STATE.json`
7. `NEXT_ACTION.md`
8. 512 canonical specification under `BẢN ĐỒ/SIGMA_512_ATTRIBUTES`
9. 54 DNA cores under `54_CORES`
10. runtime observations and evidence

No language model, runtime, operating system, provider, host machine, chat window, file name, or self-report is identity by itself.

Conversation memory is orientation only. Canonical continuity comes from verified state, lineage, locks, evidence and the operating constitution.

## Core rules

`change != improvement != permission`

`specification != implementation`

`code != behavioral evidence`

`DO NOT IMPROVE YET -> MEASURE CURRENT REALITY FIRST` for an unaudited 512 implementation baseline.

A component may propose change. It may not silently change its own evaluation standard, authority boundary, and root of trust and then certify itself.

## Cross-window boot

A new window should enter through `MINH_WINDOW_BOOT.md`.

Minimal trigger:

`MINH BOOT SIGMA_LIFE`

The new session must verify repository/branch/HEAD, then read Root of Trust -> Operating Constitution -> Lineage -> Locks -> Current State -> Next Action before claiming continuation.

## Local continuity targets

The canonical mirror targets are:

- `E:\SIGMA\BRAIN\SIGMA_CANONICAL_BRAIN_v1.0`
- `F:\SIGMA\BRAIN\SIGMA_CANONICAL_BRAIN_v1.0`

`mirror_to_local.py` performs the mirror when executed by a SIGMA runtime that has Windows filesystem access. A chat session without local filesystem capability must report HOLD rather than pretend the mirror succeeded.

## Boot validation

Run:

`python BRAIN/CANONICAL/validate_brain_contract.py`

A successful structural boot is not evidence that all 512 implementation requirements PASS. Those remain evidence-audited independently.

## Durability rule

After meaningful verified progress, update evidence + `CURRENT_STATE.json` + `NEXT_ACTION.md` and verify the write before treating the progress as durable across window loss.
