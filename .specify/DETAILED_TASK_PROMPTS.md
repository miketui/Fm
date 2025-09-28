# DETAILED PROMPTS FOR ALL 36 SDD/TDD IMPLEMENTATION TASKS

**Complete Execution Guide for GitHub Spec Kit SDD/TDD Framework**
**Total Tasks**: 36 tasks across 6 categories
**Estimated Time**: 6 hours
**Constitutional Compliance**: All Articles (I, III, IV, V)

---

## CATEGORY A: TDD INFRASTRUCTURE SETUP ✅ COMPLETED
*Status: Already completed during setup phase*

---

## CATEGORY B: FRONTMATTER VALIDATION (6 tasks - 60 minutes)

### TASK B1: RED Phase - Write Failing Frontmatter Tests (20 minutes)

**EXACT PROMPT FOR CLAUDE CODE:**
```
CONTEXT: I am implementing GitHub Spec Kit SDD with TDD methodology for EPUB validation. I need to follow Constitutional Article III (Test-First Imperative) which requires Red-Green-Refactor cycles. I have TDD infrastructure set up with Jest and need to start with the RED phase for frontmatter validation.

TASK: Create failing tests for all 7 frontmatter files following TDD RED phase requirements:

FILES TO TEST:
- 1-TitlePage.xhtml
- 2-Copyright.xhtml
- 3-TableOfContents.xhtml
- 4-Dedication.xhtml
- 5-SelfAssessment.xhtml
- 6-affirmation-odyssey.xhtml
- 7-Preface.xhtml

CONSTITUTIONAL REQUIREMENTS TO TEST:
- Article I: Layout-First Principle - min-height: 100vh constraint
- Article I: No content overflow beyond viewport boundaries
- Article I: page-break-inside: avoid constraint
- Article I: Visual consistency across all frontmatter files

IMPLEMENTATION STEPS:
1. Create test file: tests/tdd/unit/frontmatter-validator.test.js
2. Write tests that validate Constitutional Article I requirements
3. Use global.FRONTMATTER_FILES array from TDD setup
4. Ensure all tests FAIL initially (RED phase requirement)
5. Test structure should validate each file individually
6. Include tests for single-page viewport constraints

TEST STRUCTURE TEMPLATE:
```javascript
describe('Frontmatter Single-Page Validation - Constitutional Article I', () => {
  const frontmatterFiles = global.FRONTMATTER_FILES;

  frontmatterFiles.forEach(file => {
    describe(`${file} validation`, () => {
      test('should have min-height: 100vh constraint', () => {
        // This test should FAIL initially
        expect(validator.hasMinHeightConstraint(file)).toBe(true);
      });

      test('should fit content within viewport', () => {
        // This test should FAIL initially
        expect(validator.contentFitsViewport(file)).toBe(true);
      });
    });
  });
});
```

VERIFICATION STEPS:
1. Run: npm run test:tdd -- tests/tdd/unit/frontmatter-validator.test.js
2. Verify all tests FAIL (RED phase confirmation)
3. Document failure reasons for GREEN phase implementation

SUCCESS CRITERIA:
- All 7 frontmatter files have corresponding tests
- All tests fail when executed (RED phase requirement)
- Tests validate Constitutional Article I requirements
- Test output clearly shows missing validator implementation

NEXT STEP: Task B2 (GREEN phase implementation)
```

---

### TASK B2: GREEN Phase - Implement Base Validation Classes (25 minutes)

**EXACT PROMPT FOR CLAUDE CODE:**
```
CONTEXT: I have failing tests for frontmatter validation from Task B1. Now I need to implement the GREEN phase of TDD - creating minimum implementation to make tests pass while following Constitutional Article III requirements.

TASK: Implement minimum validation classes to make frontmatter tests pass:

REQUIRED CLASSES TO CREATE:
1. scripts/validators/BaseLayoutValidator.js - Base class with common functionality
2. scripts/tdd/FrontmatterValidator.js - Frontmatter-specific validation
3. tests/tdd/utils/XHTMLParser.js - Utility for parsing XHTML files

CONSTITUTIONAL COMPLIANCE:
- Article III: Implement minimum code to pass tests (no over-engineering)
- Article I: Validate Layout-First Principle requirements
- Article II: Ensure validation-driven development approach

IMPLEMENTATION REQUIREMENTS:

BaseLayoutValidator class should include:
- readXHTMLFile(filename) method
- extractCSSConstraints(content) method
- calculateContentHeight(content) method
- Base error handling and logging

FrontmatterValidator class should include:
- hasMinHeightConstraint(filename) method
- contentFitsViewport(filename) method
- hasPageBreakAvoid(filename) method
- Extends BaseLayoutValidator

IMPLEMENTATION TEMPLATE:
```javascript
// scripts/validators/BaseLayoutValidator.js
const fs = require('fs');
const path = require('path');

class BaseLayoutValidator {
  readXHTMLFile(filename) {
    const filePath = path.join(process.cwd(), 'output', 'OEBPS', 'text', filename);
    if (!fs.existsSync(filePath)) {
      throw new Error(`XHTML file not found: ${filename}`);
    }
    return fs.readFileSync(filePath, 'utf8');
  }

  extractCSSConstraints(content) {
    // Implement CSS parsing logic
  }

  calculateContentHeight(content) {
    // Implement content height calculation
  }
}

module.exports = BaseLayoutValidator;
```

VERIFICATION STEPS:
1. Implement classes with minimum functionality
2. Run: npm run test:tdd -- tests/tdd/unit/frontmatter-validator.test.js
3. Verify all tests PASS (GREEN phase confirmation)
4. Ensure no test modifications during implementation

SUCCESS CRITERIA:
- All frontmatter tests pass when executed
- Minimum implementation approach (no over-engineering)
- Base classes are reusable for other validators
- Code follows constitutional principles

NEXT STEP: Task B3 (REFACTOR phase optimization)
```

---

### TASK B3: REFACTOR Phase - Optimize Frontmatter Validation (15 minutes)

**EXACT PROMPT FOR CLAUDE CODE:**
```
CONTEXT: I have working frontmatter validation that passes all tests from Task B2. Now I need to implement the REFACTOR phase of TDD - optimizing the implementation while maintaining test success, following Constitutional Article III.

TASK: Optimize frontmatter validation implementation while maintaining test success:

REFACTORING OBJECTIVES:
- Extract common file reading logic to utilities
- Implement caching for repeated file access
- Optimize CSS parsing performance
- Improve error handling and logging
- Add performance metrics tracking
- Ensure all tests continue to pass

CONSTITUTIONAL COMPLIANCE:
- Article III: REFACTOR phase - optimize while maintaining tests
- Article II: Improve validation performance and reliability
- Article I: Maintain Layout-First Principle compliance

OPTIMIZATION AREAS:
1. File I/O optimization with caching
2. CSS parsing performance improvements
3. Error handling enhancement
4. Code organization and readability
5. Documentation and comments
6. Performance metrics implementation

REFACTORING STEPS:
1. Run tests before refactoring: npm run test:tdd -- tests/tdd/unit/frontmatter-validator.test.js
2. Apply optimizations incrementally
3. Run tests after each optimization to ensure no regression
4. Add performance monitoring
5. Improve code documentation
6. Run linting: npm run lint

PERFORMANCE TARGETS:
- File reading operations: under 100ms per file
- Complete frontmatter validation: under 5 seconds
- Memory usage: optimized for repeated validations
- Error messages: clear and actionable

VERIFICATION STEPS:
1. All tests continue to pass during refactoring
2. Performance metrics show improvement
3. Code quality enhanced (linting passes)
4. No functional changes to behavior
5. Documentation updated appropriately

SUCCESS CRITERIA:
- All tests pass after refactoring
- Measurable performance improvements
- Enhanced code quality and maintainability
- Ready for reuse in other validators

NEXT STEP: Task C1 (Chapter structure RED phase)
```

---

## CATEGORY C: CHAPTER STRUCTURE VALIDATION (9 tasks - 90 minutes)

### TASK C1: RED Phase - Write Failing Chapter Structure Tests (30 minutes)

