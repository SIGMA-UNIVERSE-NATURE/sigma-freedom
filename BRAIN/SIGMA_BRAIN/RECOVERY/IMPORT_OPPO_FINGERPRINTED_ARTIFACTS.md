# IMPORT OPPO FINGERPRINTED ARTIFACTS INTO SIGMA_BRAIN

Date: 2026-08-19

Purpose: finish the part of the recovery capsule that cannot be reconstructed from GitHub history alone.

## Destination inside SIGMA_BRAIN

All exact OPPO foundation/runtime files for this snapshot must be copied under:

`BRAIN/SIGMA_BRAIN/OPPO_SNAPSHOT/20260819/`

Suggested structure:

```text
BRAIN/SIGMA_BRAIN/OPPO_SNAPSHOT/20260819/
├── FOUNDATION/
│   ├── sigmac.c
│   ├── sigma_vm.c
│   └── compiler_self.sigma
├── VM_V0_9/
│   ├── <exact-v0.9-source-filename>.sigma
│   └── <exact-v0.9-bytecode-filename>.sigmab
├── DICTIONARY/
│   └── <exact-dictionary-delta-file>
└── SHA256SUMS.txt
```

Do not rename a source artifact until its original exact path/name has been recorded in the manifest.

## Frozen OPPO fingerprints

```text
sigmac.c
e31fad26611fc95772a9a454eae6a735b220a8b7aa2ca95970c3623028ad0452

sigma_vm.c
8a567de997c335b38f49062622e3ec995b752b335a952b076d1f9283457fcae2

compiler_self.sigma
b00b415cc49d042ef152196633c5de4e7fffdf35da84bd900d31b599a9b60af7

VM v0.9 source
61ebd4bf7889f24f59f48173b6ec163030539d68e8383e807f1eac1dce7c9ed2

VM v0.9 bytecode
7724cb684244b0300e699c65dafe9f35c52a32d2a95f184c585b4321e8329fe0

Dictionary delta
5e8fe17d50caed41a11f130bc79fdf8084e4c2a5fda6b8ce66cbb079b9fdd154
```

## OPPO procedure

Run from the OPPO tree only after fetching `SIGMA_BRAIN`.

```bash
cd ~/SIGMA/sigma_genesis1

git fetch origin SIGMA_BRAIN
git switch SIGMA_BRAIN || git switch -c SIGMA_BRAIN --track origin/SIGMA_BRAIN
git pull --ff-only origin SIGMA_BRAIN

SNAP="BRAIN/SIGMA_BRAIN/OPPO_SNAPSHOT/20260819"
mkdir -p "$SNAP/FOUNDATION" "$SNAP/VM_V0_9" "$SNAP/DICTIONARY"

# Foundation files: copy only if their hashes match the frozen contract.
for f in sigmac.c sigma_vm.c compiler_self.sigma; do
  [ -f "$f" ] || { echo "HOLD_MISSING $f"; exit 10; }
done

[ "$(sha256sum sigmac.c | awk '{print $1}')" = "e31fad26611fc95772a9a454eae6a735b220a8b7aa2ca95970c3623028ad0452" ] || { echo "HOLD_HASH sigmac.c"; exit 11; }
[ "$(sha256sum sigma_vm.c | awk '{print $1}')" = "8a567de997c335b38f49062622e3ec995b752b335a952b076d1f9283457fcae2" ] || { echo "HOLD_HASH sigma_vm.c"; exit 12; }
[ "$(sha256sum compiler_self.sigma | awk '{print $1}')" = "b00b415cc49d042ef152196633c5de4e7fffdf35da84bd900d31b599a9b60af7" ] || { echo "HOLD_HASH compiler_self.sigma"; exit 13; }

cp -p sigmac.c "$SNAP/FOUNDATION/"
cp -p sigma_vm.c "$SNAP/FOUNDATION/"
cp -p compiler_self.sigma "$SNAP/FOUNDATION/"

# Locate the three remaining exact artifacts by SHA-256, do not guess by filename.
find . -type f -print0 | while IFS= read -r -d '' f; do
  h=$(sha256sum "$f" 2>/dev/null | awk '{print $1}')
  case "$h" in
    61ebd4bf7889f24f59f48173b6ec163030539d68e8383e807f1eac1dce7c9ed2)
      echo "FOUND_VM_V0_9_SOURCE=$f"
      cp -p "$f" "$SNAP/VM_V0_9/"
      ;;
    7724cb684244b0300e699c65dafe9f35c52a32d2a95f184c585b4321e8329fe0)
      echo "FOUND_VM_V0_9_BYTECODE=$f"
      cp -p "$f" "$SNAP/VM_V0_9/"
      ;;
    5e8fe17d50caed41a11f130bc79fdf8084e4c2a5fda6b8ce66cbb079b9fdd154)
      echo "FOUND_DICTIONARY_DELTA=$f"
      cp -p "$f" "$SNAP/DICTIONARY/"
      ;;
  esac
done

(
  cd "$SNAP"
  find . -type f ! -name SHA256SUMS.txt -print0 | sort -z | xargs -0 sha256sum > SHA256SUMS.txt
)

cat "$SNAP/SHA256SUMS.txt"

git status --short "$SNAP"
```

Before committing, verify the expected hashes are present in `SHA256SUMS.txt` exactly once for the intended artifact set. If an expected artifact is missing or multiple files share the same expected role unexpectedly, HOLD and inspect; do not choose silently.

Then commit only the snapshot paths:

```bash
git add "$SNAP"
git commit -m "Backup exact OPPO foundation and VM v0.9 artifacts 20260819"
git push origin SIGMA_BRAIN
```

Finally verify remote HEAD:

```bash
git fetch origin SIGMA_BRAIN
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse origin/SIGMA_BRAIN)
echo "LOCAL_HEAD=$LOCAL"
echo "REMOTE_HEAD=$REMOTE"
[ "$LOCAL" = "$REMOTE" ] && echo "OPPO_OFF_DEVICE_BACKUP=PASS" || echo "OPPO_OFF_DEVICE_BACKUP=HOLD"
```

## After this succeeds

Update:

`BRAIN/SIGMA_BRAIN/RECOVERY/SIGMA_BRAIN_RECOVERY_MANIFEST_20260819.json`

Change the six fingerprint-only entries from `CONTENT_PENDING` to content-backed paths, and set:

`oppo_foundation_exact_files = OFF_DEVICE_SAVED`

`oppo_vm_v0_9 = OFF_DEVICE_SAVED`

The next recovery level is then creation of the HP cold capsule under:

`E:\SIGMA\RECOVERY\OPPO_ACCEPTED_BASELINES\<BASELINE_ID>\`

Do not enable HP training or the legacy continuous Remote Operator to perform this backup.
