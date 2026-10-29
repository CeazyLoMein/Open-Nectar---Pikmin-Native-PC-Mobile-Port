import importlib.util,json,tempfile,unittest
from pathlib import Path
from types import SimpleNamespace
import subprocess
from unittest.mock import patch
module=Path(__file__).with_name('run_ios_room_checks.py')
spec=importlib.util.spec_from_file_location('checks',module);checks=importlib.util.module_from_spec(spec);spec.loader.exec_module(checks)

class RunnerTests(unittest.TestCase):
 def setUp(self):
  capture=patch('builtins.print');capture.start();self.addCleanup(capture.stop)
 def run_case(self,fail=None):
  calls=[]
  def execute(args,**kwargs):
   calls.append(args)
   target=' '.join(map(str,args))
   bad=fail and fail(target)
   return SimpleNamespace(returncode=1 if bad else 0,stdout='failure evidence' if bad else '/sdk/or/compiler')
  with tempfile.TemporaryDirectory() as tmp:
   result=checks.run_checks(Path(tmp),Path(tmp)/'out',execute)
   receipt=Path(tmp)/'out/result.json'
   if result['result']=='PASS':checks.verify_receipt(receipt,'success')
   else:
    with self.assertRaises(ValueError):checks.verify_receipt(receipt,'success')
  return result,calls
 def test_all_required_pass(self):
  result,_=self.run_case();self.assertEqual(result['result'],'PASS');self.assertEqual(len(result['checks']),13)
 def test_fixture_failure_collects_other_independent_errors(self):
  result,calls=self.run_case(lambda s:'pikmin1_ios_room_ux_test.py' in s or 'ios_coop_arc_names_test.py' in s)
  self.assertEqual(result['checks']['room-fixture']['status'],'FAIL')
  self.assertEqual(result['checks']['arc-getters']['status'],'FAIL')
  self.assertTrue(any('ios/ios_coop_room.mm' in c for c in calls))
 def test_content_compile_blocks_only_its_execution(self):
  result,calls=self.run_case(lambda s:'ios_coop_content_identity_test.mm' in s)
  self.assertEqual(result['checks']['content-run']['status'],'BLOCKED')
  self.assertEqual(result['checks']['room-ui']['status'],'PASS')
  self.assertFalse(any(len(c)==1 and c[0].endswith('content-identity-test') for c in calls))
 def test_missing_sdk_still_runs_portable_checks(self):
  result,_=self.run_case(lambda s:'--sdk iphoneos --show-sdk-path' in s)
  self.assertEqual(result['checks']['source-identity']['status'],'PASS')
  self.assertEqual(result['checks']['room-ui']['status'],'BLOCKED')
 def test_timeout_retains_partial_output_and_checks_continue(self):
  def execute(args,**kwargs):
   if 'tests/pikmin1_ios_room_ux_test.py' in args:
    raise subprocess.TimeoutExpired(args,kwargs['timeout'],output=b'partial compiler evidence')
   return SimpleNamespace(returncode=0,stdout='/sdk/or/compiler')
  with tempfile.TemporaryDirectory() as tmp:
   out=Path(tmp)/'out';result=checks.run_checks(Path(tmp),out,execute)
   self.assertIn('partial compiler evidence',(out/'room-fixture.log').read_text())
   self.assertEqual(result['checks']['room-ui']['status'],'PASS')
   self.assertEqual(result['result'],'FAIL')
 def test_gate_rejects_failed_step_even_with_pass_receipt(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp)/'r.json';p.write_text(json.dumps({'result':'PASS','checks':{n:{'status':'PASS','returncode':0} for n in checks.CHECK_NAMES}}))
   for outcome in ['failure','skipped','cancelled',None]:
    with self.assertRaises(ValueError):checks.verify_receipt(p,outcome)
 def test_gate_rejects_missing_and_hidden_failed_checks(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp)/'r.json'
   for bad in [{},{'room-ui':{'status':'PASS','returncode':0}},
       {n:{'status':'PASS','returncode':1 if n=='room-ui' else 0} for n in checks.CHECK_NAMES}]:
    p.write_text(json.dumps({'result':'PASS','checks':bad}))
    with self.assertRaises(ValueError):checks.verify_receipt(p,'success')

class FixtureAggregationTests(unittest.TestCase):
 def setUp(self):
  capture=patch('builtins.print');capture.start();self.addCleanup(capture.stop)
 def load_fixture(self):
  path=Path(__file__).with_name('pikmin1_ios_room_ux_test.py')
  spec=importlib.util.spec_from_file_location('fixture',path)
  module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
 def test_failed_desktop_compile_still_checks_native_and_never_runs_stale_binary(self):
  fixture=self.load_fixture();calls=[]
  def execute(args,**kwargs):
   calls.append(args)
   if args[0]=='clang++' and '-DNECTAR_IOS_COOP_ROOM=1' not in args and '-DNECTAR_DESKTOP_COOP_ROOM=1' not in args:
    raise subprocess.CalledProcessError(1,args)
   return SimpleNamespace(returncode=0)
  with tempfile.TemporaryDirectory() as tmp,patch.object(fixture.subprocess,'run',side_effect=execute):
   with self.assertRaises(RuntimeError):fixture.compile_and_run(Path(tmp)/'fixture.cpp','clang++')
  self.assertEqual(sum(c[0]=='clang++' for c in calls),3)
  runs=[c for c in calls if c[0]!='clang++']
  self.assertEqual(len(runs),2) # Only the two successfully compiled binaries may run.
  self.assertIn('room-ux-native',runs[0][0])
  self.assertIn('room-ux-desktop-coop',runs[1][0])
 def test_all_three_failed_modes_are_reported(self):
  fixture=self.load_fixture();calls=[]
  def execute(args,**kwargs):
   calls.append(args);raise subprocess.CalledProcessError(1,args)
  with tempfile.TemporaryDirectory() as tmp,patch.object(fixture.subprocess,'run',side_effect=execute):
   with self.assertRaisesRegex(RuntimeError,'desktop, native, desktop-coop'):
    fixture.compile_and_run(Path(tmp)/'fixture.cpp','clang++')
  self.assertEqual(len(calls),3)
  self.assertTrue(all(c[0]=='clang++' for c in calls))


 def test_desktop_coop_failure_does_not_execute_a_stale_binary(self):
  fixture=self.load_fixture();calls=[]
  def execute(args,**kwargs):
   calls.append(args)
   if args[0]=='clang++' and '-DNECTAR_DESKTOP_COOP_ROOM=1' in args:
    raise subprocess.CalledProcessError(1,args)
   return SimpleNamespace(returncode=0)
  with tempfile.TemporaryDirectory() as tmp,patch.object(fixture.subprocess,'run',side_effect=execute):
   with self.assertRaisesRegex(RuntimeError,'desktop-coop'):
    fixture.compile_and_run(Path(tmp)/'fixture.cpp','clang++')
  runs=[c for c in calls if c[0]!='clang++']
  self.assertEqual(len(runs),2)
  self.assertFalse(any('room-ux-desktop-coop' in c[0] for c in runs))

if __name__=='__main__':unittest.main()
