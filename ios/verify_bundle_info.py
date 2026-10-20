"""Validate configured iOS app metadata before compilation and IPA packaging."""
import argparse
from pathlib import Path
import plistlib
import re


def validate(plist_path, game, require_binary=False):
    with Path(plist_path).open('rb') as stream:
        info = plistlib.load(stream)
    expected = {
        'CFBundleExecutable': f'Nectar-{game}',
        'CFBundleIdentifier': f'org.opennectar.experimental.{game}',
        'CFBundleDisplayName': f'Open Nectar Pikmin {1 if game == "pikmin1" else 2}',
        'CFBundlePackageType': 'APPL',
    }
    for key, value in expected.items():
        if info.get(key) != value:
            raise ValueError(f'{key}: expected {value!r}, got {info.get(key)!r}')

    def check_values(value):
        if isinstance(value, str) and re.search(r'\$\([^)]*\)|\$\{[^}]*\}|@[A-Z][A-Z0-9_]*@', value):
            raise ValueError(f'Unresolved build placeholder: {value!r}')
        if isinstance(value, dict):
            for item in value.values():
                check_values(item)
        elif isinstance(value, list):
            for item in value:
                check_values(item)
    check_values(info)
    if require_binary:
        binary = Path(plist_path).parent / expected['CFBundleExecutable']
        if not binary.is_file() or binary.stat().st_size == 0:
            raise ValueError(f'Bundle executable missing or empty: {binary}')
    return info


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('plist', type=Path)
    parser.add_argument('--game', required=True, choices=['pikmin1', 'pikmin2'])
    parser.add_argument('--require-binary', action='store_true')
    args = parser.parse_args()
    try:
        info = validate(args.plist, args.game, args.require_binary)
    except (ValueError, OSError, plistlib.InvalidFileException) as error:
        parser.exit(1, f'iOS bundle validation failed: {error}\n')
    print(f'Validated {args.game} metadata: {info["CFBundleExecutable"]}')
