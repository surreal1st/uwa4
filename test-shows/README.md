# Test Shows Directory

This directory contains generated show files during testing phase.

## Purpose

When running `python scripts/generate_shows.py --test`, all generated show files will be saved here instead of the production `/shows` directory.

## Structure

Test shows will be organized as:
```
test-shows/
  ├── TEST-001.html
  ├── TEST-002.html
  └── ...
```

## Important Notes

- **These are NOT canon** - Test shows are for development and testing purposes only
- Test files should be reviewed before any content is moved to production
- This directory can be cleaned/reset at any time during development

## Current Status

📂 Empty - Awaiting first test generation
