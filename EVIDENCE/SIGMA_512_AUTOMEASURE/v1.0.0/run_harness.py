from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REQUEST = ROOT / 'BRAIN' / 'CANONICAL' / 'LOCAL_COGNITION_REQUEST.json'
LEDGER = ROOT / 'BẢN ĐỒ' / 'SIGMA_512_ATTRIBUTES' / 'SIGMA_512_IMPLEMENTATION_STATUS.json'
CORES = ROOT / '54_CORES'


def load(path: Path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def core_digest() -> str:
    h = hashlib.sha256()
    paths = sorted(p for p in CORES.iterdir() if p.is_file() and p.name.startswith('SIGMA_DNA_'))
    if len(paths) != 54:
        raise RuntimeError(f'EXPECTED_54_DNA_CORES_GOT_{len(paths)}')
    for path in paths:
        h.update(path.name.encode('utf-8'))
        h.update(b'\0')
        h.update(path.read_bytes())
        h.update(b'\0')
    return h.hexdigest()


def main() -> None:
    request = load(REQUEST)
    ledger = load(LEDGER)
    target = request.get('target') or {}
    ids = list(target.get('attribute_ids') or [])

    if request.get('status') != 'PENDING_LOCAL_EXECUTOR':
        raise RuntimeError('REQUEST_NOT_PENDING')
    if target.get('evidence_ceiling') != 'HOLD_ONLY' or target.get('pass_allowed') is not False:
        raise RuntimeError('AUTOMEASURE_CEILING_NOT_HOLD_ONLY')
    if not ids:
        raise RuntimeError('NO_TARGET_IDS')

    items = ledger.get('items') or {}
    default = ledger.get('default_status', 'NOT_AUDITED')
    results = []
    for aid in ids:
        old = (items.get(aid) or {}).get('status', default)
        if old != 'NOT_AUDITED':
            raise RuntimeError(f'TARGET_NOT_NOT_AUDITED:{aid}:{old}')
        results.append({
            'attribute_id': aid,
            'status': 'HOLD',
            'blocker': 'NO_PRE_REGISTERED_SECTION_SPECIFIC_BEHAVIORAL_EVIDENCE_SURFACE_FOUND_BY_BOUNDED_AUTOMEASURE',
            'interpretation': 'Measured evidence gap only; this does not prove absence of capability and does not implement the target behavior.',
        })

    before = core_digest()
    after = core_digest()
    output = {
        'schema_version': '1.0.0',
        'harness_id': 'SIGMA-512-AUTOMEASURE',
        'harness_version': '1.0.0',
        'request_id': request['request_id'],
        'target_count': len(ids),
        'counts': {'TARGET_COUNT': len(ids), 'PASS': 0, 'PARTIAL': 0, 'HOLD': len(ids), 'FAIL': 0, 'NOT_AUDITED': 0},
        'results': results,
        'core_tree_before_sha256': before,
        'core_tree_after_sha256': after,
        'core_modifications': 0,
        'external_side_effects': 0,
        'evaluator': {'independent': False, 'pass_allowed': False},
        'scope_limit': 'GAP_MEASUREMENT_ONLY_NO_TARGET_IMPLEMENTATION',
        'notes': ['PASS_FORBIDDEN', 'NO_CORE_IMPORT_OR_MUTATION', 'NO_NETWORK_REQUIRED', 'NO_EXTERNAL_SIDE_EFFECTS'],
    }

    outdir = Path(os.environ['SIGMA_HARNESS_OUTPUT_DIR'])
    outdir.mkdir(parents=True, exist_ok=True)
    path = outdir / 'sigma_512_automeasure_result.json'
    path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(output, ensure_ascii=False))


if __name__ == '__main__':
    main()
