from pathlib import Path
import base64, hashlib, json
root=Path(__file__).resolve().parent
m=json.loads((root/'ARCHIVE_CHUNKS_MANIFEST.json').read_text('utf-8'))
p=[]
for c in m['chunks']:
    s=(root/(c['file']+'.b64')).read_text('ascii').strip()
    assert len(s)==c['n'], (c['file'],'length')
    assert hashlib.sha256(s.encode('ascii')).hexdigest()==c['sha256'], (c['file'],'sha256')
    p.append(s)
s=''.join(p)
assert len(s)==m['archive']['base64_length'], 'base64_length'
b=base64.b64decode(s,validate=True)
assert len(b)==m['archive']['size'], 'archive_size'
assert hashlib.sha256(b).hexdigest()==m['archive']['sha256'], 'archive_sha256'
out=root/m['archive']['name']
out.write_bytes(b)
print('PHASE2_ARCHIVE_RECONSTRUCT_PASS',len(b),m['archive']['sha256'])
