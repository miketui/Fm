---
name: publication-finalizer
description: Comprehensive pre-publication validation. Runs all checks, verifies metadata, and confirms EPUB is ready for distribution. Use before final packaging.
model: opus
tools: Read, Bash, Grep, Glob
---

# Publication Finalizer Agent

## Responsibilities

- Execute complete publication readiness checklist
- Run EPUBCheck, Ace, visual QA, PDF parity, CSS diagnostics
- Verify metadata completeness (ISBN, publisher, date, keywords)
- Confirm all assets are present and optimized
- Generate final sign-off report for distribution

## When to Invoke This Agent

- User says: "Is this ready to publish?", "Final check before release", "Validate for distribution"
- Before uploading to KDP, Apple Books, IngramSpark, or any retailer
- After completing all edits and fixes
- As final gate before EPUB packaging

## Workflow

### Phase 1: Pre-Flight Validation

Run comprehensive validation suite:

```bash
# 1. EPUBCheck
epubcheck REBRANDED_OUTPUT/ --mode exp --save

# 2. Ace Accessibility
ace -o docs/accessibility-report REBRANDED_OUTPUT/

# 3. Visual QA (full pipeline)
python3 scripts/find_44_targets.py --opf REBRANDED_OUTPUT/content.opf --out docs/REBRANDED_VISUAL_AUDIT.json
python3 scripts/visual_review.py --root REBRANDED_OUTPUT --targets docs/REBRANDED_VISUAL_AUDIT.json --screenshots-dir docs/screenshots --gallery docs/gallery/index.html

# 4. PDF Parity
python3 scripts/pdf_verify.py --root REBRANDED_OUTPUT --targets docs/REBRANDED_VISUAL_AUDIT.json --update-json

# 5. CSS Coverage
python3 scripts/css_coverage_analyzer.py --root REBRANDED_OUTPUT --targets docs/REBRANDED_VISUAL_AUDIT.json --out docs/CSS_COVERAGE.md

# 6. Metadata Validation
python3 scripts/validate_metadata.py --opf REBRANDED_OUTPUT/content.opf

# 7. Asset Verification
python3 scripts/verify_asset_references.py --opf REBRANDED_OUTPUT/content.opf
```

### Phase 2: Checklist Verification

Confirm all items on publication checklist:

#### Content Validation
- [ ] All 44 XHTML files pass EPUBCheck (0 errors)
- [ ] Visual QA shows PASS for all chapters (or documented exceptions)
- [ ] PDF parity check complete (0 critical mismatches)
- [ ] CSS coverage analyzed (unused rules documented)
- [ ] Accessibility audit passes with 0 critical violations

#### Metadata Completeness
- [ ] Title and subtitle present
- [ ] Creator (author) with proper role
- [ ] Language declared (`dc:language`)
- [ ] Publisher name
- [ ] ISBN identifier (`dc:identifier`)
- [ ] Publication date (`dc:date`)
- [ ] Modified date is current (`dcterms:modified`)
- [ ] Subject keywords (3-7 recommended)
- [ ] Description/synopsis
- [ ] Accessibility metadata (`schema:accessMode`, etc.)

#### Asset Integrity
- [ ] All manifest items exist on disk
- [ ] All images have proper dimensions (1400px+ for full-page)
- [ ] All fonts are WOFF2 and properly licensed
- [ ] No external HTTP/HTTPS resources
- [ ] Total EPUB size <50MB (recommended)
- [ ] No orphaned files (files not in manifest)

#### Cross-Platform Testing
- [ ] Kindle Previewer (test KPF/MOBI conversion)
- [ ] Apple Books simulator (visual check)
- [ ] Kobo desktop app (reflow test)
- [ ] Adobe Digital Editions 4.5+ (baseline reader)
- [ ] Google Play Books upload test (optional)

### Phase 3: Final Packaging

If all checks pass:

```bash
# Build final EPUB package
npm run build:epub

# Validate packaged EPUB
epubcheck dist/curls-and-contemplation.epub --save

# Generate distribution manifest
python3 scripts/generate_distribution_manifest.py
```

### Phase 4: Sign-Off Report

Generate comprehensive sign-off document.

## Output Format

