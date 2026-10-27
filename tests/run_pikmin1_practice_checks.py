"""Collect admission/view/authority/population source fixtures; require all before packaging."""
import argparse,json,subprocess,sys
from pathlib import Path

CHECKS={'ios-sdk','generate-admission','compile-admission','run-admission','ios-admission',
        'generate-view','compile-view','run-view','ios-view',
        'generate-authority','compile-authority','run-authority','ios-authority',
        'generate-population','compile-population','run-population','ios-population'}

def run_checks(root,output,execute=subprocess.run):
 root=root.resolve();output=output.resolve();output.mkdir(parents=True,exist_ok=True)
 results={};outputs={}
 def check(name,args,needs=(),cwd=None):
  if any(results[n]['status']!='PASS' for n in needs):
   results[name]={'status':'BLOCKED','dependencies':list(needs)};return
  print('PRACTICE CHECK '+name,flush=True)
  try:
   completed=execute([str(a) for a in args],cwd=cwd or root,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=180)
   text=completed.stdout or '';outputs[name]=text.strip();results[name]={'status':'PASS' if completed.returncode==0 else 'FAIL','returncode':completed.returncode}
  except Exception as error:
   text=getattr(error,'output',None) or ''
   if isinstance(text,bytes):text=text.decode('utf-8',errors='replace')
   text+='\n'+str(error);results[name]={'status':'FAIL','error':type(error).__name__}
  (output/(name+'.log')).write_text(text,encoding='utf-8')
  if text:print(text,flush=True)
 check('ios-sdk',['xcrun','--sdk','iphoneos','--show-sdk-path'])
 pc=root/'games/pikmin1/pc_port'
 for name in ['admission','view','authority','population']:
  fixture=output/(name+'-fixture');binary=fixture/('practice-'+name+'-test')
  check('generate-'+name,[sys.executable,root/('tests/pikmin1_practice_'+name+'_test.py'),fixture])
  sources=[fixture/('practice-'+name+'-test.cpp')]
  if name=='admission':sources+=[pc/p for p in ['dolphin_stubs/card_stubs.cpp','pc_day_history.cpp','netplay/pc_coop_switch.cpp','netplay/pc_coop_practice_start.cpp']]
  elif name=='population':sources+=[pc/'netplay/pc_coop_pikmin_visuals.cpp',*[root/'libs/nectar_net/src'/p for p in ['pikmin_replication.cpp','world.cpp','byte_io.cpp']]]
  else:sources+=[pc/'netplay/pc_netplay_present.cpp',pc/'timing/pc_render_phase.cpp']
  flags=['-std=c++17','-pthread','-Wall','-Wextra','-Werror','-DPIKI_PC_PORT=1','-DNECTAR_P1_SOLO_TEST=0','-I'+str(fixture),'-I'+str(pc),'-I'+str(root/'libs/nectar_net/include')]
  if name!='admission':flags+=['-DNECTAR_COOP_WORLD=1']
  if name=='authority':flags+=['-DPC_NETPLAY_PRESENT_HOST=1']
  check('compile-'+name,['xcrun','--sdk','macosx','clang++',*flags,*sources,'-o',binary],('generate-'+name,))
  run=output/(name+'-run');run.mkdir(exist_ok=True)
  check('run-'+name,[binary,*([run/'state'] if name=='admission' else [])],('compile-'+name,),cwd=run)
  check('ios-'+name,['xcrun','--sdk','iphoneos','clang++','-target','arm64-apple-ios15.0','-isysroot',outputs.get('ios-sdk',''),*flags,'-fsyntax-only',*sources],('generate-'+name,'ios-sdk'))
 assert set(results)==CHECKS
 receipt={'result':'PASS' if all(v['status']=='PASS' for v in results.values()) else 'FAIL','checks':results}
 (output/'result.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
 print(json.dumps(receipt,indent=2),flush=True);return receipt

def verify_receipt(path,outcome):
 receipt=json.loads(path.read_text(encoding='utf-8'))
 if outcome!='success' or receipt.get('result')!='PASS' or set(receipt.get('checks',{}))!=CHECKS:
  raise ValueError('Practice startup/view/authority/population checks incomplete or failed; refusing IPA packaging')
 if any(c.get('status')!='PASS' or c.get('returncode')!=0 for c in receipt['checks'].values()):
  raise ValueError('Failed/blocked practice check; refusing IPA packaging')
 print('PASS: actual practice startup/save/view/authority/population fixtures; packaging may continue')

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);parser.add_argument('--verify',type=Path);parser.add_argument('--outcome')
 args=parser.parse_args()
 if args.verify:verify_receipt(args.verify,args.outcome)
 else:
  if not args.output:parser.error('--output is required')
  raise SystemExit(0 if run_checks(Path(__file__).resolve().parents[1],args.output)['result']=='PASS' else 1)
