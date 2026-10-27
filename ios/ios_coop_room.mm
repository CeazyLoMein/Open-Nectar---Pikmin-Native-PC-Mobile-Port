#if defined(NECTAR_COOP_WORLD) && NECTAR_COOP_WORLD
#include "netplay/pc_coop_practice_bridge.h"
#endif
#import <UIKit/UIKit.h>
#include "ios_coop_content_identity.h"
#include "ios_coop_room.h"
#include "ios_coop_handoff.h"
#include "nectar_net/coop_connection.h"
#include "nectar_coop_build_identity.h"
#include "nectar_net/room.h"
#include <chrono>
#include <ctime>
#include <memory>
#include <atomic>

using namespace nectar::net;
namespace {
constexpr std::uint32_t kConnectionCheckCapability = 0x00020000;
std::uint64_t nowMs() {
    return static_cast<std::uint64_t>(std::chrono::duration_cast<std::chrono::milliseconds>(
        std::chrono::steady_clock::now().time_since_epoch()).count());
}
std::uint64_t unixSeconds() { return static_cast<std::uint64_t>(std::time(nullptr)); }

NSString* joinError(JoinFailure failure, CompatibilityField field) {
    switch (failure) {
    case JoinFailure::BadCode: return @"That room code is incomplete. Copy it again from the host.";
    case JoinFailure::Expired: return @"That room code expired. Ask the host to make a new room.";
    case JoinFailure::WrongVersion: return @"Both phones need the same P1 update.";
    case JoinFailure::Refused: return @"That room is no longer available. Copy a new code from the host.";
    case JoinFailure::RoomFull: return @"Someone already joined that room.";
    case JoinFailure::Incompatible:
        if (field == CompatibilityField::Content) return @"The phones have different game data. No game was started.";
        return @"Both phones need the same P1 update and game version. No game was started.";
    case JoinFailure::Lost: return @"Connection lost. Host or join again when both phones are ready.";
    default: return @"Couldn't reach the host. Use the same Wi-Fi, allow Local Network access, and leave the host's connection screen open. Then try again.";
    }
}
}

@interface NectarCoopRoomController : UIViewController {
    std::unique_ptr<HostRoom> _host;
    std::unique_ptr<GuestJoin> _guest;
    std::unique_ptr<CoopConnection> _handoff;
    CompatibilityInfo _identity;
    BOOL _checked;
    BOOL _closed;
    BOOL _away;
}
- (BOOL)detachConnection:(std::unique_ptr<CoopConnection>*)output;
- (BOOL)rememberEvent:(TransportEvent*)event;
@property(nonatomic, strong) UILabel* status;
@property(nonatomic, strong) UITextView* code;
@property(nonatomic, strong) UIButton* hostButton;
@property(nonatomic, strong) UIButton* practiceButton;
@property(nonatomic, strong) UIButton* joinButton;
@property(nonatomic, strong) UIButton* clipboardButton;
@property(nonatomic, strong) UIButton* pasteButton;
@property(nonatomic, strong) UIButton* leaveButton;
@property(nonatomic, strong) UIButton* rejoinButton;
@property(nonatomic, copy) NSString* pendingJoinCode;
@property(nonatomic, strong) NSTimer* timer;
@end

static NectarCoopRoomController* sRoomController;
// Process memory only. Never write private invite credentials to preferences/logs.
static NSString* sLastJoinedRoomCode;
static std::atomic<bool> sRoomCoversGame{false};

