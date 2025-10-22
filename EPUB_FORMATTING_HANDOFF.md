# EPUB Formatting Handoff: Curls & Contemplation

This handoff document provides the complete production brief for preparing the **Curls & Contemplation** EPUB package. Follow these guidelines exactly so that the reformatted output preserves every word of the source manuscript while aligning with the ACISS layout system and downstream PDF requirements.

## 1. Assets overview

### 1.1 Fonts
- Libre Baskerville (regular, italic, bold), Cinzel Decorative (regular), and Montserrat (regular, bold) live in `OEBPS/fonts/`. They are already declared in `fonts.css` where base classes and print fallbacks are defined.
- Import the shared font and layout styles into every XHTML file:
  ```html
  <link rel="stylesheet" type="text/css" href="../styles/fonts.css"/>
  <link rel="stylesheet" type="text/css" href="../styles/style.css"/>
  <link rel="stylesheet" type="text/css" href="../styles/print.css" media="print"/>
  ```

### 1.2 Images
- Decorative assets (brushstrokes, frames, quote marks, icons) are stored in `OEBPS/images/`. Always provide descriptive `alt` text for accessibility.
- Journal and worksheet pages use `ruled-paper.svg` as a tiling background applied via CSS.
- Chapter closing images (`chapter-i-quote.jpeg`, etc.) must be referenced with paths relative to the XHTML file.

### 1.3 CSS
- `style.css` already contains embedded SVG variables and base utility classes (`.quote-marks-icon`, `.ruled-paper-bg`, `.toc-divider-img`, `.quiz-checkbox`, `.chapter-frame`). Append the layout, typography, spacing, and responsive rules described below beneath the existing comments.
- `print.css` contains the starter overrides for PDF output. Extend it if you need to adjust margins or hide decorative backgrounds when rendering to paper.

## 2. Global conventions
1. **Page wrappers** – Assign each `<body>` to `.frontmatter-page`, `.part-page`, `.chapter-page`, or `.backmatter-page` depending on file type. These wrappers enforce flex centring, `min-height: 100vh`, and consistent padding.
2. **Single-page enforcement** – All frontmatter and backmatter files must fit within a single viewport and declare `page-break-inside: avoid`. Worksheets and quizzes start on fresh pages and stay within `90vh` to prevent overflow.
3. **Page-break helpers** – Use `<div class="page-break"></div>` or helper classes (`.page-break-before`, `.page-break-after`) to force new pages before/after quizzes, worksheets, endnotes, and closing images.
4. **Responsive design** – Apply `clamp()` and breakpoint queries (`≤768px`, `769–1024px`, `≥1025px`) to scale fonts and spacing. Use `.mobile-hidden` for decorative elements that should disappear on small screens and `.print-only` for print-specific content.
5. **Typography** – Never hardcode fonts inline. Rely on `fonts.css` classes; introduce new semantic classes for headings, titles, and metadata as needed.

## 3. Frontmatter files (1–7)
Each of the seven files in `text/` (Title Page, Copyright, Table of Contents, Dedication, Self-Assessment, affirmation-odyssey, Preface) must:

1. Wrap page content inside `<body class="frontmatter-page">` with a `<main epub:type="frontmatter" role="main">` region and a `.frontmatter-shell` or `.single-page` section. Example:
   ```html
   <body class="frontmatter-page">
     <main epub:type="frontmatter" role="main">
       <section class="frontmatter-shell title-page" aria-label="Title Page">
         <!-- existing content -->
       </section>
     </main>
   </body>
   ```
2. Apply layouts per file type:
   - **Title page (`1-TitlePage.xhtml`)** – Centre title, subtitle, author, and publisher both vertically and horizontally. Use `.frontmatter-title` for the main heading and `.frontmatter-divider` (SVG rule) between elements. A gradient or tinted background adds visual polish.
   - **Copyright (`2-Copyright.xhtml`)** – Wrap the legal copy in `.copyright-page`, centre the text, and keep margins generous enough to keep the page single-screen.
   - **Table of Contents (`3-TableOfContents.xhtml`)** – Place entries in a list within `.toc-page`. Use flex wrappers to align titles with page numbers and insert `<div class="toc-divider-img"></div>` between sections.
   - **Dedication (`4-Dedication.xhtml`)** – Use a centred paragraph in `.dedication-page`; optional decorative SVGs or rules are welcome.
   - **Self-Assessment (`5-SelfAssessment.xhtml`)` and `affirmation-odyssey (`6-affirmation-odyssey.xhtml`)** – Treat these as interactive worksheets. Use `.worksheet`, `.assessment`, or `.affirmation-sheet` classes, provide instructions, and ensure input areas (`<textarea>` or `<div contenteditable>`) stay in-viewport.
   - **Preface (`7-Preface.xhtml`)** – Place text inside `.preface-page`, style the heading with `.preface-title`, and optionally add a quote or ornament image at the top.
