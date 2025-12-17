#!/usr/bin/env python3
"""
Fix duplicate quiz and worksheet sections in chapter files.
More aggressive approach using line-by-line parsing.
"""

import os
from pathlib import Path

# Allow configuration via environment variable or default to relative path
DEFAULT_XHTML_DIR = Path(__file__).parent.parent / "REBRANDED_OUTPUT" / "xhtml"
XHTML_DIR = Path(os.environ.get("XHTML_DIR", DEFAULT_XHTML_DIR))

CHAPTERS = [
    "10-chapter-ii-refining-your-creative-toolkit.xhtml",
    "11-chapter-iii-reigniting-your-creative-fire.xhtml",
    "13-chapter-iv-the-art-of-networking-in-freelance-hairstyling.xhtml",
    "14-chapter-v-cultivating-creative-excellence-through-mentorship.xhtml",
    "15-chapter-vi-mastering-the-business-of-hairstyling.xhtml",
    "16-chapter-vii-embracing-wellness-and-self-care.xhtml",
    "17-chapter-viii-advancing-skills-through-continuous-education.xhtml",
    "19-chapter-ix-stepping-into-leadership.xhtml",
    "20-chapter-x-crafting-enduring-legacies.xhtml",
    "21-chapter-xi-advanced-digital-strategies-for-freelance-hairstylists.xhtml",
    "22-chapter-xii-financial-wisdom-building-sustainable-ventures.xhtml",
    "23-chapter-xiii-embracing-ethics-and-sustainability-in-hairstyling.xhtml",
    "25-chapter-xiv-the-impact-of-ai-on-the-beauty-industry.xhtml",
    "26-chapter-xv-cultivating-resilience-and-well-being-in-hairstyling.xhtml",
    "27-chapter-xvi-tresses-and-textures-embracing-diversity-in-hairstyling.xhtml",
]


def find_section_boundaries(lines, start_pattern, end_tag):
    """
    Find all occurrences of a section type and return their line ranges.
    Returns list of (start_line, end_line) tuples.
    """
    sections = []
    i = 0
    while i < len(lines):
        if start_pattern in lines[i]:
            start = i
            # Find the closing tag
            depth = 1
            i += 1
            while i < len(lines) and depth > 0:
                if '<section' in lines[i] or '<aside' in lines[i]:
                    depth += 1
                if end_tag in lines[i]:
                    depth -= 1
                    if depth == 0:
                        sections.append((start, i))
                        break
                i += 1
        i += 1
    return sections


def remove_duplicate_sections(content):
    """Remove duplicate quiz and worksheet sections, keeping only the first."""

    lines = content.split('\n')
    lines_to_remove = set()

    # Find all quiz sections
    quiz_sections = []
    for i, line in enumerate(lines):
        if 'class="quiz-container' in line or 'class="quiz ' in line:
            # Found a quiz section start
            start = i
            # Find end of this section
            depth = 1
            j = i + 1
            while j < len(lines) and depth > 0:
                if '<section' in lines[j]:
                    depth += 1
                if '</section>' in lines[j]:
                    depth -= 1
                    if depth == 0:
                        quiz_sections.append((start, j))
                        break
                j += 1

    # Keep only the first quiz section
    if len(quiz_sections) > 1:
        print(f"   Found {len(quiz_sections)} quiz sections, removing duplicates")
        for start, end in quiz_sections[1:]:
            for line_num in range(start, end + 1):
                lines_to_remove.add(line_num)

    # Find all worksheet sections
    worksheet_sections = []
    for i, line in enumerate(lines):
        if 'class="worksheet' in line and '<section' in line:
            # Found a worksheet section start
            start = i
            # Find end of this section
            depth = 1
            j = i + 1
            while j < len(lines) and depth > 0:
                if '<section' in lines[j]:
                    depth += 1
                if '</section>' in lines[j]:
                    depth -= 1
                    if depth == 0:
                        worksheet_sections.append((start, j))
                        break
                j += 1

    # Keep only the first worksheet section
    if len(worksheet_sections) > 1:
        print(f"   Found {len(worksheet_sections)} worksheet sections, removing duplicates")
        for start, end in worksheet_sections[1:]:
            for line_num in range(start, end + 1):
                lines_to_remove.add(line_num)

    # Remove marked lines
    if lines_to_remove:
        cleaned_lines = [line for i, line in enumerate(lines) if i not in lines_to_remove]
        return '\n'.join(cleaned_lines)

    return content


def clean_trailing_content(content):
    """Ensure clean ending after </main>."""
    # Find last </main>
    main_idx = content.rfind('</main>')
    if main_idx == -1:
        return content

    # Keep everything up to and including </main>, then just closing tags
    return content[:main_idx + 7] + '\n</body>\n</html>\n'


def main():
    print("=" * 70)
    print("Fixing Duplicate Quiz/Worksheet Sections")
    print("=" * 70)
    print()

    fixed_count = 0

    for chapter_file in CHAPTERS:
        filepath = XHTML_DIR / chapter_file

        if not filepath.exists():
            print(f"⚠️  File not found: {chapter_file}")
            continue

        print(f"Processing {chapter_file}...")

        original_content = filepath.read_text(encoding='utf-8')

        # Count issues before
        quiz_before = original_content.count('class="quiz-container')
        quiz_before += original_content.count('class="quiz ')
        worksheet_before = original_content.count('<section class="worksheet')

        if quiz_before <= 1 and worksheet_before <= 1:
            print(f"   ✓ Already clean (quiz:{quiz_before}, worksheet:{worksheet_before})")
            print()
            continue

        print(f"   Before: quiz sections={quiz_before}, worksheet sections={worksheet_before}")

        # Apply fixes
        cleaned_content = remove_duplicate_sections(original_content)
        cleaned_content = clean_trailing_content(cleaned_content)

        # Count after
        quiz_after = cleaned_content.count('class="quiz-container')
        quiz_after += cleaned_content.count('class="quiz ')
        worksheet_after = cleaned_content.count('<section class="worksheet')

        print(f"   After:  quiz sections={quiz_after}, worksheet sections={worksheet_after}")

        if cleaned_content != original_content:
            # Create backup of original
            backup_path = filepath.with_suffix('.xhtml.bak2')
            backup_path.write_text(original_content, encoding='utf-8')

            # Write cleaned version
            filepath.write_text(cleaned_content, encoding='utf-8')
            print(f"   ✅ Fixed and saved (backup: {backup_path.name})")
            fixed_count += 1
        else:
            print(f"   ℹ️  No changes made")

        print()

    print("=" * 70)
    print(f"✅ Fixed {fixed_count} chapter files")
    print("=" * 70)


if __name__ == "__main__":
    main()
