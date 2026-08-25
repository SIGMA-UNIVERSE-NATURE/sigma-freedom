#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from fastapi.testclient import TestClient

from sigma_semantic_codec_service import app

ROOT = Path(__file__).resolve().parent


def main() -> None:
    demo = json.loads((ROOT / "multilingual_mapping_demo.json").read_text(encoding="utf-8"))
    graph = demo["semantic_graph"]
    text = demo["views"][0]["text"]

    with TestClient(app) as client:
        encoded_r = client.post(
            "/v1/encode",
            json={
                "text": text,
                "source_language": "vi",
                "semantic_graph": graph,
                "provenance": [{"id": "REF_V1_1", "source": "FROZEN_REFERENCE"}],
                "preserve_exact_raw": True,
            },
        )
        assert encoded_r.status_code == 200, encoded_r.text
        package = encoded_r.json()

        verify_r = client.post("/v1/verify", json={"package": package})
        assert verify_r.status_code == 200, verify_r.text
        verified = verify_r.json()
        assert verified["pass"] is True, verified
        assert verified["exact_raw_roundtrip"] is True, verified

        decode_r = client.post("/v1/decode", json={"package": package, "mode": "exact"})
        assert decode_r.status_code == 200, decode_r.text
        assert decode_r.json()["text"] == text

        map_r = client.post(
            "/v1/map-languages",
            json={"package": package, "views": demo["views"]},
        )
        assert map_r.status_code == 200, map_r.text
        mapped = map_r.json()
        assert mapped["target_language_count"] == 12, mapped
        assert mapped["all_structural_coverage_pass"] is True, mapped

    print("PASS: exact RAW round-trip")
    print("PASS: graph structure/hash verification")
    print("PASS: 12-language proposition-ID structural coverage")
    print("NOTE: linguistic semantic equivalence still requires independent re-extraction and signature comparison.")


if __name__ == "__main__":
    main()
