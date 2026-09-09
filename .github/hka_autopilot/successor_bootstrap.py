#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

CONTROL_ROOT = Path("DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/CURRICULUM_AUTOPILOT")
REGISTRY = CONTROL_ROOT / "WINDOW_REGISTRY.json"
PROMPTS = CONTROL_ROOT / "AUTOPILOT" / "WORKER_PROMPTS"


def find(registry: dict, window: str) -> dict | None:
    for stage in registry.get("stages", []):
        for family in stage.get("windows", []):
            if family.get("window_id") == window:
                return family
            for child in family.get("children", []):
                if child.get("window_id") == window:
                    return child
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default="work")
    ap.add_argument("--request-window", required=True)
    args = ap.parse_args()
    repo = Path(args.repo)
    registry = json.loads((repo / REGISTRY).read_text(encoding="utf-8"))

    target = find(registry, args.request_window)
    if not target or target.get("status") != "READY" or not target.get("execution_branch"):
        active = registry.get("active_transition", {})
        if active.get("status") == "READY" and active.get("execution_branch"):
            target = active
        else:
            raise SystemExit("No READY successor with execution_branch after Director opening")

    window = target["window_id"]
    branch = target["execution_branch"]
    prompt = repo / PROMPTS / f"{window}.md"
    if not prompt.exists():
        raise SystemExit(f"Director did not create durable Worker prompt template: {prompt}")

    print(json.dumps({"window_id": window, "branch": branch, "prompt_source": str(prompt)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
