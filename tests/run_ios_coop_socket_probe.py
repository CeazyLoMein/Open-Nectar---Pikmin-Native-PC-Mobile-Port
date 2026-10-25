"""Run the real socket/session CLI inside iOS Simulator, retaining exact evidence."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import traceback

from run_ios_scene_smoke import select_device


def command(*args, timeout=180):
    result = subprocess.run(args, text=True, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, timeout=timeout)
    if result.returncode:
        raise RuntimeError(f'{args}: exit {result.returncode}\n{result.stdout}')
    return result.stdout


def run(binary, output, execute=command):
    output.mkdir(parents=True, exist_ok=True)
    receipt = {'result': 'FAIL', 'binary_sha256': hashlib.sha256(binary.read_bytes()).hexdigest(),
               'scope': 'iOS simulator encrypted loopback socket/session; no phone or campaign test'}
    udid = None
    started = False
    try:
        # Both slices are ARM64. Architecture alone cannot distinguish them.
        platform = execute('xcrun', 'vtool', '-show-build', str(binary))
        (output / 'binary-platform.txt').write_text(platform)
        if 'IOSSIMULATOR' not in platform:
            raise AssertionError('Refusing a binary that is not built for iOS Simulator')
        devices = json.loads(execute('xcrun', 'simctl', 'list', 'devices', 'available', '--json'))['devices']
        runtime, device = select_device(devices)
        udid = device['udid']
        receipt.update(runtime=runtime, device=device['name'])
        started = device['state'] != 'Booted'
        if started:
            execute('xcrun', 'simctl', 'boot', udid)
        execute('xcrun', 'simctl', 'bootstatus', udid, '-b')
        text = execute('xcrun', 'simctl', 'spawn', udid, str(binary), timeout=90)
        (output / 'socket-session.log').write_text(text)
        print(text, flush=True)
        if 'NECTAR_COOP_SOCKET_PROBE_PASS' not in text or 'FAIL ' in text:
            raise AssertionError('Probe exited without its complete success marker')
        receipt['result'] = 'PASS'
    except Exception:
        receipt['error'] = traceback.format_exc()
        (output / 'failure.txt').write_text(receipt['error'])
        raise
    finally:
        (output / 'result.json').write_text(json.dumps(receipt, indent=2))
        if started and udid:
            try:
                execute('xcrun', 'simctl', 'shutdown', udid)
            except Exception:
                (output / 'cleanup-error.txt').write_text(traceback.format_exc())
    return receipt


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--binary', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    run(args.binary.resolve(), args.output.resolve())
