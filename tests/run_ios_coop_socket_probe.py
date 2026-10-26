"""Run the real socket/session CLI inside iOS Simulator, retaining exact evidence."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import time
import traceback

from run_ios_scene_smoke import select_device

HEALTH_MARKER = 'NECTAR_SIMULATOR_HEALTH_PASS'
START_MARKER = 'NECTAR_COOP_SOCKET_PROBE_STARTED'
PASS_MARKER = 'NECTAR_COOP_SOCKET_PROBE_PASS'


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


def health_check(binary, udid, output, execute, label):
    """A tiny separately linked program; no GNS/game/static initialization."""
    try:
        text = execute('xcrun', 'simctl', 'spawn', udid, str(binary), timeout=20)
        (output / f'{label}.log').write_text(text, encoding='utf-8')
        if HEALTH_MARKER not in text.splitlines():
            raise AssertionError('Simulator health program exited without exact completion marker')
    except Exception as error:
        partial = output_text(getattr(error, 'output', None))
        if partial:
            (output / f'{label}.log').write_text(partial, encoding='utf-8')
        (output / f'{label}-error.txt').write_text(traceback.format_exc(), encoding='utf-8')
        raise


def valid_probe_output(text):
    lines = text.splitlines()
    return (START_MARKER in lines and PASS_MARKER in lines and
            lines.index(START_MARKER) < lines.index(PASS_MARKER) and
            'FAIL ' not in text)


def run(binary, output, execute=command, *, health_binary=None):
    output.mkdir(parents=True, exist_ok=True)
    receipt = {'result': 'FAIL', 'binary_sha256': hashlib.sha256(binary.read_bytes()).hexdigest(),
               'scope': 'iOS simulator encrypted loopback socket/session; no phone or campaign test'}
    udid = None
    started = False
    stage = 'platform'
    begun = time.monotonic()
    try:
        platform = execute('xcrun', 'vtool', '-show-build', str(binary))
        (output / 'binary-platform.txt').write_text(platform, encoding='utf-8')
        if 'IOSSIMULATOR' not in platform:
            raise AssertionError('Refusing a binary that is not built for iOS Simulator')
        if health_binary is not None:
            stage = 'health-platform'
            receipt['health_binary_sha256'] = hashlib.sha256(health_binary.read_bytes()).hexdigest()
            platform = execute('xcrun', 'vtool', '-show-build', str(health_binary))
            (output / 'health-platform.txt').write_text(platform, encoding='utf-8')
            if 'IOSSIMULATOR' not in platform:
                raise AssertionError('Refusing wrong-platform simulator health binary')
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
        if health_binary is not None:
            stage = 'health'
            health_check(health_binary, udid, output, execute, 'health-before-probe')
            receipt['health_before_probe'] = 'PASS'
        stage = 'probe'
        (output / 'socket-session.log').write_text('', encoding='utf-8')
        text = execute('xcrun', 'simctl', 'spawn', udid, str(binary), timeout=90)
        (output / 'socket-session.log').write_text(text, encoding='utf-8')
        print(text, flush=True)
        receipt['probe_entered_main_observed'] = START_MARKER in text.splitlines()
        if not valid_probe_output(text):
            raise AssertionError('Probe exited without ordered startup/completion markers or reported FAIL')
        receipt['result'] = 'PASS'
    except Exception as error:
        partial = output_text(getattr(error, 'output', None))
        (output / 'last-command-output.log').write_text(partial, encoding='utf-8')
        if partial:
            print(partial, flush=True)
            if stage == 'probe':
                (output / 'socket-session.log').write_text(partial, encoding='utf-8')
        receipt['failed_stage'] = stage
        entered = receipt.get('probe_entered_main_observed', False) or START_MARKER in partial.splitlines()
        receipt['probe_entered_main_observed'] = entered
        if stage == 'health':
            receipt['failure_kind'] = 'simulator_execution_unhealthy_before_probe'
        elif stage == 'probe' and isinstance(error, subprocess.TimeoutExpired) and not entered:
            receipt['failure_kind'] = 'probe_preentry_timeout_unclassified'
            # A healthy separate executable means the actual probe/loader needs
            # investigation. Never turn an empty probe log into an infra pass.
            if health_binary is not None and udid:
                try:
                    health_check(health_binary, udid, output, execute, 'health-after-preentry-timeout')
                    receipt['health_after_timeout'] = 'PASS'
                    receipt['failure_kind'] = 'probe_preentry_timeout_with_healthy_simulator'
                except Exception:
                    receipt['health_after_timeout'] = 'FAIL'
                    receipt['failure_kind'] = 'probe_preentry_timeout_and_simulator_execution_unhealthy'
        elif stage == 'probe':
            receipt['failure_kind'] = 'native_probe_failed_or_incomplete'
        else:
            receipt['failure_kind'] = 'simulator_setup_or_platform_failed'
        receipt['error'] = traceback.format_exc()
        (output / 'failure.txt').write_text(receipt['error'], encoding='utf-8')
        if udid:
            collect_failure(udid, output, execute)
        raise
    finally:
        receipt['elapsed_seconds'] = round(time.monotonic() - begun, 3)
        (output / 'result.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
        if started and udid:
            try:
                execute('xcrun', 'simctl', 'shutdown', udid, timeout=20)
            except Exception:
                (output / 'cleanup-error.txt').write_text(traceback.format_exc(), encoding='utf-8')
    return receipt


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--binary', type=Path, required=True)
    parser.add_argument('--health-binary', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    run(args.binary.resolve(), args.output.resolve(), health_binary=args.health_binary.resolve())
