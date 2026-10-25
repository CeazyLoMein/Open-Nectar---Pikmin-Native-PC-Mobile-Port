"""Run the real socket/session CLI inside iOS Simulator, retaining exact evidence."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import time
import traceback

from run_ios_scene_smoke import select_device


def output_text(value):
    return value.decode('utf-8', errors='replace') if isinstance(value, bytes) else (value or '')


class CommandFailed(RuntimeError):
    def __init__(self, args, code, output):
        self.output = output_text(output)
        super().__init__(f'{args}: exit {code}\n{self.output}')


def command(*args, timeout=180):
    print('$ ' + ' '.join(map(str, args)), flush=True)
    result = subprocess.run(args, text=True, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, timeout=timeout)
    if result.returncode:
        raise CommandFailed(args, result.returncode, result.stdout)
    return result.stdout


def collect_failure(udid, output, execute):
    errors = []
    commands = [
        ('failure-simulator-state.json', ('xcrun', 'simctl', 'list', 'devices', 'available', '--json')),
        ('failure-probe-console.log', ('xcrun', 'simctl', 'spawn', udid, 'log', 'show',
             '--last', '2m', '--style', 'compact', '--predicate',
             'process == "nectar_net_coop_socket_probe"')),
    ]
    for name, args in commands:
        try:
            (output / name).write_text(execute(*args, timeout=15), encoding='utf-8')
        except Exception as error:
            partial = output_text(getattr(error, 'output', None))
            (output / name).write_text(partial, encoding='utf-8')
            errors.append(f'{name}: {error}')
    (output / 'diagnostic-errors.json').write_text(json.dumps(errors, indent=2), encoding='utf-8')


def run(binary, output, execute=command):
    output.mkdir(parents=True, exist_ok=True)
    receipt = {'result': 'FAIL', 'binary_sha256': hashlib.sha256(binary.read_bytes()).hexdigest(),
               'scope': 'iOS simulator encrypted loopback socket/session; no phone or campaign test'}
    udid = None
    started = False
    stage = "platform"
    begun = time.monotonic()
    try:
        # Both slices are ARM64. Architecture alone cannot distinguish them.
        platform = execute('xcrun', 'vtool', '-show-build', str(binary))
        (output / 'binary-platform.txt').write_text(platform)
        if 'IOSSIMULATOR' not in platform:
            raise AssertionError('Refusing a binary that is not built for iOS Simulator')
        stage = 'inventory'
        devices = json.loads(execute('xcrun', 'simctl', 'list', 'devices', 'available', '--json'))['devices']
        runtime, device = select_device(devices)
        udid = device['udid']
        receipt.update(runtime=runtime, device=device['name'])
        started = device['state'] != 'Booted'
        stage = 'boot'
        if started:
            execute('xcrun', 'simctl', 'boot', udid)
        execute('xcrun', 'simctl', 'bootstatus', udid, '-b')
        receipt['boot_completed'] = True
        stage = 'probe'
        (output / 'socket-session.log').write_text('', encoding='utf-8')
        text = execute('xcrun', 'simctl', 'spawn', udid, str(binary), timeout=90)
        (output / 'socket-session.log').write_text(text)
        print(text, flush=True)
        if 'NECTAR_COOP_SOCKET_PROBE_PASS' not in text or 'FAIL ' in text:
            raise AssertionError('Probe exited without its complete success marker')
        receipt['result'] = 'PASS'
    except Exception as error:
        partial = output_text(getattr(error, 'output', None))
        (output / 'last-command-output.log').write_text(partial, encoding='utf-8')
        if partial:
            print(partial, flush=True)
            if stage == 'probe':
                (output / 'socket-session.log').write_text(partial, encoding='utf-8')
        receipt['failed_stage'] = stage
        receipt['probe_entered_main_observed'] = 'NECTAR_COOP_SOCKET_PROBE_STARTED' in partial
        receipt['error'] = traceback.format_exc()
        (output / 'failure.txt').write_text(receipt['error'])
        if udid:
            collect_failure(udid, output, execute)
        raise
    finally:
        receipt['elapsed_seconds'] = round(time.monotonic() - begun, 3)
        (output / 'result.json').write_text(json.dumps(receipt, indent=2))
        if started and udid:
            try:
                execute('xcrun', 'simctl', 'shutdown', udid, timeout=20)
            except Exception:
                (output / 'cleanup-error.txt').write_text(traceback.format_exc())
    return receipt


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--binary', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    run(args.binary.resolve(), args.output.resolve())
