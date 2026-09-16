# Accessibility Requirements

## Normative

- Every persona journey must declare a11y acceptance criteria.  
- AccessibilityCapability inventory must be exportable per device profile.  
- Screen reader / magnifier / high-contrast / captions / keyboard-only paths required for ordinary-user baseline.  
- **Lint ≠ accessibility PASS.** Human evaluation HUMAN_PENDING until earned.

## Current state (CX0)

Device OS: `accessibility_manager.SUPPORTED_FEATURES`, phase_xv AT-SPI-style tree, Cont IX a11y hardening — **PARTIAL**. Guest AT-SPI bus connect failures observed historically.

## Gaps (P0)

1. Journey-level a11y evidence harness  
2. Reliable AT-SPI / portal a11y bridge on guest  
3. AccessibilityCapability v1 contract adoption  
4. Human study protocol packet  
