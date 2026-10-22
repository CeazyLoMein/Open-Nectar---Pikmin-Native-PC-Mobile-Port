"""Exercise the actual CMake metadata and bundle verifier without an Apple SDK."""
import argparse
import importlib.util
from pathlib import Path
import plistlib
import subprocess
import tempfile
import shutil

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cmake', default='cmake')
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location('verify_bundle_info', ROOT/'ios/verify_bundle_info.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    checks = 0
    with tempfile.TemporaryDirectory() as temporary:
        temp = Path(temporary)
        identities = set()
        for game, variant in [('pikmin1','standard'), ('pikmin2','standard'), ('pikmin1','solo-test'), ('pikmin1','solo-update')]:
            target = temp/f'{game}-{variant}.app'
            target.mkdir()
            script = temp/'configure.cmake'
            script.write_text(f'''set(NECTAR_IOS_GAME "{game}")
set(NECTAR_IOS_VARIANT "{variant}" CACHE STRING "" FORCE)
include("{(ROOT/'ios/app_variant.cmake').as_posix()}")
configure_file("{(ROOT/'ios/Info.plist.in').as_posix()}" "{(target/'Info.plist').as_posix()}" @ONLY)
''')
            subprocess.run([args.cmake,'-P',str(script)],check=True)
            info = module.validate(target/'Info.plist',game,variant=variant)
            identities.add(info['CFBundleIdentifier'])
            assert info['UIFileSharingEnabled'] and 'com.apple.security.application-groups' not in info
            try:
                module.validate(target/'Info.plist',game,True,variant)
            except ValueError:
                checks += 1
            else:
                raise AssertionError('missing executable accepted')
            (target/info['CFBundleExecutable']).write_bytes(b'test-binary')
            for icon in (ROOT/'ios/icons'/game).glob('Icon-*.png'):
                shutil.copy2(icon,target/icon.name)
            module.validate(target/'Info.plist',game,True,variant)
            wrong = dict(info,CFBundleIdentifier='org.opennectar.experimental.pikmin1')
            if variant == 'solo-test':
                with (target/'Info.plist').open('wb') as stream: plistlib.dump(wrong,stream)
                try: module.validate(target/'Info.plist',game,True,variant)
                except ValueError: checks += 1
                else: raise AssertionError('test app with original P1 identity accepted')
            if variant == 'solo-update':
                info['CFBundleIdentifier']='org.opennectar.experimental.pikmin1.solotest'
                with (target/'Info.plist').open('wb') as stream: plistlib.dump(info,stream)
                try: module.validate(target/'Info.plist',game,True,variant)
                except ValueError: checks += 1
                else: raise AssertionError('update app with separate-test identity accepted')
            checks += 3
        assert len(identities)==3
        for game,variant in [('pikmin2','solo-test'),('pikmin2','solo-update'),('pikmin1','bad')]:
            script.write_text(f'''set(NECTAR_IOS_GAME "{game}")
set(NECTAR_IOS_VARIANT "{variant}" CACHE STRING "" FORCE)
include("{(ROOT/'ios/app_variant.cmake').as_posix()}")
''')
            result = subprocess.run([args.cmake,'-P',str(script)],capture_output=True)
            assert result.returncode != 0
            checks += 1
    storage = (ROOT/'ios/ios_storage.mm').read_text(encoding='utf-8')
    assert 'solo_bundle_matches(actualID, nectar_ios::solo_bundle_id(updateExisting))' in storage
    assert 'solo_storage_name(updateExisting)' in storage
    assert 'solo_card_directory(updateExisting)' in storage
    assert 'setenv("NECTAR_SAVE_DIR", cardRoot.fileSystemRepresentation, 1)' in storage
    assert storage.index('Wrong bundle identity') < storage.index('createDirectoryAtPath:directory')
    cmake = (ROOT/'ios/CMakeLists.txt').read_text(encoding='utf-8')
    assert 'XCODE_ATTRIBUTE_COMPRESS_PNG_FILES "NO"' in cmake
    gate = cmake[cmake.index('if(NOT NECTAR_IOS_VARIANT STREQUAL "standard")'):]
    assert gate.index('NECTAR_P1_SOLO_TEST=1') < gate.index('endif()')
    print(f'PASS: {checks+6} actual bundle/configure, identity rejection and storage wiring checks')

if __name__ == '__main__': main()
