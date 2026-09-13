# SIGMA R11 Whole-Passage Semantic Invariance Learning R1

This directory carries a transport-safe Base64 split of the local R11 ZIP artifact because the ChatGPT attachment transport failed in the originating session.

Branch: `SIGMA_LANGUAGE_TOOLS`

Artifact reconstructed from parts:
`SIGMA_R11_WHOLE_PASSAGE_SEMANTIC_INVARIANCE_LEARNING_R1_BUNDLE.zip`

Expected ZIP SHA-256:
`f854990cf549d4c507ebd410857cc42cdd83a52ff743df99f94398ba6d96363c`

Important evidence boundary: this is a source/runtime bundle publication only. Local manifest/selftest passed before publication. R11 Termux runtime PASS is NOT claimed until an actual runtime receipt proves it.

## Reconstruct on Termux

```bash
cd "$HOME/storage/downloads"
OUT="SIGMA_R11_WHOLE_PASSAGE_SEMANTIC_INVARIANCE_LEARNING_R1_BUNDLE.zip"
: > "$OUT.b64"
for n in $(seq -f '%03g' 0 15); do
  curl -fsSL "https://raw.githubusercontent.com/SIGMA-UNIVERSE-NATURE/sigma-freedom/SIGMA_LANGUAGE_TOOLS/ARTIFACTS/R11_WHOLE_PASSAGE_SEMANTIC_INVARIANCE_LEARNING_R1/bundle.b64.part${n}" >> "$OUT.b64" || exit 1
done
base64 -d "$OUT.b64" > "$OUT" || exit 1
rm -f "$OUT.b64"
sha256sum "$OUT"
```

The printed hash must equal the expected SHA-256 above before running the bundle.