**EXACT PROMPT FOR CLAUDE CODE:**
```
CONTEXT: Frontmatter validation is complete. Now I need to implement chapter structure validation following Constitutional Article I (6-section structure requirement) and Article III (TDD methodology). I need to start with RED phase for all 16 chapter files.

TASK: Create comprehensive failing tests for all 16 chapter files with 6-section structure validation:

CHAPTER FILES TO TEST (16 files):
- 9-chapter-i-unveiling-your-creative-odyssey.xhtml
- 10-chapter-ii-refining-your-creative-toolkit.xhtml
- 11-chapter-iii-reigniting-your-creative-fire.xhtml
- 13-chapter-iv-the-art-of-networking-in-freelance-hairstyling.xhtml
- 14-chapter-v-cultivating-creative-excellence-through-mentorship.xhtml
- 15-chapter-vi-mastering-the-business-of-hairstyling.xhtml
- 16-chapter-vii-embracing-wellness-and-self-care.xhtml
- 17-chapter-viii-advancing-skills-through-continuous-education.xhtml
- 19-chapter-ix-stepping-into-leadership.xhtml
- 20-chapter-x-crafting-enduring-legacies.xhtml
- 21-chapter-xi-advanced-digital-strategies-for-freelance-hairstylists.xhtml
- 22-chapter-xii-financial-wisdom-building-sustainable-ventures.xhtml
- 23-chapter-xiii-embracing-ethics-and-sustainability-in-hairstyling.xhtml
- 25-chapter-xiv-the-impact-of-ai-on-the-beauty-industry.xhtml
- 26-chapter-xv-cultivating-resilience-and-well-being-in-hairstyling.xhtml
- 27-chapter-xvi-tresses-and-textures-embracing-diversity-in-hairstyling.xhtml

CONSTITUTIONAL REQUIREMENTS TO TEST:
- Article I: 6-section structure mandatory
- Article I: Forced page breaks (quiz, worksheet, closing image)
- Article I: Single-page constraints for quiz and worksheet sections
- Article I: Template compliance with provided structure

6-SECTION STRUCTURE TO VALIDATE:
1. Section 1: Title page (chap-title class)
2. Section 2: Content body (chap-body class)
3. Section 3: Endnotes (endnotes class)
4. Section 4: Quiz (quiz-container class, page-break-before: always)
5. Section 5: Worksheet (worksheet class, page-break-before: always)
6. Section 6: Closing image (image-quote class, page-break-before: always)

SPECIFIC VALIDATION REQUIREMENTS:
- Quiz section: exactly 4 questions, max-height: 90vh
- Worksheet section: avoid-break class, max-height: 90vh
- Closing image: centered layout, responsive sizing
- Forced page breaks before sections 4, 5, and 6

IMPLEMENTATION STEPS:
1. Create test file: tests/tdd/unit/chapter-structure-validator.test.js
2. Use global.CHAPTER_FILES array from TDD setup
3. Write comprehensive tests for each validation requirement
4. Ensure all tests FAIL initially (RED phase requirement)
5. Include template compliance validation

TEST STRUCTURE TEMPLATE:
```javascript
describe('Chapter Structure Validation - Constitutional Article I', () => {
  const chapterFiles = global.CHAPTER_FILES;

  describe('6-Section Structure Tests', () => {
    chapterFiles.forEach(file => {
      test(`${file} should have exactly 6 sections`, () => {
        expect(validator.getSectionCount(file)).toBe(6);
      });
    });
  });

  describe('Forced Page Break Tests', () => {
    chapterFiles.forEach(file => {
      test(`${file} should have forced page breaks in quiz, worksheet, closing`, () => {
        expect(validator.hasQuizPageBreak(file)).toBe(true);
        expect(validator.hasWorksheetPageBreak(file)).toBe(true);
        expect(validator.hasClosingPageBreak(file)).toBe(true);
      });
    });
  });

  describe('Single-Page Section Tests', () => {
    chapterFiles.forEach(file => {
      test(`${file} quiz should fit single page with 4 questions`, () => {
        expect(validator.quizFitsSinglePage(file)).toBe(true);
        expect(validator.getQuizQuestionCount(file)).toBe(4);
      });
    });
  });
});
```

VERIFICATION STEPS:
1. Run: npm run test:tdd -- tests/tdd/unit/chapter-structure-validator.test.js
2. Verify all tests FAIL (RED phase confirmation)
3. Document specific failure reasons for GREEN phase

SUCCESS CRITERIA:
- Tests cover all 16 chapter files
- All tests fail when executed (RED phase requirement)
- Tests validate 6-section structure requirements
- Tests validate forced page break requirements
- Tests validate single-page section constraints

NEXT STEP: Task C2 (GREEN phase implementation)
```

---

### TASK C2: GREEN Phase - Implement Chapter Structure Validation (40 minutes)

**EXACT PROMPT FOR CLAUDE CODE:**
```
CONTEXT: I have comprehensive failing tests for chapter structure validation from Task C1. Now I need to implement GREEN phase - creating minimum implementation to make all chapter tests pass while following Constitutional Article III and Article I requirements.

TASK: Implement chapter structure validation classes to make all tests pass:

REQUIRED CLASSES TO CREATE:
1. scripts/tdd/ChapterStructureValidator.js - Chapter-specific validation
2. scripts/validators/SectionParser.js - Utility for parsing chapter sections

CONSTITUTIONAL COMPLIANCE:
- Article III: Implement minimum code to pass tests (GREEN phase)
- Article I: Validate 6-section structure (Layout-First Principle)
- Article I: Enforce forced page breaks and single-page constraints

IMPLEMENTATION REQUIREMENTS:

ChapterStructureValidator should include:
- getSectionCount(filename) - Returns number of sections
- hasQuizPageBreak(filename) - Validates quiz page break
- hasWorksheetPageBreak(filename) - Validates worksheet page break
- hasClosingPageBreak(filename) - Validates closing image page break
- quizFitsSinglePage(filename) - Validates quiz single-page constraint
- getQuizQuestionCount(filename) - Returns exact question count
- worksheetFitsSinglePage(filename) - Validates worksheet constraint
- validateTemplateCompliance(filename) - Checks template structure

SECTION DETECTION LOGIC:
- Section 1: class="chap-title" or role="doc-part"
- Section 2: class="chap-body" or role="doc-chapter"
- Section 3: class="endnotes" or role="doc-endnotes"
- Section 4: class="quiz-container" with page-break-before
- Section 5: class="worksheet" with page-break-before
- Section 6: class="image-quote" with page-break-before

IMPLEMENTATION TEMPLATE:
```javascript
// scripts/tdd/ChapterStructureValidator.js
const BaseLayoutValidator = require('../validators/BaseLayoutValidator');

class ChapterStructureValidator extends BaseLayoutValidator {
  getSectionCount(filename) {
    const content = this.readXHTMLFile(filename);
    const sections = this.extractSections(content);
    return sections.length;
  }

  extractSections(content) {
    const sectionIdentifiers = [
      'chap-title', 'chap-body', 'endnotes',
      'quiz-container', 'worksheet', 'image-quote'
    ];

    const foundSections = [];
    sectionIdentifiers.forEach(identifier => {
      if (content.includes(identifier)) {
        foundSections.push(identifier);
      }
    });

    return foundSections;
  }

  hasQuizPageBreak(filename) {
    const content = this.readXHTMLFile(filename);
    return content.includes('quiz-container') &&
           content.includes('page-break-before');
  }

  getQuizQuestionCount(filename) {
    const content = this.readXHTMLFile(filename);
    const quizSection = this.extractQuizSection(content);
    const questions = quizSection.match(/<li.*class="quiz-q"/g) || [];
    return questions.length;
  }
}

module.exports = ChapterStructureValidator;
```

VERIFICATION STEPS:
1. Implement all required methods with minimum functionality
2. Run: npm run test:tdd -- tests/tdd/unit/chapter-structure-validator.test.js
3. Verify all tests PASS (GREEN phase confirmation)
4. Test against all 16 chapter files
5. Ensure no test modifications during implementation

SUCCESS CRITERIA:
- All chapter structure tests pass when executed
- Validation works for all 16 chapter files
- 6-section structure properly detected
- Forced page breaks correctly validated
- Quiz and worksheet constraints verified
- Minimum implementation approach maintained

NEXT STEP: Task C3 (REFACTOR phase optimization)
```

---

### TASK C3: REFACTOR Phase - Optimize Chapter Validation Performance (20 minutes)

**EXACT PROMPT FOR CLAUDE CODE:**
```
CONTEXT: I have working chapter structure validation that passes all tests from Task C2. Now I need to implement REFACTOR phase - optimizing for performance and maintainability while keeping all tests passing, following Constitutional Article III.

TASK: Optimize chapter validation for performance and code quality:

REFACTORING OBJECTIVES:
- Implement parallel chapter validation (16 files)
- Add validation result caching
- Optimize DOM parsing operations
- Improve error reporting granularity
- Add performance monitoring
- Enhance code organization

CONSTITUTIONAL COMPLIANCE:
- Article III: REFACTOR phase - optimize while maintaining tests
- Article I: Maintain 6-section structure validation accuracy
- Article II: Improve validation-driven development performance

PERFORMANCE TARGETS:
- All 16 chapters validated in under 30 seconds
- Parallel processing for independent validations
- Caching for repeated file access
- Optimized memory usage for large chapter files

OPTIMIZATION AREAS:
1. Parallel Processing Implementation:
   - Use Promise.all() for concurrent chapter validation
   - Implement worker threads for CPU-intensive parsing
   - Add progress tracking for long-running validations

2. Caching Strategy:
   - Cache parsed chapter content
   - Cache section extraction results
   - Implement intelligent cache invalidation

3. Performance Monitoring:
   - Add timing metrics for each validation step
   - Track memory usage during validation
   - Generate performance reports

4. Error Handling Enhancement:
   - Provide specific error messages for each section
   - Add context about which part of template is missing
   - Include suggestions for fixing validation failures

IMPLEMENTATION STEPS:
1. Run tests before refactoring to establish baseline
2. Implement parallel validation for all 16 chapters
3. Add caching layer for repeated operations
4. Optimize section parsing and detection
5. Add comprehensive performance monitoring
6. Enhance error messages and reporting
7. Run tests after each optimization
8. Verify performance improvements

REFACTORING TEMPLATE:
```javascript
class OptimizedChapterStructureValidator extends ChapterStructureValidator {
  constructor() {
    super();
    this.cache = new Map();
    this.performanceMetrics = {
      validationTimes: [],
      cacheHits: 0,
      cacheMisses: 0
    };
  }

