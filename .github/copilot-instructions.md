# Copilot Instructions - EPUB Production Repository

## Project Overview

Professional EPUB 3.2 production for **"The Artisan's Path: A Comprehensive Guide to Professional Hairstyling Excellence"** (formerly "Curls & Contemplation"). Multi-format output: digital EPUB and print-on-demand PDF. Publisher: Terragon Labs.

## Critical Architecture

### Primary Source: REBRANDED_OUTPUT/
**This is the canonical production directory.** All EPUB builds compile from here.

```
REBRANDED_OUTPUT/
├── content.opf              # EPUB 3.2 manifest (44 spine items)
├── xhtml/                   # 45 XHTML files (44 content + nav.xhtml)
│   ├── nav.xhtml            # Navigation with clickable TOC
│   ├── 1-TitlePage.xhtml    # Frontmatter (files 1-7)
│   ├── 9-chapter-i-*.xhtml  # Chapters (16 files, 6-section structure)
│   └── styles/              # CSS MUST be at xhtml/styles/
│       ├── style.css        # Main styles
│       ├── fonts.css        # Font declarations
│       └── artisan-path-style.css
├── images/                  # 31 assets (~6.2MB total)
├── fonts/                   # 6 WOFF2 files (374KB)
├── pdf-pod/                 # Print-on-demand PDFs (44 matching files)
└── META-INF/container.xml
```

**CSS Path Convention:** XHTML files reference `styles/style.css` (NOT `../styles/`). This is EPUB-compliant.

### File Structure by Type

- **Frontmatter (7 files):** Single-page layouts with `min-height: 100vh`, `page-break-inside: avoid`
- **Chapters (16 files):** 6-section structure: (1) title page with Roman numeral badge, Bible quote, intro; (2-4) content sections; (5) endnotes; (6) quiz (max 4 questions) + worksheet
- **Part Dividers (4 files):** Clean separator pages between parts I-IV
- **Backmatter (17 files):** Journal pages, worksheets, reference materials

## Safe Edit Zones

### ✅ SAFE (Automate Freely)
- `scripts/` - Build automation, validation, QA tools
- `tests/` - Jest TDD, integration, regression tests
- `docs/` - Reports, audits, documentation
- `.claude/` - Workflow automation config

### ⚠️ READ-ONLY (Report Issues, Manual Review Required)
- `REBRANDED_OUTPUT/xhtml/*.xhtml` - Chapter content (content fidelity is paramount)
- `REBRANDED_OUTPUT/xhtml/styles/*.css` - Stylesheets
- `REBRANDED_OUTPUT/content.opf` - Package manifest (critical file)
- `REBRANDED_OUTPUT/pdf-pod/*.pdf` - Reference PDFs

### 🚫 NEVER EDIT
- `REBRANDED_OUTPUT/mimetype` - Must be uncompressed, first file in ZIP
- `REBRANDED_OUTPUT/META-INF/` - Container specification
- Binary assets (fonts, images) without explicit approval

## Developer Workflows

### Build Commands

```bash
# Full validation + test suite
npm run build:full

# Production EPUB (validates, packages, runs epubcheck)
npm run build:production
# OR via shell script:
./scripts/build-epub.sh

# Quick validation
npm run validate              # EPUBCheck + structure
npm run validate:assets       # Image optimization check
npm run validate:xhtml        # XHTML structure (non-destructive)

# Testing
npm run test                  # Integration + regression
npm run test:tdd              # Jest TDD suite (100% coverage required)
npm run test:tdd:watch        # TDD watch mode

# XHTML workflows (safe, non-destructive)
npm run workflow:xhtml:dry-run     # Preview XHTML fixes
npm run workflow:xhtml             # Apply XHTML structure fixes
```

### Build Process Sequence
1. **Validation:** `validate-epub.sh` checks structure, assets, TOC links
2. **XHTML Formatting:** Optional `format-xhtml.sh` (preserves content)
3. **Testing:** Jest TDD + integration + regression suites
4. **Packaging:** ZIP mimetype (stored, uncompressed) → add META-INF + OEBPS
5. **Final Validation:** EPUBCheck 5.x strict mode

### Testing Strategy

**Test Framework:** Jest with jsdom (100% coverage threshold)
```javascript
// jest.config.tdd.js enforces 100% coverage on:
// - scripts/validators/**/*.js
// - scripts/tdd/**/*.js
```

**Test Types:**
- **TDD Unit Tests:** `tests/tdd/unit/` - Validators, parsers, formatters
- **Integration Tests:** `tests/integration/epub-reader-test.js` - EPUB reader compatibility
- **Regression Tests:** `tests/regression/path-reference-test.js` - Baseline comparison

