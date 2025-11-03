# Master Chapter Template - Phase 2
## Complete XHTML Chapter Template with Image Assets

### Overview
This master chapter template provides a comprehensive, production-ready structure for all chapters in "The Artisan's Path." It includes all 7 sections with proper image asset integration and professional styling.

---

## Template Structure

The template follows a **7-section architecture**:

1. **Chapter Title Page** - Roman numeral with brushstroke background
2. **Chapter Body Content** - Main educational content
3. **Endnotes** - Citations and references
4. **Chapter Quiz** - Knowledge assessment
5. **Chapter Worksheet** - Practical exercises
6. **Chapter Summary** - Key takeaways
7. **Reflection Journal** - Personal growth prompts

---

## Image Assets Reference

### All Available Images in `/images/` Directory:

#### **Decorative Elements:**
- `brushstroke.svg` - Background for Roman numeral (centered on chapter title page)
- `decorative-line.svg` - Section dividers and ornamental breaks
- `crown-ornament.svg` - Headers for quizzes, worksheets, summaries, journals
- `chapter-frame.svg` - Case study boxes and special callouts
- `quote-marks.svg` - Quote decorations
- `endnote-marker.png` - Endnotes section icon

#### **Chapter Quote Images:**
- `chapter-i-quote.jpeg` through `chapter-xvi-quote.jpeg`
- `preface-quote.jpeg`
- `conclusion-quote.jpeg`

#### **Interactive Elements:**
- `quiz-checkbox-unchecked.svg` - Quiz answer options
- `quiz-checkbox-checked.svg` - Checked answer (for answer key)
- `quiz-checkbox.svg` - Generic checkbox

#### **Worksheet Elements:**
- `ruled-paper.svg` - Background for writing areas

#### **Other Assets:**
- `cover.png` - Book cover image
- `Michael.jpeg` - Author photo
- `part-border.svg` - Part divider pages
- `toc-divider.svg` - Table of contents

---

## How to Use This Template

### Step 1: Copy the Template
```bash
cp REBRANDED_OUTPUT/MASTER_CHAPTER_TEMPLATE.xhtml REBRANDED_OUTPUT/xhtml/[NUMBER]-chapter-[name].xhtml
```

### Step 2: Replace Placeholders

#### **File Metadata:**
- `[NUMBER]` → Chapter number (e.g., "XVII", "XVIII")
- `[CHAPTER TITLE]` → Full chapter title

#### **Title Page Section:**
- `[ROMAN_NUMERAL]` → Roman numeral (I, II, III, etc.)
- `[TITLE] [LINE] [TWO] [THREE]` → Break chapter title into 2-4 lines
- `[CHAPTER_NUMBER]` → Lowercase chapter identifier (i, ii, iii, etc.) for quote image
- `[INSERT BIBLE VERSE...]` → Inspirational quote or Bible verse
- `[SCRIPTURE REFERENCE]` → Citation (e.g., "Ephesians 2:10")
- `[FIRST_LETTER]` → First letter of introduction for drop cap

#### **Body Content:**
- `[ANECDOTE TITLE]` → Personal story heading
- `[MAIN SECTION TITLE]` → Primary section headings (I, II, III, etc.)
- `[Subsection Heading]` → H3 level headings
- All content paragraphs and case studies
- Endnote references (`<sup id="fnref-1"><a href="#fn-1">1</a></sup>`)

#### **Quiz Section:**
- Add 5-10 questions with multiple choice options
- Use `quiz-checkbox-unchecked.svg` for all options

#### **Worksheet Section:**
- Add 3-5 practical exercises
- Include ruled paper backgrounds for writing areas

#### **Summary Section:**
- List 5-7 key takeaways
- Write connecting paragraph to next chapter

#### **Journal Section:**
- Keep the 3 reflection prompts or customize as needed

### Step 3: Verify Image Paths

All image paths use **relative paths** from the `xhtml/` directory:
```html
<img src="../images/brushstroke.svg" />
<img src="../images/chapter-i-quote.jpeg" />
<img src="../images/decorative-line.svg" />
```

### Step 4: Update Endnotes

Match endnote IDs with in-text references:
- In-text: `<sup id="fnref-1"><a href="#fn-1">1</a></sup>`
- Endnote: `<li id="fn-1"><p>Citation... <a href="#fnref-1">↩</a></p></li>`

---

## Key Visual Elements

### 1. **Roman Numeral with Brushstroke Background**
```html
<figure class="chapter-number-figure" aria-hidden="true">
  <img class="chapter-number-brush" src="../images/brushstroke.svg" alt="" role="presentation"/>
  <figcaption class="chapter-number-roman accent-teal">I</figcaption>
</figure>
```
**Purpose:** Creates a centered, visually striking chapter number with brushstroke SVG as background

### 2. **Chapter Title Stack**
```html
<div class="title-stack">
  <div class="title-bar accent-gold"></div>
  <h1 class="title-lines accent-teal">
    <span class="title-line">Line One</span>
    <span class="title-line">Line Two</span>
  </h1>
</div>
```
**Purpose:** Multi-line title with gold accent bar

