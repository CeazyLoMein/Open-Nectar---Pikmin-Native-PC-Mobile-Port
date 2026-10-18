#import <Foundation/Foundation.h>
#include <cstdio>
#include <unistd.h>

// This first-phase port expects extracted PC-game assets, NOT an ISO, in:
// Files > On My iPhone > Open Nectar Pikmin [1/2] > pikmin[1/2] > assets
// It uses a per-game Documents dir, so relative asset/save/config paths used
// by the existing native game have a writable parent. Import UI comes later.
extern "C" int nectar_ios_prepare_storage(const char* game)
{
    @autoreleasepool {
        if (!game || ![NSString stringWithUTF8String:game]) return 0;
        NSString* gameName = [NSString stringWithUTF8String:game];
        NSString* directory = [[NSHomeDirectory() stringByAppendingPathComponent:@"Documents"]
                                  stringByAppendingPathComponent:gameName];
        NSError* error = nil;
        if (![[NSFileManager defaultManager] createDirectoryAtPath:directory
                                       withIntermediateDirectories:YES
                                                        attributes:nil error:&error]) {
            fprintf(stderr, "[iOS] Cannot create Documents/%s: %s\n", game,
                    [[error description] UTF8String]);
            return 0;
        }
        if (chdir([directory fileSystemRepresentation]) != 0) {
            fprintf(stderr, "[iOS] Cannot chdir to Documents/%s\n", game);
            return 0;
        }
        fprintf(stderr, "[iOS] Working directory: %s\n", [directory fileSystemRepresentation]);
        if (![[NSFileManager defaultManager] fileExistsAtPath:
                [directory stringByAppendingPathComponent:@"assets"]]) {
            fprintf(stderr, "[iOS] No assets yet. Copy extracted game assets into Documents/%s/assets.\n", game);
        }
        return 1;
    }
}
