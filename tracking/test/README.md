# Test Tracking Files

This directory contains test versions of all tracking JSON files used during development and testing.

## Purpose

When running `python scripts/generate_shows.py --test`, the script uses these test files instead of the production tracking files in `/tracking/`.

## Files

- **championships.json** - Test championship data (titles, champions, reign statistics)
- **match-history.json** - Test match records
- **injuries-absences.json** - Test injury tracking and protected wrestlers
- **storyline-progression.json** - Test storyline data

## How It Works

1. On first test run, files are copied from production `/tracking/` folder
2. Test generations update these files (leaving production files untouched)
3. You can reset test files by deleting this directory and running `--test` again

## Current State

Starting from Week 0 (initial state) with all current champions and storylines.

## Important Notes

- **Safe Testing** - Production files are never modified during test runs
- **Independent** - Test tracking is completely separate from production
- **Resettable** - Can delete and regenerate at any time
- **Not Canon** - Changes here don't affect production until manually promoted
