# Mother Repository Contents

Quick reference guide for all files and directories in this repository.

## Directory Structure

```
mother-repo/
├── README.md                      (This repository's main documentation)
├── SETUP_INSTRUCTIONS.md          (How to push to GitHub)
├── CONTENTS.md                    (This file - directory overview)
├── setup-repository.sh            (Automated setup script)
├── .gitignore                     (Git ignore rules)
├── REBRANDED_OUTPUT/              (172 MB, 304 files)
└── OEBPS/                         (11 MB, 208 files)
```

## REBRANDED_OUTPUT Directory (Production-Ready)

**Size:** 172 MB
**Files:** 304
**Status:** ✅ Production-ready EPUB 3.2 package

### Top-Level Files
```
REBRANDED_OUTPUT/
├── README.md                      (Detailed EPUB documentation)
├── AUTOMATION_SUMMARY.md          (Automation workflow details)
├── COMPLETION_REPORT.md           (Phase 3-5 completion report)
├── EPUB_AUTOMATION_GUIDE.md       (Automation guide)
├── FINAL_PROJECT_SUMMARY.md       (Complete project overview)
├── MASTER_CHAPTER_TEMPLATE.xhtml  (Chapter template)
├── MASTER_CHAPTER_TEMPLATE_README.md (Template documentation)
├── The-Artisans-Path.epub         (Pre-built EPUB ~85 MB)
├── build_fixed_epub.sh            (Build script)
├── content.opf                    (EPUB package manifest)
├── content.opf.backup             (Backup of manifest)
└── mimetype                       (EPUB identifier)
```

### Subdirectories

#### META-INF/
EPUB container specification
- `container.xml` - Points to content.opf location

#### fonts/ (6 files, 374 KB)
Embedded WOFF2 fonts
- `CinzelDecorative.woff2` - Decorative font for special elements
- `Montserrat-Bold.woff2` - Bold sans-serif for headings
- `Montserrat-Regular.woff2` - Regular sans-serif
- `librebaskerville-bold.woff2` - Bold serif
- `librebaskerville-italic.woff2` - Italic serif
- `librebaskerville-regular.woff2` - Regular serif body text

#### images/ (31 files, ~6.2 MB)
Optimized images for digital and print
- `chapter-i-quote.jpeg` through `chapter-xvi-quote.jpeg` (16 chapter quotes)
- `Michael.jpeg` - Author photo
- Various SVG graphics and supporting images
- All images optimized for EPUB (1400px min width)

#### xhtml/ (46 files)
Complete XHTML content

**Structure:**
```
xhtml/
├── nav.xhtml                      (Navigation with clickable TOC)
├── styles/
│   ├── style.css                  (Main digital stylesheet - 27KB)
│   ├── fonts.css                  (Font declarations)
│   └── artisan-path-style.css     (Branding stylesheet)
│
├── Frontmatter (7 files):
│   ├── 1-TitlePage.xhtml
│   ├── 2-Copyright.xhtml
│   ├── 3-TableOfContents.xhtml
│   ├── 4-AuthorNote.xhtml
│   ├── 5-HowToUse.xhtml
│   ├── 6-Dedication.xhtml
│   └── 7-Introduction.xhtml
│
├── Part Dividers (4 files):
│   ├── 8-part-i-intro.xhtml
│   ├── 22-part-ii-intro.xhtml
│   ├── 31-part-iii-intro.xhtml
│   └── 40-part-iv-intro.xhtml
│
├── Chapters (16 files):
│   ├── 9-chapter-i-1-laying-foundations.xhtml
│   ├── 10-chapter-ii-2-art-cutting.xhtml
│   ├── 11-chapter-iii-3-mastering-color.xhtml
│   ├── ... (13 more chapters)
│   └── 44-chapter-xvi-16-legacy-leadership.xhtml
│
└── Backmatter (17 files):
    ├── 45-Quiz-Answer-Key.xhtml
    ├── 46-Worksheet-Guide.xhtml
    ├── 47-Progress-Journal-1.xhtml
    ├── ... (14 more files)
    └── 60-Acknowledgments.xhtml
```

