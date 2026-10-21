# Personal iOS Home Screen artwork

AI-generated game-themed artwork, created with the built-in image_gen tool on2026-10-21. User explicitly approved the generated pictures. Not official Nintendo cover art or extracted game assets. Full exact prompt set in prompts.json.

Each game has an opaque RGB1024px Artwork.png master and six icon PNG sizes:29pt@2x/3x,40pt@2x/3x and60pt@2x/3x. Only Icon-*.png are copied into the app root. Original1254px generated files remain preserved in the local workspace outputs and image-generation directory. Standard image resampling/opaque RGB encoding prepared iPhone resource sizes without creative alterations.

Info.plist uses CFBundleIcons > CFBundlePrimaryIcon > CFBundleIconFiles with Icon-60,Icon-40,Icon-29. Reference: [Apple CFBundleIcons documentation](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html). These loose PNG resources support the existing Xcode/Makefile build paths. No app identity, executable, signing account, save folder or private game assets changed.

ios/CMakeLists.txt copies icons after the target builds; verify_bundle_info.py checks the actual packaged names, dimensions and opaque8-bitRGB headers. Historical pre-icon IPAs use earlier metadata; preserve their existing verification records instead of applying the new strict verifier to old originals.
