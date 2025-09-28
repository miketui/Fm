# Product Development Requirements (PDR) v3.0 - DETAILED
## "Curls & Contemplation: A Stylist's Interactive Journey Journal"
### EPUB Production with Integrated SDD Spec Kit & TDD + Granular Layout Validation

---

## EXECUTIVE SUMMARY

This enhanced PDR v3.0 provides comprehensive specifications for producing a commercial-quality EPUB with **rigorous layout validation**, **GitHub Spec Kit (SDD) integration**, and **Test-Driven Development (TDD)** methodologies. The document includes granular validation requirements for all 45 XHTML files, ensuring perfect single-page layouts, forced page breaks, and commercial distribution readiness.

**Critical Requirements Addressed:**
- ✅ **Frontmatter (Files 1-7)**: Single-page layout validation with `min-height: 100vh`
- ✅ **Chapter Files (16 chapters)**: 6-section structured layout with forced page breaks
- ✅ **Part Dividers (4 files)**: Clean divider page validation
- ✅ **Backmatter (17 files)**: Journal and worksheet layout validation
- ✅ **Chapter Template**: Exact implementation of provided template structure
- ✅ **Font & CSS**: Complete validation of 6 fonts and 3 CSS files

---

## PART I: SDD SPEC KIT INTEGRATION

### 1.1 Constitutional Framework (GitHub Spec Kit)

#### Article I: Library-First Principle
**Specification**: Every EPUB feature must be modular and reusable
```yaml
specification_id: "epub-library-first"
version: "3.0.0"
requirements:
  - validation_modules: "standalone_components"
  - layout_validators: "reusable_across_file_types"
  - test_frameworks: "modular_test_suites"
  - build_tools: "independent_validation_libraries"
```

#### Article II: CLI Interface Mandate
**Specification**: All operations accept text input, produce text output
```yaml
specification_id: "epub-cli-interface"
version: "3.0.0"
commands:
  validate_layout: "npm run validate:layout -- --file=FILE --type=TYPE"
  validate_fonts: "npm run validate:fonts -- --check-loading"
  validate_pagebreaks: "npm run validate:pagebreaks -- --strict"
  build_production: "npm run build:sdd-tdd-production"
```

#### Article III: Test-First Imperative
**Specification**: No layout changes without corresponding validation tests
```yaml
specification_id: "epub-test-first"
version: "3.0.0"
test_categories:
  layout_tests: "before_any_styling_changes"
  font_tests: "before_font_modifications"
  pagebreak_tests: "before_pagination_changes"
  content_tests: "before_content_updates"
```

### 1.2 SDD Specification Architecture

#### Core File Type Specifications

**Frontmatter Specification**:
```yaml
specification_id: "frontmatter-layout-spec"
version: "3.0.0"
intent: "Single-page layouts for files 1-7 with no overflow"
constraints:
  page_height: "min-height: 100vh"
  page_break: "page-break-inside: avoid"
  overflow: "no_content_overflow_allowed"
  fonts: "consistent_typography_across_all_files"
file_requirements:
  file_1_title_page:
    layout: "centered_vertical_horizontal"
    elements: ["title", "subtitle", "author", "decorative_elements"]
    constraints: "single_page_only"
  file_2_copyright:
    layout: "legal_text_centered"
    elements: ["copyright_notice", "legal_disclaimers"]
    constraints: "single_page_only"
  file_3_toc:
    layout: "navigation_list"
    elements: ["chapter_links", "page_numbers", "decorative_dividers"]
    constraints: "single_page_compact_layout"
  file_4_dedication:
    layout: "centered_text"
    elements: ["dedication_text", "optional_decorative_elements"]
    constraints: "single_page_only"
  file_5_self_assessment:
    layout: "worksheet_form"
    elements: ["assessment_questions", "input_areas", "instructions"]
    constraints: "single_page_interactive_layout"
  file_6_affirmation_odyssey:
    layout: "worksheet_form"
    elements: ["affirmation_sections", "writing_areas", "guided_prompts"]
    constraints: "single_page_interactive_layout"
  file_7_preface:
    layout: "text_content"
    elements: ["introduction_text", "author_note", "book_overview"]
    constraints: "single_page_text_only"
```

**Chapter Specification**:
```yaml
specification_id: "chapter-layout-spec"
version: "3.0.0"
intent: "6-section chapter structure with forced page breaks"
template_structure:
  section_1_title_page:
    elements:
      - roman_numeral_badge: "centered_top"
      - title_stack: "vertical_left_aligned"
      - bible_quote_container: "centered_pill_design"
      - introduction_heading: "uppercase_centered"
      - introduction_paragraph: "dropcap_justified"
    constraints:
      page_break: "avoid"
      height: "min-height: 100vh"
      overflow: "none"
  section_2_content:
    elements:
      - chapter_headings: "h2_styled"
      - body_paragraphs: "justified_text"
      - blockquotes: "highlighted_sections"
    constraints:
      flow: "natural_pagination"
      typography: "consistent_with_design"
  section_3_endnotes:
    elements:
      - endnotes_title: "section_heading"
      - numbered_references: "ordered_list"
    constraints:
      page_break_before: "optional"
      layout: "reference_format"
  section_4_quiz:
    elements:
      - quiz_title: "centered_heading"
      - four_questions: "mcq_format_only"
      - answer_choices: "a_b_c_d_options"
      - note: "answer_key_reference"
    constraints:
      page_break_before: "always"
      page_break_after: "always"
      layout: "single_page_only"
      height: "max-height: 90vh"
  section_5_worksheet:
    elements:
      - worksheet_title: "section_heading"
      - activity_sections: "interactive_areas"
      - writing_prompts: "guided_questions"
    constraints:
      page_break_before: "always"
      page_break_after: "always"
      layout: "single_page_only"
      height: "max-height: 90vh"
  section_6_closing_image:
    elements:
      - chapter_quote_image: "centered_responsive"
      - image_caption: "descriptive_text"
    constraints:
      page_break_before: "always"
      layout: "centered_image_page"
      height: "min-height: 90vh"
      image_sizing: "max-width: 80%, max-height: 70vh"
```

