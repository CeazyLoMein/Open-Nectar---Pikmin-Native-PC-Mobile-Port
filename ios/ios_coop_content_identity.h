#pragma once
#import <Foundation/Foundation.h>
#import <CommonCrypto/CommonDigest.h>
#include <array>
#include <cstdint>

namespace nectar_ios {
// Preserve original paths for file I/O; normalize only the identity key.
// NFC and NFD encode identical Japanese characters differently on the two phones.
inline NSString* canonicalContentName(NSString* name) {
    return [name precomposedStringWithCanonicalMapping];
}

// Immutable base game data only. No reading/writing cards, settings or personal files.
// Cosmetic replacements may differ. Runtime gameplay options need a separate gate
// before a later build can START a shared simulation; this screen cannot do that.
inline bool contentIdentity(NSURL* root, std::array<std::uint8_t, 32>& output) {
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
    NSMutableDictionary<NSString*, NSString*>* originalNames = [NSMutableDictionary dictionary];
    NSString* prefix = [root.path stringByAppendingString:@"/"];
    for (NSURL* url in enumerator) {
        NSNumber* regular = nil;
        NSNumber* directory = nil;
        NSNumber* link = nil;
        if (![url.path hasPrefix:prefix] ||
            ![url getResourceValue:&link forKey:NSURLIsSymbolicLinkKey error:nil] || link.boolValue ||
            ![url getResourceValue:&regular forKey:NSURLIsRegularFileKey error:nil] ||
            ![url getResourceValue:&directory forKey:NSURLIsDirectoryKey error:nil]) return false;
        if (regular.boolValue) {
            NSString* original = [url.path substringFromIndex:prefix.length];
            NSString* canonical = canonicalContentName(original);
            // Different spellings of the same Unicode name hash identically.
            // Ambiguous aliases in one tree are rejected instead of overwritten.
            if (!canonical || originalNames[canonical]) return false;
            originalNames[canonical] = original;
            [names addObject:canonical];
        }
        else if (!directory.boolValue) return false;
        if (names.count > 100000) return false;
    }
    if (enumerationFailed || !names.count) return false;
    [names sortUsingComparator:^NSComparisonResult(NSString* a, NSString* b) {
        return [a compare:b options:NSLiteralSearch];
    }];
    CC_SHA256_CTX tree;
    CC_SHA256_Init(&tree);
    const char domain[] = "NECTAR-P1-DATA-v2";
    CC_SHA256_Update(&tree, domain, sizeof(domain));
    std::uint64_t total = 0;
    for (NSString* name in names) {
        @autoreleasepool {
            NSData* key = [name dataUsingEncoding:NSUTF8StringEncoding];
            if (!key || key.length > 16384) return false;
            NSString* path = [root.path stringByAppendingPathComponent:originalNames[name]];
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
} // namespace nectar_ios