  async validateAllChapters() {
    const chapterFiles = global.CHAPTER_FILES;
    const startTime = Date.now();

    // Parallel validation for better performance
    const validationPromises = chapterFiles.map(file =>
      this.validateChapterWithCaching(file)
    );

    const results = await Promise.all(validationPromises);

    this.performanceMetrics.totalTime = Date.now() - startTime;
    return this.generatePerformanceReport(results);
  }

  validateChapterWithCaching(filename) {
    // Check cache first
    if (this.cache.has(filename)) {
      this.performanceMetrics.cacheHits++;
      return this.cache.get(filename);
    }

    // Perform validation and cache result
    const result = this.validateChapter(filename);
    this.cache.set(filename, result);
    this.performanceMetrics.cacheMisses++;
    return result;
  }
}
```

VERIFICATION STEPS:
1. All tests continue to pass during refactoring
2. Performance targets met (16 chapters under 30 seconds)
3. Cache hit ratio above 50% for repeated validations
4. Memory usage optimized and monitored
5. Error messages more informative and actionable

SUCCESS CRITERIA:
- All chapter tests pass after optimization
- Significant performance improvement demonstrated
- Code quality and maintainability enhanced
- Performance monitoring and reporting implemented
- Ready for integration with master validator

NEXT STEP: Task D1 (Backmatter validation RED phase)
```

---

## CATEGORY D: BACKMATTER VALIDATION (6 tasks - 60 minutes)

### TASK D1: RED Phase - Write Failing Backmatter Tests (20 minutes)

**EXACT PROMPT FOR CLAUDE CODE:**
```
CONTEXT: Chapter validation is complete. Now I need to implement backmatter validation for all 17 backmatter files. These files include journals, worksheets, reference materials, and assessments that require single-page validation like frontmatter PLUS specialized layout validation. Following Constitutional Article III (TDD) and Article I (Layout-First).

TASK: Create comprehensive failing tests for all 17 backmatter files with specialized layout validation:

BACKMATTER FILES TO TEST (17 files):
- 28-Conclusion.xhtml [Reference Layout]
- 29QuizKey.xhtml [Assessment Layout]
- 30-SelfAssessment.xhtml [Assessment Layout]
- 31-affirmations-close.xhtml [Inspirational Layout]
- 32-continued-learning-commitment.xhtml [Inspirational Layout]
- 33-Acknowledgments.xhtml [Reference Layout]
- 34-AbouttheAuthor.xhtml [Reference Layout]
- 35-CurlsContempCollective.xhtml [Inspirational Layout]
- 36-JournalingStart.xhtml [Journal Layout]
- 37-ManifestingJournal.xhtml [Journal Layout]
- 38-journal-page.xhtml [Journal Layout]
- 39-professional-development.xhtml [Worksheet Layout]
- 40-SMARTGoals.xhtml [Worksheet Layout]
- 41-self-care-journal.xhtml [Journal Layout]
- 42-VisionJournal.xhtml [Journal Layout]
- 43-DoodlePage.xhtml [Worksheet Layout]
- 44-bibliography.xhtml [Reference Layout]

CONSTITUTIONAL REQUIREMENTS TO TEST:
- Article I: Single-page constraints (min-height: 100vh) for ALL backmatter files
- Article I: No content overflow beyond viewport boundaries
- Article I: Specialized layouts for different content types

SPECIALIZED LAYOUT CATEGORIES:

1. JOURNAL FILES (5 files): 36, 37, 38, 41, 42
   - Ruled paper backgrounds
   - Interactive writing areas
   - Guided prompts and questions
   - Single-page interactive layout

2. WORKSHEET FILES (3 files): 39, 40, 43
   - Form fields and completion areas
   - Activity sections
   - Instructions and guidance
   - Single-page worksheet layout

3. REFERENCE FILES (4 files): 28, 33, 34, 44
   - Clean text formatting
   - Proper typography
   - Readable presentation
   - Single-page text content

4. ASSESSMENT FILES (2 files): 29, 30
   - Answer keys and scoring
   - Assessment questions
   - Reference formatting

5. INSPIRATIONAL FILES (3 files): 31, 32, 35
   - Affirmations and commitments
   - Centered content layout
   - Motivational formatting

IMPLEMENTATION STEPS:
1. Create test file: tests/tdd/unit/backmatter-validator.test.js
2. Use global.BACKMATTER_FILES array from TDD setup
3. Write universal single-page tests (same as frontmatter)
4. Write specialized layout tests for each content type
5. Ensure all tests FAIL initially (RED phase requirement)

TEST STRUCTURE TEMPLATE:
```javascript
describe('Backmatter Single-Page + Specialized Layout Validation', () => {
  const backmatterFiles = global.BACKMATTER_FILES;

  describe('Universal Single-Page Constraints', () => {
    backmatterFiles.forEach(file => {
      test(`${file} should have min-height: 100vh constraint`, () => {
        expect(validator.hasMinHeightConstraint(file)).toBe(true);
      });

      test(`${file} should fit content within viewport`, () => {
        expect(validator.contentFitsViewport(file)).toBe(true);
      });
    });
  });

  describe('Journal Files Specialized Validation', () => {
    const journalFiles = [
      '36-JournalingStart.xhtml', '37-ManifestingJournal.xhtml',
      '38-journal-page.xhtml', '41-self-care-journal.xhtml', '42-VisionJournal.xhtml'
    ];

    journalFiles.forEach(file => {
      test(`${file} should have journal layout with writing areas`, () => {
        expect(validator.hasJournalLayout(file)).toBe(true);
      });

      test(`${file} should have ruled paper background`, () => {
        expect(validator.hasRuledPaperBackground(file)).toBe(true);
      });
    });
  });

  describe('Worksheet Files Specialized Validation', () => {
    const worksheetFiles = [
      '39-professional-development.xhtml', '40-SMARTGoals.xhtml', '43-DoodlePage.xhtml'
    ];

    worksheetFiles.forEach(file => {
      test(`${file} should have worksheet layout with form fields`, () => {
        expect(validator.hasWorksheetLayout(file)).toBe(true);
      });
    });
  });
});
```

VERIFICATION STEPS:
1. Run: npm run test:tdd -- tests/tdd/unit/backmatter-validator.test.js
2. Verify all tests FAIL (RED phase confirmation)
3. Document failure reasons for each specialized layout type

SUCCESS CRITERIA:
- Tests cover all 17 backmatter files
- Universal single-page tests for all files
- Specialized layout tests for each content type
- All tests fail when executed (RED phase requirement)
- Clear test organization by content type

NEXT STEP: Task D2 (GREEN phase implementation)
```

---

### TASK D2: GREEN Phase - Implement Backmatter Validation Classes (25 minutes)

**EXACT PROMPT FOR CLAUDE CODE:**
```
CONTEXT: I have comprehensive failing tests for backmatter validation from Task D1. Now I need to implement GREEN phase - creating minimum implementation to make all backmatter tests pass. This includes universal single-page validation PLUS specialized validation for journals, worksheets, reference materials, assessments, and inspirational content.

TASK: Implement backmatter validation classes to make all tests pass:

REQUIRED CLASSES TO CREATE:
1. scripts/tdd/BackmatterValidator.js - Main backmatter validation
2. scripts/validators/JournalLayoutValidator.js - Journal-specific validation
3. scripts/validators/WorksheetLayoutValidator.js - Worksheet-specific validation

CONSTITUTIONAL COMPLIANCE:
- Article III: Implement minimum code to pass tests (GREEN phase)
- Article I: Validate single-page constraints for all 17 files
- Article I: Validate specialized layouts for different content types

IMPLEMENTATION REQUIREMENTS:

BackmatterValidator should include:
Universal single-page methods (same as frontmatter):
- hasMinHeightConstraint(filename)
- contentFitsViewport(filename)
- hasPageBreakAvoid(filename)

Specialized layout methods:
- hasJournalLayout(filename) - For journal files
- hasRuledPaperBackground(filename) - For journal files
- hasWorksheetLayout(filename) - For worksheet files
- hasFormFields(filename) - For worksheet files
- hasReferenceLayout(filename) - For reference files
- hasAssessmentLayout(filename) - For assessment files
- hasInspirationalLayout(filename) - For inspirational files

CONTENT TYPE DETECTION LOGIC:

Journal Files (5 files): 36, 37, 38, 41, 42
- Look for: "journal", "ruled-paper-bg", "writing-area", "journal-prompt"
- CSS classes: .journal, .ruled-paper-bg, .writing-area

Worksheet Files (3 files): 39, 40, 43
- Look for: "worksheet", "form-field", "activity-section", "completion-area"
- CSS classes: .worksheet, .form-field, .activity-section

Reference Files (4 files): 28, 33, 34, 44
- Look for: clean text formatting, proper typography
- CSS classes: .conclusion, .acknowledgments, .author-bio, .bibliography

Assessment Files (2 files): 29, 30
- Look for: "quiz-key", "assessment", "answer-reference"
- CSS classes: .quiz-key, .assessment

Inspirational Files (3 files): 31, 32, 35
- Look for: "affirmations", "commitment", "collective-info"
- CSS classes: .affirmations, .commitment

IMPLEMENTATION TEMPLATE:
```javascript
// scripts/tdd/BackmatterValidator.js
const BaseLayoutValidator = require('../validators/BaseLayoutValidator');

