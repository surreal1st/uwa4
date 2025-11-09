# United Wrestling Accord - Automated Content Generator

An automated professional wrestling promotion featuring three distinct brands with AI-generated weekly shows, storylines, and championships.

## 🎭 The Brands

- **REIGN** (Fridays) - Los Angeles - Prestige & Legacy
- **The Resistance** (Mondays) - Northeast - Heart & Honor  
- **PW:NEO** (Wednesdays) - Chicago - Political Intrigue

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
├── /design-mockups            # Design options (reference)
├── index.html                 # Home page
├── about.html                 # About the UWA
├── results.html               # Latest weekly results (updated weekly)
├── archive.html               # Archive of all weeks (updated weekly)
├── UWA_COMPLETE_GUIDE.md      # Complete storyline reference
├── PROJECT_SPECIFICATION.md   # Full technical & creative specs
├── final-design.html          # Approved design reference
└── .github/workflows          # GitHub Actions (to be created)
```

## 🎨 Design

**Selected Design:** Modern Sports Clean (Dark Theme)
- Dark backgrounds for comfortable viewing
- Brand colors: REIGN (Red), The Resistance (Blue), PW:NEO (Purple)
- Responsive, mobile-friendly layout
- Clean, professional aesthetic

## 📊 Tracking System

The automation system maintains four JSON files:

1. **championships.json** - Current title holders and reign statistics
2. **match-history.json** - Complete record of every match
3. **injuries-absences.json** - Wrestler status and protected talent (SHOOT Project)
4. **storyline-progression.json** - Active storylines across all brands

## 🤖 Automation

- **Schedule:** Fridays at 2:00 AM EST
- **Platform:** GitHub Actions + Claude API
- **Process:** Generate 3 shows → Update tracking → Build HTML → Deploy via FTP
- **Content:** 7-10 minute read per show, 3 shows per week

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

## 📖 Documentation

- **[PROJECT_SPECIFICATION.md](PROJECT_SPECIFICATION.md)** - Complete technical and creative requirements
- **[UWA_COMPLETE_GUIDE.md](UWA_COMPLETE_GUIDE.md)** - Detailed roster, championships, and storylines

## 🚀 Next Steps

1. ✅ Design and structure complete
2. ⏳ Create show generation system
3. ⏳ Build GitHub Actions workflow
4. ⏳ Configure FTP deployment
5. ⏳ Generate first week of shows
6. ⏳ Launch automation

## 🔗 Links

- **Final Design:** [final-design.html](final-design.html)
- **Design Mockups:** [design-mockups/](design-mockups/)

---

*A Reality Check Entertainment Production*