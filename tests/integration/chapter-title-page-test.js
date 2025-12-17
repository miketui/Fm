/**
 * Integration Test: ChapterTitlePage React Component
 * 
 * Tests the visual canvas component structure and rendering
 * 
 * Run with: node tests/integration/chapter-title-page-test.js
 */

const fs = require('fs');
const path = require('path');

// ANSI color codes for terminal output
const colors = {
  reset: '\x1b[0m',
  green: '\x1b[32m',
  red: '\x1b[31m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  cyan: '\x1b[36m'
};

class ChapterTitlePageTest {
  constructor() {
    this.results = {
      passed: 0,
      failed: 0,
      tests: []
    };
  }

  log(message, color = colors.reset) {
    console.log(`${color}${message}${colors.reset}`);
  }

  test(name, fn) {
    try {
      fn();
      this.results.passed++;
      this.results.tests.push({ name, status: 'PASS' });
      this.log(`✓ ${name}`, colors.green);
    } catch (error) {
      this.results.failed++;
      this.results.tests.push({ name, status: 'FAIL', error: error.message });
      this.log(`✗ ${name}`, colors.red);
      this.log(`  Error: ${error.message}`, colors.red);
    }
  }

  assert(condition, message) {
    if (!condition) {
      throw new Error(message);
    }
  }

  fileExists(filePath) {
    return fs.existsSync(filePath);
  }

  readFile(filePath) {
    return fs.readFileSync(filePath, 'utf8');
  }

  run() {
    const repoRoot = path.join(__dirname, '../..');
    
    this.log('\n==============================================', colors.cyan);
    this.log('Chapter Title Page Component - Integration Test', colors.cyan);
    this.log('==============================================\n', colors.cyan);

    // Test 1: Component file exists
    this.test('React component file exists', () => {
      const componentPath = path.join(repoRoot, 'src/ChapterTitlePage.jsx');
      this.assert(this.fileExists(componentPath), 'ChapterTitlePage.jsx not found');
    });

    // Test 2: Component exports the function
    this.test('Component exports ChapterTitlePage function', () => {
      const componentPath = path.join(repoRoot, 'src/ChapterTitlePage.jsx');
      const content = this.readFile(componentPath);
      this.assert(
        content.includes('export function ChapterTitlePage'),
        'Component does not export ChapterTitlePage function'
      );
    });

    // Test 3: Component has all required sections
    this.test('Component contains all required sections', () => {
      const componentPath = path.join(repoRoot, 'src/ChapterTitlePage.jsx');
      const content = this.readFile(componentPath);
      
      const requiredSections = [
        'chapter-number-figure',
        'chapter-number-roman',
        'title-stack',
        'title-bar',
        'title-lines',
        'bible-quote-container',
        'bible-quote-text',
        'bible-quote-reference',
        'introduction-heading',
        'introduction-paragraph'
      ];

      requiredSections.forEach(section => {
        this.assert(
          content.includes(section),
          `Missing required section: ${section}`
        );
      });
    });

    // Test 4: Standalone HTML viewer exists
    this.test('Standalone HTML viewer exists', () => {
      const htmlPath = path.join(repoRoot, 'chapter-title-page-canvas.html');
      this.assert(this.fileExists(htmlPath), 'chapter-title-page-canvas.html not found');
    });

    // Test 5: HTML viewer contains component structure
    this.test('HTML viewer contains component structure', () => {
      const htmlPath = path.join(repoRoot, 'chapter-title-page-canvas.html');
      const content = this.readFile(htmlPath);
      
      this.assert(content.includes('chap-title'), 'Missing chap-title section');
      this.assert(content.includes('Chapter Title Page Visual Canvas'), 'Missing page title');
      this.assert(content.includes('CRAFTING'), 'Missing title text');
      this.assert(content.includes('ENDURING LEGACIES'), 'Missing title text');
    });

    // Test 6: Assets directory exists
    this.test('Assets directory exists', () => {
      const assetsPath = path.join(repoRoot, 'assets');
      this.assert(this.fileExists(assetsPath), 'assets/ directory not found');
    });

    // Test 7: Brushstroke asset exists
    this.test('Brushstroke asset files exist', () => {
      const svgPath = path.join(repoRoot, 'assets/brush-teal.svg');
      const pngPath = path.join(repoRoot, 'assets/brush-teal.png');
      
      this.assert(
        this.fileExists(svgPath) || this.fileExists(pngPath),
        'No brushstroke asset found (svg or png)'
      );
    });

    // Test 8: Documentation exists
    this.test('Component documentation exists', () => {
      const docPath = path.join(repoRoot, 'CHAPTER_TITLE_PAGE_COMPONENT.md');
      this.assert(this.fileExists(docPath), 'CHAPTER_TITLE_PAGE_COMPONENT.md not found');
    });

    // Test 9: Documentation contains required sections
    this.test('Documentation contains all required sections', () => {
      const docPath = path.join(repoRoot, 'CHAPTER_TITLE_PAGE_COMPONENT.md');
      const content = this.readFile(docPath);
      
      const requiredSections = [
        '## Overview',
        '## Component Structure',
        '## Usage',
        '## Design System',
        '## Responsive Design',
        '## Accessibility'
      ];

      requiredSections.forEach(section => {
        this.assert(
          content.includes(section),
          `Missing documentation section: ${section}`
        );
      });
    });

    // Test 10: Component uses correct color scheme
    this.test('Component uses correct brand colors', () => {
      const componentPath = path.join(repoRoot, 'src/ChapterTitlePage.jsx');
      const content = this.readFile(componentPath);
      
      // Teal primary color
      this.assert(content.includes('#2B9999'), 'Missing teal primary color');
      // Gold accent color
      this.assert(content.includes('#C9A961'), 'Missing gold accent color');
      // Cream background
      this.assert(content.includes('#F5F3EF'), 'Missing cream background color');
    });

    // Test 11: Component has proper typography
    this.test('Component uses correct font families', () => {
      const componentPath = path.join(repoRoot, 'src/ChapterTitlePage.jsx');
      const content = this.readFile(componentPath);
      
      this.assert(
        content.includes('Cinzel Decorative'),
        'Missing Cinzel Decorative font'
      );
      this.assert(
        content.includes('Libre Baskerville'),
        'Missing Libre Baskerville font'
      );
      this.assert(
        content.includes('Montserrat'),
        'Missing Montserrat font'
      );
    });

    // Test 12: Component has responsive scaling
    this.test('Component uses clamp() for responsive typography', () => {
      const componentPath = path.join(repoRoot, 'src/ChapterTitlePage.jsx');
      const content = this.readFile(componentPath);
      
      this.assert(
        content.includes('clamp('),
        'Component does not use clamp() for responsive sizing'
      );
    });

    // Test 13: Screenshot exists
    this.test('Component screenshot exists', () => {
      const screenshotPath = path.join(repoRoot, 'chapter-title-page-visual-canvas.png');
      this.assert(this.fileExists(screenshotPath), 'Screenshot file not found');
    });

    // Test 14: Package.json has canvas script
    this.test('package.json includes canvas:chapter-title script', () => {
      const packagePath = path.join(repoRoot, 'package.json');
      const content = this.readFile(packagePath);
      
      this.assert(
        content.includes('canvas:chapter-title'),
        'Missing canvas:chapter-title script in package.json'
      );
    });

    // Print summary
    this.log('\n==============================================', colors.cyan);
    this.log('Test Summary', colors.cyan);
    this.log('==============================================', colors.cyan);
    this.log(`Total Tests: ${this.results.passed + this.results.failed}`, colors.blue);
    this.log(`Passed: ${this.results.passed}`, colors.green);
    this.log(`Failed: ${this.results.failed}`, this.results.failed > 0 ? colors.red : colors.green);
    this.log('==============================================\n', colors.cyan);

    // Exit with appropriate code
    process.exit(this.results.failed > 0 ? 1 : 0);
  }
}

// Run tests
const tester = new ChapterTitlePageTest();
tester.run();
