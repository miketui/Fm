# XHTML Templates for ACISS Layout System

This directory contains XHTML templates that conform to the ACISS layout system as specified in `EPUB_FORMATTING_HANDOFF.md`. These templates demonstrate the correct structure, class usage, and formatting conventions for creating EPUB content.

## Template Files

### 1. frontmatter-template.xhtml
Template for frontmatter pages (files 1-7). Includes variants for:
- Title Page
- Copyright Page
- Table of Contents
- Dedication Page
- Preface
- Self-Assessment/Worksheets

**Key Features:**
- Uses `<body class="frontmatter-page">` wrapper
- Implements single-page enforcement with `page-break-inside: avoid`
- Demonstrates proper use of `.frontmatter-shell` and related classes
- All variants fit within `min-height: 100vh`

### 2. part-divider-template.xhtml
Template for part divider pages (files 8, 12, 18, 24).

**Key Features:**
- Uses `<body class="part-page">` wrapper
- Full-screen `.part-divider` section with flex centering
- Includes `.part-title`, `.part-subtitle`, and `.decorative-line`
- Gradient background treatment
- Single-page constraint with `page-break-inside: avoid`

### 3. chapter-template.xhtml
Complete 6-section chapter template (files 9-27).

**Six-Section Structure:**
1. **Title Page** - Chapter number, title (one word per line), optional bible quote, introduction with drop cap
2. **Body Content** - Main chapter text with headings, paragraphs, lists, blockquotes
3. **Endnotes** (optional) - Numbered references with proper citations
4. **Quiz** - Always 4 questions with A-D options
5. **Worksheet** - Reflection questions with ruled paper backgrounds
6. **Closing Image** - Inspirational quote image with alt text

**Key Features:**
- Uses `<body class="chapter-page">` wrapper
- All six sections in order (body/endnotes flexible; quiz, worksheet, closing fixed)
- Page breaks between major sections
- Responsive typography with `clamp()`
- No inline styles - all formatting via CSS classes

### 4. backmatter-template.xhtml
Template for backmatter pages (files 28-44 plus nav.xhtml). Includes variants for:
- Conclusion
- Acknowledgments
- Author Bio
- Bibliography
- Quiz Key
- Assessment Scoring
- Affirmations
- Commitment Pages
- Journal Pages
- Worksheets (SMART Goals, Professional Development)
- Doodle Page
- Navigation (nav.xhtml)

**Key Features:**
- Uses `<body class="backmatter-page">` wrapper
- Single-page layouts with `page-break-inside: avoid`
- Specialized classes for different content types
- Grid layouts for journals (responsive: 1 column mobile, 2 columns desktop)

## Usage Guidelines

### 1. Copy the Appropriate Template
Choose the template that matches your content type:
- Frontmatter → `frontmatter-template.xhtml`
- Part Divider → `part-divider-template.xhtml`
- Chapter → `chapter-template.xhtml`
- Backmatter → `backmatter-template.xhtml`

### 2. Update Required Elements

**For All Templates:**
- Update `<title>` element in `<head>`
- Verify stylesheet links are correct (`../styles/fonts.css`, etc.)
- Set appropriate `epub:type` attributes

**For Frontmatter:**
- Uncomment the variant you need
- Replace placeholder text with actual content
- Remove unused variant sections

**For Part Dividers:**
- Update part number and title
- Customize subtitle/chapter range
- Modify or remove descriptive paragraph

**For Chapters:**
- Update chapter number (Roman numeral) and title
- Split title across `.title-line` elements (one word each)
- Replace introduction text (preserve drop cap on first letter)
- Add body content, preserving hierarchy
- Update endnotes if present
- Customize quiz questions (keep exactly 4)
- Modify worksheet reflection questions
- Update closing image path and alt text

**For Backmatter:**
- Uncomment the variant you need
- Replace placeholder content
- For journals: adjust number of prompts as needed
- For worksheets: customize questions/sections
- Remove unused variant sections

### 3. Validate Structure

**Checklist:**
- [ ] Correct `<body>` class applied (`.frontmatter-page`, `.part-page`, `.chapter-page`, `.backmatter-page`)
- [ ] All required CSS classes present
- [ ] No inline `style=""` attributes (except minimal exceptions in templates)
- [ ] All `<img>` elements have `alt` attributes
- [ ] Page breaks properly placed (chapters and backmatter)
- [ ] Hierarchical heading structure (h1 → h2 → h3)
- [ ] ARIA labels on sections and interactive elements
- [ ] Proper `epub:type` attributes

### 4. Class Reference

**See Section 8 of EPUB_FORMATTING_HANDOFF.md** for complete class reference.

