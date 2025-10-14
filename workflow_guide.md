# Complete EPUB Workflow Guide
## "Unveiling Your Creative Odyssey" - ACISS Design Implementation

### Phase 1: Environment Setup

#### Step 1: Initial Setup
1. **Download and run setup script**:
   ```bash
   chmod +x codex_setup.sh
   ./codex_setup.sh
   ```

2. **Place your current EPUB file** in the `epub-project/` directory

3. **Extract EPUB for editing**:
   ```bash
   cd epub-project
   ./tools/unzip-epub.sh your-book.epub
   ```

4. **Verify file structure**:
   ```bash
   ./tools/check-files.sh
   ```

#### Step 2: Backup Original Files
```bash
cp -r /workspace/Fm/OEBPS/text \
      "/workspace/Fm/backups/original-$(date +%Y%m%d-%H%M%S)/"
```

#### Step 3: Add Brushstroke Image
1. Save the generated SVG brushstroke as `/workspace/Fm/OEBPS/images/brushstroke.svg`
2. Update any existing brushstroke references in CSS

### Phase 2: File Analysis and Preparation

#### Step 4: Analyze Current Structure
```bash
find /workspace/Fm/OEBPS/text -name "*.xhtml" | sort > file-list.txt
```

Expected structure:
- **Frontmatter (7 files)**: `1-*` through `7-*`
- **Main Content (20 files)**: `8-*` through `27-*`
- **Backmatter (17 files)**: `28-*` through `44-*`

#### Step 5: Content Inventory
For each file type, document:
- File name and purpose
- Current word count
- Special elements (footnotes, worksheets, etc.)
- Bible quotes and references
- Case studies and examples

### Phase 3: Codex Processing

#### Step 6: Prepare Codex Environment
1. **Place AGENTS.md** in the `epub-project/` root directory

2. **Start Codex** with the project directory:
   ```bash
   codex --project epub-project/
   ```

3. **Initial Codex Commands**:
   ```
   @agents Read the AGENTS.md file and understand the mission
   @agents Analyze the /workspace/Fm/OEBPS/text directory structure
   @agents Create a processing plan for all 45 files (including nav.xhtml)
   ```

#### Step 7: Process Files in Order

**Phase 3A: Frontmatter Processing**
```
@agents Process frontmatter files (1-* through 7-*):
- Apply basic ACISS styling
- Preserve all content word-for-word
- Handle 2 activity worksheets as static HTML
- Ensure proper XHTML structure
```

**Phase 3B: Part Divider Processing**
```
@agents Process part divider files (8, 12, 18, 24):
- Clean CSS link references
- Standardize HTML formatting
- Preserve all descriptive content
- Apply consistent styling
```

**Phase 3C: Chapter Processing**
```
@agents Process chapter files (9-11, 13-17, 19-23, 25-27):
- Implement full ACISS design system
- Create 6-page structure per chapter
- Extract and convert chapter numbers to Roman numerals
- Break titles into vertical stacks
- Preserve Bible quotes with proper styling
- Maintain 100% content fidelity
- Apply all required CSS classes
```

**Phase 3D: Backmatter Processing**
```
@agents Process backmatter files (28-* through 44-*):
- Apply consistent ACISS styling
- Handle activity worksheet journals as static HTML
- Preserve all content exactly
- Ensure proper cross-references
```

#### Step 8: Quality Validation

**Content Verification**:
```
@agents For each processed file:
- Verify word count matches original exactly
- Confirm all footnotes and references preserved
- Check all case studies and examples included
- Validate all implementation steps maintained
- Ensure no content truncated or generated
```

**Technical Validation**:
```
./tools/validate.sh
```

### Phase 4: Testing and Refinement

#### Step 9: Device Compatibility Testing

**Create test EPUB**:
```bash
./tools/compile.sh
```

**Test on multiple platforms**:
- iPhone Books app
- iPad Books app
- Android readers
- Web browsers
- Desktop EPUB readers

#### Step 10: Issue Resolution

**Common Issues and Fixes**:

1. **CSS Not Loading**:
   - Verify relative paths: `../styles/style.css`
   - Check file existence in output directory
   - Validate CSS syntax

2. **Images Missing**:
   - Confirm `brushstroke.svg` in `/workspace/Fm/output/OEBPS/images/`
   - Check image paths in XHTML: `../images/brushstroke.svg`
   - Validate image file format

3. **XHTML Validation Errors**:
   - Fix DOCTYPE declarations
   - Close all HTML tags properly
   - Ensure proper XML namespace

