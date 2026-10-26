import importlib.util,json,subprocess,tempfile,unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('practice_checks',Path(__file__).with_name('run_pikmin1_practice_checks.py'))
runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner)

class Checks(unittest.TestCase):
 def execute(self,fail=None,timeout=None):
  def result(args,**kwargs):
   text=' '.join(args)
   if timeout and timeout in text:raise subprocess.TimeoutExpired(args,180,output=b'partial compile diagnostic')
   return subprocess.CompletedProcess(args,1 if fail and fail in text else 0,'controlled compiler output')
  return result
 def test_success_and_gate(self):
  with tempfile.TemporaryDirectory() as d:
   out=Path(d)/'results';receipt=runner.run_checks(Path(d),out,self.execute())
   self.assertEqual(receipt['result'],'PASS');self.assertEqual(len(receipt['checks']),9);runner.verify_receipt(out/'result.json','success')
 def test_generation_failure_still_attempts_other_fixture(self):
  with tempfile.TemporaryDirectory() as d:
   receipt=runner.run_checks(Path(d),Path(d)/'results',self.execute(fail='pikmin1_practice_admission_test.py'))
   self.assertEqual(receipt['result'],'FAIL');self.assertEqual(receipt['checks']['compile-admission']['status'],'BLOCKED');self.assertEqual(receipt['checks']['run-view']['status'],'PASS')
 def test_compile_failure_collects_ios_and_other_fixture(self):
  with tempfile.TemporaryDirectory() as d:
   receipt=runner.run_checks(Path(d),Path(d)/'results',self.execute(fail='--sdk macosx'))
   self.assertEqual(receipt['checks']['run-admission']['status'],'BLOCKED');self.assertEqual(receipt['checks']['run-view']['status'],'BLOCKED')
   self.assertEqual(receipt['checks']['ios-admission']['status'],'PASS');self.assertEqual(receipt['checks']['ios-view']['status'],'PASS')
 def test_timeout_preserves_output(self):
  with tempfile.TemporaryDirectory() as d:
   out=Path(d)/'results';receipt=runner.run_checks(Path(d),out,self.execute(timeout='arm64-apple-ios15.0'))
   self.assertEqual(receipt['result'],'FAIL');self.assertIn('partial compile diagnostic',(out/'ios-view.log').read_text())
 def test_gate_rejects_false_success_and_failed_step(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'result.json';receipt={'result':'PASS','checks':{k:{'status':'PASS','returncode':0} for k in runner.CHECKS}}
   p.write_text(json.dumps(receipt))
   for outcome in ['failure','skipped','cancelled','']:
    with self.assertRaises(ValueError):runner.verify_receipt(p,outcome)
   receipt['checks']['ios-view']['returncode']=1;p.write_text(json.dumps(receipt))
   with self.assertRaises(ValueError):runner.verify_receipt(p,'success')
   del receipt['checks']['ios-view'];p.write_text(json.dumps(receipt))
   with self.assertRaises(ValueError):runner.verify_receipt(p,'success')
 def test_missing_receipt_refused(self):
  with tempfile.TemporaryDirectory() as d:
   with self.assertRaises(FileNotFoundError):runner.verify_receipt(Path(d)/'missing.json','success')

if __name__=='__main__':unittest.main()
