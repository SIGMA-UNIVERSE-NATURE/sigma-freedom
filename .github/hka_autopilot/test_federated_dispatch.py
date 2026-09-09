#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('federated_dispatch', HERE / 'federated_dispatch.py')
assert SPEC and SPEC.loader
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)

base = {
    'control_plane_branch': 'hka-tree/curriculum-master',
    'role': 'DIRECTOR',
    'action': 'RUN_DIRECTOR_OPEN_SUCCESSOR',
    'target_window': 'C01-W05-B1.4-EARTH-UNIVERSE-FAMILY-C04-C06',
    'target_branch': None,
    'control_plane_sha': 'a' * 40,
}
new_head = dict(base)
new_head['control_plane_sha'] = 'b' * 40

assert mod.stable_request_id(base) == mod.stable_request_id(new_head)
assert mod.semantic_equal(base, new_head)

changed_action = dict(base)
changed_action['action'] = 'RUN_WORKER'
assert mod.stable_request_id(base) != mod.stable_request_id(changed_action)
assert not mod.semantic_equal(base, changed_action)

print('FEDERATED_DISPATCH_IDEMPOTENCY_PASS')
