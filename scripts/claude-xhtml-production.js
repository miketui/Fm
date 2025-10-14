#!/usr/bin/env node

/**
 * Claude XHTML Production Script
 * Automated processing for all 45 XHTML files
 *
 * Integrates with GitHub Spec Kit SDD/TDD Framework
 * Constitutional Compliance: Articles I, II, III
 *
 * Usage:
 *   node scripts/claude-xhtml-production.js [options]
 *
 * Options:
 *   --dry-run              Show what would be done without making changes
 *   --frontmatter-only     Process only frontmatter files (1-7)
 *   --chapters-only        Process only chapter files (16 files)
 *   --backmatter-only      Process only backmatter files (17 files)
 *   --sync                 Sync directories after processing
 *   --verbose              Show detailed output
 *   --validate-only        Run validation without processing
 *
 * @version 1.0.0
 * @author Terragon Labs
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// ANSI color codes for terminal output
const colors = {
  reset: '\x1b[0m',
  bright: '\x1b[1m',
  dim: '\x1b[2m',
  red: '\x1b[31m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  magenta: '\x1b[35m',
  cyan: '\x1b[36m',
};

// File categorizations (Constitutional requirement)
const FILE_CATEGORIES = {
  frontmatter: [
    '1-TitlePage.xhtml',
    '2-Copyright.xhtml',
    '3-TableOfContents.xhtml',
    '4-Dedication.xhtml',
    '5-SelfAssessment.xhtml',
    '6-affirmation-odyssey.xhtml',
    '7-Preface.xhtml'
  ],
  partDividers: [
    '8-Part-I-Foundations-of-Creative-Hairstyling.xhtml',
    '12-Part-II-Building-Your-Professional-Practice.xhtml',
    '18-Part-III-Advanced-Business-Strategies.xhtml',
    '24-Part-IV-Future-Focused-Growth.xhtml'
  ],
  chapters: [
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
  ],
  backmatter: [
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
  ],
  navigation: ['nav.xhtml']
};

class ClaudeXHTMLProduction {
  constructor(options = {}) {
    this.rootDir = path.join(__dirname, '../OEBPS/text');
    this.outputDir = path.join(__dirname, '../output/OEBPS/text');
    this.options = options;

    this.stats = {
      processed: 0,
      errors: 0,
      validated: 0,
      warnings: 0,
      skipped: 0,
      startTime: Date.now()
    };

    this.issues = {
      structural: [],
      validation: [],
      constitutional: []
    };
  }

  // Logging utilities
  log(message, level = 'info') {
    const prefix = {
      info: `${colors.blue}ℹ${colors.reset}`,
      success: `${colors.green}✅${colors.reset}`,
      warning: `${colors.yellow}⚠${colors.reset}`,
      error: `${colors.red}❌${colors.reset}`,
      progress: `${colors.cyan}⏳${colors.reset}`
    };

    console.log(`${prefix[level]} ${message}`);
  }

  verbose(message) {
    if (this.options.verbose) {
      console.log(`${colors.dim}   ${message}${colors.reset}`);
    }
  }

  // Main execution flow
  async run() {
    try {
      this.log('Claude XHTML Production Starting...', 'info');
      this.log(`Mode: ${this.getModeDescription()}`, 'info');
      console.log('');

      // Phase 1: Setup and verification
      await this.verifyEnvironment();
      await this.inventoryFiles();

      // Phase 2: Directory comparison
      if (!this.options.validateOnly) {
        await this.compareDirectories();
      }

      // Phase 3: Processing (if not validate-only)
      if (!this.options.validateOnly) {
        if (!this.options.chaptersOnly && !this.options.backmatterOnly) {
          await this.processFrontmatter();
        }

        if (!this.options.frontmatterOnly && !this.options.backmatterOnly) {
          await this.processPartDividers();
          await this.processChapters();
        }

        if (!this.options.frontmatterOnly && !this.options.chaptersOnly) {
          await this.processBackmatter();
        }
      }

      // Phase 4: Validation
      await this.runValidation();

      // Phase 5: Sync (if requested)
      if (this.options.sync && !this.options.dryRun) {
        await this.syncDirectories();
      }

      // Phase 6: Final report
      this.generateReport();

    } catch (error) {
      this.log(`Fatal error: ${error.message}`, 'error');
      if (this.options.verbose) {
        console.error(error.stack);
      }
      process.exit(1);
    }
  }

  getModeDescription() {
    if (this.options.dryRun) return 'Dry Run (no changes)';
    if (this.options.validateOnly) return 'Validation Only';
    if (this.options.frontmatterOnly) return 'Frontmatter Only';
    if (this.options.chaptersOnly) return 'Chapters Only';
    if (this.options.backmatterOnly) return 'Backmatter Only';
    return 'Full Production';
  }

  // Environment verification
  async verifyEnvironment() {
    this.log('Verifying environment...', 'progress');

    // Check directories exist
    if (!fs.existsSync(this.rootDir)) {
      throw new Error(`Root directory not found: ${this.rootDir}`);
    }

    // Create output directory if needed
    if (!fs.existsSync(this.outputDir)) {
      this.verbose(`Creating output directory: ${this.outputDir}`);
      fs.mkdirSync(this.outputDir, { recursive: true });
    }

    // Verify Node.js version
    const nodeVersion = process.version;
    this.verbose(`Node.js version: ${nodeVersion}`);

    // Check for required packages
    try {
      require('xml2js');
      this.verbose('xml2js package available');
    } catch (e) {
      this.log('xml2js package not found - some validations may be limited', 'warning');
    }

    this.log('Environment verified', 'success');
  }

  // File inventory
  async inventoryFiles() {
    this.log('Taking file inventory...', 'progress');

    const totalFiles = Object.values(FILE_CATEGORIES).flat().length;
    let existingFiles = 0;
    let missingFiles = [];

    for (const [category, files] of Object.entries(FILE_CATEGORIES)) {
      for (const file of files) {
        const filePath = path.join(this.rootDir, file);
        if (fs.existsSync(filePath)) {
          existingFiles++;
          this.verbose(`Found: ${file}`);
        } else {
          missingFiles.push(file);
          this.log(`Missing: ${file}`, 'warning');
        }
      }
    }

    this.log(`Found ${existingFiles}/${totalFiles} XHTML files`, 'success');

    if (missingFiles.length > 0) {
      this.log(`${missingFiles.length} files missing`, 'warning');
      this.issues.structural.push(`Missing files: ${missingFiles.join(', ')}`);
    }

    console.log('');
  }

  // Directory comparison
  async compareDirectories() {
    this.log('Comparing root and output directories...', 'progress');

    let identical = 0;
    let different = 0;
    let outputOnly = 0;
    let rootOnly = 0;

    const allFiles = Object.values(FILE_CATEGORIES).flat();

    for (const file of allFiles) {
      const rootPath = path.join(this.rootDir, file);
      const outputPath = path.join(this.outputDir, file);

      const rootExists = fs.existsSync(rootPath);
      const outputExists = fs.existsSync(outputPath);

      if (rootExists && outputExists) {
        const rootContent = fs.readFileSync(rootPath, 'utf8');
        const outputContent = fs.readFileSync(outputPath, 'utf8');

        if (rootContent === outputContent) {
          identical++;
          this.verbose(`Identical: ${file}`);
        } else {
          different++;
          this.verbose(`Different: ${file}`);
        }
      } else if (rootExists && !outputExists) {
        rootOnly++;
        this.verbose(`Root only: ${file}`);
      } else if (!rootExists && outputExists) {
        outputOnly++;
        this.verbose(`Output only: ${file}`);
      }
    }

    this.log(`Comparison: ${identical} identical, ${different} different`, 'info');
    if (rootOnly > 0) this.log(`${rootOnly} files only in root`, 'warning');
    if (outputOnly > 0) this.log(`${outputOnly} files only in output`, 'warning');

    console.log('');
  }

  // Process frontmatter files (7 files)
  async processFrontmatter() {
    this.log('Processing frontmatter files (7 files)...', 'progress');

    for (const file of FILE_CATEGORIES.frontmatter) {
      await this.processFile(file, 'frontmatter');
    }

    this.log('Frontmatter processing complete', 'success');
    console.log('');
  }

  // Process part divider files (4 files)
  async processPartDividers() {
    this.log('Processing part divider files (4 files)...', 'progress');

    for (const file of FILE_CATEGORIES.partDividers) {
      await this.processFile(file, 'partDivider');
    }

    this.log('Part dividers processing complete', 'success');
    console.log('');
  }

  // Process chapter files (16 files)
  async processChapters() {
    this.log('Processing chapter files (16 files)...', 'progress');

    for (const file of FILE_CATEGORIES.chapters) {
      await this.processFile(file, 'chapter');
    }

    this.log('Chapter processing complete', 'success');
    console.log('');
  }

  // Process backmatter files (17 files)
  async processBackmatter() {
    this.log('Processing backmatter files (17 files)...', 'progress');

    for (const file of FILE_CATEGORIES.backmatter) {
      await this.processFile(file, 'backmatter');
    }

    this.log('Backmatter processing complete', 'success');
    console.log('');
  }

  // Process individual file
  async processFile(filename, type) {
    try {
      const rootPath = path.join(this.rootDir, filename);
      const outputPath = path.join(this.outputDir, filename);

      if (!fs.existsSync(rootPath)) {
        this.log(`Skipping missing file: ${filename}`, 'warning');
        this.stats.skipped++;
        return;
      }

      this.verbose(`Processing: ${filename} (${type})`);

      // Read file content
      const content = fs.readFileSync(rootPath, 'utf8');

      // Validate basic structure
      const validation = this.validateFileStructure(content, filename, type);

      if (!validation.valid) {
        this.log(`Validation issues in ${filename}`, 'warning');
        validation.issues.forEach(issue => {
          this.verbose(`  - ${issue}`);
          this.issues.validation.push(`${filename}: ${issue}`);
        });
        this.stats.warnings++;
      }

      // In dry-run mode, don't write files
      if (this.options.dryRun) {
        this.verbose(`Would write: ${outputPath} (dry-run)`);
      } else {
        // Copy to output directory
        fs.writeFileSync(outputPath, content, 'utf8');
        this.verbose(`Written: ${outputPath}`);
      }

      this.stats.processed++;

    } catch (error) {
      this.log(`Error processing ${filename}: ${error.message}`, 'error');
      this.stats.errors++;
    }
  }

  // Validate file structure
  validateFileStructure(content, filename, type) {
    const issues = [];

    // Basic XML validation
    if (!content.startsWith('<?xml')) {
      issues.push('Missing XML declaration');
    }

    if (!content.includes('<!DOCTYPE html>')) {
      issues.push('Missing DOCTYPE declaration');
    }

    if (!content.includes('xmlns="http://www.w3.org/1999/xhtml"')) {
      issues.push('Missing XHTML namespace');
    }

    // Type-specific validation
    switch (type) {
      case 'frontmatter':
        if (!content.includes('min-height: 100vh') && !content.includes('min-height: 80vh')) {
          issues.push('Missing min-height viewport constraint (Constitutional Article I)');
        }
        if (!content.includes('page-break-inside: avoid')) {
          issues.push('Missing page-break-inside: avoid (Constitutional Article I)');
        }
        break;

      case 'chapter':
        // Check for 6-section structure (Constitutional Article I)
        const requiredSections = [
          'chap-title',
          'chap-body',
          'endnotes',
          'quiz-container',
          'worksheet',
          'quote-page'
        ];

        requiredSections.forEach(section => {
          if (!content.includes(section)) {
            issues.push(`Missing required section: ${section} (Constitutional Article I)`);
          }
        });

        // Check for forced page breaks
        if (!content.includes('page-break-before: always')) {
          issues.push('Missing forced page breaks (Constitutional Article I)');
        }

        // Check quiz structure
        const quizMatches = content.match(/<li[^>]*class="quiz-q"/g);
        if (quizMatches && quizMatches.length !== 4) {
          issues.push(`Quiz should have exactly 4 questions, found ${quizMatches ? quizMatches.length : 0}`);
        }
        break;

      case 'partDivider':
        if (!content.includes('part-divider') && !content.includes('Part')) {
          issues.push('Missing part divider structure');
        }
        break;

      case 'backmatter':
        // Basic structure check
        if (content.length < 100) {
          issues.push('File appears to be empty or incomplete');
        }
        break;
    }

    // Check for asset references
    const imageRefs = content.match(/src="[^"]*"/g);
    if (imageRefs) {
      imageRefs.forEach(ref => {
        if (!ref.includes('../images/') && !ref.includes('data:')) {
          issues.push(`Possibly incorrect image path: ${ref}`);
        }
      });
    }

    return {
      valid: issues.length === 0,
      issues
    };
  }

  // Run validation suite
  async runValidation() {
    this.log('Running validation suite...', 'progress');

    const validations = [];

    // XHTML structure validation
    validations.push({ name: 'XHTML Structure', command: 'npm run validate:xhtml' });

    // Asset validation
    validations.push({ name: 'Asset References', command: 'npm run validate:assets' });

    // TOC validation
    validations.push({ name: 'Table of Contents', command: 'npm run validate:toc' });

    for (const validation of validations) {
      try {
        this.verbose(`Running: ${validation.name}`);

        if (!this.options.dryRun) {
          const result = execSync(validation.command, {
            encoding: 'utf8',
            stdio: 'pipe'
          });

          if (this.options.verbose) {
            console.log(result);
          }

          this.stats.validated++;
          this.verbose(`✓ ${validation.name} passed`);
        } else {
          this.verbose(`Would run: ${validation.command} (dry-run)`);
        }

      } catch (error) {
        this.log(`${validation.name} validation failed`, 'warning');
        if (this.options.verbose) {
          console.error(error.stdout || error.message);
        }
        this.issues.validation.push(`${validation.name} validation failed`);
      }
    }

    this.log(`Validation complete: ${this.stats.validated} checks run`, 'success');
    console.log('');
  }

  // Sync directories
  async syncDirectories() {
    this.log('Syncing directories...', 'progress');

    const allFiles = Object.values(FILE_CATEGORIES).flat();
    let synced = 0;

    for (const file of allFiles) {
      const outputPath = path.join(this.outputDir, file);
      const rootPath = path.join(this.rootDir, file);

      if (fs.existsSync(outputPath)) {
        const content = fs.readFileSync(outputPath, 'utf8');
        fs.writeFileSync(rootPath, content, 'utf8');
        synced++;
        this.verbose(`Synced: ${file}`);
      }
    }

    this.log(`Synced ${synced} files from output to root`, 'success');
    console.log('');
  }

  // Generate final report
  generateReport() {
    const duration = ((Date.now() - this.stats.startTime) / 1000).toFixed(2);

    console.log('');
    console.log('═'.repeat(60));
    console.log(`${colors.bright}${colors.cyan}CLAUDE XHTML PRODUCTION REPORT${colors.reset}`);
    console.log('═'.repeat(60));
    console.log('');

    console.log(`${colors.bright}Statistics:${colors.reset}`);
    console.log(`  Processed:   ${colors.green}${this.stats.processed}${colors.reset} files`);
    console.log(`  Validated:   ${colors.blue}${this.stats.validated}${colors.reset} checks`);
    console.log(`  Warnings:    ${colors.yellow}${this.stats.warnings}${colors.reset}`);
    console.log(`  Errors:      ${colors.red}${this.stats.errors}${colors.reset}`);
    console.log(`  Skipped:     ${colors.dim}${this.stats.skipped}${colors.reset}`);
    console.log(`  Duration:    ${colors.cyan}${duration}s${colors.reset}`);
    console.log('');

    if (this.issues.structural.length > 0) {
      console.log(`${colors.yellow}Structural Issues:${colors.reset}`);
      this.issues.structural.forEach(issue => {
        console.log(`  ${colors.yellow}⚠${colors.reset} ${issue}`);
      });
      console.log('');
    }

    if (this.issues.validation.length > 0) {
      console.log(`${colors.yellow}Validation Issues:${colors.reset}`);
      this.issues.validation.forEach(issue => {
        console.log(`  ${colors.yellow}⚠${colors.reset} ${issue}`);
      });
      console.log('');
    }

    if (this.issues.constitutional.length > 0) {
      console.log(`${colors.red}Constitutional Compliance Issues:${colors.reset}`);
      this.issues.constitutional.forEach(issue => {
        console.log(`  ${colors.red}❌${colors.reset} ${issue}`);
      });
      console.log('');
    }

    // Success message
    if (this.stats.errors === 0 && this.issues.constitutional.length === 0) {
      console.log(`${colors.green}${colors.bright}✅ Production processing completed successfully!${colors.reset}`);
    } else if (this.stats.errors === 0) {
      console.log(`${colors.yellow}⚠ Processing completed with warnings${colors.reset}`);
    } else {
      console.log(`${colors.red}❌ Processing completed with errors${colors.reset}`);
    }

    console.log('');
    console.log(`${colors.dim}Next steps:${colors.reset}`);
    console.log(`  1. Review any warnings or errors above`);
    console.log(`  2. Run: npm run build:production`);
    console.log(`  3. Validate: ./validate-epub.sh`);
    console.log('');
    console.log('═'.repeat(60));
  }
}

// CLI Execution
if (require.main === module) {
  const args = process.argv.slice(2);

  const options = {
    dryRun: args.includes('--dry-run'),
    frontmatterOnly: args.includes('--frontmatter-only'),
    chaptersOnly: args.includes('--chapters-only'),
    backmatterOnly: args.includes('--backmatter-only'),
    sync: args.includes('--sync'),
    verbose: args.includes('--verbose'),
    validateOnly: args.includes('--validate-only')
  };

  // Show help
  if (args.includes('--help') || args.includes('-h')) {
    console.log(`
Claude XHTML Production Script

Usage:
  node scripts/claude-xhtml-production.js [options]

Options:
  --dry-run              Show what would be done without making changes
  --frontmatter-only     Process only frontmatter files (7 files)
  --chapters-only        Process only chapter files (16 files)
  --backmatter-only      Process only backmatter files (17 files)
  --sync                 Sync directories after processing
  --verbose              Show detailed output
  --validate-only        Run validation without processing
  --help, -h             Show this help message

Examples:
  node scripts/claude-xhtml-production.js
  node scripts/claude-xhtml-production.js --dry-run --verbose
  node scripts/claude-xhtml-production.js --chapters-only --sync
  node scripts/claude-xhtml-production.js --validate-only

Framework:
  GitHub Spec Kit SDD/TDD
  Constitutional Compliance: Articles I, II, III
  See: .specify/DETAILED_TASK_PROMPTS.md
    `);
    process.exit(0);
  }

  // Run production
  const production = new ClaudeXHTMLProduction(options);
  production.run().catch(error => {
    console.error(`${colors.red}Fatal error:${colors.reset}`, error.message);
    process.exit(1);
  });
}

module.exports = ClaudeXHTMLProduction;