**Most Common Classes:**

**Wrappers:**
- `.frontmatter-page`, `.part-page`, `.chapter-page`, `.backmatter-page`

**Frontmatter:**
- `.title-page`, `.copyright-page`, `.toc-page`, `.dedication-page`, `.preface-page`

**Chapters:**
- `.chap-title`, `.chapter-number-figure`, `.title-stack`, `.title-line`
- `.chap-body`, `.content-area`
- `.endnotes`, `.endnotes-title`
- `.quiz-container`, `.quiz-question`, `.quiz-option`
- `.worksheet`, `.writing-area`
- `.closing`, `.image-quote`

**Backmatter:**
- `.conclusion`, `.acknowledgments`, `.author-bio`, `.bibliography`
- `.quiz-key`, `.assessment`, `.affirmations`
- `.journal`, `.journal-entry`, `.journal-prompt`

**Utilities:**
- `.ruled-paper-bg` - Adds lined paper background
- `.page-break`, `.page-break-before`, `.page-break-after` - Controls page breaks
- `.avoid-break` - Prevents page breaks inside element
- `.mobile-hidden` - Hides on mobile devices
- `.print-only` - Shows only when printing

## Best Practices

### Text Fidelity
- **Never** alter the original manuscript text
- Preserve every word, punctuation mark, and paragraph
- Only wrap text in appropriate HTML elements
- Maintain original heading hierarchy

### Accessibility
- Always include `alt` text for images (descriptive, not decorative mentions)
- Use semantic HTML (`<nav>`, `<section>`, `<aside>`)
- Include ARIA labels on regions (`aria-label`, `aria-labelledby`)
- Ensure heading hierarchy is logical (no skipped levels)
- Maintain sufficient color contrast (WCAG AA minimum)

### Responsive Design
- Use `clamp()` for font sizes: `clamp(min, preferred, max)`
- Test at breakpoints: mobile (≤768px), tablet (769-1024px), desktop (≥1025px)
- Ensure content remains readable at all viewport sizes
- Use `.mobile-hidden` sparingly for truly decorative elements

### Page Breaks
- Frontmatter: Single-page, no internal breaks
- Chapters: Break before quiz, worksheet, and closing image
- Backmatter: Single-page when possible; break between major sections if needed
- Use `<div class="page-break"></div>` for explicit breaks
- Use `.page-break-before` class for element-level control

### Performance
- Reference existing SVG variables from `style.css` (don't duplicate)
- Use relative paths for images: `../images/filename.ext`
- Keep worksheets and quizzes within `max-height: 90vh` to avoid overflow

## Testing

After creating content from templates:

1. **Validate XHTML:**
   ```bash
   xmllint --noout --valid yourfile.xhtml
   ```

2. **Preview in EPUB Reader:**
   - Test in Calibre, Adobe Digital Editions, or Apple Books
   - Verify single-page constraints on frontmatter/backmatter
   - Check page breaks occur correctly in chapters

3. **Responsive Testing:**
   - View at mobile width (360px)
   - View at tablet width (768px)
   - View at desktop width (1200px+)

4. **Accessibility Check:**
   - Verify all images have alt text
   - Test keyboard navigation
   - Use screen reader to verify proper structure
   - Check color contrast ratios

5. **Print Preview:**
   - Verify `print.css` overrides apply correctly
   - Check page breaks align with content sections

## Examples

### Creating a New Chapter

1. Copy `chapter-template.xhtml` to `text/XX-chapter-title.xhtml`
2. Update title and chapter number
3. Replace introduction text (keep drop cap)
4. Add body content in `.chap-body .content-area`
5. Update or remove endnotes section
6. Customize 4 quiz questions
7. Modify worksheet reflection questions
8. Update closing image path and alt text
9. Remove all HTML comments
10. Validate and test

### Creating a New Journal Page

1. Copy `backmatter-template.xhtml` to `text/XX-journal-name.xhtml`
2. Uncomment the journal variant section
3. Update page title
4. Customize journal prompts (adjust number as needed)
5. Ensure grid layout for desktop (defined in CSS)
6. Remove unused variant sections
7. Validate and test

## Support

For questions or issues:
- Refer to `EPUB_FORMATTING_HANDOFF.md` for detailed specifications
- Review existing XHTML files in `OEBPS/text/` for examples
- Check `OEBPS/styles/style.css` for class definitions

## Version History

- **v1.0** (2025-10-22): Initial template set with ACISS layout system
  - Frontmatter, Part Divider, Chapter (6-section), and Backmatter templates
  - Full class reference and responsive design
  - Comprehensive documentation and usage guidelines
