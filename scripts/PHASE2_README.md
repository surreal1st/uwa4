# Phase 2: Results & Archive System

## ✅ Completed Features

Phase 2 adds automatic generation of website pages after each show is created:

1. **Results Page (`results.html`)** - Latest show and current champions
2. **Archive Page (`archive.html`)** - Complete show history

## 🚀 Quick Start

### Automatic Generation (Recommended)

When you run the main show generator, website pages are updated automatically:

```bash
# Test mode - updates results.html and archive.html with test data
python scripts/generate_shows.py --test

# Production mode - updates live pages
python scripts/generate_shows.py
```

### Manual Generation

You can also generate pages independently:

```bash
# Generate results page
python scripts/generate_results_page.py --test
python scripts/generate_results_page.py  # production

# Generate archive page
python scripts/generate_archive_page.py --test
python scripts/generate_archive_page.py  # production
```

## 📄 Script Details

### generate_results_page.py

**Purpose:** Creates `results.html` with latest show and current champions

**Features:**
- Displays most recent show with prominent link
- Shows all current champions by brand
- Brand-color coded sections (REIGN, Resistance, NEO)
- Responsive card-based design
- Auto-updates date stamp

**Data Sources:**
- `tracking/championships.json` (or test version)
- Latest file in `shows/` (or `test-shows/`)

**Output:** `/results.html` (root directory)

### generate_archive_page.py

**Purpose:** Creates `archive.html` with complete show archive

**Features:**
- Chronological listing (newest first)
- Show week numbers and dates
- Clickable links to individual shows
- Total show count display
- Formatted archive cards with hover effects

**Data Sources:**
- All HTML files in `shows/` (or `test-shows/`)
- File modification dates

**Output:** `/archive.html` (root directory)

## 🔄 Integration Flow

```
generate_shows.py
    ├─> Generate weekly shows (REIGN, Resistance, NEO)
    ├─> Update tracking files (championships, matches, storylines)
    ├─> Save show HTML files
    ├─> Call generate_results_page.py
    └─> Call generate_archive_page.py
```

## 📊 Page Structure

### Results Page

```html
Header (Navigation)
├─ Latest Show Section
│  ├─ Week number
│  ├─ Gradient button link to show
│  └─ Update date
└─ Current Champions Section
   ├─ REIGN Championships (Red theme)
   ├─ Resistance Championships (Blue theme)
   └─ NEO Championships (Purple theme)
```

### Archive Page

```html
Header (Navigation)
└─ Archive List
   ├─ Week X (Most recent)
   ├─ Week X-1
   ├─ Week X-2
   └─ ... (Chronological order)
```

## 🎨 Styling

Both pages use the existing `/assets/css/style.css` for:
- Brand color themes
- Card layouts
- Responsive design
- Navigation consistency

Additional inline styles for:
- Champion grids
- Archive item hover effects
- Gradient buttons

## 🧪 Test Mode Behavior

When using `--test` flag:
- Reads from `/tracking/test/*.json`
- Scans `/test-shows/` for show files
- Updates root `results.html` and `archive.html` with test data
- Show paths point to `test-shows/` directory

## 📝 Example Usage

### Complete Workflow
```bash
# 1. Generate new show (test mode)
python scripts/generate_shows.py --test

# 2. Pages automatically update:
#    - results.html shows latest test show
#    - archive.html lists all test shows

# 3. View results
open results.html
open archive.html
```

### Manual Updates
```bash
# Update results page after manual tracking changes
python scripts/generate_results_page.py

# Rebuild archive after adding shows manually
python scripts/generate_archive_page.py
```

## 🔧 Customization

### Changing Page Templates

Edit the HTML template strings in:
- `generate_results_page.py` → `build_champions_html()` and `build_latest_show_html()`
- `generate_archive_page.py` → `build_archive_list_html()`

### Modifying Show Links

Archive links are auto-generated as:
- Test: `test-shows/TEST-001.html`
- Production: `shows/1.html`

## 🐛 Troubleshooting

### "No shows found"
- Check that show files exist in correct directory
- Verify HTML files (not just .txt files)

### "Championship data not loading"
- Ensure `championships.json` exists in tracking directory
- Check JSON formatting is valid

### "Archive showing wrong shows"
- Test and production use same results/archive files
- Use `--test` flag consistently during testing

## ✨ Future Enhancements

Planned for future phases:
- Championship history visualization
- Storyline progress tracking
- Match statistics aggregation
- Wrestler profile pages
- Search functionality

## 📚 Related Documentation

- [PROJECT_SPECIFICATIONS.md](../PROJECT_SPECIFICATIONS.md) - Complete system overview
- [UWA_COMPLETE_GUIDE.md](../UWA_COMPLETE_GUIDE.md) - Roster and storylines
- Main generator: `generate_shows.py`

---

**Phase 2 Status:** ✅ Complete  
**Last Updated:** November 9, 2025
