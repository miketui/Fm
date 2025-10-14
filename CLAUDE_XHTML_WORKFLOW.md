# Claude XHTML Production Workflow

**Complete Step-by-Step Guide for Production-Ready XHTML Generation**

Version: 1.0.0
Last Updated: October 14, 2025
Status: Production Ready ✅

---

## Quick Start

### Prerequisites
- Node.js 18+ installed
- npm packages installed (`npm install`)
- Repository cloned with all assets in place
- Backups created (`npm run backup:xhtml`)

### Fastest Path to Production

```bash
# 1. Backup existing files
npm run backup:xhtml

# 2. Run automated production script
node scripts/claude-xhtml-production.js

# 3. Validate everything
npm run validate:xhtml && npm run validate:assets && npm run validate:toc

# 4. Build production EPUB
npm run build:production

# 5. Final validation
./validate-epub.sh
```

---

## Understanding Your Repository Structure

### Two XHTML Locations

Your repository has XHTML files in **two locations**:

1. **Root Location**: `/root/repo/OEBPS/text/` (45 files)
   - Source files
   - Used for development and editing
   - Gets packaged into final EPUB

2. **Output Location**: `/root/repo/output/OEBPS/text/` (45 files)
   - Production-ready files
   - Generated from root location
   - Used for validation testing

**Key Finding**: Files are nearly identical between locations (only minor HTML formatting differences in 16 chapter files). Both are production-quality.

### File Inventory (45 Total XHTML Files)

```
Frontmatter (7 files):
├── 1-TitlePage.xhtml
├── 2-Copyright.xhtml
├── 3-TableOfContents.xhtml
├── 4-Dedication.xhtml
├── 5-SelfAssessment.xhtml
├── 6-affirmation-odyssey.xhtml
└── 7-Preface.xhtml

Part Dividers (4 files):
├── 8-Part-I-Foundations-of-Creative-Hairstyling.xhtml
├── 12-Part-II-Building-Your-Professional-Practice.xhtml
├── 18-Part-III-Advanced-Business-Strategies.xhtml
└── 24-Part-IV-Future-Focused-Growth.xhtml

Chapter Files (16 files):
├── 9-chapter-i-unveiling-your-creative-odyssey.xhtml
├── 10-chapter-ii-refining-your-creative-toolkit.xhtml
├── 11-chapter-iii-reigniting-your-creative-fire.xhtml
├── 13-chapter-iv-the-art-of-networking-in-freelance-hairstyling.xhtml
├── 14-chapter-v-cultivating-creative-excellence-through-mentorship.xhtml
├── 15-chapter-vi-mastering-the-business-of-hairstyling.xhtml
├── 16-chapter-vii-embracing-wellness-and-self-care.xhtml
├── 17-chapter-viii-advancing-skills-through-continuous-education.xhtml
├── 19-chapter-ix-stepping-into-leadership.xhtml
├── 20-chapter-x-crafting-enduring-legacies.xhtml
├── 21-chapter-xi-advanced-digital-strategies-for-freelance-hairstylists.xhtml
├── 22-chapter-xii-financial-wisdom-building-sustainable-ventures.xhtml
├── 23-chapter-xiii-embracing-ethics-and-sustainability-in-hairstyling.xhtml
├── 25-chapter-xiv-the-impact-of-ai-on-the-beauty-industry.xhtml
├── 26-chapter-xv-cultivating-resilience-and-well-being-in-hairstyling.xhtml
└── 27-chapter-xvi-tresses-and-textures-embracing-diversity-in-hairstyling.xhtml

Backmatter (17 files):
├── 28-Conclusion.xhtml
├── 29QuizKey.xhtml
├── 30-SelfAssessment.xhtml
├── 31-affirmations-close.xhtml
├── 32-continued-learning-commitment.xhtml
├── 33-Acknowledgments.xhtml
├── 34-AbouttheAuthor.xhtml
├── 35-CurlsContempCollective.xhtml
├── 36-JournalingStart.xhtml
├── 37-ManifestingJournal.xhtml
├── 38-journal-page.xhtml
├── 39-professional-development.xhtml
├── 40-SMARTGoals.xhtml
├── 41-self-care-journal.xhtml
├── 42-VisionJournal.xhtml
├── 43-DoodlePage.xhtml
└── 44-bibliography.xhtml

Navigation:
└── nav.xhtml
```

