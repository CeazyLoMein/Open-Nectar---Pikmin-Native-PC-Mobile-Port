#pragma once
#include <algorithm>
#include <cmath>

#if defined(__APPLE__) && !defined(__IPHONEOS__)
#include <TargetConditionals.h>
#endif

// Fractions of the current SDL view, independent of Retina drawable scale.
struct PcMobileInsets { float left = 0, top = 0, right = 0, bottom = 0; };
#if defined(__IPHONEOS__) || (defined(__APPLE__) && TARGET_OS_IPHONE)
PcMobileInsets pc_mobile_safe_insets();
#else
inline PcMobileInsets pc_mobile_safe_insets() { return {}; }
#endif

struct PcMobileFrame { float x, y, w, h, unit; };
inline float pc_mobile_inset(float value) {
    return std::isfinite(value) ? std::max(0.0f, std::min(0.4f, value)) : 0.0f;
}
inline PcMobileFrame pc_mobile_frame(float w, float h, PcMobileInsets insets) {
    w = std::max(1.0f, w); h = std::max(1.0f, h);
    const float left = pc_mobile_inset(insets.left), right = pc_mobile_inset(insets.right);
    const float top = pc_mobile_inset(insets.top), bottom = pc_mobile_inset(insets.bottom);
    const float width = w * (1 - left - right), height = h * (1 - top - bottom);
    // Keep opposing thumb groups apart on less-wide landscape windows.
    return {w * left, h * top, width, height, std::min(height, width / 1.5f)};
}
inline float pc_mobile_clamp(float value, float start, float length, float radius) {
    radius = std::min(radius, length * 0.5f);
    return std::max(start + radius, std::min(start + length - radius, value));
}
inline void pc_mobile_button(const PcMobileFrame& f, float x, float y, bool right, float r,
                             float& px, float& py) {
    px = pc_mobile_clamp(right ? f.x + f.w - x * f.unit : f.x + x * f.unit, f.x, f.w, r);
    py = pc_mobile_clamp(f.y + y * f.unit, f.y, f.h, r);
}
inline void pc_mobile_save_position(const PcMobileFrame& f, float px, float py,
                                   bool& right, float& x, float& y) {
    right = px > f.x + f.w * 0.5f;
    x = (right ? f.x + f.w - px : px - f.x) / f.unit;
    y = (py - f.y) / f.unit;
}
