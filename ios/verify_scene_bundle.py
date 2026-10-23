"""Reject a new iOS27 package that lacks the compiled scene lifecycle."""
from pathlib import Path
import plistlib,sys
app=Path(sys.argv[1]);info=plistlib.loads((app/'Info.plist').read_bytes())
scene=info['UIApplicationSceneManifest']
assert scene['UIApplicationSupportsMultipleScenes'] is False
entry=scene['UISceneConfigurations']['UIWindowSceneSessionRoleApplication'][0]
assert entry['UISceneDelegateClassName']=='NectarSDLSceneDelegate'
assert entry['UISceneClassName']=='UIWindowScene'
binary=(app/info['CFBundleExecutable']).read_bytes()
for value in [b'NectarSDLSceneDelegate',b'nectarConnectWindowScene:',b'nectarMainEntered']:
 assert value in binary, f'Scene metadata exists but compiled SDL lifecycle is missing: {value}'
assert info['CADisableMinimumFrameDurationOnPhone'] is True
assert set(info['UISupportedInterfaceOrientations'])=={'UIInterfaceOrientationLandscapeLeft','UIInterfaceOrientationLandscapeRight'}
print('PASS: packaged scene manifest, compiled delegate/once-only entry, landscape and ProMotion permission')
