"""Compile the screen's actual synthesized getters without needing UIKit headers.

This catches Cocoa owned-object naming rules even on a Windows Clang frontend.
The full native screen is still compiled against the real iPhoneOS SDK in CI.
"""
import argparse
from pathlib import Path
import re
import subprocess
import tempfile


def run(compiler, sdk_root=None):
    root = Path(__file__).resolve().parents[1]
    source = (root / 'ios/ios_coop_room.mm').read_text(encoding='utf-8')
    properties = re.findall(r'^@property[^;]+;', source, re.MULTILINE)
    if not properties:
        raise AssertionError('No actual screen properties found')
    classes = sorted(set(re.findall(r'\b(\w+)\s*\*', '\n'.join(properties))))
    fixture = ('__attribute__((objc_root_class)) @interface ProbeRoot @end\n'
               '@class ' + ', '.join(classes) + ';\n'
               '@interface Probe : ProbeRoot\n' + '\n'.join(properties) +
               '\n@end\n@implementation Probe @end\n')
    flags = ['-target', 'arm64-apple-ios15.0', '-x', 'objective-c++', '-fobjc-arc',
             '-fsyntax-only', '-Wall', '-Wextra', '-Werror']
    if sdk_root:
        flags += ['-isysroot', str(sdk_root)]
    tidy = 'clang-tidy' in Path(compiler).name
    with tempfile.TemporaryDirectory(prefix='nectar-coop-arc-') as folder:
        for label, text, success in [
            ('actual', fixture, True),
            ('ownership-negative', fixture.replace('@interface Probe : ProbeRoot\n',
                '@interface Probe : ProbeRoot\n@property(nonatomic, strong) ProbeRoot* copyOwnershipTrap;\n'), False)
        ]:
            path = Path(folder) / (label + '.mm')
            path.write_text(text, encoding='utf-8')
            if tidy:
                # clang-tidy takes its source before -- and forwards the flags.
                command = [str(compiler), str(path), '--checks=-*,clang-analyzer-core.DivideZero',
                           '--warnings-as-errors=*', '--', *flags]
            else:
                # clang's -x applies to FOLLOWING inputs, including .mm fixtures.
                command = [str(compiler), *flags, str(path)]
            result = subprocess.run(command, text=True, capture_output=True, timeout=60)
            output = result.stdout + result.stderr
            if success and result.returncode:
                raise AssertionError('Actual UI getters fail ARC compilation:\n' + output)
            if not success and (not result.returncode or 'property follows Cocoa naming convention' not in output):
                raise AssertionError('Compiler did not reject the owned-object getter negative control:\n' + output)
    print(f'PASS actual {len(properties)} co-op UI properties under iOS ARC; original ownership naming error rejected')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--compiler', required=True)
    parser.add_argument('--sdk-root', type=Path)
    args = parser.parse_args()
    run(args.compiler, args.sdk_root)
