# Image Optimization Guide for EPUB

## MANDATORY Image Requirements for Bestseller Quality

### 1. SVG Image Optimization

**Brushstroke Background (brushstroke.svg)**
```xml
<!-- Optimized SVG template -->
<svg width="150" height="150" viewBox="0 0 150 150" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="roughen">
      <feTurbulence baseFrequency="0.02" numOctaves="3" result="noise"/>
      <feDisplacementMap in="SourceGraphic" in2="noise" scale="2"/>
    </filter>
  </defs>
  <path d="M20 75 Q30 45 60 35 Q90 30 120 45 Q135 55 130 75 Q125 95 100 110 Q70 120 40 105 Q15 85 20 75 Z" 
        fill="#4ECDC4" opacity="0.9" filter="url(#roughen)"/>
</svg>
```

**SVG Optimization Checklist:**
- [ ] Remove unnecessary metadata and comments
- [ ] Minimize decimal places in path data
- [ ] Use efficient gradients and filters
- [ ] Compress without quality loss
- [ ] File size target: Under 5KB

### 2. Raster Image Optimization

**JPEG Images (portraits, photographs)**
- **Quality**: 85% (optimal balance of quality/file size)
- **Encoding**: Progressive JPEG for faster perceived loading
- **Color Profile**: sRGB for consistent color reproduction
- **Maximum Width**: 1200px for full-width images
- **File Size Target**: Under 150KB per image

**PNG Images (graphics, illustrations)**
- **Bit Depth**: 8-bit when possible, 24-bit for complex images
- **Optimization**: Use PNG optimization tools (OptiPNG, PNGCrush)
- **Transparency**: Optimize alpha channel efficiency
- **File Size Target**: Under 100KB per image

### 3. Responsive Image Implementation

**Standard Implementation:**
```xml
<img src="../images/optimized-image.jpg" 
     alt="Professional hairstylist demonstrating advanced cutting technique with precision and artistry" 
     style="max-width: 100%; height: auto; display: block; margin: 0 auto;"
     loading="lazy"
     class="content-image"/>
```

**Accessibility Enhanced:**
```xml
<figure class="image-container" role="img" aria-labelledby="img-caption-1">
    <img src="../images/hairstyle-transformation.jpg" 
         alt="Before and after comparison showing dramatic hair transformation from long straight hair to modern layered bob with copper highlights" 
         style="max-width: 100%; height: auto;"
         loading="lazy"
         class="content-image"/>
    <figcaption id="img-caption-1" class="image-caption">
        Sarah's transformation: From corporate conservative to confident and stylish
    </figcaption>
</figure>
```

### 4. Performance Optimization Techniques

**Lazy Loading Implementation:**
```xml
<!-- For non-critical images -->
<img src="../images/example.jpg" 
     alt="Descriptive alt text" 
     loading="lazy"
     style="max-width: 100%; height: auto;"/>

<!-- For critical images (above the fold) -->
<img src="../images/chapter-hero.jpg" 
     alt="Descriptive alt text" 
     loading="eager"
     style="max-width: 100%; height: auto;"/>
```

**CSS for Responsive Images:**
```css
.content-image {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 1rem auto;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.brushstroke-img {
    position: absolute;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: 1;
}

.closing-image {
    max-width: 200px;
    height: auto;
    display: block;
    margin: 2rem auto;
    opacity: 0.8;
}
```

### 5. Image Format Decision Tree

**Use SVG for:**
- Icons and simple graphics
- Scalable decorative elements (brushstroke)
- Line art and logos
- Mathematical diagrams

**Use JPEG for:**
- Photographs of people
- Complex scenes with many colors
- Hair styling examples
- Before/after comparisons

**Use PNG for:**
- Graphics with transparency
- Simple illustrations
- Text overlays
- Screenshots with text

### 6. Accessibility Requirements

**Alt Text Guidelines:**

**Decorative Images:**
```xml
<img src="../images/brushstroke.svg" 
     alt="Decorative teal brushstroke background" 
     class="brushstroke-img"/>
```

**Informative Images:**
```xml
<img src="../images/cutting-technique.jpg" 
     alt="Professional hairstylist using point cutting technique on shoulder-length blonde hair to create textured layers" 
     class="content-image"/>
```

**Complex Images:**
```xml
<img src="../images/color-wheel.jpg" 
     alt="Professional hair color wheel showing complementary colors: warm tones including golden blonde, copper, and auburn on the left side, cool tones including ash blonde, platinum, and chocolate brown on the right side" 
     class="content-image"/>
```

### 7. File Naming Convention

**Organized File Structure:**
```
OEBPS/images/
├── brushstroke.svg (chapter decorations)
├── closing-ornament.png (chapter endings)
├── cover.jpg (book cover)
├── author-photo.jpg (author information)
├── chapter-01/
│   ├── hero-image.jpg
│   ├── technique-demo.jpg
│   └── before-after.jpg
├── chapter-02/
│   ├── hero-image.jpg
│   └── tools-layout.jpg
└── icons/
    ├── quiz-icon.svg
    └── worksheet-icon.svg
```

**File Naming Rules:**
- Use lowercase letters only
- Separate words with hyphens
- Include descriptive keywords
- Keep names under 50 characters

### 8. Optimization Tools and Commands

**Command Line Tools:**
```bash
# JPEG optimization
jpegoptim --size=150k *.jpg

# PNG optimization  
optipng -o7 *.png

# SVG optimization
svgo --multipass *.svg

# Batch resize images
mogrify -resize 1200x1200\> -quality 85 *.jpg
```

**Online Optimization:**
- TinyPNG for PNG compression
- JPEG.io for JPEG optimization
- SVGOMG for SVG optimization

### 9. Quality Assurance Checklist

**Before finalizing each image:**
- [ ] File size meets target requirements
- [ ] Quality is appropriate for intended use
- [ ] Alt text is descriptive and meaningful
- [ ] Image displays correctly at various sizes
- [ ] Color reproduction is accurate
- [ ] Loading performance is optimized
- [ ] Accessibility requirements met

### 10. EPUB-Specific Considerations

**Device Compatibility:**
- Test on high-DPI displays (Retina, etc.)
- Verify rendering on grayscale e-readers
- Check performance on older devices
- Ensure images work in night mode

**File Size Limits:**
- Individual image: Max 1MB
- Total EPUB size: Target under 50MB
- Consider device storage limitations
- Balance quality vs. file size

### 11. Implementation in Codex Commands

**Image Processing Commands:**
```bash
@agents OPTIMIZE ALL IMAGES for performance and accessibility:

1. SVG OPTIMIZATION:
   - Compress brushstroke.svg to under 5KB
   - Remove unnecessary metadata
   - Optimize path data for efficiency
   - Maintain visual quality

2. RASTER IMAGE OPTIMIZATION:
   - JPEG: 85% quality, progressive encoding
   - PNG: 8-bit when possible, optimize transparency
   - Maximum width: 1200px
   - Compress all images to meet size targets

3. ACCESSIBILITY IMPLEMENTATION:
   - Add descriptive alt text to every image
   - Use semantic figure/figcaption where appropriate
   - Implement proper ARIA labels
   - Ensure screen reader compatibility

4. RESPONSIVE IMPLEMENTATION:
   - Add CSS for responsive sizing
   - Include lazy loading attributes
   - Optimize for various screen sizes
   - Test cross-device compatibility
```

This comprehensive optimization ensures your EPUB delivers professional quality while maintaining excellent performance across all devices.