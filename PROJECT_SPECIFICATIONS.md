# UWA Generation System - Project Specifications

## Project Overview
Automated weekly wrestling show generation system for the United Wrestling Accord (UWA), featuring three brands (REIGN, Resistance, PW:NEO) with AI-powered storyline continuity and automatic tracking.

---

## Current Status: PHASE 1 COMPLETE ✅

### What's Working:
1. ✅ Repository structure with tracking system
2. ✅ Claude API integration for show generation
3. ✅ Automatic match parsing and tracking updates
4. ✅ Championship defense tracking
5. ✅ Storyline progression automation
6. ✅ Test mode for safe development

### What's Next:
- Results page generation (results.html)
- Archive system for past shows
- FTP deployment automation

---

## System Architecture

### 1. Repository Structure
```
uwa4/
├── tracking/               # Production tracking files
│   ├── championships.json
│   ├── match-history.json
│   ├── injuries-absences.json
│   └── storyline-progression.json
├── tracking/test/          # Test mode tracking files
│   └── (same structure)
├── shows/                  # Production HTML shows
├── test-shows/             # Test mode HTML shows
├── scripts/
│   └── generate_shows.py   # Main generation script
├── assets/
│   └── css/
│       └── style.css       # Website styling
└── UWA_COMPLETE_GUIDE.md   # Roster and character details
```

### 2. Tracking System (JSON Files)

**championships.json**
- Current champions for all brands
- Championship defense counts
- Reign start dates
- Week number tracking

**match-history.json**
- Complete match results archive
- Winner, method, duration
- Championship match flags
- Storyline linkage

**storyline-progression.json**
- Active storylines per brand
- Current "nextBeat" for each storyline
- Priority levels
- Participant tracking

**injuries-absences.json**
- Wrestler availability
- Injury/absence reasons
- Return dates

---

## Generation Workflow

### How It Works:

1. **Load Tracking Data**
   - Reads all JSON tracking files
   - Loads UWA_COMPLETE_GUIDE.md for roster info
   - Validates current state

2. **Build Comprehensive Prompt**
   - Current champions
   - Active storylines with "nextBeat"
   - Complete roster/character details
   - Week number

3. **Claude API Generation**
   - Model: `claude-sonnet-4-20250514`
   - Generates all 3 brands in one call
   - Returns JSON match data + HTML content

4. **Parse Response**
   - Extracts match data JSON
   - Extracts HTML for each brand
   - Validates data integrity

5. **Update Tracking Files**
   - Adds matches to match-history.json
   - Increments championship defenses
   - Updates storyline "nextBeat" values
   - Increments week number

6. **Save Output**
   - Combined HTML file with all 3 brands
   - Raw response for debugging
   - Updated tracking files

### Command Usage:

**Test Mode (Safe):**
```bash
python scripts/generate_shows.py --test
```
- Uses `/tracking/test/` files
- Saves to `/test-shows/`
- Week format: TEST-001, TEST-002, etc.

**Production Mode:**
```bash
python scripts/generate_shows.py
```
- Uses `/tracking/` files
- Saves to `/shows/`
- Week format: 1, 2, 3, etc.

---

## Claude API Integration Details

### Generation Format:

Claude returns TWO parts:

**Part 1: JSON Match Data**
```json
{
  "reign": [
    {
      "participants": ["Wrestler A", "Wrestler B"],
      "winner": "Wrestler A",
      "method": "pinfall/submission/countout/dq",
      "duration": "12:45",
      "championship": "Title Name" or null,
      "championship_change": false,
      "storyline_id": "reign-001",
      "storyline_advancement": "How storyline progressed"
    }
  ],
  "resistance": [...],
  "neo": [...],
  "storyline_updates": [
    {
      "storyline_id": "reign-001",
      "new_next_beat": "Updated beat based on events"
    }
  ]
}
```

**Part 2: HTML Show Content**
- Complete narrative for each brand
- Match descriptions with full promo dialogue
- 3-4 segments per show
- Show metrics (attendance, gate, rating)

### Show Requirements:
- 4-6 matches per brand
- 3-4 segments (promos, backstage, confrontations)
- Each match advances a storyline
- Full dialogue in quotation marks
- 7-10 minute read length
- Realistic show metrics

---

## Automatic Tracking Updates

### Championships:
- Defense count increments automatically
- Championship changes flagged for review
- Week number updates

