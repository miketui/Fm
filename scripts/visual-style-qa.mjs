#!/usr/bin/env node

/**
 * Visual Style QA Agent — XHTML Repository Analyzer
 * - Crawls OEBPS/text/*.xhtml
 * - Runs structural/style/a11y checks against a lightweight contract derived from the repo
 * - Renders screenshots at key viewports using Playwright (Chromium)
 * - Emits reports/findings and artifacts
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { execSync } from 'child_process';
import { chromium } from 'playwright';
import { JSDOM } from 'jsdom';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const REPO_PATH = process.cwd();
const TEXT_DIR = path.join(REPO_PATH, 'OEBPS', 'text');
const CSS_PATHS = [
  'OEBPS/styles/style.css',
  'OEBPS/styles/fonts.css',
  'OEBPS/styles/print.css'
];

const VIEWPORTS = [
  { name: '360x640', width: 360, height: 640 },
  { name: '768x1024', width: 768, height: 1024 },
  { name: '1080x1920', width: 1080, height: 1920 },
  { name: '1366x768', width: 1366, height: 768 }
];

const OUTPUT_DIR = path.join(REPO_PATH, 'reports');
const ARTIFACTS_DIR = path.join(REPO_PATH, 'artifacts');
fs.mkdirSync(OUTPUT_DIR, { recursive: true });
fs.mkdirSync(ARTIFACTS_DIR, { recursive: true });

function loadSpine() {
  try {
    const xml = fs.readFileSync(path.join(REPO_PATH, 'OEBPS', 'content.opf'), 'utf8');
    // lightweight href extraction
    const ids = Array.from(xml.matchAll(/<item\s+id="([^"]+)"\s+href="([^"]+)"/g)).reduce((acc, m) => {
      acc[m[1]] = m[2];
      return acc;
    }, {});
    const order = Array.from(xml.matchAll(/<itemref\s+idref="([^"]+)"/g)).map(m => ids[m[1]]).filter(Boolean);
    return order.map(href => path.join('OEBPS', href));
  } catch {
    // fallback to fs ordering
    return fs.readdirSync(TEXT_DIR).filter(f => f.endsWith('.xhtml')).map(f => path.join('OEBPS', 'text', f));
  }
}

function checkStructure(xhtmlPath) {
  const html = fs.readFileSync(path.join(REPO_PATH, xhtmlPath), 'utf8');
  const dom = new JSDOM(html);
  const d = dom.window.document;

  const issues = [];

  // Valid head elements
  if (!d.querySelector('head title')) {
    issues.push({ id: 'DOC_TITLE', severity: 'warn', loc: 'head', msg: 'Missing <title> element' });
  }

  // Heading outline: expect a single h1 (page title) or nav h1 only in TOC
  const h1s = Array.from(d.querySelectorAll('h1'));
  if (h1s.length > 1 && !xhtmlPath.endsWith('nav.xhtml')) {
    issues.push({ id: 'HEADINGS_MULTIPLE_H1', severity: 'warn', loc: 'body', msg: `Found ${h1s.length} <h1> elements` });
  }

  // Intro heading should be semantic (h2) if present
  const introDiv = d.querySelector('.introduction-heading');
  if (introDiv && introDiv.tagName.toLowerCase() !== 'h2') {
    issues.push({ id: 'INTRO_HEADING_LEVEL', severity: 'error', loc: 'intro', msg: 'Introduction heading should be <h2> with class="introduction-heading"' });
  }

  // Chapter title block presence
  const chapTitle = d.querySelector('.chap-title');
  if (chapTitle) {
    if (!d.querySelector('.chapter-number-text')) {
      issues.push({ id: 'CHAP_NUMBER_MISSING', severity: 'error', loc: 'chap-title', msg: 'Missing .chapter-number-text' });
    }
  }

  // Image alt text quality
  const imgs = Array.from(d.querySelectorAll('img'));
  for (const img of imgs) {
    const alt = img.getAttribute('alt');
    if (alt === null) {
      issues.push({ id: 'IMG_ALT_MISSING', severity: 'error', loc: 'img', msg: 'Image missing alt attribute' });
    }
  }

  // Links integrity (local anchors)
  const anchors = new Set(Array.from(d.querySelectorAll('[id]')).map(n => n.id));
  for (const a of Array.from(d.querySelectorAll('a[href^="#"]'))) {
    const target = a.getAttribute('href').slice(1);
    if (target && !anchors.has(target)) {
      issues.push({ id: 'LINK_ANCHOR_MISSING', severity: 'error', loc: 'a', msg: `Broken local anchor: #${target}` });
    }
  }

  return issues;
}

async function renderScreenshots(spine) {
  const browser = await chromium.launch();
  const context = await browser.newContext();

  const results = [];
  for (const rel of spine) {
    const abs = 'file://' + path.join(REPO_PATH, rel);
    const base = path.basename(rel, '.xhtml');
    const artDir = path.join(ARTIFACTS_DIR, base);
    fs.mkdirSync(artDir, { recursive: true });

    const page = await context.newPage();
    for (const vp of VIEWPORTS) {
      await page.setViewportSize({ width: vp.width, height: vp.height });
      await page.goto(abs);
      await page.screenshot({ path: path.join(artDir, `${base}-${vp.name}.png`), fullPage: true });
    }
    await page.close();
    results.push({ file: rel, artifacts: artDir });
  }

  await context.close();
  await browser.close();
  return results;
}

function summarize(findings) {
  const summary = { errors: 0, warnings: 0 };
  for (const f of findings) {
    for (const iss of f.issues) {
      if (iss.severity === 'error') summary.errors++;
      else summary.warnings++;
    }
  }
  return summary;
}

async function main() {
  // Ensure Playwright deps are installed
  try {
    execSync('npx playwright --version', { stdio: 'ignore' });
  } catch {
    console.log('Installing Playwright Chromium...');
    execSync('npm i -D playwright', { stdio: 'inherit' });
    execSync('npx playwright install --with-deps chromium', { stdio: 'inherit' });
  }

  const spine = loadSpine();
  const findings = [];

  for (const f of spine) {
    const issues = checkStructure(f);
    findings.push({ path: f, status: issues.some(i => i.severity === 'error') ? 'needs-fix' : 'ok', issues });
  }

  // Render screenshots
  await renderScreenshots(spine);

  const summary = summarize(findings);
  const sha = execSync('git rev-parse --short HEAD', { encoding: 'utf8' }).trim();

  const report = {
    repo: REPO_PATH,
    commit: sha,
    totals: { files: spine.length, errors: summary.errors, warnings: summary.warnings },
    files: findings
  };

  fs.writeFileSync(path.join(OUTPUT_DIR, 'findings.json'), JSON.stringify(report, null, 2));

  // Markdown summary
  let md = `# Visual Style QA — Summary\n\n`;
  md += `- Commit: ${sha}\n`;
  md += `- Files: ${spine.length}\n`;
  md += `- Errors: ${summary.errors}\n`;
  md += `- Warnings: ${summary.warnings}\n\n`;
  const top = findings.flatMap(f => f.issues.map(i => ({...i, file: f.path}))).slice(0, 10);
  if (top.length > 0) {
    md += `## Top Issues\n\n`;
    for (const t of top) {
      md += `- [${t.severity.toUpperCase()}] ${t.file}: ${t.id} — ${t.msg}\n`;
    }
    md += `\n`;
  } else {
    md += `All checks passed with no blocking issues.\n`;
  }
  fs.writeFileSync(path.join(OUTPUT_DIR, 'summary.md'), md);

  console.log('QA complete -> reports/summary.md, reports/findings.json, artifacts/*');
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});

