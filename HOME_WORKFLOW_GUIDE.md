# HOME Directory - EPUB Compilation Workflow

This guide explains how to use the HOME directory to compile and validate EPUB files.

## Quick Start

### 1. Verify the Structure
```bash
python3 verify_home_structure.py
```

Expected output:
```
✅ ALL CHECKS PASSED!
HOME directory is ready for EPUB compilation.
```

### 2. Build the EPUB
```bash
python3 build_home_epub.py
```

Output:
```
🔄 Creating EPUB from HOME directory...
📄 Adding mimetype...
📁 Adding META-INF...
📚 Adding OEBPS...
✅ EPUB created successfully: ./dist/home-curls-and-contemplation.epub
📊 File size: 1.89 MB
📋 Total files: 88
```

### 3. Validate the EPUB
```bash
java -jar epubcheck/epubcheck.jar dist/home-curls-and-contemplation.epub
```

Expected output:
```
Validating using EPUB version 3.3 rules.
No errors or warnings detected.
Messages: 0 fatals / 0 errors / 0 warnings / 0 infos
EPUBCheck completed
```

## What's in the HOME Directory?

The HOME directory contains a complete EPUB structure:

```
HOME/
├── mimetype                                    # EPUB mimetype (required first file)
├── META-INF/
│   └── container.xml                          # Points to package document
└── OEBPS/
    ├── content.opf                            # Package document with metadata
    ├── fonts/                                 # 6 font files in WOFF2 format
    ├── images/                                # 31 images (JPEG/SVG)
    ├── styles/                                # 3 CSS files (fonts, style, print)
    └── text/                                  # 45 XHTML content files
        ├── Frontmatter (1-7)
        ├── Part Dividers (8, 12, 18, 24)
        ├── Chapters (9-11, 13-17, 19-23, 25-27)
        └── Backmatter (28-44, nav.xhtml)
```

## File Details

### Total Files: 89
- **1** mimetype
- **1** container.xml
- **1** content.opf
- **45** XHTML text files
- **3** CSS stylesheets
- **6** font files
- **31** image files
- **1** README.md (documentation)

### XHTML Files (45 total)

**Frontmatter (7 files):**
1. Title Page
2. Copyright
3. Table of Contents
4. Dedication
5. Self Assessment
6. Affirmation Odyssey
7. Preface

**Parts (4 files):**
8. Part I: Foundations of Creative Hairstyling
12. Part II: Building Your Professional Practice
18. Part III: Advanced Business Strategies
24. Part IV: Future-Focused Growth

**Chapters (16 files):**
9. Chapter I: Unveiling Your Creative Odyssey
10. Chapter II: Refining Your Creative Toolkit
11. Chapter III: Reigniting Your Creative Fire
13. Chapter IV: The Art of Networking in Freelance Hairstyling
14. Chapter V: Cultivating Creative Excellence Through Mentorship
15. Chapter VI: Mastering the Business of Hairstyling
16. Chapter VII: Embracing Wellness and Self-Care
17. Chapter VIII: Advancing Skills Through Continuous Education
19. Chapter IX: Stepping into Leadership
20. Chapter X: Crafting Enduring Legacies
21. Chapter XI: Advanced Digital Strategies for Freelance Hairstylists
22. Chapter XII: Financial Wisdom Building Sustainable Ventures
23. Chapter XIII: Embracing Ethics and Sustainability in Hairstyling
25. Chapter XIV: The Impact of AI on the Beauty Industry
26. Chapter XV: Cultivating Resilience and Well-Being in Hairstyling
27. Chapter XVI: Tresses and Textures: Embracing Diversity in Hairstyling

**Backmatter (18 files):**
28. Conclusion
29. Quiz Key
30. Self Assessment
31. Affirmations Close
32. Continued Learning Commitment
33. Acknowledgments
34. About the Author
35. Curls & Contemplation Collective
36. Journaling Start
37. Manifesting Journal
38. Journal Page
39. Professional Development
40. SMART Goals
41. Self-Care Journal
42. Vision Journal
43. Doodle Page
44. Bibliography
nav.xhtml (Navigation document)

## Build Process Details

The `build_home_epub.py` script follows EPUB standards:

1. **Mimetype First**: Added uncompressed as the first file (required by EPUB spec)
2. **META-INF**: Contains container.xml pointing to content.opf
3. **OEBPS**: Contains all content, styles, fonts, and images
4. **Compression**: All files except mimetype are compressed using ZIP_DEFLATED

### EPUB Structure Compliance

✅ **EPUB 3.0+ Standards**
- Valid mimetype file
- Proper META-INF/container.xml
- Complete content.opf with metadata, manifest, and spine
- XHTML 1.1 compliant content files
- CSS stylesheets (no inline styles in templates)
- Proper namespace declarations

✅ **Accessibility**
- ARIA labels on sections
- Semantic HTML elements
- Alt text on images
- Proper heading hierarchy