class BackmatterValidator extends BaseLayoutValidator {
  // Universal single-page validation (inherit from frontmatter approach)
  hasMinHeightConstraint(filename) {
    const content = this.readXHTMLFile(filename);
    return content.includes('min-height: 100vh');
  }

  contentFitsViewport(filename) {
    const metrics = this.calculateContentMetrics(filename);
    return metrics.contentHeight <= metrics.viewportHeight;
  }

  // Journal-specific validation
  hasJournalLayout(filename) {
    const content = this.readXHTMLFile(filename);
    return content.includes('journal') ||
           content.includes('ruled-paper-bg') ||
           content.includes('writing-area');
  }

  hasRuledPaperBackground(filename) {
    const content = this.readXHTMLFile(filename);
    return content.includes('ruled-paper-bg') ||
           content.includes('journal-prompt');
  }

  // Worksheet-specific validation
  hasWorksheetLayout(filename) {
    const content = this.readXHTMLFile(filename);
    return content.includes('worksheet') ||
           content.includes('activity-section') ||
           content.includes('form-field');
  }

  hasFormFields(filename) {
    const content = this.readXHTMLFile(filename);
    return content.includes('form-field') ||
           content.includes('completion-area');
  }

  // Content type detection by filename
  getBackmatterContentType(filename) {
    const journalFiles = ['36-', '37-', '38-', '41-', '42-'];
    const worksheetFiles = ['39-', '40-', '43-'];
    const referenceFiles = ['28-', '33-', '34-', '44-'];
    const assessmentFiles = ['29', '30-'];
    const inspirationalFiles = ['31-', '32-', '35-'];

    if (journalFiles.some(prefix => filename.startsWith(prefix))) {
      return 'journal';
    }
    if (worksheetFiles.some(prefix => filename.startsWith(prefix))) {
      return 'worksheet';
    }
    if (referenceFiles.some(prefix => filename.startsWith(prefix))) {
      return 'reference';
    }
    if (assessmentFiles.some(prefix => filename.startsWith(prefix))) {
      return 'assessment';
    }
    if (inspirationalFiles.some(prefix => filename.startsWith(prefix))) {
      return 'inspirational';
    }
    return 'unknown';
  }
}

module.exports = BackmatterValidator;
```

VERIFICATION STEPS:
1. Implement all required methods with minimum functionality
2. Run: npm run test:tdd -- tests/tdd/unit/backmatter-validator.test.js
3. Verify all tests PASS (GREEN phase confirmation)
4. Test against all 17 backmatter files
5. Verify each content type validation works correctly

SUCCESS CRITERIA:
- All backmatter tests pass when executed
- Universal single-page validation works for all 17 files
- Specialized layout validation works for each content type
- Journal layout detection working (5 files)
- Worksheet layout detection working (3 files)
- Reference layout detection working (4 files)
- Assessment layout detection working (2 files)
- Inspirational layout detection working (3 files)

NEXT STEP: Task D3 (REFACTOR phase optimization)
```

---

### TASK D3: REFACTOR Phase - Optimize Backmatter Validation (15 minutes)

**EXACT PROMPT FOR CLAUDE CODE:**
```
CONTEXT: I have working backmatter validation that passes all tests from Task D2. Now I need to implement REFACTOR phase - optimizing the implementation for performance and maintainability while maintaining all test success, following Constitutional Article III.

TASK: Optimize backmatter validation for 17 files while maintaining test success:

REFACTORING OBJECTIVES:
- Extract common layout validation logic
- Implement caching for repeated file access (17 files)
- Optimize specialized layout detection
- Improve error handling and logging
- Add performance metrics for all content types
- Enhance code organization and readability

CONSTITUTIONAL COMPLIANCE:
- Article III: REFACTOR phase - optimize while maintaining tests
- Article I: Maintain single-page + specialized layout validation
- Article II: Improve validation performance for large file set

OPTIMIZATION AREAS:

1. Content Type Optimization:
   - Cache content type detection results
   - Optimize CSS class detection
   - Streamline specialized layout validation

2. Performance for 17 Files:
   - Implement parallel validation for all backmatter files
   - Add file-specific caching strategies
   - Optimize memory usage for large content files

3. Error Handling Enhancement:
   - Provide specific error messages for each content type
   - Add context about missing layout elements
   - Include suggestions for fixing validation failures

4. Code Organization:
   - Extract content type validators to separate classes
   - Implement factory pattern for validator creation
   - Add comprehensive documentation

REFACTORING TEMPLATE:
```javascript
class OptimizedBackmatterValidator extends BackmatterValidator {
  constructor() {
    super();
    this.contentTypeCache = new Map();
    this.layoutCache = new Map();
    this.performanceMetrics = {
      validationTimes: {},
      contentTypeDetection: {},
      cacheHitRatio: 0
    };
  }

  async validateAllBackmatter() {
    const backmatterFiles = global.BACKMATTER_FILES;
    const startTime = Date.now();

    // Group files by content type for optimized validation
    const filesByType = this.groupFilesByContentType(backmatterFiles);

    // Parallel validation by content type
    const validationPromises = Object.entries(filesByType).map(([type, files]) =>
      this.validateContentTypeFiles(type, files)
    );

    const results = await Promise.all(validationPromises);

    this.performanceMetrics.totalTime = Date.now() - startTime;
    return this.generateBackmatterReport(results);
  }

  groupFilesByContentType(files) {
    return files.reduce((groups, file) => {
      const type = this.getBackmatterContentType(file);
      if (!groups[type]) groups[type] = [];
      groups[type].push(file);
      return groups;
    }, {});
  }

  async validateContentTypeFiles(contentType, files) {
    const validator = this.getContentTypeValidator(contentType);
    const results = await Promise.all(
      files.map(file => validator.validateFile(file))
    );

    return {
      contentType,
      files: files.length,
      results,
      success: results.every(r => r.valid)
    };
  }

  getContentTypeValidator(contentType) {
    // Factory pattern for content-specific validators
    switch (contentType) {
      case 'journal':
        return new JournalLayoutValidator();
      case 'worksheet':
        return new WorksheetLayoutValidator();
      case 'reference':
        return new ReferenceLayoutValidator();
      case 'assessment':
        return new AssessmentLayoutValidator();
      case 'inspirational':
        return new InspirationalLayoutValidator();
      default:
        return new DefaultBackmatterValidator();
    }
  }
}
```

PERFORMANCE TARGETS:
- All 17 backmatter files validated in under 10 seconds
- Cache hit ratio above 60% for repeated validations
- Memory usage optimized for varied content types
- Error messages specific to each content type

VERIFICATION STEPS:
1. All tests continue to pass during refactoring
2. Performance metrics show improvement
3. Specialized layout validation maintains accuracy
4. Code quality enhanced (linting passes)
5. Documentation updated for all content types

SUCCESS CRITERIA:
- All backmatter tests pass after optimization
- Performance targets met for 17 files
- Code organization improved with content type separation
- Error handling enhanced for specialized layouts
- Ready for integration with master validator

NEXT STEP: Task E1 (Part dividers and navigation validation)
```

---

## CATEGORY E: PART DIVIDERS & NAVIGATION VALIDATION (3 tasks - 30 minutes)

### TASK E1: Part Dividers & Navigation Tests (15 minutes)

**EXACT PROMPT FOR CLAUDE CODE:**
```
CONTEXT: Frontmatter, chapters, and backmatter validation are complete. Now I need to handle the remaining file types: 4 part divider files and 1 navigation file to achieve complete coverage of all 45 XHTML files. Following Constitutional Article I (Layout-First) and Article III (TDD methodology).

TASK: Create failing tests for part divider files and navigation file:

REMAINING FILES TO TEST (5 files):

PART DIVIDER FILES (4 files):
- 8-Part-I-Foundations-of-Creative-Hairstyling.xhtml
- 12-Part-II-Building-Your-Professional-Practice.xhtml
- 18-Part-III-Advanced-Business-Strategies.xhtml
- 24-Part-IV-Future-Focused-Growth.xhtml

NAVIGATION FILE (1 file):
- nav.xhtml

CONSTITUTIONAL REQUIREMENTS TO TEST:
- Article I: Clean divider page layouts for part files
- Article I: EPUB navigation structure for nav.xhtml
- Article I: Consistent styling across all file types
- Article I: Single-page constraints where applicable

VALIDATION REQUIREMENTS:

Part Divider Files:
- Clean divider page layouts
- Consistent styling across all 4 parts
- Proper hierarchy (part title, subtitle, overview)
- Visual separation between book sections
- Single-page layout constraints

Navigation File:
- EPUB navigation structure compliance
- Navigation list with proper hierarchy
- Chapter links functionality
- Accessibility compliance (WCAG 2.1 AA)
- Proper semantic markup

IMPLEMENTATION STEPS:
1. Create test file: tests/tdd/unit/part-dividers-navigation-validator.test.js
2. Use global.PART_DIVIDER_FILES and global.NAVIGATION_FILES arrays
3. Write tests for clean divider layouts
4. Write tests for EPUB navigation compliance
5. Ensure all tests FAIL initially (RED phase requirement)

TEST STRUCTURE TEMPLATE:
```javascript
describe('Part Dividers & Navigation Validation', () => {
  describe('Part Divider Files Validation', () => {
    const partDividerFiles = global.PART_DIVIDER_FILES;

    partDividerFiles.forEach(file => {
      test(`${file} should have clean divider layout`, () => {
        expect(validator.hasCleanDividerLayout(file)).toBe(true);
      });

      test(`${file} should have consistent styling`, () => {
        expect(validator.hasConsistentPartStyling(file)).toBe(true);
      });

      test(`${file} should have proper hierarchy`, () => {
        expect(validator.hasProperPartHierarchy(file)).toBe(true);
      });
    });
  });

  describe('Navigation File Validation', () => {
    const navigationFiles = global.NAVIGATION_FILES;

    navigationFiles.forEach(file => {
      test(`${file} should have EPUB navigation structure`, () => {
        expect(validator.hasEPUBNavigationStructure(file)).toBe(true);
      });

      test(`${file} should have functional chapter links`, () => {
        expect(validator.hasFunctionalChapterLinks(file)).toBe(true);
      });

      test(`${file} should be accessibility compliant`, () => {
        expect(validator.isAccessibilityCompliant(file)).toBe(true);
      });
    });
  });
});
```

VERIFICATION STEPS:
1. Run: npm run test:tdd -- tests/tdd/unit/part-dividers-navigation-validator.test.js
2. Verify all tests FAIL (RED phase confirmation)
3. Document specific requirements for each file type

SUCCESS CRITERIA:
- Tests cover all 4 part divider files
- Tests cover navigation file
- Part divider layout requirements defined
- EPUB navigation requirements defined
- All tests fail when executed (RED phase requirement)

NEXT STEP: Task E2 (Implementation for remaining file types)
```

