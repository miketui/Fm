#!/usr/bin/env python3
"""
Restructure chapter XHTML files to extract image quotes into standalone files.
Removes duplicate content and properly formats chapters according to EPUB 3.2 spec.
"""

import re
import shutil
from pathlib import Path
from typing import Tuple, Optional

# Map of chapter files to their Roman numerals and image filenames
CHAPTERS = [
    ("9-chapter-i-unveiling-your-creative-odyssey.xhtml", "I", "chapter-i-quote.jpeg", "Unveiling Your Creative Odyssey"),
    ("10-chapter-ii-refining-your-creative-toolkit.xhtml", "II", "chapter-ii-quote.jpeg", "Refining Your Creative Toolkit"),
    ("11-chapter-iii-reigniting-your-creative-fire.xhtml", "III", "chapter-iii-quote.jpeg", "Reigniting Your Creative Fire"),
    ("13-chapter-iv-the-art-of-networking-in-freelance-hairstyling.xhtml", "IV", "chapter-iv-quote.jpeg", "The Art of Networking in Freelance Hairstyling"),
    ("14-chapter-v-cultivating-creative-excellence-through-mentorship.xhtml", "V", "chapter-v-quote.jpeg", "Cultivating Creative Excellence Through Mentorship"),
    ("15-chapter-vi-mastering-the-business-of-hairstyling.xhtml", "VI", "chapter-vi-quote.jpeg", "Mastering the Business of Hairstyling"),
    ("16-chapter-vii-embracing-wellness-and-self-care.xhtml", "VII", "chapter-vii-quote.jpeg", "Embracing Wellness and Self-Care"),
    ("17-chapter-viii-advancing-skills-through-continuous-education.xhtml", "VIII", "chapter-viii-quote.jpeg", "Advancing Skills Through Continuous Education"),
    ("19-chapter-ix-stepping-into-leadership.xhtml", "IX", "chapter-ix-quote.jpeg", "Stepping Into Leadership"),
    ("20-chapter-x-crafting-enduring-legacies.xhtml", "X", "chapter-x-quote.jpeg", "Crafting Enduring Legacies"),
    ("21-chapter-xi-advanced-digital-strategies-for-freelance-hairstylists.xhtml", "XI", "chapter-xi-quote.jpeg", "Advanced Digital Strategies for Freelance Hairstylists"),
    ("22-chapter-xii-financial-wisdom-building-sustainable-ventures.xhtml", "XII", "chapter-xii-quote.jpeg", "Financial Wisdom Building Sustainable Ventures"),
    ("23-chapter-xiii-embracing-ethics-and-sustainability-in-hairstyling.xhtml", "XIII", "chapter-xiii-quote.jpeg", "Embracing Ethics and Sustainability in Hairstyling"),
    ("25-chapter-xiv-the-impact-of-ai-on-the-beauty-industry.xhtml", "XIV", "chapter-xiv-quote.jpeg", "The Impact of AI on the Beauty Industry"),
    ("26-chapter-xv-cultivating-resilience-and-well-being-in-hairstyling.xhtml", "XV", "chapter-xv-quote.jpeg", "Cultivating Resilience and Well-Being in Hairstyling"),
    ("27-chapter-xvi-tresses-and-textures-embracing-diversity-in-hairstyling.xhtml", "XVI", "chapter-xvi-quote.jpeg", "Tresses and Textures Embracing Diversity in Hairstyling"),
]

XHTML_DIR = Path("/root/repo/REBRANDED_OUTPUT/xhtml")


def create_standalone_quote_file(
    output_filename: str,
    roman_numeral: str,
    image_filename: str,
    chapter_title: str
) -> str:
    """Create a standalone XHTML file for chapter quote image."""

    template = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en" xml:lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Chapter {roman_numeral} Quote – The Artisan's Path</title>
  <link rel="stylesheet" type="text/css" href="styles/fonts.css"/>
  <link rel="stylesheet" type="text/css" href="styles/style.css"/>
  <link rel="stylesheet" type="text/css" href="styles/print.css" media="print"/>
</head>
<body class="quote-page">
  <main role="main">
    <section class="image-quote page" role="region" aria-label="Chapter {roman_numeral} Inspirational Quote">
      <figure class="quote-figure">
        <img src="../images/{image_filename}"
             alt="Inspirational quote for Chapter {roman_numeral}: {chapter_title}"/>
      </figure>
    </section>
  </main>
