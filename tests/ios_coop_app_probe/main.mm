#import <UIKit/UIKit.h>
#import <dispatch/dispatch.h>
#include <stdio.h>

#if NECTAR_PROBE_HEALTH
extern "C" int nectar_simulator_health_main(void);
#else
int nectar_coop_socket_probe_main();
#endif

@interface NectarProbeScene : UIResponder <UIWindowSceneDelegate>
@property(nonatomic, strong) UIWindow* window;
@end
@implementation NectarProbeScene
- (void)scene:(UIScene*)scene willConnectToSession:(UISceneSession*)session options:(UISceneConnectionOptions*)options {
    (void)session; (void)options;
    if (![scene isKindOfClass:[UIWindowScene class]]) return;
    self.window = [[UIWindow alloc] initWithWindowScene:(UIWindowScene*)scene];
    self.window.rootViewController = [[UIViewController alloc] init];
    [self.window makeKeyAndVisible];
    // UIKit calls scene connection on the main thread. Run once per process;
    // keep that thread responsive while the unchanged socket fixture runs.
    static BOOL started = NO;
    if (started) return;
    started = YES;
    puts("NECTAR_UIKIT_PROBE_ENTERED"); fflush(stdout);
    dispatch_async(dispatch_get_global_queue(QOS_CLASS_USER_INITIATED, 0), ^{
        @autoreleasepool {
            int code = 1;
            try {
#if NECTAR_PROBE_HEALTH
                code = nectar_simulator_health_main();
#else
                code = nectar_coop_socket_probe_main();
#endif
            } catch (...) {
                puts("FAIL unhandled native test exception");
            }
            fflush(stdout); fflush(stderr);
            printf("NECTAR_UIKIT_PROBE_EXIT %d\n", code);
            fflush(stdout);
        }
    });
}
@end

@interface NectarProbeDelegate : UIResponder <UIApplicationDelegate>
@end
@implementation NectarProbeDelegate
- (UISceneConfiguration*)application:(UIApplication*)application configurationForConnectingSceneSession:(UISceneSession*)session options:(UISceneConnectionOptions*)options {
    (void)application; (void)options;
    UISceneConfiguration* config = [[UISceneConfiguration alloc] initWithName:@"Probe" sessionRole:session.role];
    config.delegateClass = [NectarProbeScene class];
    return config;
}
@end

int main(int argc, char** argv) {
    @autoreleasepool {
        setvbuf(stdout, nullptr, _IOLBF, 0);
        return UIApplicationMain(argc, argv, nil, NSStringFromClass([NectarProbeDelegate class]));
    }
}