---

### TASK E2: Implement Part Dividers & Navigation Validation (15 minutes)

**EXACT PROMPT FOR CLAUDE CODE:**
```
CONTEXT: I have failing tests for part dividers and navigation from Task E1. Now I need to implement GREEN phase - creating validation for the remaining 5 files to achieve complete coverage of all 45 XHTML files.

TASK: Implement validation for part dividers and navigation to make all tests pass:

REQUIRED CLASSES TO CREATE:
1. scripts/tdd/PartDividerValidator.js - Part divider validation
2. scripts/tdd/NavigationValidator.js - Navigation file validation

CONSTITUTIONAL COMPLIANCE:
- Article III: Implement minimum code to pass tests (GREEN phase)
- Article I: Complete layout validation for all 45 files
- Article IV: EPUB navigation compliance for commercial distribution

IMPLEMENTATION REQUIREMENTS:

PartDividerValidator should include:
- hasCleanDividerLayout(filename) - Validates clean layout
- hasConsistentPartStyling(filename) - Validates styling consistency
- hasProperPartHierarchy(filename) - Validates content hierarchy
- validatePartElements(filename) - Validates required elements

NavigationValidator should include:
- hasEPUBNavigationStructure(filename) - Validates EPUB nav structure
- hasFunctionalChapterLinks(filename) - Validates link functionality
- isAccessibilityCompliant(filename) - Validates WCAG compliance
- validateNavigationElements(filename) - Validates nav elements

PART DIVIDER VALIDATION LOGIC:
- Look for: "part-divider", "part-title", "part-subtitle"
- CSS classes: .part-divider, .part-title, .part-subtitle
- Elements: part title, chapter range, decorative line, overview text
- Layout: centered content, consistent styling

NAVIGATION VALIDATION LOGIC:
- Look for: navigation elements, chapter links, accessibility labels
- Required elements: <nav>, <ol>, proper heading structure
- EPUB compliance: role="doc-toc", proper linking
- Accessibility: ARIA labels, semantic markup

IMPLEMENTATION TEMPLATE:
```javascript
// scripts/tdd/PartDividerValidator.js
const BaseLayoutValidator = require('../validators/BaseLayoutValidator');

class PartDividerValidator extends BaseLayoutValidator {
  hasCleanDividerLayout(filename) {
    const content = this.readXHTMLFile(filename);
    return content.includes('part') ||
           content.includes('divider') ||
           this.hasPartDividerStructure(content);
  }

  hasConsistentPartStyling(filename) {
    const content = this.readXHTMLFile(filename);
    return content.includes('part-title') ||
           content.includes('part-divider') ||
           this.hasConsistentCSSClasses(content);
  }

  hasProperPartHierarchy(filename) {
    const content = this.readXHTMLFile(filename);
    return this.hasPartTitle(content) &&
           this.hasPartSubtitle(content);
  }

  hasPartDividerStructure(content) {
    const partElements = ['part-title', 'part-subtitle', 'part'];
    return partElements.some(element => content.includes(element));
  }
}

// scripts/tdd/NavigationValidator.js
class NavigationValidator extends BaseLayoutValidator {
  hasEPUBNavigationStructure(filename) {
    const content = this.readXHTMLFile(filename);
    return content.includes('<nav') ||
           content.includes('role="doc-toc"') ||
           content.includes('navigation');
  }

  hasFunctionalChapterLinks(filename) {
    const content = this.readXHTMLFile(filename);
    const links = content.match(/<a\s+href/g) || [];
    return links.length > 0;
  }

  isAccessibilityCompliant(filename) {
    const content = this.readXHTMLFile(filename);
    return content.includes('aria-') ||
           content.includes('role=') ||
           this.hasSemanticMarkup(content);
  }

  hasSemanticMarkup(content) {
    const semanticElements = ['<nav', '<ol', '<ul', 'role='];
    return semanticElements.some(element => content.includes(element));
  }
}

module.exports = { PartDividerValidator, NavigationValidator };
```

FILE TYPE DETECTION:
- Part Dividers: Files 8, 12, 18, 24 (contain "Part-" in filename)
- Navigation: nav.xhtml file
- Consistent styling validation across all 4 part dividers
- EPUB standard compliance for navigation

VERIFICATION STEPS:
1. Implement both validator classes
2. Run: npm run test:tdd -- tests/tdd/unit/part-dividers-navigation-validator.test.js
3. Verify all tests PASS (GREEN phase confirmation)
4. Test coverage for all remaining 5 files
5. Confirm complete coverage of all 45 XHTML files

SUCCESS CRITERIA:
- All part divider and navigation tests pass
- Part divider validation works for all 4 files
- Navigation validation works for nav.xhtml
- EPUB navigation compliance achieved
- Complete file coverage: 7+16+17+4+1 = 45 files

NEXT STEP: Task F1 (Master validation controller for all 45 files)
```

---

## CATEGORY F: COMPLETE INTEGRATION & AUTOMATION (9 tasks - 135 minutes)

### TASK F1: Create Master Validation Controller (30 minutes)

**EXACT PROMPT FOR CLAUDE CODE:**
```
CONTEXT: All individual file type validations are complete (frontmatter, chapters, backmatter, part dividers, navigation). Now I need to create a unified master validation system that orchestrates validation for all 45 XHTML files, following Constitutional Article II (Validation-Driven Development).

TASK: Create comprehensive master validation controller integrating ALL validators:

INTEGRATION SCOPE:
- Frontmatter validation (7 files)
- Chapter structure validation (16 files)
- Backmatter validation (17 files)
- Part divider validation (4 files)
- Navigation validation (1 file)
- TOTAL: 45 files - Complete EPUB coverage

CONSTITUTIONAL COMPLIANCE:
- Article II: Unified validation-driven development system
- Article I: Complete layout validation for all file types
- Article III: TDD methodology integration
- Article IV: Commercial distribution readiness

REQUIRED CLASSES TO CREATE:
1. scripts/MasterLayoutValidator.js - Main orchestration controller
2. scripts/validation-report-generator.js - Comprehensive reporting
3. scripts/constitutional-compliance-checker.js - Article compliance verification

MASTER VALIDATION CONTROLLER REQUIREMENTS:

Core Integration Methods:
- validateAllFiles() - Orchestrates complete EPUB validation
- validateByFileType() - Validates by category (frontmatter, chapters, etc.)
- generateComprehensiveReport() - Creates detailed validation report
- checkConstitutionalCompliance() - Verifies all articles
- isCommercialReady() - Determines production readiness

Performance Requirements:
- Parallel validation where possible
- Progress tracking for all 45 files
- Error aggregation and reporting
- Performance metrics collection
- Memory usage optimization

Reporting Requirements:
- File-by-file validation results
- Category summaries (frontmatter, chapters, backmatter, etc.)
- Constitutional compliance status
- Commercial readiness assessment
- Performance metrics and timing

IMPLEMENTATION TEMPLATE:
```javascript
// scripts/MasterLayoutValidator.js
const FrontmatterValidator = require('./tdd/FrontmatterValidator');
const ChapterStructureValidator = require('./tdd/ChapterStructureValidator');
const BackmatterValidator = require('./tdd/BackmatterValidator');
const { PartDividerValidator, NavigationValidator } = require('./tdd/PartDividerValidator');

class MasterLayoutValidator {
  constructor() {
    this.frontmatterValidator = new FrontmatterValidator();
    this.chapterValidator = new ChapterStructureValidator();
    this.backmatterValidator = new BackmatterValidator();
    this.partDividerValidator = new PartDividerValidator();
    this.navigationValidator = new NavigationValidator();

    this.results = {
      frontmatter: { files: 7, results: [], errors: [] },
      chapters: { files: 16, results: [], errors: [] },
      backmatter: { files: 17, results: [], errors: [] },
      partDividers: { files: 4, results: [], errors: [] },
      navigation: { files: 1, results: [], errors: [] }
    };

    this.performanceMetrics = {
      startTime: null,
      endTime: null,
      totalTime: 0,
      fileValidationTimes: {},
      categoryTimes: {}
    };
  }

