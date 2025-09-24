# Codex Execution Commands
## Step-by-Step Processing Instructions

### Initial Setup Commands

```bash
# 1. Start Codex in your project directory
codex --project epub-project/

# 2. Load the agent instructions
@agents Read and understand the AGENTS.md file completely. Confirm you understand the mission to maintain 100% content fidelity while implementing ACISS design.

# 3. Analyze the project structure
@agents Analyze the input/OEBPS/text/ directory. List all 44 files and categorize them into frontmatter (7), main content (20), and backmatter (17).

# 4. Create processing plan
@agents Create a detailed processing plan for all 44 files, starting with frontmatter, then part dividers, then chapters, then backmatter.
```

### Phase 1: Frontmatter Processing (Files 1-7)

```bash
@agents Process frontmatter files 1-7:
- Read each file completely, preserving every word exactly
- Apply basic ACISS styling with proper XHTML structure
- For the 2 activity worksheet files, convert interactive elements to static HTML
- Ensure dedication page is properly formatted
- Use consistent CSS classes and maintain proper file structure
- Output processed files to output/OEBPS/text/

Files to process:
1-[filename].xhtml
2-[filename].xhtml
3-[filename].xhtml
4-[filename].xhtml
5-[filename].xhtml
6-[filename].xhtml
7-[filename].xhtml
```

### Phase 2: Part Divider Processing (Files 8, 12, 18, 24)

```bash
@agents Process part divider files:
- Clean CSS link references to use "../styles/style.css" format
- Standardize HTML formatting with proper XHTML 1.1 structure
- Preserve all descriptive content exactly as written
- Apply consistent ACISS styling
- Remove empty whitespace sections
- Fix any broken references

Files to process:
8-Part-I-Foundations-of-Creative-Hairstyling.xhtml
12-Part-II-Building-Your-Professional-Practice.xhtml
18-Part-III-Advanced-Business-Strategies.xhtml
24-Part-IV-Future-Focused-Growth.xhtml
```

### Phase 3: Chapter Processing (16 Files) - CRITICAL PHASE

```bash
@agents CRITICAL PHASE - Chapter Processing. 
For each chapter file, implement the full ACISS design system with 6-page structure.
ABSOLUTE REQUIREMENT: Preserve 100% of original content - every word, footnote, case study, and implementation step.

Process these 16 chapter files using the exact template I've provided:

9-chapter-i-unveiling-your-creative-odyssey.xhtml
10-chapter-ii-refining-your-creative-toolkit.xhtml
11-chapter-iii-reigniting-your-creative-fire.xhtml
13-chapter-iv-the-art-of-networking-in-freelance-hairstyling.xhtml
14-chapter-v-cultivating-creative-excellence-through-mentorship.xhtml
15-chapter-vi-mastering-the-business-of-hairstyling.xhtml
16-chapter-vii-embracing-wellness-and-self-care.xhtml
17-chapter-viii-advancing-skills-through-continuous-education.xhtml
19-chapter-ix-stepping-into-leadership.xhtml
20-chapter-x-crafting-enduring-legacies.xhtml
21-chapter-xi-advanced-digital-strategies-for-freelance-hairstylists.xhtml
22-chapter-xii-financial-wisdom-building-sustainable-ventures.xhtml
23-chapter-xiii-embracing-ethics-and-sustainability-in-hairstyling.xhtml
25-chapter-xiv-the-impact-of-ai-on-the-beauty-industry.xhtml
26-chapter-xv-cultivating-resilience-and-well-being-in-hairstyling.xhtml
27-chapter-xvi-tresses-and-textures-embracing-diversity-in-hairstyling.xhtml

For EACH chapter, follow this exact process:
1. Extract chapter number and convert to Roman numeral
2. Extract exact chapter title and break into vertical lines
3. Find Bible quote and reference
4. Identify introduction paragraph with drop cap
5. Preserve ALL body content with proper section headings
6. Include ALL footnotes in endnotes page
7. Create quiz with maximum 4 questions
8. Add worksheet elements
9. Insert proper page breaks between sections
```