3. Guarantee each shell sets `min-height: 100vh`, `page-break-inside: avoid`, and `overflow: hidden` in CSS.
4. Remove inline `style="..."` attributes; move declarations to `style.css` (e.g., replace `style="margin-top:2rem;"` with `.mt-2 { margin-top: 2rem; }`).

## 4. Part divider pages (8, 12, 18, 24)
- Use `<body class="part-page">`.
- Build a full-screen `<section class="part-divider">` with flex centring and gradient background. Include:
  - `<h1 class="part-title">` for the part name.
  - `<h2 class="part-subtitle">` for the chapter range.
  - `<div class="decorative-line"></div>` to pull in `decorative-line.svg` or `--toc-divider-svg`.
  - Optional descriptive paragraph.
- Style `.part-page` and `.part-divider` in CSS with `min-height: 100vh`, flex layout, responsive padding, and background treatments. Set `.part-title`/`.part-subtitle` in Cinzel Decorative with responsive sizes.
- Ensure `page-break-inside: avoid` and confirm everything fits on a single page.

## 5. Chapter files (9–27)
All sixteen chapters must share the six-section structure described below.

### 5.1 General wrapper
- Set `<body class="chapter-page">`.
- Inside `<main epub:type="bodymatter chapter" role="main">`, wrap each section in its own `<section>` with relevant classes.

### 5.2 Section 1 – Title page
Structure:
```html
<section class="chap-title">
  <figure class="chapter-number-figure">
    <img class="chapter-number-brush" src="../images/brushstroke.svg" alt="Decorative brushstroke background"/>
    <figcaption class="chapter-number-roman">I</figcaption>
  </figure>
  <div class="title-stack">
    <div class="title-bar"></div>
    <div class="title-lines">
      <div class="title-line">Unveiling</div>
      <!-- one word per .title-line -->
    </div>
  </div>
  <figure class="bible-quote-container">
    <blockquote class="bible-quote-text">"Quoted scripture text."</blockquote>
    <figcaption class="bible-quote-reference">— Reference</figcaption>
  </figure>
  <h2 class="introduction-heading">Introduction</h2>
  <div class="introduction-paragraph dropcap-first-letter">
    <p><strong>P</strong>icture …</p>
  </div>
</section>
```
Implementation details:
- Replace numerals and titles with the correct content per chapter, one word per `.title-line`.
- Overlay the Roman numeral on the brushstroke via absolutely positioned CSS.
- Include bible quote and citation when provided; omit `<figure>` if none exists.
- Wrap introduction text so the first letter is styled using `.dropcap-first-letter`.
- Set `min-height: 100vh` and `.avoid-break` to keep the section intact.

### 5.3 Section 2 – Content body
```html
<section class="chap-body">
  <!-- original headings, paragraphs, blockquotes, and lists -->
</section>
```
- Preserve all existing text exactly.
- Remove inline styles and use `.chap-body` (plus optional `.content-area`) for consistent typography and spacing.
- For blockquotes, retain `<blockquote>` wrappers and optionally prepend `<span class="quote-marks-icon"></span>` for decoration.

### 5.4 Section 3 – Endnotes (optional)
```html
<section class="endnotes">
  <h2 class="endnotes-title">Endnotes</h2>
  <ol>
    <li>First note.</li>
    <!-- remaining notes -->
  </ol>
</section>
```
- Include only when notes exist. Apply smaller typography via CSS; you may use `endnote-marker.png` for numbering if desired.
- Insert `<div class="page-break"></div>` before this section when the previous section runs long.

