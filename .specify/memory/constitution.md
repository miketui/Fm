# EPUB Production Constitution
## "Curls & Contemplation: A Stylist's Interactive Journey Journal"

## Core Principles

### I. Layout-First Principle (NON-NEGOTIABLE)
**Every EPUB layout decision must prioritize structural integrity and single-page constraints.**
- Frontmatter files (1-7) MUST display within single page constraints (`min-height: 100vh`)
- Chapter files (9-11, 13-17, 19-23, 25-27) MUST maintain 6-section structure with forced page breaks
- Backmatter files (28-44, nav.xhtml) MUST display within single page constraints for journals, worksheets, and reference materials
- Part divider files (8, 12, 18, 24) MUST maintain clean divider page layouts
- No content overflow beyond viewport boundaries allowed for any file type
- Layout validation precedes all content modifications
- Visual consistency across all 45 XHTML files mandatory

### II. Validation-Driven Development
**No layout, font, or structural changes without corresponding automated validation.**
- Pre-implementation validation tests required for all modifications
- Comprehensive validation pipeline covering layout, fonts, CSS, and commercial readiness
- Validation failures block development progress until resolved
- CLI-based validation tools for all operations: `npm run validate:layout`, `npm run validate:fonts`, `npm run validate:pagebreaks`

### III. Test-First Imperative (NON-NEGOTIABLE)
**TDD methodology mandatory: Red-Green-Refactor cycle strictly enforced.**
- Tests written → User approved → Tests fail → Implementation begins
- Layout validation tests for frontmatter single-page constraints
- Chapter structure validation tests for 6-section compliance
- Font loading and CSS validation tests before styling changes
- Integration tests for complete EPUB production pipeline

### IV. Commercial Distribution Readiness
**All implementations must ensure multi-platform compatibility and print-on-demand readiness.**
- Amazon Kindle, Apple Books, Google Play Books, Kobo compatibility required
- Print-on-demand optimization with 300 DPI images and proper page breaks
- EPUB 3.0 compliance with zero EPUBCheck errors
- WCAG 2.1 AA accessibility standards adherence
- File size optimization within platform distribution limits

### V. Typography and Styling Standards
**Consistent typography and styling foundation across all content.**
- Six required fonts must load correctly: Libre Baskerville (3 variants), Cinzel Decorative, Montserrat (2 variants)
- CSS class validation for critical layout components: `.chap-title`, `.quiz-container`, `.worksheet`, `.page-break-before`
- Font fallback stacks defined for cross-platform compatibility
- Responsive design principles for multiple screen sizes and e-reader devices

## Technical Implementation Standards

### Modular Validation Architecture
- Standalone validation modules for each file type (frontmatter, chapters, backmatter)
- Reusable validation libraries across different content categories
- Independent test suites for layout, typography, and content validation
- CLI interface for all validation operations with JSON and human-readable output formats

### Quality Gates and Automation
- Automated validation pipeline integrated with build process
- Pre-commit hooks preventing invalid layout submissions
- Continuous integration testing for all EPUB production stages
- Performance metrics tracking for validation speed and accuracy

## Development Workflow

### SDD Specification Compliance
- All features begin with detailed YAML specifications
- Implementation plans created before coding begins
- Task lists generated from specifications with measurable completion criteria
- Regular specification reviews and updates based on validation results

### Review and Approval Process
- Constitution compliance verification required for all changes
- Layout validation results reviewed before merge approval
- Cross-platform testing verification before production deployment
- Documentation updates mandatory for constitutional amendments

## Governance

**This constitution supersedes all other development practices and guidelines.**
- All development decisions must align with constitutional principles
- Amendments require formal documentation, stakeholder approval, and migration plan
- Layout validation failures constitute constitutional violations requiring immediate resolution
- Complexity must be justified against constitutional principles and commercial readiness requirements

**Emergency Override Protocol**: Only for critical production issues affecting commercial distribution deadlines, with mandatory post-resolution constitutional compliance review.

**Version**: 1.0.0 | **Ratified**: September 28, 2025 | **Last Amended**: September 28, 2025