**CSS and Font Specification**:
```yaml
specification_id: "styling-assets-spec"
version: "3.0.0"
intent: "Complete font loading and CSS validation"
font_requirements:
  required_fonts:
    - "librebaskerville-regular.woff2"
    - "librebaskerville-bold.woff2"
    - "librebaskerville-italic.woff2"
    - "CinzelDecorative.woff2"
    - "Montserrat-Regular.woff2"
    - "Montserrat-Bold.woff2"
  font_families:
    primary: "Libre Baskerville, Georgia, serif"
    decorative: "Cinzel Decorative, serif"
    sans_serif: "Montserrat, Arial, sans-serif"
css_requirements:
  required_files:
    - "fonts.css": "font_face_declarations"
    - "style.css": "main_styling_rules"
    - "print.css": "print_optimized_styles"
  critical_classes:
    - ".chap-title": "chapter_title_pages"
    - ".chapter-number-container": "roman_numeral_badges"
    - ".title-stack": "vertical_title_layout"
    - ".bible-quote-container": "quote_pill_design"
    - ".quiz-container": "quiz_page_layout"
    - ".worksheet": "worksheet_page_layout"
    - ".page-break-before": "forced_page_breaks"
    - ".avoid-break": "keep_content_together"
```

---

## PART II: TDD ENHANCED METHODOLOGY

### 2.1 Layout Validation TDD Framework

#### Red-Green-Refactor for EPUB Layout

**RED Phase: Write Failing Layout Tests**
```javascript
// Layout Validation Test Suite
describe('EPUB Layout Validation', () => {
  describe('Frontmatter Single-Page Layouts', () => {
    const frontmatterFiles = [
      '1-TitlePage.xhtml',
      '2-Copyright.xhtml',
      '3-TableOfContents.xhtml',
      '4-Dedication.xhtml',
      '5-SelfAssessment.xhtml',
      '6-affirmation-odyssey.xhtml',
      '7-Preface.xhtml'
    ];

    frontmatterFiles.forEach(file => {
      it(`${file} should have single-page layout constraint`, async () => {
        const content = await readXHTMLFile(`output/OEBPS/text/${file}`);
        const hasMinHeight = content.includes('min-height: 100vh');
        const hasPageBreakAvoid = content.includes('page-break-inside: avoid');

        expect(hasMinHeight).toBe(true);
        expect(hasPageBreakAvoid).toBe(true);
      });

      it(`${file} should have no content overflow`, async () => {
        const metrics = await calculateContentHeight(`output/OEBPS/text/${file}`);
        expect(metrics.contentHeight).toBeLessThanOrEqual(metrics.viewportHeight);
      });
    });
  });

  describe('Chapter Structure Validation', () => {
    const chapterFiles = [
      '9-chapter-i-unveiling-your-creative-odyssey.xhtml',
      '10-chapter-ii-refining-your-creative-toolkit.xhtml',
      // ... all 16 chapter files
    ];

    chapterFiles.forEach(file => {
      it(`${file} should have 6-section structure`, async () => {
        const sections = await extractChapterSections(`output/OEBPS/text/${file}`);

        expect(sections).toHaveLength(6);
        expect(sections[0]).toMatch(/title.*page/i);
        expect(sections[1]).toMatch(/content.*body/i);
        expect(sections[2]).toMatch(/endnotes/i);
        expect(sections[3]).toMatch(/quiz/i);
        expect(sections[4]).toMatch(/worksheet/i);
        expect(sections[5]).toMatch(/closing.*image/i);
      });

      it(`${file} should have forced page breaks`, async () => {
        const content = await readXHTMLFile(`output/OEBPS/text/${file}`);
        const pageBreaks = content.match(/page-break-before:\s*always/g);

        expect(pageBreaks).toHaveLength(3); // quiz, worksheet, closing image
      });

      it(`${file} quiz should be single page`, async () => {
        const quizSection = await extractQuizSection(`output/OEBPS/text/${file}`);
        const hasMaxHeight = quizSection.includes('max-height: 90vh');
        const questionCount = (quizSection.match(/<li.*quiz-q/g) || []).length;

        expect(hasMaxHeight).toBe(true);
        expect(questionCount).toBe(4);
      });

      it(`${file} worksheet should be single page`, async () => {
        const worksheetSection = await extractWorksheetSection(`output/OEBPS/text/${file}`);
        const hasMaxHeight = worksheetSection.includes('max-height: 90vh');
        const hasWorksheetClass = worksheetSection.includes('class="worksheet"');

        expect(hasMaxHeight).toBe(true);
        expect(hasWorksheetClass).toBe(true);
      });
    });
  });
});
```

**GREEN Phase: Implement Layout Validation**
```javascript
// Layout Validation Implementation
class EPUBLayoutValidator {
  constructor() {
    this.errors = [];
    this.warnings = [];
  }

  async validateFrontmatterLayouts() {
    const frontmatterFiles = await this.getFrontmatterFiles();

    for (const file of frontmatterFiles) {
      await this.validateSinglePageLayout(file);
      await this.validateFontLoading(file);
      await this.validateCSSClasses(file);
    }
  }

  async validateChapterStructures() {
    const chapterFiles = await this.getChapterFiles();

    for (const file of chapterFiles) {
      await this.validateChapterTemplate(file);
      await this.validatePageBreaks(file);
      await this.validateQuizLayout(file);
      await this.validateWorksheetLayout(file);
      await this.validateClosingImage(file);
    }
  }

  async validateSinglePageLayout(filePath) {
    const content = await fs.readFile(filePath, 'utf8');

    // Check for required CSS
    if (!content.includes('min-height: 100vh')) {
      this.errors.push(`${filePath}: Missing min-height: 100vh constraint`);
    }

    if (!content.includes('page-break-inside: avoid')) {
      this.errors.push(`${filePath}: Missing page-break-inside: avoid`);
    }

    // Validate content doesn't exceed viewport
    const contentHeight = await this.calculateContentHeight(filePath);
    if (contentHeight > 100) { // 100vh equivalent
      this.errors.push(`${filePath}: Content exceeds single page constraint`);
    }
  }

  async validateChapterTemplate(filePath) {
    const content = await fs.readFile(filePath, 'utf8');

    // Validate required template elements
    const requiredElements = [
      'chapter-number-container',
      'title-stack',
      'bible-quote-container',
      'introduction-heading',
      'dropcap-first-letter'
    ];

    for (const element of requiredElements) {
      if (!content.includes(element)) {
        this.errors.push(`${filePath}: Missing required element: ${element}`);
      }
    }
  }
}
```

