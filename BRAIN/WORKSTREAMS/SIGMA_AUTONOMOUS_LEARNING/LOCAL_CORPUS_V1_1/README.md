# SIGMA Local Autonomous Learning — GitHub Handoff V1

## Purpose

Preserve the current local-corpus learning candidate and its evidence without modifying SIGMA Production, compiler, VM, or the Obsidian vaults.

## Candidate that can connect to the existing VM surface

`source/SIGMA_LOCAL_CORPUS_MIRROR_AND_CHECKPOINT_V1_1.sigma`

The candidate uses only these requested host operations:

```text
input
list_get
list_len
listdir
mkdir
read_text
str_ends
to_int
write_text
```

Its intended data path is:

```text
source registry
→ SIGMA source V1.1
→ native/sigmac
→ native/sigma-vm.v09_candidate
→ external mirror/checkpoints
```

This is a nonactive candidate. Compilation and runtime compatibility on OPPO remain `NOT_DONE` until machine evidence is produced for this exact source hash.

## Evidence boundary

- V1 was compiled and invoked by the official native VM.
- V1 stopped with VM RC 26 because `crypto_digest` was unavailable.
- V1 produced zero content records, zero path records, and zero checkpoints.
- V1.1 removes `crypto_digest` and does not claim semantic understanding.
- Reading, mirroring, or comparing bytes is not evidence of learning or understanding.

## Included

- Exact V1.1 SIGMA source.
- Window J evidence-bound handoff.
- Machine-readable status.
- OPPO GitHub upload helper.

The OPPO helper additionally imports the exact safe checkpoint and the two known source-registry entries before committing.

## Excluded

- Obsidian document contents.
- Secrets or credentials.
- Temporary bytecode.
- SIGMA compiler or VM binaries.
- Any Production/core modification.
- Any claim that semantic learning has occurred.

## Next runtime gate

```text
VERIFY_V1_1_SOURCE_ON_OPPO
→ COMPILE_ONLY
→ NATIVE_VM_RUNTIME_TEST
→ MIRROR_AND_CHECKPOINT_EVIDENCE
```

