import importlib.util
from pathlib import Path
import tempfile
import unittest

MODULE = Path(__file__).resolve().parents[1] / 'ios/generate_coop_build_identity.py'
spec = importlib.util.spec_from_file_location('identity', MODULE)
identity = importlib.util.module_from_spec(spec)
spec.loader.exec_module(identity)


class IdentityTest(unittest.TestCase):
    def test_actual_bytes_names_version_and_line_endings(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / 'games/pikmin1/a.cpp'
            source.parent.mkdir(parents=True)
            source.write_bytes(b'code\r\n')
            names = ['games/pikmin1/a.cpp']
            baseline = identity.build_digest(root, names, 'USA1')[0]
            source.write_bytes(b'code\n')
            self.assertEqual(baseline, identity.build_digest(root, names, 'USA1')[0])
            source.write_bytes(b'new code\n')
            self.assertNotEqual(baseline, identity.build_digest(root, names, 'USA1')[0])
            self.assertNotEqual(baseline, identity.build_digest(root, names, 'PAL')[0])
            source.rename(source.with_name('b.cpp'))
            self.assertNotEqual(baseline, identity.build_digest(root, ['games/pikmin1/b.cpp'], 'USA1')[0])

    def test_docs_order_duplicates_and_unknown_files_do_not_change_identity(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'ios').mkdir()
            (root / 'ios/a.mm').write_text('native code')
            a = identity.build_digest(root, ['ios/a.mm'], 'USA1')
            b = identity.build_digest(root, ['ios/new-doc.md', 'ios/a.mm', 'unrelated.cpp', 'ios/a.mm'], 'USA1')
            self.assertEqual(a, b)
            self.assertEqual(a[1], 1)
            for names in [[], ['ios/../../outside.cpp']]:
                with self.assertRaises(ValueError):
                    identity.build_digest(root, names, 'USA1')


if __name__ == '__main__':
    unittest.main()