**REFACTOR Phase: Optimize and Enhance**
```javascript
// Enhanced Layout Validator with Performance Optimization
class OptimizedEPUBLayoutValidator extends EPUBLayoutValidator {
  constructor() {
    super();
    this.cache = new Map();
    this.parallelValidation = true;
  }

  async validateAllFiles() {
    const validationPromises = [];

    // Parallel validation for better performance
    if (this.parallelValidation) {
      validationPromises.push(this.validateFrontmatterLayouts());
      validationPromises.push(this.validateChapterStructures());
      validationPromises.push(this.validatePartDividers());
      validationPromises.push(this.validateBackmatter());
    }

    await Promise.all(validationPromises);
    return this.generateValidationReport();
  }
}
```

### 2.2 Specification-Driven Test Generation

#### Automated Test Creation from SDD Specs
```yaml
test_generation_spec:
  input: "SDD YAML specifications"
  output: "Automated test suites"
  process:
    1. "Parse YAML specifications"
    2. "Generate test cases for each constraint"
    3. "Create validation functions"
    4. "Build assertion statements"
    5. "Package into test suite"
```

---

## PART III: GRANULAR FILE VALIDATION SPECIFICATIONS

### 3.1 Frontmatter Files (1-7) - Single Page Layout Requirements

#### File 1: Title Page (1-TitlePage.xhtml)
```yaml
file_spec:
  id: "title-page-validation"
  requirements:
    layout:
      constraint: "min-height: 100vh"
      positioning: "centered_vertical_horizontal"
      overflow: "none_allowed"
    elements:
      title: "main_book_title"
      subtitle: "descriptive_subtitle"
      author: "author_name"
      decorative: "background_gradients_brushstrokes"
    css_classes:
      - ".title-page": "main_container"
      - ".title-text": "primary_heading"
      - ".author-text": "author_credit"
    validation_tests:
      - "single_page_constraint"
      - "centered_layout"
      - "typography_consistency"
      - "responsive_design"
```

#### File 2: Copyright (2-Copyright.xhtml)
```yaml
file_spec:
  id: "copyright-page-validation"
  requirements:
    layout:
      constraint: "min-height: 100vh"
      positioning: "centered_legal_text"
      overflow: "none_allowed"
    elements:
      copyright_notice: "legal_copyright_text"
      publisher_info: "publication_details"
      legal_disclaimers: "required_legal_text"
    css_classes:
      - ".copyright-page": "main_container"
      - ".legal-text": "copyright_styling"
    validation_tests:
      - "single_page_constraint"
      - "legal_text_formatting"
      - "readability_standards"
```

#### File 3: Table of Contents (3-TableOfContents.xhtml)
```yaml
file_spec:
  id: "toc-validation"
  requirements:
    layout:
      constraint: "min-height: 100vh"
      positioning: "organized_navigation"
      overflow: "compact_single_page"
    elements:
      chapter_links: "clickable_navigation"
      page_numbers: "reference_numbers"
      decorative_dividers: "visual_separators"
    css_classes:
      - ".contents-page": "main_container"
      - ".toc-container": "navigation_layout"
      - ".toc-entry": "individual_links"
    validation_tests:
      - "single_page_constraint"
      - "link_functionality"
      - "navigation_accessibility"
```

#### Files 4-7: Similar detailed specifications for Dedication, Self Assessment, Affirmation Odyssey, and Preface

### 3.2 Chapter Files (9-11, 13-17, 19-23, 25-27) - 6-Section Structure

#### Chapter Template Implementation (Based on Provided Template)
```html
<!-- EXACT TEMPLATE STRUCTURE TO VALIDATE -->
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en" class="epub-dark">
  <head>
    <title>Chapter Template</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" type="text/css" href="../styles/fonts.css" />
    <link rel="stylesheet" type="text/css" href="../styles/style.css" />
  </head>
  <body class="chap-title">
    <!-- Section 1: Title Page Layout -->
    <section class="chap-title" role="doc-part">
      <div class="chapter-number-container" aria-label="Chapter Number">
        <div class="chapter-number-brush">
          <img class="brushstroke-img" src="../images/brushstroke.svg" alt="" />
          <div class="chapter-number-text"><!-- ROMAN_NUMERAL --></div>
        </div>
      </div>

      <div class="chapter-title-container">
        <div class="chapter-title-stack">
          <div class="chapter-title-vertical" aria-hidden="true">
            <!-- vertical bar is the left border via CSS -->
          </div>
          <div>
            <h1 class="chapter-title chapter-title-word"><!-- TITLE_LINE_1 --></h1>
            <h1 class="chapter-title chapter-title-word"><!-- TITLE_LINE_2 --></h1>
            <h1 class="chapter-title chapter-title-word"><!-- TITLE_LINE_3 --></h1>
            <h1 class="chapter-title chapter-title-word"><!-- TITLE_LINE_4 --></h1>
          </div>
        </div>
      </div>

      <figure class="bible-quote-container image-quote" role="group" aria-labelledby="bq-text bq-ref">
        <blockquote class="bible-quote-text" id="bq-text">
          <!-- BIBLE_QUOTE_TEXT -->
        </blockquote>
        <figcaption class="bible-quote-reference" id="bq-ref"><!-- BIBLE_QUOTE_REF --></figcaption>
      </figure>

      <div class="introduction-heading" role="heading" aria-level="2">Introduction</div>

      <div class="introduction-paragraph dropcap-first-letter">
        <!-- INTRO_PARAGRAPH_HTML -->
      </div>
    </section>

    <!-- Section 2: Chapter Body -->
    <section class="chap-body" role="doc-chapter">
      <div class="content-area">
        <!-- XHTMLFRAG_BODY -->
      </div>

      <!-- Section 3: Endnotes -->
      <aside class="endnotes" role="doc-endnotes">
        <h2 class="endnotes-title">References</h2>
        <!-- XHTMLFRAG_ENDNOTES -->
      </aside>

      <!-- Section 4: Chapter Quiz (FORCED PAGE BREAK) -->
      <section class="quiz-container chap-quiz avoid-break page-break-before" role="region" aria-labelledby="quiz-title">
        <h2 id="quiz-title" class="quiz-title">Chapter Quiz</h2>
        <ol class="quiz-questions">
          <!-- EXACTLY 4 QUESTIONS -->
          <!-- XHTMLFRAG_QUIZ_4Q_ONLY -->
        </ol>
        <p class="sr-only">Answer key provided in the back matter section.</p>
      </section>

      <!-- Section 5: Chapter Worksheet (FORCED PAGE BREAK) -->
      <section class="worksheet avoid-break page-break-before" role="region" aria-labelledby="ws-title">
        <h2 id="ws-title" class="worksheet-title">Worksheet</h2>
        <!-- XHTMLFRAG_WORKSHEET_STATIC -->
      </section>

      <!-- Section 6: Closing Image (FORCED PAGE BREAK) -->
      <section class="image-quote page-break-before" role="group" aria-labelledby="closing-caption">
        <figure>
          <img src="../images/<!-- CLOSING_IMAGE_FILE -->" alt="Chapter closing inspirational quote image." />
          <figcaption id="closing-caption" class="font-small color-light">
            <!-- CLOSING_IMAGE_CAPTION -->
          </figcaption>
        </figure>
      </section>
    </section>
  </body>
</html>
```