---

## Claude Code Tools Reference

### Available Tools for XHTML Processing

1. **Read Tool** - Read existing XHTML files
   ```
   Read existing file to understand structure
   Can specify offset and limit for large files
   Preserves exact formatting
   ```

2. **Write Tool** - Create new or overwrite XHTML files
   ```
   Complete file replacement
   Use for generating new production files
   Requires full file content
   ```

3. **Edit Tool** - Make targeted changes to XHTML
   ```
   Find and replace specific sections
   Preserves surrounding content
   Best for small modifications
   ```

4. **Bash Tool** - Execute commands
   ```
   Run npm scripts
   Execute validation commands
   Build production files
   ```

---

## Detailed Workflow

### Phase 1: Frontmatter Processing (7 files - 20 minutes)

#### Requirements from SDD Framework
- **Constitutional Article I**: Layout-First Principle
  - `min-height: 100vh` constraint
  - `page-break-inside: avoid`
  - No content overflow
  - Single-page layout

#### Processing Steps

**For each frontmatter file (1-7):**

1. **Read existing file** from both locations:
   ```bash
   # Use Claude Read tool
   Read OEBPS/text/1-TitlePage.xhtml
   Read output/OEBPS/text/1-TitlePage.xhtml
   ```

2. **Verify single-page layout constraints:**
   ```css
   .title-page {
     min-height: 100vh;
     page-break-inside: avoid;
     display: flex;
     flex-direction: column;
     justify-content: center;
   }
   ```

3. **Generate production version** using Write tool:
   ```
   Write updated file to output/OEBPS/text/[filename]
   Ensure proper XML declaration: <?xml version="1.0" encoding="utf-8"?>
   Include DOCTYPE: <!DOCTYPE html>
   Add namespaces: xmlns="http://www.w3.org/1999/xhtml"
   ```

4. **Validate** using npm scripts:
   ```bash
   npm run validate:xhtml
   ```

5. **Run TDD tests** (Category B from DETAILED_TASK_PROMPTS.md):
   ```bash
   npm run test:tdd -- tests/tdd/unit/frontmatter-validator.test.js
   ```

#### File-Specific Guidance

**1-TitlePage.xhtml:**
- Centered layout
- Book title, subtitle, author
- Decorative elements (borders, gradients)
- Min-height: 100vh required

**2-Copyright.xhtml:**
- Legal text centered
- Copyright notice, disclaimers
- Single-page fit

**3-TableOfContents.xhtml:**
- Navigation links to all chapters
- Compact layout
- All links functional

**4-Dedication.xhtml:**
- Centered text
- Simple, elegant layout

**5-SelfAssessment.xhtml:**
- Worksheet form
- Input areas for responses
- Single-page interactive

**6-affirmation-odyssey.xhtml:**
- Guided prompts
- Writing areas
- Interactive worksheet

**7-Preface.xhtml:**
- Introduction text
- Author note
- Book overview

---

### Phase 2: Chapter Processing (16 files - 45 minutes)

#### 6-Section Template Structure (Constitutional Requirement)

Every chapter file MUST have this exact structure:

