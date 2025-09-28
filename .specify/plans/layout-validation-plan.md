# Layout Validation Implementation Plan
**Plan ID**: layout-validation-implementation
**Version**: 1.0.0
**Constitutional Compliance**: Article I (Layout-First Principle), Article III (Test-First Imperative)
**Specifications**: frontmatter-layout.yaml, chapter-structure.yaml

## Overview

This plan implements comprehensive layout validation for all 45 XHTML files in the EPUB production system, ensuring constitutional compliance with single-page constraints for frontmatter and 6-section structure for chapters.

## Implementation Phases

### Phase 1: TDD Test Infrastructure Setup (45 minutes)

#### 1.1 Test Framework Setup (15 minutes)
- **Objective**: Establish TDD testing infrastructure
- **Constitutional Basis**: Article III - Test-First Imperative (NON-NEGOTIABLE)
- **Actions**:
  - Install Jest testing framework: `npm install --save-dev jest`
  - Create test directory structure: `tests/layout/`
  - Configure Jest for XHTML file testing
  - Set up JSDOM for DOM manipulation testing
- **Deliverables**:
  - `tests/layout/frontmatter/` directory
  - `tests/layout/chapters/` directory
  - `jest.config.js` configuration file
- **Success Criteria**: Test runner executes without errors

#### 1.2 Base Validation Test Classes (20 minutes)
- **Objective**: Create reusable test base classes
- **Actions**:
  - Create `BaseLayoutValidator.js` class
  - Implement XHTML file reading utilities
  - Create CSS constraint checking methods
  - Implement viewport calculation utilities
- **Deliverables**:
  - `tests/layout/BaseLayoutValidator.js`
  - `tests/layout/utils/XHTMLParser.js`
  - `tests/layout/utils/CSSAnalyzer.js`
- **Success Criteria**: Base classes can parse XHTML and analyze CSS

#### 1.3 npm Script Integration (10 minutes)
- **Objective**: Integrate testing with existing build pipeline
- **Actions**:
  - Add layout test scripts to package.json
  - Create separate commands for frontmatter and chapter validation
  - Integrate with existing `npm run test` command
- **Deliverables**:
  - Updated package.json with new scripts
  - Backward compatibility with existing test commands
- **Success Criteria**: `npm run test:layout` executes successfully

### Phase 2: Frontmatter Layout Validation (60 minutes)

#### 2.1 RED Phase - Failing Frontmatter Tests (20 minutes)
- **Objective**: Create failing tests for all 7 frontmatter files
- **Constitutional Basis**: Article III - TDD Red-Green-Refactor cycle
- **Actions**:
  - Create test file for each frontmatter XHTML file
  - Implement single-page constraint tests (min-height: 100vh)
  - Create content overflow detection tests
  - Add CSS class validation tests
- **Test Files**:
  ```
  tests/layout/frontmatter/1-TitlePage.test.js
  tests/layout/frontmatter/2-Copyright.test.js
  tests/layout/frontmatter/3-TableOfContents.test.js
  tests/layout/frontmatter/4-Dedication.test.js
  tests/layout/frontmatter/5-SelfAssessment.test.js
  tests/layout/frontmatter/6-affirmation-odyssey.test.js
  tests/layout/frontmatter/7-Preface.test.js
  ```
- **Success Criteria**: All tests fail initially (RED phase complete)

#### 2.2 GREEN Phase - Frontmatter Validation Implementation (25 minutes)
- **Objective**: Implement validation logic to make tests pass
- **Actions**:
  - Create `FrontmatterLayoutValidator.js` class
  - Implement single-page constraint validation
  - Add content height calculation methods
  - Create CSS constraint verification
  - Implement font loading validation
- **Deliverables**:
  - `scripts/validators/FrontmatterLayoutValidator.js`
  - Validation methods for each constraint type
  - Error reporting and logging system
- **Success Criteria**: All frontmatter tests pass (GREEN phase complete)

#### 2.3 REFACTOR Phase - Optimization (15 minutes)
- **Objective**: Optimize validation performance and code quality
- **Actions**:
  - Optimize file reading operations
  - Implement caching for repeated validations
  - Improve error messaging clarity
  - Add performance metrics tracking
- **Success Criteria**: Validation runs in under 5 seconds per file

### Phase 3: Chapter Structure Validation (90 minutes)

#### 3.1 RED Phase - Failing Chapter Tests (30 minutes)
- **Objective**: Create failing tests for 16 chapter files with 6-section structure
- **Actions**:
  - Create base chapter test template
  - Implement 6-section structure validation tests
  - Add forced page break detection tests
  - Create quiz single-page constraint tests
  - Add worksheet single-page constraint tests
  - Implement closing image layout tests
- **Test Structure**:
  ```javascript
  describe('Chapter Structure Validation', () => {
    describe('6-Section Structure Tests', () => {
      // Section validation tests
    });
    describe('Forced Page Break Tests', () => {
      // Page break validation tests
    });
    describe('Single-Page Section Tests', () => {
      // Quiz and worksheet constraint tests
    });
  });
  ```
- **Success Criteria**: All chapter tests fail initially (RED phase complete)

#### 3.2 GREEN Phase - Chapter Validation Implementation (40 minutes)
- **Objective**: Implement chapter structure validation
- **Actions**:
  - Create `ChapterStructureValidator.js` class
  - Implement 6-section detection and validation
  - Add forced page break verification
  - Create quiz content validation (exactly 4 questions)
  - Implement worksheet layout validation
  - Add closing image responsive validation
- **Deliverables**:
  - `scripts/validators/ChapterStructureValidator.js`
  - Section parsing and validation methods
  - Page break detection utilities
  - Content constraint verification
