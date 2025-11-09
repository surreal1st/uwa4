# United Wrestling Accord - Automated Content Generator

An automated professional wrestling promotion featuring three distinct brands with AI-generated weekly shows, storylines, and championships.

## 🎭 The Brands

- **REIGN** (Fridays) - Los Angeles - Prestige & Legacy - Red
- **The Resistance** (Mondays) - Northeast - Heart & Honor - Blue
- **PW:NEO** (Wednesdays) - Chicago - Political Intrigue - Purple

## 📁 Repository Structure

```
/uwa4
├── /assets
│   └── /css
│       └── style.css          # Main stylesheet
├── /shows                     # Generated weekly shows (created by automation)
│   ├── /week-001
│   └── /week-XXX
├── /tracking                  # JSON data files
│   ├── championships.json     # Current champions
│   ├── match-history.json     # Complete match records
│   ├── injuries-absences.json # Injury tracking
│   └── storyline-progression.json # Active storylines
├── /scripts                   # Automation scripts
│   ├── generate_shows.py      # Show generation (to be built)
│   └── deploy_ftp.py          # FTP deployment
├── /design-mockups            # Design options (reference)
├── index.html                 # Home page
├── about.html                 # About the UWA
├── results.html               # Latest weekly results (updated weekly)
├── archive.html               # Archive of all weeks (updated weekly)
├── UWA_COMPLETE_GUIDE.md      # Complete storyline reference
├── PROJECT_SPECIFICATION.md   # Full technical & creative specs
├── SECRETS_SETUP.md           # GitHub Secrets configuration guide
├── final-design.html          # Approved design reference
└── .github/workflows          # GitHub Actions automation
    └── generate-shows.yml
```

## 🎨 Design

**Selected Design:** Modern Sports Clean (Dark Theme)
- Dark backgrounds for comfortable viewing (#0f0f0f, #1a1a1a)
- Brand colors: REIGN (Red #DC143C), The Resistance (Blue #00BFFF), PW:NEO (Purple #9333EA)
- Responsive, mobile-friendly layout
- Clean, professional aesthetic

## 📊 Tracking System

The automation system maintains four JSON files:

1. **championships.json** - Current title holders and reign statistics
2. **match-history.json** - Complete record of every match
3. **injuries-absences.json** - Wrestler status and protected talent (SHOOT Project)
4. **storyline-progression.json** - Active storylines across all brands

## 🤖 Automation

- **Schedule:** Fridays at 2:00 AM EST (7:00 AM UTC)
- **Platform:** GitHub Actions + Claude API
- **Process:** Generate 3 shows → Update tracking → Build HTML → Deploy via FTP
- **Content:** 7-10 minute read per show, 3 shows per week
- **Manual Trigger:** Available via GitHub Actions for testing

## 📝 Content Format

**Weekly Shows Include:**
- 4-6 matches per brand
- 1-2 segments between matches
- Full promo dialogue
- Business metrics (attendance, gate, ratings)
- Narrative prose style

**Special Events:**
- Brand PPVs every 4-5 weeks
- UWA Super Shows every 6-8 weeks

## 🏆 Current Champions (Week 0)

### UWA
- **World:** Avalanche Anderson (REIGN)

### REIGN
- **World:** Avalanche Anderson
- **Horizon:** Cameron Grayson
- **Women's:** Ivy Knight
- **DeathKore:** Chris Carnage
- **Tag Team:** Los Asesinos

### The Resistance
- **World:** Holden Nobody
- **Television:** Mike McCoy
- **Cruiserweight:** Pyro
- **Women's:** Mia Taylor
- **Tag Team:** The Southern Rebels

### PW:NEO
- **World:** Judge James Morgan
- **Internet:** Adam Winters
- **Women's:** Monica Cruz
- **Tag Team:** The Consortium

## ⚙️ GitHub Secrets Required

To run the automation, configure these secrets in your repository:

1. `ANTHROPIC_API_KEY` - Claude API key
2. `FTP_HOST` - FTP server hostname
3. `FTP_USERNAME` - FTP username
4. `FTP_PASSWORD` - FTP password
5. `FTP_REMOTE_DIR` - Target directory on server (e.g., `/public_html/uwa`)
6. `FTP_PORT` - FTP port (optional, defaults to 21)

See [SECRETS_SETUP.md](SECRETS_SETUP.md) for detailed configuration instructions.

## 📖 Documentation

- **[PROJECT_SPECIFICATION.md](PROJECT_SPECIFICATION.md)** - Complete technical and creative requirements
- **[UWA_COMPLETE_GUIDE.md](UWA_COMPLETE_GUIDE.md)** - Detailed roster, championships, and storylines
- **[SECRETS_SETUP.md](SECRETS_SETUP.md)** - GitHub Secrets configuration guide

## ✅ Implementation Status

### Completed (November 9, 2025):
- ✅ Website design and structure
- ✅ All HTML pages (index, about, results, archive)
- ✅ CSS styling with dark theme
- ✅ Tracking JSON files initialized
- ✅ GitHub Actions workflow
- ✅ FTP deployment script
- ✅ Secrets configuration
- ✅ FTP deployment tested and operational

### In Progress:
- ⏳ Show generation system (scripts/generate_shows.py)

### Upcoming:
- ⏳ End-to-end workflow testing
- ⏳ First automated show generation

## 🚀 Next Steps

1. ✅ Design and structure complete
2. ✅ GitHub Actions workflow configured
3. ✅ FTP deployment tested successfully
4. ⏳ Build show generation system
5. ⏳ Generate first week of shows
6. ⏳ Launch automation

## 🔗 Links

- **Repository:** https://github.com/surreal1st/uwa4
- **Final Design:** [final-design.html](final-design.html)
- **Design Mockups:** [design-mockups/](design-mockups/)

## 🧪 Testing

To manually trigger the workflow:
1. Go to [Actions](https://github.com/surreal1st/uwa4/actions)
2. Select "Generate UWA Weekly Shows"
3. Click "Run workflow"
4. Monitor execution

## 📊 Current Status

**Infrastructure:** ✅ Complete and operational
- Website deployed with styling
- FTP deployment functional
- GitHub Actions configured
- Tracking systems initialized

**Content Generation:** ⏳ Next phase
- Show generation system to be built
- Once complete, full automation will be operational

---

*A Reality Check Entertainment Production*