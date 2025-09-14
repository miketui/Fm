#!/usr/bin/env node

/**
 * Safe XHTML Fixing Script
 * Carefully fixes XHTML issues with backup and validation
 * Uses proper XML parsing instead of dangerous regex
 */

const fs = require('fs');
const path = require('path');
const xml2js = require('xml2js');

// Color codes for console output
const colors = {
  red: '\x1b[31m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  reset: '\x1b[0m'
};

function log(level, message) {
  const prefix = {
    info: `${colors.blue}ℹ️`,
    success: `${colors.green}✅`,
    warning: `${colors.yellow}⚠️`,
    error: `${colors.red}❌`
  };
  console.log(`${prefix[level]} ${message}${colors.reset}`);
}

class SafeXHTMLFixer {
  constructor() {
    this.fixedCount = 0;
    this.totalFiles = 0;
    this.dryRun = process.argv.includes('--dry-run');
  }

  createBackup(filePath) {
    const backupPath = `${filePath}.backup.${Date.now()}`;
    fs.copyFileSync(filePath, backupPath);
    return backupPath;
  }

  fixXMLDeclaration(content) {
    // Fix malformed XML declaration
    if (content.startsWith('<?xml') && !content.startsWith('<?xml version="1.0"')) {
      content = content.replace(/^<\?xml[^>]*\?>/, '<?xml version="1.0" encoding="UTF-8"?>');
      return { content, fixed: true, message: 'Fixed malformed XML declaration' };
    }
    
    // Add missing XML declaration if starting with DOCTYPE
    if (content.startsWith('<!DOCTYPE html>')) {
      content = '<?xml version="1.0" encoding="UTF-8"?>\n' + content;
      return { content, fixed: true, message: 'Added missing XML declaration' };
    }
    
    return { content, fixed: false };
  }

  fixDOCTYPE(content) {
    // Fix self-closing DOCTYPE
    if (content.includes('<!DOCTYPE html/>')) {
      content = content.replace('<!DOCTYPE html/>', '<!DOCTYPE html>');
      return { content, fixed: true, message: 'Fixed self-closing DOCTYPE' };
    }
    return { content, fixed: false };
  }

  fixBasicStructure(content) {
    const fixes = [];
    let fixed = false;
    
    // Fix malformed namespace declarations (very carefully)
    const namespaceRegex = /xmlns="""""([^"]*)/g;
    if (namespaceRegex.test(content)) {
      content = content.replace(namespaceRegex, 'xmlns="$1');
      fixes.push('Fixed malformed xmlns attributes');
      fixed = true;
    }

    // Fix malformed attribute quotes (multiple quotes)
    const malformedQuotes = /(\w+)="""""([^"]*)/g;
    if (malformedQuotes.test(content)) {
      content = content.replace(/(\w+)="""""([^"]*)/g, '$1="$2');
      fixes.push('Fixed malformed attribute quotes');
      fixed = true;
    }

    // Fix self-closing tags that shouldn't be self-closing
    const problematicSelfClosing = /<(head|title|style|body|html|main|section|div|p|h[1-6]|span)[^>]*\/>/g;
    if (problematicSelfClosing.test(content)) {
      content = content.replace(/<(head|title|style|body|html|main|section|div|p|h[1-6]|span)([^>]*)\/>/g, '<$1$2></$1>');
      fixes.push('Fixed inappropriate self-closing tags');
      fixed = true;
    }

    return { content, fixed, message: fixes.join(', ') };
  }

  validateXHTML(content) {
    return new Promise((resolve) => {
      try {
        const parser = new xml2js.Parser({
          strict: true,
          explicitArray: false
        });
        
        parser.parseString(content, (err, result) => {
          if (err) {
            resolve({ valid: false, error: err.message });
          } else {
            resolve({ valid: true, doc: result });
          }
        });
      } catch (error) {
        resolve({ valid: false, error: error.message });
      }
    });
  }

  async fixFile(filePath) {
    this.totalFiles++;
    log('info', `Processing ${filePath}...`);

    try {
      // Read original content
      const originalContent = fs.readFileSync(filePath, 'utf8');
      let content = originalContent;
      const appliedFixes = [];

      // Apply fixes step by step
      const xmlFix = this.fixXMLDeclaration(content);
      if (xmlFix.fixed) {
        content = xmlFix.content;
        appliedFixes.push(xmlFix.message);
      }

      const doctypeFix = this.fixDOCTYPE(content);
      if (doctypeFix.fixed) {
        content = doctypeFix.content;
        appliedFixes.push(doctypeFix.message);
      }

      const structureFix = this.fixBasicStructure(content);
      if (structureFix.fixed) {
        content = structureFix.content;
        appliedFixes.push(structureFix.message);
      }

      // Validate the result
      const validation = await this.validateXHTML(content);
      
      if (!validation.valid) {
        log('warning', `Could not safely fix ${filePath}: ${validation.error}`);
        return { success: false, reason: validation.error };
      }

      // Check if any changes were made
      if (content === originalContent) {
        log('info', `No changes needed for ${filePath}`);
        return { success: true, changed: false };
      }

      if (this.dryRun) {
        log('info', `[DRY RUN] Would fix ${filePath}:`);
        appliedFixes.forEach(fix => log('info', `  - ${fix}`));
        return { success: true, changed: true, dryRun: true };
      }

      // Create backup and write fixed content
      const backupPath = this.createBackup(filePath);
      fs.writeFileSync(filePath, content, 'utf8');

      // Verify the fix by re-reading and validating
      const verifyContent = fs.readFileSync(filePath, 'utf8');
      const verifyValidation = await this.validateXHTML(verifyContent);

      if (!verifyValidation.valid) {
        // Restore backup
        fs.copyFileSync(backupPath, filePath);
        log('error', `Fix verification failed for ${filePath}, restored backup`);
        return { success: false, reason: 'Fix verification failed' };
      }

      // Clean up backup on success
      fs.unlinkSync(backupPath);
      
      this.fixedCount++;
      log('success', `Fixed ${filePath}:`);
      appliedFixes.forEach(fix => log('info', `  - ${fix}`));
      
      return { success: true, changed: true, fixes: appliedFixes };

    } catch (error) {
      log('error', `Error processing ${filePath}: ${error.message}`);
      return { success: false, reason: error.message };
    }
  }

  async processDirectory(dirPath) {
    if (!fs.existsSync(dirPath)) {
      log('error', `Directory not found: ${dirPath}`);
      return false;
    }

    const files = fs.readdirSync(dirPath)
      .filter(file => file.endsWith('.xhtml'))
      .map(file => path.join(dirPath, file));

    if (files.length === 0) {
      log('warning', 'No XHTML files found');
      return true;
    }

    log('info', `Found ${files.length} XHTML files to process`);

    const results = [];
    for (const file of files) {
      const result = await this.fixFile(file);
      results.push({ file, ...result });
    }

    // Generate summary
    const successful = results.filter(r => r.success).length;
    const changed = results.filter(r => r.success && r.changed && !r.dryRun).length;
    const failed = results.filter(r => !r.success).length;

    console.log('\n' + '='.repeat(50));
    log('info', `Processing complete:`);
    log('success', `  ✅ ${successful}/${files.length} files processed successfully`);
    
    if (this.dryRun) {
      const wouldChange = results.filter(r => r.success && r.changed).length;
      log('info', `  🔍 ${wouldChange} files would be modified`);
    } else {
      log('info', `  🔧 ${changed} files actually modified`);
    }
    
    if (failed > 0) {
      log('warning', `  ⚠️ ${failed} files could not be processed`);
    }

    return failed === 0;
  }
}

async function main() {
  const fixer = new SafeXHTMLFixer();
  
  if (fixer.dryRun) {
    log('info', '🔍 Running in DRY RUN mode - no files will be modified');
  } else {
    log('info', '🔧 Starting Safe XHTML Fixing');
  }
  
  const textDir = 'OEBPS/text';
  const success = await fixer.processDirectory(textDir);
  
  if (success) {
    log('success', '🎉 All files processed successfully!');
    if (!fixer.dryRun) {
      log('info', '🔍 Run validation to verify fixes: node scripts/validate-xhtml-safe.js');
    }
  } else {
    log('error', '❌ Some files could not be processed');
  }

  process.exit(success ? 0 : 1);
}

if (require.main === module) {
  main().catch(error => {
    log('error', `Unexpected error: ${error.message}`);
    process.exit(1);
  });
}

module.exports = SafeXHTMLFixer;