#### Chapter Validation Specifications
```yaml
chapter_validation:
  section_1_title_page:
    required_classes:
      - "chap-title"
      - "chapter-number-container"
      - "chapter-title-stack"
      - "bible-quote-container"
      - "dropcap-first-letter"
    validation_rules:
      - "roman_numeral_present"
      - "title_lines_stacked_vertically"
      - "bible_quote_in_pill_container"
      - "introduction_with_dropcap"
    layout_constraints:
      - "min-height: 100vh"
      - "avoid page break"

  section_4_quiz:
    required_classes:
      - "quiz-container"
      - "chap-quiz"
      - "avoid-break"
      - "page-break-before"
    validation_rules:
      - "exactly_four_questions"
      - "multiple_choice_format"
      - "answer_key_reference"
    layout_constraints:
      - "max-height: 90vh"
      - "single page only"
      - "forced page break before"

  section_5_worksheet:
    required_classes:
      - "worksheet"
      - "avoid-break"
      - "page-break-before"
    validation_rules:
      - "interactive_elements_static"
      - "worksheet_title_present"
      - "activity_sections_defined"
    layout_constraints:
      - "max-height: 90vh"
      - "single page only"
      - "forced page break before"

  section_6_closing_image:
    required_classes:
      - "image-quote"
      - "page-break-before"
    validation_rules:
      - "chapter_specific_image"
      - "centered_layout"
      - "responsive_sizing"
    layout_constraints:
      - "min-height: 90vh"
      - "image max-width: 80%"
      - "image max-height: 70vh"
      - "forced page break before"
```

### 3.3 Part Dividers (8, 12, 18, 24) - Clean Layout Validation

```yaml
part_divider_spec:
  id: "part-divider-validation"
  files:
    - "8-Part-I-Foundations-of-Creative-Hairstyling.xhtml"
    - "12-Part-II-Building-Your-Professional-Practice.xhtml"
    - "18-Part-III-Advanced-Business-Strategies.xhtml"
    - "24-Part-IV-Future-Focused-Growth.xhtml"
  requirements:
    layout:
      constraint: "clean_divider_page"
      positioning: "centered_content"
      styling: "consistent_across_parts"
    elements:
      part_title: "main_heading"
      part_subtitle: "chapter_range"
      decorative_line: "visual_separator"
      introduction_text: "overview_paragraphs"
    css_classes:
      - ".part-divider": "main_container"
      - ".part-title": "primary_heading"
      - ".part-subtitle": "secondary_heading"
    validation_tests:
      - "consistent_styling"
      - "proper_hierarchy"
      - "clean_layout"
```

### 3.4 Backmatter Files (28-44) - Journal and Worksheet Validation

```yaml
backmatter_spec:
  id: "backmatter-validation"
  file_types:
    conclusion: "28-Conclusion.xhtml"
    quiz_key: "29QuizKey.xhtml"
    assessments: ["30-SelfAssessment.xhtml"]
    journals:
      - "36-JournalingStart.xhtml"
      - "37-ManifestingJournal.xhtml"
      - "38-journal-page.xhtml"
      - "41-self-care-journal.xhtml"
      - "42-VisionJournal.xhtml"
    worksheets:
      - "39-professional-development.xhtml"
      - "40-SMARTGoals.xhtml"
      - "43-DoodlePage.xhtml"
    reference:
      - "33-Acknowledgments.xhtml"
      - "34-AbouttheAuthor.xhtml"
      - "44-bibliography.xhtml"
  requirements:
    journal_layout:
      constraint: "interactive_worksheet_design"
      elements: ["ruled_paper_background", "writing_areas", "prompts"]
      styling: "consistent_with_brand"
    worksheet_layout:
      constraint: "activity_based_design"
      elements: ["form_fields", "instructions", "completion_areas"]
      styling: "professional_appearance"
    reference_layout:
      constraint: "clean_text_layout"
      elements: ["formatted_text", "proper_typography"]
      styling: "readable_presentation"
```

---

## PART IV: CSS AND FONT VALIDATION FRAMEWORK

### 4.1 Font Loading Validation

#### Required Font Specifications
```yaml
font_validation_spec:
  id: "font-loading-validation"
  required_fonts:
    libre_baskerville:
      regular: "librebaskerville-regular.woff2"
      bold: "librebaskerville-bold.woff2"
      italic: "librebaskerville-italic.woff2"
      usage: "primary_body_text"
    cinzel_decorative:
      regular: "CinzelDecorative.woff2"
      usage: "chapter_titles_decorative_elements"
    montserrat:
      regular: "Montserrat-Regular.woff2"
      bold: "Montserrat-Bold.woff2"
      usage: "headings_ui_elements"
  validation_tests:
    - "font_files_exist"
    - "font_face_declarations_valid"
    - "font_loading_successful"
    - "fallback_fonts_defined"
    - "cross_platform_compatibility"
```

