# XHTML Canvas Visualization

## Overview

This project creates a beautiful canvas visualization of the EPUB chapter "Chapter I – Unveiling Your Creative Odyssey" from the XHTML file `9-chapter-i-unveiling-your-creative-odyssey.xhtml`.

## Generated Files

### 🖼️ Visualization Images
- **`chapter-i-canvas-visualization.png`** - Full-size visualization (1000×800px)
- **`chapter-i-canvas-preview.png`** - Preview version (500×400px)

### 🌐 Web Interface
- **`canvas-viewer.html`** - Interactive web viewer to display the visualization
- **`xhtml-canvas-visualization.html`** - React-based web application (standalone)

### 🛠️ Source Code
- **`generate-canvas-visualization.js`** - Node.js script that generates the canvas visualization
- **`src/XHTMLCanvasVisualizer.jsx`** - React component for browser-based visualization
- **`src/XHTMLCanvasReader.jsx`** - Enhanced React component with file reading
- **`src/App.jsx`** - Main React application

## Features

### Visual Elements
- ✨ Chapter number "I" with decorative brushstroke background
- 📚 Stacked title design: "Unveiling Your Creative Odyssey"
- 📖 Biblical quotation in highlighted container (Ephesians 2:10)
- 🎨 Professional typography with shadow effects
- 🌊 Teal accent color scheme (#1797a6)
- 🔘 Decorative patterns and border frames

### Content Structure
- 📋 Introduction section with opening narrative
- 📊 8 main content sections extracted from XHTML
- 🎯 Alternating background colors for readability
- 🔢 Section numbering and hierarchical organization
- ✨ Decorative footer elements

### Technical Implementation
- ⚙️ Generated using Node.js Canvas API
- 🔍 XHTML content parsed with JSDOM
- 🎨 High-quality antialiased rendering
- 📱 Responsive design elements
- 🖼️ PNG format with transparency support

## Usage

### Generate Visualization
```bash
# Install dependencies
npm install

# Generate the canvas visualization
node generate-canvas-visualization.js
```

### View in Browser
```bash
# Open the web viewer
open canvas-viewer.html

# Or serve locally
python -m http.server 8000
# Then visit: http://localhost:8000/canvas-viewer.html
```

### Download Images
- Full size: [chapter-i-canvas-visualization.png](chapter-i-canvas-visualization.png)
- Preview: [chapter-i-canvas-preview.png](chapter-i-canvas-preview.png)

## Source Content

The visualization is generated from the EPUB chapter file:
- **File**: `OEBPS/text/9-chapter-i-unveiling-your-creative-odyssey.xhtml`
- **Theme**: Conscious hairstyling and creativity
- **Format**: EPUB 3.2 compliant XHTML
- **Content**: Professional development journal for hairstylists

### Extracted Elements
1. **Chapter Number**: Roman numeral "I"
2. **Title Lines**: "Unveiling", "Your", "Creative", "Odyssey"
3. **Bible Quote**: Ephesians 2:10 quotation
4. **Introduction**: Opening paragraph with celebrity stylist example
5. **Main Sections**: 8 content sections covering hairstyling topics
6. **Visual Design**: Colors, fonts, and layout from CSS styles

## Dependencies

- `canvas` - Node.js Canvas API for image generation
- `jsdom` - DOM parsing for XHTML content
- `react` & `react-dom` - For browser-based components
- `fs` & `path` - File system operations

## Output Specifications

### Full Visualization (1000×800px)
- **Format**: PNG with transparency
- **Size**: ~140KB
- **DPI**: High-quality for print/display
- **Colors**: Professional color palette

### Preview Version (500×400px)
- **Format**: PNG with transparency  
- **Size**: ~64KB
- **Use**: Thumbnails, web display
- **Quality**: Optimized for web

## Customization

### Colors
```javascript
const colors = {
  backgroundColor: '#f7f9fa',
  accentColor: '#1797a6',
  textColor: '#1a1a1a',
  quoteColor: '#e0f2f1'
};
```

### Canvas Dimensions
```javascript
const width = 1000;  // Adjust width
const height = 800;  // Adjust height
```

### Content Sections
The script automatically extracts content sections from the XHTML file. To modify the display:
1. Edit the section selection in `generate-canvas-visualization.js`
2. Adjust the `yPos` and `sectionHeight` variables
3. Customize the section styling

## Browser Support

### Web Viewer (`canvas-viewer.html`)
- ✅ Chrome 60+
- ✅ Firefox 55+
- ✅ Safari 12+
- ✅ Edge 79+

### React Components
- ✅ Modern browsers with ES6 support
- ✅ React 16.8+ (hooks support)
- ✅ Canvas API support required

## Development

### Project Structure
```
Fm/
├── OEBPS/text/9-chapter-i-unveiling-your-creative-odyssey.xhtml
├── generate-canvas-visualization.js
├── canvas-viewer.html
├── src/
│   ├── App.jsx
│   ├── XHTMLCanvasVisualizer.jsx
│   └── XHTMLCanvasReader.jsx
├── chapter-i-canvas-visualization.png
├── chapter-i-canvas-preview.png
└── CANVAS_VISUALIZATION_README.md
```

### Commands
```bash
# Generate visualization
npm run canvas:generate

# Serve web viewer
npm run canvas:serve

# Clean generated files
npm run canvas:clean
```

## Credits

- **Content**: "Curls & Contemplation: A Stylist's Interactive Journey Journal"
- **Technology**: Node.js Canvas API, React, JSDOM
- **Design**: Based on EPUB CSS styles and professional layout principles
- **Generated**: Programmatically from XHTML source content

---

*This visualization transforms structured EPUB content into a beautiful visual representation that captures the essence of the chapter's design and message.*