### Chapter-by-Chapter Processing Commands

```bash
# Process Chapter I
@agents Process file: 9-chapter-i-unveiling-your-creative-odyssey.xhtml
- Roman numeral: I
- Title: "UNVEILING YOUR CREATIVE ODYSSEY" (break into 4 lines)
- Extract Bible quote and reference exactly
- Preserve complete original content
- Apply 6-page ACISS structure
- Verify no content lost or modified

# Process Chapter II
@agents Process file: 10-chapter-ii-refining-your-creative-toolkit.xhtml
- Roman numeral: II
- Extract exact title and break into lines
- Find Bible quote if present
- Preserve all content including case studies and implementation steps
- Apply full ACISS design system

# Continue for each chapter...
# [Repeat similar commands for all 16 chapters]
```

### Phase 4: Backmatter Processing (Files 28-44)

```bash
@agents Process backmatter files 28-44:
- Apply consistent ACISS styling
- Preserve all content word-for-word
- Handle activity worksheet journals as static HTML elements
- Ensure proper cross-references and links
- Maintain professional formatting throughout

Files to process: 28-[filename].xhtml through 44-[filename].xhtml
```

### Verification Commands

```bash
# After each phase, run verification
@agents Verify the last processed files:
1. Compare word count with original files
2. Check that all footnotes are preserved
3. Confirm case studies are complete
4. Validate XHTML structure
5. Verify CSS classes are applied correctly

# If any issues found:
@agents STOP PROCESSING. Fix the identified issues before continuing.
Show me the specific problems and how they will be corrected.
```

### Quality Assurance Commands

```bash
# Final quality check
@agents Perform comprehensive quality assurance:
1. Validate all 44 processed files for XHTML compliance
2. Verify 100% content preservation across all files
3. Check consistent ACISS design implementation
4. Confirm proper page break placement
5. Validate all CSS class usage
6. Test file references and image paths

# Generate report
@agents Create a detailed report showing:
- Files processed successfully: [count]
- Content preservation status: [100% confirmed]
- XHTML validation results: [passed/failed]
- ACISS implementation consistency: [confirmed]
- Any issues that need attention: [list]
```

### Final Compilation Commands

```bash
# Prepare for EPUB compilation
@agents Final preparation checklist:
1. All 44 files processed and validated ✓
2. Content fidelity maintained at 100% ✓
3. ACISS design implemented consistently ✓
4. All CSS references correct ✓
5. Image paths verified ✓
6. XHTML structure valid ✓

# Ready for compilation
@agents Confirm all files are ready for EPUB compilation.
List any final items that need attention before running ./tools/compile.sh
```

### Emergency Stop Commands

```bash
# If content loss detected
@agents EMERGENCY STOP - Content truncation detected.
1. Stop all processing immediately
2. Restore from backup if necessary
3. Show me exactly what content was lost
4. Provide solution to prevent future content loss

# If validation fails
@agents VALIDATION FAILURE - Fix required.
1. Identify specific validation errors
2. Show exact line numbers and issues
3. Provide corrected code
4. Re-validate before continuing
```

### Success Verification Commands

```bash
# Final success check
@agents SUCCESS VERIFICATION:
1. Confirm all 44 files processed ✓
2. Content preservation: 100% maintained ✓
3. ACISS design: Fully implemented ✓
4. XHTML validation: All files pass ✓
5. Ready for device testing ✓

Project status: COMPLETE AND READY FOR PUBLICATION
```

## Usage Instructions

1. **Copy each command block** exactly as written
2. **Run commands in order** - do not skip phases
3. **Wait for confirmation** before proceeding to next phase
4. **Stop immediately** if any content loss is detected
5. **Verify success** at each checkpoint before continuing

## Critical Success Factors

- **NEVER allow content truncation** - stop and fix immediately
- **Preserve every word exactly** - no paraphrasing or summarization  
- **Apply ACISS design consistently** - use exact CSS classes
- **Validate continuously** - check XHTML at each step
- **Document any issues** - maintain clear communication with Codex

This systematic approach ensures professional results while maintaining absolute content integrity.