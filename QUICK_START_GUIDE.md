# Quick Start Guide: Using EPUB XHTML Templates

This guide provides step-by-step instructions for using the ACISS layout system templates to create EPUB content.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Quick Reference](#quick-reference)
3. [Creating a Chapter](#creating-a-chapter)
4. [Creating Frontmatter](#creating-frontmatter)
5. [Creating Backmatter](#creating-backmatter)
6. [Common Patterns](#common-patterns)
7. [Troubleshooting](#troubleshooting)

## Prerequisites

Before you begin:
- [x] Read `EPUB_FORMATTING_HANDOFF.md` for complete specifications
- [x] Review `templates/README.md` for detailed usage guidelines
- [x] Ensure you have access to the stylesheet files in `OEBPS/styles/`
- [x] Have your source content ready (text, images, references)

## Quick Reference

### File Naming Convention
```
Frontmatter:    1-7   (e.g., 1-TitlePage.xhtml, 2-Copyright.xhtml)
Part Dividers:  8, 12, 18, 24
Chapters:       9-27  (e.g., 9-chapter-i-title.xhtml)
Backmatter:     28-44 (e.g., 28-Conclusion.xhtml)
Navigation:     nav.xhtml
```

### Body Class Mapping
```
Files 1-7:      <body class="frontmatter-page">
Files 8,12,18,24: <body class="part-page">
Files 9-27:     <body class="chapter-page">
Files 28-44:    <body class="backmatter-page">
```

### Template Selection
```
Need frontmatter?  → templates/frontmatter-template.xhtml
Need part divider? → templates/part-divider-template.xhtml
Need chapter?      → templates/chapter-template.xhtml
Need backmatter?   → templates/backmatter-template.xhtml
```

## Creating a Chapter

### Step 1: Copy Template
```bash
cp templates/chapter-template.xhtml OEBPS/text/XX-chapter-title.xhtml
```

### Step 2: Update Metadata
Open the file and update:
```xml
<title>Chapter I – Your Chapter Title</title>
```

### Step 3: Customize Section 1 (Title Page)

**Update chapter number:**
```xml
<figcaption class="chapter-number-roman">I</figcaption>
<!-- Change to: II, III, IV, V, VI, VII, VIII, IX, X, XI, XII, XIII, XIV, XV, XVI -->
```

**Update title (one word per line):**
```xml
<div class="title-lines">
  <div class="title-line">Your</div>
  <div class="title-line">Chapter</div>
  <div class="title-line">Title</div>
</div>
```

**Add or remove Bible quote:**
```xml
<!-- If no quote, remove entire <figure class="bible-quote-container"> block -->
<!-- If quote exists, update text and reference -->
<blockquote class="bible-quote-text" id="bq-text">
  "Your scripture quote here."
</blockquote>
<figcaption class="bible-quote-reference" id="bq-ref">— Reference</figcaption>
```

**Update introduction (keep drop cap):**
```xml
<div class="introduction-paragraph dropcap-first-letter">
  <p><strong>P</strong>icture yourself... [your introduction text]</p>
  <p>Additional introduction paragraphs...</p>
</div>
```

### Step 4: Add Section 2 (Body Content)

Replace placeholder content with your chapter text:
```xml
<section class="chap-body" role="region" aria-label="Chapter content">
  <div class="content-area">
    <h2>Your Main Section Heading</h2>
    <p>Your content here...</p>
    
    <h3>Subsection Heading</h3>
    <p>More content...</p>
    
    <!-- Add footnote references like this: -->
    <p>Text with citation.<sup id="fnref-1"><a href="#fn-1">1</a></sup></p>
  </div>
</section>
```

### Step 5: Update Section 3 (Endnotes)

**If you have endnotes:**
```xml
<section class="endnotes" role="region" aria-label="Endnotes">
  <h2 class="endnotes-title">Endnotes</h2>
  <ol>
    <li id="fn-1">
      <p>Your citation here...</p>
    </li>
    <!-- Add more as needed -->
  </ol>
</section>
```

**If no endnotes:**
```xml
<!-- Remove entire <section class="endnotes"> block -->
```

### Step 6: Customize Section 4 (Quiz)

Update 4 questions (keep A-D structure):
```xml
<div class="quiz-question-block">
  <p class="quiz-question"><strong>1. Your question here?</strong></p>
  <ul class="quiz-options">
    <li class="quiz-option"><span class="opt-label">A)</span> Answer option A</li>
    <li class="quiz-option"><span class="opt-label">B)</span> Answer option B</li>
    <li class="quiz-option"><span class="opt-label">C)</span> Answer option C</li>
    <li class="quiz-option"><span class="opt-label">D)</span> Answer option D</li>
  </ul>
</div>
<!-- Repeat for questions 2, 3, 4 -->
```

### Step 7: Customize Section 5 (Worksheet)

Update reflection questions:
```xml
<section class="worksheet page-break-before avoid-break">
  <h2 id="ws-title" class="worksheet-title">Chapter Worksheet</h2>
  <div class="activity-section">
    <ol>
      <li>
        <p><strong>Your custom question?</strong></p>
        <div class="writing-area ruled-paper-bg" style="min-height: 8rem;"></div>
      </li>
      <!-- Repeat for 3-4 questions -->
    </ol>
  </div>
</section>
```

### Step 8: Update Section 6 (Closing Image)

Update image path and alt text:
```xml
<section class="closing image-quote page-break-before">
  <figure>
    <img src="../images/chapter-i-quote.jpeg" 
         alt="Inspirational quote: [Describe the actual quote or message in the image]"/>
    <figcaption>Optional caption</figcaption>
  </figure>
</section>
```

### Step 9: Clean Up

- Remove all HTML comments (<!-- ... -->)
- Verify all image paths are correct
- Check that footnote IDs match between text and endnotes
- Ensure proper heading hierarchy (h2 → h3, no h4 unless needed)

### Step 10: Validate

- Preview in EPUB reader
- Check page breaks occur correctly
- Verify responsive behavior at different sizes
- Test accessibility with screen reader

## Creating Frontmatter

### Example: Title Page

```bash
cp templates/frontmatter-template.xhtml OEBPS/text/1-TitlePage.xhtml
```

Uncomment the title page section, customize:
```xml
<body class="frontmatter-page">
  <main epub:type="frontmatter" role="main">
    <section class="frontmatter-shell title-page" aria-label="Title Page">
      <h1 class="frontmatter-title" epub:type="title">YOUR BOOK TITLE</h1>
      <h2 class="subtitle" epub:type="subtitle">Your Subtitle</h2>
      <div class="frontmatter-divider" aria-hidden="true"></div>
      <div class="author" epub:type="creator">Author Name</div>
      <div class="publisher-info" epub:type="publisher">Publisher</div>
      <div class="publisher-info">City, State</div>
      <div class="publisher-info">2025</div>
    </section>
  </main>
</body>
```

### Example: Table of Contents

```xml
<section class="frontmatter-shell toc-page" aria-label="Table of Contents">
  <h1>Contents</h1>
  <ul>
    <li>
      <span class="toc-entry-title">Chapter I: Title</span>
      <span class="toc-page-number">15</span>
    </li>
    <div class="toc-divider-img" aria-hidden="true"></div>
    <li>
      <span class="toc-entry-title">Chapter II: Title</span>
      <span class="toc-page-number">42</span>
    </li>
  </ul>
</section>
```

## Creating Backmatter

### Example: Conclusion

```bash
cp templates/backmatter-template.xhtml OEBPS/text/28-Conclusion.xhtml
```

Uncomment conclusion section:
```xml
<body class="backmatter-page">
  <main epub:type="backmatter" role="main">
    <section class="backmatter-card conclusion" aria-label="Conclusion">
      <h1>Conclusion</h1>
      <p>Your concluding text here...</p>
    </section>
  </main>
</body>
```

### Example: Journal Page

```xml
<section class="journal" aria-label="Journaling Space">
  <h1 style="text-align: center; margin-bottom: 2rem;">Daily Reflections</h1>
  
  <div class="journal-entry">
    <p class="journal-prompt">What are you grateful for today?</p>
    <div class="writing-area ruled-paper-bg" style="min-height: 12rem;"></div>
  </div>
  
  <div class="journal-entry">
    <p class="journal-prompt">What did you accomplish?</p>
    <div class="writing-area ruled-paper-bg" style="min-height: 12rem;"></div>
  </div>
</section>
```

## Common Patterns

### Adding a Blockquote
```xml
<blockquote>
  <p>"Your quote text here."</p>
</blockquote>
```

### Adding a Case Study
```xml
<h2>Case Study: Title</h2>
<p><strong>Challenge:</strong> Describe the problem.</p>
<p><strong>Solution:</strong> Explain the approach.</p>
<p><strong>Outcome:</strong> Share the results.</p>
```

### Adding a List
```xml
<ul>
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
</ul>
```

### Adding Footnote Reference
```xml
<!-- In body text: -->
<p>Your text here.<sup id="fnref-1"><a href="#fn-1">1</a></sup></p>

<!-- In endnotes section: -->
<li id="fn-1">
  <p>Author Name, <em>Book Title</em> (Publisher: Location, Year), page.</p>
</li>
```

### Adding Ruled Writing Area
```xml
<div class="writing-area ruled-paper-bg" style="min-height: 10rem;"></div>
```

### Adding Page Break
```xml
<div class="page-break"></div>
```

## Troubleshooting

### Problem: Page breaks not working
**Solution:** Ensure you're using the correct class:
```xml
<!-- For explicit break: -->
<div class="page-break"></div>

<!-- For break before element: -->
<section class="quiz-container page-break-before">
```

### Problem: Images not displaying
**Solution:** Check relative path from text/ to images/:
```xml
<!-- Correct: -->
<img src="../images/filename.jpg" alt="Description"/>

<!-- Incorrect: -->
<img src="images/filename.jpg" alt="Description"/>
```

### Problem: Styles not applying
**Solution:** Verify body class and stylesheet links:
```xml
<body class="chapter-page">  <!-- Must match file type -->
<link rel="stylesheet" type="text/css" href="../styles/style.css"/>
```

### Problem: Text overflowing page
**Solution:** For quizzes/worksheets, ensure max-height:
```xml
<section class="quiz-container chap-quiz page-break-before avoid-break">
  <!-- Content limited to 90vh by CSS -->
</section>
```

### Problem: Drop cap not working
**Solution:** Ensure proper structure:
```xml
<div class="introduction-paragraph dropcap-first-letter">
  <p><strong>F</strong>irst word must start with styled letter...</p>
</div>
```

## Best Practices Checklist

Before finalizing any file:

- [ ] Correct `<body>` class applied
- [ ] All `<img>` elements have descriptive `alt` text
- [ ] No inline `style=""` attributes (except minimal examples)
- [ ] Proper heading hierarchy (h1 → h2 → h3)
- [ ] ARIA labels on sections
- [ ] Footnote IDs match between text and endnotes
- [ ] Image paths are correct (../images/)
- [ ] Page breaks strategically placed
- [ ] No HTML comments left in final file
- [ ] File tested in EPUB reader

## Additional Resources

- **Complete Specification:** `EPUB_FORMATTING_HANDOFF.md`
- **Detailed Usage Guide:** `templates/README.md`
- **Implementation Summary:** `XHTML_TEMPLATES_IMPLEMENTATION.md`
- **Validation Report:** `TEMPLATE_VALIDATION_REPORT.md`
- **CSS Classes Reference:** Section 8 of `EPUB_FORMATTING_HANDOFF.md`

## Support

If you encounter issues:
1. Check the relevant template file for examples
2. Review the class definitions in `OEBPS/styles/style.css`
3. Consult `EPUB_FORMATTING_HANDOFF.md` for specifications
4. Examine existing files in `OEBPS/text/` for working examples

---

**Version:** 1.0  
**Last Updated:** 2025-10-22  
**Compatibility:** EPUB 3.0+, ACISS Layout System
