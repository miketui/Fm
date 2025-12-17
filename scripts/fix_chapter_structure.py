#!/usr/bin/env python3
"""
Fix EPUB Chapter Structure Script

Restructures chapter XHTML files to follow the correct format:
1. Title page section
2. Page break
3. Body content section
4. Page break
5. Quiz section (single, no duplicates)
6. Page break
7. Worksheet section (single, no duplicates)
8. Footnotes/Endnotes section (single)
9. Quote-page section with chapter image quote

Removes duplicate sections and ensures proper closing image quote.
"""

import sys
from pathlib import Path
from bs4 import BeautifulSoup

# Chapter mapping for roman numerals to image filenames
CHAPTER_MAP = {
    '9-chapter-i-unveiling-your-creative-odyssey.xhtml': ('I', 'chapter-i-quote.jpeg'),
    '10-chapter-ii-refining-your-creative-toolkit.xhtml': ('II', 'chapter-ii-quote.jpeg'),
    '11-chapter-iii-reigniting-your-creative-fire.xhtml': ('III', 'chapter-iii-quote.jpeg'),
    '13-chapter-iv-the-art-of-networking-in-freelance-hairstyling.xhtml': ('IV', 'chapter-iv-quote.jpeg'),
    '14-chapter-v-cultivating-creative-excellence-through-mentorship.xhtml': ('V', 'chapter-v-quote.jpeg'),
    '15-chapter-vi-mastering-the-business-of-hairstyling.xhtml': ('VI', 'chapter-vi-quote.jpeg'),
    '16-chapter-vii-embracing-wellness-and-self-care.xhtml': ('VII', 'chapter-vii-quote.jpeg'),
    '17-chapter-viii-advancing-skills-through-continuous-education.xhtml': ('VIII', 'chapter-viii-quote.jpeg'),
    '19-chapter-ix-stepping-into-leadership.xhtml': ('IX', 'chapter-ix-quote.jpeg'),
    '20-chapter-x-crafting-enduring-legacies.xhtml': ('X', 'chapter-x-quote.jpeg'),
    '21-chapter-xi-advanced-digital-strategies-for-freelance-hairstylists.xhtml': ('XI', 'chapter-xi-quote.jpeg'),
    '22-chapter-xii-financial-wisdom-building-sustainable-ventures.xhtml': ('XII', 'chapter-xii-quote.jpeg'),
    '23-chapter-xiii-embracing-ethics-and-sustainability-in-hairstyling.xhtml': ('XIII', 'chapter-xiii-quote.jpeg'),
    '25-chapter-xiv-the-impact-of-ai-on-the-beauty-industry.xhtml': ('XIV', 'chapter-xiv-quote.jpeg'),
    '26-chapter-xv-cultivating-resilience-and-well-being-in-hairstyling.xhtml': ('XV', 'chapter-xv-quote.jpeg'),
    '27-chapter-xvi-tresses-and-textures-embracing-diversity-in-hairstyling.xhtml': ('XVI', 'chapter-xvi-quote.jpeg'),
}


def create_quote_page_section(roman_numeral: str, image_filename: str) -> str:
    """Create the closing quote-page section HTML."""
    return f'''
<section class="quote-page">
<figure>
<img src="../images/{image_filename}" alt="Inspirational quote for Chapter {roman_numeral}" />
</figure>
</section>'''