</body>
</html>
'''

    return template.strip()


def remove_image_quote_sections(content: str) -> str:
    """Remove all image quote sections from chapter content."""

    # Remove SECTION 6 comment and following image-quote sections
    # Pattern 1: <!-- SECTION 6: IMAGE QUOTE ... --> ... </section>
    content = re.sub(
        r'<!-- SECTION 6: IMAGE QUOTE.*?-->.*?</section>\s*',
        '',
        content,
        flags=re.DOTALL
    )

    # Pattern 2: Standalone <section class="quote-page"> ... </section>
    content = re.sub(
        r'<section class="quote-page">.*?</section>',
        '',
        content,
        flags=re.DOTALL
    )

    # Pattern 3: Any remaining image-quote class sections
    content = re.sub(
        r'<section[^>]*class="[^"]*image-quote[^"]*"[^>]*>.*?</section>',
        '',
        content,
        flags=re.DOTALL
    )

    return content


def remove_duplicate_sections(content: str) -> str:
    """Remove duplicate quiz/worksheet/endnote sections."""

    # Find all quiz sections
    quiz_sections = list(re.finditer(
        r'<section[^>]*class="[^"]*quiz[^"]*"[^>]*>.*?</section>',
        content,
        flags=re.DOTALL
    ))

    # If multiple quiz sections found, keep only the first one
    if len(quiz_sections) > 1:
        for match in reversed(quiz_sections[1:]):
            content = content[:match.start()] + content[match.end():]

    # Find all worksheet sections
    worksheet_sections = list(re.finditer(
        r'<section[^>]*class="[^"]*worksheet[^"]*"[^>]*>.*?</section>',
        content,
        flags=re.DOTALL
    ))

    # If multiple worksheet sections found, keep only the first one
    if len(worksheet_sections) > 1:
        for match in reversed(worksheet_sections[1:]):
            content = content[:match.start()] + content[match.end():]

    # Find all endnotes sections (be more careful with this)
    endnotes_sections = list(re.finditer(
        r'<aside[^>]*class="[^"]*endnotes[^"]*"[^>]*>.*?</aside>',
        content,
        flags=re.DOTALL
    ))

    # If multiple endnotes sections found, keep only the first one
    if len(endnotes_sections) > 1:
        for match in reversed(endnotes_sections[1:]):
            content = content[:match.start()] + content[match.end():]

    return content


def clean_trailing_content(content: str) -> str:
    """Clean up any trailing content after closing main tag."""

    # Find the last </main> tag
    main_close = content.rfind('</main>')
    if main_close == -1:
        return content

    # Keep everything up to and including </main>, then just </body></html>
    return content[:main_close + 7] + '\n</body>\n</html>\n'


def process_chapter_file(filepath: Path, roman_numeral: str) -> Tuple[str, bool]:
    """
    Process a chapter file to remove image quotes and duplicates.
    Returns (cleaned_content, had_issues).
    """

    content = filepath.read_text(encoding='utf-8')
    original_content = content

    # Remove image quote sections
    content = remove_image_quote_sections(content)

    # Remove duplicate sections
    content = remove_duplicate_sections(content)

    # Clean trailing content
    content = clean_trailing_content(content)

    # Check if any changes were made
    had_issues = (content != original_content)

    return content, had_issues


def main():
    """Main execution function."""

    print("=" * 70)
    print("EPUB Chapter Restructuring Script")
    print("=" * 70)
    print()

    modified_chapters = []
    created_quotes = []

    for chapter_file, roman, image_file, title in CHAPTERS:
        chapter_path = XHTML_DIR / chapter_file

        if not chapter_path.exists():
            print(f"⚠️  Chapter file not found: {chapter_file}")
            continue

        print(f"Processing Chapter {roman}: {chapter_file}")

        # Process chapter file
        cleaned_content, had_issues = process_chapter_file(chapter_path, roman)

        if had_issues:
            # Create backup copy before modifying original
            backup_path = chapter_path.with_suffix('.xhtml.bak')
            try:
                shutil.copy2(chapter_path, backup_path)
                print(f"   ✓ Backed up original to {backup_path.name}")
                
                # Write cleaned content (original file preserved if this fails)
                chapter_path.write_text(cleaned_content, encoding='utf-8')
                print(f"   ✓ Removed image quotes and duplicates")
                modified_chapters.append(chapter_file)
            except (IOError, OSError, UnicodeError) as e:
                print(f"   ❌ Error processing {chapter_file}: {e}")
                # Original file is preserved since we used copy instead of rename
                if backup_path.exists():
                    backup_path.unlink()  # Clean up partial backup if needed
                continue
        else:
            print(f"   ℹ️  No issues found (already clean)")

        # Create standalone quote file
        # Extract base filename (e.g., "9" from "9-chapter-i-...")
        base_num = chapter_file.split('-')[0]
        quote_filename = f"{base_num}a-chapter-{roman.lower()}-quote.xhtml"
        quote_path = XHTML_DIR / quote_filename

        quote_content = create_standalone_quote_file(
            quote_filename,
            roman,
            image_file,
            title
        )

        quote_path.write_text(quote_content, encoding='utf-8')
        print(f"   ✓ Created standalone quote file: {quote_filename}")
        created_quotes.append(quote_filename)
        print()

    # Summary
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Modified chapters: {len(modified_chapters)}")
    print(f"Created quote files: {len(created_quotes)}")
    print()

    if modified_chapters:
        print("Modified chapters:")
        for ch in modified_chapters:
            print(f"  - {ch}")
        print()

    print("Created quote files:")
    for qf in created_quotes:
        print(f"  - {qf}")
    print()

    print("✅ Chapter restructuring complete!")
    print()
    print("Next steps:")
    print("  1. Review modified chapter files")
    print("  2. Update content.opf manifest and spine")
    print("  3. Run EPUBCheck validation")


if __name__ == "__main__":
    main()