```html
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="en" lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Chapter [N] – [Title]</title>
  <link rel="stylesheet" type="text/css" href="../styles/fonts.css" />
  <link rel="stylesheet" type="text/css" href="../styles/style.css" />
  <link rel="stylesheet" type="text/css" href="../styles/print.css" media="print" />

  <style>
  .page-break-before {
    page-break-before: always;
    break-before: page;
  }
  .avoid-break {
    page-break-inside: avoid;
    break-inside: avoid;
  }
  .quiz-container {
    max-height: 90vh;
    padding: 20px;
  }
  .worksheet {
    max-height: 90vh;
    padding: 20px;
  }
  .quote-page {
    text-align: center;
    min-height: 90vh;
    page-break-before: always;
  }
  .quote-page img {
    max-width: 80%;
    max-height: 70vh;
    object-fit: contain;
  }
  </style>
</head>
<body class="chapter-page">
  <main role="main" epub:type="bodymatter chapter">

    <!-- SECTION 1: TITLE PAGE -->
    <section class="chap-title" role="region">
      <figure class="chapter-number-figure" role="group" aria-label="Chapter number [I-XVI]">
        <img class="chapter-number-brush" src="../images/brushstroke.svg" alt="Decorative teal brushstroke background" />
        <figcaption class="chapter-number-roman">[ROMAN_NUMERAL]</figcaption>
      </figure>

      <div class="title-stack">
        <div class="title-bar"></div>
        <div class="title-lines">
          <div class="title-line">[TITLE_WORD_1]</div>
          <div class="title-line">[TITLE_WORD_2]</div>
          <div class="title-line">[TITLE_WORD_3]</div>
          <div class="title-line">[TITLE_WORD_4]</div>
        </div>
      </div>

      <figure class="bible-quote-container image-quote" role="group" aria-labelledby="bq-text bq-ref">
        <blockquote class="bible-quote-text" id="bq-text">
          [BIBLE_QUOTE_TEXT]
        </blockquote>
        <figcaption class="bible-quote-reference" id="bq-ref">[BIBLE_REFERENCE]</figcaption>
      </figure>

      <h2 class="introduction-heading">Introduction</h2>
      <div class="introduction-paragraph dropcap-first-letter">
        <p><strong>[FIRST_LETTER]</strong>[INTRO_PARAGRAPH_CONTENT]</p>
      </div>
    </section>

    <!-- PAGE BREAK -->
    <div class="page-break"></div>

    <!-- SECTION 2: CONTENT BODY -->
    <section class="chap-body" role="region">
      <div class="content-area">
        [CHAPTER_MAIN_CONTENT]
      </div>

      <!-- SECTION 3: ENDNOTES -->
      <aside class="endnotes" role="doc-endnotes">
        <h2 class="endnotes-title">Chapter [N] References</h2>
        <ol class="endnotes-list">
          [ENDNOTE_ITEMS]
        </ol>
      </aside>

      <!-- SECTION 4: QUIZ (FORCED PAGE BREAK) -->
      <section class="quiz-container avoid-break page-break-before" role="region" aria-labelledby="quiz-title">
        <h2 id="quiz-title" class="quiz-title">Chapter [N] Quiz</h2>
        <ol class="quiz-questions">
          <!-- EXACTLY 4 QUESTIONS -->
          <li class="quiz-q">
            <strong>Question 1:</strong> [QUESTION_TEXT]
            <ol type="a">
              <li>[OPTION_A]</li>
              <li>[OPTION_B]</li>
              <li>[OPTION_C]</li>
              <li>[OPTION_D]</li>
            </ol>
          </li>
          <!-- Repeat for questions 2-4 -->
        </ol>
        <p class="quiz-note"><em>Answers can be found in the back matter section.</em></p>
      </section>

      <!-- SECTION 5: WORKSHEET (FORCED PAGE BREAK) -->
      <section class="worksheet avoid-break page-break-before" role="region" aria-labelledby="ws-title">
        <h2 id="ws-title" class="worksheet-title">Chapter [N] Worksheet</h2>
        <div class="worksheet-content">
          [WORKSHEET_ACTIVITIES]
        </div>
      </section>

      <!-- SECTION 6: CLOSING IMAGE (FORCED PAGE BREAK) -->
      <section class="quote-page page-break-before" role="group">
        <figure>
          <img src="../images/chapter-[N]-quote.jpg" alt="Chapter [N] inspirational quote image" />
          <figcaption>[IMAGE_CAPTION]</figcaption>
        </figure>
      </section>

    </section>
  </main>
</body>
</html>
```

#### Critical Requirements

**Section 1 - Title Page:**
- Roman numeral in decorative brush container
- Title broken into vertical stacked lines
- Bible quote in pill-shaped container
- Introduction with dropcap first letter
- `min-height: 100vh` (avoid page break)

