// iOS UIApplication lifecycle entry: SDL owns UIKit; the game provides the callback.
// We intentionally disable SDL2main in the vendored SDL static library to avoid
// duplicate symbols for main(). See SDL2/README-ios (SDL_UIKitRunApp).
#import <SDL.h>
#import <SDL_main.h>
extern int nectar_game_main(int argc, char* argv[]);

int main(int argc, char* argv[])
{
    @autoreleasepool {
        return SDL_UIKitRunApp(argc, argv, nectar_game_main);
    }
}
