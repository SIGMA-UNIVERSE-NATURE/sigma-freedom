#!/usr/bin/env python3
from pathlib import Path
import base64, gzip, hashlib, json

root = Path(__file__).resolve().parent
manifest = json.loads((root / "INGEST_MANIFEST.json").read_text(encoding="utf-8"))
out = root / "reconstructed"
out.mkdir(exist_ok=True)
failed = []

for rec in manifest["records"]:
    if "representation_parts" in rec:
        rep = b"".join((root / part["name"]).read_bytes() for part in rec["representation_parts"])
    else:
        rep = (root / rec["representation_name"]).read_bytes()

    rep_sha = hashlib.sha256(rep).hexdigest()
    raw = gzip.decompress(base64.b64decode(rep.strip()))
    raw_sha = hashlib.sha256(raw).hexdigest()
    target = out / rec["source_name"]
    target.write_bytes(raw)

    ok = (
        rep_sha == rec["representation_sha256"]
        and len(rep) == rec["representation_bytes"]
        and raw_sha == rec["source_sha256"]
        and len(raw) == rec["source_bytes"]
    )
    print(("PASS" if ok else "FAIL"), rec["source_name"], raw_sha, len(raw))
    if not ok:
        failed.append(rec["source_name"])

raise SystemExit(1 if failed else 0)
