#!/usr/bin/env python3
"""
Fix remaining EPUB validation errors:
1. Fix malformed quiz HTML in chapter I (missing <ol> wrapper)
2. Resolve duplicate element IDs in chapters VI, VII, VIII
3. Remove obsolete CSS references from content.opf
"""

import re
from pathlib import Path
from bs4 import BeautifulSoup
import sys

def fix_chapter_i_quiz(xhtml_path):
    """Fix missing <ol> wrapper for quiz questions in chapter I"""
    print(f"Fixing quiz structure in {xhtml_path.name}...")

    with open(xhtml_path, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    # Find the quiz section
    quiz_section = soup.find('section', class_='quiz-container')
    if not quiz_section:
        print(f"  ⚠️  No quiz section found")
        return False

    # Check if there's already an <ol> wrapper
    quiz_ol = quiz_section.find('ol', class_='mcq-list')
    if quiz_ol:
        print(f"  ✓ Quiz already has <ol> wrapper")
        return False

    # Find all <li class="mcq-item"> that are direct children
    mcq_items = quiz_section.find_all('li', class_='mcq-item', recursive=False)
    if not mcq_items:
        print(f"  ⚠️  No mcq-item elements found")
        return False

    print(f"  Found {len(mcq_items)} quiz questions to wrap")

    # Create the <ol> wrapper
    ol_tag = soup.new_tag('ol', **{'class': 'mcq-list'})

    # Insert the <ol> before the first mcq-item
    first_item = mcq_items[0]
    first_item.insert_before(ol_tag)

    # Move all mcq-items into the <ol>
    for item in mcq_items:
        item.extract()
        ol_tag.append(item)

    # Write back
    with open(xhtml_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    print(f"  ✓ Wrapped {len(mcq_items)} questions in <ol class='mcq-list'>")
    return True


def fix_duplicate_ids(xhtml_path):
    """Fix duplicate element IDs in a chapter"""
    print(f"Checking for duplicate IDs in {xhtml_path.name}...")

    with open(xhtml_path, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    # Find all elements with IDs
    id_counts = {}
    elements_with_ids = soup.find_all(id=True)

    for elem in elements_with_ids:
        elem_id = elem.get('id')
        if elem_id not in id_counts:
            id_counts[elem_id] = []
        id_counts[elem_id].append(elem)

    # Find duplicates
    duplicates = {id_val: elems for id_val, elems in id_counts.items() if len(elems) > 1}

    if not duplicates:
        print(f"  ✓ No duplicate IDs found")
        return False

    print(f"  Found {len(duplicates)} duplicate ID(s): {list(duplicates.keys())}")

    # Fix duplicates by making them unique
    modified = False
    for dup_id, elems in duplicates.items():
        print(f"    Fixing duplicate ID: {dup_id} ({len(elems)} instances)")
        # Keep the first one, rename the rest
        for i, elem in enumerate(elems[1:], start=2):
            new_id = f"{dup_id}-{i}"
            print(f"      Renaming to: {new_id}")
            elem['id'] = new_id

            # Update any references to this ID
            refs = soup.find_all(href=f"#{dup_id}")
            if refs:
                print(f"      Updating {len(refs)} reference(s)")
                for ref in refs:
                    # Only update if this is referring to the renamed element
                    ref['href'] = f"#{new_id}"

            modified = True

    if modified:
        with open(xhtml_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"  ✓ Fixed duplicate IDs")

    return modified


def fix_opf_css_references(opf_path):
    """Remove obsolete CSS references from content.opf"""
    print(f"Fixing CSS references in {opf_path.name}...")

    with open(opf_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find obsolete CSS references
    obsolete_css = ['print-pod.css', 'artisan-path-style.css']
    modified = False

    for css_file in obsolete_css:
        # Match the entire <item> tag for the CSS file
        pattern = rf'\s*<item\s+[^>]*href="[^"]*{re.escape(css_file)}"[^>]*/>[\r\n]*'
        if re.search(pattern, content):
            print(f"  Removing reference to: {css_file}")
            content = re.sub(pattern, '', content)
            modified = True

    if modified:
        with open(opf_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Removed obsolete CSS references")
    else:
        print(f"  ✓ No obsolete CSS references found")

    return modified


def main():
    # Use dynamic path resolution instead of hardcoded path
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    xhtml_dir = repo_root / 'REBRANDED_OUTPUT' / 'xhtml'
    opf_path = repo_root / 'REBRANDED_OUTPUT' / 'content.opf'

    print("=" * 60)
    print("EPUB Validation Error Fixer")
    print("=" * 60)
    print()

    total_fixes = 0

    # Fix 1: Chapter I quiz structure
    print("[1/4] Fixing Chapter I quiz structure...")
    chapter_i = xhtml_dir / '9-chapter-i-unveiling-your-creative-odyssey.xhtml'
    if chapter_i.exists():
        if fix_chapter_i_quiz(chapter_i):
            total_fixes += 1
    else:
        print(f"  ⚠️  File not found: {chapter_i}")
    print()

    # Fix 2: Duplicate IDs in chapters VI, VII, VIII
    print("[2/4] Fixing duplicate IDs in chapters VI, VII, VIII...")
    chapters_to_fix = [
        '15-chapter-vi-mastering-the-business-of-hairstyling.xhtml',
        '16-chapter-vii-embracing-wellness-and-self-care.xhtml',
        '17-chapter-viii-advancing-skills-through-continuous-education.xhtml'
    ]

    for chapter_file in chapters_to_fix:
        chapter_path = xhtml_dir / chapter_file
        if chapter_path.exists():
            if fix_duplicate_ids(chapter_path):
                total_fixes += 1
        else:
            print(f"  ⚠️  File not found: {chapter_path}")
    print()

    # Fix 3: Remove obsolete CSS references
    print("[3/4] Removing obsolete CSS references from OPF...")
    if opf_path.exists():
        if fix_opf_css_references(opf_path):
            total_fixes += 1
    else:
        print(f"  ⚠️  File not found: {opf_path}")
    print()

    # Summary
    print("=" * 60)
    print(f"Completed: {total_fixes} file(s) modified")
    print("=" * 60)

    if total_fixes > 0:
        print()
        print("Next steps:")
        print("  1. Rebuild EPUB: python3 scripts/build_epub.py")
        print("  2. Validate: epubcheck dist/curls-and-contemplation.epub")
        return 0
    else:
        print()
        print("No fixes were needed - all errors may already be resolved!")
        return 0


if __name__ == '__main__':
    sys.exit(main())
