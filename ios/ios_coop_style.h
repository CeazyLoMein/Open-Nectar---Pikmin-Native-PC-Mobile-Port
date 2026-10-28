#pragma once
#import <UIKit/UIKit.h>
#import <QuartzCore/QuartzCore.h>
// A shared, accessible blue-and-gold treatment for the experimental screens.
static inline UIColor* nectarCoopBackground(void) { return [UIColor colorWithRed:0.035 green:0.10 blue:0.26 alpha:1.0]; }
static inline void nectarCoopStyleButton(UIButton* button) {
    button.tintColor=[UIColor colorWithRed:1.0 green:0.84 blue:0.34 alpha:1.0];
    button.backgroundColor=[UIColor colorWithRed:0.12 green:0.25 blue:0.49 alpha:1.0];
    button.layer.cornerRadius=10.0;
    button.titleLabel.adjustsFontForContentSizeCategory=YES;
    button.titleLabel.adjustsFontSizeToFitWidth=YES;
    button.titleLabel.minimumScaleFactor=0.75;
}
static inline void nectarCoopStyleLabel(UILabel* label) {
    label.textColor=UIColor.whiteColor;
    label.adjustsFontForContentSizeCategory=YES;
}
