# SIGMA.AIL G2B - Canonical Brain Head Gate

This capsule starts the G2B runtime closure work.

It creates a producer-side mechanical receipt for the canonical `.sigma_ail` brain state. It does not promote G2 and does not claim semantic cognition.

## Mission

~~~text
GATE_ID=G2B_NATIVE_DOT_SIGMA_AIL_HEAD_STATE_VERSION_RECEIPT
SYSTEM_IDENTITY=SIGMA.AIL
CANONICAL_ROOT=.sigma_ail
ACTIVE_BRAIN_HEAD=<from .sigma_ail/BRAIN_HEAD>
MODEL_GENERATION=<from .sigma_ail/MODEL_GENERATION>
STATE_VERSION=<from .sigma_ail/STATE_VERSION>
HOST_COGNITION=NO
RUNTIME_TRUTH_SOURCE=EVIDENCE_OR_MACHINE_RECEIPT
~~~

## Oppo command

From the extracted capsule directory:

~~~bash
bash RUN_G2B_CANONICAL_RECEIPT.sh "$HOME/SIGMA/sigma_genesis1"
~~~

For the second run after restart/reload, pass the previous receipt:

~~~bash
bash RUN_G2B_CANONICAL_RECEIPT.sh "$HOME/SIGMA/sigma_genesis1" \
  --previous-receipt /path/to/previous/g2b_receipt.json
~~~

## Result boundary

The Python file performs byte/file/lock mechanics only. It reads canonical state fields, checks symlinks and hashes, holds the canonical writer lock while taking the snapshot, and writes a receipt. It does not understand content, choose beliefs, create semantic labels, or decide SIGMA cognition.


## Bind command

After the active R3 head has been discovered, bind .sigma_ail only when the legacy writer is idle:

~~~bash
bash RUN_G2B_BIND_CANONICAL.sh "$HOME/SIGMA/sigma_genesis1"
~~~

If SIGMA is writing, the bind command returns HOLD with LEGACY_WRITER_ACTIVE. That is the correct result while the supervisor is doing work.
