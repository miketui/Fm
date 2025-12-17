# Chapter Title Page React Component

## Overview

This document describes the **ChapterTitlePage** React component - a visual canvas implementation that displays the chapter title page structure from "The Artisan's Path" EPUB book.

![Chapter Title Page Visual Canvas](chapter-title-page-visual-canvas.png)

## Component Structure

The component follows the EPUB 3.2 chapter title page structure with these key sections:

### 1. Chapter Number Emblem
- Roman numeral (X) displayed over a decorative teal circular brushstroke
- Centered at the top of the page
- Uses gradient background with shadow effects
- Fallback support if brush image is unavailable

### 2. Title Stack
- Decorative gold gradient bar
- Stacked title lines in uppercase
- "CRAFTING ENDURING LEGACIES" split across two lines
- Teal color (#2B9999) matching brand guidelines

### 3. Scripture Quote
- Biblical quotation in styled container
- Cream background (#F5F3EF) with gold border accent
- Italic text with proper attribution
- Example: "But the fruit of the Spirit is love, joy, peace…" — Galatians 5:22–23

### 4. Introduction Section
- "Introduction" heading in decorative font
- Opening paragraph with drop cap styling
- First letter (C) enlarged and styled in teal
- Left-aligned text with optimal line length (65 characters)

## Files Created

### Component Files
1. **`src/ChapterTitlePage.jsx`** - React component with inline styles
2. **`chapter-title-page-viewer.html`** - React viewer with CDN dependencies
3. **`chapter-title-page-canvas.html`** - Standalone HTML demonstration

### Assets
- **`assets/brush-teal.svg`** - SVG brushstroke image
- **`assets/brush-teal.png`** - PNG version (fallback)

### Documentation
- **`CHAPTER_TITLE_PAGE_COMPONENT.md`** - This file
- **`chapter-title-page-visual-canvas.png`** - Screenshot of the rendered component

## Usage

### React Component

```jsx
import { ChapterTitlePage } from './src/ChapterTitlePage';

function App() {
  return (
    <div>
      <ChapterTitlePage />
    </div>
  );
}
```

### Standalone HTML

Open `chapter-title-page-canvas.html` in any modern browser to view the component without React.

```bash
# Serve locally
python3 -m http.server 8000

# Open in browser
open http://localhost:8000/chapter-title-page-canvas.html
```

## Design System

### Colors

| Element | Color | Hex Code | CSS Variable |
|---------|-------|----------|--------------|
| Teal Primary | ![#2B9999](https://via.placeholder.com/15/2B9999/000000?text=+) | `#2B9999` | `--clr-teal-primary` |
| Gold Accent | ![#C9A961](https://via.placeholder.com/15/C9A961/000000?text=+) | `#C9A961` | `--clr-gold-accent` |
| Cream Background | ![#F5F3EF](https://via.placeholder.com/15/F5F3EF/000000?text=+) | `#F5F3EF` | `--clr-cream` |
| Text Primary | ![#0F1616](https://via.placeholder.com/15/0F1616/000000?text=+) | `#0F1616` | `--clr-ink` |

### Typography

| Element | Font Family | Size | Weight |
|---------|-------------|------|--------|
| Chapter Number | Cinzel Decorative | 4rem-6rem (clamp) | 400 |
| Title Lines | Cinzel Decorative | 2rem-3rem (clamp) | 400 |
| Body Text | Libre Baskerville | 1.05rem-1.2rem | 400 |
| Scripture Reference | Montserrat | 0.94rem-1.05rem | 600 |

### Spacing

- Section padding: 3rem vertical, 1.5rem horizontal
- Chapter number margin: 2rem bottom
- Title stack margin: 3rem bottom
- Quote container: 3rem bottom
- Introduction heading: 3rem top, 1.75rem bottom

## Component Props

The current implementation uses fixed content, but can be extended to accept props:

```jsx
export function ChapterTitlePage({
  chapterNumber = "X",
  titleLines = ["CRAFTING", "ENDURING LEGACIES"],
  quote = "But the fruit of the Spirit is love, joy, peace…",
  reference = "— Galatians 5:22–23",
  introText = "Consider the impact of your work not just today, but as a legacy…"
}) {
  // Component implementation
}
```

## Responsive Design

The component uses CSS `clamp()` for fluid typography:
- **Chapter number:** Scales from 4rem to 6rem
- **Title text:** Scales from 2rem to 3rem  
- **Body text:** Scales from 1.05rem to 1.2rem

The brushstroke emblem scales responsively:
- Width/Height: `clamp(200px, 40vw, 280px)`

## Browser Compatibility

- ✅ Chrome 88+
- ✅ Firefox 75+
- ✅ Safari 13.1+
- ✅ Edge 88+

Requires CSS Grid, Flexbox, and CSS Custom Properties support.

## Accessibility

- Semantic HTML structure with `<section>`, `<h2>`, `<p>` elements
- ARIA labels on decorative elements (`aria-hidden="true"`)
- Sufficient color contrast ratios (WCAG AA compliant)
- Keyboard navigation support
- Screen reader friendly structure

## Source Reference

Based on the EPUB chapter structure from:
- **File:** `REBRANDED_OUTPUT/xhtml/20-chapter-x-crafting-enduring-legacies.xhtml`
- **Styles:** `REBRANDED_OUTPUT/xhtml/styles/style.css` (lines 329-450)
- **Book:** "The Artisan's Path: A Comprehensive Guide to Professional Hairstyling Excellence"

## Testing

View the component in a browser:

1. Start local server: `npm run canvas:serve` or `python3 -m http.server 8000`
2. Open: http://localhost:8000/chapter-title-page-canvas.html
3. Verify all sections render correctly
4. Test responsive behavior by resizing browser window
5. Check browser console for errors

## Integration with Existing Project

The component integrates with the existing EPUB production system:
- Matches CSS design tokens from `style.css`
- Uses same color scheme (teal/gold hybrid branding)
- Follows established typography hierarchy
- Compatible with existing React components in `REBRANDED_OUTPUT/react-components/`

## Future Enhancements

Potential improvements:
1. **Dynamic Content:** Accept chapter data as props
2. **Animation:** Add entrance animations for title elements
3. **Image Support:** Better handling of brushstroke SVG/PNG
4. **Theming:** Support for different chapter color schemes
5. **Print Styles:** Optimize for PDF export

## License

All rights reserved - Curls Contemporary Collective / The Artisan's Path

---

**Created:** December 17, 2024  
**Component Version:** 1.0.0  
**Repository:** miketui/Fm
