#!/usr/bin/env node

/**
 * Fix Critical XHTML Issues
 * Fixes the most critical validation errors found by EPUBCheck
 */

const fs = require('fs');
const path = require('path');

class CriticalXHTMLFixer {
    constructor() {
        this.fixedFiles = [];
        this.errors = [];
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

    fixUnclosedDivs(content, filePath) {
        let fixedContent = content;
        let fixes = 0;

        // Count opening and closing div tags
        const openDivs = (content.match(/<div[^>]*(?<!\/)\>/g) || []).length;
        const closeDivs = (content.match(/<\/div>/g) || []).length;
        const selfClosingDivs = (content.match(/<div[^>]*\/>/g) || []).length;

        const missingClosing = openDivs - closeDivs - selfClosingDivs;

        if (missingClosing > 0) {
            // Add closing divs before </body>
            let closingDivs = '';
            for (let i = 0; i < missingClosing; i++) {
                closingDivs += '        </div>\n';
            }

            fixedContent = fixedContent.replace(
                /(\s*)<\/body>/,
                `${closingDivs}$1</body>`
            );

            fixes = missingClosing;
            this.log(`Fixed ${fixes} unclosed div tags in ${filePath}`, 'fix');
        }

        return { content: fixedContent, fixes };
    }

    fixInvalidAttributes(content, filePath) {
        let fixedContent = content;
        let fixes = 0;

        // Remove invalid 'key' attributes (JSX artifacts)
        const keyAttrRegex = /\s+key="[^"]*"/g;
        const originalLength = fixedContent.length;
        fixedContent = fixedContent.replace(keyAttrRegex, '');

        if (fixedContent.length !== originalLength) {
            fixes++;
            this.log(`Removed invalid 'key' attributes from ${filePath}`, 'fix');
        }

        return { content: fixedContent, fixes };
    }

    fixEntityReferences(content, filePath) {
        let fixedContent = content;
        let fixes = 0;

        // Fix unescaped ampersands
        const ampersandRegex = /&(?![a-zA-Z0-9]+;|#[0-9]+;|#x[0-9a-fA-F]+;)/g;
        const matches = content.match(ampersandRegex);

        if (matches) {
            fixedContent = fixedContent.replace(ampersandRegex, '&amp;');
            fixes = matches.length;
            this.log(`Fixed ${fixes} unescaped ampersands in ${filePath}`, 'fix');
        }

        return { content: fixedContent, fixes };
    }

    fixJSXArtifacts(content, filePath) {
        let fixedContent = content;
        let fixes = 0;

        // Remove JSX map functions and similar artifacts
        const jsxMapRegex = /\{[^}]*\.map\([^}]*\)\}/g;
        const jsxVarRegex = /\{[^}]*\}/g;

        const mapMatches = content.match(jsxMapRegex);
        if (mapMatches) {
            // Replace with placeholder or remove
            fixedContent = fixedContent.replace(jsxMapRegex, '<!-- JSX content removed -->');
            fixes += mapMatches.length;
            this.log(`Removed ${mapMatches.length} JSX map functions from ${filePath}`, 'fix');
        }

        return { content: fixedContent, fixes };
    }

    fixMimetypeIssue() {
        const mimetypePath = 'mimetype';
        if (fs.existsSync(mimetypePath)) {
            const content = fs.readFileSync(mimetypePath, 'utf8');
            if (content.trim() !== 'application/epub+zip') {
                fs.writeFileSync(mimetypePath, 'application/epub+zip');
                this.log('Fixed mimetype file content', 'fix');
                return 1;
            }
        }
        return 0;
    }

    processFile(filePath) {
        try {
            let content = fs.readFileSync(filePath, 'utf8');
            let totalFixes = 0;

            // Apply all fixes
            const unclosedResult = this.fixUnclosedDivs(content, filePath);
            content = unclosedResult.content;
            totalFixes += unclosedResult.fixes;

            const attrResult = this.fixInvalidAttributes(content, filePath);
            content = attrResult.content;
            totalFixes += attrResult.fixes;

            const entityResult = this.fixEntityReferences(content, filePath);
            content = entityResult.content;
            totalFixes += entityResult.fixes;

            const jsxResult = this.fixJSXArtifacts(content, filePath);
            content = jsxResult.content;
            totalFixes += jsxResult.fixes;

            // Write back if changes were made
            if (totalFixes > 0) {
                fs.writeFileSync(filePath, content);
                this.fixedFiles.push({ file: filePath, fixes: totalFixes });
                this.log(`Applied ${totalFixes} total fixes to ${filePath}`, 'success');
            } else {
                this.log(`No fixes needed for ${filePath}`, 'info');
            }

        } catch (error) {
            this.log(`Error processing ${filePath}: ${error.message}`, 'error');
            this.errors.push({ file: filePath, error: error.message });
        }
    }

    async run() {
        this.log('🚀 Starting Critical XHTML Issue Fixes', 'info');

        try {
            // Fix mimetype issue
            const mimetypeFixes = this.fixMimetypeIssue();

            // Find and process all XHTML files
            const fs = require('fs');
            const files = fs.readdirSync('OEBPS/text')
                           .filter(file => file.endsWith('.xhtml'))
                           .map(file => `OEBPS/text/${file}`);

            this.log(`Found ${files.length} XHTML files to process`, 'info');

            for (const file of files) {
                this.processFile(file);
            }

            // Summary
            const totalFiles = this.fixedFiles.length;
            const totalFixes = this.fixedFiles.reduce((sum, f) => sum + f.fixes, 0) + mimetypeFixes;

            this.log(`\n=== SUMMARY ===`, 'info');
            this.log(`Files processed: ${files.length}`, 'info');
            this.log(`Files with fixes: ${totalFiles}`, 'success');
            this.log(`Total fixes applied: ${totalFixes}`, 'success');
            this.log(`Errors encountered: ${this.errors.length}`, this.errors.length > 0 ? 'error' : 'info');

            if (this.errors.length > 0) {
                this.log('\nErrors:', 'error');
                for (const error of this.errors) {
                    this.log(`${error.file}: ${error.error}`, 'error');
                }
            }

            return this.errors.length === 0 ? 0 : 1;

        } catch (error) {
            this.log(`Fatal error: ${error.message}`, 'error');
            console.error(error.stack);
            return 2;
        }
    }
}

// Run if called directly
if (require.main === module) {
    const fixer = new CriticalXHTMLFixer();
    fixer.run().then(process.exit);
}

module.exports = CriticalXHTMLFixer;
