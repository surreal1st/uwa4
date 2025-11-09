# UWA4 Project Specification
## Automated Wrestling Promotion Content Generator

---

## PROJECT OVERVIEW

This project is an automated content generation system for the **United Wrestling Accord (UWA)**, a fictional professional wrestling organization consisting of three distinct brands. The system generates weekly wrestling shows with compelling storylines, match results, and character development - all running autonomously with minimal human intervention.

**Core Objective:** Create a sustainable, self-running wrestling promotion that generates 7-10 minutes of reading content per show (3 shows weekly), maintains continuity, develops storylines, and produces a clean web interface for fans to follow along.

---

## THE BRANDS

The UWA operates three independent wrestling brands under the Reality Check Entertainment network:

### REIGN
- **Show:** REIGN: Ascension
- **Airs:** Fridays (in-universe)
- **Location:** Los Angeles, CA
- **Philosophy:** Prestige, legacy, championship glory
- **Style:** Sports entertainment meets athleticism
- **Tone:** Larger-than-life, cinematic, epic
- **Brand Color:** Red

### The Resistance
- **Show:** Resistance: Uprising  
- **Airs:** Mondays (in-universe)
- **Location:** American Northeast
- **Philosophy:** Heart, honor, raw physicality
- **Style:** Pure, old-school professional wrestling
- **Tone:** Raw, authentic, blue-collar
- **Brand Color:** Blue

### PW:NEO
- **Show:** PW:NEO: Paradigm Shift
- **Airs:** Wednesdays (in-universe)
- **Location:** Chicago, IL
- **Philosophy:** Layered faction warfare, political intrigue
- **Style:** Cerebral battleground, narrative-driven
- **Tone:** Intellectual, layered, philosophical
- **Brand Color:** Purple

**Reality Check Entertainment:** The streaming network that owns all three brands (also owns SHOOT Project)

---

## DESIGN DECISIONS

### Website Design Choice
**Selected Design:** Option 2 - Modern Sports Clean (Dark Theme Variant)

**Date Chosen:** November 8, 2025

**Design Characteristics:**
- Contemporary sports network aesthetic adapted to dark theme
- Card-based layouts with subtle shadows
- Clean, organized information hierarchy
- Modern sans-serif typography
- Smooth hover animations
- Professional, easy-on-the-eyes dark backgrounds

**Brand Color Scheme:**
- **REIGN:** Red (primary brand color throughout design)
- **The Resistance:** Blue (sky blue / cyan tones)
- **PW:NEO:** Purple (primary brand color throughout design)

**Design Philosophy:**
Modern sports presentation (ESPN/Fox Sports style) converted to dark mode for comfortable viewing, with brand-specific color accents creating visual distinction while maintaining professional cohesion.

**Rationale:**
Clean, professional aesthetic appropriate for modern streaming audience while maintaining sports entertainment energy. Dark theme reduces eye strain for extended reading sessions.

---

## TECHNICAL ARCHITECTURE

### Automation System
- **Platform:** GitHub Actions + Claude API integration
- **Schedule:** Fridays at 2:00 AM EST
- **Process:** Generate all three weekly shows, update tracking files, build website, deploy via FTP

### Repository Structure (Recommended)
```
/uwa4
├── /assets
│   ├── /images (brand logos)
│   └── /css (stylesheets)
├── /shows
│   ├── /week-001
│   ├── /week-002
│   └── ... (generated weekly)
├── /tracking
│   ├── match-history.json
│   ├── storyline-progression.json
│   ├── championships.json
│   └── injuries-absences.json
├── /templates (HTML templates for generation)
├── index.html
├── about.html
├── results.html (updated weekly)
├── archive.html
├── UWA_COMPLETE_GUIDE.md (storyline reference)
├── PROJECT_SPECIFICATION.md (this file)
└── .github/workflows/generate-shows.yml
```

### Deployment
- **Method:** FTP to domain
- **Credentials:** Stored in GitHub Secrets
- **Files Deployed:** All HTML pages, assets, archived shows

---

