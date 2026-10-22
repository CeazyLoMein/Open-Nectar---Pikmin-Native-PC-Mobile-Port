"""Restore approved loose PNG icons into an unsigned game bundle before IPA creation."""
import argparse
from pathlib import Path
import shutil
from verify_bundle_info import validate


def prepare(app, game, variant='standard'):
    app = Path(app)
    if (app/'_CodeSignature').exists() or (app/'embedded.mobileprovision').exists():
        raise ValueError('Icon preparation requires an unsigned build bundle')
    validate(app/'Info.plist', game, variant=variant)
    icons = sorted((Path(__file__).parent/'icons'/game).glob('Icon-*.png'))
    if len(icons) != 6:
        raise ValueError('Expected six approved iPhone PNG source icons')
    # Xcode can combine @2x/@3x files into TIFFs. Copy the original PNGs
    # after Xcode finishes so its image transformations cannot remove them.
    for icon in icons:
        shutil.copyfile(icon, app/icon.name)
    validate(app/'Info.plist', game, require_binary=True, variant=variant)
    return [icon.name for icon in icons]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('app', type=Path)
    parser.add_argument('--game', required=True, choices=['pikmin1', 'pikmin2'])
    parser.add_argument('--variant', default='standard', choices=['standard', 'solo-test', 'solo-update'])
    args = parser.parse_args()
    try:
        names = prepare(args.app, args.game, args.variant)
    except (OSError, ValueError) as error:
        parser.exit(1, f'iOS icon preparation failed: {error}\n')
    print(f'Prepared and validated {len(names)} original PNG icons for {args.game}')
