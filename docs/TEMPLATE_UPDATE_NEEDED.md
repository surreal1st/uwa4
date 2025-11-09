# Generate Shows Script Update Required

## Issue
The `build_combined_html()` method in `scripts/generate_shows.py` uses an old simple HTML template. It needs to match the Week 1 template with proper navigation, brand headers, and styling.

## Method to Replace
Find the `build_combined_html` method (around line 477) and replace it with the updated version below.

## Updated Method

```python
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
```

## Changes Made
1. Added proper header with UWA logo and full navigation
2. Added section title and subtitle with date
3. Added brand-colored quick navigation buttons
4. Each show section now has:
   - Brand logo in header
   - Brand-colored borders (via CSS classes)
   - Proper show-content wrapper
   - Location information
5. Added proper footer with logos

This matches the Week 1 template and will be applied to all future generations.
