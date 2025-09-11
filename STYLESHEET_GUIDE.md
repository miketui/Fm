# Stylesheet Modification Guide

## Overview

This guide provides instructions for modifying stylesheets in the "Curls & Contemplation" EPUB project. The stylesheets are organized in the `styles/` directory and follow a modular structure for maintainability.

## File Structure

```
styles/
├── fonts.css      # Font definitions and typography
├── style.css      # Main styles for screen display
├── print.css      # Print-optimized styles
├── *.woff2        # Font files
```

## Core Stylesheets

### 1. fonts.css
**Purpose**: Defines all font faces and typography hierarchy

**Key Fonts**:
- **Libre Baskerville**: Body text, quotations, dropcaps
- **Cinzel Decorative**: Chapter titles and decorative elements
- **Montserrat**: Supporting labels, metadata, page numbers

**Modification Guidelines**:
- Font files are located in the same `styles/` directory
- Use relative paths without `../` prefix
- Maintain fallback fonts for better compatibility
- Test font loading across different EPUB readers

**Example**:
```css
@font-face {
  font-family: 'Libre Baskerville';
  src: url('librebaskerville-regular.woff2') format('woff2');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

### 2. style.css
**Purpose**: Main stylesheet for digital reading experience

**Key Sections**:
- Layout and positioning
- Color schemes and themes
- Interactive elements
- Responsive design
- Chapter-specific styling

**Modification Guidelines**:
- Maintain EPUB compatibility
- Use relative units (em, rem, %)
- Ensure accessibility compliance
- Test across different screen sizes

### 3. print.css
**Purpose**: Optimized styles for printing and PDF generation

**Key Features**:
- Print-safe colors (darker text, no backgrounds)
- Page break controls
- Proper margins and typography for print
- Hidden elements that shouldn't print

**Modification Guidelines**:
- Use `@media print` queries
- Specify page sizes and margins
- Avoid color backgrounds
- Use `page-break-before/after` for control

**Example**:
```css
@media print {
  @page {
    size: 8.5in 11in;
    margin: 0.75in;
  }
  
  .quiz-container {
    page-break-before: always;
  }
}
```

## Asset Organization

### Images
- Location: `images/` directory
- Reference: `src="images/filename.ext"`
- Supported formats: JPEG, PNG
- Naming convention: descriptive-kebab-case

### Fonts
- Location: `styles/` directory (same as CSS files)
- Reference: `url('fontname.woff2')`
- Format: WOFF2 for optimal compression
- Include proper fallbacks

## Modification Workflow

### 1. Before Making Changes
```bash
# Validate current state
npm run validate

# Check file structure
ls -la styles/
ls -la images/
```

### 2. Making Changes
1. Edit the appropriate CSS file
2. Test in browser/EPUB reader
3. Run validation
4. Commit changes

### 3. After Changes
```bash
# Validate EPUB structure
npm run validate

# Run build process
npm run build
```

## Common Modifications

### Adding New Fonts
1. Add font files to `styles/` directory
2. Define `@font-face` rules in `fonts.css`
3. Add font assignments for specific elements
4. Update print fallbacks

### Updating Colors
1. Modify color variables in `style.css`
2. Update print-safe versions in `print.css`
3. Ensure sufficient contrast ratios
4. Test in dark/light mode readers

### Adjusting Layout
1. Use flexible units (em, rem, %)
2. Test across different screen sizes
3. Maintain EPUB reader compatibility
4. Update print styles accordingly

### Print Optimization
1. Modify `print.css` for print-specific needs
2. Use appropriate page break controls
3. Adjust margins and typography
4. Remove decorative elements if needed

## Best Practices

### EPUB Compatibility
- Use standard CSS properties
- Avoid advanced CSS features not widely supported
- Test in multiple EPUB readers
- Maintain semantic HTML structure

### Performance
- Optimize font loading with `font-display: swap`
- Use efficient CSS selectors
- Minimize stylesheet size
- Leverage browser caching

### Accessibility
- Maintain sufficient color contrast
- Use semantic HTML with CSS styling
- Provide print-friendly alternatives
- Test with screen readers

### Maintainability
- Use consistent naming conventions
- Comment complex CSS rules
- Organize styles logically
- Keep related styles together

## Testing Checklist

### Visual Testing
- [ ] Chapter titles display correctly
- [ ] Images load and display properly
- [ ] Fonts render as expected
- [ ] Colors are appropriate
- [ ] Layout is responsive

### Print Testing
- [ ] Print styles activate correctly
- [ ] Page breaks work as intended
- [ ] Typography is readable
- [ ] Images scale appropriately
- [ ] No content is cut off

### EPUB Validation
- [ ] Run `npm run validate`
- [ ] Check for CSS errors
- [ ] Verify font loading
- [ ] Test in EPUB readers
- [ ] Validate HTML structure

## Troubleshooting

### Font Not Loading
1. Check file path in `fonts.css`
2. Verify font file exists in `styles/`
3. Check `@font-face` syntax
4. Test with fallback fonts

### Images Not Displaying
1. Verify image path: `images/filename.ext`
2. Check file exists in `images/` directory
3. Validate HTML `src` attribute
4. Test image format support

### Print Styles Not Working
1. Check `@media print` syntax
2. Verify print.css is linked correctly
3. Test in print preview
4. Clear browser cache

### EPUB Validation Errors
1. Run `npm run validate` for details
2. Check HTML structure
3. Verify CSS syntax
4. Test in EPUB readers

## Resources

- [EPUB 3.3 Specification](https://www.w3.org/publishing/epub3/)
- [CSS Print Guidelines](https://www.w3.org/TR/css-print/)
- [Web Content Accessibility Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [EPUBCheck Validation Tool](https://github.com/w3c/epubcheck)

## Support

For questions about stylesheet modifications:
1. Check this guide first
2. Run validation tools
3. Test across multiple readers
4. Document any issues found

Remember to always validate your changes and test across different reading environments to ensure the best user experience.