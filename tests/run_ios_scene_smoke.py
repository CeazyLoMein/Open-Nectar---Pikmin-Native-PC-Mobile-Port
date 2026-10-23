"""Launch the shared SDL scene entry on a disposable CI simulator; no game assets."""
from pathlib import Path
import argparse
import json
import plistlib
import re
import shutil
import subprocess
import time
import traceback

BUNDLE = 'org.opennectar.tests.scene'
PROCESS = 'NectarSceneSmoke'


def command(*args):
    print('$ ' + ' '.join(map(str, args)), flush=True)
    result = subprocess.run(args, text=True, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, timeout=180)
    print(result.stdout, flush=True)
    if result.returncode:
        raise RuntimeError(f'Command failed ({result.returncode}): {args}')
    return result.stdout.strip()


def select_device(devices):
    choices = []
    for runtime, items in devices.items():
        version = re.search(r'\.iOS-(\d+(?:-\d+)*)$', runtime)
        if not version:
            continue
        numbers = tuple(map(int, version[1].split('-')))
        if numbers[0] != 27:
            continue
        for device in items:
            if device.get('isAvailable') and device['name'].startswith('iPhone'):
                choices.append((numbers, device['state'] == 'Booted', runtime, device))
    assert choices, 'No available iOS27 iPhone simulator; cannot claim a runtime pass'
    # Exercise the newest installed runtime, including 27.1, rather than whichever
    # older runtime happens to appear first. Boot state only breaks version ties.
    _, _, runtime, device = max(choices, key=lambda row: (row[0], row[1]))
    return runtime, device


def read_report(path):
    text = path.read_text(encoding='utf-8', errors='replace')
    prefix = 'NECTAR_PROBE_STATE '
    # Read the last complete report, ignoring a partially written final line
    # and any unrelated process output. Keep ordinary JSON evidence readable.
    for line in reversed(text.splitlines()):
        if line.startswith(prefix):
            try:
                state = json.loads(line[len(prefix):])
            except json.JSONDecodeError:
                continue
            if isinstance(state, dict):
                return state
    state = json.loads(text)
    if not isinstance(state, dict):
        raise ValueError('Probe report must be a JSON object')
    return state


def await_state(path, predicate, label, seconds=30):
    deadline = time.monotonic() + seconds
    last = {}
    while time.monotonic() < deadline:
        try:
            last = read_report(path)
        except (OSError, ValueError):
            pass
        else:
            if last.get('error'):
                raise AssertionError(f'{label} failed: {last}')
            if predicate(last):
                return last
        time.sleep(.2)
    raise AssertionError(f'{label} timed out; last report={last}')


def collect_diagnostics(udid, output, since, report_path, roots=None):
    """Each diagnostic is independent: one failure must not hide the others."""
    failures = []
    if report_path and report_path.exists():
        try:
            state = read_report(report_path)
            (output / 'scene-smoke-last-report.json').write_text(json.dumps(state, indent=2))
        except (OSError, ValueError) as error:
            failures.append(f'Last report parsing: {error}')
    roots = roots if roots is not None else [
        Path.home() / 'Library/Logs/DiagnosticReports',
        Path.home() / 'Library/Developer/CoreSimulator/Devices' / udid / 'data/Library/Logs/CrashReporter',
    ]
    for index, root in enumerate(roots):
        try:
            for path in root.glob(PROCESS + '*'):
                if path.is_file() and path.stat().st_mtime >= since - 5:
                    shutil.copy2(path, output / f'crash-{index}-{path.name}')
        except OSError as error:
            failures.append(f'Crash report collection: {error}')
    for filename, args in [
        ('scene-smoke-console.log', ['xcrun', 'simctl', 'spawn', udid, 'log', 'show', '--last', '5m', '--style', 'compact', '--predicate', f'process == "{PROCESS}"']),
        ('scene-smoke-processes.log', ['xcrun', 'simctl', 'spawn', udid, 'launchctl', 'list']),
    ]:
        try:
            with (output / filename).open('w') as stream:
                result = subprocess.run(args, stdout=stream, stderr=subprocess.STDOUT, timeout=45)
                if result.returncode:
                    failures.append(f'{filename}: exit {result.returncode}')
        except (OSError, subprocess.TimeoutExpired) as error:
            failures.append(f'{filename}: {error}')
    (output / 'diagnostic-collection.json').write_text(json.dumps({'errors': failures}, indent=2))


