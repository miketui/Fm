#!/usr/bin/env node

/**
 * Multi-Format EPUB Validator
 * Validates EPUB files against different versions and specifications
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const xml2js = require('xml2js');

class MultiFormatEPUBValidator {
    constructor(options = {}) {
        this.options = {
            validateVersions: options.validateVersions || ['2.0.1', '3.0', '3.1', '3.2', '3.3'],
            includeAccessibility: options.includeAccessibility || true,
            validateFixed: options.validateFixed || false,
            ...options
        };
        
        this.results = {};
        this.errors = [];
        this.detectedVersion = null;
        this.detectedFeatures = [];
    }

    log(message, type = 'info') {
        const timestamp = new Date().toISOString();
        const prefix = {
            info: '📋',
            success: '✅',
            warning: '⚠️',
            error: '❌',
            version: '📚'
        }[type] || '📋';
        
        console.log(`${prefix} [${timestamp}] ${message}`);
    }

    // Detect EPUB version from OPF file
    async detectEPUBVersion() {
        this.log('Detecting EPUB version and features...', 'version');
        
        const opfPath = 'OEBPS/content.opf';
        if (!fs.existsSync(opfPath)) {
            throw new Error('content.opf not found');
        }

        const opfContent = fs.readFileSync(opfPath, 'utf8');
        const parser = new xml2js.Parser();
        
        try {
            const result = await parser.parseStringPromise(opfContent);
            const packageElement = result.package;
            
            // Extract version from package element
            this.detectedVersion = packageElement.$.version || '2.0';
            
            // Detect features based on content
            this.detectedFeatures = this.analyzeFeatures(opfContent, packageElement);
            
            this.log(`Detected EPUB version: ${this.detectedVersion}`, 'success');
            this.log(`Detected features: ${this.detectedFeatures.join(', ')}`, 'info');
            
            return {
                version: this.detectedVersion,
                features: this.detectedFeatures,
                packageElement
            };
            
        } catch (error) {
            throw new Error(`Failed to parse OPF: ${error.message}`);
        }
    }

    // Analyze EPUB features
    analyzeFeatures(opfContent, packageElement) {
        const features = [];
        
        // Check for EPUB 3+ features
        if (opfContent.includes('properties="nav"')) {
            features.push('EPUB3_Navigation');
        }
        
        if (opfContent.includes('media-overlay')) {
            features.push('Media_Overlays');
        }
        
        if (opfContent.includes('scripted')) {
            features.push('Scripting');
        }
        
        if (opfContent.includes('svg')) {
            features.push('SVG');
        }
        
        if (opfContent.includes('mathml')) {
            features.push('MathML');
        }
        
        // Check for fixed-layout
        const metadata = packageElement.metadata?.[0];
        if (metadata) {
            const metaElements = metadata.meta || [];
            for (const meta of metaElements) {
                if (meta.$ && meta.$.property === 'rendition:layout' && meta._ === 'pre-paginated') {
                    features.push('Fixed_Layout');
                }
                if (meta.$ && meta.$.name === 'fixed-layout' && meta.$.content === 'true') {
                    features.push('Fixed_Layout');
                }
            }
        }
        
        // Check for accessibility features
        if (opfContent.includes('schema:accessMode')) {
            features.push('Accessibility_Metadata');
        }
        
        // Check for fonts
        if (opfContent.includes('font/')) {
            features.push('Embedded_Fonts');
        }
        
        // Check for audio/video
        if (opfContent.includes('audio/') || opfContent.includes('video/')) {
            features.push('Audio_Video');
        }
        
        return features;
    }

    // Validate against specific EPUB version
    async validateVersion(version, tempEpubPath) {
        this.log(`Validating against EPUB ${version}...`, 'version');
        
        const validation = {
            version,
            passed: false,
            errors: [],
            warnings: [],
            infos: [],
            compatible: false
        };

        try {
            // Run epubcheck with version-specific flags
            let command = `epubcheck "${tempEpubPath}"`;
            
            // Add version-specific validation flags
            if (version === '2.0.1') {
                command += ' --mode exp';
            }
            
            const output = execSync(command, { encoding: 'utf8', stdio: 'pipe' });
            
            // Parse epubcheck output
            const lines = output.split('\n');
            let checkPassed = false;
            
            for (const line of lines) {
                if (line.includes('Check finished with no errors or warnings')) {
                    checkPassed = true;
                    validation.passed = true;
                } else if (line.startsWith('ERROR')) {
                    validation.errors.push(line);
                } else if (line.startsWith('WARNING')) {
                    validation.warnings.push(line);
                } else if (line.startsWith('INFO')) {
                    validation.infos.push(line);
                }
            }
            
            // Determine compatibility
            validation.compatible = this.checkVersionCompatibility(version, this.detectedVersion, this.detectedFeatures);
            
        } catch (error) {
            const errorOutput = error.stdout || error.stderr || error.message;
            validation.errors.push(`Validation failed: ${errorOutput}`);
        }

        return validation;
    }

    // Check if EPUB is compatible with target version
    checkVersionCompatibility(targetVersion, detectedVersion, features) {
        const versionNumbers = {
            '2.0': 2.0,
            '2.0.1': 2.01,
            '3.0': 3.0,
            '3.1': 3.1,
            '3.2': 3.2,
            '3.3': 3.3
        };

        const target = versionNumbers[targetVersion] || 2.0;
        const detected = versionNumbers[detectedVersion] || 2.0;
        
        // Basic version compatibility
        if (detected <= target) {
            // Check if features are supported in target version
            const incompatibleFeatures = this.getIncompatibleFeatures(targetVersion, features);
            return incompatibleFeatures.length === 0;
        }
        
        return false;
    }

    // Get features that are incompatible with target version
    getIncompatibleFeatures(targetVersion, features) {
        const featureSupport = {
            '2.0': [],
            '2.0.1': [],
            '3.0': ['EPUB3_Navigation', 'Media_Overlays', 'SVG', 'MathML', 'Fixed_Layout', 'Embedded_Fonts'],
            '3.1': ['EPUB3_Navigation', 'Media_Overlays', 'SVG', 'MathML', 'Fixed_Layout', 'Embedded_Fonts', 'Scripting'],
            '3.2': ['EPUB3_Navigation', 'Media_Overlays', 'SVG', 'MathML', 'Fixed_Layout', 'Embedded_Fonts', 'Scripting', 'Audio_Video'],
            '3.3': ['EPUB3_Navigation', 'Media_Overlays', 'SVG', 'MathML', 'Fixed_Layout', 'Embedded_Fonts', 'Scripting', 'Audio_Video', 'Accessibility_Metadata']
        };

        const supportedFeatures = featureSupport[targetVersion] || [];
        return features.filter(feature => !supportedFeatures.includes(feature));
    }

    // Create temporary EPUB file for validation
    async createTempEPUB() {
        const tempDir = fs.mkdtempSync('/tmp/epub-validation-');
        const epubPath = path.join(tempDir, 'test.epub');
        
        this.log(`Creating temporary EPUB: ${epubPath}`, 'info');
        
        try {
            // Create EPUB structure
            const epubStructureDir = path.join(tempDir, 'epub');
            fs.mkdirSync(epubStructureDir);
            fs.mkdirSync(path.join(epubStructureDir, 'OEBPS'));
            fs.mkdirSync(path.join(epubStructureDir, 'META-INF'));
            
            // Copy files
            if (fs.existsSync('OEBPS')) {
                this.copyRecursive('OEBPS', path.join(epubStructureDir, 'OEBPS'));
            }
            
            // Create mimetype
            fs.writeFileSync(path.join(epubStructureDir, 'mimetype'), 'application/epub+zip');
            
            // Create container.xml
            const containerXML = `<?xml version="1.0"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>`;
            fs.writeFileSync(path.join(epubStructureDir, 'META-INF', 'container.xml'), containerXML);
            
            // Create ZIP
            process.chdir(epubStructureDir);
            execSync(`zip -0 -X ../test.epub mimetype`);
            execSync(`zip -r ../test.epub META-INF/ OEBPS/`);
            
            return { epubPath, tempDir };
            
        } catch (error) {
            throw new Error(`Failed to create temporary EPUB: ${error.message}`);
        }
    }

    // Helper function to copy directories recursively
    copyRecursive(src, dest) {
        if (fs.statSync(src).isDirectory()) {
            if (!fs.existsSync(dest)) {
                fs.mkdirSync(dest);
            }
            const files = fs.readdirSync(src);
            for (const file of files) {
                this.copyRecursive(path.join(src, file), path.join(dest, file));
            }
        } else {
            fs.copyFileSync(src, dest);
        }
    }

    // Generate comprehensive validation report
    generateReport(versionInfo, validationResults) {
        const report = {
            timestamp: new Date().toISOString(),
            detectedVersion: versionInfo.version,
            detectedFeatures: versionInfo.features,
            validationResults,
            summary: {
                totalVersions: this.options.validateVersions.length,
                passedVersions: Object.values(validationResults).filter(r => r.passed).length,
                compatibleVersions: Object.values(validationResults).filter(r => r.compatible).length,
                totalErrors: Object.values(validationResults).reduce((sum, r) => sum + r.errors.length, 0),
                totalWarnings: Object.values(validationResults).reduce((sum, r) => sum + r.warnings.length, 0)
            },
            recommendations: this.generateRecommendations(versionInfo, validationResults)
        };

        // Save JSON report
        fs.writeFileSync(path.resolve('multi-format-validation-report.json'), JSON.stringify(report, null, 2));

        // Generate markdown report
        const markdown = this.generateMarkdownReport(report);
        fs.writeFileSync(path.resolve('multi-format-validation-report.md'), markdown);

        return report;
    }

    generateRecommendations(versionInfo, validationResults) {
        const recommendations = [];
        
        // Version upgrade recommendations
        const latestCompatible = Object.keys(validationResults)
            .filter(version => validationResults[version].compatible)
            .sort((a, b) => parseFloat(b) - parseFloat(a))[0];
            
        if (latestCompatible && latestCompatible !== versionInfo.version) {
            recommendations.push({
                type: 'version_upgrade',
                severity: 'medium',
                message: `Consider upgrading to EPUB ${latestCompatible} for better compatibility`,
                currentVersion: versionInfo.version,
                recommendedVersion: latestCompatible
            });
        }

        // Feature-based recommendations
        if (versionInfo.features.includes('Fixed_Layout')) {
            recommendations.push({
                type: 'fixed_layout',
                severity: 'info',
                message: 'Fixed-layout detected - ensure proper viewport meta tags',
                details: 'Fixed-layout EPUBs require careful testing across different reading systems'
            });
        }

        if (!versionInfo.features.includes('Accessibility_Metadata')) {
            recommendations.push({
                type: 'accessibility',
                severity: 'high',
                message: 'Add accessibility metadata for better compliance',
                details: 'Include schema:accessMode, accessibilityFeature, and accessibilityHazard metadata'
            });
        }

        // Error-based recommendations
        for (const [version, result] of Object.entries(validationResults)) {
            if (result.errors.length > 0) {
                const commonErrors = this.categorizeErrors(result.errors);
                for (const [errorType, count] of Object.entries(commonErrors)) {
                    recommendations.push({
                        type: 'validation_error',
                        severity: 'high',
                        message: `Fix ${errorType} errors for EPUB ${version} compatibility`,
                        count,
                        version
                    });
                }
            }
        }

        return recommendations;
    }

    categorizeErrors(errors) {
        const categories = {};
        
        for (const error of errors) {
            let category = 'other';
            
            if (error.includes('XHTML')) {
                category = 'XHTML validation';
            } else if (error.includes('OPF')) {
                category = 'OPF structure';
            } else if (error.includes('CSS')) {
                category = 'CSS validation';
            } else if (error.includes('navigation')) {
                category = 'Navigation';
            } else if (error.includes('media-type')) {
                category = 'Media types';
            }
            
            categories[category] = (categories[category] || 0) + 1;
        }
        
        return categories;
    }

    generateMarkdownReport(report) {
        let markdown = `# Multi-Format EPUB Validation Report\n\n`;
        markdown += `Generated: ${report.timestamp}\n\n`;
        
        markdown += `## EPUB Information\n\n`;
        markdown += `- **Detected Version**: ${report.detectedVersion}\n`;
        markdown += `- **Features**: ${report.detectedFeatures.join(', ') || 'None detected'}\n\n`;
        
        markdown += `## Validation Summary\n\n`;
        markdown += `- **Versions Tested**: ${report.summary.totalVersions}\n`;
        markdown += `- **Passed Validation**: ${report.summary.passedVersions}\n`;
        markdown += `- **Compatible Versions**: ${report.summary.compatibleVersions}\n`;
        markdown += `- **Total Errors**: ${report.summary.totalErrors}\n`;
        markdown += `- **Total Warnings**: ${report.summary.totalWarnings}\n\n`;
        
        markdown += `## Version Compatibility Matrix\n\n`;
        markdown += `| Version | Validation | Compatibility | Errors | Warnings |\n`;
        markdown += `|---------|------------|---------------|--------|---------|\n`;
        
        for (const [version, result] of Object.entries(report.validationResults)) {
            const validation = result.passed ? '✅' : '❌';
            const compatibility = result.compatible ? '✅' : '❌';
            markdown += `| ${version} | ${validation} | ${compatibility} | ${result.errors.length} | ${result.warnings.length} |\n`;
        }
        markdown += `\n`;
        
        if (report.recommendations.length > 0) {
            markdown += `## Recommendations\n\n`;
            
            const severityOrder = { 'high': 1, 'medium': 2, 'low': 3, 'info': 4 };
            const sortedRecs = report.recommendations.sort((a, b) => 
                (severityOrder[a.severity] || 5) - (severityOrder[b.severity] || 5)
            );
            
            for (const rec of sortedRecs) {
                const icon = {
                    'high': '🔴',
                    'medium': '🟡',
                    'low': '🟢',
                    'info': '🔵'
                }[rec.severity] || '⚪';
                
                markdown += `### ${icon} ${rec.message}\n`;
                markdown += `**Severity**: ${rec.severity}\n\n`;
                
                if (rec.details) {
                    markdown += `${rec.details}\n\n`;
                }
                
                if (rec.currentVersion && rec.recommendedVersion) {
                    markdown += `Current: ${rec.currentVersion} → Recommended: ${rec.recommendedVersion}\n\n`;
                }
                
                if (rec.count && rec.version) {
                    markdown += `Count: ${rec.count} errors in EPUB ${rec.version}\n\n`;
                }
            }
        }
        
        // Detailed validation results
        for (const [version, result] of Object.entries(report.validationResults)) {
            if (result.errors.length > 0 || result.warnings.length > 0) {
                markdown += `## EPUB ${version} Details\n\n`;
                
                if (result.errors.length > 0) {
                    markdown += `### Errors\n\n`;
                    for (const error of result.errors) {
                        markdown += `- ${error}\n`;
                    }
                    markdown += `\n`;
                }
                
                if (result.warnings.length > 0) {
                    markdown += `### Warnings\n\n`;
                    for (const warning of result.warnings) {
                        markdown += `- ${warning}\n`;
                    }
                    markdown += `\n`;
                }
            }
        }
        
        return markdown;
    }

    // Main execution method
    async run() {
        this.log('🚀 Starting Multi-Format EPUB Validation', 'version');
        
        const originalDir = process.cwd();
        
        try {
            // Detect EPUB version and features
            const versionInfo = await this.detectEPUBVersion();
            
            // Create temporary EPUB
            const { epubPath, tempDir } = await this.createTempEPUB();
            
            // Return to original directory after EPUB creation
            process.chdir(originalDir);
            
            // Validate against each version
            const validationResults = {};
            
            for (const version of this.options.validateVersions) {
                validationResults[version] = await this.validateVersion(version, epubPath);
            }
            
            // Cleanup
            fs.rmSync(tempDir, { recursive: true, force: true });
            
            // Generate report
            const report = this.generateReport(versionInfo, validationResults);
            
            // Summary
            this.log(`✅ Validation completed for ${this.options.validateVersions.length} versions`, 'success');
            this.log(`📊 ${report.summary.compatibleVersions}/${report.summary.totalVersions} versions compatible`, 'info');
            
            if (report.summary.totalErrors > 0) {
                this.log(`⚠️  ${report.summary.totalErrors} total errors found`, 'warning');
                return 1;
            } else {
                this.log('🎉 No errors found across all versions', 'success');
                return 0;
            }
            
        } catch (error) {
            this.log(`Fatal error: ${error.message}`, 'error');
            console.error(error.stack);
            return 2;
        }
    }
}

// Install xml2js if not available
try {
    require('xml2js');
} catch (error) {
    console.log('Installing xml2js dependency...');
    try {
        execSync('npm install xml2js', { stdio: 'inherit' });
    } catch (installError) {
        console.error('Failed to install xml2js. Please run: npm install xml2js');
        process.exit(1);
    }
}

// CLI handling
if (require.main === module) {
    const args = process.argv.slice(2);
    const options = {
        validateVersions: args.includes('--all-versions') ? 
            ['2.0.1', '3.0', '3.1', '3.2', '3.3'] :
            args.find(arg => arg.startsWith('--versions='))?.split('=')[1]?.split(',') || ['3.0', '3.2', '3.3'],
        includeAccessibility: !args.includes('--no-accessibility'),
        validateFixed: args.includes('--include-fixed-layout')
    };
    
    if (args.includes('--help')) {
        console.log(`
Multi-Format EPUB Validator

Usage: node multi-format-validator.js [options]

Options:
  --versions=VERSION_LIST        Comma-separated list of versions to validate (default: 3.0,3.2,3.3)
  --all-versions                 Validate against all supported versions
  --no-accessibility             Skip accessibility validation
  --include-fixed-layout         Include fixed-layout specific validation
  --help                         Show this help message

Examples:
  node multi-format-validator.js                                    # Validate against EPUB 3.0, 3.2, 3.3
  node multi-format-validator.js --all-versions                     # Validate against all versions
  node multi-format-validator.js --versions=3.0,3.3                # Validate against specific versions
  node multi-format-validator.js --include-fixed-layout             # Include fixed-layout tests
        `);
        process.exit(0);
    }
    
    const validator = new MultiFormatEPUBValidator(options);
    validator.run().then(process.exit);
}

module.exports = MultiFormatEPUBValidator;