4. **Content Truncation**:
   - Compare word counts with originals
   - Check for missing sections
   - Verify complete footnote preservation

### Phase 5: Final Production

#### Step 11: Final Quality Assurance

**Complete Checklist**:
- [ ] All 45 files processed successfully
- [ ] 100% content fidelity maintained
- [ ] ACISS design implemented consistently
- [ ] All CSS classes applied correctly
- [ ] Roman numerals converted properly
- [ ] Bible quotes formatted correctly
- [ ] Page breaks inserted appropriately
- [ ] XHTML 1.1 validation passed
- [ ] EPUB 3.0 compliance confirmed
- [ ] Cross-device compatibility tested

#### Step 12: SEO and Metadata Enhancement

**Update package.opf**:
```xml
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:title>Unveiling Your Creative Odyssey: A Christian Journey Through Hairstyling Excellence</dc:title>
    <dc:creator>Your Author Name</dc:creator>
    <dc:description>A comprehensive guide for Christian hairstylists combining faith, creativity, and business excellence in the beauty industry.</dc:description>
    <dc:subject>Hairstyling</dc:subject>
    <dc:subject>Christian Living</dc:subject>
    <dc:subject>Beauty Industry</dc:subject>
    <dc:subject>Entrepreneurship</dc:subject>
    <dc:subject>Creative Arts</dc:subject>
    <dc:language>en</dc:language>
    <dc:date>2025</dc:date>
    <meta property="dcterms:modified">2025-09-16T12:00:00Z</meta>
</metadata>
```

#### Step 13: Final Compilation

```bash
# Create final production EPUB
./tools/compile.sh

# Validate final product
java -jar tools/epubcheck/epubcheck.jar book.epub

# Create distribution copy
cp book.epub "Unveiling-Your-Creative-Odyssey-FINAL.epub"
```

### Phase 6: Distribution Preparation

#### Step 14: Multi-Platform Testing

Test final EPUB on:
- **iOS**: iPhone/iPad Books app
- **Android**: Google Play Books, Adobe Digital Editions
- **Desktop**: Calibre, Adobe Digital Editions
- **Web**: EPUB.js readers

#### Step 15: Performance Optimization

**File Size Optimization**:
- Compress images if needed
- Optimize CSS for faster loading
- Remove unnecessary whitespace

**Reading Experience**:
- Test font rendering across devices
- Verify proper page breaks
- Check navigation functionality
- Validate table of contents

### Troubleshooting Guide

#### Common Codex Issues

**If Codex truncates content**:
```
@agents STOP. Content preservation is critical. 
Please ensure complete original content is maintained.
Show me word count comparison for the last processed file.
```

**If styling doesn't apply**:
```
@agents Check CSS class names against the AGENTS.md specification.
Verify all required classes are used exactly as specified.
```

**If XHTML validation fails**:
```
@agents Fix XHTML structure issues:
- Ensure proper DOCTYPE declaration
- Close all tags properly
- Use correct XML namespaces
```

### Success Metrics

#### Content Quality (100% Required)
- ✅ Every word preserved from original
- ✅ All footnotes and references intact
- ✅ Complete case studies included
- ✅ Full implementation guidance maintained

#### Technical Quality (100% Required)
- ✅ Valid XHTML 1.1 structure
- ✅ EPUB 3.0 compliance
- ✅ Proper CSS implementation
- ✅ Cross-device compatibility

#### Design Quality (Professional Standard)
- ✅ Consistent ACISS implementation
- ✅ Professional typography
- ✅ Proper chapter structure (6 pages each)
- ✅ Bestseller-quality presentation

### Emergency Procedures

#### If Content is Lost or Modified
1. Stop all processing immediately
2. Restore from backup: `rsync -av "/workspace/Fm/backups/original-*/" /workspace/Fm/OEBPS/text/`
3. Re-run Codex with stricter content preservation instructions
4. Verify word-for-word accuracy before proceeding

#### If EPUB Won't Open on Devices
1. Run full validation: `./tools/validate.sh`
2. Check mimetype file: `cat /workspace/Fm/output/mimetype`
3. Verify package.opf structure
4. Test with EPUBCheck: `java -jar tools/epubcheck/epubcheck.jar book.epub`

### Final Delivery

The completed EPUB should:
- Open flawlessly on all major platforms
- Display beautifully with ACISS design system
- Maintain 100% original content fidelity
- Meet bestseller-quality standards
- Be ready for immediate publication

This workflow ensures professional results while maintaining absolute content integrity throughout the entire process.