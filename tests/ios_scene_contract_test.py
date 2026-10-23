"""Check shared production/smoke startup wiring; runtime proof requires the simulator probe."""
from pathlib import Path
import copy,plistlib,re
r=Path(__file__).resolve().parents[1]
def validate(info):
 m=info['UIApplicationSceneManifest'];assert m['UIApplicationSupportsMultipleScenes'] is False
 rows=m['UISceneConfigurations']['UIWindowSceneSessionRoleApplication'];assert len(rows)==1
 assert rows[0]['UISceneClassName']=='UIWindowScene'
 assert rows[0]['UISceneConfigurationName']=='NectarGame'
 assert rows[0]['UISceneDelegateClassName']=='NectarSDLSceneDelegate'
 assert info['CADisableMinimumFrameDurationOnPhone'] is True
 assert set(info['UISupportedInterfaceOrientations'])=={'UIInterfaceOrientationLandscapeLeft','UIInterfaceOrientationLandscapeRight'}
info=plistlib.loads((r/'ios/Info.plist.in').read_bytes());validate(info);checks=1
for key in ['UIApplicationSceneManifest','CADisableMinimumFrameDurationOnPhone','UISupportedInterfaceOrientations']:
 bad=copy.deepcopy(info);del bad[key]
 try:validate(bad)
 except (KeyError,AssertionError):checks+=1
 else:raise AssertionError('Missing scene/FPS/orientation metadata accepted: '+key)
for name,needle in [('ios/CMakeLists.txt','include("${CMAKE_CURRENT_SOURCE_DIR}/sdl_scene_support.cmake")'),('tests/ios_scene_smoke/CMakeLists.txt','include("${NECTAR_ROOT}/ios/sdl_scene_support.cmake")')]:
 assert needle in (r/name).read_text(encoding='utf-8');checks+=1
assert 'target_compile_definitions(SDL2-static PRIVATE NECTAR_IOS_SCENES=1)' in (r/'ios/sdl_scene_support.cmake').read_text();checks+=1
u=r/'games/pikmin1/third_party/SDL2-android/src/video/uikit'
app=(u/'SDL_uikitappdelegate.m').read_text(encoding='utf-8')
assert '@implementation NectarSDLSceneDelegate' in app
assert 'configuration.delegateClass = [NectarSDLSceneDelegate class]' in app
assert 'if (self.nectarMainEntered) return;' in app
assert 'if (self.nectarMainScheduled)' in app
assert '[self performSelector:@selector(postFinishLaunch)' in app
assert 'window.windowScene = scene' in app
checks+=6
win=(u/'SDL_uikitwindow.m').read_text(encoding='utf-8')
assert 'initWithWindowScene:scene' in win and 'CGRect frame = uiwindow.bounds;' in win;checks+=2
# App notification fallback is conditional, preventing double delivery in scene mode.
events=(u/'SDL_uikitevents.m').read_text(encoding='utf-8')
assert 'notification.object != app.nectarWindowScene' in events
assert 'UISceneWillDeactivateNotification' in events
assert '#else\n        [notificationCenter addObserver:self selector:@selector(applicationDidBecomeActive)' in events
checks+=3
audio=(r/'games/pikmin1/third_party/SDL2-android/src/audio/coreaudio/SDL_coreaudio.m').read_text(encoding='utf-8')
assert 'name:UISceneDidActivateNotification' in audio and 'name:UISceneWillEnterForegroundNotification' in audio
hid=(r/'games/pikmin1/third_party/SDL2-android/src/hidapi/ios/hid.m').read_text(encoding='utf-8')
assert 'name:UISceneWillDeactivateNotification' in hid and 'name:UISceneDidActivateNotification' in hid
checks+=2
# Build46 failed in the real CoreAudio TU: UIApplication.h alone does not
# declare UIScene notifications. Keep the owning header inside its iOS-only
# scene opt-in branch. This is a dependency check, not an Apple compile test.
def validate_audio_scene_import(header):
 assert re.search(r'#if defined\(NECTAR_IOS_SCENES\) && !TARGET_OS_TV\s+(?:/\*.*?\*/\s+)?#import <UIKit/UIScene\.h>\s+#endif', header, re.S)
audio_header=(r/'games/pikmin1/third_party/SDL2-android/src/audio/coreaudio/SDL_coreaudio.h').read_text(encoding='utf-8')
validate_audio_scene_import(audio_header);checks+=1
try:validate_audio_scene_import(audio_header.replace('#import <UIKit/UIScene.h>', ''))
except AssertionError:checks+=1
else:raise AssertionError('Missing CoreAudio scene declaration header accepted')
# Other notification users already import the full UIKit declarations.
assert '#import <UIKit/UIKit.h>' in (u/'SDL_uikitappdelegate.h').read_text(encoding='utf-8');checks+=1
assert '#import <UIKit/UIKit.h>' in hid;checks+=1
print(f'PASS: {checks} scene metadata, missing-key negative controls and shared SDL entry/window/lifecycle wiring checks (not runtime proof)')
