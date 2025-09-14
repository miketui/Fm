#!/usr/bin/env node

/**
 * Safe XHTML Validation Script
 * Validates XHTML files without modifying them
 * Provides detailed reports for manual fixes
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

function validateXHTMLStructure(filePath, content) {
  const issues = [];
  const lines = content.split('\n');
  
  // Check XML declaration
  if (!content.startsWith('<?xml version="1.0"')) {
    if (content.startsWith('<!DOCTYPE')) {
      issues.push({
        type: 'warning',
        line: 1,
        message: 'Missing XML declaration (recommended for XHTML)'
      });
    } else {
      issues.push({
        type: 'error',
        line: 1,
        message: 'Invalid or missing XML declaration'
      });
    }
  }
  
  // Check DOCTYPE
  const doctypeMatch = content.match(/<!DOCTYPE\s+html>/);
  if (!doctypeMatch) {
    issues.push({
      type: 'error',
      line: findLineNumber(content, '<!DOCTYPE') || 2,
      message: 'Missing or malformed DOCTYPE declaration'
    });
  }
  
  // Check XHTML namespace
  if (!content.includes('xmlns="http://www.w3.org/1999/xhtml"')) {
    issues.push({
      type: 'error',
      line: findLineNumber(content, '<html') || 3,
      message: 'Missing XHTML namespace declaration'
    });
  }
  
  // Check for malformed attributes (multiple quotes, unclosed quotes)
  const contentLines = content.split('\n');
  for (let lineNum = 0; lineNum < contentLines.length; lineNum++) {
    const line = contentLines[lineNum];
    
    // Check for unclosed quotes in attributes
    const quoteCount = (line.match(/"/g) || []).length;
    if (quoteCount % 2 !== 0) {
      // Only flag if it's clearly malformed, not just HTML content
      if (line.includes('=') && !line.includes('>')) {
        issues.push({
          type: 'warning',
          line: lineNum + 1,
          message: 'Potential unclosed quote in attributes'
        });
      }
    }
    
    // Check for corruption patterns (4+ consecutive quotes is definitely corruption)
    if (line.includes('""""')) {
      issues.push({
        type: 'error',
        line: lineNum + 1,
        message: 'Multiple consecutive quotes detected (corruption)'
      });
    }
  }
  
  // Check for unclosed tags (basic check)
  const unclosedTags = findUnclosedTags(content);
  unclosedTags.forEach(tag => {
    issues.push({
      type: 'error',
      line: tag.line,
      message: `Potentially unclosed tag: ${tag.tagName}`
    });
  });
  
  // Try XML parsing with xml2js
  try {
    const parser = new xml2js.Parser({
      strict: true,
      explicitArray: false
    });
    
    parser.parseString(content, (err, result) => {
      if (err) {
        issues.push({
          type: 'error',
          line: extractLineFromError(err.message) || 1,
          message: `XML parsing failed: ${err.message}`
        });
      }
    });
  } catch (error) {
    issues.push({
      type: 'error',
      line: 1,
      message: `XML parsing failed: ${error.message}`
    });
  }
  
  return issues;
}

function findLineNumber(content, searchText) {
  const lines = content.split('\n');
  for (let i = 0; i < lines.length; i++) {
    if (lines[i].includes(searchText)) {
      return i + 1;
    }
  }
  return null;
}

function findUnclosedTags(content) {
  const issues = [];
  const selfClosingTags = new Set(['img', 'br', 'hr', 'input', 'meta', 'link']);
  const tagStack = [];
  const lines = content.split('\n');
  
  for (let lineNum = 0; lineNum < lines.length; lineNum++) {
    const line = lines[lineNum];
    
    // Find opening tags
    const openTags = line.match(/<(\w+)(?:\s[^>]*)?(?<!\/)\>/g);
    if (openTags) {
      openTags.forEach(tag => {
        const tagName = tag.match(/<(\w+)/)[1];
        if (!selfClosingTags.has(tagName)) {
          tagStack.push({ tagName, line: lineNum + 1 });
        }
      });
    }
    
    // Find closing tags
    const closeTags = line.match(/<\/(\w+)>/g);
    if (closeTags) {
      closeTags.forEach(tag => {
        const tagName = tag.match(/<\/(\w+)>/)[1];
        const lastOpen = tagStack.findIndex(item => item.tagName === tagName);
        if (lastOpen !== -1) {
          tagStack.splice(lastOpen, 1);
        }
      });
    }
  }
  
  return tagStack.slice(0, 5); // Limit to first 5 issues
}

function extractLineFromError(errorMsg) {
  const lineMatch = errorMsg.match(/line:(\d+)/);
  return lineMatch ? parseInt(lineMatch[1]) : null;
}

function validateFile(filePath) {
  try {
    log('info', `Validating ${filePath}...`);
    
    const content = fs.readFileSync(filePath, 'utf8');
    const issues = validateXHTMLStructure(filePath, content);
    
    if (issues.length === 0) {
      log('success', `${filePath} - No issues found`);
      return { file: filePath, valid: true, issues: [] };
    } else {
      const errors = issues.filter(i => i.type === 'error');
      const warnings = issues.filter(i => i.type === 'warning');
      
      if (errors.length > 0) {
        log('error', `${filePath} - ${errors.length} errors, ${warnings.length} warnings`);
      } else {
        log('warning', `${filePath} - ${warnings.length} warnings`);
      }
      
      // Show first few issues
      issues.slice(0, 3).forEach(issue => {
        const level = issue.type === 'error' ? 'error' : 'warning';
        console.log(`  Line ${issue.line || '?'}: ${issue.message}`);
      });
      
      if (issues.length > 3) {
        console.log(`  ... and ${issues.length - 3} more issues`);
      }
      
      return { file: filePath, valid: false, issues };
    }
  } catch (error) {
    log('error', `Failed to read ${filePath}: ${error.message}`);
    return { file: filePath, valid: false, issues: [{ type: 'error', message: error.message }] };
  }
}

function main() {
  log('info', '🔍 Starting Safe XHTML Validation');
  
  // Check if OEBPS/text directory exists
  const textDir = 'OEBPS/text';
  if (!fs.existsSync(textDir)) {
    log('error', 'OEBPS/text directory not found. Run from EPUB project root.');
    process.exit(1);
  }
  
  // Find all XHTML files
  const files = fs.readdirSync(textDir)
    .filter(file => file.endsWith('.xhtml'))
    .map(file => path.join(textDir, file));
  
  if (files.length === 0) {
    log('warning', 'No XHTML files found');
    process.exit(0);
  }
  
  log('info', `Found ${files.length} XHTML files to validate`);
  
  const results = [];
  let validCount = 0;
  
  for (const file of files) {
    const result = validateFile(file);
    results.push(result);
    if (result.valid) validCount++;
  }
  
  // Summary
  console.log('\n' + '='.repeat(50));
  log('info', `Validation complete: ${validCount}/${files.length} files valid`);
  
  if (validCount === files.length) {
    log('success', '🎉 All XHTML files are valid!');
  } else {
    log('warning', `${files.length - validCount} files need attention`);
    
    // Generate detailed report
    const reportPath = 'xhtml-validation-report.json';
    fs.writeFileSync(reportPath, JSON.stringify(results, null, 2));
    log('info', `Detailed report saved to ${reportPath}`);
  }
  
  process.exit(validCount === files.length ? 0 : 1);
}

if (require.main === module) {
  main();
}

module.exports = { validateXHTMLStructure, validateFile };