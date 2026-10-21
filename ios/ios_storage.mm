#import <Foundation/Foundation.h>
#include <cstdio>
#include <cstdlib>
#include <unistd.h>
#include "pikmin1_ios_profile.h"
#if NECTAR_P1_SOLO_TEST
#include "pikmin1_solo_test_profile.h"
#include "pikmin1_solo_app_policy.h"
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
#if NECTAR_P1_SOLO_UPDATE
        constexpr bool updateExisting=true;
#else
        constexpr bool updateExisting=false;
#endif
        const char* actualID=[NSBundle mainBundle].bundleIdentifier.UTF8String;
        if (![gameName isEqualToString:@"pikmin1"] || !actualID ||
            !nectar_ios::solo_bundle_matches(actualID, nectar_ios::solo_bundle_id(updateExisting))) {
            fprintf(stderr, "[P1 Solo Test] Wrong bundle identity; storage preparation refused.\n");
            return 0;
        }
        storageName = [NSString stringWithUTF8String:nectar_ios::solo_storage_name(updateExisting)];
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
        NSString* cardRoot = [directory stringByAppendingPathComponent:
            [NSString stringWithUTF8String:nectar_ios::solo_card_directory(updateExisting)]];
        if (setenv("NECTAR_SAVE_DIR", cardRoot.fileSystemRepresentation, 1) != 0) return 0;
        NSString* notice = [directory stringByAppendingPathComponent:@"P1 SOLO TEST - READ ME.txt"];
        if (![[NSFileManager defaultManager] fileExistsAtPath:notice]) {
            [@"P1 solo systems test. Normal/Standard new files supply Day2, the engine and 100 leaf Pikmin per Onion.\n"
              "The update uses existing assets/settings with a separate save-solo-test card folder.\n"
              "Use familiar earlier areas. Final boss/ending testing is deferred to preserve your surprise.\n"
              "End the day, save normally, reload and compare inventory: no new-file refills should occur.\n"
              "Artificial presets do not verify normal unlock progression or full campaign completion.\n"
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
