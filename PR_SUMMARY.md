# Pull Request: Fix HTML Template and Holden Nobody Character

## Overview
This PR fixes two critical issues identified after Week 2 generation:
1. HTML template in show generation script
2. Holden Nobody character description in UWA Complete Guide

## Changes Made

### 1. scripts/generate_shows.py
**Method Updated:** `build_combined_html()` (line ~477)

**What Changed:**
- Replaced simple HTML structure with full site template
- Added proper header with UWA logo and navigation
- Added brand-colored quick navigation buttons  
- Added brand-specific show headers with logos
- Added proper footer with logos
- Added current date display

**Result:** Generated show pages now match the Week 1 formatting with consistent navigation, branding, and styling.

### 2. UWA_COMPLETE_GUIDE.md
**Sections Updated:**
- Line ~600: Roster section
- Line ~800: "THE MERCENARY DESTROYER" storyline
- Line ~900: "HOLDEN NOBODY'S CHAMPIONSHIP REIGN" storyline

**What Changed:**
- Removed all references to Holden Nobody being a "SHOOT Project legend"
- Updated to correctly describe him as a "rookie rising star"
- Removed references to "20 years of experience" and "legendary career"
- Updated storyline narratives to reflect underdog rookie vs. veteran destroyer dynamic

**Result:** Holden Nobody is now correctly portrayed as a talented young rookie who shocked the world, not a seasoned legend.

## Why These Changes Matter

### HTML Template
Without this fix, future show generations will continue using the old simple template instead of matching the site's design. This creates inconsistency and a poor user experience.

### Holden Nobody Character
The "legend" characterization was factually wrong and made the storylines less compelling. The corrected "rookie underdog" story is:
- More dramatic (inexperienced champion vs. career-ending mercenary)
- More realistic (explains why Quincannon is such a threat)
- Better storytelling (David vs. Goliath dynamic)

## Testing Checklist
- [ ] Generate test show with `--test` flag
- [ ] Verify HTML output matches Week 1 format
- [ ] Check Holden Nobody descriptions in generated content
- [ ] Deploy to FTP and verify live site
- [ ] Generate Week 3 (or regenerate Week 2)

## Files Modified
- `scripts/generate_shows.py` - HTML template update
- `UWA_COMPLETE_GUIDE.md` - Character corrections (4 locations)
