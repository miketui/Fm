# Finding the Most Updated EPUB in REBRANDED_OUTPUT

## Quick Answer

**The most updated EPUB file is: `The-Artisans-Path-Normalized-v2.epub`**

- **Location**: `REBRANDED_OUTPUT/dist/The-Artisans-Path-Normalized-v2.epub`
- **Size**: 32.65 MB
- **Content Status**: Most complete with all fixes and full worksheet content

## Why This File?

According to the documentation in `docs/FINAL_NORMALIZATION_SUMMARY.md`, the "Normalized v2" edition contains:

1. **Fixed Chapter I Styling** - Resolved double drop-cap effect
2. **Complete Backmatter Worksheets** - Full content instead of placeholders:
   - Self-Care Journal (41-self-care-journal.xhtml)
   - Vision Journal (42-VisionJournal.xhtml)
   - Journal Page (38-journal-page.xhtml)
   - Creative Doodle Page (43-DoodlePage.xhtml)
3. **Proper Page Breaks** - All 16 chapters have correct page breaks
4. **46 Complete XHTML Files** - All chapters with full content

## All Available EPUB Files

| File | Size | Status | Description |
|------|------|--------|-------------|
| **The-Artisans-Path-Normalized-v2.epub** | 32.65 MB | ✅ Valid | **RECOMMENDED** - Latest complete edition |
| The-Artisans-Path-Normalized.epub | 16.32 MB | ✅ Valid | First normalized edition |
| The-Artisans-Path.epub | 6.38 MB | ✅ Valid | Standard production EPUB |
| curls.epub | 6.41 MB | ✅ Valid | Alternative build (62 XHTML files) |
| The-Artisans-Path1.epub | 0.00 MB | ❌ Invalid | Corrupted file |

## Using the Analysis Script

To get a detailed analysis of all EPUB files in the repository:

```bash
python3 find_most_updated_epub.py
```

### What the Script Does

1. **Scans** all EPUB files in `REBRANDED_OUTPUT/dist/`
2. **Validates** each file:
   - Checks for valid ZIP structure
   - Verifies mimetype is `application/epub+zip`
   - Confirms presence of required EPUB files
   - Counts XHTML chapters and images
3. **Prioritizes** based on content version:
   - Highest: "Normalized-v2" (latest content updates)
   - Medium: "Normalized" (intermediate)
   - Standard: Production versions
4. **Reports** comprehensive analysis with recommendations

### Sample Output

```
================================================================================
MOST UPDATED EPUB
================================================================================

✅ RECOMMENDED FILE: The-Artisans-Path-Normalized-v2.epub

📄 Filename: The-Artisans-Path-Normalized-v2.epub
📍 Path: /home/runner/work/Fm/Fm/REBRANDED_OUTPUT/dist/The-Artisans-Path-Normalized-v2.epub
📦 Size: 32.65 MB
🕐 Last Modified: 2025-12-09 14:33:02
✓ Validation: Valid EPUB structure
📊 Contents:
   - Total files: 101
   - XHTML chapters: 46
   - Images: 32
```

## Related Documentation

- `docs/FINAL_NORMALIZATION_SUMMARY.md` - Details of v2 changes
- `docs/DISTRIBUTION_PACKAGE_REPORT.md` - Production EPUB info
- `REBRANDED_OUTPUT/dist/README.md` - Distribution guide
- `docs/EPUB_VALIDATION_REPORT.md` - Validation details

## Technical Details

### Content Differences

**Normalized-v2 vs. Normalized:**
- Fixed drop-cap styling bug in Chapter I
- Replaced 4 placeholder worksheets with complete content
- Verified page breaks across all chapters

**Normalized-v2 vs. Standard (The-Artisans-Path.epub):**
- All normalization fixes included
- Same 46 XHTML chapter structure
- Larger file size due to uncompressed or additional assets

**curls.epub:**
- Alternative build with different chapter organization
- Contains 62 XHTML files (vs. standard 46)
- May represent an earlier project structure

## Quick Reference Commands

```bash
# Find the most updated EPUB (recommended method)
python3 find_most_updated_epub.py

# List all EPUBs with timestamps
ls -lh REBRANDED_OUTPUT/dist/*.epub

# Validate a specific EPUB with EPUBCheck (if installed)
epubcheck REBRANDED_OUTPUT/dist/The-Artisans-Path-Normalized-v2.epub

# Check EPUB contents
unzip -l REBRANDED_OUTPUT/dist/The-Artisans-Path-Normalized-v2.epub | head -50
```

## Conclusion

**Use `REBRANDED_OUTPUT/dist/The-Artisans-Path-Normalized-v2.epub`** for the most complete and up-to-date version of "The Artisan's Path" workbook with all content fixes and complete worksheets.