## CONTENT GENERATION SPECIFICATIONS

### Weekly Show Format

**Each Brand Produces:**
- 4-6 matches per show
- 1-2 segments between each match
- Opening segment (varies - sometimes cold open, sometimes promo)
- Closing segment (varies - sometimes cliffhanger, sometimes celebration)
- Total reading time: 7-10 minutes per show

**Segment Types:**
- Backstage promos (with full dialogue)
- In-ring promos (with full dialogue)
- Backstage attacks
- Interview segments
- Confrontations
- Video packages (rare)

**Match Format:**
- Written in narrative/prose style
- Key moments highlighted
- Psychology and story progression emphasized
- Near-falls and false finishes for drama
- Clean finishes unless story dictates otherwise

### Special Events

**PPV Events (Brand-Specific):**
- Frequency: Every 4-5 weeks
- Each brand runs their own PPV
- Names vary (mix of themed names and "WrestleMania-style" event names)
- Recommendation: 1-2 mega-PPVs per brand annually

**UWA Super Shows (Cross-Brand):**
- Frequency: Every 6-8 weeks
- All three brands participate
- Championship unification matches possible
- Major storyline intersections

### Business Metrics (Per Show)

**Attendance:**
- REIGN (Los Angeles): 8,000-12,000
- The Resistance (Northeast venues): 3,000-6,000
- PW:NEO (Chicago): 5,000-9,000
- Fluctuates based on card quality and storyline heat

**Gate Revenue:**
- Calculated based on attendance and ticket pricing
- Varies by market and show importance

**Network Rating:**
- Nielsen-style scale (0.0-3.0)
- Fluctuates based on overall show quality and buzz

---

## WEBSITE STRUCTURE

### Pages Required

1. **Index Page (index.html)**
   - Welcome/hero section
   - Latest show highlights
   - Quick links to results and archive
   - Brand logos with descriptions

2. **About Page (about.html)**
   - Explanation of the UWA
   - History of Reality Check Entertainment
   - How the three brands came together
   - Brand philosophies and show schedules

3. **Results Page (results.html)**
   - Updated weekly with all three shows
   - One long page showing all shows in order (Monday, Wednesday, Friday)
   - Current champions section at top
   - Business metrics for each show
   - Note that shows take place M/W/F but page updates Friday

4. **Archive Page (archive.html)**
   - Single page with links to each week
   - Format: "Week 1", "Week 2", etc. (newsletter-style)
   - Links go to individual week pages

5. **Individual Week Pages (/shows/week-XXX/index.html)**
   - Contains that week's three shows
   - Preserved exactly as generated
   - Business metrics included

### Design Requirements

**Visual Style:**
- Dark theme throughout for eye comfort
- Clean and minimal
- Professional presentation
- Modern sports network aesthetic

**Brand Colors:**
- REIGN: Red
- The Resistance: Blue (sky blue / cyan)
- PW:NEO: Purple
- Colors carry through website elements
- Consistent with brand identity

**Logos Provided:**
- PW:NEO: https://sp2025.shootproject.com/uploads/NEO-transparent.png
- REIGN: https://sp2025.shootproject.com/uploads/REIGN-transparent.png
- The Resistance: https://sp2025.shootproject.com/uploads/TheResistance-transparent.png
- UWA: https://sp2025.shootproject.com/uploads/UWA-transparent.png
- Reality Check Wrestling: https://sp2025.shootproject.com/uploads/RCE-transparent.png

---

## CONTENT TRACKING SYSTEMS

### Match History
**Format:** JSON tracking every match
```json
{
  "week": 1,
  "brand": "REIGN",
  "match": "Avalanche Anderson vs Ryan Odyssey",
  "winner": "Ryan Odyssey",
  "finish": "Submission",
  "notes": "Non-title match"
}
```

### Storyline Progression
**Format:** Detailed logs updated after each show generation
- Current storylines for each brand
- Priority levels
- Key developments each week
- Next planned beats
- Long-term direction

