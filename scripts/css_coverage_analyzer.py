#!/usr/bin/env python3
"""CSS coverage analysis for EPUB XHTML files.

Scans all XHTML files for class/ID usage and compares against CSS rules
to identify unused selectors, missing definitions, and opportunities for optimization.
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from typing import Dict, List, Set

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("❌ Missing dependency. Install with: pip install beautifulsoup4 lxml")
    sys.exit(1)


def load_audit_json(path: str) -> Dict:
    """Load visual audit JSON."""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def extract_selectors_from_xhtml(file_path: str) -> Set[str]:
    """Extract all class and ID selectors used in an XHTML file."""
    selectors = set()

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'xml')

        # Find all elements with class attribute
        for elem in soup.find_all(class_=True):
            classes = elem.get('class')
            if isinstance(classes, list):
                for cls in classes:
                    selectors.add(f'.{cls}')
            elif isinstance(classes, str):
                for cls in classes.split():
                    selectors.add(f'.{cls}')

        # Find all elements with id attribute
        for elem in soup.find_all(id=True):
            elem_id = elem.get('id')
            if elem_id:
                selectors.add(f'#{elem_id}')

    except Exception as e:
        print(f"  ⚠️  Error reading {file_path}: {e}")

    return selectors


def parse_css_selectors(css_path: str) -> Set[str]:
    """Extract selectors defined in a CSS file (simplified parsing)."""
    selectors = set()

    try:
        with open(css_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove comments
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)

        # Find selectors (simplified - matches .class and #id patterns)
        class_matches = re.findall(r'\.([\w-]+)', content)
        id_matches = re.findall(r'#([\w-]+)', content)

        selectors.update(f'.{cls}' for cls in class_matches)
        selectors.update(f'#{id_match}' for id_match in id_matches)

    except Exception as e:
        print(f"  ⚠️  Error reading CSS {css_path}: {e}")

    return selectors


def analyze_coverage(
    xhtml_selectors: Set[str],
    css_selectors: Set[str]
) -> Dict:
    """Compare XHTML usage against CSS definitions."""
    used = xhtml_selectors & css_selectors
    unused_in_css = css_selectors - xhtml_selectors
    missing_in_css = xhtml_selectors - css_selectors

    return {
        'used': sorted(list(used)),
        'unused_in_css': sorted(list(unused_in_css)),
        'missing_in_css': sorted(list(missing_in_css)),
        'stats': {
            'total_css_selectors': len(css_selectors),
            'total_xhtml_selectors': len(xhtml_selectors),
            'used_count': len(used),
            'unused_count': len(unused_in_css),
            'missing_count': len(missing_in_css),
            'coverage_pct': round(len(used) / len(css_selectors) * 100, 1) if css_selectors else 0
        }
    }


def generate_markdown_report(analysis: Dict, output_path: str) -> None:
    """Generate human-readable CSS coverage report."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    stats = analysis['stats']

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# CSS Coverage Analysis\n\n")

        f.write("## Summary\n\n")
        f.write(f"- **Total CSS selectors**: {stats['total_css_selectors']}\n")
        f.write(f"- **Used selectors**: {stats['used_count']} ({stats['coverage_pct']}%)\n")
        f.write(f"- **Unused selectors**: {stats['unused_count']}\n")
        f.write(f"- **Missing definitions**: {stats['missing_count']}\n\n")

        # Unused selectors
        f.write("## Unused Selectors in CSS\n\n")
        f.write("These selectors are defined in CSS but not used in any XHTML file:\n\n")

        if analysis['unused_in_css']:
            for sel in analysis['unused_in_css'][:50]:  # Show first 50
                f.write(f"- `{sel}`\n")
            if len(analysis['unused_in_css']) > 50:
                f.write(f"\n... and {len(analysis['unused_in_css']) - 50} more\n")
        else:
            f.write("_(None - all CSS selectors are used!)_\n")

        f.write("\n")

        # Missing definitions
        f.write("## Missing Definitions in CSS\n\n")
        f.write("These selectors are used in XHTML but not defined in CSS:\n\n")

        if analysis['missing_in_css']:
            for sel in analysis['missing_in_css']:
                f.write(f"- `{sel}`\n")
        else:
            f.write("_(None - all used selectors are defined!)_\n")

        f.write("\n")

        # Recommendations
        f.write("## Recommendations\n\n")

        if stats['unused_count'] > 0:
            savings_pct = round(stats['unused_count'] / stats['total_css_selectors'] * 100, 1)
            f.write(f"1. **Remove unused selectors**: {stats['unused_count']} selectors ({savings_pct}% of total) can potentially be removed to reduce file size.\n\n")

        if stats['missing_count'] > 0:
            f.write(f"2. **Add missing definitions**: {stats['missing_count']} selectors are used but not styled. Add CSS rules for these.\n\n")

        if stats['coverage_pct'] > 90:
            f.write("✅ **Excellent CSS coverage!** Over 90% of defined styles are actively used.\n")
        elif stats['coverage_pct'] > 75:
            f.write("✅ **Good CSS coverage.** Most defined styles are in use.\n")
        else:
            f.write("⚠️ **Consider CSS optimization.** Less than 75% of defined styles are used.\n")


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(description='CSS Coverage Analysis')
    parser.add_argument('--root', required=True, help='Root directory (REBRANDED_OUTPUT)')
    parser.add_argument('--targets', required=True, help='Visual audit JSON')
    parser.add_argument('--out', required=True, help='Output markdown report path')

    args = parser.parse_args()

    print("=" * 60)
    print("CSS Coverage Analysis - Starting")
    print("=" * 60)

    audit_data = load_audit_json(args.targets)

    # Collect all selectors from XHTML files
    all_xhtml_selectors = set()

    for file_entry in audit_data['files']:
        xhtml_path = file_entry['file']
        selectors = extract_selectors_from_xhtml(xhtml_path)
        all_xhtml_selectors.update(selectors)

    print(f"Found {len(all_xhtml_selectors)} unique selectors in XHTML files")

    # Parse CSS files
    css_files = [
        os.path.join(args.root, 'xhtml/styles/style.css'),
        os.path.join(args.root, 'xhtml/styles/print-pod.css')
    ]

    all_css_selectors = set()

    for css_file in css_files:
        if os.path.exists(css_file):
            selectors = parse_css_selectors(css_file)
            all_css_selectors.update(selectors)
            print(f"Found {len(selectors)} selectors in {os.path.basename(css_file)}")

    print(f"Total CSS selectors: {len(all_css_selectors)}")

    # Analyze coverage
    analysis = analyze_coverage(all_xhtml_selectors, all_css_selectors)

    # Save JSON
    json_path = args.out.replace('.md', '.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(analysis, f, indent=2)

    print(f"✅ Saved JSON: {json_path}")

    # Generate markdown report
    generate_markdown_report(analysis, args.out)
    print(f"✅ Saved report: {args.out}")

    print("\n" + "=" * 60)
    print(f"Coverage: {analysis['stats']['coverage_pct']}% - Unused: {analysis['stats']['unused_count']} - Missing: {analysis['stats']['missing_count']}")
    print("=" * 60)

    return 0


if __name__ == '__main__':
    sys.exit(main())
