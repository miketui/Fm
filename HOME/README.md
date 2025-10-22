# HOME - EPUB Compilation Directory

This directory contains the complete EPUB structure ready to be compiled into an EPUB file.

## Directory Structure

```
HOME/
├── mimetype                    # EPUB mimetype file (must be first, uncompressed)
├── META-INF/
│   └── container.xml          # Points to content.opf
└── OEBPS/
    ├── content.opf            # Package document (metadata, manifest, spine)
    ├── fonts/                 # Font files (6 font files)
    │   ├── CinzelDecorative.woff2
    │   ├── Montserrat-Bold.woff2
    │   ├── Montserrat-Regular.woff2
    │   ├── librebaskerville-bold.woff2
    │   ├── librebaskerville-italic.woff2
    │   └── librebaskerville-regular.woff2
    ├── images/                # Image files (38 images)
    │   ├── Michael.jpeg
    │   ├── chapter-*-quote.jpeg (16 chapter quote images)
    │   ├── conclusion-quote.jpeg
    │   ├── preface-quote.jpeg
    │   └── *.svg (decorative elements)
    ├── styles/                # CSS stylesheets (3 files)
    │   ├── fonts.css         # Font definitions
    │   ├── print.css         # Print-specific styles
    │   └── style.css         # Main ACISS layout system styles
    └── text/                  # XHTML content files (45 files)
        ├── 1-TitlePage.xhtml
        ├── 2-Copyright.xhtml
        ├── 3-TableOfContents.xhtml
        ├── 4-Dedication.xhtml
        ├── 5-SelfAssessment.xhtml
        ├── 6-affirmation-odyssey.xhtml
        ├── 7-Preface.xhtml
        ├── 8-Part-I-Foundations-of-Creative-Hairstyling.xhtml
        ├── 9-chapter-i-unveiling-your-creative-odyssey.xhtml
        ├── 10-chapter-ii-refining-your-creative-toolkit.xhtml
        ├── ... (35 more chapter and backmatter files)
        └── nav.xhtml
```

## File Count Summary

- **Total Files:** 88
- **XHTML Text Files:** 45
- **CSS Files:** 3
- **Font Files:** 6
- **Image Files:** 38
- **Metadata Files:** 2 (mimetype, container.xml)
- **Package File:** 1 (content.opf)

## Content Organization

### Frontmatter (Files 1-7)
1. Title Page
2. Copyright
3. Table of Contents
4. Dedication
5. Self Assessment
6. Affirmation Odyssey
7. Preface

### Part Dividers (Files 8, 12, 18, 24)
- Part I: Foundations of Creative Hairstyling
- Part II: Building Your Professional Practice
- Part III: Advanced Business Strategies
- Part IV: Future-Focused Growth

### Chapters (Files 9-27)
16 chapters organized into 4 parts, each with:
- Title page
- Body content
- Endnotes (optional)
- Quiz (4 questions)
- Worksheet
- Closing image

### Backmatter (Files 28-44 + nav.xhtml)
- Conclusion
- Quiz Key
- Self Assessment
- Affirmations
- Continued Learning Commitment
- Acknowledgments
- About the Author
- Curls & Contemplation Collective
- Journaling pages (5 types)
- SMART Goals
- Doodle Page
- Bibliography
- Navigation (nav.xhtml)

## Building the EPUB

To compile this directory into an EPUB file, use the provided build script:

```bash
python3 build_home_epub.py
```

This will create `dist/home-curls-and-contemplation.epub` with:
- Correct mimetype (uncompressed, first file)
- Proper META-INF structure
- Complete OEBPS package

## EPUB Standards Compliance

This directory follows EPUB 3.0+ standards:
- ✅ Valid mimetype file
- ✅ META-INF/container.xml pointing to content.opf
- ✅ content.opf with metadata, manifest, and spine
- ✅ XHTML files with proper namespace declarations
- ✅ CSS stylesheets (ACISS layout system)
- ✅ Font files in WOFF2 format
- ✅ Images in JPEG/SVG formats
- ✅ Responsive design (mobile, tablet, desktop)
- ✅ Accessibility features (ARIA, semantic HTML)

## Templates Used

The files in this directory follow the template system from `/templates/`:
- **frontmatter-template.xhtml** - For files 1-7
- **part-divider-template.xhtml** - For files 8, 12, 18, 24
- **chapter-template.xhtml** - For files 9-27 (6-section structure)
- **backmatter-template.xhtml** - For files 28-44

## CSS Classes

All XHTML files use the ACISS layout system with CSS classes from `styles/style.css`:
- Page wrappers: `.frontmatter-page`, `.part-page`, `.chapter-page`, `.backmatter-page`
- Section classes: `.frontmatter-shell`, `.part-divider`, `.chapter-title`, etc.
- Typography classes: `.drop-cap`, `.body-text`, `.blockquote-text`, etc.
- Layout classes: `.quiz-grid`, `.journal-grid`, `.worksheet-section`, etc.
- Responsive breakpoints at 768px and 1024px

## Ready for Production

This directory is production-ready and can be:
1. Compiled into a valid EPUB file
2. Validated with EPUBCheck
3. Tested in EPUB readers
4. Published to digital bookstores

## File Size

Expected EPUB size: ~1.9 MB (compressed)

## Documentation

For more information, see:
- `/EPUB_FORMATTING_HANDOFF.md` - Complete specifications
- `/QUICK_START_GUIDE.md` - Template usage guide
- `/XHTML_TEMPLATES_IMPLEMENTATION.md` - Implementation details
- `/templates/README.md` - Template documentation
- `/INDEX.md` - Documentation index

---

**Status:** Ready for EPUB compilation ✅  
**Last Updated:** 2025-10-22  
**EPUB Version:** 3.0+