**Chapter Structure (6 sections each):**
1. Title page with Roman numeral badge
2-4. Content sections
5. Endnotes (if applicable)
6. Quiz (4 questions) + Worksheet (4 prompts)

#### pdf-pod/ (44 files, organized for print)
Print-ready 6×9" PDFs for print-on-demand

**Structure:**
```
pdf-pod/
├── ASSEMBLY_GUIDE.md              (Detailed POD instructions)
├── frontmatter/                   (7 PDFs)
├── part-dividers/                 (4 PDFs)
├── chapters/                      (16 PDFs)
└── backmatter/                    (17 PDFs)
```

Each PDF is formatted for 6×9" print with proper margins and page breaks.

#### Other Directories:
- **dist/** - Build output directory
- **scripts/** - Build and automation scripts
- **templates/** - XHTML templates
- **react-components/** - React-based preview components
- **.claude/** - Claude AI workflow configurations

## OEBPS Directory (Alternative Structure)

**Size:** 11 MB
**Files:** 208
**Status:** Legacy structure, alternative organization

### Structure
```
OEBPS/
├── content.opf                    (Alternative package manifest)
├── ebook/                         (eBook-specific assets)
├── fonts/                         (Embedded fonts)
├── images/                        (Image assets)
├── styles/                        (CSS stylesheets)
└── text/                          (XHTML content files)
```

This directory contains an alternative organization of the EPUB content with the same source material but different file structure.

## File Counts by Type

### REBRANDED_OUTPUT:
- XHTML files: 46
- CSS files: 3
- Font files: 6 (WOFF2)
- Image files: 31
- PDF files: 44
- Documentation: 7 markdown files
- Scripts: 2

### OEBPS:
- XHTML files: ~45 (in text/ directory)
- CSS files: Multiple (in styles/)
- Font files: Multiple (in fonts/)
- Image files: Multiple (in images/)

## Key Documentation Files

1. **Repository Level:**
   - `README.md` - Main repository documentation
   - `SETUP_INSTRUCTIONS.md` - GitHub setup guide
   - `CONTENTS.md` - This file
   - `setup-repository.sh` - Automated setup script

2. **REBRANDED_OUTPUT Level:**
   - `README.md` - EPUB-specific documentation
   - `FINAL_PROJECT_SUMMARY.md` - Complete project details
   - `COMPLETION_REPORT.md` - Production completion report
   - `MASTER_CHAPTER_TEMPLATE_README.md` - Template documentation
   - `pdf-pod/ASSEMBLY_GUIDE.md` - Print assembly instructions

3. **Technical Documentation:**
   - `AUTOMATION_SUMMARY.md` - Workflow automation
   - `EPUB_AUTOMATION_GUIDE.md` - Build automation guide

## Content Summary

**Book Details:**
- Title: The Artisan's Path
- Subtitle: A Comprehensive Guide to Professional Hairstyling Excellence
- Author: Michael David Warren Jr.
- Publisher: Terragon Labs
- Format: EPUB 3.2 + Print PDFs (6×9")

**Content:**
- 16 Chapters (organized in 4 Parts)
- 7 Frontmatter files
- 17 Backmatter files
- 64 quiz questions (4 per chapter)
- 64 worksheet prompts (4 per chapter)
- Complete answer key and worksheet guide

**Assets:**
- 31 optimized images
- 6 embedded fonts
- Professional CSS with teal/gold branding
- 44 print-ready PDFs

## Total Repository Size

- REBRANDED_OUTPUT: 172 MB
- OEBPS: 11 MB
- **Total: ~183 MB**

## Build Status

✅ All files validated and ready for distribution
✅ EPUB validates with EPUBCheck
✅ TOC navigation verified
✅ All assets optimized
✅ Print PDFs generated successfully
✅ 100% content preserved from original

---

**Last Updated:** December 17, 2024
**Source:** miketui/Fm repository
**Transferred to:** mother repository
