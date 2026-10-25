"""Hash tracked code/configuration bytes, independent of documentation commits."""
import argparse
import hashlib
from pathlib import Path
import subprocess

SUFFIXES = {'.c', '.cc', '.cpp', '.cxx', '.h', '.hpp', '.hxx', '.m', '.mm', '.cmake', '.in', '.py', '.S', '.s'}
ROOTS = ('games/pikmin1/', 'libs/', 'ios/')


def build_digest(root, names, game_version):
    digest = hashlib.sha256(b'NECTAR-IOS-P1-ROOM-CHECK-v1\0' + game_version.encode() + b'\0')
    count = 0
    for name in sorted(set(names)):
        relative = Path(name)
        if relative.is_absolute() or '..' in relative.parts:
            raise ValueError('Source path escapes repository')
        if not name.startswith(ROOTS) or (relative.suffix not in SUFFIXES and relative.name != 'CMakeLists.txt'):
            continue
        path = root / relative
        if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
            raise ValueError('Source identity must not follow links outside the repository')
        # Git checkouts may use different line endings. Hash the compiled text consistently.
        content = path.read_bytes().replace(b'\r\n', b'\n')
        key = name.encode('utf-8')
        digest.update(len(key).to_bytes(4, 'big') + key)
        digest.update(hashlib.sha256(content).digest())
        count += 1
    if not count:
        raise ValueError('No tracked game source found; refusing an empty identity')
    return digest.digest(), count


def generate(root, output, game_version):
    names = subprocess.check_output(['git', '-C', str(root), 'ls-files', '-z'], text=True, encoding='utf-8').split('\0')
    digest, count = build_digest(root, [name for name in names if name], game_version)
    output.parent.mkdir(parents=True, exist_ok=True)
    values = ', '.join(f'0x{byte:02x}' for byte in digest)
    output.write_text('#pragma once\n#include <array>\n#include <cstdint>\n'
                      'namespace nectar_ios {\n'
                      f'inline constexpr std::array<std::uint8_t,32> coop_build_identity = {{{values}}};\n'
                      '}\n', encoding='utf-8')
    print(f'Co-op build identity: {digest.hex()} ({count} tracked source/configuration files)')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--game-version', required=True)
    args = parser.parse_args()
    generate(args.root.resolve(), args.output.resolve(), args.game_version)
