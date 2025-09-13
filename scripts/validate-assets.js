#!/usr/bin/env node

/**
 * Asset Validation Script for EPUB
 * Validates that all referenced assets exist and reports broken links
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

class EPUBAssetValidator {
    constructor() {
        this.errors = [];
        this.warnings = [];
        this.stats = {
            filesChecked: 0,
            imagesFound: 0,
            stylesheetsFound: 0,
            fontsFound: 0,
            brokenReferences: 0
        };
    }

    log(message, type = 'info') {
        const timestamp = new Date().toISOString();
        const prefix = {
            info: '📋',
            success: '✅',
            warning: '⚠️',
            error: '❌'
        }[type] || '📋';
        
        console.log(`${prefix} [${timestamp}] ${message}`);
    }

    validateFile(filePath) {
        if (!fs.existsSync(filePath)) {
            this.errors.push(`File not found: ${filePath}`);
            return false;
        }
        return true;
    }

    extractReferences(content, filePath) {
        const references = {
            images: [],
            stylesheets: [],
            fonts: []
        };

        // Extract image references
        const imageRegex = /(?:src|href)=["']([^"']*\.(?:png|jpe?g|gif|svg|webp))["']/gi;
        let match;
        while ((match = imageRegex.exec(content)) !== null) {
            references.images.push({
                path: match[1],
                line: this.getLineNumber(content, match.index),
                file: filePath
            });
        }

        // Extract stylesheet references
        const cssRegex = /(?:href)=["']([^"']*\.css)["']/gi;
        while ((match = cssRegex.exec(content)) !== null) {
            references.stylesheets.push({
                path: match[1],
                line: this.getLineNumber(content, match.index),
                file: filePath
            });
        }

        // Extract font references from CSS
        if (filePath.endsWith('.css')) {
            const fontRegex = /url\(['"]?([^'"]*\.(?:woff2?|ttf|eot|otf))['"]?\)/gi;
            while ((match = fontRegex.exec(content)) !== null) {
                references.fonts.push({
                    path: match[1],
                    line: this.getLineNumber(content, match.index),
                    file: filePath
                });
            }
        }

        return references;
    }

    getLineNumber(content, index) {
        return content.substring(0, index).split('\n').length;
    }

    resolveAssetPath(referencePath, sourceFile) {
        // Handle relative paths from OEBPS/text/ or OEBPS/styles/
        const sourceDir = path.dirname(sourceFile);
        const absolutePath = path.resolve(sourceDir, referencePath);
        
        // Convert to relative path from project root
        return path.relative(process.cwd(), absolutePath);
    }

    validateAssetReferences() {
        this.log('Starting asset reference validation...', 'info');

        const filesToCheck = [
            ...this.globFiles('OEBPS/text/*.xhtml'),
            ...this.globFiles('OEBPS/styles/*.css')
        ];

        for (const filePath of filesToCheck) {
            if (!this.validateFile(filePath)) continue;

            this.stats.filesChecked++;
            const content = fs.readFileSync(filePath, 'utf8');
            const references = this.extractReferences(content, filePath);

            // Validate image references
            for (const ref of references.images) {
                this.stats.imagesFound++;
                const assetPath = this.resolveAssetPath(ref.path, filePath);
                
                if (!fs.existsSync(assetPath)) {
                    this.errors.push({
                        type: 'missing_asset',
                        message: `Missing image: ${ref.path}`,
                        file: ref.file,
                        line: ref.line,
                        assetPath: assetPath
                    });
                    this.stats.brokenReferences++;
                }
            }

            // Validate stylesheet references
            for (const ref of references.stylesheets) {
                this.stats.stylesheetsFound++;
                const assetPath = this.resolveAssetPath(ref.path, filePath);
                
                if (!fs.existsSync(assetPath)) {
                    this.errors.push({
                        type: 'missing_asset',
                        message: `Missing stylesheet: ${ref.path}`,
                        file: ref.file,
                        line: ref.line,
                        assetPath: assetPath
                    });
                    this.stats.brokenReferences++;
                }
            }

            // Validate font references
            for (const ref of references.fonts) {
                this.stats.fontsFound++;
                const assetPath = this.resolveAssetPath(ref.path, filePath);
                
                if (!fs.existsSync(assetPath)) {
                    this.errors.push({
                        type: 'missing_asset',
                        message: `Missing font: ${ref.path}`,
                        file: ref.file,
                        line: ref.line,
                        assetPath: assetPath
                    });
                    this.stats.brokenReferences++;
                }
            }
        }
    }

    validateOPFManifest() {
        this.log('Validating OPF manifest...', 'info');
        
        const opfPath = 'OEBPS/content.opf';
        if (!this.validateFile(opfPath)) return;

        const opfContent = fs.readFileSync(opfPath, 'utf8');
        const manifestItems = this.extractManifestItems(opfContent);

        for (const item of manifestItems) {
            const assetPath = path.join('OEBPS', item.href);
            if (!fs.existsSync(assetPath)) {
                this.errors.push({
                    type: 'missing_manifest_item',
                    message: `Manifest item not found: ${item.href}`,
                    file: opfPath,
                    id: item.id,
                    mediaType: item.mediaType
                });
            }
        }
    }

    extractManifestItems(opfContent) {
        const items = [];
        const itemRegex = /<item[^>]+id=["']([^"']+)["'][^>]+href=["']([^"']+)["'][^>]+media-type=["']([^"']+)["'][^>]*\/>/g;
        
        let match;
        while ((match = itemRegex.exec(opfContent)) !== null) {
            items.push({
                id: match[1],
                href: match[2],
                mediaType: match[3]
            });
        }
        
        return items;
    }

    globFiles(pattern) {
        try {
            // Support patterns like "OEBPS/text/*.xhtml" or "OEBPS/styles/*.css"
            const m = pattern.match(/^(.*)\/(\*\.[^\/]+)$/);
            let cmd;
            if (m) {
                const dir = m[1];
                const name = m[2]; // e.g., *.xhtml
                cmd = `find "${dir}" -type f -name "${name}" 2>/dev/null || true`;
            } else {
                // Fallback: treat as a directory
                cmd = `find "${pattern}" -type f 2>/dev/null || true`;
            }
            const result = execSync(cmd, { encoding: 'utf8' });
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
        fs.writeFileSync('asset-validation-report.json', JSON.stringify(report, null, 2));

        // Generate markdown report
        let markdown = `# EPUB Asset Validation Report\n\n`;
        markdown += `Generated: ${report.timestamp}\n\n`;
        markdown += `## Summary\n\n`;
        markdown += `- **Status**: ${report.summary.passed ? '✅ PASSED' : '❌ FAILED'}\n`;
        markdown += `- **Files Checked**: ${this.stats.filesChecked}\n`;
        markdown += `- **Images Referenced**: ${this.stats.imagesFound}\n`;
        markdown += `- **Stylesheets Referenced**: ${this.stats.stylesheetsFound}\n`;
        markdown += `- **Fonts Referenced**: ${this.stats.fontsFound}\n`;
        markdown += `- **Broken References**: ${this.stats.brokenReferences}\n`;
        markdown += `- **Total Issues**: ${report.summary.totalIssues}\n\n`;

        if (this.errors.length > 0) {
            markdown += `## Errors\n\n`;
            for (const error of this.errors) {
                markdown += `- **${error.type}**: ${error.message}\n`;
                markdown += `  - File: \`${error.file}\`\n`;
                if (error.line) markdown += `  - Line: ${error.line}\n`;
                if (error.assetPath) markdown += `  - Expected Path: \`${error.assetPath}\`\n`;
                markdown += `\n`;
            }
        }

        if (this.warnings.length > 0) {
            markdown += `## Warnings\n\n`;
            for (const warning of this.warnings) {
                markdown += `- ${warning}\n`;
            }
        }

        fs.writeFileSync('asset-validation-report.md', markdown);
        
        return report;
    }

    async run() {
        this.log('🚀 Starting EPUB Asset Validation', 'info');
        
        try {
            this.validateAssetReferences();
            this.validateOPFManifest();
            
            const report = this.generateReport();
            
            if (report.summary.passed) {
                this.log('✅ All asset references are valid!', 'success');
                return 0;
            } else {
                this.log(`❌ Found ${report.summary.totalIssues} issues`, 'error');
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
    const validator = new EPUBAssetValidator();
    validator.run().then(process.exit);
}

module.exports = EPUBAssetValidator;
