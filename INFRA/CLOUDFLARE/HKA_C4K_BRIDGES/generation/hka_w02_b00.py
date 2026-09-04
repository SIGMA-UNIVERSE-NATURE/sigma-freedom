import base64,hashlib,io,json,os,re,subprocess,tempfile,zipfile
from pathlib import Path
import requests
from PIL import Image,ImageDraw,ImageFont

BRAND_COMMIT='2d3aa9d8418acccd39a3d263e917d4157e029e17'
PROMPT_COMMIT='295f73a8e833b5a0ffb9642078514e7e3924700a'
MANIFEST_COMMIT='7028f0c008bca4e8dcaea2bd878ef9210113e223'
RUN='HKA-W02-B00-R01';BATCH='HKA-W02-B00';MODEL='gpt-image-2-2026-04-21'
ROOT='DOCS/HKA_KNOWLEDGE_SYSTEM_TREES/WINDOWS/W02_HUMAN_ROOTS'
REFS={
'sigma.png':('assets/characters/sigma.png','72e29ad1ba8e71a25f7fc7d4da656a6196fdf6db',1094258),
'cricket.png':('assets/characters/cricket.png','87e30fe00beb0a122fefde8126c54d98ae7c0e08',1535430),
'little-ant.png':('assets/characters/little-ant.png','a931ae833d184ecb48f1b20bc90a8cbeee181d8c',1224688),
'professor-owl.png':('assets/characters/professor-owl.png','b5c58c5502ee39aff941769fa143f071384c3472',1843472),
'sigma-logo-master.jpg':('assets/logo/sigma-logo-master.jpg','1f19dcbb970ef414fe3a58d406d1b4b55360853e',225466)}
ASSETS={'HKA-VIS-W02-0001':['sigma.png','cricket.png','little-ant.png','professor-owl.png'],'HKA-VIS-W02-0002':['professor-owl.png']}

def sh(*a):return subprocess.check_output(a,text=False)
def sha(b):return hashlib.sha256(b).hexdigest()
def git_blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def git_show(commit,path):return sh('git','show',f'{commit}:{path}')
def prompt_for(text,asset):
 s=re.search(rf'## {re.escape(asset)} .*?### H — Generation prompts\n.*?PROMPT EN:\n(.*?)(?:\n\nGLOBAL NEGATIVE PROMPT:\n)(.*?)(?=\n\n### I — Output)',text,re.S)
 if not s:raise RuntimeError('PROMPT_PARSE_FAILED:'+asset)
 return s.group(1).strip()+'\n\nHard negatives: '+re.sub(r'\s+',' ',s.group(2).strip())
def fetch_refs(tmp):
 out={}
 for name,(path,blob,size) in REFS.items():
  u=f'https://raw.githubusercontent.com/linkcomltd-byte/sigma-universe-web/{BRAND_COMMIT}/{path}'
  b=requests.get(u,timeout=90).content
  if len(b)!=size or git_blob(b)!=blob:raise RuntimeError('REFERENCE_VERIFY_FAILED:'+name)
  p=Path(tmp)/name;p.write_bytes(b);out[name]=p
 return out
def bridge(method,path,token,base,**kw):
 h=kw.pop('headers',{});h['Authorization']='Bearer '+token
 r=requests.request(method,base.rstrip('/')+path,headers=h,timeout=180,**kw)
 if r.status_code==409:return {'status':'EXISTS','detail':r.text}
 if not r.ok:raise RuntimeError(f'BRIDGE_{r.status_code}:{r.text[:1000]}')
 return r.json()
def generate(prompt,ref_paths,out):
 files=[]
 opened=[]
 try:
  for p in ref_paths:
   f=open(p,'rb');opened.append(f);files.append(('image[]',(p.name,f,'image/png')))
  data={'model':MODEL,'prompt':prompt,'size':'3840x2160','quality':'high','output_format':'png','n':'1'}
  r=requests.post('https://api.openai.com/v1/images/edits',headers={'Authorization':'Bearer '+os.environ['OPENAI_API_KEY']},data=data,files=files,timeout=900)
  if not r.ok:raise RuntimeError('IMAGE_API_FAILED:'+r.text[:1500])
  b=base64.b64decode(r.json()['data'][0]['b64_json']);Image.open(io.BytesIO(b)).verify();im=Image.open(io.BytesIO(b))
  if im.size!=(3840,2160):raise RuntimeError(f'OUTPUT_CAPABILITY_BLOCKED:{im.size}')
  out.write_bytes(b);return b
 finally:
  for f in opened:f.close()
def brand(clean,logo,out):
 im=Image.open(clean).convert('RGB');lg=Image.open(logo).convert('RGB');w=int(im.width*.105);lg.thumbnail((w,int(im.height*.15)))
 x=im.width-lg.width-int(im.width*.04);y=int(im.height*.035);im.paste(lg,(x,y))
 d=ImageDraw.Draw(im);text='PEACEFUL MIND-KINDLY HEART-KEEP GROWING.';fontp='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf';font=ImageFont.truetype(fontp,40)
 box=d.textbbox((0,0),text,font=font);tx=(im.width-(box[2]-box[0]))//2;ty=im.height-int(im.height*.045)-40
 d.rounded_rectangle((tx-28,ty-14,tx+(box[2]-box[0])+28,ty+58),radius=12,fill=(255,255,255,225));d.text((tx,ty),text,font=font,fill=(25,25,25))
 im.save(out,'PNG');return out.read_bytes()
