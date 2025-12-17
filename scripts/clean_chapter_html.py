#!/usr/bin/env python3
"""
Clean malformed HTML in chapter XHTML files.

Fixes issues from BeautifulSoup processing by:
1. Removing stray closing tags before quote-page section
2. Ensuring proper structure
"""

import re
import sys
from pathlib import Path

# Chapter files to process
CHAPTER_FILES = [
    '9-chapter-i-unveiling-your-creative-odyssey.xhtml',
    '10-chapter-ii-refining-your-creative-toolkit.xhtml',
    '11-chapter-iii-reigniting-your-creative-fire.xhtml',
    '13-chapter-iv-the-art-of-networking-in-freelance-hairstyling.xhtml',
    '14-chapter-v-cultivating-creative-excellence-through-mentorship.xhtml',
    '15-chapter-vi-mastering-the-business-of-hairstyling.xhtml',
    '16-chapter-vii-embracing-wellness-and-self-care.xhtml',
    '17-chapter-viii-advancing-skills-through-continuous-education.xhtml',
    '19-chapter-ix-stepping-into-leadership.xhtml',
    '20-chapter-x-crafting-enduring-legacies.xhtml',
    '21-chapter-xi-advanced-digital-strategies-for-freelance-hairstylists.xhtml',
    '22-chapter-xii-financial-wisdom-building-sustainable-ventures.xhtml',
    '23-chapter-xiii-embracing-ethics-and-sustainability-in-hairstyling.xhtml',
    '25-chapter-xiv-the-impact-of-ai-on-the-beauty-industry.xhtml',
    '26-chapter-xv-cultivating-resilience-and-well-being-in-hairstyling.xhtml',
    '27-chapter-xvi-tresses-and-textures-embracing-diversity-in-hairstyling.xhtml',
]


def clean_chapter_html(filepath: Path, dry_run: bool = False) -> dict:
    """Clean malformed HTML in a chapter file."""
    result = {
        'filename': filepath.name,
        'issues_fixed': [],
        'error': None
    }

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content

        # Fix stray closing tags right before quote-page
        # Find the quote-page section and what's immediately before it
        match = re.search(r'((?:</\w+>)+)\s*(<section class="quote-page">)', content)
        if match:
            stray_tags = match.group(1)
            # Count opening vs closing tags - if there are more closings than expected, it's wrong
            if '</ol></section></div></section>' in stray_tags or '</section></section>' in stray_tags:
                result['issues_fixed'].append(f"Removed stray closing tags: {stray_tags}")
                # Replace with just a newline before quote-page
                content = re.sub(
                    r'((?:</\w+>)+)\s*(<section class="quote-page">)',
                    r'\n\n\2',
                    content
                )

        # Pattern 2: Ensure proper closing at end of file
        # Should end with: </section></main></body></html>
        end_pattern = re.compile(r'</section>\s*</main>\s*</body>\s*</html>\s*$')
        if not end_pattern.search(content):
            # Fix the ending
            content = re.sub(
                r'</section>\s*</main>\s*</body>\s*</html>\s*$',
                '</section>\n</main>\n</body>\n</html>\n',
                content
            )

        # Pattern 3: Clean up SECTION 6 comments that have stray closings after them
        content = re.sub(
            r'(<!-- SECTION 6: (?:IMAGE QUOTE|CLOSING IMAGE/QUOTE)[^>]*-->)\s*\n\s*((?:</\w+>)+)\s*\n',
            r'\1\n\n',
            content
        )

        if content != original:
            if not dry_run:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
            if not result['issues_fixed']:
                result['issues_fixed'].append("Cleaned malformed HTML structure")

        return result

    except Exception as e:
        result['error'] = str(e)
        return result


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Clean malformed HTML in chapter files')
    parser.add_argument('--root', type=str, default='REBRANDED_OUTPUT/xhtml',
                        help='Path to xhtml directory')
    parser.add_argument('--dry-run', action='store_true',
                        help='Report issues without making changes')

    args = parser.parse_args()

    xhtml_dir = Path(args.root)

    if not xhtml_dir.exists():
        print(f"Error: Directory not found: {xhtml_dir}")
        sys.exit(1)

    print("\n" + "=" * 70)
    print("HTML CLEANUP REPORT")
    print("=" * 70)
    print(f"Mode: {'DRY RUN' if args.dry_run else 'FIXING FILES'}")
    print("-" * 70)

    fixed_count = 0
    for filename in CHAPTER_FILES:
        filepath = xhtml_dir / filename
        if filepath.exists():
            result = clean_chapter_html(filepath, args.dry_run)
            if result['issues_fixed']:
                print(f"\n{filename}")
                for issue in result['issues_fixed']:
                    print(f"  - {issue}")
                fixed_count += 1
            if result['error']:
                print(f"\n{filename}")
                print(f"  ERROR: {result['error']}")

    print("\n" + "-" * 70)
    print(f"Summary: {len(CHAPTER_FILES)} files checked, {fixed_count} files cleaned")
    print("=" * 70)


if __name__ == '__main__':
    main()
