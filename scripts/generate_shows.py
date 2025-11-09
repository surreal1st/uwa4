#!/usr/bin/env python3
"""
UWA Show Generation System
Generates weekly shows for all three brands using Claude API
"""

import os
import sys
import json
import argparse
import subprocess
from datetime import datetime
from pathlib import Path

# Anthropic SDK
try:
    from anthropic import Anthropic
except ImportError:
    print("ERROR: Anthropic SDK not installed. Run: pip install anthropic")
    sys.exit(1)

class UWAShowGenerator:
    """Main class for generating UWA weekly shows"""
    
    def __init__(self, test_mode=False):
        """
        Initialize the show generator
        
        Args:
            test_mode (bool): If True, use test directories and files
        """
        self.test_mode = test_mode
        self.repo_root = Path(__file__).parent.parent
        
        # Set up paths based on mode
        if test_mode:
            print("🧪 Running in TEST MODE")
            self.tracking_dir = self.repo_root / "tracking" / "test"
            self.shows_dir = self.repo_root / "test-shows"
            self.week_prefix = "TEST"
        else:
            print("🚀 Running in PRODUCTION MODE")
            self.tracking_dir = self.repo_root / "tracking"
            self.shows_dir = self.repo_root / "shows"
            self.week_prefix = "WEEK"
        
        # Ensure directories exist
        self.tracking_dir.mkdir(parents=True, exist_ok=True)
        self.shows_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize tracking data
        self.championships = None
        self.match_history = None
        self.injuries = None
        self.storylines = None
        self.complete_guide = None
        
        # Store generated data
        self.generated_matches = None
        self.week_number = None
        
        # Initialize Anthropic client
        api_key = os.environ.get('ANTHROPIC_API_KEY')
        if not api_key:
            print("ERROR: ANTHROPIC_API_KEY environment variable not set")
            sys.exit(1)
        self.client = Anthropic(api_key=api_key)
        
    def load_tracking_files(self):
        """Load all tracking JSON files"""
        print("\n📂 Loading tracking files...")
        
        # Define file paths
        files = {
            'championships': self.tracking_dir / 'championships.json',
            'match_history': self.tracking_dir / 'match-history.json',
            'injuries': self.tracking_dir / 'injuries-absences.json',
            'storylines': self.tracking_dir / 'storyline-progression.json'
        }
        
        # Load or create each file
        for name, filepath in files.items():
            if filepath.exists():
                print(f"  ✓ Loading {name} from {filepath}")
                with open(filepath, 'r') as f:
                    data = json.load(f)
                    setattr(self, name, data)
            else:
                print(f"  ⚠ {name} not found, creating from production template...")
                # In test mode, copy from production files if they don't exist
                if self.test_mode:
                    prod_file = self.repo_root / "tracking" / filepath.name
                    if prod_file.exists():
                        with open(prod_file, 'r') as f:
                            data = json.load(f)
                            setattr(self, name, data)
                        # Save to test location
                        with open(filepath, 'w') as f:
                            json.dump(data, f, indent=2)
                        print(f"  ✓ Created test version of {name}")
                    else:
                        print(f"  ✗ ERROR: Production file {prod_file} not found!")
                        setattr(self, name, {})
                else:
                    print(f"  ✗ ERROR: {filepath} not found!")
                    setattr(self, name, {})
        
        # Load UWA Complete Guide
        guide_path = self.repo_root / "UWA_COMPLETE_GUIDE.md"
        if guide_path.exists():
            print(f"  ✓ Loading UWA Complete Guide")
            with open(guide_path, 'r') as f:
                self.complete_guide = f.read()
        else:
            print(f"  ✗ ERROR: UWA_COMPLETE_GUIDE.md not found!")
            self.complete_guide = ""
    
    def print_current_state(self):
        """Print current state for verification"""
        print("\n📊 Current State:")
        print(f"  Mode: {'TEST' if self.test_mode else 'PRODUCTION'}")
        print(f"  Tracking Directory: {self.tracking_dir}")
        print(f"  Shows Directory: {self.shows_dir}")
        
        if self.championships:
            print(f"\n  Current Week: {self.championships.get('currentWeek', 'Unknown')}")
            print(f"  Last Updated: {self.championships.get('lastUpdated', 'Unknown')}")
            
            # Print current champions
            print("\n  🏆 Current Champions:")
            champs = self.championships.get('champions', {})
            
            # UWA World Champion
            if 'uwa' in champs:
                print(f"    UWA World: {champs['uwa']['champion']} ({champs['uwa']['brand']})")
            
            # REIGN Champions
            if 'reign' in champs:
                print("\n    REIGN:")
                for title in champs['reign']:
                    if 'teamName' in title:
                        print(f"      {title['title']}: {title['teamName']}")
                    else:
                        print(f"      {title['title']}: {title['champion']}")
            
            # Resistance Champions
            if 'resistance' in champs:
                print("\n    Resistance:")
                for title in champs['resistance']:
                    if 'teamName' in title:
                        print(f"      {title['title']}: {title['teamName']}")
                    else:
                        print(f"      {title['title']}: {title['champion']}")
            
            # NEO Champions
            if 'neo' in champs:
                print("\n    NEO:")
                for title in champs['neo']:
                    if 'teamName' in title:
                        print(f"      {title['title']}: {title['teamName']}")
                    else:
                        print(f"      {title['title']}: {title['champion']}")
        
        if self.storylines:
            # Collect all active storylines from all brands
            active_storylines = []
            storylines_data = self.storylines.get('storylines', {})
            for brand in ['reign', 'resistance', 'neo']:
                brand_stories = storylines_data.get(brand, [])
                active_storylines.extend([s for s in brand_stories if s.get('status') == 'active'])
            
            print(f"\n  📖 Active Storylines: {len(active_storylines)}")
            for story in active_storylines[:3]:  # Show first 3
                brand_name = 'REIGN' if 'reign' in story.get('id', '') else 'Resistance' if 'resistance' in story.get('id', '') else 'NEO'
                print(f"    - {story.get('title', 'Untitled')} ({brand_name})")
        
        print("\n" + "="*60)
    
    def build_prompt(self, week_number):
        """Build the comprehensive prompt for Claude"""
        print("\n📝 Building generation prompt...")
        
        # Format current champions
        champs_text = "CURRENT CHAMPIONS:\n"
        champs = self.championships.get('champions', {})
        
        if 'uwa' in champs:
            champs_text += f"UWA World: {champs['uwa']['champion']} ({champs['uwa']['brand']})\n"
        
        for brand_key, brand_name in [('reign', 'REIGN'), ('resistance', 'Resistance'), ('neo', 'NEO')]:
            if brand_key in champs:
                champs_text += f"\n{brand_name}:\n"
                for title in champs[brand_key]:
                    if 'teamName' in title:
                        champs_text += f"  {title['title']}: {title['teamName']}\n"
                    else:
                        champs_text += f"  {title['title']}: {title['champion']}\n"
        
        # Format active storylines
        storylines_text = "ACTIVE STORYLINES:\n"
        storylines_data = self.storylines.get('storylines', {})
        for brand_key, brand_name in [('reign', 'REIGN'), ('resistance', 'Resistance'), ('neo', 'NEO')]:
            brand_stories = storylines_data.get(brand_key, [])
            active_stories = [s for s in brand_stories if s.get('status') == 'active']
            if active_stories:
                storylines_text += f"\n{brand_name}:\n"
                for story in active_stories:
                    storylines_text += f"  - {story.get('title')} (ID: {story.get('id')})\n"
                    storylines_text += f"    Next Beat: {story.get('nextBeat')}\n"
        
        prompt = f"""You are generating weekly professional wrestling shows for the United Wrestling Accord (UWA). 

IMPORTANT CONTEXT:
This is Week {week_number} of the Reality Check Entertainment era.

{champs_text}

{storylines_text}

ROSTER AND CHARACTER DETAILS:
{self.complete_guide}

YOUR TASK:
Generate shows for all THREE brands in a single response:
1. REIGN (Los Angeles - Fridays)
2. The Resistance (Northeast - Mondays)  
3. PW:NEO (Chicago - Wednesdays)

REQUIREMENTS FOR EACH BRAND'S SHOW:

**CRITICAL: VARIATION AND FRESHNESS (NEW REQUIREMENT):**
- **Segment titles MUST be unique each week** - Never repeat titles like "The Mind Games Begin" or "Opening Segment: [Same Title]"
- Vary your storytelling approach between weeks:
  - Week 1 might open with a promo, Week 2 with a confrontation, Week 3 with a match
  - Rotate between backstage segments, in-ring promos, video packages, interview segments
  - Use different narrative structures (build tension vs. explosive action vs. character development)
- Even for continuing storylines, present them differently:
  - If last week was "The Mind Games Begin", this week could be "Psychological Warfare Escalates" or "Champion Under Siege"
  - Vary the participants in segments - different wrestlers commenting, different interview locations
  - Change the tone/format: formal promo → casual backstage → heated confrontation → calculated announcement
- Make each week feel like a new episode of TV, not a rerun
- Be creative with segment naming - make them descriptive and specific to THIS week's events

**Content Structure:**
- 4-6 matches per show
- 3-4 segments between matches (promos, backstage interviews, confrontations)
- Each match should advance at least one active storyline
- Include full promo dialogue in quotation marks
- Write in narrative prose style (like reading a wrestling newsletter)
- 7-10 minute read length per brand

**Match Variety:**
- Mix of singles, tag team, and multi-person matches
- Vary match types (regular, championship, non-title, etc.)
- Feature different wrestlers each week - avoid repetitive bookings
- Give development time to new/unbooked wrestlers occasionally

**Show Metrics** (realistic for each brand's venue):
- Attendance (venue capacity range)
- Gate revenue (based on ticket prices and attendance)
- TV rating (Nielsen rating for the timeslot)

**OUTPUT FORMAT:**
Return your response in TWO parts:

PART 1 - JSON DATA (for tracking):
<match_data>
{{
  "reign": [
    {{
      "participants": ["Wrestler A", "Wrestler B"],
      "winner": "Wrestler A",
      "method": "pinfall/submission/countout/dq",
      "duration": "12:45",
      "championship": "REIGN World Championship" (or null if non-title),
      "championship_change": false,
      "storyline_id": "reign-001",
      "storyline_advancement": "Brief description of how storyline progressed"
    }}
  ],
  "resistance": [...],
  "neo": [...],
  "storyline_updates": [
    {{
      "storyline_id": "reign-001",
      "new_next_beat": "Updated next beat based on what happened this week"
    }}
  ]
}}
</match_data>

PART 2 - PROPERLY FORMATTED HTML CONTENT:

CRITICAL HTML FORMATTING REQUIREMENTS:
- Use <h2> tags for segment titles (e.g., "Opening Segment", "Match 1", "Backstage Segment")
- Use <h3> tags for wrestler names or match participants
- Wrap EVERY paragraph in <p></p> tags
- Use <strong> tags for emphasis on important moments
- Use <em> tags for spoken dialogue attribution
- Add proper spacing with line breaks between sections
- Include <div class="show-metrics"> wrapper for the metrics section at the end

Example HTML structure for reference:
<h2>Opening Segment: Title Here</h2>
<p>First paragraph of content goes here.</p>
<p>Second paragraph continues the narrative.</p>

<h2>Match 1: Wrestler A vs. Wrestler B</h2>
<h3>Participants: Wrestler A vs. Wrestler B</h3>
<p>Match description with <strong>key moments</strong> emphasized.</p>
<p>Continued match narrative in separate paragraphs.</p>

<reign>
[Properly formatted HTML content with all tags as described above]
</reign>

<resistance>
[Properly formatted HTML content with all tags as described above]
</resistance>

<neo>
[Properly formatted HTML content with all tags as described above]
</neo>

REMEMBER: Every paragraph must be wrapped in <p> tags. Every section needs proper header tags. This is critical for readability on the website.

Begin generation now."""

        return prompt
    
    def generate_shows(self):
        """Generate all three brand shows using Claude API"""
        print("\n🎬 Generating shows via Claude API...")
        
        # Determine week number
        current_week = self.championships.get('currentWeek', 0)
        next_week = current_week + 1
        
        if self.test_mode:
            self.week_number = f"{self.week_prefix}-{next_week:03d}"
        else:
            self.week_number = next_week
        
        print(f"  Generating for: {self.week_number}")
        
        # Build prompt
        prompt = self.build_prompt(self.week_number)
        
        print(f"  Calling Claude API (model: claude-sonnet-4-20250514)...")
        print(f"  This may take 30-60 seconds...")
        
        try:
            # Call Claude API
            message = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=16000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            response_text = message.content[0].text
            print(f"  ✓ Received response ({len(response_text)} characters)")
            
            # Save raw response for debugging
            debug_file = self.shows_dir / f"{self.week_number}_raw_response.txt"
            with open(debug_file, 'w') as f:
                f.write(response_text)
            print(f"  ✓ Saved raw response to {debug_file}")
            
            # Parse the response to extract match data and HTML
            self.parse_response(response_text)
            
        except Exception as e:
            print(f"  ✗ ERROR calling Claude API: {e}")
            raise
    
    def parse_response(self, response_text):
        """Parse Claude's response to extract JSON data and HTML"""
        print("\n📄 Parsing response...")
        
        import re
        
        # Extract match data JSON
        match_data_match = re.search(r'<match_data>(.*?)</match_data>', response_text, re.DOTALL)
        if match_data_match:
            try:
                match_data_str = match_data_match.group(1).strip()
                # Remove markdown code blocks if present
                match_data_str = re.sub(r'```json\s*', '', match_data_str)
                match_data_str = re.sub(r'```\s*', '', match_data_str)
                self.generated_matches = json.loads(match_data_str)
                print(f"  ✓ Parsed match data JSON")
            except json.JSONDecodeError as e:
                print(f"  ✗ ERROR parsing match data JSON: {e}")
                print(f"  Raw match data: {match_data_str[:200]}...")
                self.generated_matches = None
        else:
            print("  ⚠ No match data found in response")
            self.generated_matches = None
        
        # Extract HTML sections
        reign_match = re.search(r'<reign>(.*?)</reign>', response_text, re.DOTALL)
        resistance_match = re.search(r'<resistance>(.*?)</resistance>', response_text, re.DOTALL)
        neo_match = re.search(r'<neo>(.*?)</neo>', response_text, re.DOTALL)
        
        if not all([reign_match, resistance_match, neo_match]):
            print("  ✗ ERROR: Could not find all three brand sections in response")
            print(f"  REIGN found: {bool(reign_match)}")
            print(f"  Resistance found: {bool(resistance_match)}")
            print(f"  NEO found: {bool(neo_match)}")
            return
        
        shows = {
            'REIGN': reign_match.group(1).strip(),
            'Resistance': resistance_match.group(1).strip(),
            'NEO': neo_match.group(1).strip()
        }
        
        # Save combined show file
        self.save_shows(shows)
        
    def save_shows(self, shows):
        """Save the combined HTML show file"""
        print("\n💾 Saving show files...")
        
        combined_html = self.build_combined_html(shows)
        show_file = self.shows_dir / f"{self.week_number}.html"
        
        with open(show_file, 'w') as f:
            f.write(combined_html)
        
        print(f"  ✓ Saved combined show: {show_file}")
        
    def build_combined_html(self, shows):
        """Combine all three brand shows into one HTML file"""
        
        # Get current date
        current_date = datetime.now().strftime("%B %d, %Y")
        
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UWA Week {self.week_number} - All Shows</title>
    <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>
    <header>
        <div class="header-content">
            <div class="logo-section">
                <img src="https://sp2025.shootproject.com/uploads/UWA-transparent.png" alt="UWA Logo" class="main-logo">
                <span class="site-title">UWA</span>
            </div>
            <nav>
                <ul>
                    <li><a href="../index.html">Home</a></li>
                    <li><a href="../about.html">About</a></li>
                    <li><a href="../results.html">Results</a></li>
                    <li><a href="../archive.html">Archive</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <section class="content">
        <h1 class="section-title">Week {self.week_number} - All Three Brand Shows</h1>
        <p class="section-subtitle">{current_date}</p>
        
        <!-- Quick Navigation -->
        <div class="card" style="text-align: center; padding: 30px;">
            <h2 style="margin-bottom: 20px;">Jump to Show</h2>
            <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
                <a href="#reign" style="display: inline-block; padding: 12px 30px; background: #DC143C; color: white; text-decoration: none; border-radius: 6px; font-weight: 600; transition: all 0.3s;">REIGN: Ascension</a>
                <a href="#resistance" style="display: inline-block; padding: 12px 30px; background: #00BFFF; color: white; text-decoration: none; border-radius: 6px; font-weight: 600; transition: all 0.3s;">Resistance: Uprising</a>
                <a href="#neo" style="display: inline-block; padding: 12px 30px; background: #9333EA; color: white; text-decoration: none; border-radius: 6px; font-weight: 600; transition: all 0.3s;">PW:NEO: Paradigm Shift</a>
            </div>
        </div>

        <!-- REIGN Show -->
        <section id="reign" class="show-section">
            <div class="show-header reign">
                <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 15px;">
                    <img src="https://sp2025.shootproject.com/uploads/REIGN-transparent.png" alt="REIGN" style="height: 60px;">
                    <h2 style="margin: 0;">REIGN: Ascension</h2>
                </div>
                <div class="show-meta">
                    <span>📍 Los Angeles, CA</span>
                </div>
            </div>
            <div class="show-content">
                {shows['REIGN']}
            </div>
        </section>

        <!-- The Resistance Show -->
        <section id="resistance" class="show-section" style="margin-top: 60px;">
            <div class="show-header resistance">
                <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 15px;">
                    <img src="https://sp2025.shootproject.com/uploads/TheResistance-transparent.png" alt="The Resistance" style="height: 60px;">
                    <h2 style="margin: 0;">Resistance: Uprising</h2>
                </div>
                <div class="show-meta">
                    <span>📍 Philadelphia, PA</span>
                </div>
            </div>
            <div class="show-content">
                {shows['Resistance']}
            </div>
        </section>

        <!-- PW:NEO Show -->
        <section id="neo" class="show-section" style="margin-top: 60px;">
            <div class="show-header neo">
                <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 15px;">
                    <img src="https://sp2025.shootproject.com/uploads/NEO-transparent.png" alt="PW:NEO" style="height: 60px;">
                    <h2 style="margin: 0;">PW:NEO: Paradigm Shift</h2>
                </div>
                <div class="show-meta">
                    <span>📍 Chicago, IL</span>
                </div>
            </div>
            <div class="show-content">
                {shows['NEO']}
            </div>
        </section>
    </section>

    <footer>
        <div class="footer-content">
            <div class="footer-logos">
                <img src="https://sp2025.shootproject.com/uploads/RCE-transparent.png" alt="Reality Check Entertainment" class="footer-logo">
                <img src="https://sp2025.shootproject.com/uploads/UWA-transparent.png" alt="UWA" class="footer-logo">
            </div>
            <p>&copy; 2025 United Wrestling Accord. A Reality Check Entertainment Production.</p>
        </div>
    </footer>
