# XHTML Live Preview Guide

This guide explains how to preview XHTML files in real-time during development.

## Quick Start

The easiest way to preview XHTML files is to use the built-in preview server:

```bash
# Start the preview server
npm run preview
```

This will:
1. Start a local HTTP server on port 8000
2. Serve all XHTML files with proper MIME types
3. Display a preview URL you can open in your browser

Then open your browser to: **http://localhost:8000/xhtml-preview.html**

## Preview Features

### Interactive File Selector
- Drop-down menu with all XHTML files organized by type:
  - 📄 Frontmatter (Title Page, Copyright, TOC, etc.)
  - 📑 Part Dividers
  - 📖 Chapters
  - 🗺️ Navigation

### Real-Time Viewing
- Select any file from the dropdown to instantly preview it
- Files are displayed with their actual CSS styling
- All images, fonts, and styles load correctly

### Convenient Controls
- **🔄 Reload Button**: Refresh the current file to see your latest changes
- **🔗 Open Direct**: Open the XHTML file directly in a new tab
- **Keyboard Shortcuts**:
  - `Ctrl/Cmd + R`: Reload current file
  - `Ctrl/Cmd + O`: Open in new tab

## Usage Examples

### Preview the Title Page
```bash
npm run preview
# Then open: http://localhost:8000/xhtml-preview.html?file=OEBPS/text/1-TitlePage.xhtml
```

Or use the shortcut (macOS):
```bash
npm run preview:title
```

### Preview Any XHTML File
1. Start the server: `npm run preview`
2. Open http://localhost:8000/xhtml-preview.html in your browser
3. Use the dropdown to select any file
4. Make changes to your XHTML file
5. Click the "🔄 Reload" button to see your changes

### Direct File Access
You can also access files directly by URL:
```
http://localhost:8000/xhtml-preview.html?file=OEBPS/text/1-TitlePage.xhtml
http://localhost:8000/xhtml-preview.html?file=OEBPS/text/3-TableOfContents.xhtml
http://localhost:8000/xhtml-preview.html?file=OEBPS/text/9-chapter-i-unveiling-your-creative-odyssey.xhtml
```

## Development Workflow

### Typical Workflow for Editing XHTML Files

1. **Start the preview server:**
   ```bash
   npm run preview
   ```

2. **Open the preview in your browser:**
   ```
   http://localhost:8000/xhtml-preview.html
   ```

3. **Select your file:**
   - Use the dropdown to select `1-TitlePage.xhtml` or any other file

4. **Edit your XHTML file:**
   - Open `/OEBPS/text/1-TitlePage.xhtml` in your text editor
   - Make your changes

5. **See your changes:**
   - Click the "🔄 Reload" button in the preview
   - Or press `Ctrl/Cmd + R`

6. **Repeat:**
   - Continue editing and reloading to see changes in real-time

## Technical Details

### Server Features
- **Proper MIME Types**: XHTML files are served with `application/xhtml+xml`
- **CORS Enabled**: Local file access is allowed
- **Port 8000**: Default port (configurable in `preview-server.py`)
- **Current Directory**: Serves from the repository root

### Preview Interface
- **Responsive Design**: Works on desktop and mobile
- **Iframe-based**: Renders XHTML files in isolation
- **URL State**: File selection is stored in the URL for bookmarking
- **Browser History**: Back/forward buttons work as expected

### File Structure
```
/
├── preview-server.py       # Python HTTP server with XHTML support
├── xhtml-preview.html      # Interactive preview interface
└── OEBPS/
    ├── text/              # Your XHTML files
    ├── styles/            # CSS stylesheets
    ├── images/            # Images
    └── fonts/             # Font files
```

## Troubleshooting

### Port Already in Use
If port 8000 is already in use:
```bash
# Edit preview-server.py and change PORT = 8000 to another port
# Or stop the other application using port 8000
```

### Files Not Loading
- Make sure the server is running (`npm run preview`)
- Check that the file path is correct
- Verify the file exists in `/OEBPS/text/`

### Styles Not Showing
- Ensure CSS files exist in `/OEBPS/styles/`
- Check that the XHTML file has correct stylesheet links
- Look for console errors in browser developer tools

### Changes Not Appearing
- Click the "🔄 Reload" button
- Try a hard refresh in your browser (Ctrl+Shift+R or Cmd+Shift+R)
- Clear your browser cache

## Advanced Usage

### Custom Port
Edit `preview-server.py` and change:
```python
PORT = 8000  # Change to your desired port
```

### Add More Files
Edit `xhtml-preview.html` and add entries to the `xhtmlFiles` array:
```javascript
const xhtmlFiles = [
    { path: 'OEBPS/text/your-file.xhtml', label: '📄 Your File' },
    // ... more files
];
```

### Stopping the Server
Press `Ctrl+C` in the terminal where the server is running.

## Comparison with Other Methods

| Method | Pros | Cons |
|--------|------|------|
| **Preview Server** (This) | Real-time updates, proper styling, easy to use | Requires running server |
| Direct browser open | No server needed | No styling, security warnings |
| EPUB reader | See actual EPUB | Must rebuild EPUB each time |
| Canvas viewer | Artistic visualization | Not actual render, static |

## Summary

The XHTML preview server provides the best balance of convenience and accuracy:
- ✅ See XHTML files with actual styling
- ✅ Quick reload to see changes
- ✅ No need to rebuild EPUB
- ✅ Works for all XHTML files in the project
- ✅ Simple to use

Perfect for iterative development and design work!
