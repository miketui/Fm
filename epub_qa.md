# EPUB Project Q&A Guide
## "Unveiling Your Creative Odyssey" - Comprehensive Troubleshooting

### General Questions

**Q: Why does my EPUB fail to open on iPhone/iPad?**
A: Common causes and solutions:
- **Corrupted mimetype**: Ensure `mimetype` file contains exactly `application/epub+zip` with no newline
- **Invalid XHTML**: Run validation with `./tools/validate.sh`
- **Missing CSS references**: Check paths are `../styles/style.css` not absolute paths
- **Broken package.opf**: Verify all file references in manifest match actual files

**Q: How do I ensure 100% content preservation?**
A: Follow these verification steps:
1. Count words in original vs processed files
2. Compare footnote counts exactly
3. Verify all case studies are complete
4. Check that no implementation steps are missing
5. Use diff tools to compare content sections

**Q: What if Codex truncates content?**
A: Immediately stop and:
```bash
@agents CRITICAL: Content truncation detected. 
Please process this file again with complete original content.
Show me the full word count comparison.
```

### ACISS Design Implementation

**Q: How do I handle long chapter titles?**
A: Break titles into vertical lines following these rules:
- Maximum 6 lines
- Break at natural word boundaries
- Each word becomes a separate `<div class="title-line">`

Examples:
```xml
<!-- "THE ART OF NETWORKING IN FREELANCE HAIRSTYLING" -->
<div class="title-line">THE</div>
<div class="title-line">ART</div>
<div class="title-line">OF</div>
<div class="title-line">NETWORKING</div>
<div class="title-line">IN</div>
<div class="title-line">FREELANCE</div>
<div class="title-line">HAIRSTYLING</div>
```

**Q: What if the brushstroke image doesn't display?**
A: Check these elements:
1. File exists at `OEBPS/images/brushstroke.svg`
2. CSS references correct path: `../images/brushstroke.svg`
3. Image is included in package.opf manifest
4. SVG markup is valid XML

**Q: How do I handle Bible quotes formatting?**
A: Use this exact structure:
```xml
<div class="bible-quote-container">
    <div class="bible-quote-text">For we are God's handiwork, created in Christ Jesus to do good works, which God prepared in advance for us to do.</div>
    <div class="bible-quote-reference">— Ephesians 2:10</div>
</div>
```

### File Structure Issues

**Q: What if I have more or fewer than 44 files?**
A: Verify your EPUB structure:
- **Expected**: 7 frontmatter + 20 main content + 17 backmatter = 44 total
- Run `./tools/check-files.sh` to count actual files
- Check if any files were accidentally excluded during extraction

**Q: How do I identify which files are worksheets?**
A: Look for these indicators:
- Filename contains "worksheet", "activity", or "journal"
- Content includes fill-in-the-blank sections
- Interactive elements like checkboxes or form fields
- Convert interactive elements to static HTML for EPUB compatibility

**Q: What about part divider pages?**
A: Process these 4 files with simplified structure:
- `8-Part-I-Foundations-of-Creative-Hairstyling.xhtml`
- `12-Part-II-Building-Your-Professional-Practice.xhtml`
- `18-Part-III-Advanced-Business-Strategies.xhtml`
- `24-Part-IV-Future-Focused-Growth.xhtml`

Apply basic ACISS styling but maintain their descriptive content exactly.

### Technical Validation

**Q: How do I fix XHTML validation errors?**
A: Common fixes:
```xml
<!-- Ensure proper DOCTYPE -->
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>

<!-- Correct namespace -->
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<!-- Close all tags properly -->
<img src="../images/brushstroke.svg" alt="" />
<div class="page-break"></div>

<!-- Use proper meta tags -->
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
```

**Q: What CSS classes are absolutely required?**
A: Every chapter must use these exact classes:
```css
/* Title Page - Required */
.chap-title
.chapter-number-container
.chapter-number-brush
.brushstroke-img
.chapter-number-text
.chapter-title-container
.title-stack
.title-bar
.title-lines
.title-line
.bible-quote-container
.bible-quote-text
.bible-quote-reference
.introduction-heading
.dropcap-first-letter

/* Content Pages - Required */
.chap-body
.section-heading
.page-break

/* Endnotes - Required */
.endnotes
.endnotes-title
.footnote
.footnote-number
.footnote-text
```

**Q: Why doesn't my EPUB pass EPUBCheck validation?**
A: Common issues:
1. **Missing files**: Check all files in package.opf manifest exist
2. **Invalid paths**: Use relative paths without leading slashes
3. **Broken navigation**: Ensure nav.xhtml references are correct
4. **Metadata errors**: Validate package.opf structure

### Content-Specific Issues

**Q: How do I preserve footnotes correctly?**
A: Use this structure for each footnote:
```xml
<div class="footnote">
    <span class="footnote-number">1</span>
    <span class="footnote-text">Exact original footnote text preserved word-for-word without any modifications or summarization.</span>
</div>
```

