#import <UIKit/UIKit.h>
#import <UniformTypeIdentifiers/UniformTypeIdentifiers.h>
#if NECTAR_IOS_P2_FEATURES
#include "pc_host_alloc.h"
#define PICKER_HOST() PcNativeHostAllocScope pickerHostScope
#else
#define PICKER_HOST() ((void)0)
#endif

extern "C" void nectar_ios_mod_picker_result(int kind, const char* path, const char* error);

@interface NectarModPickerDelegate : NSObject <UIDocumentPickerDelegate, UIAdaptivePresentationControllerDelegate>
@property(nonatomic) int kind;
@property(nonatomic) BOOL finished;
@property(nonatomic) BOOL copying;
@end

static NectarModPickerDelegate* sPickerDelegate;

@implementation NectarModPickerDelegate
- (void)finishWithPath:(NSString*)path error:(NSString*)error {
    PICKER_HOST();
    if (self.finished) return;
    self.finished = YES;
    nectar_ios_mod_picker_result(self.kind, path.fileSystemRepresentation, error.UTF8String);
    sPickerDelegate = nil;
}
- (void)documentPickerWasCancelled:(UIDocumentPickerViewController*)controller {
    PICKER_HOST();
    (void)controller;
    if (self.copying) return;
    [self finishWithPath:nil error:nil];
}
- (void)presentationControllerDidDismiss:(UIPresentationController*)presentationController {
    PICKER_HOST();
    (void)presentationController;
    if (self.copying) return;
    [self finishWithPath:nil error:nil];
}
- (void)documentPicker:(UIDocumentPickerViewController*)controller didPickDocumentsAtURLs:(NSArray<NSURL*>*)urls {
    PICKER_HOST();
    (void)controller;
    if (self.finished || self.copying) return;
    NSURL* source = urls.firstObject;
    if (!source) { [self finishWithPath:nil error:nil]; return; }
    self.copying = YES;
    BOOL scoped = [source startAccessingSecurityScopedResource];
    dispatch_async(dispatch_get_global_queue(QOS_CLASS_USER_INITIATED, 0), ^{
        @autoreleasepool {
            PICKER_HOST();
            NSFileManager* manager = NSFileManager.defaultManager;
            NSString* directory = [NSTemporaryDirectory() stringByAppendingPathComponent:
                [@"NectarModImport." stringByAppendingString:NSUUID.UUID.UUIDString]];
            NSString* name = source.lastPathComponent;
            NSError* error = nil;
            NSString* path = [directory stringByAppendingPathComponent:name ?: @"import.zip"];
            BOOL copied = name.length && [manager createDirectoryAtPath:directory
                withIntermediateDirectories:YES attributes:nil error:&error] &&
                [manager copyItemAtURL:source toURL:[NSURL fileURLWithPath:path] error:&error];
            if (scoped) [source stopAccessingSecurityScopedResource];
            if (!copied) {
                [manager removeItemAtPath:directory error:nil];
                NSString* reason = error.localizedDescription ?: @"Could not copy the selected ZIP.";
                dispatch_async(dispatch_get_main_queue(), ^{
                    PICKER_HOST();
                    [self finishWithPath:nil error:reason];
                });
                return;
            }
            dispatch_async(dispatch_get_main_queue(), ^{
                PICKER_HOST();
                [self finishWithPath:path error:nil];
            });
        }
    });
}
@end

extern "C" void nectar_ios_open_mod_picker(int kind) {
    dispatch_async(dispatch_get_main_queue(), ^{
        PICKER_HOST();
        if (sPickerDelegate) {
            nectar_ios_mod_picker_result(kind, nullptr, "An import picker is already open.");
            return;
        }
        UIWindow* window = nil;
        for (UIScene* scene in UIApplication.sharedApplication.connectedScenes) {
            if (scene.activationState != UISceneActivationStateForegroundActive ||
                ![scene isKindOfClass:UIWindowScene.class]) continue;
            for (UIWindow* candidate in ((UIWindowScene*)scene).windows) {
                if (candidate.isKeyWindow) { window = candidate; break; }
            }
            if (window) break;
        }
        // SDL's legacy UIApplicationDelegate does not require scene manifests.
        if (!window) {
            for (UIWindow* candidate in UIApplication.sharedApplication.windows) {
                if (candidate.isKeyWindow) { window = candidate; break; }
            }
        }
        UIViewController* presenter = window.rootViewController;
        while (presenter.presentedViewController && !presenter.presentedViewController.isBeingDismissed)
            presenter = presenter.presentedViewController;
        if (!presenter || presenter.presentedViewController ||
            presenter.isBeingDismissed || presenter.isBeingPresented) {
            nectar_ios_mod_picker_result(kind, nullptr, "Cannot open Files right now. Try again from the settings menu.");
            return;
        }
        NectarModPickerDelegate* delegate = [NectarModPickerDelegate new];
        delegate.kind = kind;
        sPickerDelegate = delegate;
        UIDocumentPickerViewController* picker = [[UIDocumentPickerViewController alloc]
            initForOpeningContentTypes:@[UTTypeZIP] asCopy:YES];
        picker.delegate = delegate;
        picker.allowsMultipleSelection = NO;
        picker.modalPresentationStyle = UIModalPresentationFormSheet;
        picker.presentationController.delegate = delegate;
        [presenter presentViewController:picker animated:YES completion:nil];
    });
}

extern "C" void nectar_ios_cleanup_mod_import(const char* importedPath) {
    @autoreleasepool {
        PICKER_HOST();
        if (!importedPath) return;
        NSString* path = [[NSString stringWithUTF8String:importedPath] stringByStandardizingPath];
        NSString* parent = path.stringByDeletingLastPathComponent;
        NSString* temporary = [NSTemporaryDirectory() stringByStandardizingPath];
        // Remove only our own single import directory, never the chosen source.
        if ([parent.stringByDeletingLastPathComponent isEqualToString:temporary] &&
            [parent.lastPathComponent hasPrefix:@"NectarModImport."])
            [NSFileManager.defaultManager removeItemAtPath:parent error:nil];
    }
}
