#!/usr/bin/env python3
"""
UWA Show Generation System
Generates weekly shows for all three brands using Claude API
"""

import os
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path

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
        else:
            print("🚀 Running in PRODUCTION MODE")
            self.tracking_dir = self.repo_root / "tracking"
            self.shows_dir = self.repo_root / "shows"
        
        # Ensure directories exist
        self.tracking_dir.mkdir(parents=True, exist_ok=True)
        self.shows_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize tracking data
        self.championships = None
        self.match_history = None
        self.injuries = None
        self.storylines = None
        
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
            active_storylines = [s for s in self.storylines.get('storylines', []) if s.get('status') == 'active']
            print(f"\n  📖 Active Storylines: {len(active_storylines)}")
            for story in active_storylines[:3]:  # Show first 3
                print(f"    - {story.get('title', 'Untitled')} ({story.get('brand', 'Unknown')})")
        
        print("\n" + "="*60)
    
    def generate_shows(self):
        """Generate all three brand shows (placeholder for now)"""
        print("\n🎬 Generating shows...")
        print("  (This will call Claude API in the next step)")
        
    def update_tracking_files(self):
        """Update all tracking files after show generation (placeholder)"""
        print("\n💾 Updating tracking files...")
        print("  (This will update JSON files in the next step)")
        
    def create_html_pages(self):
        """Create results.html and archive pages (placeholder)"""
        print("\n📄 Creating HTML pages...")
        print("  (This will create HTML files in the next step)")
    
    def run(self):
        """Main execution flow"""
        print("\n" + "="*60)
        print("UWA SHOW GENERATOR")
        print("="*60)
        
        # Step 1: Load tracking files
        self.load_tracking_files()
        
        # Step 2: Print current state
        self.print_current_state()
        
        # Step 3: Generate shows (placeholder)
        self.generate_shows()
        
        # Step 4: Update tracking (placeholder)
        self.update_tracking_files()
        
        # Step 5: Create HTML (placeholder)
        self.create_html_pages()
        
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
