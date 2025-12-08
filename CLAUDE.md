# Curls & Contemplation - EPUB Production & Publication Constitution

## Project Overview

This is a professional EPUB 3.2 production repository for "Curls & Contemplation: A Creative Hairstylist's Workbook" by Terragon Labs. The project maintains multiple output formats (digital EPUB, print-on-demand PDF) with strict quality controls for publication readiness.

## Architecture Overview

### Directory Structure
```
/root/repo/
├── REBRANDED_OUTPUT/              # Primary publication artifacts
│   ├── content.opf                # EPUB 3.2 package manifest (44 spine items)
│   ├── xhtml/                     # 44 chapter XHTML files + nav
│   │   └── styles/                # style.css, print-pod.css
│   ├── pdf-pod/                   # 44 matching PDFs for POD edition
│   ├── images/                    # 31 visual assets
│   └── fonts/                     # 6 WOFF2 web fonts
├── scripts/                       # Production automation
├── tests/                         # Quality assurance tests
├── docs/                          # Reports, audits, best practices
└── .claude/                       # Workflow automation config
```

### Safe Edit Zones

**SAFE (automation-friendly)**:
- `scripts/` - Build, validation, and QA automation
- `docs/` - Reports, audits, galleries, documentation
- `tests/` - Test suites and fixtures
- `.claude/` - Skills, subagents, hooks, settings

**READ-ONLY (manual review required)**:
- `REBRANDED_OUTPUT/xhtml/*.xhtml` - Chapter content (no automatic edits)
- `REBRANDED_OUTPUT/xhtml/styles/*.css` - Stylesheets (report issues only)
- `REBRANDED_OUTPUT/content.opf` - Package manifest (critical file)
- `REBRANDED_OUTPUT/pdf-pod/*.pdf` - Reference PDFs (immutable)

**NEVER EDIT**:
- `REBRANDED_OUTPUT/mimetype`
- `REBRANDED_OUTPUT/META-INF/`
- Binary assets (fonts, images) without explicit approval

## Coding Standards

### Languages & Versions
- **Python**: 3.11+ (scripts, validation, QA automation)
- **Node.js**: 18+ (build tools, EPUB packaging)
- **XHTML**: EPUB 3.2 specification
- **CSS**: EPUB 3 safe subset (no grid, limited flexbox)

### Style Guidelines
- **Python**: PEP 8, Black formatter, type hints preferred
- **JavaScript**: Prettier, ESM modules
- **XHTML**: W3C valid, semantic HTML5 elements
- **CSS**: Mobile-first, rem units, WCAG 2.2 AA compliant

### Testing Standards
- **Coverage target**: >85% for critical paths
- **Test framework**: pytest (Python), Jest (JavaScript)
- **Validation**: EPUBCheck 5.x strict mode, Ace by DAISY

## EPUB 3.2 Publication Standards

### Typography
- **Body font**: 1rem–1.1rem, line-height 1.45–1.6
- **Max line length**: 60–75 characters
- **Paragraph spacing**: 0.75–1.2em
- **Font pairing**: Serif body + Sans-serif headings

### Layout
- **Text alignment**: Left-aligned (justify only with hyphens: auto)
- **Semantic structure**: Proper h1–h6 hierarchy, no skips
- **Z-order**: Logical reading flow (title → subtitle → body)
- **Responsive**: Works on 5" phone to 10" tablet

### Accessibility (WCAG 2.2 AA)
- **Contrast ratio**: Minimum 4.5:1 for body text
- **Alt text**: Required for all informational images
- **Landmarks**: `<main>`, `<nav>`, `<section>` with ARIA/epub:type
- **Heading hierarchy**: No h1→h3 jumps without h2
- **Screen reader**: Logical tab order, no empty elements

### Assets
- **Images**: 1400px min width, optimized PNGs/JPEGs
- **File sizes**: Quotes 130–160KB, backgrounds <300KB
- **Fonts**: WOFF2 format, subset if possible
- **SVG**: Inline only, <60KB per graphic

## Visual QA Workflow

### Commands

Run the full visual QA pipeline in sequence:

```bash
# Step 1: Discover the 44 target XHTML files from OPF spine
python3 scripts/find_44_targets.py \
  --opf REBRANDED_OUTPUT/content.opf \
  --out docs/REBRANDED_VISUAL_AUDIT.json

# Step 2: Render XHTMLs with headless browser, capture screenshots
python3 scripts/visual_review.py \
  --root REBRANDED_OUTPUT \
  --targets docs/REBRANDED_VISUAL_AUDIT.json \
  --screenshots-dir docs/screenshots \
  --gallery docs/gallery/index.html

# Step 3: Verify PDF parity (page count, size, visual hash)
python3 scripts/pdf_verify.py \
  --root REBRANDED_OUTPUT \
  --targets docs/REBRANDED_VISUAL_AUDIT.json \
  --update-json

# Step 4: Analyze CSS coverage and usage patterns
python3 scripts/css_coverage_analyzer.py \
  --root REBRANDED_OUTPUT \
  --targets docs/REBRANDED_VISUAL_AUDIT.json \
  --out docs/CSS_COVERAGE.md
```

### Viewing Reports

- **JSON summary**: `docs/REBRANDED_VISUAL_AUDIT.json` (machine-readable)
- **Markdown summary**: `docs/REBRANDED_VISUAL_AUDIT.md` (44-row table, executive summary)
- **CSS coverage**: `docs/CSS_COVERAGE.md` (used vs unused selectors)
- **Screenshot gallery**: `docs/gallery/index.html` (open in browser)
- **Best practices**: `docs/EPUB_BEST_PRACTICES.md` (industry standards checklist)

