# NEXT STEPS - UWA Automation System

**Date:** November 9, 2025 - EVENING SESSION
**System Status:** ⚠️ **REQUIRES UPDATES**

---

## 🎯 CURRENT SESSION PROGRESS

### Issues Identified from Week 2 Generation

1. ✅ **HTML Template Formatting** - Documented
2. ✅ **Holden Nobody Character Error** - Documented  
3. ⏸️ **Repetition Prevention** - NOT YET ADDRESSED (paused as requested)

---

## 📋 IMMEDIATE ACTION ITEMS

### 1. Fix HTML Template in Generation Script
**File:** `scripts/generate_shows.py`
**Method:** `build_combined_html()` (around line 477)
**Documentation:** `docs/TEMPLATE_UPDATE_NEEDED.md`

**Problem:** Week 2 shows used old simple template instead of the updated Week 1 format with:
- Proper header with logo and navigation
- Brand-colored section headers
- Quick jump navigation
- Show metadata display

**Solution:** Replace the `build_combined_html()` method with the version documented in `docs/TEMPLATE_UPDATE_NEEDED.md`

**How to Fix:**
1. Edit `scripts/generate_shows.py` on GitHub
2. Find the `build_combined_html` method
3. Replace with new version from documentation
4. Commit the change

---

### 2. Fix Holden Nobody Character Description
**File:** `UWA_COMPLETE_GUIDE.md`
**Documentation:** `docs/HOLDEN_NOBODY_FIX.md`

**Problem:** Holden Nobody is incorrectly described as a "SHOOT Project legend" with 20 years of experience. He is actually a **rookie rising star**, NOT a legend.

**Incorrect References:**
- Roster section: "SHOOT Project legend"
- Storyline "THE MERCENARY DESTROYER": "legendary career"
- Storyline "HOLDEN NOBODY'S CHAMPIONSHIP REIGN": "living legend from SHOOT Project"

**Solution:** Update all references to reflect that he's:
- A talented rookie
- A rising star
- An underdog champion
- Someone with potential but NOT decades of experience

**Narrative Impact:** This makes the story BETTER - young rookie shocking the world by beating a veteran (Volkov) and now facing a career-ending mercenary (Quincannon). It's a David vs. Goliath story, not legend vs. legend.

---

### 3. Address Repetition Prevention (NOT YET STARTED)
**Status:** Paused as requested

**Problem:** Segment titles and storyline beats are repeating across weeks:
- Week 1 REIGN: "The Mind Games Begin" (Ryan Odyssey opening segment)
- Week 2 REIGN: "The Mind Games Begin" (Ryan Odyssey opening segment)

**Goal:** Each week should feel like episodic television with:
- Unique segment titles
- Fresh story beats
- No repetitive patterns
- Progression and evolution

**This will be addressed in the next conversation.**

---

## 🔧 TECHNICAL FIXES NEEDED

### Files to Update:
1. **`scripts/generate_shows.py`**
   - Update `build_combined_html()` method
   - See: `docs/TEMPLATE_UPDATE_NEEDED.md`

2. **`UWA_COMPLETE_GUIDE.md`**
   - Fix all Holden Nobody references (4 locations)
   - See: `docs/HOLDEN_NOBODY_FIX.md`

3. **`scripts/generate_shows.py`** (for repetition prevention - future)
   - Update prompt to check for repetitive segment titles
   - Add tracking for segment names used in previous weeks
   - Implement variation requirements
   - *Will be addressed after current fixes are complete*

---

## 📝 VERIFICATION STEPS AFTER FIXES

### After Fixing HTML Template:
1. Regenerate Week 2 (or generate Week 3 in test mode)
2. Check that the show page has:
   - ✅ Proper header with UWA logo
   - ✅ Navigation to Home, About, Results, Archive
   - ✅ Quick jump buttons (brand-colored)
   - ✅ Brand headers with logos
   - ✅ Show metadata display
   - ✅ Proper content wrappers

### After Fixing Holden Nobody:
1. Regenerate any show with Resistance content
2. Verify that Holden Nobody is described as:
   - ✅ A rookie or rising star
   - ✅ NOT a legend
   - ✅ Underdog champion
   - ✅ Young talent facing a veteran destroyer

### After Repetition Prevention (Future):
1. Generate multiple weeks consecutively
2. Check segment titles are unique
3. Verify storyline beats evolve and don't repeat
4. Confirm each week feels fresh

---

## 🗂️ DOCUMENTATION CREATED

- **`docs/TEMPLATE_UPDATE_NEEDED.md`** - Complete HTML template fix
- **`docs/HOLDEN_NOBODY_FIX.md`** - Character correction details

These documents contain:
- Exact problem descriptions
- Line-by-line fixes needed
- Complete corrected text
- Rationale for changes

---

## 💡 NEXT CONVERSATION TOPICS

When you return, we should:

1. **Verify Fixes Were Applied**
   - Check if HTML template was updated
   - Check if Holden Nobody was corrected

2. **Test Generation**
   - Run a test generation to see if fixes work
   - Verify output matches Week 1 formatting

3. **Address Repetition Prevention**
   - Design system to track used segment titles
   - Add variation requirements to prompt
   - Implement freshness checks

4. **Deploy and Verify**
   - Deploy updated files to FTP
   - Check live site reflects changes
   - Generate Week 3 (or regenerate Week 2)

---

## 🎭 SYSTEM STATUS

**Working:**
- ✅ Weekly generation system
- ✅ Tracking files (championships, matches, storylines)
- ✅ FTP deployment
- ✅ Results and archive page generation

**Needs Fixes:**
- ⚠️ HTML template in generation script
- ⚠️ Holden Nobody character description
- ⚠️ Repetition prevention system (not yet designed)

**Ready for Production After Fixes:**
- HTML template update
- Character correction
- Repetition prevention implementation

---

## 🚀 DEPLOYMENT WORKFLOW

After fixes are applied:

1. **Manual Template Fix**: Edit `generate_shows.py` on GitHub
2. **Manual Character Fix**: Edit `UWA_COMPLETE_GUIDE.md` on GitHub
3. **Test Generation**: Run `python scripts/generate_shows.py --test`
4. **Verify Output**: Check test show matches Week 1 format
5. **Deploy**: Run "Deploy to FTP" workflow
6. **Live Check**: Verify https://shootproject.com/uwa4/ shows updates

---

*Last Updated: November 9, 2025 - Evening*
*Next Session: Apply documented fixes and address repetition prevention*