def run_probe(app, output, execute=command):
    output = output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    since = time.time()
    # Preserve the actual compiled probe and metadata even if it never enters SDL.
    shutil.make_archive(str(output / 'scene-smoke-built-app'), 'zip', app.parent, app.name)
    symbols = app.parent / (app.name + '.dSYM')
    if symbols.is_dir():
        shutil.make_archive(str(output / 'scene-smoke-symbols'), 'zip', symbols.parent, symbols.name)
    info = plistlib.loads((app / 'Info.plist').read_bytes())
    assert info['CFBundleIdentifier'] == BUNDLE
    (output / 'scene-smoke-bundle-info.json').write_text(json.dumps(info, indent=2))
    devices = json.loads(execute('xcrun', 'simctl', 'list', 'devices', 'available', '--json'))['devices']
    (output / 'simulator-inventory.json').write_text(json.dumps(devices, indent=2))
    runtime, device = select_device(devices)
    udid = device['udid']
    started = device['state'] != 'Booted'
    report_path = None
    stage = 'boot'
    try:
        if started:
            execute('xcrun', 'simctl', 'boot', udid)
        execute('xcrun', 'simctl', 'bootstatus', udid, '-b')
        stage = 'install'
        execute('xcrun', 'simctl', 'install', udid, str(app))
        # Read the native report through stdout redirected to this known host
        # path. No app-container query is needed (Build49 timed out there).
        report_path = output / 'scene-smoke-stdout.log'
        report_path.write_text('')
        stage = 'launch'
        launch = execute('xcrun', 'simctl', 'launch',
                         '--stdout=' + str(output / 'scene-smoke-stdout.log'),
                         '--stderr=' + str(output / 'scene-smoke-stderr.log'), udid, BUNDLE)
        stage = 'scene startup'
        first = await_state(report_path, lambda state: state.get('ready') and state.get('active'), stage)
        assert first['entry_count'] == 1 and first['window_has_scene'], first
        assert first['scene_delegate'] == 'NectarSDLSceneDelegate', first
        assert first['width'] > first['height'] > 0, first
        assert first['reconnect_preserved_window'] and first['foreign_events_ignored'], first
        keys = ['will_background', 'did_background', 'will_foreground', 'did_foreground']
        initial = {key: first[key] for key in keys}
        stage = 'background'
        execute('xcrun', 'simctl', 'launch', udid, 'com.apple.Preferences')
        background = await_state(report_path, lambda state: state.get('did_background', 0) > initial['did_background'], stage)
        for key in ['will_background', 'did_background']:
            assert background[key] == initial[key] + 1, background
        stage = 'resume'
        resumed_launch = execute('xcrun', 'simctl', 'launch', udid, BUNDLE)
        assert launch.rsplit(':', 1)[-1].strip() == resumed_launch.rsplit(':', 1)[-1].strip(), 'Resume restarted the process'
        final = await_state(report_path, lambda state: state.get('active') and state.get('did_foreground', 0) > initial['did_foreground'], stage)
        assert final['entry_count'] == 1 and final['reconnect_preserved_window'], final
        for key in keys:
            assert final[key] == initial[key] + 1, final
        result = {'result': 'PASS', 'runtime': runtime, 'device': device['name'], 'initial': first,
                  'background': background, 'resumed': final, 'launch': launch, 'resumed_launch': resumed_launch}
        (output / 'scene-smoke-result.json').write_text(json.dumps(result, indent=2))
        print('PASS: actual SDL/UIKit scene startup and background/resume; one entry/window and no duplicate SDL events.', flush=True)
        return result
    except Exception:
        (output / 'scene-smoke-failure.json').write_text(json.dumps({
            'result': 'FAIL', 'stage': stage, 'runtime': runtime,
            'device': device['name'], 'traceback': traceback.format_exc()}, indent=2))
        raise
    finally:
        try:
            collect_diagnostics(udid, output, since, report_path)
        except Exception:
            (output / 'diagnostic-collection-exception.txt').write_text(traceback.format_exc())
        # Never mask the test result if diagnostic collection or cleanup fails.
        for args in [('terminate', udid, BUNDLE)] + ([('shutdown', udid)] if started else []):
            try:
                subprocess.run(['xcrun', 'simctl', *args], stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, timeout=45)
            except (OSError, subprocess.TimeoutExpired):
                pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--build-root', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    apps = list(args.build_root.rglob('NectarSceneSmoke.app'))
    assert len(apps) == 1, apps
    run_probe(apps[0], args.output)


if __name__ == '__main__':
    main()
