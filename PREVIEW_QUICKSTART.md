# Quick Start: Preview Your XHTML Files

Need to see how your XHTML file looks? Follow these simple steps:

## 1. Start the Preview Server

```bash
npm run preview
```

You'll see output like this:
```
======================================================================
🌐 XHTML Preview Server Running
======================================================================
📂 Serving directory: /path/to/Fm
🔗 Server URL: http://localhost:8000
📄 Preview URL: http://localhost:8000/xhtml-preview.html
======================================================================
```

## 2. Open Your Browser

Open this URL in any web browser:
```
http://localhost:8000/xhtml-preview.html
```

## 3. Select Your File

The preview will automatically show **1-TitlePage.xhtml** by default.

To view other files:
- Click the **"File:"** dropdown
- Select any file from the list (organized by type)
- The file will load instantly with proper styling

## 4. Make Changes and Reload

1. Edit your XHTML file in your text editor
2. Save your changes
3. Click the **🔄 Reload** button in the preview
4. See your changes immediately!

## 5. Stop the Server

When you're done, press `Ctrl+C` in the terminal where the server is running.

---

## Pro Tips

### Direct File Access
You can bookmark specific files:
```
http://localhost:8000/xhtml-preview.html?file=OEBPS/text/1-TitlePage.xhtml
http://localhost:8000/xhtml-preview.html?file=OEBPS/text/3-TableOfContents.xhtml
```

### Keyboard Shortcuts
- `Ctrl+R` (or `Cmd+R` on Mac) - Reload current file
- `Ctrl+O` (or `Cmd+O` on Mac) - Open in new tab

### Open Title Page Directly (macOS)
```bash
npm run preview:title
```

---

That's it! You now have a live preview of your XHTML files with full styling.

For more details, see [XHTML_PREVIEW_GUIDE.md](XHTML_PREVIEW_GUIDE.md)