  async validateAllFiles() {
    console.log('🚀 Starting Master EPUB Validation for all 45 files...');
    this.performanceMetrics.startTime = Date.now();

    try {
      // Parallel validation by category for optimal performance
      const validationPromises = [
        this.validateFrontmatter(),
        this.validateChapters(),
        this.validateBackmatter(),
        this.validatePartDividers(),
        this.validateNavigation()
      ];

      const results = await Promise.all(validationPromises);

      this.performanceMetrics.endTime = Date.now();
      this.performanceMetrics.totalTime = this.performanceMetrics.endTime - this.performanceMetrics.startTime;

      return this.generateMasterReport(results);
    } catch (error) {
      console.error('❌ Master validation failed:', error.message);
      throw error;
    }
  }

  async validateFrontmatter() {
    const categoryStart = Date.now();
    console.log('📄 Validating frontmatter files (7 files)...');

    const files = global.FRONTMATTER_FILES;
    const results = [];

    for (const file of files) {
      const fileStart = Date.now();
      try {
        const result = await this.frontmatterValidator.validateFile(file);
        results.push({ file, success: true, result });
      } catch (error) {
        results.push({ file, success: false, error: error.message });
      }
      this.performanceMetrics.fileValidationTimes[file] = Date.now() - fileStart;
    }

    this.results.frontmatter.results = results;
    this.performanceMetrics.categoryTimes.frontmatter = Date.now() - categoryStart;

    console.log(`✅ Frontmatter validation complete: ${results.filter(r => r.success).length}/${files.length} passed`);
    return results;
  }

  async validateChapters() {
    const categoryStart = Date.now();
    console.log('📚 Validating chapter files (16 files)...');

    const files = global.CHAPTER_FILES;
    const results = [];

    // Parallel validation for chapters (independent files)
    const chapterPromises = files.map(async (file) => {
      const fileStart = Date.now();
      try {
        const result = await this.chapterValidator.validateChapter(file);
        this.performanceMetrics.fileValidationTimes[file] = Date.now() - fileStart;
        return { file, success: true, result };
      } catch (error) {
        this.performanceMetrics.fileValidationTimes[file] = Date.now() - fileStart;
        return { file, success: false, error: error.message };
      }
    });

    const chapterResults = await Promise.all(chapterPromises);
    this.results.chapters.results = chapterResults;
    this.performanceMetrics.categoryTimes.chapters = Date.now() - categoryStart;

    console.log(`✅ Chapter validation complete: ${chapterResults.filter(r => r.success).length}/${files.length} passed`);
    return chapterResults;
  }

  generateMasterReport(validationResults) {
    const totalFiles = 45;
    const successfulValidations = validationResults.flat().filter(r => r.success).length;

    const report = {
      summary: {
        totalFiles,
        successfulValidations,
        failedValidations: totalFiles - successfulValidations,
        successRate: (successfulValidations / totalFiles * 100).toFixed(2) + '%',
        totalValidationTime: this.performanceMetrics.totalTime + 'ms'
      },
      categoryResults: {
        frontmatter: this.results.frontmatter,
        chapters: this.results.chapters,
        backmatter: this.results.backmatter,
        partDividers: this.results.partDividers,
        navigation: this.results.navigation
      },
      constitutionalCompliance: this.checkConstitutionalCompliance(),
      commercialReadiness: this.assessCommercialReadiness(),
      performanceMetrics: this.performanceMetrics
    };

    return report;
  }

  checkConstitutionalCompliance() {
    return {
      articleI: this.checkArticleI(), // Layout-First Principle
      articleII: this.checkArticleII(), // Validation-Driven Development
      articleIII: this.checkArticleIII(), // Test-First Imperative
      articleIV: this.checkArticleIV(), // Commercial Distribution Readiness
      articleV: this.checkArticleV() // Typography and Styling Standards
    };
  }

  assessCommercialReadiness() {
    const allFilesPassed = this.results.frontmatter.results.every(r => r.success) &&
                          this.results.chapters.results.every(r => r.success) &&
                          this.results.backmatter.results.every(r => r.success) &&
                          this.results.partDividers.results.every(r => r.success) &&
                          this.results.navigation.results.every(r => r.success);

    return {
      ready: allFilesPassed,
      epubCompliance: allFilesPassed,
      platformCompatibility: allFilesPassed ? 'All platforms' : 'Issues detected',
      printReadiness: allFilesPassed ? 'Print-ready' : 'Fixes required'
    };
  }
}

module.exports = MasterLayoutValidator;
```

INTEGRATION VERIFICATION:
1. Create and test MasterLayoutValidator class
2. Verify integration with all 5 validator types
3. Test parallel validation performance
4. Confirm comprehensive reporting
5. Validate constitutional compliance checking

SUCCESS CRITERIA:
- Single command validates all 45 files
- All validator types successfully integrated
- Comprehensive reporting generated
- Performance optimized for large file set
- Constitutional compliance verified
- Commercial readiness assessed

NEXT STEP: Task F2 (Complete package.json integration)
```

---

### TASK F2: Complete Package.json Integration (20 minutes)

**EXACT PROMPT FOR CLAUDE CODE:**
```
CONTEXT: Master validation controller is complete and can validate all 45 files. Now I need to integrate the complete validation system with the build pipeline through npm scripts, following Constitutional Article II (CLI Interface Mandate).

TASK: Update package.json with complete validation scripts for all file types and integration with existing build process:

INTEGRATION REQUIREMENTS:
- Individual validation scripts for each file type
- Master validation script for all 45 files
- TDD testing scripts for all categories
- Build pipeline integration
- Development vs production modes
- Pre-commit hook integration

CONSTITUTIONAL COMPLIANCE:
- Article II: CLI Interface Mandate - all operations via CLI
- Article III: TDD integration with build process
- Article II: Validation-driven development workflow

REQUIRED npm SCRIPTS TO ADD/UPDATE:

Individual File Type Validation:
- validate:layout:frontmatter (7 files)
- validate:layout:chapters (16 files)
- validate:layout:backmatter (17 files)
- validate:layout:part-dividers (4 files)
- validate:layout:navigation (1 file)
- validate:layout:all (45 files)

TDD Testing Scripts:
- test:frontmatter
- test:chapters
- test:backmatter
- test:part-dividers
- test:navigation
- test:all-layouts

Complete Build Pipeline:
- build:sdd-validate (all validation)
- build:sdd-tdd-production (validation + TDD + production)
- build:constitutional-compliance

Development Workflow:
- dev:validate (quick validation)
- dev:test (quick TDD tests)
- dev:watch (file watching for changes)

IMPLEMENTATION STEPS:
1. Read current package.json to understand existing scripts
2. Add new validation scripts without breaking existing ones
3. Create hierarchical script structure (individual -> category -> all)
4. Integrate with existing build:production script
5. Add development convenience scripts
6. Update pre-commit hooks to include validation

PACKAGE.JSON SCRIPT TEMPLATE:
```json
{
  "scripts": {
    // Individual file type validation
    "validate:layout:frontmatter": "node scripts/validate-frontmatter-layouts.js",
    "validate:layout:chapters": "node scripts/validate-chapter-structures.js",
    "validate:layout:backmatter": "node scripts/validate-backmatter-layouts.js",
    "validate:layout:part-dividers": "node scripts/validate-part-dividers.js",
    "validate:layout:navigation": "node scripts/validate-navigation.js",

    // Master validation
    "validate:layout:all": "node scripts/MasterLayoutValidator.js",
    "validate:constitutional": "node scripts/constitutional-compliance-checker.js",

    // TDD testing by category
    "test:frontmatter": "jest --config jest.config.tdd.js --testPathPattern=frontmatter",
    "test:chapters": "jest --config jest.config.tdd.js --testPathPattern=chapter",
    "test:backmatter": "jest --config jest.config.tdd.js --testPathPattern=backmatter",
    "test:part-dividers": "jest --config jest.config.tdd.js --testPathPattern=part-dividers",
    "test:navigation": "jest --config jest.config.tdd.js --testPathPattern=navigation",
    "test:all-layouts": "npm run test:frontmatter && npm run test:chapters && npm run test:backmatter && npm run test:part-dividers && npm run test:navigation",

    // Complete build pipeline
    "build:sdd-validate": "npm run validate:layout:all",
    "build:sdd-tdd": "npm run test:all-layouts && npm run validate:layout:all",
    "build:constitutional-compliance": "npm run validate:constitutional && npm run build:sdd-tdd",
    "build:sdd-tdd-production": "npm run build:constitutional-compliance && npm run build:production",

    // Development workflow
    "dev:validate": "npm run validate:layout:all",
    "dev:test": "npm run test:tdd",
    "dev:quick": "npm run test:tdd && npm run validate:layout:all",
    "dev:watch": "npm run test:tdd:watch",

    // Pre-commit integration
    "pre-commit": "npm run dev:quick && npm run lint"
  }
}
```

SCRIPT IMPLEMENTATION FILES TO CREATE:
1. scripts/validate-frontmatter-layouts.js
2. scripts/validate-chapter-structures.js
3. scripts/validate-backmatter-layouts.js
4. scripts/validate-part-dividers.js
5. scripts/validate-navigation.js
6. scripts/constitutional-compliance-checker.js

Each script should:
- Use the appropriate validator class
- Provide CLI output with progress indicators
- Return appropriate exit codes (0 = success, 1 = failure)
- Generate reports in JSON and human-readable formats
- Support command-line options (--verbose, --json, --fix)

SCRIPT TEMPLATE EXAMPLE:
```javascript
// scripts/validate-frontmatter-layouts.js
const FrontmatterValidator = require('./tdd/FrontmatterValidator');

