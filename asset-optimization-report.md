# EPUB Asset Optimization Report

Generated: 2025-09-14T18:31:14.830Z

## Summary

- **Mode**: Dry Run (Analysis Only)
- **Images Analyzed**: 29
- **Fonts Analyzed**: 6
- **Total Recommendations**: 38
- **Estimated Savings**: 85KB

## Image Optimization

### Michael.jpeg
- **Size**: 169KB
- **Recommendations**:
  - **jpeg_optimization**: JPEG can be optimized with quality adjustment
    - Command: `jpegoptim --max=85 "OEBPS/images/Michael.jpeg"`
  - **webp_conversion**: Consider converting to WebP format for better compression
    - Estimated savings: 51KB
    - Command: `cwebp -q 85 "OEBPS/images/Michael.jpeg" -o "OEBPS/images/Michael.webp"`

### brushstroke.jpeg
- **Size**: 11KB
- **Recommendations**:
  - **jpeg_optimization**: JPEG can be optimized with quality adjustment
    - Command: `jpegoptim --max=85 "OEBPS/images/brushstroke.jpeg"`

### chapter-frame.png
- **Size**: 2KB
- **Recommendations**:
  - **png_optimization**: PNG can be compressed without quality loss
    - Command: `pngcrush -reduce -brute "OEBPS/images/chapter-frame.png" "OEBPS/images/chapter-frame.png.tmp" && mv "OEBPS/images/chapter-frame.png.tmp" "OEBPS/images/chapter-frame.png"`

### chapter-i-quote.jpeg
- **Size**: 49KB
- **Recommendations**:
  - **jpeg_optimization**: JPEG can be optimized with quality adjustment
    - Command: `jpegoptim --max=85 "OEBPS/images/chapter-i-quote.jpeg"`

### chapter-ii-quote.jpeg
- **Size**: 72KB
- **Recommendations**:
  - **jpeg_optimization**: JPEG can be optimized with quality adjustment
    - Command: `jpegoptim --max=85 "OEBPS/images/chapter-ii-quote.jpeg"`

### chapter-iii-quote.jpeg
- **Size**: 43KB
- **Recommendations**:
  - **jpeg_optimization**: JPEG can be optimized with quality adjustment
    - Command: `jpegoptim --max=85 "OEBPS/images/chapter-iii-quote.jpeg"`

### chapter-iv-quote.jpeg
- **Size**: 55KB
- **Recommendations**:
  - **jpeg_optimization**: JPEG can be optimized with quality adjustment
    - Command: `jpegoptim --max=85 "OEBPS/images/chapter-iv-quote.jpeg"`

### chapter-ix-quote.jpeg
- **Size**: 69KB
- **Recommendations**:
  - **jpeg_optimization**: JPEG can be optimized with quality adjustment
    - Command: `jpegoptim --max=85 "OEBPS/images/chapter-ix-quote.jpeg"`

### chapter-v-quote.jpeg
- **Size**: 75KB
- **Recommendations**:
  - **jpeg_optimization**: JPEG can be optimized with quality adjustment
    - Command: `jpegoptim --max=85 "OEBPS/images/chapter-v-quote.jpeg"`

### chapter-vi-quote.jpeg
- **Size**: 56KB
- **Recommendations**:
  - **jpeg_optimization**: JPEG can be optimized with quality adjustment
    - Command: `jpegoptim --max=85 "OEBPS/images/chapter-vi-quote.jpeg"`

### chapter-vii-quote.jpeg
- **Size**: 70KB
- **Recommendations**:
  - **jpeg_optimization**: JPEG can be optimized with quality adjustment
    - Command: `jpegoptim --max=85 "OEBPS/images/chapter-vii-quote.jpeg"`

### chapter-viii-quote.jpeg
- **Size**: 54KB
- **Recommendations**:
  - **jpeg_optimization**: JPEG can be optimized with quality adjustment
    - Command: `jpegoptim --max=85 "OEBPS/images/chapter-viii-quote.jpeg"`

### chapter-x-quote.jpeg
- **Size**: 69KB
- **Recommendations**:
  - **jpeg_optimization**: JPEG can be optimized with quality adjustment
    - Command: `jpegoptim --max=85 "OEBPS/images/chapter-x-quote.jpeg"`

### chapter-xi-quote.jpeg
- **Size**: 69KB
- **Recommendations**:
  - **jpeg_optimization**: JPEG can be optimized with quality adjustment
    - Command: `jpegoptim --max=85 "OEBPS/images/chapter-xi-quote.jpeg"`

### chapter-xii-quote.jpeg
- **Size**: 68KB
- **Recommendations**:
  - **jpeg_optimization**: JPEG can be optimized with quality adjustment
    - Command: `jpegoptim --max=85 "OEBPS/images/chapter-xii-quote.jpeg"`

### chapter-xiii-quote.jpeg
- **Size**: 68KB
- **Recommendations**:
  - **jpeg_optimization**: JPEG can be optimized with quality adjustment
    - Command: `jpegoptim --max=85 "OEBPS/images/chapter-xiii-quote.jpeg"`

### chapter-xiv-quote.jpeg
- **Size**: 69KB
- **Recommendations**:
  - **jpeg_optimization**: JPEG can be optimized with quality adjustment
    - Command: `jpegoptim --max=85 "OEBPS/images/chapter-xiv-quote.jpeg"`

