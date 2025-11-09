#!/usr/bin/env python3
"""
UWA Archive Page Generator
Generates archive.html with links to all past shows
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime
import re

class ArchivePageGenerator:
    """Generate archive.html with all past shows"""
    
    def __init__(self, test_mode=False):
        """
        Initialize the archive page generator
        
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
        
        self.output_file = self.repo_root / "archive.html"
    
    def get_all_shows(self):
        """Get all show files sorted by week number"""
        if not self.shows_dir.exists():
            return []
        
        # Get all HTML files
        show_files = list(self.shows_dir.glob("*.html"))
        
        # Filter out non-show files (like READMEs)
        show_files = [f for f in show_files if f.stem not in ['README', 'readme']]
        
        if not show_files:
            return []
        
        # Sort shows
        def get_week_number(filename):
            """Extract week number for sorting"""
            stem = filename.stem
            
            # Handle TEST-001 format
            if 'TEST-' in stem:
                match = re.search(r'TEST-(\d+)', stem)
                if match:
                    return int(match.group(1))
            
            # Handle WEEK-1 or just "1" format
            match = re.search(r'(\d+)', stem)
            if match:
                return int(match.group(1))
            
            return 0
        
        show_files.sort(key=get_week_number, reverse=True)  # Most recent first
        return show_files
    
    def get_show_metadata(self, show_file):
        """Extract metadata from a show file"""
        stem = show_file.stem
        
        # Get week display name
        if 'TEST-' in stem:
            week_display = stem  # e.g., "TEST-001"
            week_num = re.search(r'TEST-(\d+)', stem)
            week_number = int(week_num.group(1)) if week_num else 0
        else:
            week_num = re.search(r'(\d+)', stem)
            week_number = int(week_num.group(1)) if week_num else 0
            week_display = f"Week {week_number}"
        
        # Get file stats
        stat = show_file.stat()
        date_str = datetime.fromtimestamp(stat.st_mtime).strftime("%B %d, %Y")
        
        # Build path
        if self.test_mode:
            path = f"test-shows/{show_file.name}"
        else:
            path = f"shows/{show_file.name}"
        
        return {
            'week_display': week_display,
            'week_number': week_number,
            'date': date_str,
            'path': path,
            'filename': show_file.name
        }
    
    def build_archive_list_html(self, shows):
        """Build the archive list HTML"""
        if not shows:
            return '''<li style="text-align: center; padding: 40px; color: #888;">
                No shows archived yet. Check back after the first week of action!
            </li>'''
        
        html = ""
        for show in shows:
            metadata = self.get_show_metadata(show)
            
            html += f'''        <li class="archive-item">
            <a href="{metadata['path']}" class="archive-link">
                <div class="archive-week">{metadata['week_display']}</div>
                <div class="archive-date">{metadata['date']}</div>
                <div class="archive-brands">REIGN • Resistance • PW:NEO</div>
            </a>
        </li>\n'''
        
        return html
    
    def generate_archive_page(self):
        """Generate the complete archive.html page"""
        print("\n📚 Generating archive.html...")
        
        # Get all shows
        shows = self.get_all_shows()
        
        if shows:
            print(f"  ✓ Found {len(shows)} show(s)")
        else:
            print("  ℹ No shows found yet")
        
        # Build archive list
        archive_html = self.build_archive_list_html(shows)
        
        # Build complete page
        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Archive - United Wrestling Accord</title>
    <link rel="stylesheet" href="assets/css/style.css">
    <style>
        .archive-list {{
            list-style: none;
            padding: 0;
            margin: 0;
        }}
        
        .archive-item {{
            margin-bottom: 15px;
        }}
        
        .archive-link {{
            display: block;
            padding: 20px 25px;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            text-decoration: none;
            color: inherit;
            transition: all 0.3s ease;
        }}
        
        .archive-link:hover {{
            background: rgba(255, 255, 255, 0.06);
            border-color: rgba(255, 255, 255, 0.2);
            transform: translateX(5px);
        }}
        
        .archive-week {{
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 8px;
            background: linear-gradient(135deg, #DC143C 0%, #00BFFF 50%, #9333EA 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        
        .archive-date {{
            font-size: 14px;
            color: #888;
            margin-bottom: 5px;
        }}
        
        .archive-brands {{
            font-size: 12px;
            color: #666;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
    </style>
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
                    <li><a href="results.html">Results</a></li>
                    <li><a href="archive.html" class="active">Archive</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <section class="content">
        <h1 class="section-title">Show Archive</h1>
        <p class="section-subtitle">Browse past weeks of UWA action • {len(shows)} week(s) archived</p>
        
        <div class="card">
            <h2>All Weeks</h2>
            <ul class="archive-list">
{archive_html}
            </ul>
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
        print("  ✓ Archive page generated successfully!")
    
    def run(self):
        """Main execution"""
        print("\n" + "="*60)
        print("UWA ARCHIVE PAGE GENERATOR")
        print("="*60)
        
        self.generate_archive_page()
        
        print("="*60 + "\n")


def main():
    """Main entry point"""
    import argparse
    parser = argparse.ArgumentParser(description='Generate UWA archive page')
    parser.add_argument('--test', action='store_true',
                       help='Use test mode directories')
    
    args = parser.parse_args()
    
    generator = ArchivePageGenerator(test_mode=args.test)
    generator.run()


if __name__ == "__main__":
    main()
