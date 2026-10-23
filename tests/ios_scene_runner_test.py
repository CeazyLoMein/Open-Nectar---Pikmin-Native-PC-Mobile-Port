"""Host regressions for simulator orchestration/diagnostics, not UIKit proof."""
from pathlib import Path
from types import SimpleNamespace
from unittest import TestCase, main, mock
import json
import contextlib
import io
import os
import plistlib
import subprocess
import tempfile
import time
import zipfile
import run_ios_scene_smoke as runner


def devices():
    return {
        'com.apple.CoreSimulator.SimRuntime.iOS-27-0': [
            {'name': 'iPhone 18 Pro', 'udid': 'older', 'isAvailable': True, 'state': 'Booted'}],
        'com.apple.CoreSimulator.SimRuntime.iOS-27-1': [
            {'name': 'iPhone Duo', 'udid': 'newer', 'isAvailable': True, 'state': 'Shutdown'}],
    }


class RunnerTests(TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def test_newest_runtime_beats_older_booted_device(self):
        runtime, device = runner.select_device(devices())
        self.assertTrue(runtime.endswith('27-1'))
        self.assertEqual(device['udid'], 'newer')

    def test_booted_device_breaks_equal_runtime_tie(self):
        inventory = devices()
        inventory[next(key for key in inventory if key.endswith('27-1'))].append(
            {'name': 'iPhone Duo', 'udid': 'booted-newer', 'isAvailable': True, 'state': 'Booted'})
        self.assertEqual(runner.select_device(inventory)[1]['udid'], 'booted-newer')

    def test_unavailable_or_wrong_os_does_not_fake_runtime_pass(self):
        inventory = {'com.apple.CoreSimulator.SimRuntime.iOS-26-0': devices()[next(iter(devices()))]}
        with self.assertRaisesRegex(AssertionError, 'No available iOS27'):
            runner.select_device(inventory)

    def test_explicit_native_error_keeps_phase(self):
        report = self.root / 'report.json'
        report.write_text(json.dumps({'phase': 'before-sdl-init', 'error': 'Native exception'}))
        with self.assertRaisesRegex(AssertionError, 'before-sdl-init'):
            runner.await_state(report, lambda state: state.get('ready'), 'startup')

    def test_missing_report_fails_with_no_success_claim(self):
        with self.assertRaisesRegex(AssertionError, r'last report=\{\}'):
            runner.await_state(self.root / 'absent.json', lambda state: True, 'startup', seconds=0)

    def test_stdout_last_complete_state_survives_noise_and_partial_line(self):
        path = self.root / 'stdout.log'
        path.write_text('startup noise\nNECTAR_PROBE_STATE {"phase":"process-entry"}\n'
                        'NECTAR_PROBE_STATE {"ready":true,"phase":"running"}\n'
                        'NECTAR_PROBE_STATE {"ready":', encoding='utf-8')
        self.assertEqual(runner.read_report(path), {'ready': True, 'phase': 'running'})

    def test_stdout_native_error_still_fails_even_after_earlier_ready(self):
        path = self.root / 'stdout.log'
        path.write_text('NECTAR_PROBE_STATE {"ready":true}\n'
                        'NECTAR_PROBE_STATE {"error":"Native exception","phase":"resume"}\n', encoding='utf-8')
        with self.assertRaisesRegex(AssertionError, 'Native exception'):
            runner.await_state(path, lambda state: state.get('ready'), 'resume')

    def test_noise_is_not_a_success_report(self):
        path = self.root / 'stdout.log'
        path.write_text('application launched but no report\n')
        with self.assertRaises(ValueError):
            runner.read_report(path)

    def fixture(self, restart=False, error=False):
        app = self.root / 'NectarSceneSmoke.app'
        app.mkdir()
        (app / 'Info.plist').write_bytes(plistlib.dumps({'CFBundleIdentifier': runner.BUNDLE}))
        output = self.root / 'output'
        report = output / 'scene-smoke-stdout.log'
        history = []
        launches = 0
        state = {'entry_count': 1, 'ready': True, 'active': True, 'error': '',
                 'window_has_scene': True, 'scene_delegate': 'NectarSDLSceneDelegate',
                 'width': 932, 'height': 430, 'reconnect_preserved_window': True,
                 'foreign_events_ignored': True, 'will_background': 0, 'did_background': 0,
                 'will_foreground': 0, 'did_foreground': 0}

        def execute(*args):
            nonlocal launches
            history.append(args)
            operation = args[2]
            if operation == 'list':
                return json.dumps({'devices': devices()})
            if operation == 'get_app_container':
                raise AssertionError('Container lookup must not block startup')
            if operation == 'launch':
                if args[-1] == 'com.apple.Preferences':
                    state.update(active=False, will_background=1, did_background=1)
                else:
                    launches += 1
                    if launches == 1 and error:
                        state.update(ready=False, error='Observed failure', phase='before-sdl-init')
                    if launches > 1:
                        state.update(active=True, will_foreground=1, did_foreground=1)
                with report.open('a', encoding='utf-8') as stream:
                    stream.write('NECTAR_PROBE_STATE ' + json.dumps(state) + '\n')
                return args[-1] + ': ' + ('999' if restart and launches > 1 else '123')
            return ''
        return app, output, execute, history

    def test_complete_orchestration_retains_strict_assertions_and_raw_logs(self):
        app, output, execute, history = self.fixture()
        with mock.patch.object(runner, 'collect_diagnostics'), mock.patch.object(runner.subprocess, 'run'), contextlib.redirect_stdout(io.StringIO()):
            result = runner.run_probe(app, output, execute)
        self.assertEqual(result['result'], 'PASS')
        operations = [args[2] for args in history]
        self.assertNotIn('get_app_container', operations)
        launch = next(args for args in history if args[2] == 'launch')
        self.assertTrue(any(arg.startswith('--stderr=') for arg in launch))
        self.assertTrue(any(arg.startswith('--stdout=') for arg in launch))
        self.assertTrue((output / 'scene-smoke-result.json').exists())
        with zipfile.ZipFile(output / 'scene-smoke-built-app.zip') as archive:
            self.assertIsNone(archive.testzip())
            self.assertIn('NectarSceneSmoke.app/Info.plist', archive.namelist())

    def test_process_restart_still_fails_and_preserves_diagnostics(self):
        app, output, execute, _ = self.fixture(restart=True)
        with mock.patch.object(runner, 'collect_diagnostics') as collect, mock.patch.object(runner.subprocess, 'run'):
            with self.assertRaisesRegex(AssertionError, 'Resume restarted'):
                runner.run_probe(app, output, execute)
        collect.assert_called_once()
        self.assertEqual(json.loads((output / 'scene-smoke-failure.json').read_text())['stage'], 'resume')
        self.assertFalse((output / 'scene-smoke-result.json').exists())

    def test_collection_failure_does_not_mask_native_failure_or_cleanup(self):
        app, output, execute, _ = self.fixture(error=True)
        with mock.patch.object(runner, 'collect_diagnostics', side_effect=OSError('diagnostic failure')), \
             mock.patch.object(runner.subprocess, 'run') as cleanup:
            with self.assertRaisesRegex(AssertionError, 'Observed failure'):
                runner.run_probe(app, output, execute)
        self.assertEqual(cleanup.call_count, 2)  # terminate our app, shutdown our simulator
        self.assertTrue((output / 'diagnostic-collection-exception.txt').exists())
        self.assertEqual(json.loads((output / 'scene-smoke-failure.json').read_text())['stage'], 'scene startup')

    def test_scoped_crash_collection_survives_one_command_failure(self):
        root = self.root / 'crashes'
        root.mkdir()
        output = self.root / 'diagnostics'
        output.mkdir()
        for name in ['NectarSceneSmoke-current.ips', 'NectarSceneSmoke-old.ips', 'OtherApp.ips']:
            (root / name).write_text('sample')
        os.utime(root / 'NectarSceneSmoke-old.ips', (0, 0))
        with mock.patch.object(runner.subprocess, 'run', side_effect=[subprocess.TimeoutExpired('log', 45), SimpleNamespace(returncode=0)]) as run:
            runner.collect_diagnostics('own-simulator', output, time.time(), None, roots=[root])
        self.assertEqual(run.call_count, 2)
        self.assertTrue((output / 'crash-0-NectarSceneSmoke-current.ips').exists())
        self.assertFalse((output / 'crash-0-NectarSceneSmoke-old.ips').exists())
        self.assertFalse((output / 'crash-0-OtherApp.ips').exists())
        self.assertEqual(len(json.loads((output / 'diagnostic-collection.json').read_text())['errors']), 1)


if __name__ == '__main__':
    main()