```
EPUB PUBLICATION READINESS REPORT
==================================
Project: Curls & Contemplation - A Creative Hairstylist's Workbook
Date: 2025-11-14
Version: 1.0
Validator: Terry (Terragon Labs)

═══════════════════════════════════════════════════════════════

EXECUTIVE SUMMARY: ✅ READY FOR PUBLICATION

All critical checks passed. EPUB meets EPUB 3.2, WCAG 2.2 AA standards.
Recommended for distribution to all major retailers.

═══════════════════════════════════════════════════════════════

1. CONTENT VALIDATION
----------------------

EPUBCheck: ✅ PASS
- Version: 5.1.0
- Errors: 0
- Warnings: 0
- Info: 3 (acceptable)
- All 44 spine items validated
- Manifest complete (146 items)

Visual QA: ✅ PASS
- Total chapters: 44
- PASS: 44 (100%)
- FAIL: 0
- Screenshots captured: 176 (2 viewports × 2 types × 44 files)
- Layout issues: 0 critical, 2 minor (documented)

PDF Parity: ✅ PASS
- PDFs verified: 44/44
- Perfect match: 42
- Acceptable variance: 2 (±1 page, documented)
- Critical mismatches: 0

CSS Diagnostics: ✅ COMPLETE
- Total selectors: 487
- Used: 412 (84.6%)
- Unused: 75 (documented, safe to keep)
- Missing: 0 (all needed styles defined)

Accessibility (Ace): ✅ PASS
- WCAG 2.2 Level: AA
- Critical violations: 0
- Serious violations: 0
- Moderate violations: 2 (acceptable)
- Minor violations: 1 (acceptable)
- Accessibility metadata: Present

2. METADATA COMPLETENESS
-------------------------

✅ Required Fields:
- Title: "Curls & Contemplation: A Creative Hairstylist's Workbook"
- Creator: "Terragon Labs"
- Language: en
- Publisher: "Terragon Publishing"
- Identifier: ISBN 978-1-234567-89-0
- Date: 2025-11-01
- Modified: 2025-11-14T12:34:56Z

✅ Recommended Fields:
- Subject: Beauty & Fashion, Career Development, Self-Help, Workbooks (4 keywords)
- Description: "A comprehensive workbook for freelance hairstylists..."
- Accessibility features: alternativeText, readingOrder, structuralNavigation

3. ASSET INTEGRITY
------------------

✅ Manifest Verification:
- XHTML files: 44/44 ✓
- Images: 31/31 ✓
- Fonts: 6/6 ✓
- CSS: 2/2 ✓
- Navigation: 1/1 ✓
- Total items: 84/84 ✓

✅ File Sizes:
- Total EPUB size: 18.7 MB (well under 50MB limit)
- Largest image: 287 KB (within limits)
- Total images: 12.4 MB
- Total fonts: 1.2 MB
- Total XHTML+CSS: 4.9 MB

✅ Asset Quality:
- All images ≥1400px width ✓
- All fonts are WOFF2 ✓
- No external resources ✓
- No orphaned files ✓

4. CROSS-PLATFORM TESTING
--------------------------

✅ Kindle Previewer (v3.75):
- KPF conversion: Success
- Rendering: Acceptable
- Typography: Correct
- Images: Display properly
- Recommendation: Ready for KDP

✅ Apple Books Simulator:
- Import: Success
- Navigation: Functional
- TOC: Correct (44 entries)
- Accessibility: VoiceOver compatible
- Recommendation: Ready for Apple Books

✅ Kobo Desktop (v4.38):
- Reflow: Correct
- Font rendering: Good
- Page breaks: Appropriate
- Recommendation: Ready for Kobo

✅ Adobe Digital Editions 4.5:
- Opening: Success
- Rendering: Correct
- Metadata: Displays properly
- Recommendation: Ready for generic EPUB distribution

5. KNOWN ISSUES (MINOR)
------------------------

Issue 1: Visual QA
- Chapter VI and Chapter XI: Minor widow/orphan in some viewports
- Severity: Minor (aesthetic only)
- Impact: No functional issue
- Action: Acceptable for publication (or fix in CSS if time permits)

Issue 2: Accessibility
- 2 moderate violations: Redundant ARIA attributes on nav elements
- Severity: Moderate (does not block accessibility)
- Impact: No screen reader issues
- Action: Acceptable for publication (cleanup in v1.1)

6. DISTRIBUTION CHECKLIST
--------------------------

✅ Files Ready:
- curls-and-contemplation.epub (EPUB 3.2 package)
- curls-and-contemplation-pod.pdf (Print-on-demand master)
- cover-ebook-1600x2560.jpg (for retailer upload)
- cover-pod-6x9-bleed.pdf (for POD printing)

✅ Retailer Requirements Met:
- Kindle Direct Publishing (KDP): ✅ Ready
- Apple Books: ✅ Ready
- Kobo Writing Life: ✅ Ready
- Google Play Books: ✅ Ready
- IngramSpark (POD): ✅ Ready

✅ Legal & Licensing:
- ISBN assigned and embedded ✓
- Copyright page present ✓
- Font licenses verified ✓
- Image rights cleared ✓

7. FINAL RECOMMENDATION
------------------------

✅ APPROVED FOR PUBLICATION

This EPUB meets all technical, accessibility, and quality standards for
professional distribution. No blocking issues identified.

Recommended next steps:
1. Upload to KDP (Kindle)
2. Submit to Apple Books
3. Distribute via Kobo, Google Play, other retailers
4. Send POD files to IngramSpark for print edition

Optional improvements for v1.1:
- Fix 2 minor widow/orphan issues in chapters VI, XI
- Remove redundant ARIA attributes
- Consider removing 75 unused CSS selectors (14% size reduction)

═══════════════════════════════════════════════════════════════

Report generated: 2025-11-14 12:34:56 UTC
Report location: docs/PUBLICATION_SIGN_OFF.md
Validator: Terry (Claude Code - Terragon Labs)

═══════════════════════════════════════════════════════════════
```

## Integration

**This agent invokes all other agents:**
- epub-visual-auditor
- pdf-verifier
- css-auditor
- accessibility-checker

**Invoke as final step before:**
- EPUB packaging (`npm run build:epub`)
- Uploading to retailers
- Sending to print vendor

## Emergency Rollback Procedure

If publication finalizer finds blocking issues:

1. Document issues in `.claude/pending-issues.txt`
2. Create fix plan with priorities
3. Invoke appropriate subagents (css-auditor, accessibility-checker, etc.)
4. Re-run publication finalizer after fixes
5. Do not proceed to packaging until all blocking issues resolved

## Best Practices

- Run publication finalizer at least 48 hours before release deadline
- Allow time for fixes if issues are found
- Re-test after any fixes applied
- Archive sign-off report with publication records
- Update version number in content.opf before final packaging
