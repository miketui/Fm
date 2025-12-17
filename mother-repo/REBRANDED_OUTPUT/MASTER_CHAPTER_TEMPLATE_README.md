# Master Chapter Template - Phase 2 (Updated)
## Complete XHTML Chapter Template with Enhanced Design & Image Assets

### Overview
This master chapter template provides a comprehensive, production-ready structure for all chapters in "The Artisan's Path." It features an **enhanced circular brushstroke design** based on the mockup, with proper page breaks and streamlined content flow.

---

## Template Structure

The template follows a **6-section architecture** with proper page breaks:

1. **Chapter Title Page** - Circular teal brushstroke with centered Roman numeral, vertical bar title layout
2. **Chapter Body Content** - Main educational content (NEW PAGE after title)
3. **Endnotes** - Citations and references (NEW PAGE after body)
4. **Chapter Quiz** - 4 multiple choice questions (NEW PAGE after endnotes)
5. **Chapter Worksheet** - Practical exercises (NEW PAGE after quiz)
6. **Chapter Closing Quote** - Centered inspirational quote image (NEW PAGE after worksheet)

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

### 1. **Circular Teal Brushstroke with Roman Numeral (Enhanced Design)**
```html
<div class="chapter-number-section">
  <div class="brushstroke-circle">
    <img class="brushstroke-bg" src="../images/brushstroke.svg" alt="" role="presentation"/>
    <div class="roman-numeral-overlay accent-teal">I</div>
  </div>
</div>
```
**Purpose:** Creates a circular teal gradient background (inspired by mockup) with centered white Roman numeral. The brushstroke.svg provides texture/visual interest.

### 2. **Chapter Title with Vertical Bar (Updated Layout)**
```html
<div class="title-section">
  <div class="vertical-bar"></div>
  <h1 class="title-lines accent-teal">
    <span class="title-line">UNVEILING</span>
    <span class="title-line">YOUR</span>
    <span class="title-line">CREATIVE</span>
    <span class="title-line">ODYSSEY</span>
  </h1>
</div>
```
**Purpose:** Multi-line uppercase title in teal with vertical black bar on left (matches mockup design)

### 3. **Bible Quote Box with Rounded Teal Border (Enhanced)**
```html
<div class="bible-quote-box">
  <blockquote class="quote-text">
    "For we are God's handiwork, created in Christ Jesus to do good works..."
  </blockquote>
  <div class="quote-reference">— EPHESIANS 2:10</div>
</div>
```
**Purpose:** Clean, elegant quote box with rounded teal border and subtle background (matches mockup)

### 4. **Chapter Introduction with Teal Underline Heading**
```html
<div class="introduction-section">
  <h2 class="section-heading accent-teal">CHAPTER INTRODUCTION</h2>

  <p class="drop-cap-paragraph">
    <span class="drop-cap accent-teal">P</span>icture celebrity stylist...
  </p>
</div>
```
**Purpose:** "CHAPTER INTRODUCTION" heading with teal underline border, followed by drop cap paragraph (matches mockup)

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

### 7. **Quiz Questions (4 Questions Only)**
```html
<div class="quiz-question">
  <div class="question-header">
    <span class="question-number">1.</span>
    <p class="question-text">What is the main concept...</p>
  </div>
  <div class="quiz-options">
    <div class="quiz-option">
      <img src="../images/quiz-checkbox-unchecked.svg" alt="Unchecked" class="checkbox-icon"/>
      <span class="option-label">A)</span>
      <span class="option-text">First option</span>
    </div>
    <!-- Repeat for B, C, D -->
  </div>
</div>
```
**Note:** Template includes exactly 4 multiple choice questions per chapter.

### 8. **Worksheet Writing Areas**
```html
<div class="writing-area">
  <div class="ruled-lines" style="background-image: url('../images/ruled-paper.svg'); background-repeat: repeat-y; min-height: 150px;">
    <!-- Ruled paper background for writing -->
  </div>
</div>
```

### 9. **Chapter Closing Quote Image (NEW)**
```html
<section class="chapter-closing-quote">
  <div class="closing-quote-container">
    <figure class="closing-quote-figure">
      <img src="../images/chapter-i-quote.jpeg" alt="Chapter closing inspirational quote" class="closing-quote-image"/>
    </figure>
    <div class="closing-ornament">
      <img src="../images/crown-ornament.svg" alt="" aria-hidden="true"/>
    </div>
  </div>
</section>
```
**Purpose:** Full-page centered quote image at the end of each chapter with decorative crown ornament

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

## Page Break Structure (IMPORTANT!)

The template includes **5 strategic page breaks** for proper pagination:

1. **After Title Page** → Chapter Body Content starts on new page
2. **After Body Content** → Endnotes start on new page
3. **After Endnotes** → Quiz starts on new page (4 questions)
4. **After Quiz** → Worksheet starts on new page
5. **After Worksheet** → Closing Quote Image on new page

```html
<div class="page-break" epub:type="pagebreak"></div>
```

This ensures clean separation between sections for both digital and print formats.

---

## Quality Checklist

Before finalizing a chapter, verify:

- [ ] Roman numeral matches chapter number
- [ ] Circular brushstroke background displays correctly
- [ ] Vertical bar appears on left of title
- [ ] Bible quote box has rounded teal border
- [ ] "CHAPTER INTRODUCTION" heading has teal underline
- [ ] Chapter quote image exists and is linked correctly (both title page and closing)
- [ ] All image paths use `../images/` prefix
- [ ] Drop cap letter is correct and teal colored
- [ ] All endnote IDs match in-text references
- [ ] Quiz has exactly 4 multiple choice questions with 4 options each
- [ ] Worksheet has 3-4 exercises with ruled paper backgrounds
- [ ] **5 page breaks are properly placed** (after title, body, endnotes, quiz, worksheet)
- [ ] Closing quote image is centered on final page
- [ ] All sections have decorative dividers where appropriate
- [ ] File is valid XHTML

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

## Summary of Changes (Phase 2 Update)

### Enhanced Visual Design
- ✅ Circular teal brushstroke background for Roman numeral (centered)
- ✅ Vertical black bar on left of chapter title
- ✅ Rounded teal border for Bible quote box
- ✅ "CHAPTER INTRODUCTION" heading with teal underline

### Structural Improvements
- ✅ Reduced from 7 sections to 6 sections (removed separate Summary and Journal)
- ✅ Added 5 strategic page breaks for clean pagination
- ✅ Quiz reduced to exactly 4 multiple choice questions
- ✅ Added dedicated Chapter Closing Quote Image page

### Page Flow
```
Page 1: Chapter Title Page (circular brushstroke, title, quote, introduction)
  ↓ PAGE BREAK
Page 2+: Chapter Body Content (anecdotes, sections, case studies, action steps)
  ↓ PAGE BREAK
Page X: Endnotes
  ↓ PAGE BREAK
Page X+1: Quiz (4 questions)
  ↓ PAGE BREAK
Page X+2: Worksheet (3-4 exercises)
  ↓ PAGE BREAK
Page X+3: Closing Quote Image (centered, with crown ornament)
```

---

**Template Version:** 2.1 (Enhanced Design)
**Last Updated:** 2025-11-03
**Status:** Production Ready ✅
**Based On:** Chapter Title Page Mockup Design