#### Font Validation Implementation
```javascript
class FontValidator {
  async validateFontLoading() {
    const requiredFonts = [
      'librebaskerville-regular.woff2',
      'librebaskerville-bold.woff2',
      'librebaskerville-italic.woff2',
      'CinzelDecorative.woff2',
      'Montserrat-Regular.woff2',
      'Montserrat-Bold.woff2'
    ];

    for (const font of requiredFonts) {
      const fontPath = `output/OEBPS/fonts/${font}`;
      const exists = await this.fileExists(fontPath);

      if (!exists) {
        this.errors.push(`Missing required font: ${font}`);
      } else {
        await this.validateFontFile(fontPath);
      }
    }
  }

  async validateFontDeclarations() {
    const fontsCss = await fs.readFile('output/OEBPS/styles/fonts.css', 'utf8');

    const requiredDeclarations = [
      '@font-face.*Libre Baskerville.*regular',
      '@font-face.*Libre Baskerville.*bold',
      '@font-face.*Libre Baskerville.*italic',
      '@font-face.*Cinzel Decorative',
      '@font-face.*Montserrat.*regular',
      '@font-face.*Montserrat.*bold'
    ];

    for (const declaration of requiredDeclarations) {
      if (!fontsCss.match(new RegExp(declaration, 'i'))) {
        this.errors.push(`Missing font declaration: ${declaration}`);
      }
    }
  }
}
```

### 4.2 CSS Class Validation

#### Critical CSS Classes Validation
```yaml
css_validation_spec:
  id: "css-classes-validation"
  critical_classes:
    chapter_layout:
      - ".chap-title": "chapter_title_pages"
      - ".chapter-number-container": "roman_numeral_containers"
      - ".chapter-title-stack": "vertical_title_layout"
      - ".bible-quote-container": "quote_pill_design"
      - ".introduction-heading": "section_headings"
      - ".dropcap-first-letter": "paragraph_first_letters"
    page_control:
      - ".page-break-before": "forced_page_breaks"
      - ".page-break-after": "forced_page_breaks"
      - ".avoid-break": "keep_content_together"
    interactive_elements:
      - ".quiz-container": "quiz_page_layout"
      - ".quiz-questions": "question_list_styling"
      - ".worksheet": "worksheet_page_layout"
      - ".ruled-paper-bg": "journal_background"
    responsive_design:
      - ".responsive-image": "image_scaling"
      - ".mobile-hidden": "mobile_optimizations"
      - ".print-only": "print_specific_styling"
  validation_tests:
    - "class_definitions_exist"
    - "class_usage_correct"
    - "styling_consistent"
    - "responsive_behavior"
```

---

## PART V: AUTOMATED VALIDATION PIPELINE

### 5.1 SDD/TDD Integrated Build Pipeline

#### Enhanced Build Commands
```json
{
  "scripts": {
    "validate:layout:frontmatter": "node scripts/validate-frontmatter-layouts.js",
    "validate:layout:chapters": "node scripts/validate-chapter-structures.js",
    "validate:pagebreaks": "node scripts/validate-forced-pagebreaks.js",
    "validate:fonts": "node scripts/validate-font-loading.js",
    "validate:css": "node scripts/validate-css-classes.js",
    "validate:template": "node scripts/validate-chapter-template.js",

    "test:layout": "jest tests/layout",
    "test:sdd-specs": "node scripts/validate-sdd-specifications.js",
    "test:tdd-coverage": "jest --coverage tests/",

    "build:sdd-validate": "npm run validate:specifications && npm run validate:layout:all",
    "build:tdd-test": "npm run test:layout && npm run test:sdd-specs",
    "build:sdd-tdd-production": "npm run build:sdd-validate && npm run build:tdd-test && npm run build:production",

    "qa:full-validation": "npm run validate:layout:frontmatter && npm run validate:layout:chapters && npm run validate:pagebreaks && npm run validate:fonts && npm run validate:css",
    "qa:commercial-ready": "npm run qa:full-validation && npm run test:accessibility && npm run test:cross-platform"
  }
}
```

#### Validation Pipeline Implementation
```javascript
class ComprehensiveEPUBValidator {
  constructor() {
    this.frontmatterValidator = new FrontmatterLayoutValidator();
    this.chapterValidator = new ChapterStructureValidator();
    this.fontValidator = new FontValidator();
    this.cssValidator = new CSSValidator();
    this.templateValidator = new ChapterTemplateValidator();
  }

  async runFullValidation() {
    console.log('🚀 Starting Comprehensive EPUB Validation...');

    const results = {
      frontmatter: await this.frontmatterValidator.validate(),
      chapters: await this.chapterValidator.validate(),
      fonts: await this.fontValidator.validate(),
      css: await this.cssValidator.validate(),
      templates: await this.templateValidator.validate()
    };

    const report = this.generateValidationReport(results);
    await this.saveValidationReport(report);

    return this.isCommercialReady(results);
  }

  isCommercialReady(results) {
    const criticalErrors = this.getCriticalErrors(results);

    return {
      ready: criticalErrors.length === 0,
      errors: criticalErrors,
      warnings: this.getWarnings(results),
      commercialChecklist: this.generateCommercialChecklist(results)
    };
  }
}
```

### 5.2 Quality Gates for Commercial Distribution

#### Commercial Readiness Checklist
```yaml
commercial_readiness:
  layout_validation:
    - "all_frontmatter_single_page_compliant"
    - "all_chapters_6_section_structure"
    - "forced_pagebreaks_correctly_implemented"
    - "quiz_sections_single_page_only"
    - "worksheet_sections_single_page_only"
    - "closing_images_properly_centered"

  typography_validation:
    - "all_6_fonts_loading_correctly"
    - "font_fallbacks_defined"
    - "consistent_typography_across_files"
    - "responsive_font_sizing"

  technical_validation:
    - "epub_3_0_compliant"
    - "epubcheck_zero_errors"
    - "accessibility_wcag_2_1_aa"
    - "cross_platform_compatible"

  content_validation:
    - "all_45_files_present"
    - "navigation_functional"
    - "internal_links_working"
    - "images_optimized_and_accessible"

  distribution_validation:
    - "file_size_under_limits"
    - "metadata_complete"
    - "drm_compatible"
    - "print_on_demand_ready"
```

---

## PART VI: IMPLEMENTATION ROADMAP

### 6.1 Phase 1: SDD Specification Setup (30 minutes)

#### Step 1: Initialize GitHub Spec Kit Integration
```bash
# Install and initialize Spec Kit
uvx --from git+https://github.com/github/spec-kit.git specify init curls-contemplation-epub

# Create SDD directory structure
mkdir -p .spec-kit/{specifications,plans,tasks}

# Generate initial specifications
/specify "EPUB layout validation system with single-page frontmatter constraints"
/plan "Implement comprehensive layout validation framework"
/tasks "Create validation tests for all 45 XHTML files"
```