**Run tests BEFORE any XHTML/CSS changes.**

## EPUB 3.2 Standards

### Typography & Layout
- Body font: 1rem-1.1rem, line-height 1.45-1.6
- Max line length: 60-75 characters
- Text alignment: Left (justify only with `hyphens: auto`)
- Semantic heading hierarchy: h1→h2→h3 (no skips)

### Accessibility (WCAG 2.2 AA)
- Contrast ratio: Minimum 4.5:1 for body text
- Alt text: Required for all informational images
- Landmarks: Use `<main>`, `<nav>`, `<section>` with `epub:type`
- Logical tab order, no empty interactive elements

### Asset Optimization
- Images: 1400px min width, optimized PNG/JPEG
- Quote images: 130-160KB target
- Fonts: WOFF2 format, subset if possible
- SVG: Inline only, <60KB per graphic

## Project-Specific Conventions

### Content Fidelity is Sacred
**NEVER modify chapter content programmatically.** If XHTML issues exist:
1. Use `npm run validate:xhtml` to detect problems
2. Generate a report with line numbers and issue descriptions
3. Request manual review for fixes

**Validation is non-destructive.** Scripts like `validate-xhtml-safe.js` report issues without editing files.

### Chapter Template Structure
See `REBRANDED_OUTPUT/MASTER_CHAPTER_TEMPLATE.xhtml` for canonical 6-section layout:
```html
<section class="title-page">
  <div class="roman-numeral-badge">I</div>
  <div class="title-stack">...</div>
  <div class="bible-quote-container">...</div>
</section>
<section class="content-section">...</section>
<section class="endnotes">...</section>
<section class="quiz" style="page-break-before: always;">...</section>
<section class="worksheet" style="page-break-before: always;">...</section>
```

### TOC Validation
`scripts/validate-toc.js` ensures:
- `nav.xhtml` declared in `content.opf` with `properties="nav"`
- All `<a href="...">` targets exist
- Fragment identifiers (`#id`) resolve to actual elements in target files

### Python Environment
- Version: 3.11+
- Style: PEP 8, Black formatter
- Scripts in root for quick workflows (e.g., `build_home_epub.py`)

### Node.js Environment  
- Version: 18+
- Style: Prettier, ESM modules preferred
- Package scripts defined in [package.json](package.json)

## Common Pitfalls

1. **Wrong CSS Paths:** XHTML files use `styles/style.css`, not `../styles/style.css`
2. **Editing Content Directly:** Use validation reports, not automated edits
3. **Skipping Tests:** TDD suite must pass with 100% coverage before production builds
4. **Forgetting EPUBCheck:** Final validation catches EPUB spec violations
5. **Modifying Mimetype:** Must remain uncompressed, stored first in ZIP

## Quick Reference

| Task | Command |
|------|---------|
| Preview XHTML in browser | `npm run preview` → http://localhost:8000/xhtml-preview.html |
| Validate EPUB structure | `npm run validate` |
| Run full test suite | `npm test` |
| Build production EPUB | `npm run build:production` |
| TDD red-green-refactor | `npm run tdd:red` → fix → `npm run tdd:green` → `npm run tdd:refactor` |
| Check asset optimization | `npm run optimize:dry-run` |

## Integration Points

- **EPUBCheck:** Java-based validator in `epubcheck/` (version 5.x)
- **Git Hooks:** Pre-commit runs formatting + linting (`.pre-commit-config.yaml`)
- **CI/CD:** GitHub Actions workflow at `.github/workflows/validate-epub.yml`

## Key Files to Reference

- [CLAUDE.md](../CLAUDE.md) - Comprehensive project constitution and standards
- [package.json](../package.json) - All npm scripts and dependencies
- [QUICK_REFERENCE.md](../QUICK_REFERENCE.md) - File status and directory comparisons
- [EPUB_PRODUCTION_REQUIREMENTS_SDD_TDD_DETAILED.md](../EPUB_PRODUCTION_REQUIREMENTS_SDD_TDD_DETAILED.md) - Detailed specs with layout validation

## Additional Context

**Legacy Directories (Reference Only):**
- `OEBPS/` - Old structure, incorrect CSS paths
- `HOME/OEBPS/` - Simple Python build alternative (see [HOME_WORKFLOW_GUIDE.md](../HOME_WORKFLOW_GUIDE.md))
- `REBRANDED-output/` (lowercase) - Older version, smaller file sizes

**Current Status:** Production-ready. EPUB validates with EPUBCheck, TOC is clickable, all assets optimized.
