"""Verify the shipped P1 room screen metadata and exact networking notices."""
import argparse
import hashlib
from pathlib import Path
import plistlib


def verify(app, licenses, variant="standard"):
    info = plistlib.loads((app / 'Info.plist').read_bytes())
    expected = 'org.opennectar.experimental.pikmin1' + ('.solotest' if variant == 'solo-test' else '')
    if info['CFBundleIdentifier'] != expected:
        raise ValueError('Room prototype must preserve the normal P1 update identity')
    if not info.get('NSLocalNetworkUsageDescription', '').strip():
        raise ValueError('Missing local-network permission explanation')
    for name in ['OpenSSL.txt', 'protobuf.txt', 'GameNetworkingSockets.txt']:
        shipped = app / 'Licenses' / name
        original = licenses / name
        if not shipped.is_file() or not original.is_file():
            raise ValueError('Networking notice missing: ' + name)
        if hashlib.sha256(shipped.read_bytes()).digest() != hashlib.sha256(original.read_bytes()).digest():
            raise ValueError('Networking notice differs from pinned dependency: ' + name)
    print('PASS P1 room bundle: original app identity, local-network explanation and all original dependency notices')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--app', type=Path, required=True)
    parser.add_argument('--licenses', type=Path, required=True)
    parser.add_argument('--variant', choices=['standard', 'solo-test', 'solo-update'], default='standard')
    args = parser.parse_args()
    verify(args.app, args.licenses, args.variant)
