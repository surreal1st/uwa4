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
- **REIGN:** Red (#DC143C)
- **The Resistance:** Blue (#00BFFF)
- **PW:NEO:** Purple (#9333EA)

**Design Philosophy:**
Modern sports presentation (ESPN/Fox Sports style) converted to dark mode for comfortable viewing, with brand-specific color accents creating visual distinction while maintaining professional cohesion.

**Rationale:**
Clean, professional aesthetic appropriate for modern streaming audience while maintaining sports entertainment energy. Dark theme reduces eye strain for extended reading sessions.

---

## TECHNICAL DECISIONS

### Technology Stack

**Chosen Stack:** GitHub Actions + Claude API + Static HTML/CSS

**Date Chosen:** November 8, 2025

**Stack Components:**
- **Frontend:** Static HTML5 with external stylesheet
- **Automation:** GitHub Actions (scheduled workflows)
- **Content Generation:** Claude Sonnet 4.5 via Anthropic API
- **Data Storage:** JSON files in repository
- **Deployment:** FTP to web server
- **Version Control:** Git via GitHub

**Technical Choices:**

1. **Static Site Architecture**
   - No server-side processing required
   - Fast page loads
   - Easy to deploy and maintain
   - Works with any web hosting
   - **Rationale:** Simplicity, performance, and universal compatibility

2. **External Stylesheet Strategy**
   - Single external stylesheet (`/assets/css/style.css`)
   - All pages reference the same stylesheet
   - Consistent styling across all pages
   - Easier maintenance and updates
   - **Rationale:** DRY principle, maintainability

3. **JSON for Tracking Data**
   - All tracking files use JSON format
   - Easily parseable by automation scripts
   - Human-readable for debugging
   - Lightweight and efficient
   - **Rationale:** Best balance of simplicity and functionality

4. **GitHub Actions for Automation**
   - Scheduled workflows run Friday 2am EST (7am UTC)
   - Secrets management for credentials
   - Built-in version control
   - Free for public repositories
   - Manual trigger capability for testing
   - **Rationale:** Integrated with existing GitHub infrastructure

5. **FTP Deployment Configuration**
   - Direct FTP upload to web server
   - Configurable remote directory via `FTP_REMOTE_DIR` secret
   - Automatic directory structure creation
   - Compatible with most hosting providers
   - Simple and reliable
   - **Rationale:** Universal compatibility and simplicity
   - **Date Configured:** November 9, 2025

6. **GitHub Actions Permissions**
   - `permissions: contents: write` for repository commits
   - Allows workflow to push generated content back to repo
   - Uses `GITHUB_TOKEN` for authentication
   - **Rationale:** Enables automated content commits
   - **Date Configured:** November 9, 2025

**Future Considerations:**
- Could migrate to Netlify/Vercel for automatic deployments
- Could add RSS feed for show updates
- Could implement JavaScript for interactive elements
- System designed to be flexible for future enhancements

---

## TECHNICAL ARCHITECTURE

### Automation System
- **Platform:** GitHub Actions + Claude API integration
- **Schedule:** Fridays at 2:00 AM EST (7:00 AM UTC)
- **Process:** Generate all three weekly shows, update tracking files, build website, deploy via FTP
- **Manual Trigger:** Available via GitHub Actions UI for testing

### Repository Structure
```
/uwa4
├── /assets
│   └── /css
│       └── style.css (main stylesheet)
├── /shows
│   ├── /week-001
│   │   └── index.html
│   ├── /week-002
│   │   └── index.html
│   └── ... (generated weekly)
├── /tracking
│   ├── match-history.json
│   ├── storyline-progression.json
│   ├── championships.json
│   └── injuries-absences.json
├── /scripts
│   ├── generate_shows.py (to be created)
│   └── deploy_ftp.py
├── /design-mockups (reference designs)
├── index.html
├── about.html
├── results.html (updated weekly)
├── archive.html (updated weekly)
├── UWA_COMPLETE_GUIDE.md (storyline reference)
├── PROJECT_SPECIFICATION.md (this file)
├── SECRETS_SETUP.md (secrets configuration guide)
├── README.md (repository overview)
├── final-design.html (approved design reference)
└── .github/workflows/generate-shows.yml
```

### Deployment
- **Method:** FTP to configured remote directory
- **Credentials:** Stored in GitHub Secrets (6 secrets configured)
- **Files Deployed:** All HTML pages, CSS assets, weekly show directories
- **Status:** Tested and operational

### GitHub Secrets Configuration
1. `ANTHROPIC_API_KEY` - Claude API authentication
2. `FTP_HOST` - FTP server hostname
3. `FTP_USERNAME` - FTP account username
4. `FTP_PASSWORD` - FTP account password
5. `FTP_PORT` - FTP server port (optional, defaults to 21)
6. `FTP_REMOTE_DIR` - Target directory on server

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

### Pages Implemented

1. **Index Page (index.html)** ✅
   - Welcome/hero section
   - Latest show highlights
   - Quick links to results and archive
   - Brand logos with descriptions
   - **Status:** Complete and deployed

2. **About Page (about.html)** ✅
   - Explanation of the UWA
   - History of Reality Check Entertainment
   - How the three brands came together
   - Brand philosophies and show schedules
   - **Status:** Complete and deployed

3. **Results Page (results.html)** ✅
   - Current champions section
   - Placeholder for weekly show content
   - Will be updated weekly by automation
   - **Status:** Template complete, awaiting show generation

4. **Archive Page (archive.html)** ✅
   - Links to all past weeks
   - Will be updated weekly by automation
   - **Status:** Template complete, awaiting show generation

5. **Individual Week Pages (/shows/week-XXX/index.html)**
   - To be generated by automation
   - Contains that week's three shows
   - Business metrics included
   - **Status:** Awaiting show generation system

### Design Implementation

**Visual Style:** ✅ Complete
- Dark theme throughout (#0f0f0f background)
- External stylesheet (assets/css/style.css)
- Responsive mobile-friendly design
- Modern sports network aesthetic

**Brand Colors:** ✅ Implemented
- REIGN: Red (#DC143C)
- The Resistance: Blue (#00BFFF)
- PW:NEO: Purple (#9333EA)

**Logos:** ✅ Referenced via URL
- All brand logos loading from sp2025.shootproject.com

---

## CONTENT TRACKING SYSTEMS

### Tracking Files Initialized

1. **championships.json** ✅
   - All 15 current champions initialized
   - Tracking structure in place
   - Ready for weekly updates

2. **match-history.json** ✅
   - Empty array ready for match records
   - Structure defined

3. **storyline-progression.json** ✅
   - All active storylines from UWA_COMPLETE_GUIDE loaded
   - Priority levels set
   - Next beats defined

4. **injuries-absences.json** ✅
   - SHOOT Project wrestlers protected list created
   - Empty arrays for injuries/absences

**Status:** All tracking systems initialized and ready for automation

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

### Current Champions (Week 0):
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
See UWA_COMPLETE_GUIDE.md and tracking/storyline-progression.json for complete details.

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
- ✅ Automated generation workflow created
- ✅ Website structure deployed successfully
- ✅ All pages load correctly with styling
- ⏳ Archive system ready for weekly updates
- ✅ Tracking files initialized and structured

### Content Success:
- ⏳ Each show is 7-10 minutes reading time
- ⏳ Storylines progress logically
- ⏳ No repetitive matchups
- ⏳ Character development occurs naturally
- ⏳ Match variety across brands
- ⏳ Compelling promos and segments
- ⏳ Business metrics fluctuate realistically

### Creative Success:
- ⏳ Unpredictable but logical booking
- ⏳ Long-term storytelling visible
- ⏳ Characters feel distinct and alive
- ⏳ Each brand maintains unique identity
- ⏳ Fans would want to come back next week

---

## IMPLEMENTATION PROGRESS

### Completed Phases:

1. ✅ **Design Phase** (November 8, 2025)
   - Three mockup options created
   - Option 2 (Modern Sports Clean - Dark Theme) selected
   - Design documented in PROJECT_SPECIFICATION.md

2. ✅ **Structure Phase** (November 8-9, 2025)
   - Complete repository structure created
   - All directories and files in place
   - Assets folder with CSS stylesheet

3. ✅ **Template Phase** (November 8-9, 2025)
   - index.html - Complete
   - about.html - Complete
   - results.html - Template ready
   - archive.html - Template ready
   - External stylesheet implemented

4. ✅ **Tracking Phase** (November 9, 2025)
   - championships.json initialized
   - match-history.json initialized
   - storyline-progression.json initialized with all active storylines
   - injuries-absences.json initialized with SHOOT Project protections

5. ✅ **Automation Phase** (November 9, 2025)
   - GitHub Actions workflow created
   - Scheduled for Fridays 2am EST
   - Manual trigger capability added
   - Workflow permissions configured

6. ✅ **Deployment Phase** (November 9, 2025)
   - FTP deployment script created (scripts/deploy_ftp.py)
   - All 6 GitHub Secrets configured
   - FTP deployment tested successfully
   - Website live with core pages and styling

### In Progress:

7. ⏳ **Generator Phase** (Next)
   - Show generation system (scripts/generate_shows.py)
   - Claude API integration
   - Tracking file updates
   - HTML page generation

### Upcoming:

8. ⏳ **Testing Phase**
   - Generate sample Week 1 shows
   - Verify all tracking updates
   - Test complete workflow end-to-end

9. ⏳ **Launch Phase**
   - First automated Friday generation
   - Monitor for issues
   - Verify website updates correctly

---

## CURRENT STATUS SUMMARY

**Last Updated:** November 9, 2025

**Infrastructure Status:** ✅ COMPLETE
- Website structure: Deployed and operational
- CSS styling: Implemented and working
- FTP deployment: Tested and functional
- GitHub Actions: Configured and ready
- Tracking systems: Initialized with starting data

**Remaining Work:** 
- **Show Generation System** - Primary remaining task
  - Python script to generate weekly shows
  - Claude API integration
  - Tracking file update logic
  - HTML page building
  
**Estimated Completion:** Show generation system is the most complex remaining component. Once built, the entire automation system will be operational.

**Testing Notes:**
- FTP deployment successfully uploads all files to configured directory
- Website loads correctly with dark theme styling
- GitHub Actions workflow triggers successfully
- All secrets properly configured

---

## IMPORTANT NOTES

### Domain & Credentials:
- ✅ FTP credentials configured in GitHub Secrets
- ✅ Remote directory path configured
- ✅ Deployment tested successfully
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

*This specification represents the complete technical and creative requirements for the UWA4 automated wrestling content generation system.*

*Last Updated: November 9, 2025 - Updated implementation progress, added deployment status, documented technical decisions for FTP and GitHub Actions configuration*