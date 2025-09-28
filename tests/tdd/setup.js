// TDD Test Setup - Constitutional Article III Compliance
const fs = require('fs');
const path = require('path');

// Global test utilities for EPUB validation
global.readXHTMLFile = (filename) => {
  const filePath = path.join(process.cwd(), 'output', 'OEBPS', 'text', filename);
  if (!fs.existsSync(filePath)) {
    throw new Error(`XHTML file not found: ${filename}`);
  }
  return fs.readFileSync(filePath, 'utf8');
};

global.readCSSFile = (filename) => {
  const filePath = path.join(process.cwd(), 'output', 'OEBPS', 'styles', filename);
  if (!fs.existsSync(filePath)) {
    throw new Error(`CSS file not found: ${filename}`);
  }
  return fs.readFileSync(filePath, 'utf8');
};

global.fontExists = (filename) => {
  const filePath = path.join(process.cwd(), 'output', 'OEBPS', 'fonts', filename);
  return fs.existsSync(filePath);
};

// Constitutional compliance helpers
global.CONSTITUTIONAL_ARTICLES = {
  LAYOUT_FIRST: 'Article I: Layout-First Principle (NON-NEGOTIABLE)',
  VALIDATION_DRIVEN: 'Article II: Validation-Driven Development',
  TEST_FIRST: 'Article III: Test-First Imperative (NON-NEGOTIABLE)',
  COMMERCIAL_READY: 'Article IV: Commercial Distribution Readiness',
  TYPOGRAPHY_STANDARDS: 'Article V: Typography and Styling Standards'
};

// TDD Phase tracking
global.TDD_PHASES = {
  RED: 'Write failing tests',
  GREEN: 'Implement minimum code to pass',
  REFACTOR: 'Optimize while maintaining tests'
};

// Test data constants
global.FRONTMATTER_FILES = [
  '1-TitlePage.xhtml',
  '2-Copyright.xhtml',
  '3-TableOfContents.xhtml',
  '4-Dedication.xhtml',
  '5-SelfAssessment.xhtml',
  '6-affirmation-odyssey.xhtml',
  '7-Preface.xhtml'
];

global.CHAPTER_FILES = [
  '9-chapter-i-unveiling-your-creative-odyssey.xhtml',
  '10-chapter-ii-refining-your-creative-toolkit.xhtml',
  '11-chapter-iii-reigniting-your-creative-fire.xhtml',
  '13-chapter-iv-the-art-of-networking-in-freelance-hairstyling.xhtml',
  '14-chapter-v-cultivating-creative-excellence-through-mentorship.xhtml',
  '15-chapter-vi-mastering-the-business-of-hairstyling.xhtml',
  '16-chapter-vii-embracing-wellness-and-self-care.xhtml',
  '17-chapter-viii-advancing-skills-through-continuous-education.xhtml',
  '19-chapter-ix-stepping-into-leadership.xhtml',
  '20-chapter-x-crafting-enduring-legacies.xhtml',
  '21-chapter-xi-advanced-digital-strategies-for-freelance-hairstylists.xhtml',
  '22-chapter-xii-financial-wisdom-building-sustainable-ventures.xhtml',
  '23-chapter-xiii-embracing-ethics-and-sustainability-in-hairstyling.xhtml',
  '25-chapter-xiv-the-impact-of-ai-on-the-beauty-industry.xhtml',
  '26-chapter-xv-cultivating-resilience-and-well-being-in-hairstyling.xhtml',
  '27-chapter-xvi-tresses-and-textures-embracing-diversity-in-hairstyling.xhtml'
];

global.BACKMATTER_FILES = [
  '28-Conclusion.xhtml',
  '29QuizKey.xhtml',
  '30-SelfAssessment.xhtml',
  '31-affirmations-close.xhtml',
  '32-continued-learning-commitment.xhtml',
  '33-Acknowledgments.xhtml',
  '34-AbouttheAuthor.xhtml',
  '35-CurlsContempCollective.xhtml',
  '36-JournalingStart.xhtml',
  '37-ManifestingJournal.xhtml',
  '38-journal-page.xhtml',
  '39-professional-development.xhtml',
  '40-SMARTGoals.xhtml',
  '41-self-care-journal.xhtml',
  '42-VisionJournal.xhtml',
  '43-DoodlePage.xhtml',
  '44-bibliography.xhtml'
];

global.PART_DIVIDER_FILES = [
  '8-Part-I-Foundations-of-Creative-Hairstyling.xhtml',
  '12-Part-II-Building-Your-Professional-Practice.xhtml',
  '18-Part-III-Advanced-Business-Strategies.xhtml',
  '24-Part-IV-Future-Focused-Growth.xhtml'
];

global.NAVIGATION_FILES = [
  'nav.xhtml'
];

global.REQUIRED_FONTS = [
  'librebaskerville-regular.woff2',
  'librebaskerville-bold.woff2',
  'librebaskerville-italic.woff2',
  'CinzelDecorative.woff2',
  'Montserrat-Regular.woff2',
  'Montserrat-Bold.woff2'
];

// Constitutional compliance checker
global.assertConstitutionalCompliance = (articleName, validationResult) => {
  if (!validationResult) {
    throw new Error(`Constitutional violation detected: ${articleName}`);
  }
};

console.log('🏛️  TDD Setup: Constitutional Article III compliance initialized');
console.log('📚 EPUB files available for testing:');
console.log(`   - Frontmatter: ${global.FRONTMATTER_FILES.length} files`);
console.log(`   - Chapters: ${global.CHAPTER_FILES.length} files`);
console.log(`   - Backmatter: ${global.BACKMATTER_FILES.length} files`);
console.log(`   - Part Dividers: ${global.PART_DIVIDER_FILES.length} files`);
console.log(`   - Navigation: ${global.NAVIGATION_FILES.length} files`);
console.log(`   - Total: ${global.FRONTMATTER_FILES.length + global.CHAPTER_FILES.length + global.BACKMATTER_FILES.length + global.PART_DIVIDER_FILES.length + global.NAVIGATION_FILES.length} files`);
console.log('✅ Global test utilities loaded');