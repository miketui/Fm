#!/usr/bin/env node

/**
 * Comprehensive XHTML Validation and Auto-Fix Tool
 * Validates all XHTML files and fixes common issues
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

class XHTMLValidator {
    constructor() {
        this.errors = [];
        this.warnings = [];
        this.fixes = [];
        this.stats = {
            filesProcessed: 0,
            errorsFound: 0,
            warningsFound: 0,
            fixesApplied: 0
        };
    }

    log(message, type = 'info') {
        const timestamp = new Date().toISOString();
        const prefix = {
            info: '📋',
            success: '✅',
            warning: '⚠️',
            error: '❌',
            fix: '🔧'
        }[type] || '📋';

        console.log(`${prefix} [${timestamp}] ${message}`);
    }

    validateXHTMLStructure(content, filePath) {
        const issues = [];
        const lines = content.split('\n');

        // Check for XML declaration
        if (!content.startsWith('<?xml version="1.0"')) {
            issues.push({
                type: 'missing_xml_declaration',
                message: 'Missing XML declaration',
                line: 1,
                severity: 'error',
                fixable: true
            });
        }

        // Check for DOCTYPE
        if (!content.includes('<!DOCTYPE html>')) {
            issues.push({
                type: 'missing_doctype',
                message: 'Missing DOCTYPE declaration',
                line: 2,
                severity: 'error',
                fixable: true
            });
        }

        // Check for XHTML namespace
        if (!content.includes('xmlns="http://www.w3.org/1999/xhtml"')) {
            issues.push({
                type: 'missing_namespace',
                message: 'Missing XHTML namespace',
                severity: 'error',
                fixable: true
            });
        }

        // Check for unclosed tags
        this.validateTags(content, filePath, issues);

        // Check for invalid attributes
        this.validateAttributes(content, filePath, issues);

        // Check for entity references
        this.validateEntities(content, filePath, issues);

        return issues;
    }

    validateTags(content, filePath, issues) {
        const lines = content.split('\n');
        const tagStack = [];
        const selfClosingTags = new Set(['img', 'br', 'hr', 'meta', 'link', 'input', 'area', 'base', 'col', 'embed', 'source', 'track', 'wbr']);

        for (let i = 0; i < lines.length; i++) {
            const line = lines[i];
            const lineNum = i + 1;

            // Find opening and closing tags
            const tagRegex = /<\/?([a-zA-Z][a-zA-Z0-9]*)[^>]*>/g;
            let match;

            while ((match = tagRegex.exec(line)) !== null) {
                const fullTag = match[0];
                const tagName = match[1].toLowerCase();

                if (fullTag.startsWith('</')) {
                    // Closing tag
                    const lastOpen = tagStack.pop();
                    if (!lastOpen || lastOpen.name !== tagName) {
                        issues.push({
                            type: 'unclosed_tag',
                            message: `Unexpected closing tag </${tagName}>`,
                            line: lineNum,
                            severity: 'fatal',
                            fixable: false
                        });
                    }
                } else if (fullTag.endsWith('/>') || selfClosingTags.has(tagName)) {
                    // Self-closing tag - no action needed
                } else {
                    // Opening tag
                    tagStack.push({ name: tagName, line: lineNum });
                }
            }
        }

        // Check for unclosed tags
        for (const openTag of tagStack) {
            issues.push({
                type: 'unclosed_tag',
                message: `Unclosed tag <${openTag.name}> opened at line ${openTag.line}`,
                line: openTag.line,
                severity: 'fatal',
                fixable: true,
                tagName: openTag.name
            });
        }
    }

    validateAttributes(content, filePath, issues) {
        const lines = content.split('\n');

        for (let i = 0; i < lines.length; i++) {
            const line = lines[i];
            const lineNum = i + 1;

            // Check for attributes without quotes
            const unquotedAttrRegex = /\s(\w+)=([^"'\s>]+)/g;
            let match;

            while ((match = unquotedAttrRegex.exec(line)) !== null) {
                issues.push({
                    type: 'unquoted_attribute',
                    message: `Attribute ${match[1]} should be quoted`,
                    line: lineNum,
                    severity: 'error',
                    fixable: true,
                    attribute: match[1],
                    value: match[2]
                });
            }

            // Check for malformed attributes (missing quotes, etc.)
            const malformedAttrRegex = /\s(\w+)=([^"'\s>]*[^"'\s>/])/g;
            while ((match = malformedAttrRegex.exec(line)) !== null) {
                if (!match[2].includes('"') && !match[2].includes("'")) {
                    issues.push({
                        type: 'malformed_attribute',
                        message: `Malformed attribute ${match[1]}="${match[2]}"`,
                        line: lineNum,
                        severity: 'fatal',
                        fixable: true,
                        attribute: match[1],
                        value: match[2]
                    });
                }
            }
        }
    }

    validateEntities(content, filePath, issues) {
        const lines = content.split('\n');

        for (let i = 0; i < lines.length; i++) {
            const line = lines[i];
            const lineNum = i + 1;

            // Check for invalid entity references
            const entityRegex = /&[^;\s<>]+/g;
            let match;

            while ((match = entityRegex.exec(line)) !== null) {
                const entity = match[0];

                // Check if it's a valid entity (simplified check)
                const validEntities = ['&lt;', '&gt;', '&amp;', '&quot;', '&apos;', '&nbsp;'];
                const numericEntity = /&#\d+;/;
                const hexEntity = /&#x[0-9a-fA-F]+;/;

                if (!validEntities.includes(entity) &&
                    !numericEntity.test(entity) &&
                    !hexEntity.test(entity) &&
                    !entity.endsWith(';')) {

                    issues.push({
                        type: 'invalid_entity',
                        message: `Invalid entity reference: ${entity}`,
                        line: lineNum,
                        severity: 'fatal',
                        fixable: true,
                        entity: entity
                    });
                }
            }
        }
    }

    fixXHTMLIssues(content, filePath, issues) {
        let fixedContent = content;
        let appliedFixes = 0;

        // Sort issues by line number (descending) to avoid offset issues
        const sortedIssues = issues.filter(issue => issue.fixable)
                                   .sort((a, b) => b.line - a.line);

        for (const issue of sortedIssues) {
            const originalContent = fixedContent;

            switch (issue.type) {
                case 'missing_xml_declaration':
                    if (!fixedContent.startsWith('<?xml')) {
                        fixedContent = '<?xml version="1.0" encoding="UTF-8"?>\n' + fixedContent;
                        appliedFixes++;
                    }
                    break;

                case 'missing_doctype':
                    const lines = fixedContent.split('\n');
                    let insertLine = 0;

                    // Find where to insert DOCTYPE (after XML declaration)
                    if (lines[0] && lines[0].startsWith('<?xml')) {
                        insertLine = 1;
                    }

                    if (!fixedContent.includes('<!DOCTYPE html>')) {
                        lines.splice(insertLine, 0, '<!DOCTYPE html>');
                        fixedContent = lines.join('\n');
                        appliedFixes++;
                    }
                    break;

                case 'missing_namespace':
                    fixedContent = fixedContent.replace(
                        /<html([^>]*)>/,
                        '<html$1 xmlns="http://www.w3.org/1999/xhtml">'
                    );
                    if (fixedContent !== originalContent) appliedFixes++;
                    break;

                case 'unclosed_tag':
                    if (issue.tagName) {
                        // Add closing tag at the end of the body
                        fixedContent = fixedContent.replace(
                            /<\/body>/,
                            `</${issue.tagName}>\n</body>`
                        );
                        if (fixedContent !== originalContent) appliedFixes++;
                    }
                    break;

                case 'unquoted_attribute':
                    const unquotedRegex = new RegExp(`(\\s${issue.attribute})=([^"'\\s>]+)`, 'g');
                    fixedContent = fixedContent.replace(unquotedRegex, `$1="$2"`);
                    if (fixedContent !== originalContent) appliedFixes++;
                    break;

                case 'malformed_attribute':
                    const malformedRegex = new RegExp(`(\\s${issue.attribute})=([^"'\\s>]*[^"'\\s>/])`, 'g');
                    fixedContent = fixedContent.replace(malformedRegex, `$1="$2"`);
                    if (fixedContent !== originalContent) appliedFixes++;
                    break;

                case 'invalid_entity':
                    // Fix common entity issues
                    if (issue.entity.includes('&') && !issue.entity.endsWith(';')) {
                        fixedContent = fixedContent.replace(issue.entity, issue.entity + ';');
                        if (fixedContent !== originalContent) appliedFixes++;
                    }
                    break;
            }
        }

        return { content: fixedContent, fixes: appliedFixes };
    }

    processFile(filePath) {
        this.log(`Processing ${filePath}`, 'info');
        this.stats.filesProcessed++;

        try {
            const content = fs.readFileSync(filePath, 'utf8');
            const issues = this.validateXHTMLStructure(content, filePath);

            // Count issues
            const errors = issues.filter(i => i.severity === 'error' || i.severity === 'fatal');
            const warnings = issues.filter(i => i.severity === 'warning');

            this.stats.errorsFound += errors.length;
            this.stats.warningsFound += warnings.length;

            if (issues.length > 0) {
                this.log(`Found ${issues.length} issues in ${filePath}`, 'warning');

                // Apply fixes
                const { content: fixedContent, fixes } = this.fixXHTMLIssues(content, filePath, issues);

                if (fixes > 0) {
                    fs.writeFileSync(filePath, fixedContent);
                    this.stats.fixesApplied += fixes;
                    this.log(`Applied ${fixes} fixes to ${filePath}`, 'fix');
                }

                // Store remaining issues
                for (const issue of issues) {
                    if (issue.severity === 'error' || issue.severity === 'fatal') {
                        this.errors.push({ ...issue, file: filePath });
                    } else {
                        this.warnings.push({ ...issue, file: filePath });
                    }
                }
            } else {
                this.log(`✅ ${filePath} is valid`, 'success');
            }

        } catch (error) {
            this.log(`Error processing ${filePath}: ${error.message}`, 'error');
            this.errors.push({
                type: 'processing_error',
                message: error.message,
                file: filePath,
                severity: 'fatal'
            });
        }
    }

    globFiles(pattern) {
        try {
            // Use simpler approach for finding files
            const result = execSync(`find ${pattern} -type f 2>/dev/null || true`, { encoding: 'utf8' });
            return result.trim().split('\n').filter(f => f.length > 0);
        } catch (error) {
            return [];
        }
    }

    generateReport() {
        const report = {
            timestamp: new Date().toISOString(),
            stats: this.stats,
            errors: this.errors,
            warnings: this.warnings,
            summary: {
                passed: this.errors.length === 0,
                totalIssues: this.errors.length + this.warnings.length
            }
        };

        // Save JSON report
        fs.writeFileSync('xhtml-validation-report.json', JSON.stringify(report, null, 2));

        // Generate markdown report
        let markdown = `# XHTML Validation Report\n\n`;
        markdown += `Generated: ${report.timestamp}\n\n`;
        markdown += `## Summary\n\n`;
        markdown += `- **Status**: ${report.summary.passed ? '✅ PASSED' : '❌ FAILED'}\n`;
        markdown += `- **Files Processed**: ${this.stats.filesProcessed}\n`;
        markdown += `- **Errors Found**: ${this.stats.errorsFound}\n`;
        markdown += `- **Warnings Found**: ${this.stats.warningsFound}\n`;
        markdown += `- **Fixes Applied**: ${this.stats.fixesApplied}\n`;
        markdown += `- **Total Issues**: ${report.summary.totalIssues}\n\n`;

        if (this.errors.length > 0) {
            markdown += `## Errors\n\n`;
            for (const error of this.errors) {
                markdown += `- **${error.type}**: ${error.message}\n`;
                markdown += `  - File: \`${error.file}\`\n`;
                if (error.line) markdown += `  - Line: ${error.line}\n`;
                markdown += `\n`;
            }
        }

        if (this.warnings.length > 0) {
            markdown += `## Warnings\n\n`;
            for (const warning of this.warnings) {
                markdown += `- **${warning.type}**: ${warning.message}\n`;
                markdown += `  - File: \`${warning.file}\`\n`;
                if (warning.line) markdown += `  - Line: ${warning.line}\n`;
                markdown += `\n`;
            }
        }

        fs.writeFileSync('xhtml-validation-report.md', markdown);

        return report;
    }

    async run() {
        this.log('🚀 Starting Comprehensive XHTML Validation', 'info');

        try {
            // Find all XHTML files
            const xhtmlFiles = this.globFiles('OEBPS/text/*.xhtml');

            this.log(`Found ${xhtmlFiles.length} XHTML files to validate`, 'info');

            // Process each file
            for (const file of xhtmlFiles) {
                this.processFile(file);
            }

            // Generate report
            const report = this.generateReport();

            // Log summary
            this.log(`Validation complete: ${this.stats.filesProcessed} files processed`, 'info');
            this.log(`Fixes applied: ${this.stats.fixesApplied}`, this.stats.fixesApplied > 0 ? 'fix' : 'info');

            if (report.summary.passed) {
                this.log('✅ All XHTML files are valid!', 'success');
                return 0;
            } else {
                this.log(`❌ Found ${report.summary.totalIssues} issues requiring manual attention`, 'error');
                return 1;
            }

        } catch (error) {
            this.log(`Fatal error: ${error.message}`, 'error');
            console.error(error.stack);
            return 2;
        }
    }
}

// Run if called directly
if (require.main === module) {
    const validator = new XHTMLValidator();
    validator.run().then(process.exit);
}

module.exports = XHTMLValidator;
