# TDD Integration Plan for EPUB Production
**Plan ID**: tdd-integration-implementation
**Version**: 1.0.0
**Constitutional Compliance**: Article III (Test-First Imperative - NON-NEGOTIABLE)
**Specifications**: All SDD specifications with embedded TDD requirements

## Overview

This plan implements comprehensive Test-Driven Development methodology across the entire EPUB production system, ensuring constitutional Article III compliance with strict Red-Green-Refactor cycles for all validation and implementation work.

## TDD Implementation Strategy

### Constitutional Mandate
- **Article III**: TDD methodology mandatory - Tests written → User approved → Tests fail → Then implement
- **Red-Green-Refactor cycle strictly enforced**
- **No layout changes without corresponding validation tests**

### TDD Scope
- Layout validation for all 45 XHTML files
- Font loading and typography validation
- Commercial distribution compatibility testing
- CSS class and styling validation
- EPUB structure and template compliance

## Phase 1: TDD Framework Establishment (30 minutes)

### 1.1 Testing Infrastructure Setup (15 minutes)
```bash
# Install TDD-specific dependencies
npm install --save-dev jest jsdom @types/jest
npm install --save-dev puppeteer playwright  # For e-reader simulation
```

**Test Directory Structure**:
```
tests/
├── tdd/
│   ├── unit/           # Individual component tests
│   ├── integration/    # Cross-component tests
│   ├── acceptance/     # Constitutional compliance tests
│   └── fixtures/       # Test data and mock files
├── layout/
│   ├── frontmatter/    # Single-page constraint tests
│   ├── chapters/       # 6-section structure tests
│   └── typography/     # Font and CSS tests
└── commercial/
    ├── platforms/      # Platform-specific tests
    └── accessibility/  # WCAG compliance tests
```

### 1.2 TDD Methodology Configuration (15 minutes)
**Jest Configuration** (`jest.config.tdd.js`):
```javascript
module.exports = {
  testEnvironment: 'jsdom',
  testMatch: ['**/tests/tdd/**/*.test.js'],
  setupFilesAfterEnv: ['<rootDir>/tests/tdd/setup.js'],
  collectCoverageFrom: [
    'scripts/validators/**/*.js',
    'scripts/tdd/**/*.js'
  ],
  coverageThreshold: {
    global: {
      branches: 100,
      functions: 100,
      lines: 100,
      statements: 100
    }
  }
};
```

## Phase 2: Red-Green-Refactor Implementation Cycles (120 minutes)

### Cycle 1: Frontmatter Single-Page Validation (40 minutes)

#### RED Phase (15 minutes) - Write Failing Tests
**Test File**: `tests/tdd/unit/frontmatter-validator.test.js`
```javascript
describe('Frontmatter Single-Page Validation', () => {
  describe('Constitutional Article I Compliance', () => {
    test('should enforce min-height: 100vh constraint', () => {
      // Test fails initially - no implementation yet
      expect(validator.hasMinHeightConstraint('1-TitlePage.xhtml')).toBe(true);
    });

    test('should prevent content overflow beyond viewport', () => {
      // Test fails initially - no implementation yet
      expect(validator.contentFitsViewport('2-Copyright.xhtml')).toBe(true);
    });

    test('should validate page-break-inside: avoid', () => {
      // Test fails initially - no implementation yet
      expect(validator.hasPageBreakAvoid('3-TableOfContents.xhtml')).toBe(true);
    });
  });
});
```

#### GREEN Phase (15 minutes) - Implement Minimum Code
**Implementation**: `scripts/tdd/FrontmatterValidator.js`
```javascript
class FrontmatterValidator {
  hasMinHeightConstraint(filename) {
    const content = this.readXHTMLFile(filename);
    return content.includes('min-height: 100vh');
  }

  contentFitsViewport(filename) {
    const metrics = this.calculateContentMetrics(filename);
    return metrics.contentHeight <= metrics.viewportHeight;
  }

  hasPageBreakAvoid(filename) {
    const content = this.readXHTMLFile(filename);
    return content.includes('page-break-inside: avoid');
  }
}
```

#### REFACTOR Phase (10 minutes) - Optimize Implementation
- Extract common file reading logic
- Optimize CSS parsing performance
- Improve error handling and reporting
- Add comprehensive logging

### Cycle 2: Chapter Structure Validation (40 minutes)

#### RED Phase (15 minutes) - Write Failing Tests
**Test File**: `tests/tdd/unit/chapter-structure-validator.test.js`
```javascript
describe('Chapter 6-Section Structure Validation', () => {
  describe('Constitutional Article I Compliance', () => {
    test('should validate exactly 6 sections per chapter', () => {
      expect(validator.getSectionCount('9-chapter-i.xhtml')).toBe(6);
    });

    test('should enforce forced page breaks in quiz section', () => {
      expect(validator.hasQuizPageBreak('9-chapter-i.xhtml')).toBe(true);
    });

    test('should validate quiz single-page constraint', () => {
      expect(validator.quizFitsSinglePage('9-chapter-i.xhtml')).toBe(true);
    });

    test('should validate exactly 4 quiz questions', () => {
      expect(validator.getQuizQuestionCount('9-chapter-i.xhtml')).toBe(4);
    });
  });
});
```

