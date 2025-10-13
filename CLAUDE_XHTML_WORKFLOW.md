# Claude XHTML Production Workflow Guide

## Using Claude's Code Execution & File Creation Features for Production-Ready XHTML

### **Overview**
This workflow leverages Claude's powerful features to create, enhance, and validate 45 production-ready XHTML files for your EPUB.

---

## **Phase 1: Automated File Creation** 
*Use Claude's `create_file` feature*

### **Step 1.1: Create Individual XHTML Files**

**Command Pattern for Claude:**
```
Create a production-ready XHTML file for [FILENAME] with:
- Single-page layout constraint (for frontmatter)
- 6-section structure (for chapters) 
- Proper CSS styling and font loading
- EPUB accessibility compliance
```

**Example Claude Request:**
```
create_file /root/repo/output/OEBPS/text/1-TitlePage.xhtml

[Claude will generate production-ready XHTML with:]
- XML declaration and DOCTYPE
- Proper head section with CSS links
- Single-page layout styles (min-height: 100vh)
- Semantic HTML structure
- Mobile and e-reader optimization
```

### **Step 1.2: Batch File Creation** 

**Command for Claude:**
```
Use the create_file tool to generate all 44 production-ready XHTML files based on the file list:
- Frontmatter files (1-7): Single-page layouts
- Chapter files (16 chapters): 6-section structure with page breaks
- Part dividers (4 files): Clean divider layouts  
- Backmatter files (17 files): Journal/worksheet layouts
```

---

## **Phase 2: Code Execution Enhancement**
*Use Claude's code execution for automation*

### **Step 2.1: Run Production Enhancement Script**

**Command for Claude:**
```bash
# Execute the production enhancement script
node /root/repo/scripts/claude-xhtml-production.js
```

This will:
- ✅ Process all 45 XHTML files
- ✅ Apply production enhancements
- ✅ Validate layout compliance
- ✅ Generate production report

### **Step 2.2: Validate Production Quality**

**Command for Claude:**
```bash
# Run comprehensive validation
npm run validate:production-xhtml

# Check specific file types
npm run validate:frontmatter   # Files 1-7
npm run validate:chapters      # 16 chapter files  
npm run validate:backmatter    # Files 28-44
```

---

## **Phase 3: Specific File Type Production**

### **Frontmatter Files (1-7) - Single-Page Layouts**

**Claude Commands:**
```
1. Create production-ready 1-TitlePage.xhtml with:
   - Centered title/subtitle/author layout
   - min-height: 100vh constraint
   - page-break-inside: avoid
   - Responsive typography

2. Create production-ready 2-Copyright.xhtml with:
   - Legal text formatting
   - Single-page constraint
   - Professional copyright layout

3. Create production-ready 3-TableOfContents.xhtml with:
   - Clickable navigation links
   - Compact single-page layout
   - Decorative dividers

[Continue for files 4-7...]
```

### **Chapter Files (16 chapters) - 6-Section Structure**

**Claude Template Application:**
```
For each chapter file (e.g., 9-chapter-i-unveiling-your-creative-odyssey.xhtml):

create_file with 6-section structure:

Section 1: Title Page
- Roman numeral badge (centered top)
- Title stack (vertical left-aligned)
- Bible quote container (pill design)
- Introduction with dropcap

Section 2: Chapter Content  
- Main chapter text
- Proper typography
- Natural flow pagination

Section 3: Endnotes
- Reference formatting
- Numbered list

Section 4: Quiz (FORCED PAGE BREAK)
- page-break-before: always
- max-height: 90vh constraint
- Exactly 4 multiple-choice questions
- Single-page only

Section 5: Worksheet (FORCED PAGE BREAK)  
- page-break-before: always
- max-height: 90vh constraint
- Interactive elements
- Single-page only

Section 6: Closing Image (FORCED PAGE BREAK)
- page-break-before: always
- Centered responsive image
- min-height: 90vh
- Image caption
```

### **Backmatter Files (28-44) - Journal & Worksheet Layouts**

**Claude Commands for Interactive Elements:**
```
Create production-ready journal/worksheet files with:
- Interactive form elements
- Writing spaces and prompts
- Guided activity sections
- Professional formatting
```

---

## **Phase 4: Production Validation**

### **Step 4.1: Layout Validation**

