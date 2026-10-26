"""Owned simulator recovery and final-gate failures; no Apple runtime claim."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest import mock

from run_ios_coop_socket_probe import run, verify_result, CommandFailed

TEMPLATE = '00000000-0000-4000-8000-000000000001'
OTHER = '00000000-0000-4000-8000-000000000002'
OWNED = '00000000-0000-4000-8000-000000000003'
RUNTIME = 'com.apple.CoreSimulator.SimRuntime.iOS-27-1'
DEVICE_TYPE = 'com.apple.CoreSimulator.SimDeviceType.iPhone-test'


class Simulator:
    def __init__(self, *, health_timeouts=0, native='pass', fallback_type=False,
                 created=OWNED, health_marker=True, recovery_fails=False, cleanup_fails=False,
                 boot_timeouts=0):
        self.calls = []
        self.health_timeouts, self.boot_timeouts = health_timeouts, boot_timeouts
        self.native, self.fallback_type, self.created = native, fallback_type, created
        self.health_marker = health_marker
        self.recovery_fails, self.cleanup_fails = recovery_fails, cleanup_fails
        self.native_calls = self.health_calls = self.boot_calls = 0

    def __call__(self, *args, **kwargs):
        self.calls.append(args)
        if 'vtool' in args:
            return 'platform IOSSIMULATOR'
        if args[2:4] == ('list', 'devices'):
            device = {'name': 'iPhone test', 'udid': TEMPLATE, 'state': 'Booted', 'isAvailable': True}
            if not self.fallback_type:
                device['deviceTypeIdentifier'] = DEVICE_TYPE
            return json.dumps({'devices': {RUNTIME: [device,
                {'name': 'iPhone other', 'udid': OTHER, 'state': 'Shutdown', 'isAvailable': True}]}})
        if args[2:4] == ('list', 'devicetypes'):
            return json.dumps({'devicetypes': [{'name': 'iPhone test', 'identifier': DEVICE_TYPE}]})
        if args[2] == 'create':
            assert args[3].startswith('Nectar-Coop-Socket-')
            assert args[4:] == (DEVICE_TYPE, RUNTIME)
            return self.created + '\n'
        # Every boot, spawn, shutdown and delete must address the owned UUID.
        assert args[3] == OWNED, 'Borrowed simulator was mutated: ' + repr(args)
        if args[2] == 'bootstatus':
            self.boot_calls += 1
            if self.boot_calls <= self.boot_timeouts:
                raise subprocess.TimeoutExpired(args, 180, output='first boot stalled')
        if args[2] == 'spawn':
            if args[4] == 'log':
                return 'console diagnostic'
            if args[-1].endswith('health-probe'):
                self.health_calls += 1
                if self.health_calls <= self.health_timeouts:
                    raise subprocess.TimeoutExpired(args, 20, output=b'health timed out')
                return 'NECTAR_SIMULATOR_HEALTH_PASS\n' if self.health_marker else 'wrong marker\n'
            self.native_calls += 1
            if self.native in ('preentry-timeout', 'native-timeout'):
                partial = b'NECTAR_COOP_SOCKET_PROBE_STARTED\n' if self.native == 'native-timeout' else b''
                raise subprocess.TimeoutExpired(args, 90, output=partial)
            if self.native == 'exit-failure':
                raise CommandFailed(args, 1, 'NECTAR_COOP_SOCKET_PROBE_STARTED\nFAIL native\n')
            return 'NECTAR_COOP_SOCKET_PROBE_STARTED\nNECTAR_COOP_SOCKET_PROBE_PASS\n'
        if args[2] == 'shutdown' and (self.cleanup_fails or (self.recovery_fails and not self.native_calls)):
            raise subprocess.TimeoutExpired(args, 20, output=b'shutdown timed out')
        return ''


class OwnedRunnerTests(unittest.TestCase):
    def exercise(self, **options):
        sim = Simulator(**options)
        with tempfile.TemporaryDirectory() as folder, mock.patch('builtins.print'):
            root = Path(folder)
            binary, health, output = root/'probe', root/'health-probe', root/'evidence'
            binary.write_bytes(b'actual-probe-fixture');health.write_bytes(b'independent-health-fixture')
            error = None
            try:
                run(binary, output, sim, health_binary=health)
            except (RuntimeError, AssertionError, ValueError, subprocess.TimeoutExpired) as caught:
                error = caught
            receipt = json.loads((output/'result.json').read_text())
            gate = False
            if receipt['result'] == 'PASS':
                verify_result(output/'result.json', 'success')
                gate = True
            return sim, receipt, error, gate, {p.relative_to(output).as_posix():p.read_text()
                for p in output.rglob('*') if p.is_file()}

    def test_default_creates_new_device_even_with_booted_template(self):
        sim, receipt, error, gate, _ = self.exercise()
        self.assertIsNone(error);self.assertTrue(gate)
        self.assertEqual(receipt['simulator_udid'], OWNED)
        self.assertEqual(receipt['simulator_policy'], 'owned-disposable')
        self.assertEqual(sim.native_calls, 1)
        self.assertEqual(len(receipt['setup_attempts']), 1)
        self.assertEqual(receipt['cleanup_errors'], [])
        self.assertEqual(sim.calls[-2:], [('xcrun','simctl','shutdown',OWNED),('xcrun','simctl','delete',OWNED)])

    def test_inventory_without_type_resolves_exact_template_name(self):
        sim, receipt, error, gate, logs = self.exercise(fallback_type=True)
        self.assertTrue(gate);self.assertIsNone(error)
        self.assertIn('device-types.json', logs)

    def test_one_health_setup_timeout_recovers_before_exactly_one_native_run(self):
        sim, receipt, error, gate, logs = self.exercise(health_timeouts=1)
        self.assertIsNone(error);self.assertTrue(gate)
        self.assertEqual(sim.native_calls, 1)
        self.assertEqual([a['result'] for a in receipt['setup_attempts']], ['FAIL','PASS'])
        self.assertTrue(receipt['setup_recovered'])
        self.assertIn('setup-attempt-1/health-before-probe-error.txt', logs)
        self.assertIn('setup-attempt-1/diagnostic-errors.json', logs)
        self.assertIn('setup-attempt-2/health-before-probe.log', logs)

    def test_two_health_timeouts_fail_and_never_execute_native(self):
        sim, receipt, error, gate, _ = self.exercise(health_timeouts=2)
        self.assertIsNotNone(error);self.assertFalse(gate)
        self.assertEqual(receipt['result'], 'FAIL');self.assertEqual(sim.native_calls, 0)
        self.assertEqual(len(receipt['setup_attempts']), 2)
        self.assertEqual(receipt['failed_stage'], 'health')
        self.assertTrue(receipt['setup_recovery_attempted'])
        self.assertNotIn('setup_recovered', receipt)

    def test_boot_timeout_recovery_is_also_bounded_before_native(self):
        sim, receipt, error, gate, _ = self.exercise(boot_timeouts=1)
        self.assertTrue(gate);self.assertEqual(sim.native_calls, 1)
        self.assertEqual(receipt['setup_attempts'][0]['failed_stage'], 'boot')
        sim, receipt, error, gate, _ = self.exercise(boot_timeouts=2)
        self.assertFalse(gate);self.assertEqual(sim.native_calls, 0)
        self.assertEqual(len(receipt['setup_attempts']), 2)

    def test_native_failure_or_timeout_is_never_retried(self):
        for native in ['exit-failure','native-timeout','preentry-timeout']:
            with self.subTest(native=native):
                sim, receipt, error, gate, _ = self.exercise(native=native)
                self.assertFalse(gate);self.assertIsNotNone(error)
                self.assertEqual(sim.native_calls, 1)
                self.assertEqual(len(receipt['setup_attempts']), 1)
                self.assertNotIn('setup_recovered', receipt)

    def test_wrong_health_marker_is_failure_without_recovery(self):
        sim, receipt, error, gate, _ = self.exercise(health_marker=False)
        self.assertFalse(gate);self.assertEqual(sim.native_calls, 0)
        self.assertEqual(sim.health_calls, 1)
        self.assertNotIn('setup_recovered', receipt)

    def test_failed_recovery_shutdown_stops_before_native(self):
        sim, receipt, error, gate, _ = self.exercise(health_timeouts=1, recovery_fails=True)
        self.assertFalse(gate);self.assertEqual(sim.native_calls, 0)
        self.assertEqual(receipt['failed_stage'], 'setup-recovery')

    def test_ambiguous_or_borrowed_create_result_never_mutates_any_device(self):
        for created in [TEMPLATE, OTHER, 'not-a-uuid', OWNED+'\n'+OTHER]:
            with self.subTest(created=created):
                sim, receipt, error, gate, _ = self.exercise(created=created)
                self.assertFalse(gate);self.assertIsNotNone(error)
                self.assertFalse(any(call[2] in ('boot','shutdown','delete','spawn') for call in sim.calls))

    def test_cleanup_failure_is_reported_without_erasing_runtime_evidence(self):
        sim, receipt, error, gate, logs = self.exercise(cleanup_fails=True)
        self.assertTrue(gate);self.assertIsNone(error)
        self.assertTrue(receipt['cleanup_errors'])
        self.assertIn('cleanup-error.txt', logs)
        self.assertEqual(sim.calls[-1], ('xcrun','simctl','delete',OWNED))

    def test_packaging_gate_rejects_waived_failed_missing_or_partial_evidence(self):
        with tempfile.TemporaryDirectory() as folder, mock.patch('builtins.print'):
            root=Path(folder);binary=root/'probe';health=root/'health-probe'
            binary.write_bytes(b'probe');health.write_bytes(b'health')
            output=root/'evidence';run(binary, output, Simulator(), health_binary=health)
            result=output/'result.json';baseline=json.loads(result.read_text())
            for outcome in ['failure','skipped',None]:
                with self.assertRaises(AssertionError):verify_result(result,outcome)
            for changes in [{'result':'FAIL'},{'health_before_probe':'FAIL'},
                            {'probe_entered_main_observed':False},{'simulator_policy':'borrowed-fixture'},
                            {'binary_sha256':''},{'health_binary_sha256':''}]:
                result.write_text(json.dumps(dict(baseline,**changes)))
                with self.assertRaises(AssertionError):verify_result(result,'success')
            result.write_text(json.dumps(baseline))
            (output/'socket-session.log').write_text('NECTAR_COOP_SOCKET_PROBE_PASS\n')
            with self.assertRaises(AssertionError):verify_result(result,'success')


if __name__ == '__main__':
    unittest.main()
