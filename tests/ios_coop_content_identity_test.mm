#import <Foundation/Foundation.h>
#include "ios_coop_content_identity.h"
#include <cstdlib>
#include <cstdio>

static void check(bool value, const char* label) {
    if (!value) { std::fprintf(stderr, "FAIL: %s\n", label); std::exit(1); }
}
static void writeFile(NSURL* root, NSString* name, NSData* bytes) {
    NSURL* url = [root URLByAppendingPathComponent:name];
    check([NSFileManager.defaultManager createDirectoryAtURL:[url URLByDeletingLastPathComponent]
        withIntermediateDirectories:YES attributes:nil error:nil], "create fixture parent");
    check([bytes writeToURL:url options:NSDataWritingAtomic error:nil], "write fixture");
}
static std::array<std::uint8_t,32> identity(NSURL* root, const char* label) {
    std::array<std::uint8_t,32> result{};
    nectar_ios::ContentIdentityError error{};
    if (!nectar_ios::contentIdentity(root, result, &error)) {
        std::fprintf(stderr, "FAIL: %s: %s; root=%s; resolved=%s\n", label,
            nectar_ios::contentIdentityErrorName(error), root.path.UTF8String,
            root.URLByResolvingSymlinksInPath.path.UTF8String);
        std::exit(1);
    }
    std::printf("PASS hash: %s\n", label);
    std::fflush(stdout);
    return result;
}
int main() {
    @autoreleasepool {
        NSString* nfc = @"stages/\u30d7\u30ec\u30b9.bin";
        NSString* nfd = [nfc decomposedStringWithCanonicalMapping];
        check([nfc compare:nfd options:NSLiteralSearch] != NSOrderedSame, "fixture uses different encodings");
        check([nectar_ios::canonicalContentName(nfc) isEqualToString:nectar_ios::canonicalContentName(nfd)],
            "canonical names match for actual Japanese decomposition");
        check(![nectar_ios::canonicalContentName(@"Case.bin") isEqualToString:nectar_ios::canonicalContentName(@"case.bin")],
            "case is not folded");
        NSURL* base = [NSURL fileURLWithPath:[NSTemporaryDirectory() stringByAppendingPathComponent:NSUUID.UUID.UUIDString]
            isDirectory:YES];
        NSFileManager* fm = NSFileManager.defaultManager;
        check([fm createDirectoryAtURL:base withIntermediateDirectories:YES attributes:nil error:nil], "create test root");
        @try {
            std::array<std::uint8_t,32> invalid{};
            nectar_ios::ContentIdentityError reason{};
            check(!nectar_ios::contentIdentity(base, invalid, &reason) &&
                reason==nectar_ios::ContentIdentityError::EmptyTree, "empty tree rejected for correct reason");
            check(!nectar_ios::contentIdentity([base URLByAppendingPathComponent:@"missing"], invalid), "missing root rejected");
            const std::uint8_t raw[] = {0,255,1,3};
            NSData* bytes = [NSData dataWithBytes:raw length:sizeof(raw)];
            NSURL* a = [base URLByAppendingPathComponent:@"a" isDirectory:YES];
            NSURL* b = [base URLByAppendingPathComponent:@"b" isDirectory:YES];
            writeFile(a,nfc,bytes); writeFile(a,@"other.bin",[@"same" dataUsingEncoding:NSUTF8StringEncoding]);
            writeFile(b,@"other.bin",[@"same" dataUsingEncoding:NSUTF8StringEncoding]); writeFile(b,nfd,bytes);
            const auto nfcHash = identity(a,"NFC tree");
            const auto nfdHash = identity(b,"NFD tree");
            check(nfcHash==nfdHash, "equivalent filename trees and creation order have same identity");
            const auto baseline = identity(b,"modified/restored/renamed tree");
            // Test the same directory through macOS's /var and /private/var aliases.
            NSString* alternate = nil;
            if ([b.path hasPrefix:@"/private/var/"]) alternate = [b.path substringFromIndex:8];
            else if ([b.path hasPrefix:@"/var/"]) alternate = [@"/private" stringByAppendingString:b.path];
            if (alternate && [fm fileExistsAtPath:alternate]) {
                check(identity([NSURL fileURLWithPath:alternate isDirectory:YES],"same tree through path alias")==baseline,
                    "ancestor aliases do not change content identity");
            }
            writeFile(b,nfd,[@"changed" dataUsingEncoding:NSUTF8StringEncoding]);
            check(identity(b,"modified/restored/renamed tree")!=baseline, "different bytes still rejected");
            writeFile(b,nfd,bytes);
            check(identity(b,"modified/restored/renamed tree")==baseline, "restored content matches");
            check([fm moveItemAtURL:[b URLByAppendingPathComponent:@"other.bin"]
                toURL:[b URLByAppendingPathComponent:@"renamed.bin"] error:nil], "rename fixture");
            check(identity(b,"modified/restored/renamed tree")!=baseline, "real filename changes still rejected");
            NSURL* golden = [base URLByAppendingPathComponent:@"golden" isDirectory:YES];
            writeFile(golden,@"name.bin",bytes);
            const auto hash = identity(golden,"golden/empty/extra tree");
            char hex[65]{};
            for (std::size_t i=0;i<hash.size();++i) std::snprintf(hex+2*i,3,"%02x",static_cast<unsigned>(hash[i]));
            check([[NSString stringWithUTF8String:hex] isEqualToString:@"7bc95658ff552dbfcda6c9e58176dfea2ee419791264f3e5f57bece4ab5987d4"], "independent SHA256/framing golden vector");
            check([fm createDirectoryAtURL:[golden URLByAppendingPathComponent:@"empty"]
                withIntermediateDirectories:YES attributes:nil error:nil], "empty subdirectory fixture");
            check(identity(golden,"golden/empty/extra tree")==hash, "empty directories do not alter content");
            writeFile(golden,@".extra",bytes);
            check(identity(golden,"golden/empty/extra tree")!=hash, "extra hidden file still changes identity");
            NSURL* link = [base URLByAppendingPathComponent:@"root-link"];
            check([fm createSymbolicLinkAtURL:link withDestinationURL:a error:nil], "root symlink fixture");
            check(!nectar_ios::contentIdentity(link,invalid,&reason) &&
                reason==nectar_ios::ContentIdentityError::InvalidRoot, "symlink root rejected");
            check([fm createSymbolicLinkAtURL:[a URLByAppendingPathComponent:@"file-link"]
                withDestinationURL:[a URLByAppendingPathComponent:@"other.bin"] error:nil], "file symlink fixture");
            check(!nectar_ios::contentIdentity(a,invalid,&reason) &&
                reason==nectar_ios::ContentIdentityError::UnsupportedEntry, "symlink entry rejected");
            std::puts("PASS: canonical content identity, real mismatch detection, framing and filesystem safety");
        } @finally {
            check([fm removeItemAtURL:base error:nil], "remove test fixtures");
        }
    }
}
