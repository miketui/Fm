#!/usr/bin/env node

/**
 * EPUB Performance Metrics Tracker
 * Tracks validation time, build performance, and EPUB characteristics
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

class EPUBPerformanceTracker {
    constructor() {
        this.metricsFile = 'performance-metrics.json';
        this.metrics = {
            timestamp: new Date().toISOString(),
            validation: {},
            structure: {},
            assets: {},
            performance: {},
            trends: []
        };
    }

    log(message, type = 'info') {
        const timestamp = new Date().toISOString();
        const prefix = {
            info: '📊',
            success: '✅',
            warning: '⚠️',
            error: '❌',
            perf: '⚡'
        }[type] || '📊';
        
        console.log(`${prefix} [${timestamp}] ${message}`);
    }

    // Measure validation performance
    async measureValidationPerformance() {
        this.log('Measuring validation performance...', 'perf');
        
        const validationMetrics = {
            epubcheck: {},
            assetValidation: {},
            integrationTests: {},
            regressionTests: {}
        };

        // Measure epubcheck performance
        try {
            const start = Date.now();
            execSync('./validate-epub.sh', { stdio: 'pipe' });
            validationMetrics.epubcheck = {
                duration: Date.now() - start,
                status: 'passed',
                timestamp: new Date().toISOString()
            };
            this.log(`epubcheck completed in ${validationMetrics.epubcheck.duration}ms`, 'success');
        } catch (error) {
            validationMetrics.epubcheck = {
                duration: -1,
                status: 'failed',
                error: error.message,
                timestamp: new Date().toISOString()
            };
            this.log('epubcheck failed', 'error');
        }

        // Measure asset validation performance
        try {
            const start = Date.now();
            execSync('node scripts/validate-assets.js', { stdio: 'pipe' });
            validationMetrics.assetValidation = {
                duration: Date.now() - start,
                status: 'passed',
                timestamp: new Date().toISOString()
            };
            this.log(`Asset validation completed in ${validationMetrics.assetValidation.duration}ms`, 'success');
        } catch (error) {
            validationMetrics.assetValidation = {
                duration: -1,
                status: 'failed',
                error: error.message,
                timestamp: new Date().toISOString()
            };
            this.log('Asset validation failed', 'error');
        }

        // Measure integration tests performance
        try {
            const start = Date.now();
            execSync('node tests/integration/epub-reader-test.js', { stdio: 'pipe' });
            validationMetrics.integrationTests = {
                duration: Date.now() - start,
                status: 'passed',
                timestamp: new Date().toISOString()
            };
            this.log(`Integration tests completed in ${validationMetrics.integrationTests.duration}ms`, 'success');
        } catch (error) {
            validationMetrics.integrationTests = {
                duration: -1,
                status: 'failed',
                error: error.message,
                timestamp: new Date().toISOString()
            };
            this.log('Integration tests failed', 'error');
        }

        // Measure regression tests performance
        try {
            const start = Date.now();
            execSync('node tests/regression/path-reference-test.js --allow-regressions', { stdio: 'pipe' });
            validationMetrics.regressionTests = {
                duration: Date.now() - start,
                status: 'passed',
                timestamp: new Date().toISOString()
            };
            this.log(`Regression tests completed in ${validationMetrics.regressionTests.duration}ms`, 'success');
        } catch (error) {
            validationMetrics.regressionTests = {
                duration: -1,
                status: 'failed',
                error: error.message,
                timestamp: new Date().toISOString()
            };
            this.log('Regression tests failed', 'error');
        }

        this.metrics.validation = validationMetrics;
    }

    // Analyze EPUB structure metrics
    analyzeStructureMetrics() {
        this.log('Analyzing EPUB structure metrics...', 'info');
        
        const structureMetrics = {
            files: {},
            directories: {},
            content: {}
        };

        // Count files by type
        const fileTypes = {
            xhtml: this.countFiles('OEBPS/text/*.xhtml'),
            css: this.countFiles('OEBPS/styles/*.css'),
            images: this.countFiles('OEBPS/images/*'),
            fonts: this.countFiles('OEBPS/fonts/*')
        };

        structureMetrics.files = {
            ...fileTypes,
            total: Object.values(fileTypes).reduce((sum, count) => sum + count, 0)
        };

        // Directory structure
        structureMetrics.directories = {
            oebps: fs.existsSync('OEBPS'),
            text: fs.existsSync('OEBPS/text'),
            styles: fs.existsSync('OEBPS/styles'),
            images: fs.existsSync('OEBPS/images'),
            fonts: fs.existsSync('OEBPS/fonts'),
            metaInf: fs.existsSync('META-INF')
        };

        // Content analysis
        if (fs.existsSync('OEBPS/content.opf')) {
            const opfContent = fs.readFileSync('OEBPS/content.opf', 'utf8');
            structureMetrics.content = {
                manifestItems: (opfContent.match(/<item/g) || []).length,
                spineItems: (opfContent.match(/<itemref/g) || []).length,
                hasNavigation: opfContent.includes('properties="nav"'),
                hasAccessibilityMetadata: opfContent.includes('schema:accessibility')
            };
        }

        this.metrics.structure = structureMetrics;
    }

    // Analyze asset metrics
    analyzeAssetMetrics() {
        this.log('Analyzing asset metrics...', 'info');
        
        const assetMetrics = {
            sizes: {},
            totals: {},
            optimization: {}
        };

        // Calculate sizes by category
        const categories = {
            text: 'OEBPS/text',
            styles: 'OEBPS/styles',
            images: 'OEBPS/images',
            fonts: 'OEBPS/fonts'
        };

        for (const [category, dir] of Object.entries(categories)) {
            if (fs.existsSync(dir)) {
                const size = this.calculateDirectorySize(dir);
                assetMetrics.sizes[category] = {
                    bytes: size,
                    mb: Math.round(size / 1024 / 1024 * 100) / 100,
                    files: this.countFiles(`${dir}/*`)
                };
            } else {
                assetMetrics.sizes[category] = { bytes: 0, mb: 0, files: 0 };
            }
        }

        // Calculate totals
        assetMetrics.totals = {
            size: Object.values(assetMetrics.sizes).reduce((sum, cat) => sum + cat.bytes, 0),
            files: Object.values(assetMetrics.sizes).reduce((sum, cat) => sum + cat.files, 0)
        };
        assetMetrics.totals.mb = Math.round(assetMetrics.totals.size / 1024 / 1024 * 100) / 100;

        // Optimization suggestions
        assetMetrics.optimization = {
            largeImages: this.findLargeAssets('OEBPS/images', 500 * 1024), // > 500KB
            largeFonts: this.findLargeAssets('OEBPS/fonts', 100 * 1024),   // > 100KB
            duplicateFiles: this.findDuplicateAssets(),
            unusedAssets: this.findUnusedAssets()
        };

        this.metrics.assets = assetMetrics;
    }

    // Measure build performance
    measureBuildPerformance() {
        this.log('Measuring build performance...', 'perf');
        
        const performanceMetrics = {
            system: {},
            git: {},
            npm: {}
        };

        // System metrics
        try {
            performanceMetrics.system = {
                node: process.version,
                platform: process.platform,
                arch: process.arch,
                memory: {
                    used: Math.round(process.memoryUsage().heapUsed / 1024 / 1024 * 100) / 100,
                    total: Math.round(process.memoryUsage().heapTotal / 1024 / 1024 * 100) / 100
                }
            };
        } catch (error) {
            this.log(`Error collecting system metrics: ${error.message}`, 'warning');
        }

        // Git metrics
        try {
            performanceMetrics.git = {
                branch: execSync('git branch --show-current', { encoding: 'utf8' }).trim(),
                commit: execSync('git rev-parse HEAD', { encoding: 'utf8' }).trim().substring(0, 8),
                status: execSync('git status --porcelain', { encoding: 'utf8' }).trim().split('\n').length
            };
        } catch (error) {
            this.log(`Error collecting git metrics: ${error.message}`, 'warning');
        }

        // NPM metrics
        try {
            if (fs.existsSync('package.json')) {
                const packageJson = JSON.parse(fs.readFileSync('package.json', 'utf8'));
                performanceMetrics.npm = {
                    version: packageJson.version,
                    scripts: Object.keys(packageJson.scripts || {}).length,
                    dependencies: Object.keys(packageJson.dependencies || {}).length,
                    devDependencies: Object.keys(packageJson.devDependencies || {}).length
                };
            }
        } catch (error) {
            this.log(`Error collecting npm metrics: ${error.message}`, 'warning');
        }

        this.metrics.performance = performanceMetrics;
    }

    // Helper methods
    countFiles(pattern) {
        try {
            const result = execSync(`find ${pattern.replace('*', '\\*')} -type f 2>/dev/null | wc -l`, { encoding: 'utf8' });
            return parseInt(result.trim()) || 0;
        } catch (error) {
            return 0;
        }
    }

    calculateDirectorySize(dir) {
        try {
            const result = execSync(`du -sb "${dir}" 2>/dev/null | cut -f1`, { encoding: 'utf8' });
            return parseInt(result.trim()) || 0;
        } catch (error) {
            return 0;
        }
    }

    findLargeAssets(dir, threshold) {
        try {
            if (!fs.existsSync(dir)) return [];
            
            const result = execSync(`find "${dir}" -type f -size +${threshold}c 2>/dev/null`, { encoding: 'utf8' });
            return result.trim().split('\n').filter(f => f.length > 0).map(file => ({
                file: path.relative(process.cwd(), file),
                size: fs.statSync(file).size
            }));
        } catch (error) {
            return [];
        }
    }

    findDuplicateAssets() {
        // Simple duplicate detection based on file size
        try {
            const files = this.globFiles('OEBPS/**/*');
            const sizeMap = new Map();
            
            for (const file of files) {
                if (fs.statSync(file).isFile()) {
                    const size = fs.statSync(file).size;
                    if (!sizeMap.has(size)) {
                        sizeMap.set(size, []);
                    }
                    sizeMap.get(size).push(file);
                }
            }
            
            const duplicates = [];
            for (const [size, fileList] of sizeMap.entries()) {
                if (fileList.length > 1) {
                    duplicates.push({ size, files: fileList });
                }
            }
            
            return duplicates;
        } catch (error) {
            return [];
        }
    }

    findUnusedAssets() {
        // Simplified unused asset detection
        try {
            const imageFiles = this.globFiles('OEBPS/images/*');
            const xhtmlFiles = this.globFiles('OEBPS/text/*.xhtml');
            const cssFiles = this.globFiles('OEBPS/styles/*.css');
            
            const unused = [];
            
            for (const imageFile of imageFiles) {
                const imageName = path.basename(imageFile);
                let found = false;
                
                // Check if referenced in any XHTML or CSS file
                for (const textFile of [...xhtmlFiles, ...cssFiles]) {
                    const content = fs.readFileSync(textFile, 'utf8');
                    if (content.includes(imageName)) {
                        found = true;
                        break;
                    }
                }
                
                if (!found) {
                    unused.push(path.relative(process.cwd(), imageFile));
                }
            }
            
            return unused;
        } catch (error) {
            return [];
        }
    }

    globFiles(pattern) {
        try {
            const result = execSync(`find ${pattern.replace('*', '\\*')} -type f 2>/dev/null`, { encoding: 'utf8' });
            return result.trim().split('\n').filter(f => f.length > 0);
        } catch (error) {
            return [];
        }
    }

    // Load historical metrics for trend analysis
    loadHistoricalMetrics() {
        if (fs.existsSync(this.metricsFile)) {
            try {
                return JSON.parse(fs.readFileSync(this.metricsFile, 'utf8'));
            } catch (error) {
                this.log(`Error loading historical metrics: ${error.message}`, 'warning');
            }
        }
        return { trends: [] };
    }

    // Calculate trends
    calculateTrends(historical) {
        const trends = [];
        
        if (historical.trends && historical.trends.length > 0) {
            const latest = historical.trends[historical.trends.length - 1];
            
            // Size trend
            if (latest.assets && latest.assets.totals) {
                const sizeDiff = this.metrics.assets.totals.size - latest.assets.totals.size;
                trends.push({
                    metric: 'total_size',
                    change: sizeDiff,
                    percentage: latest.assets.totals.size > 0 ? 
                        Math.round(sizeDiff / latest.assets.totals.size * 10000) / 100 : 0,
                    direction: sizeDiff > 0 ? 'increased' : sizeDiff < 0 ? 'decreased' : 'stable'
                });
            }
            
            // File count trend
            if (latest.structure && latest.structure.files) {
                const filesDiff = this.metrics.structure.files.total - latest.structure.files.total;
                trends.push({
                    metric: 'file_count',
                    change: filesDiff,
                    percentage: latest.structure.files.total > 0 ? 
                        Math.round(filesDiff / latest.structure.files.total * 10000) / 100 : 0,
                    direction: filesDiff > 0 ? 'increased' : filesDiff < 0 ? 'decreased' : 'stable'
                });
            }
            
            // Validation performance trend
            if (latest.validation && latest.validation.epubcheck && this.metrics.validation.epubcheck) {
                const timeDiff = this.metrics.validation.epubcheck.duration - latest.validation.epubcheck.duration;
                trends.push({
                    metric: 'validation_time',
                    change: timeDiff,
                    percentage: latest.validation.epubcheck.duration > 0 ? 
                        Math.round(timeDiff / latest.validation.epubcheck.duration * 10000) / 100 : 0,
                    direction: timeDiff > 0 ? 'slower' : timeDiff < 0 ? 'faster' : 'stable'
                });
            }
        }
        
        this.metrics.trends = trends;
    }

    // Generate comprehensive report
    generateReport() {
        const report = {
            ...this.metrics,
            summary: {
                totalSize: this.metrics.assets.totals.mb,
                totalFiles: this.metrics.structure.files.total,
                validationPassed: this.metrics.validation.epubcheck?.status === 'passed',
                optimizationIssues: this.metrics.assets.optimization.largeImages.length + 
                                   this.metrics.assets.optimization.unusedAssets.length,
                performanceScore: this.calculatePerformanceScore()
            }
        };

        // Save JSON report
        fs.writeFileSync('performance-metrics-report.json', JSON.stringify(report, null, 2));

        // Generate markdown report
        const markdown = this.generateMarkdownReport(report);
        fs.writeFileSync('performance-metrics-report.md', markdown);

        return report;
    }

    calculatePerformanceScore() {
        let score = 100;
        
        // Deduct points for validation failures
        if (this.metrics.validation.epubcheck?.status !== 'passed') score -= 25;
        if (this.metrics.validation.assetValidation?.status !== 'passed') score -= 15;
        if (this.metrics.validation.integrationTests?.status !== 'passed') score -= 15;
        
        // Deduct points for large size
        if (this.metrics.assets.totals.mb > 50) score -= 20;
        else if (this.metrics.assets.totals.mb > 25) score -= 10;
        
        // Deduct points for optimization issues
        score -= Math.min(this.metrics.assets.optimization.largeImages.length * 5, 20);
        score -= Math.min(this.metrics.assets.optimization.unusedAssets.length * 3, 15);
        
        return Math.max(score, 0);
    }

    generateMarkdownReport(report) {
        let markdown = `# EPUB Performance Metrics Report\n\n`;
        markdown += `Generated: ${report.timestamp}\n\n`;
        
        markdown += `## Summary\n\n`;
        markdown += `- **Performance Score**: ${report.summary.performanceScore}/100\n`;
        markdown += `- **Total Size**: ${report.summary.totalSize} MB\n`;
        markdown += `- **Total Files**: ${report.summary.totalFiles}\n`;
        markdown += `- **Validation Status**: ${report.summary.validationPassed ? '✅ PASSED' : '❌ FAILED'}\n`;
        markdown += `- **Optimization Issues**: ${report.summary.optimizationIssues}\n\n`;
        
        markdown += `## Validation Performance\n\n`;
        const val = report.validation;
        markdown += `| Test | Duration | Status |\n`;
        markdown += `|------|----------|--------|\n`;
        markdown += `| epubcheck | ${val.epubcheck?.duration || 'N/A'}ms | ${val.epubcheck?.status || 'N/A'} |\n`;
        markdown += `| Asset Validation | ${val.assetValidation?.duration || 'N/A'}ms | ${val.assetValidation?.status || 'N/A'} |\n`;
        markdown += `| Integration Tests | ${val.integrationTests?.duration || 'N/A'}ms | ${val.integrationTests?.status || 'N/A'} |\n`;
        markdown += `| Regression Tests | ${val.regressionTests?.duration || 'N/A'}ms | ${val.regressionTests?.status || 'N/A'} |\n\n`;
        
        markdown += `## Asset Breakdown\n\n`;
        const assets = report.assets.sizes;
        for (const [category, data] of Object.entries(assets)) {
            markdown += `- **${category}**: ${data.mb} MB (${data.files} files)\n`;
        }
        markdown += '\n';
        
        if (report.trends.length > 0) {
            markdown += `## Trends\n\n`;
            for (const trend of report.trends) {
                const direction = trend.direction === 'increased' || trend.direction === 'slower' ? '📈' : 
                                 trend.direction === 'decreased' || trend.direction === 'faster' ? '📉' : '📊';
                markdown += `- **${trend.metric}**: ${direction} ${trend.direction} by ${Math.abs(trend.change)} (${Math.abs(trend.percentage)}%)\n`;
            }
            markdown += '\n';
        }
        
        if (report.assets.optimization.largeImages.length > 0) {
            markdown += `## Large Images (>500KB)\n\n`;
            for (const img of report.assets.optimization.largeImages) {
                markdown += `- \`${img.file}\` (${Math.round(img.size/1024)}KB)\n`;
            }
            markdown += '\n';
        }
        
        if (report.assets.optimization.unusedAssets.length > 0) {
            markdown += `## Potentially Unused Assets\n\n`;
            for (const asset of report.assets.optimization.unusedAssets) {
                markdown += `- \`${asset}\`\n`;
            }
            markdown += '\n';
        }
        
        return markdown;
    }

    // Save metrics to historical data
    saveToHistory() {
        const historical = this.loadHistoricalMetrics();
        historical.trends = historical.trends || [];
        historical.trends.push(this.metrics);
        
        // Keep only last 50 entries
        if (historical.trends.length > 50) {
            historical.trends = historical.trends.slice(-50);
        }
        
        fs.writeFileSync(this.metricsFile, JSON.stringify(historical, null, 2));
        this.log(`Saved metrics to ${this.metricsFile}`, 'success');
    }

    // Main execution
    async run() {
        this.log('🚀 Starting EPUB Performance Metrics Collection', 'perf');
        
        try {
            // Load historical data for trend analysis
            const historical = this.loadHistoricalMetrics();
            
            // Collect all metrics
            await this.measureValidationPerformance();
            this.analyzeStructureMetrics();
            this.analyzeAssetMetrics();
            this.measureBuildPerformance();
            
            // Calculate trends
            this.calculateTrends(historical);
            
            // Generate report
            const report = this.generateReport();
            
            // Save to history
            this.saveToHistory();
            
            this.log(`📊 Performance Score: ${report.summary.performanceScore}/100`, 'perf');
            this.log('✅ Performance metrics collection completed', 'success');
            
            return report.summary.performanceScore >= 80 ? 0 : 1;
            
        } catch (error) {
            this.log(`Fatal error: ${error.message}`, 'error');
            console.error(error.stack);
            return 2;
        }
    }
}

// Run if called directly
if (require.main === module) {
    const tracker = new EPUBPerformanceTracker();
    tracker.run().then(process.exit);
}

module.exports = EPUBPerformanceTracker;