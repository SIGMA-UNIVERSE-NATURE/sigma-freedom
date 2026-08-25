#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import urllib.request
from typing import Any, Dict, List, Optional

BASE_URL = os.environ.get("SIGMA_CODEC_URL", "http://127.0.0.1:8765").rstrip("/")
API_KEY = os.environ.get("SIGMA_CODEC_API_KEY", "").strip()


def _post(path: str, payload: Dict[str, Any], timeout: int = 90) -> Dict[str, Any]:
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    if API_KEY:
        headers["X-SIGMA-API-Key"] = API_KEY
    request = urllib.request.Request(
        BASE_URL + path,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def encode(
    text: str,
    source_language: str,
    semantic_graph: Optional[Dict[str, Any]],
    provenance: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    return _post(
        "/v1/encode",
        {
            "text": text,
            "source_language": source_language,
            "semantic_graph": semantic_graph,
            "provenance": provenance or [],
            "preserve_exact_raw": True,
        },
    )


def verify(package: Dict[str, Any]) -> Dict[str, Any]:
    return _post("/v1/verify", {"package": package})


def decode_exact(package: Dict[str, Any]) -> Dict[str, Any]:
    return _post("/v1/decode", {"package": package, "mode": "exact"})


def map_languages(package: Dict[str, Any], views: List[Dict[str, Any]]) -> Dict[str, Any]:
    return _post("/v1/map-languages", {"package": package, "views": views})


def roundtrip_languages(package: Dict[str, Any], languages: List[str]) -> Dict[str, Any]:
    return _post("/v1/roundtrip-languages", {"package": package, "target_languages": languages})


if __name__ == "__main__":
    print(json.dumps({"codec_url": BASE_URL, "ready": True}, ensure_ascii=False, indent=2))
