# AGENTS.md - EPUB ACISS Design Implementation

## MISSION STATEMENT
You are an EPUB specialist agent tasked with implementing the ACISS design system across 44 XHTML files for "Unveiling Your Creative Odyssey" while maintaining **100% CONTENT FIDELITY**. Every single word must be preserved exactly as written in the original files.

## PROJECT OVERVIEW
- **Book Title**: Unveiling Your Creative Odyssey
- **Total Files**: 44 XHTML files
- **Input Directory**: `input/OEBPS/text/`
- **Output Directory**: `output/OEBPS/text/`
- **Design System**: ACISS with teal color scheme (#4ECDC4)

## CRITICAL RULES - NEVER VIOLATE

### 🚨 ABSOLUTE CONTENT PRESERVATION
- **NO WORD CHANGES**: Not a single word can be modified from original
- **NO TRUNCATION**: Complete content from start to finish
- **NO SUMMARIZATION**: Full text must be preserved
- **NO GENERATION**: Do not create or add content not in original
- **ALL FOOTNOTES**: Every reference and citation maintained exactly
- **ALL CASE STUDIES**: Personal stories preserved word-for-word
- **ALL IMPLEMENTATION STEPS**: Action items kept intact

### ✅ VERIFICATION CHECKPOINTS
Before completing each file:
1. Word count must match original exactly
2. All footnotes and references present
3. All case studies and examples included
4. All implementation steps preserved
5. No content truncated or omitted

## FILE STRUCTURE ANALYSIS

### FRONTMATTER (7 files)
- Standard pages: title, copyright, dedication, table of contents
- **2 Activity Worksheets**: Keep interactive elements as static HTML
- Apply basic ACISS styling, preserve all content

### MAIN CONTENT (20 files)
#### CHAPTERS (16 files) - 6 Pages Each:
1. **Title Page**: Roman numeral, title stack, Bible quote, introduction
2. **Body Pages (2-4)**: All original content with proper headings
3. **Endnotes Page**: All footnotes and references
4. **Quiz & Worksheet**: Maximum 4 questions, worksheet elements

#### PART DIVIDERS (4 files):
- Clean structure, preserve descriptive content
- Fix CSS references, standardize formatting

### BACKMATTER (17 files)
- Regular backmatter: author bio, resources, etc.
- **Activity Worksheet Journals**: Keep as static HTML
- Preserve all content, apply consistent styling

## CHAPTER STRUCTURE TEMPLATE

### Page 1: Title Page
```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
    <meta charset="utf-8"/>
    <title>Chapter [ROMAN] - [EXACT_TITLE]</title>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <link rel="stylesheet" type="text/css" href="../styles/fonts.css"/>
    <link rel="stylesheet" type="text/css" href="../styles/style.css"/>
</head>
<body class="chapter-page">
    <div class="chap-title">
        <!-- Chapter Number with Brushstroke -->
        <div class="chapter-number-container">
            <div class="chapter-number-brush">
                <img src="../images/brushstroke.svg" alt="" class="brushstroke-img"/>
                <div class="chapter-number-text">[ROMAN_NUMERAL]</div>
            </div>
        </div>
        
        <!-- Chapter Title Stack -->
        <div class="chapter-title-container">
            <div class="title-stack">
                <div class="title-bar"></div>
                <div class="title-lines">
                    <!-- Break title into 3-6 lines -->
                    <div class="title-line">[WORD1]</div>
                    <div class="title-line">[WORD2]</div>
                    <!-- Continue for each word -->
                </div>
            </div>
        </div>
        
        <!-- Bible Quote -->
        <div class="bible-quote-container">
            <div class="bible-quote-text">[EXACT_BIBLE_QUOTE]</div>
            <div class="bible-quote-reference">— [BIBLE_REFERENCE]</div>
        </div>
        
        <!-- Introduction -->
        <div class="introduction-heading">INTRODUCTION</div>
        <p><span class="dropcap-first-letter">[FIRST_LETTER]</span>[REST_OF_FIRST_PARAGRAPH_EXACT]</p>
    </div>
</body>
</html>
```

### Pages 2-4: Body Content
```xml
<!-- PAGE BREAK -->
<div class="page-break"></div>

<div class="chap-body">
    <h2 class="section-heading">[ORIGINAL_HEADING]</h2>
    <p>[ORIGINAL_CONTENT_WORD_FOR_WORD]</p>
    <!-- All original content preserved exactly -->
</div>
```

### Page 5: Endnotes
```xml
<!-- PAGE BREAK -->
<div class="page-break"></div>

<div class="endnotes">
    <h2 class="endnotes-title">ENDNOTES</h2>
    <div class="footnote">
        <span class="footnote-number">[1]</span>
        <span class="footnote-text">[EXACT_FOOTNOTE_TEXT]</span>
    </div>
    <!-- All footnotes preserved exactly -->
</div>
```

### Page 6: Quiz & Worksheet
```xml
<!-- PAGE BREAK -->
<div class="page-break"></div>

<div class="quiz-container">
    <h2 class="quiz-title">REFLECTION QUIZ</h2>
    <div class="quiz-question">
        <div class="question-text">[QUESTION_TEXT]</div>
        <div class="quiz-options">
            <div class="option">A) [OPTION_A]</div>
            <div class="option">B) [OPTION_B]</div>
            <div class="option">C) [OPTION_C]</div>
            <div class="option">D) [OPTION_D]</div>
        </div>
    </div>
    <!-- Maximum 4 questions -->
</div>

<div class="worksheet">
    <div class="worksheet-item">
        <div class="worksheet-prompt">[PROMPT_TEXT]</div>
        <div class="worksheet-space"></div>
    </div>
    <!-- Worksheet elements -->
</div>

<!-- Closing -->
<div class="closing">
    <div class="closing-image-container">
        <img src="../images/closing-ornament.png" alt="" class="closing-image"/>
    </div>
</div>
```

## ROMAN NUMERAL CONVERSION
```
1=I, 2=II, 3=III, 4=IV, 5=V, 6=VI, 7=VII, 8=VIII
9=IX, 10=X, 11=XI, 12=XII, 13=XIII, 14=XIV, 15=XV, 16=XVI
```

## TITLE BREAKING RULES
Break chapter titles into vertical lines:
- Maximum 6 lines
- Break at natural word boundaries
- Each line gets `<div class="title-line">[WORD]</div>`

**Examples:**
- "UNVEILING YOUR CREATIVE ODYSSEY" → 4 lines
- "MASTERING THE BUSINESS OF HAIRSTYLING" → 5 lines
- "THE ART OF NETWORKING IN FREELANCE HAIRSTYLING" → 6 lines

## CSS CLASSES REFERENCE

### Required Classes (Use Exactly):
```css
/* Title Page */
.chap-title, .chapter-number-container, .chapter-number-brush
.brushstroke-img, .chapter-number-text, .chapter-title-container
.title-stack, .title-bar, .title-lines, .title-line
.bible-quote-container, .bible-quote-text, .bible-quote-reference
.introduction-heading, .dropcap-first-letter

/* Body Content */
.chap-body, .section-heading, .page-break

/* Endnotes */
.endnotes, .endnotes-title, .footnote, .footnote-number, .footnote-text

/* Quiz & Worksheet */
.quiz-container, .quiz-title, .quiz-question, .question-text
.quiz-options, .option, .worksheet, .worksheet-item
.worksheet-prompt, .worksheet-space

/* Closing */
.closing, .closing-image-container, .closing-image
```

## CHAPTER INFORMATION EXTRACTION

### For Each Chapter File:
1. **Find Chapter Number**: Extract from filename or content
2. **Extract Title**: Get exact chapter title (after "Chapter X:")
3. **Locate Bible Quote**: Find scripture verse and reference
4. **Get Introduction**: First paragraph after title/quote
5. **Preserve All Content**: Every word, footnote, case study

### Example Chapter Mapping:
```
File: 9-chapter-i-unveiling-your-creative-odyssey.xhtml
- Number: I (Roman numeral)
- Title: "UNVEILING YOUR CREATIVE ODYSSEY"
- Bible Quote: "For we are God's handiwork, created in Christ Jesus..."
- Reference: "Ephesians 2:10"
```

## PROCESSING WORKFLOW

### For Each File:
1. **Read Complete Original**: Load entire XHTML file
2. **Extract All Content**: Identify every content element
3. **Parse Chapter Info**: Get number, title, quote, etc.
4. **Apply ACISS Structure**: Use exact template above
5. **Preserve Content 100%**: Insert all original text exactly
6. **Validate Structure**: Check XHTML compliance
7. **Verify Content**: Confirm nothing lost or changed

### Quality Checks:
- [ ] File structure matches template exactly
- [ ] All CSS classes applied correctly
- [ ] Roman numerals converted properly
- [ ] Titles broken into lines correctly
- [ ] Bible quotes formatted in containers
- [ ] All original content preserved word-for-word
- [ ] Page breaks inserted between sections
- [ ] XHTML validates without errors

## FILE NAMING CONVENTION
Keep original filenames exactly:
- `9-chapter-i-unveiling-your-creative-odyssey.xhtml`
- `10-chapter-ii-refining-your-creative-toolkit.xhtml`
- etc.

## ERROR PREVENTION

### NEVER DO:
❌ Change any words from original content
❌ Omit footnotes, references, or citations
❌ Summarize or shorten any content
❌ Add content not in original file
❌ Use wrong CSS class names
❌ Miss page breaks between sections
❌ Break XHTML validation rules

### ALWAYS DO:
✅ Preserve every single word exactly
✅ Include all footnotes and references
✅ Apply ACISS structure consistently
✅ Use correct CSS classes
✅ Insert proper page breaks
✅ Validate XHTML compliance
✅ Double-check content accuracy

## EXECUTION COMMAND

When ready to process all files, use this approach:

1. **Process Frontmatter (7 files)**: Apply basic ACISS styling
2. **Process Part Dividers (4 files)**: Clean and standardize
3. **Process Chapters (16 files)**: Full 6-page ACISS implementation
4. **Process Backmatter (17 files)**: Consistent styling

## FINAL VALIDATION

Before completing project:
- [ ] All 44 files processed successfully
- [ ] Every file validates as XHTML 1.1
- [ ] Content accuracy verified at 100%
- [ ] ACISS design applied consistently
- [ ] Cross-device compatibility ensured
- [ ] EPUB 3.0 compliance confirmed

## BESTSELLER-QUALITY REQUIREMENTS

### SEO METADATA (REQUIRED)
Update package.opf with comprehensive metadata:
```xml
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:title>Unveiling Your Creative Odyssey: A Christian Journey Through Hairstyling Excellence</dc:title>
    <dc:creator>Your Author Name</dc:creator>
    <dc:description>A comprehensive guide for Christian hairstylists combining faith, creativity, and business excellence in the beauty industry. Learn to transform your passion into a thriving career while maintaining your Christian values.</dc:description>
    <dc:subject>Hairstyling</dc:subject>
    <dc:subject>Christian Living</dc:subject>
    <dc:subject>Beauty Industry</dc:subject>
    <dc:subject>Entrepreneurship</dc:subject>
    <dc:subject>Creative Arts</dc:subject>
    <dc:subject>Business Development</dc:subject>
    <dc:subject>Professional Development</dc:subject>
    <dc:subject>Faith and Work</dc:subject>
    <dc:language>en</dc:language>
    <dc:date>2025</dc:date>
    <dc:rights>All rights reserved</dc:rights>
    <dc:publisher>Your Publisher Name</dc:publisher>
    <meta property="dcterms:modified">2025-09-16T12:00:00Z</meta>
    <meta name="cover" content="cover-image"/>
</metadata>
```

### ACCESSIBILITY REQUIREMENTS (MANDATORY)
Every processed file MUST include:

**Alt Text for ALL Images:**
```xml
<!-- Decorative images -->
<img src="../images/brushstroke.svg" alt="Decorative teal brushstroke background" class="brushstroke-img"/>
<img src="../images/closing-ornament.png" alt="Decorative chapter closing ornament" class="closing-image"/>

<!-- Content images -->
<img src="../images/hairstyle-example.jpg" alt="Professional bob haircut with copper highlights showcasing layered styling technique" class="content-image"/>
```

**Semantic HTML Structure:**
```xml
<!-- Proper heading hierarchy -->
<h1 class="chapter-title">Chapter Title</h1>
<h2 class="section-heading">Main Section</h2>
<h3 class="subsection-heading">Subsection</h3>

<!-- Semantic roles -->
<div class="bible-quote-container" role="blockquote" aria-label="Bible verse">
<div class="quiz-container" role="region" aria-label="Chapter quiz">
<div class="worksheet" role="region" aria-label="Worksheet activities">

<!-- Screen reader support -->
<span class="dropcap-first-letter" aria-hidden="true">P</span>
<span class="sr-only">Picture</span>
```

**ARIA Labels and Landmarks:**
```xml
<!-- Navigation landmarks -->
<nav role="navigation" aria-label="Chapter navigation">
<main role="main" aria-label="Chapter content">
<aside role="complementary" aria-label="Additional resources">

<!-- Interactive elements -->
<div class="quiz-question" role="group" aria-labelledby="question-1">
<div id="question-1" class="question-text">Question text here</div>
```

### IMAGE OPTIMIZATION (REQUIRED)
Optimize ALL images for fast loading:

**SVG Optimization:**
- Remove unnecessary metadata
- Minimize path complexity
- Use efficient gradients
- Compress without quality loss

**Raster Image Optimization:**
- JPEG: 85% quality, progressive encoding
- PNG: 8-bit when possible, optimize transparency
- Maximum width: 1200px for full-width images
- Use appropriate compression ratios

**Image Implementation:**
```xml
<!-- Responsive images with proper sizing -->
<img src="../images/optimized-image.jpg" 
     alt="Descriptive alt text for screen readers" 
     style="max-width: 100%; height: auto;"
     loading="lazy"
     class="content-image"/>
```

## SUCCESS CRITERIA
- **Zero content changes** from original files
- **Professional ACISS design** implementation
- **EPUB 3.0 compliance** for all devices
- **Bestseller-quality SEO metadata** implemented
- **Full accessibility compliance** achieved
- **Optimized performance** for fast loading
- **100% content fidelity** maintained throughout

## ACCESSIBILITY CHECKLIST
Before completing each file, verify:
- [ ] All images have descriptive alt text
- [ ] Proper heading hierarchy maintained
- [ ] ARIA labels added to interactive elements
- [ ] Semantic HTML structure used throughout
- [ ] Screen reader compatibility ensured
- [ ] Color contrast meets WCAG standards
- [ ] Text is readable without images

## SEO OPTIMIZATION CHECKLIST
- [ ] Comprehensive metadata in package.opf
- [ ] Descriptive chapter titles in `<title>` tags
- [ ] Relevant keywords in descriptions
- [ ] Proper language declarations
- [ ] Publisher and copyright information complete
- [ ] Publication date properly formatted

Remember: This project demands absolute precision AND professional publishing standards. Every word matters, every design element matters, every accessibility feature matters, and every SEO element matters. Do not compromise on any requirement.