### 3. **Quote with Decorative Marks**
```html
<figure class="bible-quote-container">
  <img src="../images/quote-marks.svg" alt="" class="quote-decoration-start"/>
  <blockquote class="bible-quote-text">"Quote text..."</blockquote>
  <img src="../images/quote-marks.svg" alt="" class="quote-decoration-end"/>
  <figcaption class="bible-quote-reference accent-gold">— Citation</figcaption>
</figure>
```

### 4. **Drop Cap Introduction**
```html
<p><span class="drop-cap accent-teal">F</span>irst paragraph text...</p>
```
**Purpose:** Professional drop cap styling for chapter opening

### 5. **Section Dividers**
```html
<div class="decorative-break">
  <img src="../images/decorative-line.svg" alt="" aria-hidden="true"/>
</div>
```

### 6. **Action Steps Box**
```html
<div class="action-steps">
  <div class="action-steps-header">
    <img src="../images/crown-ornament.svg" alt="" class="ornament-icon"/>
    <h2>Actionable Steps</h2>
  </div>
  <ol>
    <li><em>Title:</em> Description...</li>
  </ol>
</div>
```

### 7. **Quiz Questions**
```html
<div class="quiz-option">
  <img src="../images/quiz-checkbox-unchecked.svg" alt="Unchecked" class="checkbox-icon"/>
  <span>A) Option text</span>
</div>
```

### 8. **Worksheet Writing Areas**
```html
<div class="writing-area">
  <div class="ruled-lines">
    <img src="../images/ruled-paper.svg" alt="" class="ruled-paper-bg"/>
  </div>
</div>
```

---

## CSS Classes Reference

### **Color Accents:**
- `.accent-teal` - Teal color (#2C5F5D)
- `.accent-gold` - Gold color (#D4AF37)

### **Layout Classes:**
- `.chapter` - Body class for chapter pages
- `.chap-title` - Title page section
- `.chap-body` - Main content section
- `.page-break` - Forces page break for print/PDF

### **Content Classes:**
- `.dropcap-first-letter` - Container for drop cap
- `.drop-cap` - The drop cap letter itself
- `.action-steps` - Actionable steps box
- `.case-study-box` - Case study container
- `.quiz-question` - Quiz question container
- `.worksheet-exercise` - Worksheet exercise container

---

## Accessibility Features

The template includes proper ARIA labels and semantic HTML:

- `role="main"` - Main content landmark
- `epub:type="bodymatter chapter"` - EPUB semantic inflection
- `role="doc-chapter"` - Document chapter role
- `aria-labelledby` - Associates headings with sections
- `aria-hidden="true"` - Hides decorative images from screen readers
- `role="presentation"` - Marks decorative SVGs

---

## Quality Checklist

Before finalizing a chapter, verify:

- [ ] Roman numeral matches chapter number
- [ ] Chapter quote image exists and is linked correctly
- [ ] All image paths use `../images/` prefix
- [ ] Drop cap letter is correct
- [ ] All endnote IDs match in-text references
- [ ] Quiz has 5-10 questions with 4 options each
- [ ] Worksheet has 3-5 exercises
- [ ] Summary has 5-7 key takeaways
- [ ] All sections have decorative dividers
- [ ] Page breaks are properly placed
- [ ] File is valid XHTML (validate with xmllint)

---

## Validation Command

```bash
xmllint --noout REBRANDED_OUTPUT/xhtml/[chapter-file].xhtml
```

If the file validates, there will be no output. Errors will be displayed with line numbers.

---

## Image Asset Integration Summary

### **Total Images Used in Template:**
1. `brushstroke.svg` - Roman numeral background ✅
2. `chapter-[NUMBER]-quote.jpeg` - Chapter quote image ✅
3. `quote-marks.svg` - Quote decorations (2x) ✅
4. `decorative-line.svg` - Section dividers (multiple) ✅
5. `chapter-frame.svg` - Case study frames ✅
6. `crown-ornament.svg` - Section headers (quiz, worksheet, summary, journal) ✅
7. `endnote-marker.png` - Endnotes icon ✅
8. `quiz-checkbox-unchecked.svg` - Quiz options (multiple) ✅
9. `ruled-paper.svg` - Writing area backgrounds (multiple) ✅

### **All Assets Properly Linked:** ✅
- Relative paths from `/xhtml/` directory
- Correct file extensions
- Proper alt text and ARIA labels
- Presentation roles for decorative images

---

## Example Usage

See `REBRANDED_OUTPUT/xhtml/9-chapter-i-unveiling-your-creative-odyssey.xhtml` for a complete, filled-in example of this template in use.

---

## Support

For questions or issues with the template:
1. Review existing chapter files in `REBRANDED_OUTPUT/xhtml/`
2. Check image assets in `REBRANDED_OUTPUT/images/`
3. Validate XHTML structure with xmllint
4. Refer to `REBRANDED_OUTPUT/content.opf` for manifest entries

---

**Template Version:** 2.0
**Last Updated:** 2025-11-03
**Status:** Production Ready ✅