def fix_chapter_structure(filepath: Path, dry_run: bool = False) -> dict:
    """
    Fix a single chapter file's structure.

    Returns dict with:
        - filename: str
        - issues_found: list of issues
        - fixed: bool
        - error: str or None
    """
    result = {
        'filename': filepath.name,
        'issues_found': [],
        'fixed': False,
        'error': None
    }

    if filepath.name not in CHAPTER_MAP:
        result['error'] = f"Not a chapter file or not in mapping"
        return result

    roman_numeral, image_filename = CHAPTER_MAP[filepath.name]

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')
        main_tag = soup.find('main')

        if not main_tag:
            result['error'] = "No <main> tag found"
            return result

        # Find all sections by type
        quiz_sections = main_tag.find_all('section', class_=lambda x: x and 'quiz' in x)
        worksheet_sections = main_tag.find_all('section', class_=lambda x: x and 'worksheet' in x)
        endnotes_sections = main_tag.find_all(['aside', 'section'], class_=lambda x: x and ('endnotes' in x or 'footnotes' in x))
        quote_sections = main_tag.find_all('section', class_=lambda x: x and ('quote-page' in x or 'image-quote' in x))

        # Track issues
        if len(quiz_sections) > 1:
            result['issues_found'].append(f"Duplicate quiz sections: {len(quiz_sections)}")
        if len(worksheet_sections) > 1:
            result['issues_found'].append(f"Duplicate worksheet sections: {len(worksheet_sections)}")
        if len(endnotes_sections) > 1:
            result['issues_found'].append(f"Duplicate endnotes sections: {len(endnotes_sections)}")
        if len(quote_sections) > 1:
            result['issues_found'].append(f"Duplicate quote sections: {len(quote_sections)}")
        if len(quote_sections) == 0:
            result['issues_found'].append("Missing quote-page section")

        # Check if quote section has correct image
        correct_image = False
        for qs in quote_sections:
            img = qs.find('img')
            if img and image_filename in img.get('src', ''):
                correct_image = True
                break

        if quote_sections and not correct_image:
            result['issues_found'].append(f"Quote section missing correct image: {image_filename}")

        if not result['issues_found']:
            result['fixed'] = True  # Already correct
            return result

        # === FIX THE STRUCTURE ===

        # Keep only the first of each section type, remove duplicates
        for i, section in enumerate(quiz_sections[1:], 1):
            section.decompose()

        for i, section in enumerate(worksheet_sections[1:], 1):
            section.decompose()

        for i, section in enumerate(endnotes_sections[1:], 1):
            section.decompose()

        # Remove all existing quote sections - we'll add a clean one at the end
        for section in quote_sections:
            section.decompose()

        # Remove stray duplicate quiz-question-blocks that might be outside quiz section
        # (seen in chapter I where quiz content appears inside worksheet)
        for ws in main_tag.find_all('section', class_=lambda x: x and 'worksheet' in x):
            for quiz_block in ws.find_all('div', class_='quiz-question-block'):
                quiz_block.decompose()

        # Add the correct quote-page section at the end of main
        quote_html = create_quote_page_section(roman_numeral, image_filename)
        quote_soup = BeautifulSoup(quote_html, 'html.parser')

        # Find the closing </main> and insert before it
        main_tag.append(quote_soup.section)

        if not dry_run:
            # Write the fixed content
            with open(filepath, 'w', encoding='utf-8') as f:
                # Use prettify but preserve original doctype
                output = str(soup)
                # Ensure proper XML declaration and doctype
                if not output.startswith('<?xml'):
                    output = '<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n' + output
                f.write(output)

        result['fixed'] = True
        return result

    except Exception as e:
        result['error'] = str(e)
        return result


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Fix EPUB chapter file structures')
    parser.add_argument('--root', type=str, default='REBRANDED_OUTPUT/xhtml',
                        help='Path to xhtml directory')
    parser.add_argument('--dry-run', action='store_true',
                        help='Report issues without making changes')
    parser.add_argument('--file', type=str, default=None,
                        help='Fix a single file instead of all chapters')

    args = parser.parse_args()

    xhtml_dir = Path(args.root)

    if not xhtml_dir.exists():
        print(f"Error: Directory not found: {xhtml_dir}")
        sys.exit(1)

    results = []

    if args.file:
        filepath = xhtml_dir / args.file
        if not filepath.exists():
            print(f"Error: File not found: {filepath}")
            sys.exit(1)
        results.append(fix_chapter_structure(filepath, args.dry_run))
    else:
        for filename in CHAPTER_MAP.keys():
            filepath = xhtml_dir / filename
            if filepath.exists():
                results.append(fix_chapter_structure(filepath, args.dry_run))
            else:
                results.append({
                    'filename': filename,
                    'issues_found': [],
                    'fixed': False,
                    'error': 'File not found'
                })

    # Print report
    print("\n" + "=" * 70)
    print("CHAPTER STRUCTURE FIX REPORT")
    print("=" * 70)
    print(f"Mode: {'DRY RUN' if args.dry_run else 'FIXING FILES'}")
    print("-" * 70)

    total_issues = 0
    fixed_count = 0
    error_count = 0

    for r in results:
        status = "✓ OK" if r['fixed'] and not r['issues_found'] else ""
        if r['error']:
            status = f"✗ ERROR: {r['error']}"
            error_count += 1
        elif r['issues_found']:
            if r['fixed']:
                status = "✓ FIXED"
                fixed_count += 1
            else:
                status = "⚠ ISSUES"
            total_issues += len(r['issues_found'])

        print(f"\n{r['filename']}")
        print(f"  Status: {status}")
        if r['issues_found']:
            for issue in r['issues_found']:
                print(f"    - {issue}")

    print("\n" + "-" * 70)
    print(f"Summary: {len(results)} files checked, {total_issues} issues found, {fixed_count} fixed, {error_count} errors")
    print("=" * 70)

    return 0 if error_count == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