### Storylines:
- "nextBeat" updated based on week's events
- Claude determines logical progression
- Maintains continuity across weeks

### Match History:
- All matches logged with details
- Linkage to storylines maintained
- Complete archive for reference

---

## Test Results (Week TEST-002)

### Tracking Updates Verified:

**Championships Updated:**
- Horizon Championship: Cameron Grayson (1 defense)
- REIGN Women's: Ivy Knight (1 defense)
- REIGN Tag Team: Los Asesinos (1 defense)
- Resistance Television: Mike McCoy (1 defense)
- Resistance Women's: Mia Taylor (1 defense)
- Resistance Tag Team: Southern Rebels (1 defense)
- NEO World: Judge James Morgan (1 defense)
- NEO Internet: Adam Winters (1 defense)

**Storylines Progressed:**
- "The Mind Is The New Weapon" → "Anderson confronts Odyssey directly, demands title match"
- "Horizon Championship Rematch" → "WOLF MAN demands rematch with even more extreme stipulation"
- "The Mercenary Destroyer" → "Nobody vs Quincannon championship match announced"
- All 9 active storylines updated with logical next beats

**Week Counter:** Updated from 0 → 2

---

## Known Limitations

1. **Championship Changes:**
   - Currently flagged but not auto-applied
   - Requires manual verification

2. **API Key:**
   - Must be set as environment variable
   - `ANTHROPIC_API_KEY=your_key_here`

3. **Results Page:**
   - Not yet implemented
   - Shows saved as individual HTML files

4. **FTP Deployment:**
   - Not yet integrated
   - Manual deployment required

---

## Next Development Phase

### Priority 1: Results Page
- Generate `results.html` with latest shows
- Quick-access navigation
- Show metrics display

### Priority 2: Archive System
- Automatic archive page creation
- Week-by-week navigation
- Championship history tracking

### Priority 3: FTP Deployment
- Automated upload to live site
- Post-generation deployment
- Error handling and rollback

---

## Environment Requirements

**Python Packages:**
```bash
pip install anthropic
```

**Environment Variables:**
```bash
export ANTHROPIC_API_KEY="your_api_key_here"
```

**Python Version:**
- Python 3.8+

---

## File Locations

**Production:**
- Tracking: `/tracking/*.json`
- Shows: `/shows/*.html`
- Guide: `/UWA_COMPLETE_GUIDE.md`

**Test:**
- Tracking: `/tracking/test/*.json`
- Shows: `/test-shows/*.html`

---

## Success Metrics

### Current Achievements:
✅ Fully automated show generation  
✅ Storyline continuity maintained  
✅ Championship tracking accurate  
✅ Match history comprehensive  
✅ Zero manual data entry required  
✅ Test mode prevents production issues  

### Future Goals:
⏳ One-command deployment  
⏳ Historical archive browsing  
⏳ Automatic results page updates  
⏳ FTP upload automation  

---

## Developer Notes

### To Continue Development:

1. **For Results Page:**
   - Create template for results.html
   - Parse latest show files
   - Generate navigation
   - Add show metrics

2. **For Archive System:**
   - Create archive template
   - Generate weekly archive pages
   - Build navigation system
   - Link from results page

3. **For FTP Deployment:**
   - Add FTP credentials to config
   - Implement upload function
   - Add error handling
   - Create deployment log

### Testing Protocol:
1. Always use `--test` flag first
2. Verify tracking file updates
3. Check HTML output quality
4. Review storyline progression
5. Only then run production mode

---

## Version History

**v0.4 - Current (Nov 9, 2025)**
- ✅ Automatic tracking updates
- ✅ Storyline progression automation
- ✅ Championship defense tracking
- ✅ Complete end-to-end workflow

**v0.3 - Nov 9, 2025**
- ✅ Claude API integration
- ✅ JSON + HTML dual output
- ✅ Match data parsing

**v0.2 - Nov 8, 2025**
- ✅ Tracking system established
- ✅ Test mode implementation

**v0.1 - Nov 8, 2025**
- ✅ Repository structure
- ✅ Initial tracking files

---

## Contact & Support

For questions about this system, refer to:
- `/UWA_COMPLETE_GUIDE.md` for roster/storyline details
- `/tracking/*.json` for current state
- This specification document for system architecture

**Repository:** https://github.com/surreal1st/uwa4

---

*Last Updated: November 9, 2025*  
*Status: Phase 1 Complete - Show Generation & Tracking Functional*
