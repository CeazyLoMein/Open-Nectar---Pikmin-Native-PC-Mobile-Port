#import <UIKit/UIKit.h>
#import <CommonCrypto/CommonDigest.h>
#include "ios_coop_room.h"
#include "nectar_coop_build_identity.h"
#include "nectar_net/room.h"
#include <chrono>
#include <ctime>
#include <memory>

using namespace nectar::net;
namespace {
constexpr std::uint32_t kConnectionCheckCapability = 0x00020000;
std::uint64_t nowMs() {
    return static_cast<std::uint64_t>(std::chrono::duration_cast<std::chrono::milliseconds>(
        std::chrono::steady_clock::now().time_since_epoch()).count());
}
std::uint64_t unixSeconds() { return static_cast<std::uint64_t>(std::time(nullptr)); }

// Immutable base game data only. No reading/writing cards, settings or personal files.
// Cosmetic replacements may differ. Runtime gameplay options need a separate gate
// before a later build can START a shared simulation; this screen cannot do that.
bool contentIdentity(NSURL* root, std::array<std::uint8_t, 32>& output) {
    NSFileManager* manager = NSFileManager.defaultManager;
    NSNumber* isDirectory = nil;
    NSNumber* isLink = nil;
    if (![root getResourceValue:&isDirectory forKey:NSURLIsDirectoryKey error:nil] ||
        !isDirectory.boolValue ||
        ![root getResourceValue:&isLink forKey:NSURLIsSymbolicLinkKey error:nil] || isLink.boolValue) return false;
    __block BOOL enumerationFailed = NO;
    NSDirectoryEnumerator<NSURL*>* enumerator = [manager enumeratorAtURL:root
        includingPropertiesForKeys:@[NSURLIsRegularFileKey, NSURLIsDirectoryKey, NSURLIsSymbolicLinkKey]
        options:0 errorHandler:^BOOL(NSURL* url, NSError* error) {
            (void)url; (void)error; enumerationFailed = YES; return NO;
        }];
    if (!enumerator) return false;
    NSMutableArray<NSString*>* names = [NSMutableArray array];
    NSString* prefix = [root.path stringByAppendingString:@"/"];
    for (NSURL* url in enumerator) {
        NSNumber* regular = nil;
        NSNumber* directory = nil;
        NSNumber* link = nil;
        if (![url.path hasPrefix:prefix] ||
            ![url getResourceValue:&link forKey:NSURLIsSymbolicLinkKey error:nil] || link.boolValue ||
            ![url getResourceValue:&regular forKey:NSURLIsRegularFileKey error:nil] ||
            ![url getResourceValue:&directory forKey:NSURLIsDirectoryKey error:nil]) return false;
        if (regular.boolValue) [names addObject:[url.path substringFromIndex:prefix.length]];
        else if (!directory.boolValue) return false;
        if (names.count > 100000) return false;
    }
    if (enumerationFailed || !names.count) return false;
    [names sortUsingComparator:^NSComparisonResult(NSString* a, NSString* b) {
        return [a compare:b options:NSLiteralSearch];
    }];
    CC_SHA256_CTX tree;
    CC_SHA256_Init(&tree);
    const char domain[] = "NECTAR-P1-DATA-v1";
    CC_SHA256_Update(&tree, domain, sizeof(domain));
    std::uint64_t total = 0;
    for (NSString* name in names) {
        @autoreleasepool {
            NSData* key = [name dataUsingEncoding:NSUTF8StringEncoding];
            if (!key || key.length > 16384) return false;
            NSString* path = [root.path stringByAppendingPathComponent:name];
            NSDictionary<NSFileAttributeKey, id>* before = [manager attributesOfItemAtPath:path error:nil];
            if (!before || ![before[NSFileType] isEqualToString:NSFileTypeRegular]) return false;
            const auto size = [before[NSFileSize] unsignedLongLongValue];
            if (size > 8ULL * 1024 * 1024 * 1024 - total) return false;
            total += size;
            NSInputStream* input = [NSInputStream inputStreamWithFileAtPath:path];
            [input open];
            CC_SHA256_CTX file;
            CC_SHA256_Init(&file);
            std::uint8_t buffer[65536], bytes[CC_SHA256_DIGEST_LENGTH];
            std::uint64_t read = 0;
            NSInteger n = 0;
            while ((n = [input read:buffer maxLength:sizeof(buffer)]) > 0) {
                read += static_cast<std::uint64_t>(n);
                CC_SHA256_Update(&file, buffer, static_cast<CC_LONG>(n));
                if (read > size) break;
            }
            [input close];
            NSDictionary<NSFileAttributeKey, id>* after = [manager attributesOfItemAtPath:path error:nil];
            if (n < 0 || read != size || !after ||
                ![after[NSFileModificationDate] isEqual:before[NSFileModificationDate]] ||
                [after[NSFileSize] unsignedLongLongValue] != size) return false;
            CC_SHA256_Final(bytes, &file);
            std::uint8_t length[4], fileSize[8];
            for (unsigned i = 0; i < 4; ++i) length[i] = static_cast<std::uint8_t>(key.length >> (24 - i * 8));
            for (unsigned i = 0; i < 8; ++i) fileSize[i] = static_cast<std::uint8_t>(size >> (56 - i * 8));
            CC_SHA256_Update(&tree, length, sizeof(length));
            CC_SHA256_Update(&tree, key.bytes, static_cast<CC_LONG>(key.length));
            CC_SHA256_Update(&tree, fileSize, sizeof(fileSize));
            CC_SHA256_Update(&tree, bytes, sizeof(bytes));
        }
    }
    CC_SHA256_Final(output.data(), &tree);
    return true;
}
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
    CompatibilityInfo _identity;
    BOOL _checked;
    BOOL _closed;
    BOOL _away;
}
@property(nonatomic, strong) UILabel* status;
@property(nonatomic, strong) UITextView* code;
@property(nonatomic, strong) UIButton* hostButton;
@property(nonatomic, strong) UIButton* joinButton;
@property(nonatomic, strong) UIButton* clipboardButton;
@property(nonatomic, strong) UIButton* pasteButton;
@property(nonatomic, strong) UIButton* leaveButton;
@property(nonatomic, strong) NSTimer* timer;
@end

