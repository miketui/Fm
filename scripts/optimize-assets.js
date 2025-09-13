#!/usr/bin/env node

/**
 * EPUB Asset Optimization Tool
 * Analyzes and optimizes images, fonts, and other assets for EPUB files
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

class EPUBAssetOptimizer {
    constructor(options = {}) {
        this.options = {
            dryRun: options.dryRun || false,
            maxImageSize: options.maxImageSize || 500 * 1024, // 500KB
            maxFontSize: options.maxFontSize || 200 * 1024,   // 200KB
            jpegQuality: options.jpegQuality || 85,
            pngQuality: options.pngQuality || 90,
            webpQuality: options.webpQuality || 85,
            ...options
        };
        
        this.optimizations = [];
        this.errors = [];
        this.stats = {
            imagesAnalyzed: 0,
            fontsAnalyzed: 0,
            totalSavings: 0,
            filesOptimized: 0
        };
    }

    log(message, type = 'info') {
        const timestamp = new Date().toISOString();
        const prefix = {
            info: '🔧',
            success: '✅',
            warning: '⚠️',
            error: '❌',
            optimize: '📦'
        }[type] || '🔧';
        
        console.log(`${prefix} [${timestamp}] ${message}`);
    }

    // Check if optimization tools are available
    checkOptimizationTools() {
        const tools = {
            imagemagick: { cmd: 'convert -version', name: 'ImageMagick' },
            jpegoptim: { cmd: 'jpegoptim --version', name: 'jpegoptim' },
            pngcrush: { cmd: 'pngcrush -version', name: 'pngcrush' },
            fonttools: { cmd: 'python3 -c "import fontTools"', name: 'fontTools' }
        };

        const available = {};
        const missing = [];

        for (const [tool, config] of Object.entries(tools)) {
            try {
                execSync(config.cmd, { stdio: 'pipe' });
                available[tool] = true;
                this.log(`${config.name} available`, 'success');
            } catch (error) {
                available[tool] = false;
                missing.push(config.name);
                this.log(`${config.name} not available`, 'warning');
            }
        }

        if (missing.length > 0) {
            this.log(`Missing optimization tools: ${missing.join(', ')}`, 'warning');
            this.log('Install with: apt-get install imagemagick jpegoptim pngcrush python3-fonttools', 'info');
        }

        return available;
    }

    // Analyze image files
    analyzeImages() {
        this.log('Analyzing images for optimization opportunities...', 'info');
        
        const imageDir = 'OEBPS/images';
        if (!fs.existsSync(imageDir)) {
            this.log('No images directory found', 'warning');
            return [];
        }

        const imageFiles = fs.readdirSync(imageDir).filter(file => 
            /\.(jpe?g|png|gif|webp)$/i.test(file)
        );

        const recommendations = [];

        for (const file of imageFiles) {
            const filePath = path.join(imageDir, file);
            const stats = fs.statSync(filePath);
            const size = stats.size;
            
            this.stats.imagesAnalyzed++;

            const analysis = {
                file: filePath,
                size,
                sizeKB: Math.round(size / 1024),
                type: path.extname(file).toLowerCase(),
                recommendations: []
            };

            // Check if image is too large
            if (size > this.options.maxImageSize) {
                analysis.recommendations.push({
                    type: 'size_reduction',
                    message: `Image is ${analysis.sizeKB}KB, consider reducing to under ${Math.round(this.options.maxImageSize / 1024)}KB`,
                    severity: 'high',
                    estimatedSavings: size - this.options.maxImageSize
                });
            }

            // Get image dimensions if ImageMagick is available
            try {
                const identify = execSync(`identify "${filePath}"`, { encoding: 'utf8' });
                const dimensions = identify.match(/(\d+)x(\d+)/);
                if (dimensions) {
                    analysis.width = parseInt(dimensions[1]);
                    analysis.height = parseInt(dimensions[2]);
                    
                    // Check for overly large dimensions
                    if (analysis.width > 2000 || analysis.height > 2000) {
                        analysis.recommendations.push({
                            type: 'dimension_reduction',
                            message: `High resolution (${analysis.width}x${analysis.height}), consider resizing for EPUB`,
                            severity: 'medium',
                            suggestion: 'Resize to max 1200px width for optimal EPUB performance'
                        });
                    }
                }
            } catch (error) {
                // ImageMagick not available or file issue
            }

            // Format-specific recommendations
            if (analysis.type === '.jpeg' || analysis.type === '.jpg') {
                analysis.recommendations.push({
                    type: 'jpeg_optimization',
                    message: 'JPEG can be optimized with quality adjustment',
                    severity: 'low',
                    tool: 'jpegoptim',
                    command: `jpegoptim --max=${this.options.jpegQuality} "${filePath}"`
                });
            } else if (analysis.type === '.png') {
                analysis.recommendations.push({
                    type: 'png_optimization',
                    message: 'PNG can be compressed without quality loss',
                    severity: 'low',
                    tool: 'pngcrush',
                    command: `pngcrush -reduce -brute "${filePath}" "${filePath}.tmp" && mv "${filePath}.tmp" "${filePath}"`
                });
            }

            // WebP conversion suggestion for large images
            if (size > 100 * 1024 && analysis.type !== '.webp') {
                analysis.recommendations.push({
                    type: 'webp_conversion',
                    message: 'Consider converting to WebP format for better compression',
                    severity: 'low',
                    tool: 'cwebp',
                    estimatedSavings: size * 0.3, // Rough estimate
                    command: `cwebp -q ${this.options.webpQuality} "${filePath}" -o "${filePath.replace(/\.[^.]+$/, '.webp')}"`
                });
            }

            if (analysis.recommendations.length > 0) {
                recommendations.push(analysis);
            }
        }

        return recommendations;
    }

    // Analyze font files
    analyzeFonts() {
        this.log('Analyzing fonts for optimization opportunities...', 'info');
        
        const fontDir = 'OEBPS/fonts';
        if (!fs.existsSync(fontDir)) {
            this.log('No fonts directory found', 'warning');
            return [];
        }

        const fontFiles = fs.readdirSync(fontDir).filter(file => 
            /\.(woff2?|ttf|otf|eot)$/i.test(file)
        );

        const recommendations = [];

        for (const file of fontFiles) {
            const filePath = path.join(fontDir, file);
            const stats = fs.statSync(filePath);
            const size = stats.size;
            
            this.stats.fontsAnalyzed++;

            const analysis = {
                file: filePath,
                size,
                sizeKB: Math.round(size / 1024),
                type: path.extname(file).toLowerCase(),
                recommendations: []
            };

            // Check if font is too large
            if (size > this.options.maxFontSize) {
                analysis.recommendations.push({
                    type: 'font_size',
                    message: `Font is ${analysis.sizeKB}KB, consider subsetting or optimization`,
                    severity: 'high',
                    estimatedSavings: size - this.options.maxFontSize
                });
            }

            // Font format recommendations
            if (analysis.type === '.ttf' || analysis.type === '.otf') {
                analysis.recommendations.push({
                    type: 'format_conversion',
                    message: 'Convert to WOFF2 for better compression and web compatibility',
                    severity: 'medium',
                    tool: 'fonttools',
                    estimatedSavings: size * 0.4, // WOFF2 is typically 40% smaller
                    command: `fonttools ttLib.woff2 compress "${filePath}"`
                });
            } else if (analysis.type === '.woff') {
                analysis.recommendations.push({
                    type: 'woff2_conversion',
                    message: 'Upgrade to WOFF2 for better compression',
                    severity: 'low',
                    tool: 'fonttools',
                    estimatedSavings: size * 0.2,
                    command: `fonttools ttLib.woff2 compress "${filePath}"`
                });
            }

            // Subsetting recommendation for large fonts
            if (size > 100 * 1024) {
                analysis.recommendations.push({
                    type: 'font_subsetting',
                    message: 'Consider subsetting font to include only required characters',
                    severity: 'medium',
                    tool: 'fonttools',
                    suggestion: 'Subset to Latin characters and common punctuation',
                    command: `fonttools subset "${filePath}" --unicodes=U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD`
                });
            }

            if (analysis.recommendations.length > 0) {
                recommendations.push(analysis);
            }
        }

        return recommendations;
    }

    // Analyze CSS files for unused styles
    analyzeCSS() {
        this.log('Analyzing CSS for optimization opportunities...', 'info');
        
        const recommendations = [];
        const cssFiles = ['OEBPS/styles/style.css', 'OEBPS/styles/fonts.css', 'OEBPS/styles/print.css'];
        
        for (const cssFile of cssFiles) {
            if (!fs.existsSync(cssFile)) continue;
            
            const content = fs.readFileSync(cssFile, 'utf8');
            const size = content.length;
            
            const analysis = {
                file: cssFile,
                size,
                sizeKB: Math.round(size / 1024),
                recommendations: []
            };

            // Check for large CSS files
            if (size > 50 * 1024) {
                analysis.recommendations.push({
                    type: 'css_size',
                    message: `Large CSS file (${analysis.sizeKB}KB), consider splitting or minification`,
                    severity: 'medium'
                });
            }

            // Look for potential optimizations
            const comments = (content.match(/\/\*[\s\S]*?\*\//g) || []).join('').length;
            if (comments > size * 0.1) {
                analysis.recommendations.push({
                    type: 'css_comments',
                    message: 'Remove comments to reduce file size',
                    severity: 'low',
                    estimatedSavings: comments
                });
            }

            // Check for repeated selectors or properties
            const lines = content.split('\n');
            const duplicateLines = lines.filter((line, index, arr) => 
                line.trim() && arr.indexOf(line) !== index
            );
            
            if (duplicateLines.length > 10) {
                analysis.recommendations.push({
                    type: 'css_duplication',
                    message: 'Found duplicate CSS rules that could be consolidated',
                    severity: 'low',
                    count: duplicateLines.length
                });
            }

            if (analysis.recommendations.length > 0) {
                recommendations.push(analysis);
            }
        }

        return recommendations;
    }

    // Execute optimizations (if not dry run)
    async executeOptimizations(recommendations) {
        if (this.options.dryRun) {
            this.log('Dry run mode - no files will be modified', 'info');
            return;
        }

        const tools = this.checkOptimizationTools();
        
        for (const category of recommendations) {
            for (const item of category) {
                for (const rec of item.recommendations) {
                    if (rec.command && rec.tool && tools[rec.tool]) {
                        try {
                            this.log(`Optimizing ${item.file}...`, 'optimize');
                            
                            // Create backup
                            const backup = `${item.file}.backup`;
                            fs.copyFileSync(item.file, backup);
                            
                            // Execute optimization
                            execSync(rec.command, { stdio: 'pipe' });
                            
                            // Check results
                            const newSize = fs.statSync(item.file).size;
                            const savings = item.size - newSize;
                            
                            if (savings > 0) {
                                this.stats.totalSavings += savings;
                                this.stats.filesOptimized++;
                                this.log(`Saved ${Math.round(savings / 1024)}KB on ${path.basename(item.file)}`, 'success');
                                
                                // Remove backup if successful
                                fs.unlinkSync(backup);
                            } else {
                                // Restore original if no savings
                                fs.copyFileSync(backup, item.file);
                                fs.unlinkSync(backup);
                                this.log(`No improvement for ${path.basename(item.file)}`, 'info');
                            }
                            
                        } catch (error) {
                            this.log(`Failed to optimize ${item.file}: ${error.message}`, 'error');
                            this.errors.push({ file: item.file, error: error.message });
                            
                            // Restore backup if exists
                            const backup = `${item.file}.backup`;
                            if (fs.existsSync(backup)) {
                                fs.copyFileSync(backup, item.file);
                                fs.unlinkSync(backup);
                            }
                        }
                    }
                }
            }
        }
    }

    // Generate optimization report
    generateReport(imageRecs, fontRecs, cssRecs) {
        const report = {
            timestamp: new Date().toISOString(),
            options: this.options,
            stats: this.stats,
            images: imageRecs,
            fonts: fontRecs,
            css: cssRecs,
            errors: this.errors,
            summary: {
                totalFiles: this.stats.imagesAnalyzed + this.stats.fontsAnalyzed,
                totalRecommendations: [
                    ...imageRecs.flatMap(img => img.recommendations),
                    ...fontRecs.flatMap(font => font.recommendations),
                    ...cssRecs.flatMap(css => css.recommendations)
                ].length,
                estimatedSavings: this.calculateEstimatedSavings(imageRecs, fontRecs, cssRecs),
                actualSavings: this.stats.totalSavings
            }
        };

        // Save JSON report
        fs.writeFileSync('asset-optimization-report.json', JSON.stringify(report, null, 2));

        // Generate markdown report
        const markdown = this.generateMarkdownReport(report);
        fs.writeFileSync('asset-optimization-report.md', markdown);

        return report;
    }

    calculateEstimatedSavings(imageRecs, fontRecs, cssRecs) {
        let total = 0;
        
        [...imageRecs, ...fontRecs, ...cssRecs].forEach(item => {
            item.recommendations.forEach(rec => {
                if (rec.estimatedSavings) {
                    total += rec.estimatedSavings;
                }
            });
        });
        
        return total;
    }

    generateMarkdownReport(report) {
        let markdown = `# EPUB Asset Optimization Report\n\n`;
        markdown += `Generated: ${report.timestamp}\n\n`;
        markdown += `## Summary\n\n`;
        markdown += `- **Mode**: ${report.options.dryRun ? 'Dry Run (Analysis Only)' : 'Optimization Executed'}\n`;
        markdown += `- **Images Analyzed**: ${report.stats.imagesAnalyzed}\n`;
        markdown += `- **Fonts Analyzed**: ${report.stats.fontsAnalyzed}\n`;
        markdown += `- **Total Recommendations**: ${report.summary.totalRecommendations}\n`;
        
        if (report.options.dryRun) {
            markdown += `- **Estimated Savings**: ${Math.round(report.summary.estimatedSavings / 1024)}KB\n\n`;
        } else {
            markdown += `- **Files Optimized**: ${report.stats.filesOptimized}\n`;
            markdown += `- **Actual Savings**: ${Math.round(report.stats.totalSavings / 1024)}KB\n\n`;
        }

        if (report.images.length > 0) {
            markdown += `## Image Optimization\n\n`;
            for (const img of report.images) {
                markdown += `### ${path.basename(img.file)}\n`;
                markdown += `- **Size**: ${img.sizeKB}KB\n`;
                if (img.width && img.height) {
                    markdown += `- **Dimensions**: ${img.width}x${img.height}\n`;
                }
                markdown += `- **Recommendations**:\n`;
                for (const rec of img.recommendations) {
                    markdown += `  - **${rec.type}**: ${rec.message}\n`;
                    if (rec.estimatedSavings) {
                        markdown += `    - Estimated savings: ${Math.round(rec.estimatedSavings / 1024)}KB\n`;
                    }
                    if (rec.command) {
                        markdown += `    - Command: \`${rec.command}\`\n`;
                    }
                }
                markdown += `\n`;
            }
        }

        if (report.fonts.length > 0) {
            markdown += `## Font Optimization\n\n`;
            for (const font of report.fonts) {
                markdown += `### ${path.basename(font.file)}\n`;
                markdown += `- **Size**: ${font.sizeKB}KB\n`;
                markdown += `- **Format**: ${font.type.toUpperCase()}\n`;
                markdown += `- **Recommendations**:\n`;
                for (const rec of font.recommendations) {
                    markdown += `  - **${rec.type}**: ${rec.message}\n`;
                    if (rec.estimatedSavings) {
                        markdown += `    - Estimated savings: ${Math.round(rec.estimatedSavings / 1024)}KB\n`;
                    }
                    if (rec.command) {
                        markdown += `    - Command: \`${rec.command}\`\n`;
                    }
                }
                markdown += `\n`;
            }
        }

        if (report.css.length > 0) {
            markdown += `## CSS Optimization\n\n`;
            for (const css of report.css) {
                markdown += `### ${path.basename(css.file)}\n`;
                markdown += `- **Size**: ${css.sizeKB}KB\n`;
                markdown += `- **Recommendations**:\n`;
                for (const rec of css.recommendations) {
                    markdown += `  - **${rec.type}**: ${rec.message}\n`;
                    if (rec.count) {
                        markdown += `    - Count: ${rec.count}\n`;
                    }
                    if (rec.estimatedSavings) {
                        markdown += `    - Estimated savings: ${Math.round(rec.estimatedSavings / 1024)}KB\n`;
                    }
                }
                markdown += `\n`;
            }
        }

        if (report.errors.length > 0) {
            markdown += `## Errors\n\n`;
            for (const error of report.errors) {
                markdown += `- **${error.file}**: ${error.error}\n`;
            }
            markdown += `\n`;
        }

        return markdown;
    }

    // Main execution method
    async run() {
        this.log('🚀 Starting EPUB Asset Optimization Analysis', 'optimize');
        
        try {
            // Check available tools
            this.checkOptimizationTools();
            
            // Analyze all asset types
            const imageRecs = this.analyzeImages();
            const fontRecs = this.analyzeFonts();
            const cssRecs = this.analyzeCSS();
            
            // Execute optimizations if not dry run
            if (!this.options.dryRun) {
                await this.executeOptimizations([imageRecs, fontRecs, cssRecs]);
            }
            
            // Generate report
            const report = this.generateReport(imageRecs, fontRecs, cssRecs);
            
            // Summary
            if (report.summary.totalRecommendations === 0) {
                this.log('✅ No optimization opportunities found', 'success');
                return 0;
            } else {
                this.log(`📊 Found ${report.summary.totalRecommendations} optimization opportunities`, 'info');
                if (report.options.dryRun) {
                    this.log(`💾 Estimated savings: ${Math.round(report.summary.estimatedSavings / 1024)}KB`, 'info');
                    this.log('Run without --dry-run to execute optimizations', 'info');
                } else {
                    this.log(`💾 Actual savings: ${Math.round(report.stats.totalSavings / 1024)}KB`, 'success');
                }
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
        dryRun: args.includes('--dry-run') || args.includes('-n'),
        maxImageSize: parseInt(args.find(arg => arg.startsWith('--max-image-size='))?.split('=')[1]) || 500 * 1024,
        maxFontSize: parseInt(args.find(arg => arg.startsWith('--max-font-size='))?.split('=')[1]) || 200 * 1024,
        jpegQuality: parseInt(args.find(arg => arg.startsWith('--jpeg-quality='))?.split('=')[1]) || 85,
        pngQuality: parseInt(args.find(arg => arg.startsWith('--png-quality='))?.split('=')[1]) || 90
    };
    
    if (args.includes('--help')) {
        console.log(`
EPUB Asset Optimization Tool

Usage: node optimize-assets.js [options]

Options:
  --dry-run, -n                  Analyze only, don't modify files
  --max-image-size=SIZE          Maximum image size in bytes (default: 500KB)
  --max-font-size=SIZE           Maximum font size in bytes (default: 200KB)
  --jpeg-quality=QUALITY         JPEG compression quality 1-100 (default: 85)
  --png-quality=QUALITY          PNG compression quality 1-100 (default: 90)
  --help                         Show this help message

Examples:
  node optimize-assets.js --dry-run           # Analyze only
  node optimize-assets.js                     # Execute optimizations
  node optimize-assets.js --jpeg-quality=75   # Lower JPEG quality
        `);
        process.exit(0);
    }
    
    const optimizer = new EPUBAssetOptimizer(options);
    optimizer.run().then(process.exit);
}

module.exports = EPUBAssetOptimizer;