### Championships
**Format:** Current champions with defense history
```json
{
  "title": "REIGN World Championship",
  "champion": "Avalanche Anderson",
  "reign_start": "Week 0",
  "defenses": 0,
  "next_challenger": "TBD"
}
```

### Injuries & Absences
**Format:** Currently injured/absent wrestlers
```json
{
  "wrestler": "Example Name",
  "brand": "REIGN",
  "status": "injured",
  "return_week": 8,
  "storyline_reason": "Attacked by faction"
}
```

**CRITICAL RULE:** Wrestlers designated as being from SHOOT Project can NEVER be injured in angles. Anyone else is fair game.

---

## CREATIVE CONTROL PARAMETERS

### Full Autonomy On:
- Match booking and results
- Storyline progression and creation
- Championship title changes
- Heel/face turns
- Faction formations and breakups
- Injury angles (except SHOOT Project wrestlers)
- Promo content and dialogue
- Segment structures

### Brand-Specific Rules:
- Win/loss records importance varies by brand (Claude decides)
- Title shot determination (Claude decides criteria per brand)
- Championship defense frequency (Claude decides)

### Continuity Requirements:
- Continue existing storylines from UWA_COMPLETE_GUIDE.md
- Starting point: Week 1 (fresh numbering)
- Preserve established championships and champions
- Maintain faction alignments unless story dictates changes
- Track all matches to prevent repetition
- Build on previously established character moments

### Cross-Brand Interaction:
- Wrestlers can invade other brands during weekly shows
- Existing invasions already happening (see Complete Guide)
- UWA super shows are primary cross-brand interaction points
- Respect brand philosophies when booking cross-brand content

---

## ROSTER MANAGEMENT

### Current Roster: 112 wrestlers across three brands

**REIGN:** 26 singles competitors + 11 tag teams
**The Resistance:** 29 singles competitors + 7 tag teams  
**PW:NEO:** 25 singles competitors + 7 tag teams

### Tag Team Usage:
- Singles wrestlers can team up for tag matches
- Doesn't affect singles division status
- Tag divisions exist but not strictly separated

### Character Development:
- New/developing talent should receive gradual pushes
- Established stars maintain credibility
- Rookies (Accord Initiative) build naturally
- Faction members have interconnected stories

---

## CONTENT QUALITY STANDARDS

### Writing Style:
- Narrative/prose for matches and segments
- Full dialogue for all promos
- Natural wrestling terminology
- Varied sentence structure
- Engaging and dramatic
- Approximately 7-10 minutes reading time per show

### Match Quality:
- Detail levels relatively consistent across matches
- Extra detail for:
  - Feud blow-offs
  - Championship matches
  - Special stipulation matches
  - Main events of major shows

### Segment Quality:
- Promos advance storylines or create new ones
- Backstage segments provide character depth
- Attacks/confrontations have purpose
- Interviews reveal motivations
- Every segment matters to the overall narrative

### Show Flow:
- Opening varies (cold open, promo, match)
- Segments between matches maintain pacing
- Closing varies (cliffhanger, celebration, attack)
- Mix of serious and lighter moments
- Each show should feel complete but leave threads

---

## WEEKLY GENERATION PROCESS

### Step 1: Review Current State
- Check storyline progression logs
- Review match history for variety
- Check championship status
- Review injury/absence list
- Identify stories needing advancement

### Step 2: Plan Each Show
- Determine matches for each brand
- Plan segments that advance stories
- Create new story beats where needed
- Ensure no repetitive matchups
- Balance card with mix of stories

### Step 3: Generate Content
- Write all three shows in narrative style
- Full dialogue for promos
- Business metrics for each show
- Update tracking files
- Generate championship standings

### Step 4: Build Website Pages
- Update results.html with new week
- Create archive page for new week
- Update index.html with latest highlights
- Ensure all links work correctly

### Step 5: Deploy
- FTP upload all files
- Verify deployment successful
- Website live with new content

---

## API CONSIDERATIONS

### Token Budget:
- Three detailed shows per week (~7-10 min read each)
- Tracking file updates
- HTML generation
- Estimated: Significant weekly token usage
- User is aware and approves budget