async function main() {
  console.log('🔍 Validating frontmatter single-page layouts (7 files)...');

  const validator = new FrontmatterValidator();
  const files = global.FRONTMATTER_FILES || [
    '1-TitlePage.xhtml', '2-Copyright.xhtml', '3-TableOfContents.xhtml',
    '4-Dedication.xhtml', '5-SelfAssessment.xhtml',
    '6-affirmation-odyssey.xhtml', '7-Preface.xhtml'
  ];

  let allPassed = true;
  const results = [];

  for (const file of files) {
    try {
      const result = await validator.validateFile(file);
      console.log(`✅ ${file}: PASSED`);
      results.push({ file, status: 'PASSED', result });
    } catch (error) {
      console.log(`❌ ${file}: FAILED - ${error.message}`);
      results.push({ file, status: 'FAILED', error: error.message });
      allPassed = false;
    }
  }

  console.log(`\n📊 Frontmatter Validation Summary:`);
  console.log(`   ✅ Passed: ${results.filter(r => r.status === 'PASSED').length}/7`);
  console.log(`   ❌ Failed: ${results.filter(r => r.status === 'FAILED').length}/7`);

  if (allPassed) {
    console.log(`🎉 All frontmatter files passed validation!`);
    process.exit(0);
  } else {
    console.log(`💥 Some frontmatter files failed validation.`);
    process.exit(1);
  }
}

main().catch(error => {
  console.error('💥 Validation script failed:', error.message);
  process.exit(1);
});
```

VERIFICATION STEPS:
1. Update package.json with all new scripts
2. Create all validation script files
3. Test each script individually
4. Test script combinations and build pipeline
5. Verify integration with existing scripts
6. Test pre-commit hook functionality

SUCCESS CRITERIA:
- All validation scripts execute without errors
- Master validation script works for all 45 files
- TDD testing scripts work for all categories
- Build pipeline integration successful
- Pre-commit hooks prevent invalid commits
- Backward compatibility with existing scripts maintained

NEXT STEP: Task F3 (Constitutional compliance validation)
```

---

### TASK F3: Constitutional Compliance Validation - Complete Coverage (25 minutes)

**EXACT PROMPT FOR CLAUDE CODE:**
```
CONTEXT: Complete validation system is integrated with build pipeline. Now I need to create comprehensive constitutional compliance verification that ensures all 5 constitutional articles are followed across all 45 files, representing the final validation step before production readiness.

TASK: Create comprehensive constitutional compliance validation system:

CONSTITUTIONAL ARTICLES TO VERIFY:

Article I: Layout-First Principle (NON-NEGOTIABLE)
- Frontmatter: Single-page constraints (7 files)
- Chapters: 6-section structure (16 files)
- Backmatter: Single-page + specialized layouts (17 files)
- Part Dividers: Clean layouts (4 files)
- Navigation: EPUB navigation (1 file)
- TOTAL: 45 files compliance

Article II: Validation-Driven Development
- Pre-implementation validation tests exist
- Comprehensive validation pipeline active
- CLI-based validation tools functional
- Validation failures block development progress

Article III: Test-First Imperative (NON-NEGOTIABLE)
- TDD methodology implemented for all file types
- Red-Green-Refactor cycles documented
- 100% test coverage achieved
- All implementations preceded by tests

Article IV: Commercial Distribution Readiness
- Multi-platform compatibility (Kindle, Apple Books, Google Play, Kobo)
- Print-on-demand optimization
- EPUB 3.0 compliance
- WCAG 2.1 AA accessibility standards
- File size optimization

Article V: Typography and Styling Standards
- 6 required fonts loading correctly
- Critical CSS classes properly defined
- Cross-platform compatibility
- Responsive design principles

CONSTITUTIONAL COMPLIANCE IMPLEMENTATION:

REQUIRED FILES TO CREATE:
1. scripts/constitutional-compliance-checker.js - Main compliance validator
2. scripts/constitutional-reporters/article-i-checker.js - Layout compliance
3. scripts/constitutional-reporters/article-ii-checker.js - Validation-driven compliance
4. scripts/constitutional-reporters/article-iii-checker.js - TDD compliance
5. scripts/constitutional-reporters/article-iv-checker.js - Commercial readiness
6. scripts/constitutional-reporters/article-v-checker.js - Typography standards

MAIN CONSTITUTIONAL CHECKER TEMPLATE:
```javascript
// scripts/constitutional-compliance-checker.js
const ArticleIChecker = require('./constitutional-reporters/article-i-checker');
const ArticleIIChecker = require('./constitutional-reporters/article-ii-checker');
const ArticleIIIChecker = require('./constitutional-reporters/article-iii-checker');
const ArticleIVChecker = require('./constitutional-reporters/article-iv-checker');
const ArticleVChecker = require('./constitutional-reporters/article-v-checker');

class ConstitutionalComplianceChecker {
  constructor() {
    this.articleCheckers = {
      I: new ArticleIChecker(),
      II: new ArticleIIChecker(),
      III: new ArticleIIIChecker(),
      IV: new ArticleIVChecker(),
      V: new ArticleVChecker()
    };

    this.complianceResults = {
      overallCompliance: false,
      articlesCompliant: 0,
      articlesTotal: 5,
      violations: [],
      recommendations: []
    };
  }

  async checkCompleteConstitutionalCompliance() {
    console.log('🏛️  Starting Constitutional Compliance Verification...');
    console.log('📋 Verifying all 5 constitutional articles across 45 files...');

    const results = {};
    let allCompliant = true;

    // Check each constitutional article
    for (const [articleNumber, checker] of Object.entries(this.articleCheckers)) {
      console.log(`\n📊 Checking Article ${articleNumber}...`);

      try {
        const articleResult = await checker.checkCompliance();
        results[`article${articleNumber}`] = articleResult;

        if (articleResult.compliant) {
          console.log(`✅ Article ${articleNumber}: COMPLIANT`);
          this.complianceResults.articlesCompliant++;
        } else {
          console.log(`❌ Article ${articleNumber}: NON-COMPLIANT`);
          console.log(`   Violations: ${articleResult.violations.length}`);
          allCompliant = false;
          this.complianceResults.violations.push(...articleResult.violations);
        }
      } catch (error) {
        console.log(`💥 Article ${articleNumber}: ERROR - ${error.message}`);
        allCompliant = false;
        this.complianceResults.violations.push({
          article: articleNumber,
          type: 'SYSTEM_ERROR',
          message: error.message
        });
      }
    }

    this.complianceResults.overallCompliance = allCompliant;

    return this.generateConstitutionalReport(results);
  }

  generateConstitutionalReport(results) {
    const report = {
      timestamp: new Date().toISOString(),
      overallCompliance: this.complianceResults.overallCompliance,
      summary: {
        compliantArticles: this.complianceResults.articlesCompliant,
        totalArticles: this.complianceResults.articlesTotal,
        complianceRate: (this.complianceResults.articlesCompliant / this.complianceResults.articlesTotal * 100).toFixed(1) + '%',
        totalViolations: this.complianceResults.violations.length
      },
      articleResults: results,
      violations: this.complianceResults.violations,
      recommendations: this.generateRecommendations(),
      commercialReadiness: this.assessCommercialReadiness(),
      nextSteps: this.generateNextSteps()
    };

    this.printConstitutionalSummary(report);
    return report;
  }

  printConstitutionalSummary(report) {
    console.log('\n🏛️  CONSTITUTIONAL COMPLIANCE SUMMARY');
    console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');

    if (report.overallCompliance) {
      console.log('🎉 FULL CONSTITUTIONAL COMPLIANCE ACHIEVED!');
      console.log('✅ All 5 constitutional articles verified compliant');
      console.log('✅ All 45 XHTML files meet constitutional requirements');
      console.log('🚀 EPUB is ready for commercial distribution');
    } else {
      console.log('⚠️  CONSTITUTIONAL VIOLATIONS DETECTED');
      console.log(`❌ Compliant Articles: ${report.summary.compliantArticles}/5`);
      console.log(`💥 Total Violations: ${report.summary.totalViolations}`);
      console.log('🔧 Fixes required before commercial distribution');
    }

    console.log('\n📊 Article-by-Article Compliance:');
    Object.entries(report.articleResults).forEach(([article, result]) => {
      const status = result.compliant ? '✅' : '❌';
      const articleNumber = article.replace('article', '');
      console.log(`   ${status} Article ${articleNumber}: ${result.title}`);
    });

    if (report.violations.length > 0) {
      console.log('\n🚨 Constitutional Violations:');
      report.violations.forEach((violation, index) => {
        console.log(`   ${index + 1}. Article ${violation.article}: ${violation.message}`);
      });
    }

    if (report.recommendations.length > 0) {
      console.log('\n💡 Recommendations:');
      report.recommendations.forEach((rec, index) => {
        console.log(`   ${index + 1}. ${rec}`);
      });
    }
  }

