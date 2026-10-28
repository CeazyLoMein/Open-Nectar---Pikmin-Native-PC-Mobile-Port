"""Ensure invitations stay user-initiated and both menus remain scrollable."""
from pathlib import Path
r=Path(__file__).resolve().parents[1]
room=(r/'ios/ios_coop_room.mm').read_text(encoding='utf-8')
practice=(r/'ios/ios_coop_practice.mm').read_text(encoding='utf-8')
style=(r/'ios/ios_coop_style.h').read_text(encoding='utf-8')
share=room.split('- (void)shareInvite {',1)[1].split('\n}',1)[0]
assert 'if (!_host || !self.code.text.length || self.presentedViewController) return;' in share
assert 'initWithActivityItems:@[self.code.text]' in share and 'presentViewController:share' in share
assert 'sourceView=self.shareButton' in share and 'sourceRect=self.shareButton.bounds' in share
assert room.count('initWithActivityItems:')==1 and 'action:@selector(shareInvite)' in room
assert 'self.shareButton.enabled = self.clipboardButton.enabled;' in room
background=room.split('- (void)backgrounded:',1)[1].split('- (void)foregrounded:',1)[0]
assert 'disconnectPeer(' not in background and '[self stopConnection]' not in background
assert '_away = YES' in background
foreground=room.split('- (void)foregrounded:',1)[1].split('- (BOOL)detachConnection:',1)[0]
assert '_away = NO' in foreground and 'Checking the connection' in foreground
# Both screens must monitor the game window's scene, not another window.
for source in (room, practice):
 assert 'UISceneWillDeactivateNotification' in source and 'UISceneDidActivateNotification' in source
 assert 'UIApplicationWillResignActiveNotification' not in source and 'UIApplicationDidBecomeActiveNotification' not in source
assert 'object:self.gameScene' in room and 'sRoomController.gameScene = window.windowScene' in room
assert 'object:scene' in practice and '[lifecycle observeScene:window.windowScene]' in practice
assert '[NSNotificationCenter.defaultCenter removeObserver:self]' in practice

for source in (room,practice):
 assert 'nectarCoopBackground()' in source and 'nectarCoopStyleButton(' in source
 assert 'UIScrollView' in source and 'safeAreaLayoutGuide' in source and 'scroll.contentLayoutGuide' in source
assert 'adjustsFontForContentSizeCategory=YES' in style
print('PASS share requires host action; co-op screens retain accessible scrolling and safe areas')
