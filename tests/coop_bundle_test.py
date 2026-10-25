import importlib.util
from pathlib import Path
import plistlib
import tempfile
import unittest

MODULE = Path(__file__).resolve().parents[1] / 'ios/verify_coop_bundle.py'
spec = importlib.util.spec_from_file_location('bundle', MODULE)
bundle = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bundle)


class BundleTest(unittest.TestCase):
    def test_real_bytes_and_missing_or_changed_resource_rejection(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            app, original = root / 'P1.app', root / 'dependencies'
            (app / 'Licenses').mkdir(parents=True)
            original.mkdir()
            info = {'CFBundleIdentifier': 'org.opennectar.experimental.pikmin1',
                    'NSLocalNetworkUsageDescription': 'Private room connection'}
            (app / 'Info.plist').write_bytes(plistlib.dumps(info))
            for name in ['OpenSSL.txt', 'protobuf.txt', 'GameNetworkingSockets.txt']:
                (original / name).write_text(name + ' original notice')
                (app / 'Licenses' / name).write_bytes((original / name).read_bytes())
            bundle.verify(app, original)
            notice = app / 'Licenses/OpenSSL.txt'
            notice.write_text('changed')
            with self.assertRaises(ValueError): bundle.verify(app, original)
            notice.unlink()
            with self.assertRaises(ValueError): bundle.verify(app, original)

    def test_actual_xcode_flat_resources_and_conflicting_duplicate(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            app, original = root / 'P1.app', root / 'dependencies'
            app.mkdir()
            original.mkdir()
            info = {'CFBundleIdentifier': 'org.opennectar.experimental.pikmin1',
                    'NSLocalNetworkUsageDescription': 'Private room connection'}
            (app / 'Info.plist').write_bytes(plistlib.dumps(info))
            for name in ['OpenSSL.txt', 'protobuf.txt', 'GameNetworkingSockets.txt']:
                data = (name + ' verified original notice').encode()
                (original / name).write_bytes(data)
                (app / name).write_bytes(data)
            bundle.verify(app, original)
            (app / 'Licenses').mkdir()
            duplicate = app / 'Licenses/OpenSSL.txt'
            duplicate.write_bytes((original / 'OpenSSL.txt').read_bytes())
            bundle.verify(app, original)
            duplicate.write_text('stale or altered notice')
            with self.assertRaises(ValueError): bundle.verify(app, original)
            duplicate.unlink()
            (app / 'OpenSSL.txt').write_text('altered flat notice')
            with self.assertRaises(ValueError): bundle.verify(app, original)

    def test_no_permission_and_wrong_app_cannot_pass(self):
        with tempfile.TemporaryDirectory() as folder:
            app = Path(folder)
            for info in [{'CFBundleIdentifier': 'wrong'},
                         {'CFBundleIdentifier': 'org.opennectar.experimental.pikmin1'}]:
                (app / 'Info.plist').write_bytes(plistlib.dumps(info))
                with self.assertRaises(ValueError): bundle.verify(app, app)


if __name__ == '__main__': unittest.main()
