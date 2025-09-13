#!/usr/bin/env node

/**
 * Regression Tests for Path References
 * Prevents future path reference issues in EPUB structure
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

class PathReferenceRegressionTest {
    constructor() {
        this.baselineFile = 'tests/regression/path-reference-baseline.json';
        this.errors = [];
        this.warnings = [];
        this.currentState = {
            paths: new Set(),
            references: new Map(),
            brokenLinks: []
        };
    }

    log(message, type = 'info') {
        const timestamp = new Date().toISOString();
        const prefix = {
            info: '📋',
            success: '✅',
            warning: '⚠️',
            error: '❌',
            test: '🧪'
        }[type] || '📋';
        
        console.log(`${prefix} [${timestamp}] ${message}`);
    }

    // Collect all current path references
    collectCurrentState() {
        this.log('Collecting current path references...', 'info');
        
        // Get all XHTML files
        const xhtmlFiles = this.globFiles('OEBPS/text/*.xhtml');
        
        // Get all CSS files
        const cssFiles = this.globFiles('OEBPS/styles/*.css');
        
        // Process XHTML files
        for (const file of xhtmlFiles) {
            this.processXHTMLFile(file);
        }
        
        // Process CSS files
        for (const file of cssFiles) {
            this.processCSSFile(file);
        }
        
        // Process OPF file
        this.processOPFFile('OEBPS/content.opf');
        
        return {
            paths: Array.from(this.currentState.paths),
            references: Object.fromEntries(this.currentState.references),
            brokenLinks: this.currentState.brokenLinks
        };
    }

    processXHTMLFile(filePath) {
        const content = fs.readFileSync(filePath, 'utf8');
        const relativePath = path.relative(process.cwd(), filePath);
        
        // Extract image references
        const imgRegex = /src=["']([^"']+)["']/g;
        let match;
        while ((match = imgRegex.exec(content)) !== null) {
            const refPath = match[1];
            this.addReference(relativePath, refPath, 'image');
        }
        
        // Extract stylesheet references
        const linkRegex = /href=["']([^"']*\.css)["']/g;
        while ((match = linkRegex.exec(content)) !== null) {
            const refPath = match[1];
            this.addReference(relativePath, refPath, 'stylesheet');
        }
        
        // Extract internal links
        const aRegex = /href=["']([^"']*\.xhtml[^"']*)["']/g;
        while ((match = aRegex.exec(content)) !== null) {
            const refPath = match[1];
            this.addReference(relativePath, refPath, 'internal_link');
        }
    }

    processCSSFile(filePath) {
        const content = fs.readFileSync(filePath, 'utf8');
        const relativePath = path.relative(process.cwd(), filePath);
        
        // Extract font references
        const fontRegex = /url\(['"]?([^'"]*\.[woff2?|ttf|eot|otf])['"]?\)/g;
        let match;
        while ((match = fontRegex.exec(content)) !== null) {
            const refPath = match[1];
            this.addReference(relativePath, refPath, 'font');
        }
        
        // Extract image references in CSS
        const bgImageRegex = /url\(['"]?([^'"]*\.[png|jpg|jpeg|gif|svg])['"]?\)/g;
        while ((match = bgImageRegex.exec(content)) !== null) {
            const refPath = match[1];
            this.addReference(relativePath, refPath, 'background_image');
        }
    }

    processOPFFile(filePath) {
        const content = fs.readFileSync(filePath, 'utf8');
        const relativePath = path.relative(process.cwd(), filePath);
        
        // Extract manifest item references
        const manifestRegex = /<item[^>]+href=["']([^"']+)["'][^>]*\/>/g;
        let match;
        while ((match = manifestRegex.exec(content)) !== null) {
            const refPath = match[1];
            this.addReference(relativePath, refPath, 'manifest_item');
        }
    }

    addReference(sourceFile, referencePath, type) {
        // Resolve the reference to an absolute path
        const sourceDir = path.dirname(sourceFile);
        const resolvedPath = path.resolve(sourceDir, referencePath);
        const normalizedPath = path.relative(process.cwd(), resolvedPath);
        
        // Store the reference
        if (!this.currentState.references.has(sourceFile)) {
            this.currentState.references.set(sourceFile, []);
        }
        
        this.currentState.references.get(sourceFile).push({
            path: referencePath,
            resolvedPath: normalizedPath,
            type,
            exists: fs.existsSync(resolvedPath)
        });
        
        // Add to paths set
        this.currentState.paths.add(normalizedPath);
        
        // Check if path exists
        if (!fs.existsSync(resolvedPath)) {
            this.currentState.brokenLinks.push({
                source: sourceFile,
                reference: referencePath,
                resolved: normalizedPath,
                type
            });
        }
    }

    // Load baseline state
    loadBaseline() {
        if (!fs.existsSync(this.baselineFile)) {
            this.log('No baseline found, creating new baseline...', 'warning');
            return null;
        }
        
        try {
            const baseline = JSON.parse(fs.readFileSync(this.baselineFile, 'utf8'));
            this.log(`Loaded baseline with ${baseline.paths.length} paths`, 'info');
            return baseline;
        } catch (error) {
            this.log(`Error loading baseline: ${error.message}`, 'error');
            return null;
        }
    }

    // Save current state as baseline
    saveBaseline(state) {
        // Ensure directory exists
        const dir = path.dirname(this.baselineFile);
        if (!fs.existsSync(dir)) {
            fs.mkdirSync(dir, { recursive: true });
        }
        
        const baseline = {
            timestamp: new Date().toISOString(),
            version: '1.0.0',
            ...state
        };
        
        fs.writeFileSync(this.baselineFile, JSON.stringify(baseline, null, 2));
        this.log(`Saved baseline with ${baseline.paths.length} paths`, 'success');
    }

    // Compare current state with baseline
    compareWithBaseline(currentState, baseline) {
        const results = {
            newPaths: [],
            removedPaths: [],
            newBrokenLinks: [],
            fixedLinks: [],
            changesSummary: {}
        };
        
        const currentPaths = new Set(currentState.paths);
        const baselinePaths = new Set(baseline.paths);
        const currentBroken = new Set(currentState.brokenLinks.map(link => `${link.source}:${link.reference}`));
        const baselineBroken = new Set(baseline.brokenLinks.map(link => `${link.source}:${link.reference}`));
        
        // Find new and removed paths
        results.newPaths = Array.from(currentPaths).filter(path => !baselinePaths.has(path));
        results.removedPaths = Array.from(baselinePaths).filter(path => !currentPaths.has(path));
        
        // Find new broken links and fixed links
        results.newBrokenLinks = currentState.brokenLinks.filter(link => 
            !baselineBroken.has(`${link.source}:${link.reference}`)
        );
        
        results.fixedLinks = baseline.brokenLinks.filter(link => 
            !currentBroken.has(`${link.source}:${link.reference}`)
        );
        
        // Summary
        results.changesSummary = {
            pathsAdded: results.newPaths.length,
            pathsRemoved: results.removedPaths.length,
            linksFixed: results.fixedLinks.length,
            newBrokenLinks: results.newBrokenLinks.length,
            hasChanges: results.newPaths.length > 0 || results.removedPaths.length > 0 || 
                       results.newBrokenLinks.length > 0 || results.fixedLinks.length > 0
        };
        
        return results;
    }

    // Validate path patterns
    validatePathPatterns(state) {
        const violations = [];
        
        // Expected path patterns for EPUB structure
        const patterns = {
            images: /^OEBPS\/images\/[^\/]+\.(png|jpe?g|gif|svg)$/i,
            styles: /^OEBPS\/styles\/[^\/]+\.css$/,
            fonts: /^OEBPS\/fonts\/[^\/]+\.(woff2?|ttf|eot|otf)$/,
            text: /^OEBPS\/text\/[^\/]+\.xhtml$/,
            manifest: /^OEBPS\/content\.opf$/
        };
        
        for (const filePath of state.paths) {
            let matched = false;
            
            for (const [type, pattern] of Object.entries(patterns)) {
                if (pattern.test(filePath)) {
                    matched = true;
                    break;
                }
            }
            
            if (!matched && fs.existsSync(filePath)) {
                // Check if it's a valid EPUB file we haven't accounted for
                const ext = path.extname(filePath).toLowerCase();
                const validExtensions = ['.xhtml', '.css', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.woff', '.woff2', '.ttf', '.eot', '.otf', '.opf'];
                
                if (validExtensions.includes(ext)) {
                    violations.push({
                        path: filePath,
                        issue: 'File in unexpected location for EPUB structure',
                        suggestion: 'Consider moving to appropriate OEBPS subdirectory'
                    });
                }
            }
        }
        
        return violations;
    }

    // Generate comprehensive report
    generateReport(currentState, baseline, comparison) {
        const report = {
            timestamp: new Date().toISOString(),
            summary: {
                totalPaths: currentState.paths.length,
                brokenLinks: currentState.brokenLinks.length,
                hasBaseline: baseline !== null,
                hasRegressions: comparison ? comparison.newBrokenLinks.length > 0 : false
            },
            currentState,
            comparison,
            pathPatternViolations: this.validatePathPatterns(currentState)
        };
        
        // Save JSON report
        fs.writeFileSync('path-reference-regression-report.json', JSON.stringify(report, null, 2));
        
        // Generate markdown report
        let markdown = `# Path Reference Regression Test Report\n\n`;
        markdown += `Generated: ${report.timestamp}\n\n`;
        markdown += `## Summary\n\n`;
        markdown += `- **Total Paths**: ${report.summary.totalPaths}\n`;
        markdown += `- **Broken Links**: ${report.summary.brokenLinks}\n`;
        markdown += `- **Has Baseline**: ${report.summary.hasBaseline ? '✅ Yes' : '❌ No'}\n`;
        markdown += `- **Regressions**: ${report.summary.hasRegressions ? '❌ Yes' : '✅ None'}\n\n`;
        
        if (currentState.brokenLinks.length > 0) {
            markdown += `## Current Broken Links\n\n`;
            for (const link of currentState.brokenLinks) {
                markdown += `- **${link.type}**: \`${link.reference}\`\n`;
                markdown += `  - Source: \`${link.source}\`\n`;
                markdown += `  - Resolved to: \`${link.resolved}\`\n\n`;
            }
        }
        
        if (comparison && comparison.changesSummary.hasChanges) {
            markdown += `## Changes Since Baseline\n\n`;
            markdown += `- **Paths Added**: ${comparison.changesSummary.pathsAdded}\n`;
            markdown += `- **Paths Removed**: ${comparison.changesSummary.pathsRemoved}\n`;
            markdown += `- **Links Fixed**: ${comparison.changesSummary.linksFixed}\n`;
            markdown += `- **New Broken Links**: ${comparison.changesSummary.newBrokenLinks}\n\n`;
            
            if (comparison.newBrokenLinks.length > 0) {
                markdown += `### New Broken Links (Regressions)\n\n`;
                for (const link of comparison.newBrokenLinks) {
                    markdown += `- **${link.type}**: \`${link.reference}\` in \`${link.source}\`\n`;
                }
                markdown += '\n';
            }
            
            if (comparison.fixedLinks.length > 0) {
                markdown += `### Fixed Links\n\n`;
                for (const link of comparison.fixedLinks) {
                    markdown += `- **${link.type}**: \`${link.reference}\` in \`${link.source}\`\n`;
                }
                markdown += '\n';
            }
        }
        
        if (report.pathPatternViolations.length > 0) {
            markdown += `## Path Pattern Violations\n\n`;
            for (const violation of report.pathPatternViolations) {
                markdown += `- **Path**: \`${violation.path}\`\n`;
                markdown += `  - Issue: ${violation.issue}\n`;
                markdown += `  - Suggestion: ${violation.suggestion}\n\n`;
            }
        }
        
        fs.writeFileSync('path-reference-regression-report.md', markdown);
        
        return report;
    }

    globFiles(pattern) {
        try {
            const result = execSync(`find ${pattern.replace('*', '\\*')} -type f 2>/dev/null || true`, { encoding: 'utf8' });
            return result.trim().split('\n').filter(f => f.length > 0);
        } catch (error) {
            return [];
        }
    }

    async run(options = {}) {
        this.log('🚀 Starting Path Reference Regression Tests', 'info');
        
        try {
            // Collect current state
            const currentState = this.collectCurrentState();
            
            // Load baseline
            const baseline = this.loadBaseline();
            
            let comparison = null;
            if (baseline) {
                // Compare with baseline
                comparison = this.compareWithBaseline(currentState, baseline);
                
                if (comparison.newBrokenLinks.length > 0 && !options.allowRegressions) {
                    this.log(`❌ Found ${comparison.newBrokenLinks.length} new broken links (regressions)`, 'error');
                }
            }
            
            // Generate report
            const report = this.generateReport(currentState, baseline, comparison);
            
            // Update baseline if requested
            if (options.updateBaseline) {
                this.saveBaseline(currentState);
                this.log('Updated baseline with current state', 'success');
            }
            
            // Determine exit code
            const hasRegressions = comparison && comparison.newBrokenLinks.length > 0;
            const hasBrokenLinks = currentState.brokenLinks.length > 0;
            
            if (hasRegressions && !options.allowRegressions) {
                this.log('❌ Regression test FAILED - new broken links detected', 'error');
                return 1;
            } else if (hasBrokenLinks && options.strictMode) {
                this.log('❌ Strict mode FAILED - broken links present', 'error');
                return 1;
            } else {
                this.log('✅ Regression test PASSED', 'success');
                return 0;
            }
            
        } catch (error) {
            this.log(`Fatal error: ${error.message}`, 'error');
            console.error(error.stack);
            return 2;
        }
    }
}

// CLI handling
if (require.main === module) {
    const args = process.argv.slice(2);
    const options = {
        updateBaseline: args.includes('--update-baseline'),
        allowRegressions: args.includes('--allow-regressions'),
        strictMode: args.includes('--strict')
    };
    
    if (args.includes('--help')) {
        console.log(`
Path Reference Regression Test

Usage: node path-reference-test.js [options]

Options:
  --update-baseline   Update the baseline with current state
  --allow-regressions Allow new broken links (don't fail)
  --strict           Fail if any broken links exist
  --help             Show this help message
        `);
        process.exit(0);
    }
    
    const tester = new PathReferenceRegressionTest();
    tester.run(options).then(process.exit);
}

module.exports = PathReferenceRegressionTest;