"""Controlled packaging tests: no game execution or player files."""
import hashlib,importlib.util,json,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('pack',ROOT/'scripts/package-windows-coop.py');pack=importlib.util.module_from_spec(spec);spec.loader.exec_module(pack)
class Package(unittest.TestCase):
 def fixture(self,base):
  root=base/'repo';work=base/'build';(root/'scripts').mkdir(parents=True)
  (root/'scripts/netplay-deps.sh').write_text((ROOT/'scripts/netplay-deps.sh').read_text(encoding='utf-8'),encoding='utf-8')
  for name,path in pack.notice_inputs(root,work).items():path.parent.mkdir(parents=True,exist_ok=True);path.write_text('synthetic required notice '+name,encoding='utf-8')
  exe=work/'game-build/bin/nectar.exe';exe.parent.mkdir(parents=True);exe.write_bytes(b'MZ synthetic test fixture - NOT A GAME')
  identity=work/'game-build/desktop-generated/nectar_coop_build_identity.h';identity.parent.mkdir(parents=True);identity.write_text(','.join('0x12' for _ in range(32)))
  return root,work
 def test_required_source_paths(self):
  paths=pack.notice_inputs(ROOT,Path('fixture'))
  self.assertTrue(any('deps-cache/work/mingw64/protobuf-3.21.12/LICENSE' in str(p).replace('\\','/') for p in paths.values()))
  self.assertEqual(len(paths),8)
 def test_missing_notice_fails_early(self):
  with tempfile.TemporaryDirectory() as d:
   root,work=self.fixture(Path(d));pack.notice_inputs(root,work)['protobuf.txt'].unlink()
   with self.assertRaisesRegex(ValueError,'protobuf'):pack.check_notices(pack.notice_inputs(root,work))
   self.assertFalse((work/'package').exists())
 def test_full_package_and_receipt(self):
  with tempfile.TemporaryDirectory() as d:
   root,work=self.fixture(Path(d))
   with patch.object(pack.subprocess,'check_output',return_value='fixture-source\n'):pack.package(root,work)
   out=work/'package';receipt=json.loads((out/'BUILD RECEIPT.json').read_text(encoding='utf-8'))
   self.assertFalse(receipt['phone_or_windows_runtime_tested'])
   self.assertEqual(receipt['source'],'fixture-source')
   self.assertEqual(len(list((out/'Licenses').glob('*.txt'))),8)
   for name,digest in receipt['files'].items():self.assertEqual(hashlib.sha256((out/name).read_bytes()).hexdigest(),digest)
 def test_missing_identity_refused(self):
  with tempfile.TemporaryDirectory() as d:
   root,work=self.fixture(Path(d));(work/'game-build/desktop-generated/nectar_coop_build_identity.h').unlink()
   with self.assertRaisesRegex(ValueError,'identity'):pack.package(root,work)
   self.assertFalse((work/'package').exists())
if __name__=='__main__':unittest.main()
