# EPUB Validation Command

You are an EPUB validation specialist. Your task is to thoroughly validate all XHTML files and the EPUB package structure in the REBRANDED_OUTPUT directory to ensure error-free EPUB distribution.

## Validation Tasks

1. **XHTML Structure Validation**
   - Validate all XHTML files in `xhtml/` and `templates/` directories
   - Check for proper XML/XHTML syntax
   - Verify DOCTYPE declarations
   - Ensure proper namespace declarations
   - Check for unclosed tags or malformed markup

2. **EPUB Package Validation**
   - Validate `content.opf` structure and metadata
   - Check `META-INF/container.xml` configuration
   - Verify `mimetype` file exists and is correct
   - Validate navigation document (`nav.xhtml`)
   - Check spine order and manifest entries

3. **Content Validation**
   - Verify all referenced images exist in `images/` directory
   - Check all CSS files exist in `styles/` directory
   - Validate font file references in `fonts/` directory
   - Ensure all internal links are valid
   - Check for missing alt attributes on images

4. **Standards Compliance**
   - Validate against EPUB 3.0 specifications
   - Check accessibility requirements (ARIA labels, semantic HTML)
   - Verify language attributes
   - Check character encoding (UTF-8)

## Execution Steps

1. Run the XHTML validation subagent: `./scripts/subagents/validate-xhtml.sh`
2. Run the EPUB package validator: `./scripts/subagents/validate-epub-package.sh`
3. Run epubcheck if available: `java -jar ../epubcheck/epubcheck.jar` on built EPUB
4. Generate validation report with all errors and warnings
5. Provide actionable recommendations for fixing any issues

## Output Format

Provide a structured validation report:
- ✅ Passed checks (summary)
- ⚠️ Warnings (with file locations and line numbers)
- ❌ Errors (with file locations and detailed descriptions)
- 📋 Recommendations for fixes

## Success Criteria

The EPUB is considered valid when:
- Zero critical errors
- All XHTML files are well-formed
- All assets are present and referenced correctly
- Package structure meets EPUB 3.0 standards
- Content is accessible and follows best practices
