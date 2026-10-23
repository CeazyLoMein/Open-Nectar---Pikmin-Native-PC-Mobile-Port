"""Launch the production SDL scene entry on a disposable CI simulator; no game assets."""
from pathlib import Path
import argparse,json,subprocess,time,traceback

def command(*args):
 p=subprocess.run(args,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=180)
 print('$ '+' '.join(map(str,args))+'\n'+p.stdout,flush=True)
 if p.returncode: raise RuntimeError(f'Command failed ({p.returncode}): {args}')
 return p.stdout.strip()

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--build-root',type=Path,required=True);parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
 args.output.mkdir(parents=True,exist_ok=True)
 apps=list(args.build_root.rglob('NectarSceneSmoke.app'));assert len(apps)==1,apps
 app=apps[0];bundle='org.opennectar.tests.scene'
 devices=json.loads(command('xcrun','simctl','list','devices','available','--json'))['devices']
 choices=[d for runtime,items in devices.items() if '.iOS-27' in runtime for d in items if d.get('isAvailable') and d['name'].startswith('iPhone')]
 assert choices,'No available iOS27 iPhone simulator; cannot claim a runtime launch pass'
 device=next((d for d in choices if d['state']=='Booted'),choices[0]);udid=device['udid'];started=device['state']!='Booted'
 report_path=None;final={}
 try:
  if started:command('xcrun','simctl','boot',udid)
  command('xcrun','simctl','bootstatus',udid,'-b')
  command('xcrun','simctl','install',udid,str(app))
  launch=command('xcrun','simctl','launch',udid,bundle)
  container=Path(command('xcrun','simctl','get_app_container',udid,bundle,'data'))
  report_path=container/'Documents/scene-smoke.json'
  def await_state(predicate,label,seconds=30):
   deadline=time.monotonic()+seconds;last={}
   while time.monotonic()<deadline:
    if report_path.exists():
     try:last=json.loads(report_path.read_text())
     except (OSError,json.JSONDecodeError):continue
     if last.get('error'):raise AssertionError(last)
     if predicate(last):return last
    time.sleep(.2)
   raise AssertionError(f'{label} timed out; last report={last}')
  first=await_state(lambda s:s.get('ready') and s.get('active'),'scene startup')
  assert first['entry_count']==1 and first['window_has_scene']
  assert first['scene_delegate']=='NectarSDLSceneDelegate'
  assert first['width']>first['height']>0,first
  assert first['reconnect_preserved_window'] and first['foreign_events_ignored'],first
  initial={k:first[k] for k in ['will_background','did_background','will_foreground','did_foreground']}
  command('xcrun','simctl','launch',udid,'com.apple.Preferences')
  background=await_state(lambda s:s.get('did_background',0)>initial['did_background'],'background event')
  # UIKit suspension may stop the app's outer loop immediately after the event.
  # The synchronous event watcher writes the report before returning to UIKit.
  assert background['will_background']==initial['will_background']+1,background
  assert background['did_background']==initial['did_background']+1,background
  resumed_launch=command('xcrun','simctl','launch',udid,bundle)
  assert launch.rsplit(':',1)[-1].strip()==resumed_launch.rsplit(':',1)[-1].strip(), 'Resume unexpectedly restarted the process'
  final=await_state(lambda s:s.get('active') and s.get('did_foreground',0)>initial['did_foreground'],'foreground event')
  assert final['entry_count']==1 and final['reconnect_preserved_window'],final
  assert final['will_foreground']==initial['will_foreground']+1 and final['did_foreground']==initial['did_foreground']+1,final
  assert final['will_background']==initial['will_background']+1 and final['did_background']==initial['did_background']+1,final
  (args.output/'scene-smoke-result.json').write_text(json.dumps({'result':'PASS','device':device['name'],'initial':first,'background':background,'resumed':final,'launch':launch,'resumed_launch':resumed_launch},indent=2))
  print('PASS: actual SDL/UIKit scene launch, one game entry, scene-owned window, landscape size, duplicate/reconnect guard, foreign-scene filtering and background/resume without duplicate SDL events.',flush=True)
 finally:
  if report_path and report_path.exists(): (args.output/'scene-smoke-last-report.json').write_bytes(report_path.read_bytes())
  subprocess.run(['xcrun','simctl','spawn',udid,'log','show','--last','3m','--style','compact','--predicate','process == "NectarSceneSmoke"'],stdout=(args.output/'scene-smoke-console.log').open('w'),stderr=subprocess.STDOUT,timeout=60)
  subprocess.run(['xcrun','simctl','terminate',udid,bundle],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,timeout=30)
  if started:subprocess.run(['xcrun','simctl','shutdown',udid],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,timeout=60)

if __name__=='__main__':main()
