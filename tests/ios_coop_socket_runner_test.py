"""Checks that iOS runtime evidence cannot become a false success."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tests'))
from run_ios_coop_socket_probe import run


class RunnerTest(unittest.TestCase):
    def exercise(self, *, platform='IOSSIMULATOR', marker=True, failed=False, booted=False):
        calls = []

        def execute(*args, **kwargs):
            calls.append(args)
            if 'vtool' in args:
                return f'platform {platform}'
            if 'list' in args:
                return json.dumps({'devices': {'com.apple.CoreSimulator.SimRuntime.iOS-27-1': [
                    {'name': 'iPhone probe', 'udid': 'test-only', 'isAvailable': True,
                     'state': 'Booted' if booted else 'Shutdown'}]}})
            if 'spawn' in args:
                if failed:
                    raise RuntimeError('child process failed')
                return 'NECTAR_COOP_SOCKET_PROBE_PASS\n' if marker else 'partial progress'
            return ''

        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            binary = base / 'probe'
            binary.write_bytes(b'fixture executable')
            output = base / 'evidence'
            try:
                run(binary, output, execute)
            except (RuntimeError, AssertionError):
                pass
            receipt = json.loads((output / 'result.json').read_text())
            self.assertEqual(len(receipt['binary_sha256']), 64)
        return calls, receipt

    def test_complete_success_and_owned_simulator_cleanup(self):
        calls, receipt = self.exercise()
        self.assertEqual(receipt['result'], 'PASS')
        self.assertTrue(any('shutdown' in call for call in calls))

    def test_never_shutdown_preexisting_simulator(self):
        calls, receipt = self.exercise(booted=True)
        self.assertEqual(receipt['result'], 'PASS')
        self.assertFalse(any('shutdown' in call for call in calls))

    def test_wrong_arm64_platform_never_launched(self):
        calls, receipt = self.exercise(platform='IOS')
        self.assertEqual(receipt['result'], 'FAIL')
        self.assertFalse(any('spawn' in call for call in calls))

    def test_missing_marker_and_nonzero_exit_cannot_pass(self):
        for options in [{'marker': False}, {'failed': True}]:
            with self.subTest(options=options):
                calls, receipt = self.exercise(**options)
                self.assertEqual(receipt['result'], 'FAIL')
                self.assertIn('error', receipt)
                self.assertTrue(any('shutdown' in call for call in calls))


if __name__ == '__main__':
    unittest.main()
