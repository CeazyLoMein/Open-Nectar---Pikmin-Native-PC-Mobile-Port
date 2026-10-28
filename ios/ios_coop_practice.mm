#import <UIKit/UIKit.h>
#import "ios_coop_style.h"
#include "netplay/pc_coop_practice_bridge.h"

@interface NectarPracticeController : UIViewController
@property(nonatomic,strong) UILabel* status;
@property(nonatomic,strong) UIButton* ready;
@property(nonatomic,strong) NSTimer* timer;
@end
static NectarPracticeController* sPracticePanel;
@implementation NectarPracticeController
- (UIButton*)button:(NSString*)text action:(SEL)action {
    UIButton* b=[UIButton buttonWithType:UIButtonTypeSystem];
    [b setTitle:text forState:UIControlStateNormal];
    b.titleLabel.font=[UIFont preferredFontForTextStyle:UIFontTextStyleHeadline];
    nectarCoopStyleButton(b);
    [b addTarget:self action:action forControlEvents:UIControlEventTouchUpInside];
    [b.heightAnchor constraintGreaterThanOrEqualToConstant:48].active=YES;return b;
}
- (void)viewDidLoad {
    [super viewDidLoad];self.modalInPresentation=YES;
    self.view.backgroundColor=nectarCoopBackground();
    UILabel* title=[UILabel new];title.text=@"Online Co-op â€” Practice";
    title.font=[UIFont preferredFontForTextStyle:UIFontTextStyleTitle2];
    nectarCoopStyleLabel(title);
    self.status=[UILabel new];self.status.numberOfLines=0;
    nectarCoopStyleLabel(self.status);
    self.status.font=[UIFont preferredFontForTextStyle:UIFontTextStyleBody];
    self.ready=[self button:@"Ready / Resume" action:@selector(resumePractice)];
    UIButton* view=[self button:@"View Practice Area" action:@selector(closePanel)];
    UIButton* leave=[self button:@"End Practice" action:@selector(endPractice)];
    UIStackView* stack=[[UIStackView alloc] initWithArrangedSubviews:@[title,self.status,self.ready,view,leave]];
    stack.axis=UILayoutConstraintAxisVertical;stack.spacing=18;stack.translatesAutoresizingMaskIntoConstraints=NO;
    UIScrollView* scroll=[UIScrollView new];scroll.translatesAutoresizingMaskIntoConstraints=NO;
    [self.view addSubview:scroll];[scroll addSubview:stack];
    [NSLayoutConstraint activateConstraints:@[
        [scroll.leadingAnchor constraintEqualToAnchor:self.view.safeAreaLayoutGuide.leadingAnchor],
        [scroll.trailingAnchor constraintEqualToAnchor:self.view.safeAreaLayoutGuide.trailingAnchor],
        [scroll.topAnchor constraintEqualToAnchor:self.view.safeAreaLayoutGuide.topAnchor],
        [scroll.bottomAnchor constraintEqualToAnchor:self.view.safeAreaLayoutGuide.bottomAnchor],
        [stack.leadingAnchor constraintEqualToAnchor:scroll.contentLayoutGuide.leadingAnchor constant:24],
        [stack.trailingAnchor constraintEqualToAnchor:scroll.contentLayoutGuide.trailingAnchor constant:-24],
        [stack.topAnchor constraintEqualToAnchor:scroll.contentLayoutGuide.topAnchor constant:24],
        [stack.bottomAnchor constraintEqualToAnchor:scroll.contentLayoutGuide.bottomAnchor constant:-16],
        [stack.widthAnchor constraintEqualToAnchor:scroll.frameLayoutGuide.widthAnchor constant:-48]
    ]];
    self.timer=[NSTimer scheduledTimerWithTimeInterval:0.2 target:self selector:@selector(updateStatus:) userInfo:nil repeats:YES];
    [self updateStatus:nil];
}
- (void)updateStatus:(NSTimer*)timer {
    (void)timer;char status[600];pc_coop_practice_status(status,sizeof(status));
    self.status.text=[NSString stringWithUTF8String:status];self.ready.enabled=pc_coop_practice_can_ready();
}
- (void)resumePractice { if(pc_coop_practice_ready()) [self closePanel]; }
- (void)endPractice { if(pc_coop_practice_leave()) [self closePanel]; else [self updateStatus:nil]; }
- (void)closePanel {
    [self.timer invalidate];self.timer=nil;
    [self dismissViewControllerAnimated:YES completion:^{sPracticePanel=nil;}];
}
- (void)dealloc { [self.timer invalidate]; }
@end

// Installed once for the entire admitted session, not owned by a dismissed room
// screen. Background pauses are sent while the link can still deliver them.
@interface NectarPracticeLifecycle : NSObject
@end
@implementation NectarPracticeLifecycle
- (void)away:(NSNotification*)notification { (void)notification;pc_coop_practice_background(true); }
- (void)back:(NSNotification*)notification { (void)notification;pc_coop_practice_background(false); }
@end
extern "C" void nectar_ios_open_coop_practice(void) {
    dispatch_async(dispatch_get_main_queue(), ^{
        static NectarPracticeLifecycle* lifecycle;
        if(!lifecycle) {
            lifecycle=[NectarPracticeLifecycle new];
            [NSNotificationCenter.defaultCenter addObserver:lifecycle selector:@selector(away:) name:UIApplicationWillResignActiveNotification object:nil];
            [NSNotificationCenter.defaultCenter addObserver:lifecycle selector:@selector(back:) name:UIApplicationDidBecomeActiveNotification object:nil];
        }
        if(sPracticePanel) return;
        UIWindow* window=nil;
        for(UIScene* scene in UIApplication.sharedApplication.connectedScenes) {
            if(scene.activationState!=UISceneActivationStateForegroundActive || ![scene isKindOfClass:UIWindowScene.class]) continue;
            for(UIWindow* candidate in ((UIWindowScene*)scene).windows) if(candidate.isKeyWindow) {window=candidate;break;}
            if(window)break;
        }
        UIViewController* presenter=window.rootViewController;
        if(!presenter || presenter.presentedViewController || presenter.isBeingPresented || presenter.isBeingDismissed) return;
        sPracticePanel=[NectarPracticeController new];sPracticePanel.modalPresentationStyle=UIModalPresentationOverFullScreen;
        [presenter presentViewController:sPracticePanel animated:YES completion:nil];
    });
}