**Q: What about case studies and personal stories?**
A: These must be preserved exactly:
- Keep all names, dates, and specific details
- Maintain original formatting and paragraph structure
- Include all dialogue and quotes verbatim
- Preserve any implementation steps or lessons learned

**Q: How do I handle the quiz sections?**
A: Create maximum 4 questions per chapter:
```xml
<div class="quiz-container">
    <h2 class="quiz-title">REFLECTION QUIZ</h2>
    <div class="quiz-question">
        <div class="question-text">What is the primary purpose of creative expression in hairstyling?</div>
        <div class="quiz-options">
            <div class="option">A) To show technical skill</div>
            <div class="option">B) To express personal artistry</div>
            <div class="option">C) To build client relationships</div>
            <div class="option">D) All of the above</div>
        </div>
    </div>
</div>
```

### Device Compatibility

**Q: Why does my EPUB look different on different devices?**
A: Ensure consistent rendering:
- Use relative font sizes (em, rem) not fixed pixels
- Test CSS properties across different readers
- Avoid device-specific CSS that may not be supported
- Use web-safe fonts with proper fallbacks

**Q: How do I optimize for mobile reading?**
A: Mobile-first considerations:
- Ensure text is readable without zooming
- Use appropriate line spacing and margins
- Test chapter navigation on small screens
- Verify images scale properly

**Q: What about accessibility?**
A: Include proper accessibility features:
```xml
<!-- Alt text for images -->
<img src="../images/brushstroke.svg" alt="Decorative brushstroke background" />

<!-- Proper heading hierarchy -->
<h1>Chapter Title</h1>
<h2 class="section-heading">Section Title</h2>

<!-- Semantic markup -->
<div class="bible-quote-container" role="blockquote">
```

### Advanced Troubleshooting

**Q: My EPUB file is too large - how do I optimize it?**
A: Optimization strategies:
1. **Compress images**: Use web-optimized formats
2. **Minify CSS**: Remove unnecessary whitespace
3. **Optimize SVG**: Remove unused elements
4. **Clean HTML**: Remove empty tags and comments

**Q: How do I debug CSS issues?**
A: Systematic debugging:
1. Test CSS in browser first
2. Validate CSS syntax
3. Check class name spelling exactly
4. Verify file paths are correct
5. Test one style rule at a time

**Q: What if chapters don't display the 6-page structure?**
A: Verify page break implementation:
```xml
<!-- Insert between each page section -->
<div class="page-break"></div>
```

Check CSS includes:
```css
.page-break {
    page-break-before: always;
    break-before: page;
}
```

### Quality Assurance

**Q: How do I verify content accuracy?**
A: Use these verification methods:
1. **Word count comparison**: Original vs processed files
2. **Footnote audit**: Count and compare all references
3. **Case study review**: Ensure all examples are complete
4. **Implementation check**: Verify all action items preserved

**Q: What constitutes "ready for publication"?**
A: Final checklist:
- [ ] All 44 files processed without errors
- [ ] 100% content fidelity verified
- [ ] XHTML validation passed for all files
- [ ] EPUBCheck validation successful
- [ ] Cross-device testing completed
- [ ] Professional design standards met
- [ ] SEO metadata properly configured
- [ ] Table of contents functional
- [ ] Navigation working correctly

### Emergency Procedures

**Q: What if I accidentally delete or corrupt files?**
A: Recovery process:
1. Stop all work immediately
2. Restore from backup: `cp -r backups/original-*/ input/`
3. Verify backup integrity
4. Restart processing from last good checkpoint

**Q: How do I rollback to a previous version?**
A: Version control steps:
```bash
# List available backups
ls -la backups/

# Restore specific backup
cp -r backups/checkpoint-YYYYMMDD-HHMMSS/ input/

# Verify restoration
./tools/check-files.sh
```

**Q: What if EPUBCheck fails with critical errors?**
A: Critical error resolution:
1. **Parse error log**: Identify specific file and line
2. **Fix XHTML issues**: Correct malformed markup
3. **Validate individually**: Test each file separately
4. **Rebuild package**: Recreate package.opf if needed

### Performance Optimization

**Q: How can I speed up the processing workflow?**
A: Efficiency improvements:
1. **Process in batches**: Handle similar files together
2. **Use templates**: Create standardized structures
3. **Automate validation**: Script repetitive checks
4. **Parallel processing**: Work on multiple files simultaneously

**Q: What tools can help with quality assurance?**
A: Recommended tools:
- **EPUBCheck**: Official EPUB validation
- **HTML Validator**: W3C markup validation
- **Diff tools**: Content comparison utilities
- **EPUB readers**: Multi-platform testing
- **Text editors**: Advanced find/replace capabilities

This Q&A covers the most common issues you'll encounter. Always prioritize content preservation above all other considerations.