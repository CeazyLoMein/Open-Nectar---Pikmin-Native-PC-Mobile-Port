"""Validate configured iOS app metadata before compilation and IPA packaging."""
import argparse
from pathlib import Path
import plistlib
import re


def validate(plist_path, game, require_binary=False, variant="standard"):
    if variant not in ("standard", "solo-test", "solo-update") or (variant != "standard" and game != "pikmin1"):
        raise ValueError("Unsupported game/variant")
    with Path(plist_path).open('rb') as stream:
        info = plistlib.load(stream)
    expected = {
        'CFBundleExecutable': f'Nectar-{game}',
        'CFBundleIdentifier': f'org.opennectar.experimental.{game}',
        'CFBundleDisplayName': f'Pikmin {1 if game == "pikmin1" else 2}',
        'CFBundlePackageType': 'APPL',
    }
    if variant == "solo-test":
        expected.update(CFBundleExecutable="Nectar-pikmin1-solo-test",
                        CFBundleIdentifier="org.opennectar.experimental.pikmin1.solotest",
                        CFBundleDisplayName="P1 Solo Test")
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
    if info.get('CFBundleName') != expected['CFBundleDisplayName']:
        raise ValueError('CFBundleName must match the short app label')
    primary = info.get('CFBundleIcons', {}).get('CFBundlePrimaryIcon', {})
    if primary.get('CFBundleIconFiles') != ['Icon-60', 'Icon-40', 'Icon-29']:
        raise ValueError('Missing expected primary iPhone icon declarations')
    if require_binary:
        binary = Path(plist_path).parent / expected['CFBundleExecutable']
        if not binary.is_file() or binary.stat().st_size == 0:
            raise ValueError(f'Bundle executable missing or empty: {binary}')
        import struct
        for name, size in [('Icon-29@2x.png',58),('Icon-29@3x.png',87),('Icon-40@2x.png',80),('Icon-40@3x.png',120),('Icon-60@2x.png',120),('Icon-60@3x.png',180)]:
            image = Path(plist_path).parent / name
            data = image.read_bytes()
            if len(data)<33 or data[:8]!=b'\x89PNG\r\n\x1a\n' or data[12:16]!=b'IHDR':
                raise ValueError(f'Invalid PNG icon: {name}')
            w,h,depth,colour = struct.unpack('>IIBB',data[16:26])
            if (w,h,depth,colour)!=(size,size,8,2):
                raise ValueError(f'Icon must be opaque 8-bit RGB {size}x{size}: {name}')
    return info


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('plist', type=Path)
    parser.add_argument('--game', required=True, choices=['pikmin1', 'pikmin2'])
    parser.add_argument('--require-binary', action='store_true')
    parser.add_argument('--variant', choices=['standard', 'solo-test', 'solo-update'], default='standard')
    args = parser.parse_args()
    try:
        info = validate(args.plist, args.game, args.require_binary, args.variant)
    except (ValueError, OSError, plistlib.InvalidFileException) as error:
        parser.exit(1, f'iOS bundle validation failed: {error}\n')
    print(f'Validated {args.game} metadata: {info["CFBundleExecutable"]}')
