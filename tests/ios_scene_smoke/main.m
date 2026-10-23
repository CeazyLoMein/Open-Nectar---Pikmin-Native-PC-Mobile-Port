// Asset-free runtime probe of the same SDL scene startup used by both games.
#import <UIKit/UIKit.h>
#include <SDL.h>
#include <SDL_main.h>
#include <SDL_syswm.h>
#include <stdio.h>

@protocol NectarSceneProbe
- (void)nectarConnectWindowScene:(UIWindowScene *)scene;
- (void)postFinishLaunch;
@end
static int entries, willBackground, didBackground, willForeground, didForeground;
static UIWindow *nativeWindow;
static BOOL ready, reconnectOK, foreignIgnored;
static NSString *failure;
static NSString *phase = @"process-entry";
static NSArray *exceptionStack;
static void report(void)
{
    @autoreleasepool {
        UIWindowScene *scene = nativeWindow.windowScene;
        CGRect bounds = nativeWindow ? nativeWindow.bounds : CGRectZero;
        NSDictionary *state = @{
            @"entry_count": @(entries), @"ready": @(ready), @"error": failure ?: @"",
            @"phase": phase, @"exception_stack": exceptionStack ?: @[],
            @"window_has_scene": @(scene != nil),
            @"scene_delegate": scene ? NSStringFromClass(scene.delegate.class) : @"",
            @"width": @(bounds.size.width), @"height": @(bounds.size.height),
            @"active": @(scene.activationState == UISceneActivationStateForegroundActive),
            @"reconnect_preserved_window": @(reconnectOK), @"foreign_events_ignored": @(foreignIgnored),
            @"will_background": @(willBackground), @"did_background": @(didBackground),
            @"will_foreground": @(willForeground), @"did_foreground": @(didForeground)
        };
        NSURL *folder = [[NSFileManager defaultManager] URLsForDirectory:NSDocumentDirectory inDomains:NSUserDomainMask].firstObject;
        [[NSFileManager defaultManager] createDirectoryAtURL:folder withIntermediateDirectories:YES attributes:nil error:nil];
        NSData *json = [NSJSONSerialization dataWithJSONObject:state options:NSJSONWritingPrettyPrinted error:nil];
        NSError *writeError = nil;
        if (![json writeToURL:[folder URLByAppendingPathComponent:@"scene-smoke.json"] options:NSDataWritingAtomic error:&writeError]) {
            fprintf(stderr, "NECTAR_PROBE report write failed: %s\n", writeError.description.UTF8String);
            fflush(stderr);
        }
    }
}
static void checkpoint(NSString *next)
{
    phase = next;
    fprintf(stderr, "NECTAR_PROBE phase=%s\n", phase.UTF8String);
    fflush(stderr);
    report();
}
static void uncaughtException(NSException *exception)
{
    failure = [NSString stringWithFormat:@"%@: %@", exception.name, exception.reason];
    exceptionStack = exception.callStackSymbols;
    fprintf(stderr, "NECTAR_PROBE exception: %s\n%s\n", failure.UTF8String,
            [exceptionStack componentsJoinedByString:@"\n"].UTF8String);
    fflush(stderr);
    report();
}
static int SDLCALL lifecycle(void *unused, SDL_Event *event)
{
    switch (event->type) {
    case SDL_APP_WILLENTERBACKGROUND: ++willBackground; break;
    case SDL_APP_DIDENTERBACKGROUND: ++didBackground; break;
    case SDL_APP_WILLENTERFOREGROUND: ++willForeground; break;
    case SDL_APP_DIDENTERFOREGROUND: ++didForeground; break;
    default: return 1;
    }
    report(); // Synchronous record before iOS can suspend the process.
    return 1;
}
static int scene_main(int argc, char **argv)
{
    if (++entries != 1) { failure = @"Game entry was invoked twice"; report(); return 1; }
    checkpoint(@"before-sdl-init");
    if (SDL_Init(SDL_INIT_VIDEO | SDL_INIT_EVENTS) != 0) { failure = @(SDL_GetError()); report(); return 1; }
    checkpoint(@"sdl-initialized");
    SDL_AddEventWatch(lifecycle, NULL);
    SDL_Window *window = SDL_CreateWindow("Nectar Scene Probe", 0, 0, 932, 430,
        SDL_WINDOW_SHOWN | SDL_WINDOW_RESIZABLE | SDL_WINDOW_ALLOW_HIGHDPI | SDL_WINDOW_BORDERLESS);
    if (!window) { failure = @(SDL_GetError()); report(); return 1; }
    checkpoint(@"window-created");
    SDL_SysWMinfo info;
    SDL_VERSION(&info.version);
    if (!SDL_GetWindowWMInfo(window, &info) || info.subsystem != SDL_SYSWM_UIKIT) {
        failure = @"No native SDL UIKit window"; report(); return 1;
    }
    nativeWindow = info.info.uikit.window;
    if (!nativeWindow.windowScene || !nativeWindow.rootViewController) {
        failure = @"Game window is not attached to the connected scene"; report(); return 1;
    }
    checkpoint(@"native-window-attached");
    id<NectarSceneProbe> app = (id<NectarSceneProbe>)[UIApplication sharedApplication].delegate;
    [app nectarConnectWindowScene:nativeWindow.windowScene];
    [app postFinishLaunch]; // A duplicate entry callback must also be harmless.
    SDL_SysWMinfo after;
    SDL_VERSION(&after.version);
    reconnectOK = SDL_GetWindowWMInfo(window, &after) && after.info.uikit.window == nativeWindow && entries == 1;
    checkpoint(@"reconnect-checked");
    const int before = willBackground + didBackground + willForeground + didForeground;
    for (NSNotificationName name in @[UISceneDidActivateNotification, UISceneWillDeactivateNotification,
                                      UISceneDidEnterBackgroundNotification, UISceneWillEnterForegroundNotification]) {
        [[NSNotificationCenter defaultCenter] postNotificationName:name object:[NSObject new]];
    }
    foreignIgnored = before == willBackground + didBackground + willForeground + didForeground;
    ready = YES;
    checkpoint(@"running");
    const Uint32 start = SDL_GetTicks();
    while (SDL_GetTicks() - start < 180000) {
        @autoreleasepool {
            SDL_Event event;
            while (SDL_PollEvent(&event)) { }
            report();
            SDL_Delay(50);
        }
    }
    SDL_DelEventWatch(lifecycle, NULL);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}
int main(int argc, char **argv)
{
    @autoreleasepool {
        NSSetUncaughtExceptionHandler(uncaughtException);
        checkpoint(@"process-entry");
        return SDL_UIKitRunApp(argc, argv, scene_main);
    }
}
