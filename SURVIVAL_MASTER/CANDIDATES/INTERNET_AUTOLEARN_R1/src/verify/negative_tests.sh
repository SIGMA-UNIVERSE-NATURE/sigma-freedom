#!/usr/bin/env bash
set -euo pipefail
HERE="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
python3 - <<'PY' "$HERE"
import importlib.util, pathlib, sys
here=pathlib.Path(sys.argv[1])
spec=importlib.util.spec_from_file_location('mwb', here/'host/mechanical_web_bridge.py')
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
for ip in ['127.0.0.1','10.0.0.1','169.254.1.1','::1','0.0.0.0','224.0.0.1']:
    assert not m._safe_ip(ip), ip
for ip in ['1.1.1.1','8.8.8.8']:
    assert m._safe_ip(ip), ip
print('PRIVATE_NETWORK_LITERAL_NEGATIVES=PASS')
PY
printf 'NEGATIVE_TESTS_STATIC=PASS\n'