**Claude Execution Commands:**
```javascript
// Validate single-page constraints (frontmatter)
await validateSinglePageLayouts([
  '1-TitlePage.xhtml',
  '2-Copyright.xhtml', 
  '3-TableOfContents.xhtml',
  // ... files 4-7
]);

// Validate 6-section structure (chapters)  
await validateChapterStructures([
  '9-chapter-i-unveiling-your-creative-odyssey.xhtml',
  '10-chapter-ii-refining-your-creative-toolkit.xhtml',
  // ... all 16 chapter files
]);

// Validate forced page breaks
await validatePageBreaks(['quiz', 'worksheet', 'closing-image']);
```

### **Step 4.2: CSS & Font Validation**

**Claude Commands:**
```bash
# Validate all fonts loading correctly
node -e "
const validator = require('./scripts/claude-xhtml-production.js');
validator.validateFonts([
  'librebaskerville-regular.woff2',
  'librebaskerville-bold.woff2', 
  'librebaskerville-italic.woff2',
  'CinzelDecorative.woff2',
  'Montserrat-Regular.woff2',
  'Montserrat-Bold.woff2'
]);
"

# Validate CSS classes usage
node -e "
validator.validateCSSClasses([
  '.chap-title',
  '.chapter-number-container',
  '.title-stack', 
  '.bible-quote-container',
  '.quiz-container',
  '.worksheet',
  '.page-break-before'
]);
"
```

---

## **Phase 5: Production Build & Export**

### **Step 5.1: Generate Final Production EPUB**

**Claude Commands:**
```bash
# Build production EPUB with all enhancements
npm run build:production

# Validate final EPUB
java -jar epubcheck.jar output/production-epub.epub

# Generate distribution package
npm run package:distribution
```

### **Step 5.2: Multi-Format Export**

**Claude Requests:**
```
1. Generate Kindle-compatible version:
   - Convert XHTML for Kindle rendering
   - Optimize for Kindle typography
   - Package as .mobi format

2. Generate print-ready PDF:
   - Apply print media queries
   - Ensure 300 DPI image resolution
   - Optimize page breaks for print

3. Generate accessibility-enhanced version:
   - Add ARIA labels
   - Enhance screen reader compatibility  
   - Validate WCAG 2.1 AA compliance
```

---

## **Production Commands Summary**

### **Essential Claude Commands:**

**1. Batch File Creation:**
```
Use create_file to generate all 45 production-ready XHTML files with appropriate templates and styling
```

**2. Automated Enhancement:**  
```bash
node /root/repo/scripts/claude-xhtml-production.js
```

**3. Validation Pipeline:**
```bash
npm run validate:all-xhtml
npm run validate:production-ready  
npm run validate:commercial-distribution
```

**4. Final Production Build:**
```bash
npm run build:production-epub
npm run validate:final-epub
npm run package:distribution-ready
```

---

## **Quality Assurance Checklist**

### **✅ Production Readiness Validation:**

**Frontmatter (Files 1-7):**
- [ ] Single-page layout constraints applied
- [ ] No content overflow beyond viewport
- [ ] Consistent typography and styling
- [ ] Mobile and e-reader optimization

**Chapters (16 files):**  
- [ ] 6-section structure implemented
- [ ] Forced page breaks for quiz/worksheet/closing
- [ ] Single-page constraints on quiz and worksheet
- [ ] Template compliance verified

**Technical:**
- [ ] All 6 fonts loading correctly
- [ ] CSS validation passes
- [ ] EPUB validation (EPUBCheck) passes
- [ ] Accessibility compliance verified

**Commercial Distribution:**
- [ ] Amazon Kindle compatible
- [ ] Apple Books compatible  
- [ ] Google Play Books compatible
- [ ] Print-on-demand ready (300 DPI images)
- [ ] File size under platform limits

---

## **Pro Tips for Using Claude's Features:**

1. **Parallel Processing:** Request multiple file creations simultaneously for efficiency

2. **Template Reuse:** Create master templates first, then apply to multiple files

3. **Validation Integration:** Use code execution to validate after each creation step

4. **Incremental Enhancement:** Start with basic structure, then enhance with specific features

5. **Error Handling:** Use Claude's code execution to catch and fix common issues automatically

---

**Ready to start? Begin with Phase 1, Step 1.1 and work through each phase systematically.**
