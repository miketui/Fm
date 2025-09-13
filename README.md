# Curls & Contemplation: A Stylist's Interactive Journey Journal

[![EPUB Validation](https://github.com/miketui/terragon/actions/workflows/validate-epub.yml/badge.svg)](https://github.com/miketui/terragon/actions/workflows/validate-epub.yml)

An interactive EPUB journal for professional hairstylists featuring comprehensive chapters, quizzes, worksheets, and practical strategies for building a successful, conscious hairstyling practice.

## 📚 EPUB Structure

This project follows the standard EPUB 3.0 Open eBook Publication Structure (OEBPS):

```
├── META-INF/
│   └── container.xml          # EPUB container metadata
├── OEBPS/
│   ├── content.opf            # Package document
│   ├── text/                  # XHTML content files
│   │   ├── nav.xhtml          # Navigation document
│   │   ├── 1-TitlePage.xhtml  # Title page
│   │   ├── 2-Copyright.xhtml  # Copyright page
│   │   └── ...               # Chapters and content
│   ├── styles/               # CSS stylesheets
│   │   ├── style.css        # Main styles
│   │   ├── fonts.css        # Font definitions
│   │   └── print.css        # Print media styles
│   ├── images/              # Image assets
│   │   └── ...              # JPEG/PNG images
│   └── fonts/               # Font files
│       └── ...              # WOFF2 font files
└── mimetype                 # EPUB mimetype declaration
```

## 🚀 Quick Start

### Prerequisites

- Node.js (v18 or later)
- npm

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd curls-and-contemplation-epub

# Install dependencies
npm install
```

### Available Scripts

| Command | Description |
|---------|-------------|
| `npm run validate` | Run EPUB validation with epubcheck |
| `npm run validate:assets` | Validate asset references |
| `npm run validate:multi-format` | Validate against multiple EPUB versions |
| `npm run optimize` | Optimize images, fonts, and CSS |
| `npm run optimize:dry-run` | Analyze optimization opportunities (no changes) |
| `npm test` | Run integration and regression tests |
| `npm run test:integration` | Run EPUB reader compatibility tests |
| `npm run test:regression` | Run path reference regression tests |
| `npm run format` | Format XHTML files |
| `npm run metrics` | Generate performance metrics |
| `npm run build` | Full build with validation and testing |
| `npm run build:full` | Full build including multi-format validation and optimization |
| `npm run ci` | CI pipeline (build + metrics) |
| `npm run ci:full` | Full CI pipeline with all validations |

### Development Workflow

```bash
# Format and validate your changes
npm run pre-commit

# Run full build
npm run build

# Generate performance metrics
npm run metrics
```

## 🧪 Testing & Validation

### Validation Pipeline

The project includes comprehensive validation at multiple levels:

1. **EPUB Structure Validation** - Validates against EPUB 3.0 specification
2. **Asset Reference Validation** - Ensures all assets exist and are referenced correctly
3. **Integration Testing** - Tests EPUB compatibility with readers
4. **Regression Testing** - Prevents path reference issues
5. **Performance Metrics** - Tracks build performance and optimization

### Running Tests

```bash
# Run all tests
npm test

# Individual test suites
npm run test:integration      # EPUB reader compatibility
npm run test:regression       # Path reference validation
npm run validate:assets       # Asset validation
```

### Performance Monitoring

```bash
# Generate performance report
npm run metrics

# View reports
cat performance-metrics-report.md
cat asset-validation-report.md
```

## 🔧 Development Tools

### Pre-commit Hooks

The project uses pre-commit hooks to ensure code quality:

```bash
# Install pre-commit (if not already installed)
pip install pre-commit

# Install hooks
pre-commit install

# Run manually
pre-commit run --all-files
```

### Automated Formatting

XHTML files are automatically formatted for consistency:

```bash
# Format all XHTML files
npm run format

# Format specific files
scripts/format-xhtml.sh OEBPS/text/1-TitlePage.xhtml
```

## 📊 Quality Assurance

### Continuous Integration

GitHub Actions automatically runs validation on every push and pull request:

- EPUB structure validation
- Asset reference checking  
- Integration tests
- Performance metrics collection
- Report generation

### Quality Metrics

The project tracks several quality metrics:

- **Performance Score** - Overall quality rating (0-100)
- **Validation Status** - All validation tests pass
- **Asset Optimization** - Image sizes and unused assets
- **Build Performance** - Validation and test execution times

### Accessibility

The EPUB includes comprehensive accessibility features:

- Alternative text for all images
- Proper heading structure
- Semantic markup
- Screen reader compatibility
- Keyboard navigation support

## 🛠️ Troubleshooting

### Common Issues

**epubcheck not found**
```bash
# Install globally
npm install -g epubcheck

# Or use npx (recommended in CI)
npx epubcheck
```

**Asset validation failures**
```bash
# Check asset references
npm run validate:assets

# View detailed report
cat asset-validation-report.md
```

**Path reference issues**
```bash
# Update regression baseline after structural changes
npm run test:regression:update
```

### Getting Help

1. Check the validation reports in the project root
2. Review CI logs for detailed error information
3. Run individual validation steps to isolate issues

## 📈 Performance Optimization

### Asset Optimization

The project includes comprehensive asset optimization capabilities:

**Image Optimization:**
- Automatic detection of oversized images (>500KB)
- JPEG quality optimization with jpegoptim
- PNG compression with pngcrush  
- WebP conversion recommendations for better compression
- Dimension analysis and resize suggestions

**Font Optimization:**
- Font file size analysis (flags fonts >200KB)
- WOFF2 conversion for better compression
- Font subsetting to reduce file size
- Format upgrade recommendations (TTF/OTF → WOFF2)

**CSS Optimization:**
- Large CSS file detection
- Comment removal for size reduction
- Duplicate rule identification
- Minification recommendations

**Usage:**
```bash
# Analyze optimization opportunities
npm run optimize:dry-run

# Execute optimizations
npm run optimize

# Custom optimization settings  
node scripts/optimize-assets.js --max-image-size=300000 --jpeg-quality=80
```

### Multi-Format EPUB Validation

Validates EPUB files against multiple versions and specifications:

**Version Support:**
- EPUB 2.0.1 (legacy compatibility)
- EPUB 3.0, 3.1, 3.2, 3.3 (modern standards)
- Automatic version detection from OPF
- Feature compatibility analysis

**Advanced Features:**
- Fixed-layout EPUB support
- Accessibility metadata validation
- Media overlay detection
- Scripting and interactivity analysis

**Usage:**
```bash
# Validate against default versions (3.0, 3.2, 3.3)
npm run validate:multi-format

# Validate against all supported versions
node scripts/multi-format-validator.js --all-versions

# Validate specific versions
node scripts/multi-format-validator.js --versions=3.0,3.3
```

### Build Performance

Performance metrics track:

- Validation execution time
- Test suite performance
- Asset loading efficiency
- Overall build time
- Optimization effectiveness

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run the full validation suite: `npm run build`
5. Commit with descriptive messages
6. Submit a pull request

### Commit Guidelines

- Use conventional commit format
- Include performance impact in commit messages
- Run `npm run pre-commit` before committing

## 📄 License

All Rights Reserved - MD Warren

## 🔗 Links

- [EPUB 3.0 Specification](https://www.w3.org/publishing/epub3/)
- [epubcheck Documentation](https://github.com/w3c/epubcheck)
- [EPUB Accessibility Guidelines](https://www.w3.org/publishing/epub3/a11y/)