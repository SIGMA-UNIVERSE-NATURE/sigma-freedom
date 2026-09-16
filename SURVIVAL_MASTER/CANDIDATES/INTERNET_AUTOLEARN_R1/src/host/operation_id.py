#!/usr/bin/env python3
"""Deterministic content-addressed IDs for mechanical side effects."""
import argparse, hashlib
ALLOWED = {'FETCH','DECODE','NATIVE_INPUT','NATIVE_OUTPUT','PERSIST_RECORD','QUEUE_ITEM'}

def operation_id(op_class: str, parts: list[str]) -> str:
    if op_class not in ALLOWED:
        raise ValueError('OP_CLASS_REJECTED')
    h=hashlib.sha256(); h.update(b'SIGMA_MECHANICAL_OP_R1\0'); h.update(op_class.encode()); h.update(b'\0')
    for p in parts:
        b=p.encode('utf-8'); h.update(str(len(b)).encode()); h.update(b':'); h.update(b); h.update(b'\0')
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--class', dest='op_class', required=True, choices=sorted(ALLOWED)); ap.add_argument('part', nargs='+')
    a=ap.parse_args(); print(f'OP_CLASS={a.op_class}'); print(f'OP_ID={operation_id(a.op_class,a.part)}')
if __name__=='__main__': main()
