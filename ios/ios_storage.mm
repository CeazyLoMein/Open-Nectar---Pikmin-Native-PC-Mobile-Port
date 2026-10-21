#import <Foundation/Foundation.h>
#include <cstdio>
#include <cstdlib>
#include <unistd.h>
#include "pikmin1_ios_profile.h"
#if NECTAR_P1_SOLO_TEST
#include "pikmin1_solo_test_profile.h"
#endif
#if NECTAR_IOS_P2_FEATURES
#include "pikmin2_ios_profile.h"
#endif

static void preparePikmin1Enhancements(NSString* directory)
{
    NSFileManager* manager = [NSFileManager defaultManager];
    NSString* configPath = [directory stringByAppendingPathComponent:@"pikmin_settings.conf"];
    BOOL existed = [manager fileExistsAtPath:configPath];
    NSError* error = nil;
    NSData* data = existed ? [NSData dataWithContentsOfFile:configPath options:0 error:&error] : nil;
    if (existed && !data) {
        fprintf(stderr, "[iOS] Settings unreadable; enhancement profile skipped.\n");
        return;
    }
    std::string original = data.length ? std::string((const char*)data.bytes, data.length) : std::string();
#if NECTAR_P1_SOLO_TEST
    const auto profile = nectar_ios::apply_pikmin1_solo_test_profile(original);
#else
    const auto profile = nectar_ios::apply_pikmin1_enhanced_profile(original);
#endif
    if (profile.changed) {
        NSString* backup = [directory stringByAppendingPathComponent:@"pikmin_settings.before-ios-enhanced-v1.conf"];
        if (existed && ![manager fileExistsAtPath:backup] &&
            ![manager copyItemAtPath:configPath toPath:backup error:&error]) {
            fprintf(stderr, "[iOS] Settings backup failed; enhancement profile skipped.\n");
            return;
        }
        NSData* updated = [NSData dataWithBytes:profile.text.data() length:profile.text.size()];
        if (![updated writeToFile:configPath options:NSDataWritingAtomic error:&error]) {
            fprintf(stderr, "[iOS] Could not write enhancement profile: %s\n", error.localizedDescription.UTF8String);
            return;
        }
        fprintf(stderr, "[iOS] Applied enhanced Pikmin 1 profile; later menu choices are preserved.\n");
    }
    for (NSString* subdirectory in @[@"Load/Textures", @"Load/Models"]) {
        [manager createDirectoryAtPath:[directory stringByAppendingPathComponent:subdirectory]
           withIntermediateDirectories:YES attributes:nil error:nil];
    }
}

#if NECTAR_IOS_P2_FEATURES
static void preparePikmin2Enhancements(NSString* directory)
{
    NSFileManager* manager = [NSFileManager defaultManager];
    NSString* configPath = [directory stringByAppendingPathComponent:@"pikmin_settings.conf"];
    BOOL existed = [manager fileExistsAtPath:configPath];
    NSError* error = nil;
    NSData* data = existed ? [NSData dataWithContentsOfFile:configPath options:0 error:&error] : nil;
    if (existed && !data) {
        fprintf(stderr, "[iOS] Settings unreadable; enhancement profile skipped.\n");
        return;
    }
    std::string original = data.length ? std::string((const char*)data.bytes, data.length) : std::string();
    const auto profile = nectar_ios_p2::apply_pikmin2_enhanced_profile(original);
    if (profile.changed) {
        NSString* backup = [directory stringByAppendingPathComponent:@"pikmin_settings.before-ios-enhanced-p2-v1.conf"];
        if (existed && ![manager fileExistsAtPath:backup] &&
            ![manager copyItemAtPath:configPath toPath:backup error:&error]) {
            fprintf(stderr, "[iOS] Settings backup failed; enhancement profile skipped.\n");
            return;
        }
        NSData* updated = [NSData dataWithBytes:profile.text.data() length:profile.text.size()];
        if (![updated writeToFile:configPath options:NSDataWritingAtomic error:&error]) {
            fprintf(stderr, "[iOS] Could not write enhancement profile: %s\n", error.localizedDescription.UTF8String);
            return;
        }
        fprintf(stderr, "[iOS] Applied enhanced Pikmin 2 profile; later menu choices are preserved.\n");
    }
    for (NSString* subdirectory in @[@"Load/Textures", @"Load/Models"]) {
        [manager createDirectoryAtPath:[directory stringByAppendingPathComponent:subdirectory]
           withIntermediateDirectories:YES attributes:nil error:nil];
    }
}

