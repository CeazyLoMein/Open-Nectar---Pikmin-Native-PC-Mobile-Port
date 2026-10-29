"""Independent profile hashing regressions; no phone or proprietary assets."""
import importlib.util, hashlib, tempfile, unittest
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'tools/make_practice_companion_profile.py'
spec=importlib.util.spec_from_file_location('profile_tool',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class Profiles(unittest.TestCase):
 def test_native_golden(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);raw=bytes([0,255,1,3]);(root/'name.bin').write_bytes(raw)
   value,count=m.content_identity(root)
   expected=hashlib.sha256(b'NECTAR-P1-DATA-v2\0'+(8).to_bytes(4,'big')+b'name.bin'+(4).to_bytes(8,'big')+hashlib.sha256(raw).digest()).digest()
   self.assertEqual((value,count),(expected,1))
 def test_unicode_spelling(self):
  with tempfile.TemporaryDirectory() as d:
   a=Path(d)/'a';b=Path(d)/'b';a.mkdir();b.mkdir()
   (a/'caf\u00e9.bin').write_bytes(b'data');(b/'cafe\u0301.bin').write_bytes(b'data')
   self.assertEqual(m.content_identity(a),m.content_identity(b))
 def test_empty_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   with self.assertRaises(ValueError):m.content_identity(Path(d))
 def test_change_changes_identity(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d);(p/'a').write_bytes(b'a');before=m.content_identity(p);(p/'a').write_bytes(b'b')
   self.assertNotEqual(before,m.content_identity(p))
if __name__=='__main__':unittest.main()
