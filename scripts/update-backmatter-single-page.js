#!/usr/bin/env node

/**
 * Update Backmatter Files with Single-Page Layout
 * Adds min-height: 100vh and page-break-inside: avoid to all backmatter files
 * Preserves all existing content and styling
 */

const fs = require('fs');
const path = require('path');

const BACKMATTER_FILES = [
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

const SINGLE_PAGE_CSS = `
  <style>
  /* Single-Page Layout Constraints - Constitutional Article I */
  .backmatter-page,
  .min-h-screen,
  body > div:first-child {
    min-height: 100vh !important;
    page-break-inside: avoid;
    break-inside: avoid;
  }

  /* Ensure content fits within viewport */
  .max-content-height {
    max-height: 95vh;
    overflow: visible;
  }

  /* Professional page break control */
  .page-break-before-backmatter {
    page-break-before: always;
    break-before: page;
  }

  .avoid-break-backmatter {
    page-break-inside: avoid;
    break-inside: avoid;
  }

  /* Print-friendly single page */
  @media print {
    .backmatter-page,
    body > div:first-child {
      min-height: 100vh;
      page-break-inside: avoid;
    }
  }
  </style>
`;

class BackmatterUpdater {
  constructor() {
    this.rootDir = path.join(__dirname, '../OEBPS/text');
    this.outputDir = path.join(__dirname, '../output/OEBPS/text');
    this.stats = { updated: 0, errors: 0, skipped: 0 };
  }

  async run() {
    console.log('🔄 Updating backmatter files with single-page layout...\n');

    for (const filename of BACKMATTER_FILES) {
      await this.updateFile(filename);
    }

    this.printSummary();
  }

  async updateFile(filename) {
    try {
      const filePath = path.join(this.rootDir, filename);

      if (!fs.existsSync(filePath)) {
        console.log(`⚠️  Skipped: ${filename} (not found)`);
        this.stats.skipped++;
        return;
      }

      let content = fs.readFileSync(filePath, 'utf8');

      // Check if already has single-page constraints
      if (content.includes('min-height: 100vh') && content.includes('Constitutional Article I')) {
        console.log(`✅ Already updated: ${filename}`);
        this.stats.skipped++;
        return;
      }

      // Add single-page CSS before </head>
      if (content.includes('</head>')) {
        content = content.replace('</head>', `${SINGLE_PAGE_CSS}\n</head>`);
      } else {
        console.log(`⚠️  Warning: No </head> tag found in ${filename}`);
      }

      // Ensure the main container has proper class
      if (!content.includes('class="backmatter-page"')) {
        // Add to body or main div
        content = content.replace(
          /<body([^>]*)>/,
          '<body$1><div class="backmatter-page avoid-break-backmatter">'
        );
        content = content.replace('</body>', '</div></body>');
      }

      // Write to both locations
      fs.writeFileSync(filePath, content, 'utf8');

      const outputPath = path.join(this.outputDir, filename);
      if (fs.existsSync(this.outputDir)) {
        fs.writeFileSync(outputPath, content, 'utf8');
      }

      console.log(`✅ Updated: ${filename}`);
      this.stats.updated++;

    } catch (error) {
      console.log(`❌ Error: ${filename} - ${error.message}`);
      this.stats.errors++;
    }
  }

  printSummary() {
    console.log('\n' + '═'.repeat(60));
    console.log('BACKMATTER UPDATE SUMMARY');
    console.log('═'.repeat(60));
    console.log(`Updated:        ${this.stats.updated} files`);
    console.log(`Already current: ${this.stats.skipped} files`);
    console.log(`Errors:         ${this.stats.errors} files`);
    console.log('═'.repeat(60));

    if (this.stats.errors === 0) {
      console.log('\n✅ All backmatter files successfully updated!');
      console.log('\nSingle-page layout applied:');
      console.log('  • min-height: 100vh');
      console.log('  • page-break-inside: avoid');
      console.log('  • Constitutional Article I compliant');
    }
  }
}

// Run if executed directly
if (require.main === module) {
  const updater = new BackmatterUpdater();
  updater.run().catch(error => {
    console.error('Fatal error:', error.message);
    process.exit(1);
  });
}

module.exports = BackmatterUpdater;