### 5.5 Section 4 – Quiz
```html
<div class="page-break"></div>
<section class="quiz-container chap-quiz page-break-before avoid-break">
  <h2>Chapter Quiz</h2>
  <ol class="quiz-questions">
    <li><span class="opt-label">1.</span> Question text here.
      <ul class="quiz-options">
        <li class="quiz-option"><span class="opt-label">A.</span> Option A</li>
        <li class="quiz-option"><span class="opt-label">B.</span> Option B</li>
        <li class="quiz-option"><span class="opt-label">C.</span> Option C</li>
        <li class="quiz-option"><span class="opt-label">D.</span> Option D</li>
      </ul>
    </li>
    <!-- Repeat until four questions exist -->
  </ol>
  <p>For answers, see the Quiz Key in the backmatter.</p>
</section>
```
- Always provide four questions. Adjust numbering while preserving wording.
- Use ordered questions (`<ol>`) with nested unordered option lists (`<ul>`). Style labels via `.opt-label` and `.quiz-option`.
- Enforce `.page-break-before`/`.page-break-after` and limit `.quiz-container` to `max-height: 90vh`.
- If interactive checkboxes are retained, apply `.quiz-checkbox` and `.checked` for answer keys.

### 5.6 Section 5 – Worksheet
```html
<div class="page-break"></div>
<section class="worksheet page-break-before avoid-break">
  <h2>Worksheet Title</h2>
  <div class="activity-section">
    <p>Prompt text …</p>
    <div class="writing-area ruled-paper-bg"></div>
  </div>
</section>
```
- Start on a new page.
- Use `.worksheet` plus `.avoid-break` to keep it single-page. Add `.writing-area` with `.ruled-paper-bg` for lined entries.
- Maintain every prompt and instruction; split large tables if necessary but keep within `90vh`.

### 5.7 Section 6 – Closing image/quote
```html
<div class="page-break"></div>
<section class="closing image-quote page-break-before">
  <figure>
    <img src="../images/chapter-i-quote.jpeg" alt="Inspirational quote image"/>
    <figcaption>Optional caption.</figcaption>
  </figure>
</section>
```
- Reference the correct closing image per chapter (e.g., `chapter-ii-quote.jpeg`). Supply meaningful `alt` text.
- Style `.image-quote` to centre the image with `max-width: 80%`/`max-height: 70vh` and enforce `min-height: 90vh`.

### 5.8 Post-update checklist
1. Confirm each chapter contains six `<section>` blocks in order (body/endnotes optional; quiz, worksheet, closing remain even if placeholders).
2. Remove all inline styles; rely solely on CSS classes.
3. Verify page breaks with `<div class="page-break"></div>` to keep quizzes/worksheets on single pages.

## 6. Backmatter files (28–44 plus `nav.xhtml`)
Apply `<body class="backmatter-page">` and wrap content inside `.backmatter-page` or `.backmatter-card` containers.

### 6.1 Reference and narrative pages
Files: `28-Conclusion.xhtml`, `33-Acknowledgments.xhtml`, `34-AbouttheAuthor.xhtml`, `44-bibliography.xhtml`.
- Use `<section class="reference-page">` or specific variants (`.conclusion`, `.acknowledgments`, `.author-bio`, `.bibliography`).
- Keep narrative text in `<p>` elements and headings in `<h2>`/`<h3>`.
- For bibliographies, use `<ol>`/`<ul>` with styled markers.
- Ensure the layout fits a single page with `page-break-inside: avoid`.

### 6.2 Quiz key and assessment pages
Files: `29-QuizKey.xhtml`, `30-SelfAssessment.xhtml` (distinct from frontmatter self-assessment).
- Present quiz answers using tables or definition lists (`<dl>`) within `.quiz-key`.
- Use `.assessment` containers for scoring guidelines; `.answer-reference` can describe outcomes.

### 6.3 Inspirational/commitment pages
Files: `31-affirmations-close.xhtml`, `32-continued-learning-commitment.xhtml`, `35-CurlsContempCollective.xhtml`.
- Centre content using `.affirmations`, `.commitment`, or `.collective-info`.
- Incorporate decorative dividers (`decorative-line.svg`) or icons to break up sections.
- Maintain ample margins and single-page layouts.

