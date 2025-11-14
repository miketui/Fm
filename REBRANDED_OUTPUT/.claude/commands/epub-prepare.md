# EPUB Preparation Workflow Command

You are an EPUB preparation specialist. Your task is to run the complete preparation workflow to ensure all HTML/XHTML files are properly formatted, validated, and ready for error-free EPUB distribution.

## Complete Workflow

This command orchestrates the full EPUB preparation process from validation through final packaging.

### Phase 1: Pre-Flight Checks
1. Verify directory structure is intact
2. Check all required files are present:
   - `content.opf`
   - `mimetype`
   - `META-INF/container.xml`
   - Navigation file (`xhtml/nav.xhtml`)
3. Confirm all assets exist:
   - Images (31 files in `images/`)
   - Fonts (6 files in `fonts/`)
   - Stylesheets (`styles/`)
4. Check file permissions

### Phase 2: XHTML Formatting & Linting
1. Run XHTML validation on all files in `xhtml/` and `templates/`
2. Check for:
   - Well-formed XML structure
   - Proper DOCTYPE declarations
   - Valid namespace declarations
   - Closed tags
   - Valid entities and character references
3. Lint for best practices:
   - Semantic HTML5 elements
   - Accessibility attributes
   - Proper heading hierarchy
   - Alt text on images
4. Auto-fix common issues where possible

### Phase 3: Content Verification
1. Verify content integrity:
   - All chapters present (16 chapters)
   - All frontmatter files (7 files)
   - All backmatter files (17 files)
2. Check internal consistency:
   - Table of contents matches actual content
   - All internal links resolve
   - All references are valid
3. Validate manifest in `content.opf`:
   - All files listed
   - Correct media types
   - Proper IDs

### Phase 4: Package Validation
1. Validate OPF package document
2. Verify spine order
3. Check metadata completeness:
   - Title
   - Author
   - Language
   - Publication date
   - ISBN/Identifier
4. Validate NCX (if present)

### Phase 5: Standards Compliance
1. Check EPUB 3.0 specification compliance
2. Validate accessibility features
3. Verify language attributes
4. Check for deprecated elements
5. Validate media overlays (if applicable)

### Phase 6: Build & Final Validation
1. Build EPUB package (uncompressed mimetype first)
2. Run epubcheck on built EPUB
3. Verify file integrity
4. Test in multiple readers if possible
5. Generate final validation report

## Execution Commands

Run these subagent scripts in sequence:

```bash
cd /home/user/Fm/REBRANDED_OUTPUT

# 1. Validate XHTML files
./scripts/subagents/validate-xhtml.sh

# 2. Verify EPUB package structure
./scripts/subagents/validate-epub-package.sh

# 3. Check content integrity
./scripts/subagents/check-content-integrity.sh

# 4. Build EPUB
./scripts/subagents/build-epub.sh

# 5. Final validation
./scripts/subagents/final-validation.sh
```

## Output

Provide a comprehensive preparation report:

```
═══════════════════════════════════════════════════════
  EPUB PREPARATION REPORT - The Artisan's Path
═══════════════════════════════════════════════════════

✅ Phase 1: Pre-Flight Checks
   - Directory structure: VALID
   - Required files: ALL PRESENT
   - Assets: 31 images, 6 fonts, stylesheets OK

✅ Phase 2: XHTML Formatting & Linting
   - Files validated: 46 XHTML files
   - Errors found: 0
   - Warnings: 0
   - Auto-fixes applied: 0

✅ Phase 3: Content Verification
   - Chapters: 16/16 present
   - Frontmatter: 7/7 present
   - Backmatter: 17/17 present
   - Internal links: ALL VALID

✅ Phase 4: Package Validation
   - content.opf: VALID
   - Manifest entries: 46 files
   - Spine order: CORRECT
   - Metadata: COMPLETE

✅ Phase 5: Standards Compliance
   - EPUB 3.0: COMPLIANT
   - Accessibility: LEVEL AA
   - Validation: PASSED

✅ Phase 6: Build & Final Validation
   - Build: SUCCESS
   - File: The-Artisans-Path.epub (5.8 MB)
   - epubcheck: PASSED
   - Status: READY FOR DISTRIBUTION

═══════════════════════════════════════════════════════
✅ EPUB IS PRODUCTION-READY
═══════════════════════════════════════════════════════
```

## Success Criteria

The EPUB is ready for distribution when:
- ✅ Zero critical errors
- ✅ All validation checks pass
- ✅ EPUB 3.0 compliant
- ✅ Accessible (WCAG Level AA)
- ✅ All content present and correct
- ✅ epubcheck validation passes
- ✅ File size within expected range
- ✅ Can be opened in standard ebook readers

## Next Steps After Preparation

Once preparation is complete:
1. Test EPUB in multiple readers (Calibre, Apple Books, Adobe Digital Editions)
2. Distribute to platforms (Amazon KDP, Apple Books, Google Play Books, etc.)
3. Archive source files
4. Create backup of validated EPUB

## Troubleshooting

If any phase fails:
1. Review the detailed error messages
2. Fix issues in source files
3. Re-run validation
4. Continue from the failed phase
5. Do not proceed to build until all validations pass