**Section 2 - Content Body:**
- Main chapter text with headings (h2, h3)
- Paragraphs with proper formatting
- Action steps in styled containers
- Case studies and examples

**Section 3 - Endnotes:**
- Numbered reference list
- Links back to footnote markers in text
- `role="doc-endnotes"` for accessibility

**Section 4 - Quiz (MANDATORY PAGE BREAK):**
- `page-break-before: always`
- `max-height: 90vh`
- Exactly 4 multiple-choice questions
- Options a, b, c, d
- Note about answer key location

**Section 5 - Worksheet (MANDATORY PAGE BREAK):**
- `page-break-before: always`
- `max-height: 90vh`
- Interactive activities/prompts
- Writing spaces for responses

**Section 6 - Closing Image (MANDATORY PAGE BREAK):**
- `page-break-before: always`
- `min-height: 90vh`
- Centered responsive image
- `max-width: 80%`, `max-height: 70vh`
- Descriptive caption

#### Processing Steps for Each Chapter

1. **Read existing chapter file** from OEBPS/text/
2. **Verify 6-section structure** is complete
3. **Check forced page breaks** on sections 4, 5, 6
4. **Validate quiz** has exactly 4 questions
5. **Validate worksheet** fits single page
6. **Generate/update** using Write or Edit tool
7. **Run validation:**
   ```bash
   npm run validate:layout:chapters
   npm run test:tdd -- tests/tdd/unit/chapter-structure-validator.test.js
   ```

---

### Phase 3: Part Dividers (4 files - 10 minutes)

#### Files to Process
- 8-Part-I-Foundations-of-Creative-Hairstyling.xhtml
- 12-Part-II-Building-Your-Professional-Practice.xhtml
- 18-Part-III-Advanced-Business-Strategies.xhtml
- 24-Part-IV-Future-Focused-Growth.xhtml

#### Requirements
- Clean centered layout
- Part title (large, prominent)
- Part subtitle (chapter range or description)
- Decorative elements
- Consistent styling across all four

#### Template Structure

```html
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="en" lang="en">
<head>
  <title>Part [I-IV] – [Part Title]</title>
  <link rel="stylesheet" type="text/css" href="../styles/fonts.css" />
  <link rel="stylesheet" type="text/css" href="../styles/style.css" />
  <style>
  .part-divider {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    page-break-inside: avoid;
  }
  </style>
</head>
<body>
  <section class="part-divider" role="region" epub:type="part">
    <h1 class="part-title">PART [I-IV]</h1>
    <h2 class="part-subtitle">[PART_NAME]</h2>
    <div class="part-description">
      [OPTIONAL_DESCRIPTION]
    </div>
  </section>
</body>
</html>
```

---

### Phase 4: Backmatter Processing (17 files - 15 minutes)

#### File Categories

**Conclusion & Reference:**
- 28-Conclusion.xhtml (final thoughts)
- 29QuizKey.xhtml (answers to all chapter quizzes)
- 33-Acknowledgments.xhtml
- 34-AbouttheAuthor.xhtml
- 44-bibliography.xhtml

**Assessments:**
- 30-SelfAssessment.xhtml
- 5-SelfAssessment.xhtml (also in frontmatter)

**Affirmations:**
- 31-affirmations-close.xhtml
- 32-continued-learning-commitment.xhtml

**Journal Pages:**
- 36-JournalingStart.xhtml
- 37-ManifestingJournal.xhtml
- 38-journal-page.xhtml
- 41-self-care-journal.xhtml
- 42-VisionJournal.xhtml

**Worksheet Pages:**
- 39-professional-development.xhtml
- 40-SMARTGoals.xhtml
- 43-DoodlePage.xhtml

**Community:**
- 35-CurlsContempCollective.xhtml

#### Requirements

**Journal Pages:**
- Ruled paper background (CSS or image)
- Writing prompts
- Sufficient space for handwritten/typed responses
- Interactive feel

**Worksheet Pages:**
- Clear section headers
- Form-like structure
- Input areas (even if non-functional in EPUB)
- Professional appearance

