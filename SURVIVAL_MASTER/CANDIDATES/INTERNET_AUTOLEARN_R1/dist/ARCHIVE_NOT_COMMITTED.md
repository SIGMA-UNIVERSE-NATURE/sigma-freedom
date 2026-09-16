# Archive handling

The GitHub connector used for this candidate submission writes UTF-8 repository files but does not publish the binary `.tgz` through the same text-file path. Therefore no binary placeholder is committed here.

`SUBMISSION.md` records `BUNDLE_PATH=EXTERNAL_NOT_COMMITTED` and the exact SHA256 of the deterministic archive produced from the exact `src/` tree by `src/verify/build_bundle.sh`.
