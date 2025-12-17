# Mother Repository

This repository contains the complete EPUB production files for **"The Artisan's Path: A Comprehensive Guide to Professional Hairstyling Excellence"** by Michael David Warren Jr., published by Terragon Labs.

## 📚 Repository Contents

This repository includes two primary directories transferred from the main production repository:

### 1. REBRANDED_OUTPUT (172 MB, 304 files)
The complete production-ready EPUB 3.2 package with hybrid teal/gold branding.

**Contents:**
- ✅ Complete EPUB 3.0 package structure
- ✅ 46 XHTML content files (45 content + navigation)
- ✅ 44 Print-ready PDFs (6×9" POD format)
- ✅ 31 optimized images (~6.2MB total)
- ✅ 6 embedded WOFF2 fonts (374KB)
- ✅ Professional CSS stylesheets
- ✅ Complete documentation

**Structure:**
```
REBRANDED_OUTPUT/
├── META-INF/
│   └── container.xml
├── content.opf              (EPUB 3.2 manifest - 44 spine items)
├── mimetype                 (EPUB identifier)
├── fonts/                   (6 WOFF2 files)
├── images/                  (31 assets)
├── xhtml/                   (46 XHTML files)
│   ├── nav.xhtml
│   ├── styles/
│   │   ├── style.css
│   │   ├── fonts.css
│   │   └── artisan-path-style.css
│   └── (content files)
├── pdf-pod/                 (44 print-ready PDFs)
└── The-Artisans-Path.epub  (Pre-built EPUB)
```

### 2. OEBPS (11 MB, 208 files)
Alternative EPUB structure with legacy organization.

**Contents:**
- Standard OEBPS directory structure
- Complete text content
- Embedded fonts and images
- CSS stylesheets

**Structure:**
```
OEBPS/
├── content.opf
├── ebook/
├── fonts/
├── images/
├── styles/
└── text/
```

## 📖 Book Details

**Title:** The Artisan's Path: A Comprehensive Guide to Professional Hairstyling Excellence

**Author:** Michael David Warren Jr.

**Publisher:** Terragon Labs

**Format:** 
- Digital: EPUB 3.2
- Print: 6×9" Print-on-Demand PDFs

**Content:**
- 16 Chapters across 4 Parts
- 7 Frontmatter files
- 17 Backmatter files
- 64 quiz questions (4 per chapter)
- 64 worksheet prompts (4 per chapter)
- Complete answer key

## 🎨 Branding

**Hybrid Teal/Gold Color Scheme:**
- Primary Teal: #00796B, #00A896
- Accent Gold: #D4AF37, #C9A86A

**Typography:**
- Headings: Montserrat (sans-serif)
- Body: Libre Baskerville (serif)
- Decorative: Cinzel Decorative

## 🚀 Quick Start

### Build EPUB from REBRANDED_OUTPUT

```bash
cd REBRANDED_OUTPUT
zip -X -0 The-Artisans-Path.epub mimetype
zip -X -r The-Artisans-Path.epub META-INF content.opf fonts images xhtml
```

### Validate EPUB

If you have EPUBCheck installed:
```bash
java -jar epubcheck.jar REBRANDED_OUTPUT/The-Artisans-Path.epub
```

### Use Print-Ready PDFs

All 44 print-ready PDFs are organized in `REBRANDED_OUTPUT/pdf-pod/`:
- frontmatter/ (7 PDFs)
- part-dividers/ (4 PDFs)
- chapters/ (16 PDFs)
- backmatter/ (17 PDFs)

See `REBRANDED_OUTPUT/pdf-pod/ASSEMBLY_GUIDE.md` for complete assembly instructions.

## 📂 Key Files

### In REBRANDED_OUTPUT:
- **README.md** - Detailed documentation for REBRANDED_OUTPUT
- **FINAL_PROJECT_SUMMARY.md** - Complete project overview
- **COMPLETION_REPORT.md** - Phase 3-5 completion details
- **MASTER_CHAPTER_TEMPLATE.xhtml** - Template for chapter structure
- **content.opf** - EPUB package document (manifest & spine)
- **nav.xhtml** - Navigation with clickable TOC

### In OEBPS:
- **content.opf** - Alternative package document
- **text/** - XHTML content files
- **styles/** - CSS stylesheets
- **fonts/** - Embedded fonts
- **images/** - Image assets

## ✨ EPUB Features

**Each Chapter Includes:**
1. Professional title page with Roman numerals
2. Complete body content (100% preserved from original)
3. Endnotes (where applicable)
4. Chapter-specific quiz (4 questions)
5. Chapter-specific worksheet (4 prompts)
6. Inspirational closing image

**Standards Compliance:**
- EPUB 3.2 specification
- WCAG 2.2 AA accessibility
- Typography optimized for digital reading
- Asset optimization for fast loading

## 📊 Specifications

**REBRANDED_OUTPUT EPUB:**
- Format: EPUB 3.2
- Files: 46 XHTML + 31 images + 6 fonts
- Size: ~172 MB (includes PDFs)
- EPUB file: ~5.5 MB

**OEBPS Package:**
- Format: Standard EPUB structure
- Size: ~11 MB
- Alternative organization

**Print PDFs:**
- Page Size: 6" × 9"
- Files: 44 PDFs
- Total: ~2.0 MB
- Ready for: Amazon KDP, IngramSpark, Lulu

## 📚 Documentation

Both directories contain comprehensive documentation:

1. This README (overview)
2. REBRANDED_OUTPUT/README.md (detailed EPUB guide)
3. REBRANDED_OUTPUT/FINAL_PROJECT_SUMMARY.md (project overview)
4. REBRANDED_OUTPUT/COMPLETION_REPORT.md (production details)
5. REBRANDED_OUTPUT/pdf-pod/ASSEMBLY_GUIDE.md (POD instructions)

## 🚀 Distribution Channels

**Digital Platforms:**
- Amazon Kindle
- Apple Books
- Google Play Books
- Kobo
- Barnes & Noble Nook

**Print-on-Demand:**
- Amazon KDP Print
- IngramSpark
- Lulu

**Direct Sales:**
- Author website
- Gumroad
- Payhip

## ✅ Quality Assurance

- ✅ 100% content preserved from original manuscript
- ✅ All 64 quiz questions verified chapter-specific
- ✅ All 64 worksheet prompts verified chapter-specific
- ✅ EPUB package validates with EPUBCheck
- ✅ Clickable TOC verified
- ✅ All assets optimized and included
- ✅ 44 PDFs generated successfully (0 errors)

## 📞 Contact

**Author:** Michael David Warren Jr.
**Website:** https://www.michaeldavidhair.com
**Instagram:** @michaeldavidhair
**Publisher:** Terragon Labs

## 📄 Copyright

Copyright © 2025 Michael David Warren Jr. All rights reserved.

## 🎯 Status

**✅ PRODUCTION COMPLETE - READY FOR PUBLICATION**

All files verified, validated, and ready for both digital and print distribution.

---

**Last Updated:** December 17, 2024
**Transferred from:** miketui/Fm repository
**Repository:** mother