static NectarCoopRoomController* sRoomController;

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
    title.text = @"Online Co-op — Connection Test";
    title.font = [UIFont preferredFontForTextStyle:UIFontTextStyleTitle2];
    title.numberOfLines = 0;
    UILabel* explanation = [UILabel new];
    explanation.text = @"Connect both phones to the same Wi-Fi. Host a private room, then copy its code to the other phone. This checks the connection only; it does not start co-op gameplay or change your save.";
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
    UIButton* done = [self button:@"Done" action:@selector(closeScreen)];
    UIStackView* actions = [[UIStackView alloc] initWithArrangedSubviews:@[self.hostButton, self.joinButton]];
    actions.distribution = UIStackViewDistributionFillEqually;
    UIStackView* editing = [[UIStackView alloc] initWithArrangedSubviews:@[self.clipboardButton, self.pasteButton]];
    editing.distribution = UIStackViewDistributionFillEqually;
    UIStackView* ending = [[UIStackView alloc] initWithArrangedSubviews:@[self.leaveButton, done]];
    ending.distribution = UIStackViewDistributionFillEqually;
    UIStackView* content = [[UIStackView alloc] initWithArrangedSubviews:@[title, explanation, self.status, actions, self.code, editing, ending]];
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
            const bool ok = contentIdentity(data, digest);
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
    self.clipboardButton.enabled = static_cast<bool>(_host) && self.code.text.length > 0;
    self.pasteButton.enabled = _checked && !busy;
    self.code.editable = _checked && !busy;
    self.leaveButton.enabled = busy;
}
- (void)stopConnection {
    // No CoopSession borrows these links yet; future session must end FIRST.
    if (_guest) _guest->cancel();
    if (_host) _host->close();
    _guest.reset(); _host.reset();
    self.code.text = @"";
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
    _guest = std::make_unique<GuestJoin>();
    const auto failure = _guest->start(code.UTF8String, _identity, 1, unixSeconds(), nowMs());
    if (failure != JoinFailure::None) {
        NSString* reason = joinError(failure, _guest->incompatibility());
        [self stopConnection]; self.status.text = reason; return;
    }
    self.status.text = @"Connecting… Allow Local Network access if asked.";
    [self updateButtons];
}
- (void)pump:(NSTimer*)timer {
    (void)timer;
    if (_closed || _away) return;
    GatedTransport* link = nullptr;
    if (_host) {
        TransportEvent event;
        for (int count = 0; count < 64 && _host->transport()->poll(event); ++count) {}
        link = _host->transport();
        if (link->state() == TransportState::Failed) {
            [self stopConnection];
            self.status.text = @"The room connection stopped. Check Wi-Fi and Local Network access, then host again.";
            return;
        }
        if (link->state() == TransportState::Listening)
            self.status.text = @"Room open. Waiting for the other phone. Copy this code again if you reconnect.";
    } else if (_guest) {
        TransportEvent event; bool hasEvent = false;
        const auto progress = _guest->poll(nowMs(), event, hasEvent);
        if (progress == JoinProgress::Failed) {
            NSString* reason = joinError(_guest->failure(), _guest->incompatibility());
            [self stopConnection]; self.status.text = reason; return;
        }
        link = _guest->transport();
    }
    if (link && link->state() == TransportState::Connected) {
        TransportStats stats;
        if (link->stats(stats) && stats.rttMs >= 0)
            self.status.text = [NSString stringWithFormat:@"Connected — same build and game data. Delay: %d ms. Connection check passed; co-op gameplay is still being developed.", stats.rttMs];
        else self.status.text = @"Connected — same build and game data. Connection check passed; co-op gameplay is still being developed.";
    }
}
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
        _host->transport()->disconnectPeer(false);
        self.status.text = @"Room kept open. Return here after sharing the code, before your partner joins.";
    } else if (_guest) {
        [self stopConnection];
        self.status.text = @"Connection closed while the app was away. Join again when both phones are ready.";
    }
}
- (void)foregrounded:(NSNotification*)notification {
    (void)notification;
    _away = NO;
    if (_host) self.status.text = @"Room open. Your partner can join now. Leave this screen open.";
}
- (void)closeScreen {
    _closed = YES;
    [self stopConnection];
    [self.timer invalidate]; self.timer = nil;
    [NSNotificationCenter.defaultCenter removeObserver:self];
    [self dismissViewControllerAnimated:YES completion:^{ sRoomController = nil; }];
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
        [presenter presentViewController:sRoomController animated:YES completion:nil];
    });
}