### Interpreting Results

**PASS verdicts**: Layout renders correctly, no blocking issues
**FAIL verdicts**: Critical issues found (accessibility, broken images, layout overflow)

Where to fix issues:
- **Typography/spacing**: Adjust `REBRANDED_OUTPUT/xhtml/styles/style.css`
- **Content structure**: Edit individual XHTML files (manual review required)
- **Accessibility**: Add alt text, fix heading hierarchy, improve contrast
- **Assets**: Optimize images, fix broken references

## Publication Readiness Checklist

Before final EPUB compilation and distribution, ensure:

### Pre-Flight Validation
- [ ] All 44 XHTML files pass EPUB 3.2 validation (EPUBCheck)
- [ ] Visual QA audit shows PASS for all chapters
- [ ] PDF parity check shows no mismatches
- [ ] CSS coverage analysis shows no unused critical rules
- [ ] Accessibility audit passes WCAG 2.2 AA (Ace by DAISY)

### Metadata Completeness
- [ ] `content.opf` has title, creator, language, publisher, ISBN
- [ ] Modified date is current (`dc:date`)
- [ ] Subject keywords (up to 7) are accurate
- [ ] Accessibility metadata present (`schema:accessMode`, `schema:accessibilityFeature`)

### Asset Integrity
- [ ] All images referenced in manifest exist on disk
- [ ] All fonts are properly licensed and embedded
- [ ] No external HTTP/HTTPS resources (local assets only)
- [ ] File sizes within platform limits (total EPUB <50MB recommended)

### Cross-Platform Testing
- [ ] Kindle Previewer (KPF/MOBI conversion test)
- [ ] Apple Books simulator (iBooks visual check)
- [ ] Kobo desktop app (reflow test)
- [ ] Google Play Books upload test
- [ ] Adobe Digital Editions 4.5+ (baseline EPUB reader)

## Subagent Delegation

This project uses Claude Code subagents for specialized tasks. Invoke these agents when working on:

### Content & Structure
- **epub-validator** – Run EPUBCheck, validate spine order, fix manifest errors
- **accessibility-checker** – Audit WCAG 2.2 compliance, suggest ARIA improvements
- **css-auditor** – Analyze stylesheet coverage, identify unused rules, report conflicts

### Visual & Layout
- **epub-visual-auditor** – Run visual QA pipeline, interpret screenshots, summarize layout issues
- **pdf-verifier** – Compare XHTML vs PDF parity, report mismatches, recommend fixes

### Publication & Finalization
- **publication-finalizer** – Run pre-flight checklist, validate metadata, prepare distribution package
- **test-writer** – Generate comprehensive tests for new scripts and validation logic
- **doc-writer** – Update documentation, maintain EPUB best practices guide

### General Development
- **code-reviewer** – Review Python/JS code for correctness, security, performance
- **debugger** – Reproduce and fix bugs in automation scripts
- **security-auditor** – Scan for vulnerabilities, check for committed secrets

## Assumptions & Open Questions

### Known Constraints
- Exactly **44 chapter files** in `REBRANDED_OUTPUT/xhtml/` (spine order from content.opf)
- All XHTML files reference CSS relative to `xhtml/` directory
- PDFs in `pdf-pod/` match XHTML 1:1 by basename (e.g., `1-TitlePage.xhtml` ↔ `1-TitlePage.pdf`)
- English language only (`lang="en"`)

### Clarifications Needed
- If PDF is missing for an XHTML file, should temporary reference PDFs be auto-generated?
  - **Current decision**: Yes, via headless browser print-to-PDF (not committed to repo)
- Should CSS minification be applied before final EPUB packaging?
  - **Current decision**: No, keep readable CSS for maintainability
- Are there additional distribution formats beyond EPUB and POD-PDF?
  - **Current decision**: Focus on EPUB 3.2 + POD-PDF only

## Workflow Automation (Hooks & Skills)

### Session Start
- Display git status and recent commits
- Show pending publication issues (if `.claude/pending-issues.txt` exists)
- Remind about safe edit zones

### Pre-Tool Use
- Block destructive commands (`rm -rf`, force push to main)
- Warn if editing read-only XHTML/CSS without confirmation

### Post-Tool Use
- Auto-format Python with Black (if available)
- Auto-format JS/CSS with Prettier (if available)
- Validate XHTML after edits (run EPUBCheck on changed files)

### Subagent Completion
- Log completion to `.claude/logs/subagent.log`
- Suggest next logical subagent based on pipeline status
- Check if publication readiness checklist is complete

### Stop/Session End
- Verify all files saved and tests pass
- Prompt to commit changes if git status shows modifications
- Remind to update CHANGELOG if significant work completed

## Quick Reference

### Run Full QA Pipeline
```bash
npm run qa:full  # Runs all 4 scripts in sequence
```

### Validate Single XHTML File
```bash
epubcheck REBRANDED_OUTPUT/xhtml/9-chapter-i-unveiling-your-creative-odyssey.xhtml
```

### Test Suite
```bash
python3 -m pytest tests/ -v --cov=scripts
```

### Preview Gallery
```bash
python3 -m http.server 8000 --directory docs/gallery
# Open http://localhost:8000
```

### Emergency Rollback
```bash
git checkout REBRANDED_OUTPUT/xhtml/  # Restore XHTML files
git checkout REBRANDED_OUTPUT/content.opf  # Restore manifest
```

---

**Maintained by**: Terragon Labs
**Last Updated**: 2025-11-14
**EPUB Version**: 3.2
**Accessibility Target**: WCAG 2.2 AA
