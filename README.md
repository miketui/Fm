# Curls & Contemplation: A Stylist's Interactive Journey Journal

[![EPUB Validation](https://github.com/miketui/terragon/actions/workflows/validate-epub.yml/badge.svg)](https://github.com/miketui/terragon/actions/workflows/validate-epub.yml)

Publication‑ready EPUB with automated XHTML formatting, full validation, clickable TOC verification, and one‑command compilation to an error‑free epubcheck‑validated file.

## Quick Start

- Requirements: Node.js 18+, npm
- Install: `npm install`
- One‑command build: `npm run build:epub`

This will:
- Format all XHTML files
- Validate EPUB structure and assets
- Validate TOC clickability (nav.xhtml targets)
- Run integration and regression tests
- Run lightweight device compatibility checks
- Compile a distributable EPUB at `dist/curls-and-contemplation.epub`
- Validate the final file with `epubcheck`

## Project Structure

```
├── META-INF/
│   └── container.xml
├── OEBPS/
│   ├── content.opf
│   ├── text/
│   │   ├── nav.xhtml
│   │   └── *.xhtml (45+ content files)
│   ├── styles/*.css
│   ├── images/*
│   └── fonts/*
└── mimetype
```

## Commands

- `npm run build:epub` – Full validation → clickable TOC check → compilation → epubcheck
- `npm run build:full` – Above + multi‑format validation + optimization preview
- `npm run validate` – Package in temp and run epubcheck (+ XHTML sanity checks)
- `npm run validate:assets` – Validate all referenced assets exist and resolve
- `npm run validate:toc` – Verify TOC links target valid files and IDs
- `npm run validate:multi-format` – Validate against EPUB 3.0/3.2/3.3 (and more)
- `npm run device:test` – Heuristic device compatibility checks (viewport/media queries)
- `npm run format` – Batch format XHTML files consistently
- `npm test` – Integration + regression tests
- `npm run metrics` – Generate performance metrics report

## End‑to‑End Workflow

```bash
# 1) Auto‑format and lint
npm run pre-commit

# 2) Full validation (structure + assets + tests)
npm run build

# 3) Validate TOC
npm run validate:toc

# 4) Compile to EPUB and validate output
npm run build:epub
```

Output is created at `dist/curls-and-contemplation.epub`.

## XHTML Validation & Formatting

- Batch processed for all files under `OEBPS/text/*.xhtml`
- Enforced structure checks (XML declaration, DOCTYPE, namespaces)
- Common issues flagged: missing alt on images, inconsistent DOCTYPE, namespaces
- Run: `npm run format` then `npm run validate`

## Clickable TOC Validation

- `scripts/validate-toc.js` parses `OEBPS/text/nav.xhtml`, collects TOC links, and verifies:
  - Each target XHTML exists
  - Each `#id` fragment exists in the target file
  - `content.opf` declares a nav item (`properties="nav"`)
- Run: `npm run validate:toc`

## Device Compatibility

- Heuristic checks to improve mobile and e‑reader rendering:
  - Viewport meta presence in XHTML
  - CSS image scaling (`img { max-width: 100%; height: auto; }`)
  - Presence of media queries
- Non‑blocking by default; use `npm run device:test -- --strict` to fail on issues

## Building the EPUB

- `scripts/build-epub.sh` packages files with correct order:
  - `mimetype` (stored, uncompressed)
  - `META-INF/` then `OEBPS/`
- Validates the resulting file with `epubcheck` when available
- Output: `dist/curls-and-contemplation.epub`

## Testing & CI

- Integration tests check reader compatibility and structure
- Regression tests guard path resolution/links
- Multi‑format validation covers EPUB 2.x/3.x features (optional)
- CI runs validation on push/PR and publishes reports

Run suites individually:

```bash
npm run test:integration
npm run test:regression
npm run validate:assets
npm run validate:multi-format
```

## Pre‑Compilation Checklist

- [ ] All XHTML files pass formatting and structure checks
- [ ] `nav.xhtml` points to valid files and anchors
- [ ] All images have `alt` text and scale within viewport
- [ ] `content.opf` includes a `properties="nav"` manifest item
- [ ] No broken internal links or missing assets
- [ ] `epubcheck` reports 0 errors

## Troubleshooting

- epubcheck not found
  - Install: `npm i -g epubcheck` or use `npx epubcheck`
- TOC target missing
  - Ensure target file exists and `id="..."` matches the fragment in `nav.xhtml`
- Broken links or assets
  - Run `npm run validate:assets` and inspect `asset-validation-report.md`
- Regression baseline updates
  - After structural changes: `npm run test:regression:update`

## Accessibility

- Alt text for all images, semantic structure, screen‑reader friendly markup, keyboard navigation
- Consider WCAG 2.1 techniques for color contrast and focus order

## Optimization

- Analyze and preview optimizations: `npm run optimize:dry-run`
- Full validation across versions: `npm run validate:multi-format`
- Performance metrics: `npm run metrics`

## License

All Rights Reserved - MD Warren

## References

- EPUB 3.0 Specification: https://www.w3.org/publishing/epub3/
- epubcheck: https://github.com/w3c/epubcheck
- EPUB Accessibility: https://www.w3.org/publishing/epub3/a11y/