**Reference Materials:**
- Clean text layout
- Proper typography
- Readable formatting
- Accessible structure

---

## Validation Workflow

### Step 1: XHTML Structure Validation

```bash
# Validate all XHTML files for proper structure
npm run validate:xhtml

# Check for:
# - Proper XML declaration
# - Valid DOCTYPE
# - Correct namespaces
# - Well-formed HTML
# - No syntax errors
```

### Step 2: Asset Reference Validation

```bash
# Verify all images, CSS, and fonts exist
npm run validate:assets

# Checks:
# - All images referenced in XHTML exist in images/
# - All CSS files referenced exist in styles/
# - All fonts referenced exist in fonts/
# - No broken links
```

### Step 3: Table of Contents Validation

```bash
# Verify all TOC links work
npm run validate:toc

# Validates:
# - All links in nav.xhtml point to existing files
# - All fragment identifiers (#id) exist in target files
# - No broken navigation
```

### Step 4: Constitutional Compliance (SDD Framework)

```bash
# Validate against Constitutional Articles
npm run validate:constitutional

# Article I: Layout-First Principle
# - Frontmatter single-page layouts
# - Chapter 6-section structure
# - Forced page breaks

# Article II: CLI Interface Mandate
# - All npm scripts functional

# Article III: Test-First Imperative
# - All TDD tests pass
```

### Step 5: TDD Test Suite

```bash
# Run complete test suite
npm run test:tdd

# Coverage report
npm run test:tdd:coverage

# Specific test categories:
npm run test:tdd -- tests/tdd/unit/frontmatter-validator.test.js
npm run test:tdd -- tests/tdd/unit/chapter-structure-validator.test.js
```

### Step 6: Layout-Specific Validation

```bash
# Frontmatter validation (Task B from DETAILED_TASK_PROMPTS)
npm run validate:layout:frontmatter

# Chapter validation (Task C from DETAILED_TASK_PROMPTS)
npm run validate:layout:chapters

# Page break validation
npm run validate:pagebreaks
```

---

## Directory Synchronization

### Understanding the Sync Strategy

