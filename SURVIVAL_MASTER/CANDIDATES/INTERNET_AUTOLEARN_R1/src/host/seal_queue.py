#!/usr/bin/env python3
"""Content-addressed exact-byte sealed queue; no semantic transformation."""
from __future__ import annotations
import argparse, hashlib, json, os, shutil
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def fsync_dir(p: Path):
    fd = os.open(str(p), os.O_RDONLY)
    try: os.fsync(fd)
    finally: os.close(fd)


def copy_exact(src: Path, dst: Path):
    with src.open('rb') as r, dst.open('xb') as w:
        shutil.copyfileobj(r, w, 1024 * 1024)
        w.flush(); os.fsync(w.fileno())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--queue-root', required=True)
    ap.add_argument('--raw-content', required=True)
    ap.add_argument('--native-output', required=True)
    ap.add_argument('--native-event', required=True)
    ap.add_argument('--transport-receipt', required=True)
    ap.add_argument('--native-input-sha256', required=True)
    ap.add_argument('--native-output-mode', required=True)
    args = ap.parse_args()
    raw = Path(args.raw_content); native = Path(args.native_output)
    event = Path(args.native_event); receipt = Path(args.transport_receipt)
    for p in (raw, native, event, receipt):
        if not p.is_file():
            print(f'HOLD=QUEUE_INPUT_MISSING:{p}')
            return 2
    ids = {
        'raw_content_sha256': sha256_file(raw),
        'native_output_sha256': sha256_file(native),
        'native_event_sha256': sha256_file(event),
        'transport_receipt_sha256': sha256_file(receipt),
        'native_input_sha256': args.native_input_sha256,
        'native_output_mode': args.native_output_mode,
    }
    preimage = json.dumps(ids, sort_keys=True, separators=(',', ':')).encode()
    item_id = hashlib.sha256(preimage).hexdigest()
    q = Path(args.queue_root); staging = q/'staging'; sealed = q/'sealed'
    staging.mkdir(parents=True, exist_ok=True); sealed.mkdir(parents=True, exist_ok=True)
    final = sealed/item_id
    if final.is_dir():
        manifest = final/'record.json'
        if manifest.is_file() and json.loads(manifest.read_text())['record_id'] == item_id and (final/'SEALED').is_file():
            print('QUEUE_COMMIT=IDEMPOTENT_REUSE')
            print(f'QUEUE_ITEM_ID={item_id}')
            return 0
        print('HOLD=QUEUE_ITEM_ID_CONFLICT')
        return 2
    tmp = staging/(item_id + f'.partial.{os.getpid()}')
    tmp.mkdir(mode=0o700)
    copy_exact(raw, tmp/'raw.content')
    copy_exact(native, tmp/'native.output')
    copy_exact(event, tmp/'native.event')
    copy_exact(receipt, tmp/'transport.receipt.json')
    record = {
        'record_id': item_id,
        'source_request_sha256': ids['transport_receipt_sha256'],
        'raw_content_sha256': ids['raw_content_sha256'],
        'raw_byte_count': raw.stat().st_size,
        'native_input_sha256': ids['native_input_sha256'],
        'native_output_sha256': ids['native_output_sha256'],
        'native_output_byte_count': native.stat().st_size,
        'native_output_mode': ids['native_output_mode'],
        'native_event_sha256': ids['native_event_sha256'],
        'provenance_chain_sha256': hashlib.sha256((ids['transport_receipt_sha256'] + ids['native_event_sha256']).encode()).hexdigest(),
        'host_semantic_rewrite': False,
        'canonical_model_write': False,
    }
    data = (json.dumps(record, sort_keys=True) + '\n').encode()
    with (tmp/'record.json').open('xb') as f:
        f.write(data); f.flush(); os.fsync(f.fileno())
    with (tmp/'SEALED').open('xb') as f:
        f.write((item_id + '\n').encode()); f.flush(); os.fsync(f.fileno())
    fsync_dir(tmp)
    os.replace(tmp, final)
    fsync_dir(sealed)
    print('QUEUE_COMMIT=PASS')
    print(f'QUEUE_ITEM_ID={item_id}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
