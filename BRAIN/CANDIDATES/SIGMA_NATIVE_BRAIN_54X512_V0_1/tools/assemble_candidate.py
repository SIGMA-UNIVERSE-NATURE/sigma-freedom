#!/usr/bin/env python3
from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORDER = [
    ROOT / "src" / "00_core_registry.sigma",
    ROOT / "src" / "10_skill_router_a.sigma.part",
    ROOT / "src" / "10_skill_router_b.sigma.part",
    ROOT / "src" / "20_accuracy_kernel.sigma",
    ROOT / "src" / "90_main.sigma",
]
OUTPUT = ROOT / "src" / "sigma_native_brain_54x512_v0_1.sigma"

raw = b"".join(path.read_bytes() for path in ORDER)
text = raw.decode("utf-8", errors="strict")
if "\ufffd" in text:
    raise SystemExit("UTF8_REPLACEMENT_CHARACTER_FORBIDDEN")
OUTPUT.write_bytes(raw)
print(f"ASSEMBLED {OUTPUT}")
print(f"BYTES={len(raw)}")
print(f"SHA256={hashlib.sha256(raw).hexdigest()}")