#### Step 2: Create Validation Test Structure
```bash
# Create TDD test directories
mkdir -p tests/{layout,specifications,integration}

# Generate layout validation tests
node scripts/generate-layout-tests.js --source=output/OEBPS/text/
```

#### Step 3: Validate Current Structure Against Specifications
```bash
# Run initial validation
npm run validate:layout:frontmatter
npm run validate:layout:chapters
npm run validate:fonts
npm run validate:css
```

### 6.2 Phase 2: Layout Validation Implementation (1-2 hours)

#### Frontmatter Single-Page Validation
```javascript
// scripts/validate-frontmatter-layouts.js
class FrontmatterValidator {
  async validateSinglePageLayouts() {
    const frontmatterFiles = [
      '1-TitlePage.xhtml',
      '2-Copyright.xhtml',
      '3-TableOfContents.xhtml',
      '4-Dedication.xhtml',
      '5-SelfAssessment.xhtml',
      '6-affirmation-odyssey.xhtml',
      '7-Preface.xhtml'
    ];

    const results = [];

    for (const file of frontmatterFiles) {
      const validation = await this.validateFile(`output/OEBPS/text/${file}`);
      results.push({
        file,
        singlePage: validation.hasSinglePageConstraint,
        noOverflow: validation.contentFitsInViewport,
        cssCompliant: validation.hasRequiredClasses,
        errors: validation.errors
      });
    }

    return results;
  }

  async validateFile(filePath) {
    const content = await fs.readFile(filePath, 'utf8');

    return {
      hasSinglePageConstraint: this.checkSinglePageConstraint(content),
      contentFitsInViewport: await this.checkContentHeight(filePath),
      hasRequiredClasses: this.checkRequiredClasses(content),
      errors: this.collectErrors()
    };
  }

  checkSinglePageConstraint(content) {
    return content.includes('min-height: 100vh') &&
           content.includes('page-break-inside: avoid');
  }

  async checkContentHeight(filePath) {
    // Implementation to calculate content height vs viewport
    const metrics = await this.calculateLayoutMetrics(filePath);
    return metrics.contentHeight <= metrics.viewportHeight;
  }
}
```

#### Chapter Structure Validation
```javascript
// scripts/validate-chapter-structures.js
class ChapterStructureValidator {
  async validateChapterTemplate(filePath) {
    const content = await fs.readFile(filePath, 'utf8');

    const validation = {
      hasCorrectSections: this.validateSixSectionStructure(content),
      hasForcedPageBreaks: this.validatePageBreaks(content),
      hasQuizSinglePage: this.validateQuizLayout(content),
      hasWorksheetSinglePage: this.validateWorksheetLayout(content),
      hasClosingImage: this.validateClosingImageLayout(content),
      templateCompliance: this.validateTemplateCompliance(content)
    };

    return validation;
  }

  validateSixSectionStructure(content) {
    const requiredSections = [
      'chap-title',           // Title page
      'chap-body',            // Content body
      'endnotes',             // References
      'quiz-container',       // Quiz section
      'worksheet',            // Worksheet section
      'image-quote'           // Closing image
    ];

    return requiredSections.every(section => content.includes(section));
  }

  validatePageBreaks(content) {
    const pageBreakSections = [
      'quiz-container.*page-break-before',
      'worksheet.*page-break-before',
      'image-quote.*page-break-before'
    ];

    return pageBreakSections.every(section =>
      content.match(new RegExp(section, 'i'))
    );
  }

  validateQuizLayout(content) {
    const quizSection = this.extractSection(content, 'quiz-container');

    return quizSection.includes('max-height: 90vh') &&
           quizSection.includes('avoid-break') &&
           this.countQuestions(quizSection) === 4;
  }

  countQuestions(quizSection) {
    const questions = quizSection.match(/<li.*class="quiz-q"/g) || [];
    return questions.length;
  }
}
```

### 6.3 Phase 3: Font and CSS Validation (30 minutes)

#### Font Loading Validation
```javascript
// scripts/validate-font-loading.js
class FontValidator {
  async validateAllFonts() {
    const requiredFonts = {
      'librebaskerville-regular.woff2': 'Libre Baskerville Regular',
      'librebaskerville-bold.woff2': 'Libre Baskerville Bold',
      'librebaskerville-italic.woff2': 'Libre Baskerville Italic',
      'CinzelDecorative.woff2': 'Cinzel Decorative',
      'Montserrat-Regular.woff2': 'Montserrat Regular',
      'Montserrat-Bold.woff2': 'Montserrat Bold'
    };

    const validation = {
      fontsExist: {},
      fontDeclarations: {},
      fontUsage: {},
      errors: []
    };

    // Check font files exist
    for (const [filename, fontName] of Object.entries(requiredFonts)) {
      const fontPath = `output/OEBPS/fonts/${filename}`;
      validation.fontsExist[fontName] = await this.fileExists(fontPath);

      if (!validation.fontsExist[fontName]) {
        validation.errors.push(`Missing font file: ${filename}`);
      }
    }

    // Check font declarations in CSS
    const fontsCss = await fs.readFile('output/OEBPS/styles/fonts.css', 'utf8');
    validation.fontDeclarations = this.validateFontDeclarations(fontsCss);

    // Check font usage in XHTML files
    validation.fontUsage = await this.validateFontUsage();

    return validation;
  }

  validateFontDeclarations(fontsCss) {
    const declarations = {
      'Libre Baskerville': fontsCss.includes('@font-face') && fontsCss.includes('Libre Baskerville'),
      'Cinzel Decorative': fontsCss.includes('Cinzel Decorative'),
      'Montserrat': fontsCss.includes('Montserrat')
    };

    return declarations;
  }
}
```

### 6.4 Phase 4: Commercial Distribution Validation (45 minutes)