### 6.4 Journal pages
Files: `36-JournalingStart.xhtml`, `37-ManifestingJournal.xhtml`, `38-journal-page.xhtml`, `41-self-care-journal.xhtml`, `42-VisionJournal.xhtml`.
- Wrap prompts in `<section class="journal">` containing `.journal-entry` or `.writing-area` blocks.
- Use CSS grid: two columns on desktop, one on mobile, with gaps between entries.
- Provide introductory instructions where applicable.
- Keep each journal within one page; split across files if necessary.

### 6.5 Worksheet pages
Files: `39-professional-development.xhtml`, `40-SMARTGoals.xhtml`, `43-DoodlePage.xhtml`.
- Wrap in `<section class="worksheet backmatter-worksheet">` with headings and `.activity-section` groups.
- Provide form inputs (`<input>`, `<textarea>`) or `.writing-area ruled-paper-bg` as appropriate.
- For the doodle page, supply a large blank `.writing-area` without the ruled background (override the background image) and add a subtle border.

### 6.6 Navigation page (`nav.xhtml`)
- Use `<nav class="nav toc-nav navigation-list" epub:type="toc">` with link labels matching updated titles and hierarchical structure via nested lists.
- Add `aria-label` attributes and ensure an `<h1>` heading exists.
- Keep the page single-screen; add `.page-break-before` if it appears at the end of the book.

## 7. Implementation and testing workflow
1. **Update CSS** – Merge the full ACISS layout rules into `style.css`, including responsive breakpoints at `768px` and `1024px`.
2. **Edit XHTML** – Sequentially update each file, wrapping content with the proper shells and removing inline styles while preserving text verbatim.
3. **Link images/icons** – Reference graphics with relative paths such as `../images/brushstroke.svg` and supply `alt` text for every `<img>`.
4. **Validate structure** – Confirm frontmatter/backmatter pages contain one `<section>` wrapper, chapters have six sections, and quizzes always feature four questions with proper page breaks.
5. **Preview** – Use an EPUB reader or Calibre to test across mobile, tablet, desktop, and print (via `print.css`). Verify single-page constraints, flow, and legibility.
6. **Accessibility** – Ensure every image has `alt` text, headings remain hierarchical, interactive components are keyboard accessible, and colour contrast meets WCAG guidelines.

## 8. Required class reference
- **Page wrappers** – `.frontmatter-page`, `.part-page`, `.chapter-page`, `.backmatter-page`
- **Frontmatter** – `.frontmatter-shell`, `.title-page`, `.copyright-page`, `.toc-page`, `.dedication-page`, `.worksheet`, `.preface-page`, `.frontmatter-title`, `.frontmatter-divider`
- **Part dividers** – `.part-divider`, `.part-title`, `.part-subtitle`, `.decorative-line`
- **Chapters** – `.chap-title`, `.chapter-number-figure`, `.chapter-number-brush`, `.chapter-number-roman`, `.title-stack`, `.title-bar`, `.title-line`, `.bible-quote-container`, `.introduction-heading`, `.introduction-paragraph`, `.dropcap-first-letter`, `.chap-body`, `.endnotes`, `.quiz-container`, `.quiz-questions`, `.quiz-option`, `.worksheet`, `.image-quote`, `.closing`
- **Backmatter** – `.conclusion`, `.acknowledgments`, `.author-bio`, `.bibliography`, `.quiz-key`, `.assessment`, `.answer-reference`, `.affirmations`, `.commitment`, `.collective-info`, `.journal`, `.writing-area`, `.journal-prompt`, `.worksheet`, `.activity-section`, `.form-field`, `.doodle-area`, `.nav`, `.toc-nav`, `.navigation-list`
- **Utility** – `.ruled-paper-bg`, `.toc-divider-img`, `.quiz-checkbox`, `.quote-marks-icon`, `.chapter-frame`, `.page-break`, `.page-break-before`, `.page-break-after`, `.avoid-break`, `.mobile-hidden`, `.print-only`

By following this handoff, the formatter can rebuild every XHTML page using the ACISS system while maintaining perfect text fidelity, delivering an EPUB that meets single-page front/back matter requirements, enforces the six-section chapter structure, and ensures every worksheet and interactive component renders consistently across devices and print output.