</body>
</html>"""
        
        return html
        
    def update_tracking_files(self):
        """Update all tracking files after show generation"""
        print("\n💾 Updating tracking files...")
        
        if not self.generated_matches:
            print("  ⚠ No match data to process, skipping tracking updates")
            return
        
        # Update match history
        self.update_match_history()
        
        # Update championships
        self.update_championships()
        
        # Update storylines
        self.update_storylines()
        
        print("  ✓ All tracking files updated")
        
    def update_match_history(self):
        """Update match-history.json with new matches"""
        print("  📝 Updating match history...")
        
        today = datetime.now().strftime("%Y-%m-%d")
        
        # Add all matches from all brands
        for brand in ['reign', 'resistance', 'neo']:
            brand_matches = self.generated_matches.get(brand, [])
            for match in brand_matches:
                match_record = {
                    "week": self.week_number,
                    "brand": brand,
                    "date": today,
                    "participants": match.get('participants', []),
                    "winner": match.get('winner'),
                    "method": match.get('method'),
                    "duration": match.get('duration'),
                    "championship": match.get('championship'),
                    "championship_change": match.get('championship_change', False),
                    "storyline_id": match.get('storyline_id')
                }
                self.match_history['matches'].append(match_record)
        
        # Update metadata
        self.match_history['totalMatches'] = len(self.match_history['matches'])
        self.match_history['lastUpdated'] = today
        
        # Save updated file
        history_file = self.tracking_dir / 'match-history.json'
        with open(history_file, 'w') as f:
            json.dump(self.match_history, f, indent=2)
        
        print(f"    ✓ Added {sum(len(self.generated_matches.get(b, [])) for b in ['reign', 'resistance', 'neo'])} matches")
    
    def update_championships(self):
        """Update championships.json with title defenses and changes"""
        print("  🏆 Updating championships...")
        
        today = datetime.now().strftime("%Y-%m-%d")
        
        # Count defenses for each championship
        for brand in ['reign', 'resistance', 'neo']:
            brand_matches = self.generated_matches.get(brand, [])
            for match in brand_matches:
                if match.get('championship'):
                    championship_title = match['championship']
                    
                    # Find and update the champion's defense count
                    if brand == 'reign':
                        for title in self.championships['champions']['reign']:
                            if title.get('title') == championship_title:
                                title['defenses'] = title.get('defenses', 0) + 1
                    elif brand == 'resistance':
                        for title in self.championships['champions']['resistance']:
                            if title.get('title') == championship_title:
                                title['defenses'] = title.get('defenses', 0) + 1
                    elif brand == 'neo':
                        for title in self.championships['champions']['neo']:
                            if title.get('title') == championship_title:
                                title['defenses'] = title.get('defenses', 0) + 1
                    
                    # Handle championship changes
                    if match.get('championship_change'):
                        # TODO: Implement championship change logic
                        print(f"    ⚠ Championship change detected: {championship_title} - needs manual update")
        
        # Update metadata
        current_week = self.championships.get('currentWeek', 0)
        self.championships['currentWeek'] = current_week + 1
        self.championships['lastUpdated'] = today
        
        # Save updated file
        champs_file = self.tracking_dir / 'championships.json'
        with open(champs_file, 'w') as f:
            json.dump(self.championships, f, indent=2)
        
        print(f"    ✓ Updated to Week {self.championships['currentWeek']}")
    
    def update_storylines(self):
        """Update storyline-progression.json with new beats"""
        print("  📖 Updating storylines...")
        
        today = datetime.now().strftime("%Y-%m-%d")
        
        # Update next beats based on generated data
        storyline_updates = self.generated_matches.get('storyline_updates', [])
        for update in storyline_updates:
            storyline_id = update.get('storyline_id')
            new_next_beat = update.get('new_next_beat')
            
            # Find and update the storyline
            for brand in ['reign', 'resistance', 'neo']:
                brand_stories = self.storylines['storylines'].get(brand, [])
                for story in brand_stories:
                    if story.get('id') == storyline_id:
                        story['nextBeat'] = new_next_beat
                        print(f"    ✓ Updated {storyline_id}: {new_next_beat}")
        
        # Update metadata
        current_week = self.storylines.get('currentWeek', 0)
        self.storylines['currentWeek'] = current_week + 1
        self.storylines['lastUpdated'] = today
        
        # Save updated file
        storylines_file = self.tracking_dir / 'storyline-progression.json'
        with open(storylines_file, 'w') as f:
            json.dump(self.storylines, f, indent=2)
        
        print(f"    ✓ Updated to Week {self.storylines['currentWeek']}")
        
    def create_html_pages(self):
        """Create results.html and archive.html pages"""
        print("\n📄 Generating website pages...")
        
        try:
            # Import the page generators
            sys.path.insert(0, str(self.repo_root / "scripts"))
            from generate_results_page import ResultsPageGenerator
            from generate_archive_page import ArchivePageGenerator
            
            # Generate results page
            print("  📊 Generating results.html...")
            results_gen = ResultsPageGenerator(test_mode=self.test_mode)
            results_gen.generate_results_page()
            
            # Generate archive page
            print("  📚 Generating archive.html...")
            archive_gen = ArchivePageGenerator(test_mode=self.test_mode)
            archive_gen.generate_archive_page()
            
            print("  ✓ Website pages generated successfully!")
            
        except Exception as e:
            print(f"  ⚠ Warning: Could not generate website pages: {e}")
            print("  Continuing without website page generation...")
    
    def deploy_to_ftp(self):
        """
        Deploy files to FTP server (production only)
        
        In production mode, calls the deploy_ftp.py script to upload all files.
        In test mode, this step is automatically skipped.
        """
        if self.test_mode:
            print("\n⏭️  Skipping FTP deployment (test mode)")
            return
        
        print("\n🚀 Deploying to FTP server...")
        
        # Check for FTP credentials
        ftp_host = os.environ.get('FTP_HOST')
        ftp_username = os.environ.get('FTP_USERNAME')
        ftp_password = os.environ.get('FTP_PASSWORD')
        
        if not all([ftp_host, ftp_username, ftp_password]):
            print("  ⚠ FTP credentials not found in environment variables")
            print("  Skipping FTP deployment")
            print("  Required: FTP_HOST, FTP_USERNAME, FTP_PASSWORD")
            return
        
        try:
            # Call deploy_ftp.py script as subprocess
            deploy_script = self.repo_root / "scripts" / "deploy_ftp.py"
            
            print(f"  📤 Calling deployment script: {deploy_script}")
            
            result = subprocess.run(
                [sys.executable, str(deploy_script)],
                cwd=str(self.repo_root),
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )
            
            # Print deployment output
            if result.stdout:
                print(result.stdout)
            
            if result.returncode == 0:
                print("  ✅ FTP deployment completed successfully!")
            else:
                print(f"  ⚠ FTP deployment exited with code {result.returncode}")
                if result.stderr:
                    print(f"  Error output: {result.stderr}")
                    
        except subprocess.TimeoutExpired:
            print("  ⚠ FTP deployment timed out after 5 minutes")
        except Exception as e:
            print(f"  ⚠ FTP deployment failed: {e}")
            print("  Continuing without deployment...")
    
    def run(self):
        """Main execution flow"""
        print("\n" + "="*60)
        print("UWA SHOW GENERATOR")
        print("="*60)
        
        # Step 1: Load tracking files
        self.load_tracking_files()
        
        # Step 2: Print current state
        self.print_current_state()
        
        # Step 3: Generate shows
        self.generate_shows()
        
        # Step 4: Update tracking
        self.update_tracking_files()
        
        # Step 5: Generate website pages
        self.create_html_pages()
        
        # Step 6: Deploy to FTP (production only)
        self.deploy_to_ftp()
        
        print("\n✅ Generation complete!")
        print("="*60 + "\n")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='Generate UWA weekly shows')
    parser.add_argument('--test', action='store_true', 
                       help='Run in test mode (uses test directories and files)')
    
    args = parser.parse_args()
    
    # Create and run generator
    generator = UWAShowGenerator(test_mode=args.test)
    generator.run()


if __name__ == "__main__":
    main()
