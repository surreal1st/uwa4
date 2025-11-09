#!/usr/bin/env python3
"""
UWA Results Page Generator
Generates results.html with the latest show and current champions
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime

class ResultsPageGenerator:
    """Generate results.html with latest show data"""
    
    def __init__(self, test_mode=False):
        """
        Initialize the results page generator
        
        Args:
            test_mode (bool): If True, use test directories
        """
        self.test_mode = test_mode
        self.repo_root = Path(__file__).parent.parent
        
        # Set up paths based on mode
        if test_mode:
            self.tracking_dir = self.repo_root / "tracking" / "test"
            self.shows_dir = self.repo_root / "test-shows"
        else:
            self.tracking_dir = self.repo_root / "tracking"
            self.shows_dir = self.repo_root / "shows"
        
        self.output_file = self.repo_root / "results.html"
        
    def load_championships(self):
        """Load current champions from championships.json"""
        champs_file = self.tracking_dir / "championships.json"
        if champs_file.exists():
            with open(champs_file, 'r') as f:
                return json.load(f)
        return None
    
    def get_latest_show(self):
        """Find the most recent show file"""
        if not self.shows_dir.exists():
            return None
        
        # Get all HTML files in shows directory
        show_files = list(self.shows_dir.glob("*.html"))
        
        if not show_files:
            return None
        
        # Sort by modification time to get latest
        show_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
        return show_files[0]
    
    def extract_show_summary(self, show_file):
        """Extract a summary from the show HTML file"""
        with open(show_file, 'r') as f:
            content = f.read()
        
        # Extract show week number from filename
        filename = show_file.stem  # e.g., "TEST-001" or "1"
        
        # Try to extract show metrics or key moments
        # For now, just return basic info
        return {
            'week': filename,
            'file': show_file.name,
            'path': f"shows/{show_file.name}" if not self.test_mode else f"test-shows/{show_file.name}"
        }
    
    def build_champions_html(self, champions_data):
        """Build the champions section HTML"""
        if not champions_data:
            return '<p>No championship data available</p>'
        
        champs = champions_data.get('champions', {})
        html = ""
        
        # REIGN Championships
        html += '<h3 style="margin-top: 30px; color: #DC143C;">REIGN Championships</h3>\n'
        html += '<div class="champions-grid">\n'
        
        if 'reign' in champs:
            for title in champs['reign']:
                if 'teamName' in title:
                    champion_name = title['teamName']
                else:
                    champion_name = title['champion']
                
                # Format title name (remove "REIGN" prefix for display)
                title_display = title['title'].replace('REIGN ', '')
                
                html += f'''    <div class="champion-item reign">
        <div class="champion-title">{title_display}</div>
        <div class="champion-name">{champion_name}</div>
    </div>\n'''
        
        html += '</div>\n\n'
        
        # Resistance Championships
        html += '<h3 style="margin-top: 40px; color: #00BFFF;">The Resistance Championships</h3>\n'
        html += '<div class="champions-grid">\n'
        
        if 'resistance' in champs:
            for title in champs['resistance']:
                if 'teamName' in title:
                    champion_name = title['teamName']
                else:
                    champion_name = title['champion']
                
                # Format title name (remove "Resistance" prefix for display)
                title_display = title['title'].replace('Resistance ', '')
                
                html += f'''    <div class="champion-item resistance">
        <div class="champion-title">{title_display}</div>
        <div class="champion-name">{champion_name}</div>
    </div>\n'''
        
        html += '</div>\n\n'
        
        # NEO Championships
        html += '<h3 style="margin-top: 40px; color: #9333EA;">PW:NEO Championships</h3>\n'
        html += '<div class="champions-grid">\n'
        
        if 'neo' in champs:
            for title in champs['neo']:
                if 'teamName' in title:
                    champion_name = title['teamName']
                else:
                    champion_name = title['champion']
                
                # Format title name (remove "NEO" prefix for display)
                title_display = title['title'].replace('NEO ', '')
                
                html += f'''    <div class="champion-item neo">
        <div class="champion-title">{title_display}</div>
        <div class="champion-name">{champion_name}</div>
    </div>\n'''
        
        html += '</div>\n'
        
        return html
    
    def build_latest_show_html(self, show_info):
        """Build the latest show section HTML"""
        if not show_info:
            return '''<div class="card" style="text-align: center; padding: 60px 40px;">
            <h2>Coming Soon</h2>
            <p style="font-size: 18px; margin-bottom: 30px;">The first week of UWA action will be released soon!</p>
            <p style="color: #888;">Check back every Friday for the latest results from all three brands.</p>
        </div>'''
        
        # Build show link card
        return f'''<div class="card">
            <h2>Week {show_info['week']} - Latest Results</h2>
            <p style="margin: 20px 0; font-size: 16px; color: #ccc;">
                All three brands competed this week! View the complete show for REIGN, The Resistance, and PW:NEO.
            </p>
            <div style="text-align: center; margin: 30px 0;">
                <a href="{show_info['path']}" class="btn-primary" style="display: inline-block; padding: 15px 40px; background: linear-gradient(135deg, #DC143C 0%, #00BFFF 50%, #9333EA 100%); color: white; text-decoration: none; border-radius: 8px; font-weight: bold; font-size: 18px;">
                    📺 Watch Week {show_info['week']}
                </a>
            </div>
            <p style="font-size: 14px; color: #888; margin-top: 20px;">
                Updated: {datetime.now().strftime("%B %d, %Y")}
            </p>
        </div>'''
    
    def generate_results_page(self):
        """Generate the complete results.html page"""
        print("\n📄 Generating results.html...")
        
        # Load data
        champions_data = self.load_championships()
        latest_show = self.get_latest_show()
        
        if latest_show:
            show_info = self.extract_show_summary(latest_show)
            print(f"  ✓ Found latest show: {show_info['week']}")
        else:
            show_info = None
            print("  ℹ No shows found yet")
        
        # Build HTML sections
        champions_html = self.build_champions_html(champions_data)
        show_html = self.build_latest_show_html(show_info)
        
        # Get current week for display
        current_week = "0"
        if champions_data:
            current_week = str(champions_data.get('currentWeek', 0))
        
        # Build complete page
        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Latest Results - United Wrestling Accord</title>
    <link rel="stylesheet" href="assets/css/style.css">
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
                    <li><a href="index.html">Home</a></li>
                    <li><a href="about.html">About</a></li>
                    <li><a href="results.html" class="active">Results</a></li>
                    <li><a href="archive.html">Archive</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <section class="content">
        <h1 class="section-title">Latest Results</h1>
        <p class="section-subtitle">Weekly shows air in-universe on Monday, Wednesday, and Friday • Page updates every Friday</p>
        
        <!-- Latest Show Section -->
        {show_html}
        
        <!-- Current Champions Section -->
        <div class="card">
            <h2>Current Champions</h2>
            {champions_html}
        </div>
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
</html>'''
        
        # Save file
        with open(self.output_file, 'w') as f:
            f.write(html)
        
        print(f"  ✓ Saved to {self.output_file}")
        print("  ✓ Results page generated successfully!")
    
    def run(self):
        """Main execution"""
        print("\n" + "="*60)
        print("UWA RESULTS PAGE GENERATOR")
        print("="*60)
        
        self.generate_results_page()
        
        print("="*60 + "\n")


def main():
    """Main entry point"""
    import argparse
    parser = argparse.ArgumentParser(description='Generate UWA results page')
    parser.add_argument('--test', action='store_true',
                       help='Use test mode directories')
    
    args = parser.parse_args()
    
    generator = ResultsPageGenerator(test_mode=args.test)
    generator.run()


if __name__ == "__main__":
    main()