### chapter-xv-quote.jpeg
- **Size**: 66KB
- **Recommendations**:
  - **jpeg_optimization**: JPEG can be optimized with quality adjustment
    - Command: `jpegoptim --max=85 "OEBPS/images/chapter-xv-quote.jpeg"`

### chapter-xvi-quote.jpeg
- **Size**: 70KB
- **Recommendations**:
  - **jpeg_optimization**: JPEG can be optimized with quality adjustment
    - Command: `jpegoptim --max=85 "OEBPS/images/chapter-xvi-quote.jpeg"`

### conclusion-quote.jpeg
- **Size**: 54KB
- **Recommendations**:
  - **jpeg_optimization**: JPEG can be optimized with quality adjustment
    - Command: `jpegoptim --max=85 "OEBPS/images/conclusion-quote.jpeg"`

### crown-ornament.png
- **Size**: 32KB
- **Recommendations**:
  - **png_optimization**: PNG can be compressed without quality loss
    - Command: `pngcrush -reduce -brute "OEBPS/images/crown-ornament.png" "OEBPS/images/crown-ornament.png.tmp" && mv "OEBPS/images/crown-ornament.png.tmp" "OEBPS/images/crown-ornament.png"`

### decorative-line.jpeg
- **Size**: 2KB
- **Recommendations**:
  - **jpeg_optimization**: JPEG can be optimized with quality adjustment
    - Command: `jpegoptim --max=85 "OEBPS/images/decorative-line.jpeg"`

### endnote-marker.png
- **Size**: 0KB
- **Recommendations**:
  - **png_optimization**: PNG can be compressed without quality loss
    - Command: `pngcrush -reduce -brute "OEBPS/images/endnote-marker.png" "OEBPS/images/endnote-marker.png.tmp" && mv "OEBPS/images/endnote-marker.png.tmp" "OEBPS/images/endnote-marker.png"`

### part-border.jpeg
- **Size**: 101KB
- **Recommendations**:
  - **jpeg_optimization**: JPEG can be optimized with quality adjustment
    - Command: `jpegoptim --max=85 "OEBPS/images/part-border.jpeg"`
  - **webp_conversion**: Consider converting to WebP format for better compression
    - Estimated savings: 30KB
    - Command: `cwebp -q 85 "OEBPS/images/part-border.jpeg" -o "OEBPS/images/part-border.webp"`

### preface-quote.jpeg
- **Size**: 53KB
- **Recommendations**:
  - **jpeg_optimization**: JPEG can be optimized with quality adjustment
    - Command: `jpegoptim --max=85 "OEBPS/images/preface-quote.jpeg"`

### quiz-checkbox.png
- **Size**: 9KB
- **Recommendations**:
  - **png_optimization**: PNG can be compressed without quality loss
    - Command: `pngcrush -reduce -brute "OEBPS/images/quiz-checkbox.png" "OEBPS/images/quiz-checkbox.png.tmp" && mv "OEBPS/images/quiz-checkbox.png.tmp" "OEBPS/images/quiz-checkbox.png"`

### quote-marks.png
- **Size**: 53KB
- **Recommendations**:
  - **png_optimization**: PNG can be compressed without quality loss
    - Command: `pngcrush -reduce -brute "OEBPS/images/quote-marks.png" "OEBPS/images/quote-marks.png.tmp" && mv "OEBPS/images/quote-marks.png.tmp" "OEBPS/images/quote-marks.png"`

### ruled-paper.jpeg
- **Size**: 90KB
- **Recommendations**:
  - **jpeg_optimization**: JPEG can be optimized with quality adjustment
    - Command: `jpegoptim --max=85 "OEBPS/images/ruled-paper.jpeg"`

### toc-divider.png
- **Size**: 2KB
- **Recommendations**:
  - **png_optimization**: PNG can be compressed without quality loss
    - Command: `pngcrush -reduce -brute "OEBPS/images/toc-divider.png" "OEBPS/images/toc-divider.png.tmp" && mv "OEBPS/images/toc-divider.png.tmp" "OEBPS/images/toc-divider.png"`

## Font Optimization

### Montserrat-Bold.woff2
- **Size**: 127KB
- **Format**: .WOFF2
- **Recommendations**:
  - **font_subsetting**: Consider subsetting font to include only required characters
    - Command: `fonttools subset "OEBPS/fonts/Montserrat-Bold.woff2" --unicodes=U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD`

### Montserrat-Regular.woff2
- **Size**: 124KB
- **Format**: .WOFF2
- **Recommendations**:
  - **font_subsetting**: Consider subsetting font to include only required characters
    - Command: `fonttools subset "OEBPS/fonts/Montserrat-Regular.woff2" --unicodes=U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD`

## CSS Optimization

### style.css
- **Size**: 28KB
- **Recommendations**:
  - **css_duplication**: Found duplicate CSS rules that could be consolidated
    - Count: 187

### fonts.css
- **Size**: 3KB
- **Recommendations**:
  - **css_comments**: Remove comments to reduce file size
    - Estimated savings: 1KB
  - **css_duplication**: Found duplicate CSS rules that could be consolidated
    - Count: 33

### print.css
- **Size**: 20KB
- **Recommendations**:
  - **css_comments**: Remove comments to reduce file size
    - Estimated savings: 3KB
  - **css_duplication**: Found duplicate CSS rules that could be consolidated
    - Count: 385