#### GREEN Phase (15 minutes) - Implement Chapter Validation
**Implementation**: `scripts/tdd/ChapterStructureValidator.js`
```javascript
class ChapterStructureValidator {
  getSectionCount(filename) {
    const sections = this.extractSections(filename);
    return sections.length;
  }

  hasQuizPageBreak(filename) {
    const quizSection = this.extractQuizSection(filename);
    return quizSection.includes('page-break-before: always');
  }

  quizFitsSinglePage(filename) {
    const quizSection = this.extractQuizSection(filename);
    return quizSection.includes('max-height: 90vh');
  }

  getQuizQuestionCount(filename) {
    const quizSection = this.extractQuizSection(filename);
    const questions = quizSection.match(/<li.*class="quiz-q"/g) || [];
    return questions.length;
  }
}
```

#### REFACTOR Phase (10 minutes) - Optimize and Clean
- Consolidate section extraction logic
- Implement caching for repeated file access
- Add performance monitoring
- Improve test readability

### Cycle 3: Typography and Font Validation (40 minutes)

#### RED Phase (15 minutes) - Write Failing Font Tests
**Test File**: `tests/tdd/unit/typography-validator.test.js`
```javascript
describe('Typography Validation', () => {
  describe('Constitutional Article V Compliance', () => {
    test('should validate all 6 required fonts exist', () => {
      const requiredFonts = [
        'librebaskerville-regular.woff2',
        'librebaskerville-bold.woff2',
        'librebaskerville-italic.woff2',
        'CinzelDecorative.woff2',
        'Montserrat-Regular.woff2',
        'Montserrat-Bold.woff2'
      ];

      requiredFonts.forEach(font => {
        expect(validator.fontExists(font)).toBe(true);
      });
    });

    test('should validate font declarations in CSS', () => {
      expect(validator.hasFontDeclarations()).toBe(true);
    });

    test('should validate critical CSS classes', () => {
      const criticalClasses = [
        '.chap-title', '.quiz-container', '.worksheet',
        '.page-break-before', '.avoid-break'
      ];

      criticalClasses.forEach(cssClass => {
        expect(validator.cssClassExists(cssClass)).toBe(true);
      });
    });
  });
});
```

#### GREEN Phase (15 minutes) - Implement Typography Validation
**Implementation**: `scripts/tdd/TypographyValidator.js`
```javascript
class TypographyValidator {
  fontExists(fontFilename) {
    const fontPath = `output/OEBPS/fonts/${fontFilename}`;
    return fs.existsSync(fontPath);
  }

  hasFontDeclarations() {
    const fontsCss = fs.readFileSync('output/OEBPS/styles/fonts.css', 'utf8');
    return fontsCss.includes('@font-face');
  }

  cssClassExists(className) {
    const styleCss = fs.readFileSync('output/OEBPS/styles/style.css', 'utf8');
    return styleCss.includes(className);
  }
}
```

#### REFACTOR Phase (10 minutes) - Optimize Typography Validation
- Implement CSS parsing optimization
- Add font loading verification
- Improve cross-platform compatibility checks
- Add performance metrics

## Phase 3: Integration and Acceptance Testing (45 minutes)

### 3.1 Constitutional Compliance Tests (20 minutes)
**Test File**: `tests/tdd/acceptance/constitutional-compliance.test.js`
```javascript
describe('Constitutional Compliance Validation', () => {
  describe('Article I: Layout-First Principle', () => {
    test('all frontmatter files meet single-page constraints', async () => {
      const frontmatterFiles = await getFrontmatterFiles();
      const results = await Promise.all(
        frontmatterFiles.map(file => validator.validateSinglePage(file))
      );

      expect(results.every(result => result.compliant)).toBe(true);
    });

    test('all chapters maintain 6-section structure', async () => {
      const chapterFiles = await getChapterFiles();
      const results = await Promise.all(
        chapterFiles.map(file => validator.validateChapterStructure(file))
      );

      expect(results.every(result => result.sectionsCount === 6)).toBe(true);
    });
  });

  describe('Article III: Test-First Imperative', () => {
    test('TDD methodology compliance across all validators', () => {
      const validators = getAllValidators();
      validators.forEach(validator => {
        expect(validator.hasCorrespondingTests()).toBe(true);
        expect(validator.testsPassBeforeImplementation()).toBe(true);
      });
    });
  });

  describe('Article IV: Commercial Distribution Readiness', () => {
    test('platform compatibility validation', async () => {
      const platforms = ['kindle', 'apple-books', 'google-play', 'kobo'];
      const results = await Promise.all(
        platforms.map(platform => validator.validatePlatformCompatibility(platform))
      );

      expect(results.every(result => result.compatible)).toBe(true);
    });
  });
});
```