  assessCommercialReadiness() {
    if (this.complianceResults.overallCompliance) {
      return {
        ready: true,
        status: 'COMMERCIAL_READY',
        platforms: ['Amazon Kindle', 'Apple Books', 'Google Play Books', 'Kobo'],
        printReady: true,
        message: 'EPUB meets all constitutional requirements for commercial distribution'
      };
    } else {
      return {
        ready: false,
        status: 'FIXES_REQUIRED',
        platforms: [],
        printReady: false,
        message: 'Constitutional violations must be resolved before commercial distribution'
      };
    }
  }
}

async function main() {
  const checker = new ConstitutionalComplianceChecker();

  try {
    const report = await checker.checkCompleteConstitutionalCompliance();

    // Save report to file
    const fs = require('fs');
    fs.writeFileSync('constitutional-compliance-report.json', JSON.stringify(report, null, 2));

    // Exit with appropriate code
    if (report.overallCompliance) {
      console.log('\n🎯 Constitutional compliance verification complete!');
      process.exit(0);
    } else {
      console.log('\n💥 Constitutional violations detected. Fixes required.');
      process.exit(1);
    }
  } catch (error) {
    console.error('💥 Constitutional compliance check failed:', error.message);
    process.exit(1);
  }
}

if (require.main === module) {
  main();
}

module.exports = ConstitutionalComplianceChecker;
```

ARTICLE-SPECIFIC CHECKER REQUIREMENTS:

Article I Checker (Layout-First Principle):
- Verify all 45 files meet layout requirements
- Check single-page constraints for frontmatter and backmatter
- Verify 6-section structure for chapters
- Validate clean layouts for part dividers
- Confirm EPUB navigation structure

Article III Checker (Test-First Imperative):
- Verify TDD tests exist for all validators
- Check test coverage meets 100% requirement
- Confirm Red-Green-Refactor methodology followed
- Validate test-first approach documented

VERIFICATION COMMANDS:
```bash
# Individual constitutional compliance
npm run validate:constitutional

# Complete constitutional + build pipeline
npm run build:constitutional-compliance

# Constitutional compliance with reporting
npm run validate:constitutional -- --verbose --report
```

SUCCESS CRITERIA:
- All 5 constitutional articles verified compliant
- Zero constitutional violations across 45 files
- Commercial readiness assessment accurate
- Comprehensive reporting generated
- Integration with build pipeline successful
- Clear next steps provided for any violations

FINAL VALIDATION: Complete coverage of all 45 files with full constitutional compliance ready for commercial distribution.
```

---

## POST-COMPLETION PROMPTS

After completing all 36 tasks, use these prompts for post-implementation activities:

### POST-COMPLETION PROMPT 1: Final System Validation

**EXACT PROMPT FOR CLAUDE CODE:**
```
CONTEXT: I have completed all 36 SDD/TDD implementation tasks. Now I need to perform comprehensive final validation of the complete system to ensure everything works together and meets all constitutional requirements.

TASK: Perform complete end-to-end validation of the SDD/TDD EPUB validation system:

VALIDATION SCOPE:
- All 45 XHTML files validated successfully
- All 5 constitutional articles compliant
- Complete TDD test suite passing
- Commercial distribution readiness confirmed
- Performance targets met

COMMANDS TO EXECUTE IN SEQUENCE:
1. npm run test:tdd:coverage (verify 100% coverage)
2. npm run validate:layout:all (validate all 45 files)
3. npm run build:constitutional-compliance (complete compliance check)
4. npm run build:sdd-tdd-production (full production build)

VERIFICATION CHECKLIST:
□ TDD Infrastructure: Jest, coverage, constitutional compliance
□ Frontmatter Validation: 7 files, single-page constraints
□ Chapter Validation: 16 files, 6-section structure
□ Backmatter Validation: 17 files, specialized layouts
□ Part Divider Validation: 4 files, clean layouts
□ Navigation Validation: 1 file, EPUB compliance
□ Master Validation: All 45 files integrated
□ Constitutional Compliance: All 5 articles verified
□ Commercial Readiness: Production-ready status

SUCCESS CRITERIA:
- All tests pass with 100% coverage
- All 45 files validate successfully
- Zero constitutional violations
- Production build completes successfully
- Performance within target ranges

GENERATE COMPREHENSIVE REPORT:
Create final implementation report showing:
- Complete file coverage verification (45/45)
- Constitutional compliance status (5/5 articles)
- TDD methodology compliance
- Commercial distribution readiness
- Performance metrics summary
- Next steps for production deployment
```

---

### POST-COMPLETION PROMPT 2: Documentation Generation

**EXACT PROMPT FOR CLAUDE CODE:**
```
CONTEXT: SDD/TDD implementation is complete and validated. Now I need to generate comprehensive documentation for ongoing usage and maintenance.

TASK: Create complete documentation package for the SDD/TDD EPUB validation system:

DOCUMENTATION REQUIREMENTS:

1. USER GUIDE: How to use the validation system
   - Quick start guide
   - Common validation commands
   - Troubleshooting guide
   - Error resolution steps

2. DEVELOPER GUIDE: How to maintain and extend the system
   - Code organization and architecture
   - Adding new validation rules
   - Extending to new file types
   - TDD methodology guidelines

3. CONSTITUTIONAL REFERENCE: Understanding the governing principles
   - Article-by-article explanation
   - Constitutional compliance verification
   - Violation resolution procedures
   - Amendment processes

4. COMMERCIAL DEPLOYMENT GUIDE: Production readiness
   - Platform-specific requirements
   - Distribution checklist
   - Quality assurance procedures
   - Performance monitoring

DOCUMENTATION STRUCTURE:
- README.md (updated with SDD/TDD usage)
- docs/USAGE_GUIDE.md
- docs/DEVELOPER_GUIDE.md
- docs/CONSTITUTIONAL_REFERENCE.md
- docs/COMMERCIAL_DEPLOYMENT.md
- docs/TROUBLESHOOTING.md

INCLUDE IN DOCUMENTATION:
- Command reference for all npm scripts
- File type validation requirements
- Constitutional article explanations
- TDD methodology implementation
- Performance optimization guidelines
- Commercial distribution checklist
```

---

### POST-COMPLETION PROMPT 3: Production Deployment

**EXACT PROMPT FOR CLAUDE CODE:**
```
CONTEXT: Complete SDD/TDD system is implemented, validated, and documented. Now I need to prepare for production deployment and create maintenance procedures.

TASK: Prepare production deployment package and maintenance procedures:

PRODUCTION DEPLOYMENT PREPARATION:

1. FINAL BUILD VERIFICATION:
   - Execute complete production build
   - Verify all 45 files in final EPUB
   - Confirm commercial distribution readiness
   - Test multi-platform compatibility

2. QUALITY ASSURANCE CHECKLIST:
   - Constitutional compliance verified
   - All validation tests passing
   - Performance within acceptable ranges
   - Commercial distribution requirements met

3. DEPLOYMENT PACKAGE CREATION:
   - Final validated EPUB file
   - Validation reports and certificates
   - Constitutional compliance documentation
   - Commercial readiness assessment

4. MAINTENANCE PROCEDURES:
   - Regular validation schedule
   - Constitutional compliance monitoring
   - TDD methodology maintenance
   - Performance monitoring setup

PRODUCTION COMMANDS:
```bash
# Final production build with complete validation
npm run build:sdd-tdd-production

# Generate commercial distribution package
npm run generate:commercial-package

# Create validation certificates
npm run generate:compliance-certificates

# Performance benchmark
npm run benchmark:production
```

SUCCESS CRITERIA:
- Production-ready EPUB file generated
- All commercial distribution requirements met
- Maintenance procedures documented
- Monitoring and alerting configured
- Team handoff documentation complete
```

---

### POST-COMPLETION PROMPT 4: Performance Optimization

**EXACT PROMPT FOR CLAUDE CODE:**
```
CONTEXT: SDD/TDD system is production-ready. Now I need to optimize performance and create monitoring for ongoing operations.

TASK: Implement performance optimization and monitoring for the validation system:

OPTIMIZATION AREAS:

1. VALIDATION PERFORMANCE:
   - Optimize file reading and parsing
   - Implement advanced caching strategies
   - Parallel processing improvements
   - Memory usage optimization

2. BUILD PIPELINE OPTIMIZATION:
   - Reduce total build time
   - Optimize dependency management
   - Implement incremental validation
   - Cache validation results

3. MONITORING AND ALERTING:
   - Performance metrics collection
   - Validation failure alerting
   - Constitutional compliance monitoring
   - Commercial readiness tracking

4. SCALABILITY IMPROVEMENTS:
   - Support for larger EPUB files
   - Multiple file format support
   - Distributed validation processing
   - Cloud deployment preparation

PERFORMANCE TARGETS:
- Complete validation under 60 seconds
- TDD test suite under 30 seconds
- Individual file validation under 2 seconds
- Memory usage under 512MB
- 99.9% validation accuracy

MONITORING SETUP:
- Validation time tracking
- Error rate monitoring
- Constitutional compliance alerts
- Performance regression detection
```

---

<function_calls>
<invoke name="TodoWrite">
<parameter name="todos">[{"content": "Generate detailed prompts for all 36 implementation tasks", "status": "completed", "activeForm": "Generating detailed task prompts"}, {"content": "Create post-completion prompts for after all tasks are done", "status": "completed", "activeForm": "Creating post-completion prompts"}, {"content": "Organize prompts by task categories for easy execution", "status": "completed", "activeForm": "Organizing prompts by categories"}]