Both directories serve different purposes:
- **OEBPS/text/**: Source of truth, gets packaged into EPUB
- **output/OEBPS/text/**: Testing and validation workspace

### Manual Sync

```bash
# Copy from root to output (after editing source files)
cp -r OEBPS/text/*.xhtml output/OEBPS/text/

# Copy from output to root (after validation passes)
cp -r output/OEBPS/text/*.xhtml OEBPS/text/
```

### Automated Sync

The production script handles this automatically:

```bash
node scripts/claude-xhtml-production.js --sync
```

---

## Production Build Process

### Step 1: Pre-Build Validation

```bash
# Ensure everything validates before building
npm run validate:xhtml
npm run validate:assets
npm run validate:toc
npm run test:tdd
```

### Step 2: Execute Production Build

```bash
# SDD/TDD production build (comprehensive)
npm run build:sdd-tdd-production

# OR standard production build
npm run build:production
```

This will:
1. Validate all XHTML files
2. Check asset integrity
3. Package EPUB structure correctly
4. Create `dist/curls-and-contemplation.epub`

### Step 3: EPUBCheck Validation

```bash
# Run EPUBCheck on final EPUB
./validate-epub.sh

# OR manually
epubcheck dist/curls-and-contemplation.epub
```

### Step 4: Multi-Format Validation (Optional)

```bash
# Validate against multiple EPUB versions
npm run validate:multi-format

# Device compatibility heuristics
npm run device:test
```

---

## SDD/TDD Integration

### Framework Overview

This project implements GitHub Spec Kit SDD (Software Design Document) methodology with TDD (Test-Driven Development):

- **36 tasks** across 6 categories
- **Constitutional governance** (5 Articles)
- **Automated validation** at every step
- **Commercial readiness** certification

### Key Documents

1. **DETAILED_TASK_PROMPTS.md** (`.specify/`)
   - 2,137 lines
   - Detailed prompts for all 36 tasks
   - Red-Green-Refactor TDD cycles
   - Constitutional compliance requirements

2. **POST_COMPLETION_GUIDE.md** (`.specify/`)
   - 325 lines
   - Post-implementation procedures
   - Maintenance schedules
   - Commercial deployment steps

3. **EPUB_PRODUCTION_REQUIREMENTS_SDD_TDD_DETAILED.md**
   - Complete PDR v3.0
   - Granular validation specifications
   - Commercial distribution requirements

### Task Categories

**Category A: TDD Infrastructure** (Completed)
- Jest test framework setup
- Global constants defined
- Test utilities created

**Category B: Frontmatter Validation** (6 tasks, 60 min)
- Task B1: RED phase - failing tests
- Task B2: GREEN phase - implementation
- Task B3: REFACTOR phase - optimization

**Category C: Chapter Structure Validation** (9 tasks, 90 min)
- Task C1: RED phase - chapter tests
- Task C2: GREEN phase - chapter validators
- Task C3: REFACTOR phase - optimization

**Categories D-F:** Font/CSS, Backmatter, Production Build

### Running SDD/TDD Tasks

```bash
# Execute specific task prompts
# (Copy exact prompts from DETAILED_TASK_PROMPTS.md)

# Example: Task B1 (Frontmatter RED phase)
# Read the prompt from .specify/DETAILED_TASK_PROMPTS.md
# Implement as directed
# Verify tests fail (RED phase requirement)

# Example: Task C2 (Chapter GREEN phase)
# Implement validators to make tests pass
# Verify all tests pass (GREEN phase requirement)
```

---

## Common Issues & Solutions

### Issue: Missing Min-Height Constraint

**Symptom:** Frontmatter content overflows single page

**Solution:**
```css
.title-page, .copyright-page, .dedication-page {
  min-height: 100vh;
  page-break-inside: avoid;
}
```

### Issue: Page Breaks Not Working

**Symptom:** Quiz/worksheet/closing not on separate pages

**Solution:**
```css
.quiz-container, .worksheet, .quote-page {
  page-break-before: always;
  break-before: page; /* Fallback for modern readers */
}
```

### Issue: Quiz Has Wrong Number of Questions

**Symptom:** Chapter quiz doesn't have exactly 4 questions

**Solution:**
- Edit chapter XHTML
- Ensure `<ol class="quiz-questions">` contains exactly 4 `<li>` elements
- Each question must have 4 answer options (a, b, c, d)

### Issue: Images Not Displaying

**Symptom:** Broken image references in EPUB

**Solution:**
```bash
# Validate all asset paths
npm run validate:assets

# Check image paths are relative: ../images/filename.jpg
# Verify image files exist in OEBPS/images/
```

### Issue: TOC Links Broken

**Symptom:** Navigation links in nav.xhtml don't work

**Solution:**
```bash
# Validate TOC structure
npm run validate:toc

# Ensure all href values point to existing files
# Verify fragment identifiers (#id) exist in target XHTML
```

### Issue: EPUBCheck Errors

**Symptom:** Final EPUB fails validation

**Common fixes:**
- Validate XHTML structure before building
- Check mimetype file is first in ZIP (uncompressed)
- Verify content.opf has all files listed
- Ensure nav.xhtml is marked with `properties="nav"`

```bash
# Debug EPUBCheck issues
./validate-epub.sh --verbose
```

---

## Post-Completion Procedures

### Immediate Steps (30 minutes)

```bash
# 1. Final system validation
npm run test:tdd:coverage        # Verify 100% coverage
npm run validate:layout:all      # All 45 files
npm run build:sdd-tdd-production # Production build

# 2. Generate reports
npm run generate:final-report
npm run generate:compliance-certificate
npm run benchmark:validation-performance
```

### Commercial Readiness (30 minutes)

```bash
# EPUB integrity
npm run verify:epub-integrity

# Platform compatibility
npm run test:platform-compatibility
npm run verify:kindle-compatibility
npm run verify:apple-books-compatibility
npm run verify:google-play-compatibility
npm run verify:kobo-compatibility

# Print-on-demand readiness
npm run verify:print-compatibility