#endif

// This first-phase port expects extracted PC-game assets, NOT an ISO, in:
// Files > On My iPhone > Open Nectar Pikmin [1/2] > pikmin[1/2] > assets
// It uses a per-game Documents dir, so relative asset/save/config paths used
// by the existing native game have a writable parent. P1 mods use a separate ZIP picker.
extern "C" int nectar_ios_prepare_storage(const char* game)
{
    @autoreleasepool {
        if (!game || ![NSString stringWithUTF8String:game]) return 0;
        NSString* gameName = [NSString stringWithUTF8String:game];
        NSString* storageName = gameName;
#if NECTAR_P1_SOLO_TEST
        // Signing must retain the separate test identity. This guard also
        // prevents test setup from running under a regular app identity.
        if (![gameName isEqualToString:@"pikmin1"] ||
            ![[NSBundle mainBundle].bundleIdentifier isEqualToString:@"org.opennectar.experimental.pikmin1.solotest"]) {
            fprintf(stderr, "[P1 Solo Test] Wrong bundle identity; storage preparation refused.\n");
            return 0;
        }
        storageName = @"pikmin1-solo-test";
#endif
        NSString* directory = [[NSHomeDirectory() stringByAppendingPathComponent:@"Documents"]
                                  stringByAppendingPathComponent:storageName];
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
#if NECTAR_P1_SOLO_TEST
        // Pin cards inside the disposable root; bypass desktop legacy-card discovery.
        NSString* cardRoot = [directory stringByAppendingPathComponent:@"save"];
        if (setenv("NECTAR_SAVE_DIR", cardRoot.fileSystemRepresentation, 1) != 0) return 0;
        NSString* notice = [directory stringByAppendingPathComponent:@"P1 SOLO TEST - READ ME.txt"];
        if (![[NSFileManager defaultManager] fileExistsAtPath:notice]) {
            [@"P1 Solo Test: separate disposable app. Do not import a real save.\n"
              "Start a NEW Normal/Standard story: slot A or C = areas and systems; slot B = 29-part finale preset.\n"
              "All areas are selectable; 100 leaf Pikmin per Onion are supplied once per new test file.\n"
              "Slot B leaves the real final boss, Secret Safe delivery and ending to play normally.\n"
              "Save normally at sunset and reload: stocks must not reset on reload.\n"
              "Test-only setup is not evidence of normal unlock progression or full campaign completion.\n"
              "Assets/art/Load must be copied locally into this test folder. Keep the original app alone.\n"
              writeToFile:notice atomically:YES encoding:NSUTF8StringEncoding error:nil];
        }
#endif
        fprintf(stderr, "[iOS] Working directory: %s\n", [directory fileSystemRepresentation]);
        if (![[NSFileManager defaultManager] fileExistsAtPath:
                [directory stringByAppendingPathComponent:@"assets"]]) {
            fprintf(stderr, "[iOS] No assets yet. Copy extracted game assets into Documents/%s/assets.\n", game);
        }
        if ([gameName isEqualToString:@"pikmin1"]) preparePikmin1Enhancements(directory);
#if NECTAR_IOS_P2_FEATURES
        if ([gameName isEqualToString:@"pikmin2"]) preparePikmin2Enhancements(directory);
#endif
        return 1;
    }
}