✅ **Responsive Design**
- Mobile breakpoint at 768px
- Tablet/Desktop breakpoint at 1024px
- Responsive typography using clamp()
- Flexible layouts with CSS Grid and Flexbox

## Scripts

### verify_home_structure.py
Checks that the HOME directory has all required files and proper structure.

**Checks:**
- ✅ mimetype exists and is correct
- ✅ container.xml exists
- ✅ content.opf exists
- ✅ All subdirectories exist (text, styles, fonts, images)
- ✅ Required XHTML files exist
- ✅ Required CSS files exist
- ✅ Font files exist
- ✅ Image files exist

### build_home_epub.py
Creates an EPUB file from the HOME directory.

**Process:**
1. Creates dist/ directory if needed
2. Creates ZIP archive with proper EPUB structure
3. Adds mimetype first (uncompressed)
4. Adds META-INF files
5. Adds all OEBPS files
6. Reports file size and count

**Output:** `dist/home-curls-and-contemplation.epub`

## Validation

The EPUB can be validated using EPUBCheck:

```bash
java -jar epubcheck/epubcheck.jar dist/home-curls-and-contemplation.epub
```

### Expected Results
- ✅ No fatal errors
- ✅ No errors
- ✅ No warnings
- ✅ EPUB 3.3 compliant

## Testing the EPUB

### Using EPUB Readers

1. **Calibre** (Desktop)
   ```bash
   ebook-viewer dist/home-curls-and-contemplation.epub
   ```

2. **Apple Books** (macOS/iOS)
   - Import the EPUB file
   - Preview on different devices

3. **Google Play Books** (Web/Mobile)
   - Upload to your library
   - Test on web and mobile

4. **Adobe Digital Editions** (Desktop)
   - Open the EPUB file
   - Test page navigation

### Testing Checklist

- [ ] EPUB opens without errors
- [ ] Table of Contents works
- [ ] All pages render correctly
- [ ] Images display properly
- [ ] Fonts load correctly
- [ ] CSS styles are applied
- [ ] Page breaks work as expected
- [ ] Links and navigation work
- [ ] Responsive design works on different screen sizes
- [ ] Print styles work (if testing print)

## Modifying Content

### To Update Text Files

1. Edit files in `HOME/OEBPS/text/`
2. Save changes
3. Run `python3 verify_home_structure.py`
4. Run `python3 build_home_epub.py`
5. Validate with EPUBCheck

### To Update Styles

1. Edit files in `HOME/OEBPS/styles/`
   - `fonts.css` - Font definitions
   - `style.css` - Main styles (ACISS layout system)
   - `print.css` - Print-specific styles
2. Rebuild EPUB
3. Test in EPUB reader

### To Update Images

1. Add/replace images in `HOME/OEBPS/images/`
2. Update references in XHTML files if needed
3. Update content.opf manifest if adding new images
4. Rebuild EPUB

### To Update Metadata

1. Edit `HOME/OEBPS/content.opf`
2. Update metadata section (title, author, publisher, etc.)
3. Rebuild EPUB

## Troubleshooting

### EPUB Won't Open in Reader
- Run EPUBCheck to find validation errors
- Verify mimetype file is correct
- Check that container.xml points to correct content.opf path

### Images Not Displaying
- Verify image paths in XHTML files
- Check that images are in content.opf manifest
- Ensure image files exist in HOME/OEBPS/images/

### Fonts Not Loading
- Check font paths in fonts.css
- Verify fonts are in content.opf manifest
- Ensure font files exist in HOME/OEBPS/fonts/

### Styles Not Applied
- Check CSS file paths in XHTML <head> sections
- Verify CSS files are in content.opf manifest
- Clear reader cache and reload EPUB

### EPUBCheck Errors
- Read error messages carefully
- Fix reported issues in source files
- Re-run verification and rebuild

## Production Workflow

1. **Develop**: Edit content in HOME directory
2. **Verify**: Run `verify_home_structure.py`
3. **Build**: Run `build_home_epub.py`
4. **Validate**: Run EPUBCheck
5. **Test**: Open in multiple EPUB readers
6. **Review**: Check rendering, navigation, accessibility
7. **Deploy**: Distribute the validated EPUB file

## File Size Optimization

Current EPUB size: ~1.9 MB

To reduce size:
- Optimize images (reduce JPEG quality, optimize SVG)
- Remove unused fonts
- Minify CSS files
- Remove unused images

## Related Documentation

- **HOME/README.md** - HOME directory overview
- **/INDEX.md** - Complete documentation index
- **/QUICK_START_GUIDE.md** - Template usage guide
- **/EPUB_FORMATTING_HANDOFF.md** - Complete specifications
- **/templates/README.md** - Template documentation

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review related documentation
3. Validate with EPUBCheck for specific errors
4. Check XHTML syntax and CSS validity

---

**Status:** Production Ready ✅  
**EPUB Version:** 3.0+  
**Validation:** All checks passed  
**Last Updated:** 2025-10-22