@implementation NectarCoopRoomController
- (UIButton*)button:(NSString*)title action:(SEL)action {
    UIButton* button = [UIButton buttonWithType:UIButtonTypeSystem];
    [button setTitle:title forState:UIControlStateNormal];
    button.titleLabel.font = [UIFont preferredFontForTextStyle:UIFontTextStyleHeadline];
    [button addTarget:self action:action forControlEvents:UIControlEventTouchUpInside];
    [button.heightAnchor constraintGreaterThanOrEqualToConstant:44].active = YES;
    return button;
}
- (void)viewDidLoad {
    [super viewDidLoad];
    self.view.backgroundColor = UIColor.systemBackgroundColor;
    self.modalInPresentation = YES;
    UILabel* title = [UILabel new];
    title.text = @"Online Co-op — Connect";
    title.font = [UIFont preferredFontForTextStyle:UIFontTextStyleTitle2];
    title.numberOfLines = 0;
    UILabel* explanation = [UILabel new];
    explanation.text = @"Connect both phones to the same Wi-Fi. Host a private room, then copy its code to the other phone. After connecting, tap Start Co-op Practice on both phones from the title screen. The small practice area uses disposable state and does not change your campaign. Campaign co-op is still being developed.";
    explanation.font = [UIFont preferredFontForTextStyle:UIFontTextStyleBody];
    explanation.numberOfLines = 0;
    self.status = [UILabel new];
    self.status.text = @"Checking game data… This may take a moment.";
    self.status.numberOfLines = 0;
    self.status.accessibilityTraits = UIAccessibilityTraitUpdatesFrequently;
    self.code = [UITextView new];
    self.code.font = [UIFont monospacedSystemFontOfSize:15 weight:UIFontWeightRegular];
    self.code.backgroundColor = UIColor.secondarySystemBackgroundColor;
    self.code.autocorrectionType = UITextAutocorrectionTypeNo;
    self.code.spellCheckingType = UITextSpellCheckingTypeNo;
    self.code.autocapitalizationType = UITextAutocapitalizationTypeNone;
    self.code.smartQuotesType = UITextSmartQuotesTypeNo;
    self.code.smartDashesType = UITextSmartDashesTypeNo;
    self.code.accessibilityLabel = @"Private room code";
    [self.code.heightAnchor constraintEqualToConstant:100].active = YES;
    self.hostButton = [self button:@"Host Room" action:@selector(hostRoom)];
    self.joinButton = [self button:@"Join Room" action:@selector(joinRoom)];
    self.clipboardButton = [self button:@"Copy Code" action:@selector(didTapCopy)];
    self.pasteButton = [self button:@"Paste Code" action:@selector(pasteCode)];
    self.leaveButton = [self button:@"Leave Room" action:@selector(leaveRoom)];
    self.rejoinButton = [self button:@"Rejoin Last Room" action:@selector(rejoinRoom)];
    UIButton* done = [self button:@"Done" action:@selector(closeScreen)];
#if defined(NECTAR_COOP_WORLD) && NECTAR_COOP_WORLD
    self.practiceButton=[self button:@"Start Co-op Practice" action:@selector(startPractice)];
#endif
    UIStackView* actions = [[UIStackView alloc] initWithArrangedSubviews:@[self.hostButton, self.joinButton]];
    actions.distribution = UIStackViewDistributionFillEqually;
    UIStackView* editing = [[UIStackView alloc] initWithArrangedSubviews:@[self.clipboardButton, self.pasteButton]];
    editing.distribution = UIStackViewDistributionFillEqually;
    UIStackView* ending = [[UIStackView alloc] initWithArrangedSubviews:@[self.leaveButton, done]];
    ending.distribution = UIStackViewDistributionFillEqually;
    UIStackView* content = [[UIStackView alloc] initWithArrangedSubviews:@[title, explanation, self.status, actions, self.code, editing, self.rejoinButton, ending]];
    if(self.practiceButton) [content insertArrangedSubview:self.practiceButton atIndex:3];
    content.axis = UILayoutConstraintAxisVertical;
    content.spacing = 12;
    UIScrollView* scroll = [UIScrollView new];
    scroll.keyboardDismissMode = UIScrollViewKeyboardDismissModeInteractive;
    scroll.translatesAutoresizingMaskIntoConstraints = NO;
    content.translatesAutoresizingMaskIntoConstraints = NO;
    [self.view addSubview:scroll]; [scroll addSubview:content];
    [NSLayoutConstraint activateConstraints:@[
        [scroll.leadingAnchor constraintEqualToAnchor:self.view.safeAreaLayoutGuide.leadingAnchor],
        [scroll.trailingAnchor constraintEqualToAnchor:self.view.safeAreaLayoutGuide.trailingAnchor],
        [scroll.topAnchor constraintEqualToAnchor:self.view.safeAreaLayoutGuide.topAnchor],
        [scroll.bottomAnchor constraintEqualToAnchor:self.view.safeAreaLayoutGuide.bottomAnchor],
        [content.leadingAnchor constraintEqualToAnchor:scroll.contentLayoutGuide.leadingAnchor constant:20],
        [content.trailingAnchor constraintEqualToAnchor:scroll.contentLayoutGuide.trailingAnchor constant:-20],
        [content.topAnchor constraintEqualToAnchor:scroll.contentLayoutGuide.topAnchor constant:20],
        [content.bottomAnchor constraintEqualToAnchor:scroll.contentLayoutGuide.bottomAnchor constant:-20],
        [content.widthAnchor constraintEqualToAnchor:scroll.frameLayoutGuide.widthAnchor constant:-40]
    ]];
    [self updateButtons];
    [NSNotificationCenter.defaultCenter addObserver:self selector:@selector(backgrounded:)
        name:UIApplicationDidEnterBackgroundNotification object:nil];
    [NSNotificationCenter.defaultCenter addObserver:self selector:@selector(foregrounded:)
        name:UIApplicationDidBecomeActiveNotification object:nil];
    // Resolve once before the worker starts; the game's cwd never supplies user data.
    NSURL* data = [NSURL fileURLWithPath:[NSFileManager.defaultManager.currentDirectoryPath
        stringByAppendingPathComponent:@"assets/dataDir"] isDirectory:YES];
    __weak NectarCoopRoomController* weakSelf = self;
    dispatch_async(dispatch_get_global_queue(QOS_CLASS_USER_INITIATED, 0), ^{
        @autoreleasepool {
            std::array<std::uint8_t, 32> digest{};
            const bool ok = nectar_ios::contentIdentity(data, digest);
            dispatch_async(dispatch_get_main_queue(), ^{
                NectarCoopRoomController* controller = weakSelf;
                if (!controller || controller->_closed) return;
                controller->_checked = ok;
                if (ok) {
                    controller->_identity.game = static_cast<std::uint8_t>(GameId::Pikmin1);
                    controller->_identity.region = 1;
                    controller->_identity.build = nectar_ios::coop_build_identity;
                    controller->_identity.content = digest;
                    controller->_identity.capabilities = kConnectionCheckCapability;
                    controller->_identity.requiredCapabilities = kConnectionCheckCapability;
                    requireCoopSessionCapability(controller->_identity);
                    controller.status.text = @"Ready. Host a room or paste a private room code.";
                } else controller.status.text = @"Couldn't verify the game data. Close this screen and check that P1's assets are installed.";
                [controller updateButtons];
            });
        }
    });
    self.timer = [NSTimer scheduledTimerWithTimeInterval:0.05 target:self selector:@selector(pump:) userInfo:nil repeats:YES];
}
- (void)updateButtons {
    const BOOL busy = static_cast<bool>(_host) || static_cast<bool>(_guest);
    self.hostButton.enabled = _checked && !busy;
    self.joinButton.enabled = _checked && !busy;
    self.rejoinButton.enabled = _checked && !busy && sLastJoinedRoomCode.length > 0;
    self.clipboardButton.enabled = static_cast<bool>(_host) && self.code.text.length > 0;
    self.pasteButton.enabled = _checked && !busy;
    self.code.editable = _checked && !busy;
    self.leaveButton.enabled = busy;
#if defined(NECTAR_COOP_WORLD) && NECTAR_COOP_WORLD
    GatedTransport* link=_host ? _host->transport() : _guest ? _guest->transport() : nullptr;
    self.practiceButton.enabled=pc_coop_practice_can_enter() && link && link->state()==TransportState::Connected;
#endif
}
- (void)stopConnection {
    // UI owns links only before handoff. Successful detach empties these slots;
    // CoopConnection ends its borrowed session before closing the moved room.
    if (_guest) _guest->cancel();
    if (_host) _host->close();
    _guest.reset(); _host.reset(); _handoff.reset();
    self.code.text = @"";
    self.pendingJoinCode = nil;
    [self.view endEditing:YES];
    [self updateButtons];
}
- (void)hostRoom {
    if (!_checked || _closed || _host || _guest) return;
    [self.view endEditing:YES];
    _host = std::make_unique<HostRoom>();
    RoomConfig config;
    config.compatibility = _identity;
    config.automaticPortMapping = false;
    config.includeLanEndpoint = true;
    RoomStatus status;
    const auto error = _host->open(config, unixSeconds(), status);
    if (error != RoomError::None) {
        [self stopConnection];
        self.status.text = @"Couldn't open a room. Connect to Wi-Fi, allow Local Network access, then try again.";
        return;
    }
    // Only successful hosting replaces the previously remembered guest role.
    sLastJoinedRoomCode = nil;
    self.code.text = [NSString stringWithUTF8String:status.code.c_str()];
    self.status.text = @"Room open. Copy the code to the other phone and leave this screen open.";
    [self updateButtons];
}
- (void)joinRoom {
    if (!_checked || _closed || _host || _guest) return;
    [self.view endEditing:YES];
    NSString* code = [self.code.text stringByTrimmingCharactersInSet:NSCharacterSet.whitespaceAndNewlineCharacterSet];
    if (!code.length || code.length > 4096) {
        self.status.text = @"Paste the complete code from the host first.";
        return;
    }
    self.pendingJoinCode = code;
    _guest = std::make_unique<GuestJoin>();
    const auto failure = _guest->start(code.UTF8String, _identity, 1, unixSeconds(), nowMs());
    if (failure != JoinFailure::None) {
        if ((failure == JoinFailure::Expired || failure == JoinFailure::BadCode || failure == JoinFailure::WrongVersion)
            && [sLastJoinedRoomCode isEqualToString:code]) sLastJoinedRoomCode = nil;
        NSString* reason = joinError(failure, _guest->incompatibility());
        [self stopConnection]; self.status.text = reason; return;
    }
    self.status.text = @"Connecting… Allow Local Network access if asked.";
    [self updateButtons];
}
- (void)rejoinRoom {
    if (!_checked || _closed || _host || _guest || !sLastJoinedRoomCode.length) return;
    self.code.text = sLastJoinedRoomCode;
    [self joinRoom]; // Fresh authentication/content validation; never bypass the gates.
}
- (BOOL)rememberEvent:(TransportEvent*)event {
    if (event->type == TransportEventType::Connected || event->type == TransportEventType::Disconnected ||
        event->type == TransportEventType::Error) { _handoff.reset(); return YES; }
    if (event->type != TransportEventType::Message) return YES;
    if (!_handoff) _handoff = std::make_unique<CoopConnection>();
    if (_handoff->bufferBeforeHandoff(std::move(*event))) return YES;
    [self stopConnection];
    self.status.text = @"The connection sent invalid or too many startup messages. Please reconnect.";
    return NO;
}
- (void)pump:(NSTimer*)timer {
    (void)timer;
    if (_closed || _away) return;
    GatedTransport* link = nullptr;
    if (_host) {
        TransportEvent event;
        for (int count = 0; count < 64 && _host->transport()->poll(event); ++count)
            if (![self rememberEvent:&event]) return;
        link = _host->transport();
        if (link->state() == TransportState::Failed) {
            [self stopConnection];
            self.status.text = @"The room connection stopped. Check Wi-Fi and Local Network access, then host again.";
            return;
        }
        if (link->state() == TransportState::Listening)
            self.status.text = @"Room open. Waiting for your partner. If they already joined, they can tap Rejoin Last Room.";
    } else if (_guest) {
        TransportEvent event; bool hasEvent = false;
        const auto progress = _guest->poll(nowMs(), event, hasEvent);
        if (progress == JoinProgress::Failed) {
            const auto failure = _guest->failure();
            NSString* reason = joinError(failure, _guest->incompatibility());
            if ((failure == JoinFailure::Refused || failure == JoinFailure::Expired ||
                failure == JoinFailure::Incompatible || failure == JoinFailure::WrongVersion)
                && [sLastJoinedRoomCode isEqualToString:self.pendingJoinCode]) sLastJoinedRoomCode = nil;
            if (failure == JoinFailure::Lost && sLastJoinedRoomCode.length)
                reason = @"Connection lost. When the host returns to P1, tap Rejoin Last Room. You do not need the code again.";
            [self stopConnection]; self.status.text = reason; return;
        }
        if (progress == JoinProgress::Connected && self.pendingJoinCode.length) {
            // Remember ONLY a room that completed secret/build/content validation.
            sLastJoinedRoomCode = [self.pendingJoinCode copy];
            self.pendingJoinCode = nil;
        }
        if (hasEvent && ![self rememberEvent:&event]) return;
        link = _guest->transport();
    }
    [self updateButtons];
    if (link && link->state() == TransportState::Connected) {
        TransportStats stats;
        if (link->stats(stats) && stats.rttMs >= 0)
            self.status.text = [NSString stringWithFormat:@"Connected — same build and game data. Delay: %d ms. Connection check passed. From the title screen, tap Start Co-op Practice on BOTH phones.", stats.rttMs];
        else self.status.text = @"Connected — same build and game data. Connection check passed. From the title screen, tap Start Co-op Practice on BOTH phones.";
    }
}
#if defined(NECTAR_COOP_WORLD) && NECTAR_COOP_WORLD
- (void)startPractice {
    if(!pc_coop_practice_can_enter()) {self.status.text=@"Return to P1's title screen before starting practice.";return;}
    std::unique_ptr<CoopConnection> connection;
    if(![self detachConnection:&connection]) return;
    // Same UIKit/game owning thread; no second consumer of this connection.
    if(!pc_coop_practice_adopt(connection)) {
        connection->close();
    }
}
#endif
- (void)didTapCopy {
    if (!_host || !self.code.text.length) return;
    // User-initiated only, local clipboard, expires. Never logs or uploads secrets.
    [UIPasteboard.generalPasteboard setItems:@[@{UIPasteboardTypeAutomatic:self.code.text}]
        options:@{UIPasteboardOptionLocalOnly:@YES,
                  UIPasteboardOptionExpirationDate:[NSDate dateWithTimeIntervalSinceNow:300]}];
}
- (void)pasteCode {
    if (!_checked || _host || _guest) return;
    NSString* value = UIPasteboard.generalPasteboard.string;
    if (value.length <= 4096) self.code.text = value ?: @"";
    [self.view endEditing:YES];
}
- (void)leaveRoom {
    [self stopConnection];
    self.status.text = @"Room closed. You can host or join a new one.";
}
- (void)backgrounded:(NSNotification*)notification {
    (void)notification;
    _away = YES;
    if (_host) {
        // Sharing the copied code through Messages must not invalidate the room.
        // No gameplay is active: drop any partner, keep listening/code in memory,
        // and require a fresh authenticated connection after returning.
        _handoff.reset();
        _host->transport()->disconnectPeer(false);
        self.status.text = @"Room kept open. Return here after sharing the code, before your partner joins.";
    } else if (_guest) {
        [self stopConnection];
        self.status.text = @"Connection paused while this app was away. Return the host to P1, then tap Rejoin Last Room.";
    }
}
- (void)foregrounded:(NSNotification*)notification {
    (void)notification;
    _away = NO;
    if (_host) self.status.text = @"Same room open. Your partner can rejoin now. Keep P1 in front.";
}
- (BOOL)detachConnection:(std::unique_ptr<CoopConnection>*)output {
    // Exactly one main-thread handoff; failed validation leaves UI/owners intact.
    if (!NSThread.isMainThread || !output || *output || !_checked || _closed || _away) return NO;
    if (!_handoff) _handoff = std::make_unique<CoopConnection>();
    const bool accepted = _host ? _handoff->adoptHost(_host) : _guest ? _handoff->adoptGuest(_guest) : false;
    if (!accepted) return NO;
    _closed = YES;
    self.view.userInteractionEnabled = NO;
    [self.timer invalidate]; self.timer = nil;
    [NSNotificationCenter.defaultCenter removeObserver:self];
    // Do NOT call stopConnection: it would close the link the game now owns.
    [self.view endEditing:YES]; self.code.text = @""; self.pendingJoinCode = nil;
    *output = std::move(_handoff);
    [self dismissViewControllerAnimated:YES completion:^{ sRoomController = nil; sRoomCoversGame.store(false); }];
    return YES;
}
- (void)closeScreen {
    if (_closed) return;
    _closed = YES;
    [self stopConnection];
    [self.timer invalidate]; self.timer = nil;
    [NSNotificationCenter.defaultCenter removeObserver:self];
    [self dismissViewControllerAnimated:YES completion:^{ sRoomController = nil; sRoomCoversGame.store(false); }];
}
- (void)dealloc {
    [self.timer invalidate];
    [NSNotificationCenter.defaultCenter removeObserver:self];
}
@end

