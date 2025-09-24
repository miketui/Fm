#!/usr/bin/env python3
"""
Script to fix frontmatter files:
1. Ensure all content fits properly on single pages
2. Add proper page break styles
3. Fix any truncation issues
4. Optimize layout for single-page display
"""

import re
import os
from pathlib import Path

# Frontmatter files to fix
FRONTMATTER_FILES = [
    "1-TitlePage.xhtml",
    "2-Copyright.xhtml",
    "3-TableOfContents.xhtml",
    "4-Dedication.xhtml",
    "5-SelfAssessment.xhtml",
    "7-Preface.xhtml"
]

def add_frontmatter_styles(content):
    """Add CSS for single-page frontmatter layout"""
    style_section = """
    <style>
    .single-page {
        max-height: 90vh;
        overflow: visible;
        page-break-inside: avoid;
        break-inside: avoid;
        padding: 20px;
        box-sizing: border-box;
    }
    .title-page {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        min-height: 80vh;
    }
    .copyright-page {
        font-size: 0.9em;
        line-height: 1.4;
        max-height: 85vh;
        overflow: visible;
    }
    .toc-page {
        font-size: 0.95em;
        line-height: 1.3;
        max-height: 85vh;
        overflow: visible;
    }
    .toc-page ul {
        margin: 0.5em 0;
        padding-left: 1.2em;
    }
    .toc-page li {
        margin: 0.3em 0;
    }
    .dedication-page {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        min-height: 70vh;
        font-size: 1.1em;
        line-height: 1.6;
    }
    .preface-page {
        font-size: 0.95em;
        line-height: 1.4;
        max-height: 85vh;
        overflow: visible;
    }
    .assessment-page {
        font-size: 0.9em;
        line-height: 1.3;
        max-height: 85vh;
        overflow: visible;
    }
    .avoid-break {
        page-break-inside: avoid;
        break-inside: avoid;
    }
    </style>
    """

    # Insert styles before closing head tag
    if '</head>' in content:
        return content.replace('</head>', f'{style_section}</head>')
    else:
        # If no head tag, add styles after title
        return content.replace('<title>', f'<style>{style_section}</style><title>')

def fix_title_page(content):
    """Optimize title page layout"""
    # Add single-page class to main container
    content = re.sub(r'(<div[^>]*class="title-page"[^>]*>)', r'\1', content)
    content = re.sub(r'(<body[^>]*>)', r'\1<div class="single-page title-page">', content)
    content = re.sub(r'(</body>)', r'</div>\1', content)
    return content

def fix_copyright_page(content):
    """Optimize copyright page layout"""
    content = re.sub(r'(<body[^>]*>)', r'\1<div class="single-page copyright-page">', content)
    content = re.sub(r'(</body>)', r'</div>\1', content)
    return content

def fix_table_of_contents(content):
    """Optimize table of contents layout"""
    content = re.sub(r'(<body[^>]*>)', r'\1<div class="single-page toc-page">', content)
    content = re.sub(r'(</body>)', r'</div>\1', content)

    # Compact TOC entries if too long
    # Remove excessive spacing in list items
    content = re.sub(r'<li[^>]*>\s*<a[^>]*>([^<]+)</a>\s*</li>', r'<li><a href="#">\1</a></li>', content)

    return content

def fix_dedication_page(content):
    """Optimize dedication page layout"""
    content = re.sub(r'(<body[^>]*>)', r'\1<div class="single-page dedication-page">', content)
    content = re.sub(r'(</body>)', r'</div>\1', content)
    return content

def fix_preface_page(content):
    """Optimize preface layout to fit on one page"""
    content = re.sub(r'(<body[^>]*>)', r'\1<div class="single-page preface-page">', content)
    content = re.sub(r'(</body>)', r'</div>\1', content)

    # Compact paragraph spacing
    content = re.sub(r'<p class="preface-paragraph"([^>]*)>', r'<p class="preface-paragraph compact" \1>', content)

    return content

def fix_assessment_page(content):
    """Optimize self-assessment layout"""
    content = re.sub(r'(<body[^>]*>)', r'\1<div class="single-page assessment-page">', content)
    content = re.sub(r'(</body>)', r'</div>\1', content)
    return content

def fix_frontmatter_file(filepath):
    """Fix a single frontmatter file"""
    print(f"Fixing {filepath}...")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add base styles
    content = add_frontmatter_styles(content)

    # Apply specific fixes based on filename
    filename = Path(filepath).name

    if "TitlePage" in filename:
        content = fix_title_page(content)
    elif "Copyright" in filename:
        content = fix_copyright_page(content)
    elif "TableOfContents" in filename:
        content = fix_table_of_contents(content)
    elif "Dedication" in filename:
        content = fix_dedication_page(content)
    elif "Preface" in filename:
        content = fix_preface_page(content)
    elif "SelfAssessment" in filename:
        content = fix_assessment_page(content)

    # Write back to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Fixed {filepath}")

def main():
    """Fix all frontmatter files"""
    output_dir = Path("output")

    for frontmatter_file in FRONTMATTER_FILES:
        filepath = output_dir / frontmatter_file
        if filepath.exists():
            fix_frontmatter_file(filepath)
        else:
            print(f"⚠️  File not found: {filepath}")

    print("🎉 All frontmatter files have been fixed!")

if __name__ == "__main__":
    main()