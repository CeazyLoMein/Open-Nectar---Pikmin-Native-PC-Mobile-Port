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
    def setUp(self):
        # Expected negative fixtures must not look like real CI probe failures.
        self.print_guard = mock.patch('builtins.print')
        self.print_guard.start()
        self.addCleanup(self.print_guard.stop)

    def exercise(self, *, platform='IOSSIMULATOR', marker=True, failed=False, booted=False,
                 timeout=False, partial=None, boot_timeout=False, diagnostic_failure=False,
                 health=False, health_before_fail=False, health_after_fail=False,
                 health_platform='IOSSIMULATOR', native_text=None):
        calls = []
        health_calls = []

        def execute(*args, **kwargs):
            calls.append(args)
            if 'vtool' in args:
                return f'platform {health_platform if args[-1].endswith("health-probe") else platform}'
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
            if 'spawn' in args and args[-1].endswith('health-probe'):
                health_calls.append(args)
                if (len(health_calls) == 1 and health_before_fail) or (len(health_calls) > 1 and health_after_fail):
                    raise subprocess.TimeoutExpired(args, 20, output=b'health launch pending')
                return 'NECTAR_SIMULATOR_HEALTH_PASS\n'
            if 'spawn' in args:
                if timeout:
                    raise subprocess.TimeoutExpired(args, 90, output=partial)
                if failed:
                    raise RuntimeError('child process failed')
                if native_text is not None:
                    return native_text
                return ('NECTAR_COOP_SOCKET_PROBE_STARTED\nNECTAR_COOP_SOCKET_PROBE_PASS\n'
                        if marker else 'partial progress')
            return ''

        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            binary = base / 'probe'
            binary.write_bytes(b'fixture executable')
            companion = base / 'health-probe'
            companion.write_bytes(b'separate health executable')
            output = base / 'evidence'
            try:
                run(binary, output, execute, health_binary=companion if health else None)
            except (RuntimeError, AssertionError, subprocess.TimeoutExpired):
                pass
            receipt = json.loads((output / 'result.json').read_text())
            self.assertEqual(len(receipt['binary_sha256']), 64)
            self.health_calls = health_calls
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

    def test_independent_health_program_runs_before_real_probe(self):
        calls, receipt = self.exercise(health=True)
        self.assertEqual(receipt['result'], 'PASS')
        self.assertEqual(receipt['health_before_probe'], 'PASS')
        self.assertTrue(receipt['probe_entered_main_observed'])
        self.assertEqual(len(self.health_calls), 1)
        self.assertNotEqual(receipt['health_binary_sha256'], receipt['binary_sha256'])
        launches = [call[-1] for call in calls if 'spawn' in call and 'log' not in call]
        self.assertTrue(launches[0].endswith('health-probe'))
        self.assertTrue(launches[1].endswith('probe'))

    def test_unhealthy_simulator_fails_before_starting_real_probe(self):
        calls, receipt = self.exercise(health=True, health_before_fail=True)
        self.assertEqual(receipt['result'], 'FAIL')
        self.assertEqual(receipt['failed_stage'], 'health')
        self.assertEqual(receipt['failure_kind'], 'simulator_execution_unhealthy_before_probe')
        self.assertFalse(receipt['probe_entered_main_observed'])
        self.assertFalse(any('spawn' in call and call[-1].endswith('/probe') for call in calls))
        self.assertIn('health launch pending', self.logs['health-before-probe.log'])

    def test_wrong_platform_health_binary_never_runs(self):
        calls, receipt = self.exercise(health=True, health_platform='IOS')
        self.assertEqual(receipt['result'], 'FAIL')
        self.assertEqual(receipt['failed_stage'], 'health-platform')
        self.assertFalse(any('spawn' in call for call in calls))

    def test_empty_probe_timeout_and_failed_health_still_fail(self):
        _, receipt = self.exercise(health=True, timeout=True, health_after_fail=True)
        self.assertEqual(receipt['result'], 'FAIL')
        self.assertEqual(receipt['health_after_timeout'], 'FAIL')
        self.assertEqual(receipt['failure_kind'], 'probe_preentry_timeout_and_simulator_execution_unhealthy')
        self.assertEqual(len(self.health_calls), 2)
        self.assertFalse(receipt['probe_entered_main_observed'])

    def test_healthy_simulator_does_not_excuse_probe_launch_timeout(self):
        _, receipt = self.exercise(health=True, timeout=True)
        self.assertEqual(receipt['result'], 'FAIL')
        self.assertEqual(receipt['health_after_timeout'], 'PASS')
        self.assertEqual(receipt['failure_kind'], 'probe_preentry_timeout_with_healthy_simulator')
        self.assertEqual(len(self.health_calls), 2)

    def test_real_native_timeout_is_never_reclassified_as_infrastructure(self):
        _, receipt = self.exercise(health=True, timeout=True, health_after_fail=True,
            partial='NECTAR_COOP_SOCKET_PROBE_STARTED\nSTAGE native code\n')
        self.assertEqual(receipt['result'], 'FAIL')
        self.assertTrue(receipt['probe_entered_main_observed'])
        self.assertEqual(receipt['failure_kind'], 'native_probe_failed_or_incomplete')
        self.assertEqual(len(self.health_calls), 1)

    def test_health_pass_never_replaces_ordered_complete_real_probe(self):
        for text in ['NECTAR_COOP_SOCKET_PROBE_PASS\n',
                     'NECTAR_COOP_SOCKET_PROBE_PASS\nNECTAR_COOP_SOCKET_PROBE_STARTED\n',
                     'NECTAR_COOP_SOCKET_PROBE_STARTED\nFAIL native\nNECTAR_COOP_SOCKET_PROBE_PASS\n',
                     'NECTAR_COOP_SOCKET_PROBE_STARTED\nlabel: FAIL native\nNECTAR_COOP_SOCKET_PROBE_PASS\n']:
            with self.subTest(text=text):
                _, receipt = self.exercise(health=True, native_text=text)
                self.assertEqual(receipt['result'], 'FAIL')
                self.assertEqual(receipt['failure_kind'], 'native_probe_failed_or_incomplete')

    def test_command_nonzero_retains_full_output(self):
        result = subprocess.CompletedProcess(['probe'], 124,
            'NECTAR_COOP_SOCKET_PROBE_STARTED\nFAIL native deadline\n')
        with mock.patch('run_ios_coop_socket_probe.subprocess.run', return_value=result):
            with self.assertRaises(CommandFailed) as raised:
                command('probe', timeout=2)
        self.assertEqual(raised.exception.output, result.stdout)


if __name__ == '__main__':
    unittest.main()
