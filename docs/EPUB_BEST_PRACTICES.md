# Best Techniques to Enhance EPUB Layout, Typography & Readability

This checklist reflects current **EPUB 3.2**, **WCAG 2.2 AA**, and industry trade-publishing standards—the same principles used by major publishers (Penguin, HarperCollins, Chronicle, Hachette, etc.).

---

## 1. Typography That Looks Professional

A polished EPUB starts with typography. Focus on clarity, legibility, and brand consistency.

### Use a Professional Serif + Sans-Serif Pair

- **Serif (body text)**: Libre Baskerville, Georgia, Spectral, Source Serif, Literary, Charter
- **Sans-serif (headers/UI)**: Montserrat, Inter, Source Sans, Lato

**Best practice**: Use serif for body + sans-serif for headings. Avoid decorative typefaces for paragraphs.

### Size & Line Height

- **Body font size**: 1rem–1.1rem (16–17.5px)
- **Line height**: 1.45–1.6
- **Paragraph spacing**: 0.75–1.2em
- **Max line length**: 60–75 characters

These numbers dramatically improve readability across Kindle, Apple Books, Kobo, Nook, etc.

### Avoid Full Justification (unless you have hyphenation)

- On many EPUB platforms, full-justified text without hyphenation = rivers + awkward spacing
- If you do justify:

```css
body {
  text-align: justify;
  hyphens: auto;
}
html {
  -webkit-hyphens: auto;
}
```

- Otherwise, keep text left-aligned

---

## 2. Page Layout & Structure That Feels Like a Real Book

### Logical Reading Order

Correct Z-ordering prevents screen reader chaos:
- Title → subtitle → author
- Section → heading → body text
- Images always follow the paragraphs they belong to

### Consistent Chapter Architecture

Your chapters should follow a predictable pattern:
1. Chapter title page
2. Optional quote/bible verse
3. Body text
4. Endnotes
5. Worksheet (print-friendly)
6. Quiz page
7. Image quote

Use XHTML templates so all 44 files share identical formatting and markup logic.

### Break Up Long Walls of Text

Use:
- Section headers `<h2>`, `<h3>`
- Pull quotes
- Callout boxes (TIP, NOTE, REFLECTION)
- Illustrative icons (SVG, WCAG-compliant)

---

## 3. CSS Styling That Looks Modern & Clean

### Use Modular CSS

Break files into:
- `style.css` – global typography + layout
- `fonts.css` – font-face declarations
- `colors.css` – brand palette
- `print.css` – print-specific overrides
- `utilities.css` – spacing helpers, flex utilities

### Use REM Units, Not PX

This ensures resizing works on Kindle, Kobo, and Apple Books in both reflow + fixed layout.

### Avoid Over-Styled Elements

Do not use:
- Text-shadow
- Heavy drop caps without fallbacks
- Position: absolute (breaks on some eReaders)
- Fixed pixel heights
- Background images behind text (AA fails)

---

## 4. Professional-Grade Layout Elements

### Drop Caps

Use a WCAG-safe approach:

```css
p.dropcap:first-letter {
  float: left;
  font-size: 3.8em;
  line-height: .7;
  padding-right: .1em;
  font-family: "Cinzel Decorative";
}
```

### Stylized Quote Blocks

```css
blockquote {
  margin: 1.5em 1em;
  padding-left: 1em;
  border-left: 4px solid var(--accent);
  font-style: italic;
}
```

### Beautiful Chapter Title Pages

- Use centered layout
- Add generous vertical spacing
- Include brushstroke or texture images below the heading for brand continuity
- Keep the chapter title in `<h1>` for semantics

### Image Quotes

- Use `max-width: 100%`
- Add descriptive `alt=""` text
- Place them inside semantic `<figure>` tags

---

## 5. WCAG 2.2 AA Accessibility Enhancements

### Text Contrast

- Minimum contrast: **4.5:1**
- For accents, maintain contrast with backgrounds

### Proper Semantic Markup

Use:
- `<article>`
- `<section>`
- `<nav>`
- `<header>`
- `<figure>` / `<figcaption>`

### ARIA Landmarks

```html
<main role="main">
<nav epub:type="toc">
<section epub:type="chapter">
```

### Screen Reader Navigation

- `<h1>` should appear ONCE per file
- No empty tags
- Images require descriptive alt text
- Decorative images get `alt="" role="presentation"`

---

## 6. EPUB-Safe Layout Rules

EPUB readers vary wildly. To prevent rendering bugs:

### Avoid:
- Flexbox for complex layouts
- CSS Grid (works on Apple Books, fails on Kindle)
- Position absolute for anything important
- Large SVGs inside inline text
- Javascript (Kindle rejects it)

### Use:
- Simple block elements
- Float-based layout only if absolutely needed
- Inline SVGs < 60KB
- PNG/JPEG for images

---

## 7. Images that Look Crisp & Clean

- **Min resolution**: 1400px width for full-page images
- **Image compression**:
  - Quotes: 130–160 KB
  - Backgrounds: 200–300 KB
  - Icons: SVG
- Use `srcset` where allowed for retina support

---

## 8. Metadata for Distribution Platforms

Inside `content.opf`:
- Title + subtitle
- Creator
- `dc:subject` (up to 7 keywords)
- Language
- Publisher
- Identifier (ISBN)
- Updated modified date
- Accessible metadata (conforms-to: WCAG)

Also include:
- `page-list`
- `landmarks`
- `nav.xhtml`

These improve navigation on Apple Books.

---

## 9. Footnotes & Endnotes That Behave Properly

Use EPUB 3 pop-up footnotes:

**In body text:**
```html
<a href="#note1" epub:type="noteref">1</a>
```

**In endnotes page:**
```html
<li id="note1" epub:type="footnote">
  <p>Note text here...</p>
</li>
```

---

## 10. Validate Like a Major Publisher

Run:
- **EPUBCheck** (strict)
- **Ace by DAISY** (accessibility)
- **Kindle Previewer** (Kindle format check)
- **iBooks Simulator** (Apple Books visual check)

This catches:
- Broken links
- Missing manifest items
- CSS issues
- WCAG violations
- Incorrect spine ordering

---

## Additional Resources

- [EPUB 3.2 Specification](https://www.w3.org/TR/epub-32/)
- [WCAG 2.2 Guidelines](https://www.w3.org/WAI/WCAG22/quickref/)
- [Ace by DAISY](https://daisy.github.io/ace/)
- [EPUBCheck](https://github.com/w3c/epubcheck)
- [IDPF EPUB Best Practices](http://www.idpf.org/epub/guides/)

---

**Document Version**: 1.0
**Last Updated**: 2025-11-14
**Maintained by**: Terragon Labs
**Target Audience**: EPUB production engineers, publishers, designers
