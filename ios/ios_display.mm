// UIKit must remain outside the game target's forced GameCube BOOL headers.
#import <UIKit/UIKit.h>
#include <SDL.h>
#include <SDL_syswm.h>
#include "pc_mobile_layout.h"

PcMobileInsets pc_mobile_safe_insets()
{
    // SDL's game/render loop runs on the UIKit thread. Never consult a cached
    // main screen: a fold or a rotated landscape window can change these values.
    SDL_Window* window = SDL_GL_GetCurrentWindow();
    if (!window || ![NSThread isMainThread]) return {};
    SDL_SysWMinfo info;
    SDL_VERSION(&info.version);
    if (!SDL_GetWindowWMInfo(window, &info) || info.subsystem != SDL_SYSWM_UIKIT) return {};
    UIWindow* nativeWindow = info.info.uikit.window;
    UIView* view = nativeWindow.rootViewController.view;
    if (!view) return {};
    const CGSize size = view.bounds.size;
    if (size.width <= 0 || size.height <= 0) return {};
    const UIEdgeInsets insets = view.safeAreaInsets;
    return {float(insets.left / size.width), float(insets.top / size.height),
            float(insets.right / size.width), float(insets.bottom / size.height)};
}
