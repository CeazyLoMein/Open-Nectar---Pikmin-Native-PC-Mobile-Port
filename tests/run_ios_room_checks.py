"""Collect independent native preflight failures; enforce all before IPA packaging."""
import argparse,json,subprocess,sys
from pathlib import Path

CHECK_NAMES={'mac-sdk','mac-compiler','ios-sdk','ios-compiler','room-fixture','source-identity',
             'bundle','content-compile','content-run','arc-getters','generate-identity','room-ui'}

def run_checks(root,output,execute=subprocess.run):
 root=root.resolve();output=output.resolve();output.mkdir(parents=True,exist_ok=True)
 results={};outputs={}
 def check(name,args,needs=(),timeout=180):
  if any(results[n]['status']!='PASS' for n in needs):
   results[name]={'status':'BLOCKED','dependencies':list(needs)};return
  print('ROOM CHECK '+name,flush=True)
  try:
   result=execute(args,cwd=root,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=timeout)
   text=result.stdout or '';code=result.returncode
   outputs[name]=text.strip()
   results[name]={'status':'PASS' if code==0 else 'FAIL','returncode':code}
  except Exception as error:
   partial=getattr(error,'output',None) or ''
   if isinstance(partial,bytes):partial=partial.decode('utf-8',errors='replace')
   text=partial+'\n'+str(error);results[name]={'status':'FAIL','error':type(error).__name__}
  (output/(name+'.log')).write_text(text,encoding='utf-8')
  if text:print(text,flush=True)
 for kind,sdk in [('mac','macosx'),('ios','iphoneos')]:
  check(kind+'-sdk',['xcrun','--sdk',sdk,'--show-sdk-path'])
  check(kind+'-compiler',['xcrun','--sdk',sdk,'--find','clang++'])
 check('room-fixture',[sys.executable,'tests/pikmin1_ios_room_ux_test.py',str(output/'fixture.cpp'),
       '--compiler',outputs.get('mac-compiler',''),'--sdk-root',outputs.get('mac-sdk','')],('mac-sdk','mac-compiler'),timeout=360)
 check('source-identity',[sys.executable,'tests/coop_build_identity_test.py'])
 check('bundle',[sys.executable,'tests/coop_bundle_test.py'])
 binary=output/'content-identity-test'
 check('content-compile',['xcrun','--sdk','macosx','clang++','-std=c++17','-fobjc-arc',
       '-Wall','-Wextra','-Werror','-Wno-deprecated-declarations','-Iios',
       'tests/ios_coop_content_identity_test.mm','-framework','Foundation','-o',str(binary)])
 check('content-run',[str(binary)],('content-compile',))
 check('arc-getters',[sys.executable,'tests/ios_coop_arc_names_test.py','--compiler',outputs.get('ios-compiler',''),
       '--sdk-root',outputs.get('ios-sdk','')],('ios-sdk','ios-compiler'))
 header=output/'generated/nectar_coop_build_identity.h'
 check('generate-identity',[sys.executable,'ios/generate_coop_build_identity.py','--root',str(root),
       '--output',str(header),'--game-version','VERSION_GPIE01_01'])
 check('room-ui',['xcrun','--sdk','iphoneos','clang++','-target','arm64-apple-ios15.0',
       '-isysroot',outputs.get('ios-sdk',''),'-std=c++17','-fobjc-arc','-Wall','-Wextra','-Werror',
       '-fsyntax-only','-Iios','-Ilibs/nectar_net/include','-I'+str(header.parent),'ios/ios_coop_room.mm'],
       ('ios-sdk','generate-identity'))
 assert set(results)==CHECK_NAMES
 receipt={'result':'PASS' if all(v['status']=='PASS' for v in results.values()) else 'FAIL','checks':results}
 (output/'result.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
 print(json.dumps(receipt,indent=2),flush=True)
 return receipt

def verify_receipt(path,outcome):
 receipt=json.loads(path.read_text(encoding='utf-8'))
 if outcome!='success' or receipt.get('result')!='PASS' or set(receipt.get('checks',{}))!=CHECK_NAMES:
  raise ValueError('Required native room checks did not all pass; refusing IPA packaging')
 if any(c.get('status')!='PASS' or c.get('returncode')!=0 for c in receipt['checks'].values()):
  raise ValueError('Failed/blocked/missing native check; refusing IPA packaging')
 print('PASS: all required room preflight checks; packaging may continue')

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path)
 parser.add_argument('--verify',type=Path);parser.add_argument('--outcome')
 args=parser.parse_args()
 if args.verify:verify_receipt(args.verify,args.outcome)
 else:
  if not args.output:parser.error('--output is required')
  raise SystemExit(0 if run_checks(Path(__file__).resolve().parents[1],args.output)['result']=='PASS' else 1)
