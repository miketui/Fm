#!/usr/bin/env node

/**
 * TOC (nav.xhtml) validation
 * - Ensures nav.xhtml exists and is declared in OPF as properties="nav"
 * - Validates that each href target file exists
 * - When href contains a fragment (#id), verifies the id exists in target file
 * - Reports missing/invalid links and exits non-zero on failures
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

function extractLinksFromNavText(navText) {
  // Extract all href values from anchors inside nav.xhtml
  // Accept any xhtml hrefs (with or without fragments)
  const links = [];
  const re = /<a\b[^>]*href=["']([^"']+\.xhtml(?:#[^"']*)?)["'][^>]*>/gi;
  let m;
  while ((m = re.exec(navText)) !== null) {
    links.push(m[1]);
  }
  return Array.from(new Set(links));
}

function idExistsInFile(filePath, id) {
  const content = fs.readFileSync(filePath, 'utf8');
  const re = new RegExp(`id=["']${id}["']`);
  return re.test(content);
}

async function main() {
  log('Validating TOC (nav.xhtml)');

  const navPath = path.join('OEBPS', 'text', 'nav.xhtml');
  if (!fs.existsSync(navPath)) {
    err('Missing OEBPS/text/nav.xhtml');
    process.exit(1);
  }

  // Ensure OPF declares nav item
  const opfPath = path.join('OEBPS', 'content.opf');
  if (!fs.existsSync(opfPath)) {
    err('Missing OEBPS/content.opf');
    process.exit(1);
  }

  const opfContent = fs.readFileSync(opfPath, 'utf8');
  if (!opfContent.includes('properties="nav"')) {
    warn('OPF manifest does not declare a nav item (properties="nav").');
  } else {
    ok('OPF manifest declares nav item');
  }

  // Parse nav.xhtml and extract links
  const navText = fs.readFileSync(navPath, 'utf8');
  const links = extractLinksFromNavText(navText);
  if (links.length === 0) {
    warn('No links found in nav.xhtml. TOC may not be clickable.');
    process.exitCode = 0; // warn only
    return;
  }

  ok(`Found ${links.length} TOC link(s)`);

  const errors = [];
  for (const href of links) {
    // skip external links if any
    if (/^https?:\/\//i.test(href)) continue;
    const [file, fragment] = href.split('#');
    const targetFile = path.resolve(path.join('OEBPS', 'text'), file);

    if (!fs.existsSync(targetFile)) {
      errors.push(`TOC target file missing: ${file}`);
      continue;
    }
    if (fragment && !idExistsInFile(targetFile, fragment)) {
      errors.push(`TOC target id not found: ${file}#${fragment}`);
    }
  }

  if (errors.length) {
    err('TOC validation failures:');
    errors.forEach((e) => console.log(`  - ${e}`));
    process.exit(2);
  }

  ok('TOC validation passed');
}

main().catch((e) => {
  err(e.message);
  process.exit(99);
});