extern "C" void nectar_ios_open_coop_room(void) {
    dispatch_async(dispatch_get_main_queue(), ^{
        if (sRoomController) return;
        UIWindow* window = nil;
        for (UIScene* scene in UIApplication.sharedApplication.connectedScenes) {
            if (scene.activationState != UISceneActivationStateForegroundActive ||
                ![scene isKindOfClass:UIWindowScene.class]) continue;
            for (UIWindow* candidate in ((UIWindowScene*)scene).windows)
                if (candidate.isKeyWindow) { window = candidate; break; }
            if (window) break;
        }
        UIViewController* presenter = window.rootViewController;
        if (!presenter || presenter.presentedViewController || presenter.isBeingPresented || presenter.isBeingDismissed) return;
        sRoomController = [NectarCoopRoomController new];
        sRoomController.modalPresentationStyle = UIModalPresentationOverFullScreen;
        sRoomCoversGame.store(true);
        [presenter presentViewController:sRoomController animated:YES completion:nil];
    });
}

bool nectar_ios_coop_room_take_connection(std::unique_ptr<CoopConnection>& output) {
    if (!NSThread.isMainThread || output || !sRoomController) return false;
    return [sRoomController detachConnection:&output] == YES;
}

extern "C" int nectar_ios_coop_room_is_open(void) {
    return sRoomCoversGame.load() ? 1 : 0;
}