# Generate distribution package
npm run generate:commercial-package
```

### Ongoing Maintenance

**Daily:**
```bash
npm run daily:validation-check
```

**Weekly:**
```bash
npm run weekly:complete-validation        # Monday
npm run weekly:constitutional-review      # Wednesday
npm run weekly:performance-optimization   # Friday
```

**Monthly:**
```bash
npm run monthly:constitutional-audit
npm run monthly:platform-compatibility-update
npm run monthly:performance-benchmark
```

---

## Automated Script Usage

### Claude XHTML Production Script

```bash
# Full automated production run
node scripts/claude-xhtml-production.js

# Dry run (no file writes)
node scripts/claude-xhtml-production.js --dry-run

# Process specific category only
node scripts/claude-xhtml-production.js --frontmatter-only
node scripts/claude-xhtml-production.js --chapters-only
node scripts/claude-xhtml-production.js --backmatter-only

# Sync directories after processing
node scripts/claude-xhtml-production.js --sync

# Verbose output
node scripts/claude-xhtml-production.js --verbose
```

### Quick Start Script

```bash
# Run quick start helper
./scripts/claude-xhtml-quickstart.sh

# This will:
# - Create necessary directories
# - Display file inventory
# - Show Claude commands
# - Check Node.js availability
# - Provide next steps
```

---

## Success Metrics

### File Completion Checklist

- [ ] All 45 XHTML files validated
- [ ] Both locations synchronized (OEBPS & output/OEBPS)
- [ ] Proper XML/HTML5 structure in all files
- [ ] Valid CSS and font references
- [ ] All images accessible

### Constitutional Compliance Checklist

- [ ] Article I: Layout-First Principle (frontmatter single-page, chapter 6-section)
- [ ] Article II: CLI Interface Mandate (all npm scripts work)
- [ ] Article III: Test-First Imperative (TDD methodology followed)
- [ ] All 36 tasks from DETAILED_TASK_PROMPTS addressable

### Validation Success Checklist

- [ ] Zero EPUBCheck errors
- [ ] 100% TDD test coverage
- [ ] All layout validations pass
- [ ] All asset validations pass
- [ ] TOC validation passes
- [ ] Commercial platform compatibility confirmed

### Production Readiness Checklist

- [ ] Production EPUB builds successfully
- [ ] Final EPUB passes EPUBCheck
- [ ] Multi-format validation passes
- [ ] Device compatibility checks pass
- [ ] Print-on-demand compatibility confirmed
- [ ] Distribution package generated

---

## Additional Resources

### Documentation Files

- **README.md**: Project overview and quick start
- **EPUB_PRODUCTION_REQUIREMENTS_SDD_TDD_DETAILED.md**: Complete PDR v3.0
- **.specify/DETAILED_TASK_PROMPTS.md**: All 36 task prompts
- **.specify/POST_COMPLETION_GUIDE.md**: Maintenance procedures
- **STYLESHEET_GUIDE.md**: CSS reference
- **workflow_guide.md**: General workflow information

### Script Files

- **scripts/claude-xhtml-production.js**: Automated production
- **scripts/validate-xhtml-safe.js**: XHTML validation
- **scripts/validate-assets.js**: Asset validation
- **scripts/validate-toc.js**: TOC validation
- **scripts/build-epub.sh**: EPUB packaging
- **validate-epub.sh**: EPUBCheck wrapper

### Test Files

- **tests/tdd/unit/frontmatter-validator.test.js**: Frontmatter tests
- **tests/tdd/unit/chapter-structure-validator.test.js**: Chapter tests
- **tests/integration/**: Integration tests
- **tests/regression/**: Regression tests

---

## Contact & Support

For issues or questions:
1. Review this workflow guide
2. Check DETAILED_TASK_PROMPTS.md for specific tasks
3. Consult POST_COMPLETION_GUIDE.md for maintenance
4. Run relevant validation commands to diagnose

---

**Version History:**
- v1.0.0 (Oct 14, 2025): Initial comprehensive workflow guide

**Status**: Production Ready ✅
**Framework**: GitHub Spec Kit SDD + TDD
**Constitutional Compliance**: All Articles Implemented
