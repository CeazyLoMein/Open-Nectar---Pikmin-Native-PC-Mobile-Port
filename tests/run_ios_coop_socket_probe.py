"""Run the real socket/session CLI inside iOS Simulator, retaining exact evidence."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import time
import traceback
import uuid

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
             'process == "NectarCoopSocketProbe" OR process == "NectarCoopHealthProbe" OR process == "nectar_net_coop_socket_probe"')),
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


def create_owned_simulator(runtime, template, output, execute, borrowed_udids):
    """Use inventory only as a template; never erase/restart a borrowed device."""
    device_type = template.get('deviceTypeIdentifier')
    if not device_type:
        inventory = execute('xcrun', 'simctl', 'list', 'devicetypes', '--json', timeout=30)
        (output / 'device-types.json').write_text(inventory, encoding='utf-8')
        matches = [item['identifier'] for item in json.loads(inventory)['devicetypes']
                   if item['name'] == template['name']]
        if len(matches) != 1:
            raise AssertionError('No unique device type for selected simulator template')
        device_type = matches[0]
    name = 'Nectar-Coop-Socket-' + uuid.uuid4().hex[:12]
    text = execute('xcrun', 'simctl', 'create', name, device_type, runtime, timeout=45)
    (output / 'created-simulator.txt').write_text(text, encoding='utf-8')
    # Refuse ambiguous output before claiming ownership or issuing cleanup.
    created = str(uuid.UUID(text.strip()))
    if created.lower() in borrowed_udids:
        raise AssertionError('Create returned an existing borrowed device')
    return created


def verify_result(path, outcome):
    """Mandatory gate after independent compilation; health alone never passes."""
    if outcome != 'success':
        raise AssertionError('Native socket execution step did not succeed')
    receipt = json.loads(path.read_text(encoding='utf-8'))
    if not (receipt.get('result') == 'PASS' and receipt.get('health_before_probe') == 'PASS'
            and receipt.get('probe_entered_main_observed') is True
            and receipt.get('simulator_policy') == 'owned-disposable'
            and receipt.get('execution_mode') == 'uikit-app'):
        raise AssertionError('Missing complete owned-simulator native runtime evidence')
    uuid.UUID(receipt['simulator_udid'])
    for key in ['binary_sha256', 'health_binary_sha256']:
        value = receipt.get(key, '')
        if len(value) != 64 or any(c not in '0123456789abcdef' for c in value):
            raise AssertionError('Missing binary identity: ' + key)
    if not valid_probe_output((path.parent / 'socket-session.log').read_text(encoding='utf-8')):
        raise AssertionError('Actual native log is incomplete or failed')
    print('PASS: complete real encrypted iOS socket runtime; packaging may continue', flush=True)


def run(binary, output, execute=command, *, health_binary=None, isolated=True):
    output.mkdir(parents=True, exist_ok=True)
    receipt = {'result': 'FAIL', 'binary_sha256': hashlib.sha256(binary.read_bytes()).hexdigest(),
               'scope': 'iOS simulator encrypted loopback socket/session; no phone or campaign test',
               'simulator_policy': 'owned-disposable' if isolated else 'borrowed-fixture',
               'execution_mode': getattr(execute, 'execution_mode', 'cli-fixture'),
               'setup_attempts': []}
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
        (output / 'simulator-inventory.json').write_text(json.dumps(devices, indent=2), encoding='utf-8')
        runtime, device = select_device(devices)
        receipt.update(runtime=runtime, device=device['name'])
        stage = 'create'
        if isolated:
            if health_binary is None:
                raise AssertionError('Owned simulator requires independent health binary')
            borrowed = {item['udid'].lower() for items in devices.values() for item in items}
            udid = create_owned_simulator(runtime, device, output, execute, borrowed)
            started = True
        else:
            # Explicit opt-out for old host fixtures only; CLI always isolates.
            udid = device['udid']
            started = device['state'] != 'Booted'
        receipt['simulator_udid'] = udid
        for attempt in range(1, 3 if isolated else 2):
            setup = {'number': attempt, 'result': 'FAIL'}
            receipt['setup_attempts'].append(setup)
            setup_output = output / f'setup-attempt-{attempt}' if isolated else output
            setup_output.mkdir(exist_ok=True)
            try:
                stage = 'boot'
                if started:
                    execute('xcrun', 'simctl', 'boot', udid)
                execute('xcrun', 'simctl', 'bootstatus', udid, '-b')
                receipt['boot_completed'] = True
                if health_binary is not None:
                    stage = 'health'
                    health_check(health_binary, udid, setup_output, execute, 'health-before-probe')
                    receipt['health_before_probe'] = 'PASS'
                setup['result'] = 'PASS'
                if attempt > 1:
                    receipt['setup_recovered'] = True
                break
            except Exception as error:
                setup.update(failed_stage=stage, error=traceback.format_exc())
                # Exactly one recovery for a timed-out SETUP, before any native
                # probe executes. Never retry native failures or relax its gate.
                if not (isolated and attempt == 1 and isinstance(error, subprocess.TimeoutExpired)):
                    raise
                collect_failure(udid, setup_output, execute)
                stage = 'setup-recovery'
                execute('xcrun', 'simctl', 'shutdown', udid, timeout=20)
                receipt['setup_recovery_attempted'] = True
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
        if started and udid:
            errors = []
            commands = [('shutdown', udid)] + ([('delete', udid)] if isolated else [])
            for args in commands:
                try:
                    execute('xcrun', 'simctl', *args, timeout=20)
                except Exception:
                    errors.append(traceback.format_exc())
            receipt['cleanup_errors'] = errors
            if errors:
                (output / 'cleanup-error.txt').write_text('\n'.join(errors), encoding='utf-8')
        (output / 'result.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
    return receipt


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--app', type=Path)
    parser.add_argument('--health-app', type=Path)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--verify', type=Path)
    parser.add_argument('--outcome')
    args = parser.parse_args()
    if args.verify:
        verify_result(args.verify.resolve(), args.outcome)
    else:
        if not (args.app and args.health_app and args.output):
            parser.error('--app, --health-app and --output are required for execution')
        from ios_coop_app_executor import AppExecutor, validate_app
        app, health_app, output = args.app.resolve(), args.health_app.resolve(), args.output.resolve()
        binary, _ = validate_app(app,'socket')
        health_binary, _ = validate_app(health_app,'health')
        execute = AppExecutor(app,health_app,output,command)
        run(binary,output,execute,health_binary=health_binary)