### 3.2 Master TDD Validation Pipeline (15 minutes)
**Implementation**: `scripts/tdd/MasterTDDValidator.js`
```javascript
class MasterTDDValidator {
  async runCompleteValidation() {
    const results = {
      constitutional: await this.validateConstitutionalCompliance(),
      layout: await this.validateAllLayouts(),
      typography: await this.validateTypography(),
      commercial: await this.validateCommercialReadiness()
    };

    return this.generateComprehensiveReport(results);
  }

  async validateConstitutionalCompliance() {
    // Ensure all constitutional articles are followed
    return {
      articleI: await this.validateLayoutFirst(),
      articleIII: await this.validateTDDMethodology(),
      articleIV: await this.validateCommercialReadiness(),
      articleV: await this.validateTypographyStandards()
    };
  }
}
```

### 3.3 npm Scripts Integration (10 minutes)
**Package.json Updates**:
```json
{
  "scripts": {
    "test:tdd": "jest --config jest.config.tdd.js",
    "test:tdd:watch": "jest --config jest.config.tdd.js --watch",
    "test:tdd:coverage": "jest --config jest.config.tdd.js --coverage",
    "tdd:red": "jest --config jest.config.tdd.js --bail",
    "tdd:green": "jest --config jest.config.tdd.js",
    "tdd:refactor": "jest --config jest.config.tdd.js && npm run lint",
    "validate:constitutional": "node scripts/tdd/MasterTDDValidator.js --constitutional",
    "build:tdd-compliant": "npm run test:tdd && npm run validate:constitutional && npm run build:production"
  }
}
```

## TDD Quality Gates

### Red Phase Quality Gates
- ✅ Tests written before any implementation
- ✅ Tests fail initially (expected behavior)
- ✅ Tests clearly specify expected behavior
- ✅ Constitutional compliance requirements covered

### Green Phase Quality Gates
- ✅ Minimum implementation to pass tests
- ✅ No over-engineering during Green phase
- ✅ All tests pass after implementation
- ✅ No test modifications during implementation

### Refactor Phase Quality Gates
- ✅ All tests continue to pass during refactoring
- ✅ Code quality improvements made
- ✅ Performance optimizations implemented
- ✅ Documentation updated for changes

## TDD Enforcement Mechanisms

### Pre-commit Hooks
```bash
#!/bin/sh
# .git/hooks/pre-commit
npm run test:tdd || exit 1
npm run validate:constitutional || exit 1
```

### Continuous Integration
```yaml
# .github/workflows/tdd-validation.yml
name: TDD Constitutional Compliance
on: [push, pull_request]
jobs:
  tdd-validation:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run TDD Tests
        run: npm run test:tdd:coverage
      - name: Validate Constitutional Compliance
        run: npm run validate:constitutional
```

## Success Metrics

### TDD Compliance Metrics
- **Test Coverage**: 100% (constitutional requirement)
- **Test-First Compliance**: All implementations preceded by tests
- **Red-Green-Refactor Cycles**: Documented and verified
- **Constitutional Adherence**: Zero violations allowed

### Performance Targets
- **TDD Test Execution**: Under 30 seconds for complete suite
- **Constitutional Validation**: Under 10 seconds
- **Red-Green Cycle Time**: Under 15 minutes per cycle

### Quality Targets
- **Test Reliability**: Zero flaky tests
- **Coverage Accuracy**: 100% meaningful test coverage
- **Refactoring Safety**: All refactoring maintains test success

## Risk Mitigation

### Common TDD Issues
- **Test Writing Difficulty**: Provide TDD training and templates
- **Green Phase Over-engineering**: Strict minimum implementation guidelines
- **Refactoring Fear**: Comprehensive test suite provides safety net
- **Constitutional Violations**: Automated enforcement prevents violations

### Rollback Procedures
- Revert to previous working state if TDD cycle fails
- Maintain test history for troubleshooting
- Document all Red-Green-Refactor decisions

## Dependencies

### Constitutional Requirements
- Article III: Test-First Imperative (NON-NEGOTIABLE)
- All other articles require TDD compliance validation

### Technical Dependencies
- Jest testing framework with 100% coverage requirement
- Constitutional compliance validation tools
- Existing EPUB validation infrastructure

### Process Dependencies
- Developer training on TDD methodology
- Code review process includes TDD compliance verification
- Build pipeline integration with TDD validation

## Next Steps

1. **Execute TDD Framework Setup** (30 minutes)
2. **Implement Red-Green-Refactor Cycles** (120 minutes)
3. **Create Constitutional Compliance Tests** (45 minutes)
4. **Integrate with Build Pipeline** (15 minutes)
5. **Validate Complete TDD System** (30 minutes)

**Total Implementation Time**: 4 hours
**Constitutional Compliance**: Article III (NON-NEGOTIABLE) fully enforced
**Quality Assurance**: 100% test coverage with meaningful tests
**Commercial Readiness**: TDD-validated production system