#### Print-on-Demand Compatibility
```javascript
// scripts/validate-print-compatibility.js
class PrintCompatibilityValidator {
  async validatePrintReadiness() {
    return {
      pageBreaks: await this.validatePrintPageBreaks(),
      imageResolution: await this.validateImageQuality(),
      fontEmbedding: await this.validatePrintFonts(),
      margins: await this.validatePrintMargins(),
      colorProfile: await this.validateColorProfile()
    };
  }

  async validatePrintPageBreaks() {
    const chapters = await this.getChapterFiles();
    const results = [];

    for (const chapter of chapters) {
      const content = await fs.readFile(chapter, 'utf8');

      results.push({
        file: chapter,
        hasPageBreakCSS: content.includes('page-break-before: always'),
        hasAvoidBreak: content.includes('page-break-inside: avoid'),
        printMediaQuery: content.includes('@media print')
      });
    }

    return results;
  }

  async validateImageQuality() {
    const images = await this.getImageFiles();
    const results = [];

    for (const image of images) {
      const stats = await this.getImageStats(image);

      results.push({
        file: image,
        resolution: stats.resolution,
        printReady: stats.resolution >= 300, // DPI for print
        fileSize: stats.size,
        format: stats.format
      });
    }

    return results;
  }
}
```

#### Online Platform Compatibility
```javascript
// scripts/validate-platform-compatibility.js
class PlatformCompatibilityValidator {
  async validateForPlatforms() {
    const platforms = [
      'amazon-kindle',
      'apple-books',
      'google-play-books',
      'kobo',
      'barnes-noble'
    ];

    const results = {};

    for (const platform of platforms) {
      results[platform] = await this.validateForPlatform(platform);
    }

    return results;
  }

  async validateForPlatform(platform) {
    const validators = {
      'amazon-kindle': this.validateKindleCompatibility,
      'apple-books': this.validateAppleBooksCompatibility,
      'google-play-books': this.validateGooglePlayCompatibility,
      'kobo': this.validateKoboCompatibility,
      'barnes-noble': this.validateNookCompatibility
    };

    return await validators[platform].call(this);
  }

  async validateKindleCompatibility() {
    return {
      fileSize: await this.checkFileSize() < 650 * 1024 * 1024, // 650MB limit
      cssSupport: await this.checkKindleCSSSupport(),
      fontSupport: await this.checkKindleFontSupport(),
      imageFormats: await this.checkImageFormats(['jpeg', 'png', 'gif'])
    };
  }
}
```

### 6.5 Phase 5: Production Build and Deployment (15 minutes)

#### Enhanced Build Pipeline
```bash
# Complete SDD/TDD production build
npm run build:sdd-tdd-production

# Commercial readiness validation
npm run qa:commercial-ready

# Generate final EPUB
npm run build:production

# Validate final output
npm run validate:final-epub
```

#### Deployment Commands
```bash
# Prepare for distribution
npm run prepare:distribution

# Generate multiple formats if needed
npm run generate:kindle-format
npm run generate:print-pdf

# Final quality assurance
npm run qa:final-check
```

---

## PART VII: SUCCESS METRICS AND VALIDATION CRITERIA

### 7.1 Layout Validation Success Criteria

#### Frontmatter Single-Page Compliance
```yaml
frontmatter_success_criteria:
  single_page_constraint: "100%"
  viewport_compliance: "all_files_fit_100vh"
  css_consistency: "consistent_styling_across_7_files"
  typography: "proper_font_loading_and_usage"

  specific_requirements:
    title_page: "centered_layout_no_overflow"
    copyright: "legal_text_single_page"
    toc: "navigation_compact_layout"
    dedication: "centered_text_single_page"
    self_assessment: "worksheet_single_page"
    affirmation_odyssey: "interactive_single_page"
    preface: "text_content_single_page"
```

#### Chapter Structure Compliance
```yaml
chapter_success_criteria:
  six_section_structure: "100%"
  forced_page_breaks: "quiz_worksheet_closing_image"
  template_compliance: "exact_match_provided_template"
  single_page_sections: "quiz_and_worksheet_only"

  template_elements:
    roman_numeral_badge: "centered_top_positioning"
    title_stack: "vertical_left_aligned_layout"
    bible_quote: "pill_container_design"
    quiz_questions: "exactly_4_mcq_format"
    worksheet: "activity_based_layout"
    closing_image: "centered_responsive_design"
```

### 7.2 Technical Validation Success Criteria

#### Font and CSS Compliance
```yaml
technical_success_criteria:
  font_loading: "all_6_fonts_loading_correctly"
  css_validation: "all_classes_properly_defined"
  responsive_design: "mobile_and_ereader_compatible"
  accessibility: "wcag_2_1_aa_compliant"

  font_requirements:
    libre_baskerville: "3_variants_loaded"
    cinzel_decorative: "decorative_font_loaded"
    montserrat: "2_variants_loaded"
    fallbacks: "proper_fallback_stacks_defined"
```

#### Commercial Distribution Readiness
```yaml
commercial_success_criteria:
  epub_validation: "epubcheck_zero_errors"
  platform_compatibility: "amazon_apple_google_kobo_ready"
  file_size: "under_platform_limits"
  print_compatibility: "300dpi_images_proper_pagebreaks"

  distribution_checklist:
    metadata: "complete_and_accurate"
    cover_image: "high_resolution_optimized"
    table_of_contents: "functional_navigation"
    accessibility: "screen_reader_compatible"
```

---

## PART VIII: TROUBLESHOOTING AND ERROR RESOLUTION

### 8.1 Common Layout Issues and Solutions

#### Frontmatter Overflow Problems
```yaml
overflow_issues:
  problem: "content_exceeds_single_page"
  causes:
    - "excessive_padding_margins"
    - "oversized_images_or_graphics"
    - "too_much_text_content"
    - "incorrect_font_sizing"
  solutions:
    - "adjust_css_spacing"
    - "optimize_image_dimensions"
    - "condense_text_content"
    - "reduce_font_sizes_strategically"
  validation: "npm run validate:layout:frontmatter --fix"
```

#### Chapter Page Break Issues
```yaml
pagebreak_issues:
  problem: "forced_page_breaks_not_working"
  causes:
    - "missing_page_break_before_always"
    - "conflicting_css_rules"
    - "ereader_ignoring_page_breaks"
  solutions:
    - "add_explicit_page_break_css"
    - "use_both_page_break_and_break_before"
    - "add_avoid_break_to_sections"
  validation: "npm run validate:pagebreaks --strict"
```

#### Font Loading Failures
```yaml
font_issues:
  problem: "fonts_not_loading_properly"
  causes:
    - "incorrect_font_file_paths"
    - "missing_font_declarations"
    - "unsupported_font_formats"
    - "ereader_font_restrictions"
  solutions:
    - "verify_font_file_locations"
    - "check_font_face_declarations"
    - "provide_fallback_fonts"
    - "test_on_target_devices"
  validation: "npm run validate:fonts --comprehensive"
```

