#!/usr/bin/env node

/**
 * Lightweight device compatibility checks
 * - Checks for responsive viewport meta in XHTML
 * - Scans CSS for basic responsive rules and image scaling
 * - Reports findings as warnings by default (exit 0), or exit non-zero with --strict
 */

const fs = require('fs');
const path = require('path');

const BLUE = '\u001b[34m';
const GREEN = '\u001b[32m';
const YELLOW = '\u001b[33m';
const RED = '\u001b[31m';
const NC = '\u001b[0m';

const log = (m) => console.log(`${BLUE}ℹ️  ${m}${NC}`);
const ok = (m) => console.log(`${GREEN}✅ ${m}${NC}`);
const warn = (m) => console.log(`${YELLOW}⚠️  ${m}${NC}`);
const err = (m) => console.log(`${RED}❌ ${m}${NC}`);

const STRICT = process.argv.includes('--strict');

function readAllFiles(globDir, ext) {
  const base = path.resolve(globDir);
  if (!fs.existsSync(base)) return [];
  return fs.readdirSync(base)
    .filter((f) => f.toLowerCase().endsWith(ext))
    .map((f) => path.join(base, f));
}

function hasViewportMeta(xhtml) {
  return /<meta[^>]+name=["']viewport["'][^>]*>/i.test(xhtml);
}

function hasImageScaling(css) {
  // Heuristic: look for rules that prevent overflow and scale images
  return /(img\s*\{|img[^}]+max-width\s*:\s*100%)/i.test(css);
}

function hasMediaQueries(css) {
  return /@media\s*(only\s+)?(screen|all)[^{]*\{/.test(css);
}

function main() {
  log('Running device compatibility checks');

  // XHTML checks
  const xhtmlFiles = readAllFiles('OEBPS/text', '.xhtml');
  let withViewport = 0;
  xhtmlFiles.forEach((f) => {
    const c = fs.readFileSync(f, 'utf8');
    if (hasViewportMeta(c)) withViewport += 1;
  });

  if (withViewport === 0) {
    warn('No viewport meta found in XHTML. Consider adding <meta name="viewport" content="width=device-width, initial-scale=1"> for mobile readers.');
  } else {
    ok(`Viewport meta present in ${withViewport}/${xhtmlFiles.length} files`);
  }

  // CSS checks
  const cssFiles = readAllFiles('OEBPS/styles', '.css');
  let scalingOk = false;
  let mqOk = false;
  cssFiles.forEach((f) => {
    const css = fs.readFileSync(f, 'utf8');
    scalingOk = scalingOk || hasImageScaling(css);
    mqOk = mqOk || hasMediaQueries(css);
  });

  if (!scalingOk) warn('CSS does not include image scaling rules (e.g., img { max-width: 100%; height: auto; }).');
  else ok('Image scaling rules detected in CSS');

  if (!mqOk) warn('No CSS media queries detected. Consider adding responsive adjustments for different device widths.');
  else ok('Media queries detected in CSS');

  const hasIssues = (withViewport === 0) || !scalingOk;
  if (STRICT && hasIssues) {
    err('Compatibility issues found in --strict mode');
    process.exit(2);
  }
}

main();

