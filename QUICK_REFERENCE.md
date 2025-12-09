# Quick Reference - EPUB Files Status

## ✅ REBRANDED_OUTPUT: YOUR PRIMARY SOURCE

**Location:** `/REBRANDED_OUTPUT/`  
**Status:** ✅ COMPLETE & CORRECT  
**Use For:** Production EPUB compilation

| Asset Type | Count | Status | Notes |
|------------|-------|--------|-------|
| XHTML Files | 45 | ✅ CORRECT | Uses proper CSS paths: `styles/style.css` |
| CSS Files | 4 | ✅ CORRECT | In `xhtml/styles/` subdirectory |
| Images | 32 | ✅ OPTIMIZED | Total ~6.2MB, properly formatted |
| Fonts | 6 | ✅ EMBEDDED | WOFF2 format, 374KB total |
| content.opf | 1 | ✅ VALID | All references accurate |

**File Size Comparison (sample):**
- `9-chapter-i-unveiling-your-creative-odyssey.xhtml`: **42,327 bytes** ← LARGEST/MOST COMPLETE

---

## 📁 Other Folders - For Reference Only

### REBRANDED-output/ (lowercase)
**Status:** ⚠️ LEGACY VERSION  
**Issue:** Older content, smaller file sizes  
**Use For:** Backup reference only

**File Size Example:**
- `9-chapter-i-unveiling-your-creative-odyssey.xhtml`: 37,511 bytes ← 4,816 bytes LESS than REBRANDED_OUTPUT

---

### OEBPS/ and HOME/OEBPS/
**Status:** ❌ INCORRECT STRUCTURE  
**Issue:** Wrong CSS paths (`../styles/` instead of `styles/`)  
**Use For:** Test structure, not production

**File Size Example:**
- `9-chapter-i-unveiling-your-creative-odyssey.xhtml`: 36,630 bytes ← 5,697 bytes LESS than REBRANDED_OUTPUT

**Critical Issue:** CSS references like `<link href="../styles/style.css"/>` will NOT work with EPUB structure

---

### backups/
**Status:** 📦 ARCHIVED  
**Date:** September 14, 2025  
**Use For:** Historical rollback if needed

---

## 🔧 Minor Fixes Needed (3 total)

Before final EPUB compilation, fix these filename references:

1. **nav.xhtml** (line 21):
   - Change: `xhtml/6-affirmation-odyssey.xhtml`
   - To: `6-AffirmationOdyssey.xhtml`

2. **nav.xhtml** (line 61):
   - Change: `xhtml/29QuizKey.xhtml`
   - To: `29-QuizKey.xhtml`

3. **3-TableOfContents.xhtml** (line 146):
   - Change: `xhtml/29QuizKey.xhtml`
   - To: `29-QuizKey.xhtml`

---

## 🚀 Quick Build Commands

### Build EPUB
```bash
cd /home/runner/work/Fm/Fm
python3 scripts/build_epub.py --source REBRANDED_OUTPUT --output dist/book.epub
```

### Validate EPUB
```bash
# If EPUBCheck is installed
epubcheck dist/book.epub

# Or use the provided validation script
bash validate-epub.sh dist/book.epub
```

### Run Visual QA
```bash
python3 scripts/visual_review.py --root REBRANDED_OUTPUT --screenshots-dir docs/screenshots
```

---

## 📊 Decision Matrix

**Should I use REBRANDED_OUTPUT?** → ✅ YES (for production)  
**Should I use REBRANDED-output?** → ⚠️ NO (legacy backup only)  
**Should I use OEBPS or HOME?** → ❌ NO (incorrect CSS paths)  
**Are there newer versions in other branches?** → ❌ NO (only one branch exists)  
**Do I need to merge files from multiple folders?** → ❌ NO (REBRANDED_OUTPUT is complete)

---

## ✅ Bottom Line

**Use only REBRANDED_OUTPUT for EPUB compilation.**

It contains:
- ✅ Most complete content (largest file sizes)
- ✅ Correct CSS path references
- ✅ Proper EPUB 3.2 structure
- ✅ All required assets
- ✅ Latest updates

**Just fix the 3 navigation filename references and you're ready to publish!**

---

**For detailed analysis, see:**
- `REPOSITORY_ANALYSIS_SUMMARY.md` - Executive summary
- `docs/COMPREHENSIVE_ANALYSIS_REPORT.md` - Full technical report (465 lines)