### 8.2 Automated Error Resolution

#### Self-Healing Layout Validation
```javascript
class AutomaticLayoutFixer {
  async fixCommonIssues() {
    const issues = await this.detectLayoutIssues();

    for (const issue of issues) {
      switch (issue.type) {
        case 'missing-page-constraint':
          await this.addSinglePageConstraint(issue.file);
          break;
        case 'missing-page-break':
          await this.addForcedPageBreak(issue.file, issue.section);
          break;
        case 'font-declaration-missing':
          await this.addFontDeclaration(issue.font);
          break;
        case 'css-class-missing':
          await this.addMissingCSSClass(issue.className);
          break;
      }
    }
  }

  async addSinglePageConstraint(filePath) {
    const content = await fs.readFile(filePath, 'utf8');

    if (!content.includes('min-height: 100vh')) {
      const updatedContent = this.addCSSRule(content, 'min-height: 100vh');
      await fs.writeFile(filePath, updatedContent);
    }
  }
}
```

---

## PART IX: FINAL VALIDATION AND DEPLOYMENT

### 9.1 Pre-Deployment Checklist

#### Complete Validation Pipeline
```bash
#!/bin/bash
# pre-deployment-validation.sh

echo "🚀 Starting Pre-Deployment Validation..."

# Phase 1: Layout Validation
echo "📐 Validating layouts..."
npm run validate:layout:frontmatter
npm run validate:layout:chapters
npm run validate:pagebreaks

# Phase 2: Technical Validation
echo "🔧 Validating technical requirements..."
npm run validate:fonts
npm run validate:css
npm run validate:template

# Phase 3: Content Validation
echo "📖 Validating content..."
npm run validate:content
npm run validate:links
npm run validate:images

# Phase 4: Commercial Validation
echo "💼 Validating commercial readiness..."
npm run validate:print-compatibility
npm run validate:platform-compatibility
npm run validate:accessibility

# Phase 5: Final EPUB Generation
echo "📚 Generating final EPUB..."
npm run build:production

# Phase 6: Final Validation
echo "✅ Final validation..."
npm run validate:final-epub

echo "🎉 Pre-deployment validation complete!"
```

#### Commercial Distribution Validation
```yaml
final_validation_checklist:
  layout_compliance:
    - frontmatter_single_page: "✅ All 7 files single-page compliant"
    - chapter_structure: "✅ All 16 chapters 6-section structure"
    - forced_pagebreaks: "✅ Quiz/worksheet/closing forced breaks"
    - template_compliance: "✅ Exact template implementation"

  technical_compliance:
    - font_loading: "✅ All 6 fonts loading correctly"
    - css_validation: "✅ All classes properly defined"
    - epub_validation: "✅ EPUBCheck zero errors"
    - accessibility: "✅ WCAG 2.1 AA compliant"

  commercial_readiness:
    - amazon_kindle: "✅ Compatible"
    - apple_books: "✅ Compatible"
    - google_play: "✅ Compatible"
    - print_on_demand: "✅ 300 DPI images, proper breaks"
    - file_size: "✅ Under platform limits"
```

### 9.2 Deployment Commands

#### Final Production Build
```bash
# Execute complete SDD/TDD production pipeline
npm run build:sdd-tdd-production

# Generate commercial distribution files
npm run generate:distribution-package

# Validate final outputs
npm run validate:commercial-package

# Deploy to distribution folder
npm run deploy:commercial-ready
```

---

## PART X: CONCLUSION AND MAINTENANCE

### 10.1 Implementation Summary

**✅ COMPREHENSIVE VALIDATION FRAMEWORK READY**

This enhanced PDR v3.0 provides:

- **Granular Layout Validation**: Every file type validated for specific requirements
- **SDD Integration**: GitHub Spec Kit methodology with specifications, plans, and tasks
- **TDD Framework**: Comprehensive test-driven development for EPUB production
- **Commercial Readiness**: Validation for online platforms and print-on-demand
- **Automated Pipeline**: Complete build and validation automation

### 10.2 Immediate Next Steps

1. **Execute SDD/TDD Setup**: `npm run setup:sdd-tdd-framework`
2. **Run Complete Validation**: `npm run qa:commercial-ready`
3. **Generate Production EPUB**: `npm run build:sdd-tdd-production`
4. **Validate Commercial Readiness**: `npm run validate:commercial-package`

### 10.3 Maintenance and Updates

#### Continuous Validation
```yaml
maintenance_schedule:
  daily: "layout_validation_checks"
  weekly: "font_and_css_validation"
  monthly: "platform_compatibility_updates"
  quarterly: "sdd_specification_reviews"
```

#### Future Enhancements
- Advanced accessibility features
- Enhanced print-on-demand optimization
- Additional platform compatibility
- Performance optimization improvements

---

**Document Version**: 3.0.0 - Detailed SDD/TDD Integration
**Last Updated**: September 28, 2025
**Status**: Production Ready with Comprehensive Validation ✅
**Next Review**: October 28, 2025

---

## APPENDICES

### Appendix A: Complete File Structure Validation Matrix
[Detailed validation requirements for all 45 files]

### Appendix B: SDD Specification Templates
[Complete YAML specifications for all file types]

### Appendix C: TDD Test Implementation Guide
[Comprehensive test patterns and validation functions]

### Appendix D: Commercial Distribution Checklist
[Platform-specific requirements and validation criteria]

### Appendix E: Troubleshooting and Error Resolution Guide
[Common issues, causes, and automated solutions]

<function_calls>
<invoke name="TodoWrite">
<parameter name="todos">[{"content": "Create detailed SDD specifications for each file type (frontmatter, chapters, backmatter)", "status": "completed", "activeForm": "Creating detailed SDD specifications"}, {"content": "Design granular TDD validation framework for layout requirements", "status": "completed", "activeForm": "Designing granular TDD validation framework"}, {"content": "Write comprehensive PDR with SDD/TDD integration and detailed validations", "status": "in_progress", "activeForm": "Writing comprehensive PDR"}, {"content": "Deploy enhanced PDR to output folder on main branch", "status": "pending", "activeForm": "Deploying enhanced PDR to main branch"}]