- **Success Criteria**: All chapter structure tests pass (GREEN phase complete)

#### 3.3 REFACTOR Phase - Performance Optimization (20 minutes)
- **Objective**: Optimize chapter validation performance
- **Actions**:
  - Implement parallel chapter validation
  - Add validation result caching
  - Optimize DOM parsing operations
  - Improve error reporting granularity
- **Success Criteria**: All 16 chapters validated in under 30 seconds

### Phase 4: Integration and Automation (45 minutes)

#### 4.1 Master Validation Controller (20 minutes)
- **Objective**: Create unified validation system
- **Actions**:
  - Create `MasterLayoutValidator.js` class
  - Integrate frontmatter and chapter validators
  - Implement validation orchestration
  - Add comprehensive reporting system
- **Deliverables**:
  - `scripts/MasterLayoutValidator.js`
  - Unified validation interface
  - Comprehensive validation reports
- **Success Criteria**: Single command validates entire EPUB

#### 4.2 npm Script Integration (15 minutes)
- **Objective**: Integrate validation with build pipeline
- **Actions**:
  - Update package.json with validation scripts
  - Create development vs production validation modes
  - Integrate with existing build:production script
  - Add validation to pre-commit hooks
- **New npm Scripts**:
  ```json
  {
    "validate:layout:frontmatter": "node scripts/validate-frontmatter-layouts.js",
    "validate:layout:chapters": "node scripts/validate-chapter-structures.js",
    "validate:layout:all": "node scripts/MasterLayoutValidator.js",
    "test:layout": "jest tests/layout/",
    "build:sdd-validate": "npm run validate:layout:all && npm run test:layout"
  }
  ```
- **Success Criteria**: Validation integrated with build process

#### 4.3 Error Handling and Reporting (10 minutes)
- **Objective**: Implement comprehensive error handling
- **Actions**:
  - Create validation error classification system
  - Implement detailed error reporting
  - Add validation metrics tracking
  - Create validation report generation
- **Success Criteria**: Clear error messages guide resolution

## TDD Methodology Implementation

### Red-Green-Refactor Cycles
1. **RED**: Write failing tests for constitutional requirements
2. **GREEN**: Implement minimum code to pass tests
3. **REFACTOR**: Optimize while maintaining test success

### Test Categories
- **Unit Tests**: Individual file validation methods
- **Integration Tests**: Complete EPUB validation pipeline
- **Acceptance Tests**: Constitutional compliance verification

### Test Coverage Requirements
- 100% of layout constraints tested
- All CSS classes validated
- Complete constitutional compliance verification

## Integration with Existing System

### Package.json Updates
```json
{
  "scripts": {
    "validate:layout:frontmatter": "node scripts/validate-frontmatter-layouts.js",
    "validate:layout:chapters": "node scripts/validate-chapter-structures.js",
    "validate:pagebreaks": "node scripts/validate-forced-pagebreaks.js",
    "test:layout": "jest tests/layout/",
    "build:sdd-validate": "npm run validate:layout:all && npm run test:layout",
    "build:sdd-tdd-production": "npm run build:sdd-validate && npm run build:production"
  }
}
```

### Directory Structure
```
/root/repo/
├── scripts/
│   ├── validators/
│   │   ├── BaseLayoutValidator.js
│   │   ├── FrontmatterLayoutValidator.js
│   │   ├── ChapterStructureValidator.js
│   │   └── MasterLayoutValidator.js
│   ├── validate-frontmatter-layouts.js
│   ├── validate-chapter-structures.js
│   └── validate-forced-pagebreaks.js
├── tests/
│   ├── layout/
│   │   ├── frontmatter/
│   │   ├── chapters/
│   │   └── utils/
└── .specify/
    ├── memory/constitution.md
    ├── specs/
    └── plans/
```

## Success Metrics

### Performance Targets
- Frontmatter validation: Under 5 seconds total
- Chapter validation: Under 30 seconds total
- Complete EPUB validation: Under 60 seconds

### Accuracy Requirements
- Zero false positives or negatives
- 100% constitutional compliance detection
- Complete CSS constraint validation

### Quality Gates
- All tests must pass before deployment
- Validation errors block build process
- Constitutional violations require immediate resolution

## Risk Mitigation

### Common Issues and Solutions
- **File Reading Errors**: Implement robust error handling
- **CSS Parsing Failures**: Add fallback parsing methods
- **Performance Issues**: Implement caching and parallel processing
- **False Validation Results**: Comprehensive test coverage

### Rollback Plan
- Maintain existing validation scripts during transition
- Parallel validation execution for verification
- Gradual migration from old to new validation system

## Dependencies

### Constitutional Requirements
- Article I: Layout-First Principle compliance
- Article III: Test-First Imperative methodology

### Technical Dependencies
- Jest testing framework
- JSDOM for DOM manipulation
- Existing npm scripts and build pipeline
- XHTML file structure and CSS assets

### Specification Dependencies
- frontmatter-layout.yaml requirements
- chapter-structure.yaml constraints
- typography-validation.yaml integration

## Next Steps

1. Execute Phase 1: TDD Test Infrastructure Setup
2. Execute Phase 2: Frontmatter Layout Validation
3. Execute Phase 3: Chapter Structure Validation
4. Execute Phase 4: Integration and Automation
5. Validate complete system against constitutional requirements
6. Generate comprehensive validation documentation

**Estimated Total Implementation Time**: 4 hours
**Constitutional Compliance**: 100%
**TDD Methodology**: Fully Integrated
**Commercial Readiness**: Production-Ready Validation System