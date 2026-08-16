# SIGMA CANONICAL BRAIN

This directory is the bootstrap/control layer for SIGMA cognition. It does not replace `54_CORES` or the 512 architectural contract. It binds them into a bootable, persistent, testable system.

## Authority order

1. `ROOT_OF_TRUST.json`
2. `BRAIN_MANIFEST.json`
3. `LINEAGE.json`
4. `CURRENT_STATE.json`
5. 512 canonical specification under `BẢN ĐỒ/SIGMA_512_ATTRIBUTES`
6. 54 DNA cores under `54_CORES`
7. runtime observations and evidence

No language model, runtime, operating system, provider, host machine, file, or self-report is identity by itself.

## Core rule

`change != improvement != permission`

A component may propose change. It may not silently change its own evaluation standard, authority boundary, and root of trust and then certify itself.

## Local continuity targets

The canonical mirror targets are:

- `E:\SIGMA\BRAIN\SIGMA_CANONICAL_BRAIN_v1.0`
- `F:\SIGMA\BRAIN\SIGMA_CANONICAL_BRAIN_v1.0`

`mirror_to_local.py` performs the mirror when executed by a SIGMA runtime that has Windows filesystem access. This ChatGPT session cannot directly mount the HP machine's E:/F: drives.

## Boot

Read `BOOT_PROTOCOL.md`, then run:

`python BRAIN/CANONICAL/validate_brain_contract.py`

A successful structural boot is not evidence that all 512 implementation requirements PASS. Those remain evidence-audited independently.