def upload_asset(base,token,asset,var,path):
 b=path.read_bytes();return bridge('POST',f'/v1/production/runs/{RUN}/assets',token,base,files={'file':(path.name,b,'image/png')},data={'asset_id':asset,'variant':var,'sha256':sha(b)})
def upload_record(base,token,typ,path,asset=''):
 b=path.read_bytes();return bridge('POST',f'/v1/production/runs/{RUN}/records',token,base,files={'file':(path.name,b,'application/octet-stream')},data={'record_type':typ,'asset_id':asset,'sha256':sha(b)})
def main():
 base=os.environ['HKA_PRODUCTION_BRIDGE_URL'];tok=os.environ['HKA_PRODUCTION_BRIDGE_AUTH_TOKEN']
 with tempfile.TemporaryDirectory() as td:
  td=Path(td);refs=fetch_refs(td);prompts=git_show(PROMPT_COMMIT,f'{ROOT}/PRODUCTION/BATCHES/{BATCH}/BATCH_PROMPTS.md').decode()
  bridge('POST','/v1/production/runs',tok,base,json={'window_id':'W02','tree_slug':'human-roots','prompt_commit_sha':PROMPT_COMMIT,'batch_id':BATCH,'run_id':RUN})
  sums=[];meta=[]
  for asset,names in ASSETS.items():
   clean=td/f'{asset}_CLEAN_MASTER.png';b=generate(prompt_for(prompts,asset),[refs[n] for n in names],clean);sums.append((sha(b),clean.name));upload_asset(base,tok,asset,'CLEAN_MASTER',clean)
   branded=td/f'{asset}_BRANDED_FINAL.png';bb=brand(clean,refs['sigma-logo-master.jpg'],branded);sums.append((sha(bb),branded.name));upload_asset(base,tok,asset,'BRANDED_FINAL',branded)
   mp=td/f'{asset}_ASSET.json';mp.write_text(json.dumps({'asset_id':asset,'run_id':RUN,'model':MODEL,'reference_files':names,'clean_sha256':sha(b),'branded_sha256':sha(bb)},sort_keys=True,separators=(',',':')));upload_record(base,tok,'ASSET_METADATA',mp,asset);meta.append(mp)
  manifest=td/'BATCH_MANIFEST.json';manifest.write_bytes(git_show(MANIFEST_COMMIT,f'{ROOT}/PRODUCTION/BATCHES/{BATCH}/BATCH_MANIFEST.json'));upload_record(base,tok,'BATCH_MANIFEST_JSON',manifest)
  side=td/'BATCH_MANIFEST.sha256';side.write_bytes(git_show(MANIFEST_COMMIT,f'{ROOT}/PRODUCTION/BATCHES/{BATCH}/BATCH_MANIFEST.sha256'));upload_record(base,tok,'BATCH_MANIFEST_SHA256',side)
  bp=td/'BATCH_PROMPTS.md';bp.write_bytes(git_show(PROMPT_COMMIT,f'{ROOT}/PRODUCTION/BATCHES/{BATCH}/BATCH_PROMPTS.md'));upload_record(base,tok,'BATCH_PROMPTS_MD',bp)
  report=td/'PRODUCTION_REPORT.md';report.write_text(f'# {RUN} Production Report\n\nModel: `{MODEL}`\n\nOfficial references fetched and Git-blob verified. Exact 3840x2160 outputs produced through API image-reference inputs.\n');upload_record(base,tok,'PRODUCTION_REPORT_MD',report)
  qa=td/'SELF_QA_REPORT.json';qa.write_text(json.dumps({'schema_version':'1.0','run_id':RUN,'status':'SELF_QA_PRECHECK_PASS','checks':{'reference_integrity':'PASS','dimensions':'PASS','format':'PASS','generated_logo_or_motto':'NO_MODEL_GENERATED_BRANDING'},'independent_qa_required':True},sort_keys=True,separators=(',',':')));upload_record(base,tok,'SELF_QA_REPORT_JSON',qa)
  sumsfile=td/'SHA256SUMS.txt';sumsfile.write_text(''.join(f'{h}  {n}\n' for h,n in sums));upload_record(base,tok,'SHA256SUMS_TXT',sumsfile)
  package=td/f'{BATCH}-{RUN}.zip'
  with zipfile.ZipFile(package,'w',zipfile.ZIP_DEFLATED) as z:
   for p in list(td.glob('HKA-VIS-W02-*'))+[manifest,side,bp,report,qa,sumsfile]:z.write(p,p.name)
  upload_record(base,tok,'PRODUCTION_PACKAGE_ZIP',package)
  msha=side.read_text().split()[0];bridge('POST',f'/v1/production/runs/{RUN}/complete',tok,base,json={'manifest_sha256':msha,'package_sha256':sha(package.read_bytes()),'expected_object_count':13})
  print(json.dumps({'status':'QA_PENDING','run_id':RUN,'package_sha256':sha(package.read_bytes())}))
if __name__=='__main__':main()
