"""Checks that iOS runtime evidence cannot become a false success."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
import subprocess
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tests'))
from run_ios_coop_socket_probe import run, command, CommandFailed


class RunnerTest(unittest.TestCase):
    def exercise(self, *, platform='IOSSIMULATOR', marker=True, failed=False, booted=False,
                 timeout=False, partial=None, boot_timeout=False, diagnostic_failure=False):
        calls = []

        def execute(*args, **kwargs):
            calls.append(args)
            if 'vtool' in args:
                return f'platform {platform}'
            if 'list' in args:
                return json.dumps({'devices': {'com.apple.CoreSimulator.SimRuntime.iOS-27-1': [
                    {'name': 'iPhone probe', 'udid': 'test-only', 'isAvailable': True,
                     'state': 'Booted' if booted else 'Shutdown'}]}})
            if 'bootstatus' in args and boot_timeout:
                raise subprocess.TimeoutExpired(args, 180, output=b'BOOT progress before timeout')
            if 'spawn' in args and 'log' in args:
                if diagnostic_failure:
                    raise RuntimeError('diagnostic unavailable')
                return 'filtered console'
            if 'spawn' in args:
                if timeout:
                    raise subprocess.TimeoutExpired(args, 90, output=partial)
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
            except (RuntimeError, AssertionError, subprocess.TimeoutExpired):
                pass
            receipt = json.loads((output / 'result.json').read_text())
            self.assertEqual(len(receipt['binary_sha256']), 64)
            self.logs = {p.name: p.read_text(encoding='utf-8') for p in output.iterdir() if p.is_file()}
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


    def test_timeout_preserves_partial_native_progress(self):
        partial = 'NECTAR_COOP_SOCKET_PROBE_STARTED\nPASS initial gate\nSTAGE private room creation\n'
        for value in [partial, partial.encode('utf-8')]:
            with self.subTest(kind=type(value).__name__):
                _, receipt = self.exercise(timeout=True, partial=value)
                self.assertEqual(receipt['result'], 'FAIL')
                self.assertEqual(receipt['failed_stage'], 'probe')
                self.assertTrue(receipt['probe_entered_main_observed'])
                self.assertEqual(self.logs['socket-session.log'], partial)
                self.assertEqual(self.logs['last-command-output.log'], partial)
                self.assertIn('failure-probe-console.log', self.logs)

    def test_timeout_without_output_does_not_claim_native_entry(self):
        _, receipt = self.exercise(timeout=True)
        self.assertEqual(receipt['result'], 'FAIL')
        self.assertFalse(receipt['probe_entered_main_observed'])
        self.assertEqual(self.logs['socket-session.log'], '')

    def test_boot_timeout_retains_phase_even_when_diagnostics_fail(self):
        _, receipt = self.exercise(boot_timeout=True, diagnostic_failure=True)
        self.assertEqual(receipt['failed_stage'], 'boot')
        self.assertNotIn('boot_completed', receipt)
        self.assertIn('TimeoutExpired', receipt['error'])
        self.assertIn('diagnostic unavailable', self.logs['diagnostic-errors.json'])
        self.assertEqual(self.logs['last-command-output.log'], 'BOOT progress before timeout')

    def test_command_nonzero_retains_full_output(self):
        result = subprocess.CompletedProcess(['probe'], 124,
            'NECTAR_COOP_SOCKET_PROBE_STARTED\nFAIL native deadline\n')
        with mock.patch('run_ios_coop_socket_probe.subprocess.run', return_value=result):
            with self.assertRaises(CommandFailed) as raised:
                command('probe', timeout=2)
        self.assertEqual(raised.exception.output, result.stdout)


if __name__ == '__main__':
    unittest.main()