### Optimization:
- Keep tracking files efficient (JSON)
- Reuse HTML templates where possible
- Generate only what's needed per week
- Smart caching of reference data

---

## STARTING POINT DATA

### Current Champions (as of Complete Guide):
- **UWA World Championship:** Avalanche Anderson (REIGN)
- **REIGN World Championship:** Avalanche Anderson
- **REIGN Horizon Championship:** Cameron Grayson
- **REIGN Women's Championship:** Ivy Knight
- **REIGN DeathKore Championship:** Chris Carnage
- **REIGN Tag Team Championship:** Los Asesinos
- **Resistance World Championship:** Holden Nobody
- **Resistance Television Championship:** Mike McCoy
- **Resistance Cruiserweight Championship:** Pyro
- **Resistance Women's Championship:** Mia Taylor
- **Resistance Tag Team Championship:** The Southern Rebels
- **NEO World Championship:** Judge James Morgan
- **NEO Internet Championship:** Adam Winters
- **NEO Women's Championship:** Monica Cruz
- **NEO Tag Team Championship:** The Consortium

### Active Storylines (Priority Order):
See UWA_COMPLETE_GUIDE.md for detailed storyline breakdowns across all three brands.

**REIGN Top Stories:**
1. Avalanche Anderson vs Ryan Odyssey (psychological warfare)
2. Cameron Grayson vs WOLF MAN (Horizon Championship)
3. Ivy Knight vs Thorne Alliance (Women's Championship)

**Resistance Top Stories:**
1. Archer Quincannon vs Holden Nobody (World Championship)
2. XXCW Hostile Takeover
3. Mia Taylor vs XXCW (Women's Championship)

**PW:NEO Top Stories:**
1. Preston Alexander's mysterious agenda
2. Judge Morgan's tyrannical reign
3. Consortium vs Red Letter Society

---

## SUCCESS CRITERIA

### Technical Success:
- ✅ Automated generation runs every Friday 2am EST
- ✅ Website deploys successfully via FTP
- ✅ All pages load correctly
- ✅ Archive links work properly
- ✅ Tracking files update accurately

### Content Success:
- ✅ Each show is 7-10 minutes reading time
- ✅ Storylines progress logically
- ✅ No repetitive matchups
- ✅ Character development occurs naturally
- ✅ Match variety across brands
- ✅ Compelling promos and segments
- ✅ Business metrics fluctuate realistically

### Creative Success:
- ✅ Unpredictable but logical booking
- ✅ Long-term storytelling visible
- ✅ Characters feel distinct and alive
- ✅ Each brand maintains unique identity
- ✅ Fans would want to come back next week

---

## NEXT STEPS FOR IMPLEMENTATION

1. ✅ **Design Phase:** Create three HTML/CSS mockup options for website design
2. ✅ **Design Selection:** Option 2 (Modern Sports Clean - Dark Theme) chosen
3. **Structure Phase:** Build repository file structure with all necessary folders
4. **Template Phase:** Create HTML templates for all page types
5. **Generator Phase:** Build show generation system with Claude API integration
6. **Tracking Phase:** Implement JSON tracking systems
7. **Automation Phase:** Create GitHub Actions workflow
8. **Testing Phase:** Generate sample Week 1 shows to verify format
9. **Deployment Phase:** Configure FTP deployment with GitHub Secrets
10. **Launch Phase:** Run first automated generation

---

## IMPORTANT NOTES

### Domain & Credentials:
- FTP credentials stored in GitHub Secrets
- Domain information to be provided by user
- Never hardcode sensitive information

### Maintenance:
- System designed to run autonomously
- User can intervene for directorial input if desired
- User does not need to intervene otherwise
- System handles all creative decisions

### Expandability:
- System designed to potentially add more brands in future
- Architecture supports scaling to additional shows
- Tracking systems can accommodate new brands

---

*This specification represents the complete technical and creative requirements for the UWA4 automated wrestling content generation system as understood on November 8, 2025.*

*Last Updated: November 8, 2025 - Added Design Decisions section*