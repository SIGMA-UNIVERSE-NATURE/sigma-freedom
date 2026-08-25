#!/data/data/com.termux/files/usr/bin/python
# -*- coding: utf-8 -*-
"""Run structural proposition-coverage test against a live local Termux codec.

This runner does not stop, restart, kill, or modify the codec process. It only
reads local JSON files and POSTs to /v1/map-languages.
"""
from __future__ import annotations

import argparse
import json
import os
import urllib.request
from pathlib import Path
from typing import Any, Dict

DEFAULT_URL = os.environ.get("SIGMA_CODEC_URL", "http://127.0.0.1:8765").rstrip("/")
API_KEY = os.environ.get("SIGMA_CODEC_API_KEY", "").strip()


def load(path: str) -> Dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise SystemExit(f"JSON_OBJECT_REQUIRED:{path}")
    return value


def post(path: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    if API_KEY:
        headers["X-SIGMA-API-Key"] = API_KEY
    request = urllib.request.Request(
        DEFAULT_URL + path,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        value = json.loads(response.read().decode("utf-8"))
    if not isinstance(value, dict):
        raise SystemExit("RESPONSE_OBJECT_REQUIRED")
    return value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("package_file")
    parser.add_argument("views_file")
    args = parser.parse_args()

    package = load(args.package_file)
    views_doc = load(args.views_file)
    views = views_doc.get("views")
    if not isinstance(views, list) or not views:
        raise SystemExit("VIEWS_REQUIRED")

    result = post("/v1/map-languages", {"package": package, "views": views})
    print(json.dumps(result, ensure_ascii=False, indent=2))

    results = result.get("results", [])
    languages = [x.get("language") for x in results if isinstance(x, dict)]
    passed = [x.get("language") for x in results if isinstance(x, dict) and x.get("pass") is True]
    print("=== SUMMARY ===")
    print(f"TARGET_LANGUAGES={len(languages)}")
    print(f"STRUCTURAL_PASS={len(passed)}")
    print(f"ALL_STRUCTURAL_COVERAGE_PASS={result.get('all_structural_coverage_pass')}")
    print("SEMANTIC_EQUIVALENCE_VERIFIED=false")
    print("NOTE=Structural proposition coverage is not independent linguistic verification.")


if __name__ == "__main__":
    main()
