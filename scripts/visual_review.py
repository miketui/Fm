#!/usr/bin/env python3
"""Visual review and screenshot capture for EPUB XHTML files.

Uses Playwright headless Chromium to render XHTML files at multiple viewports,
capture screenshots, analyze computed styles, and detect layout/accessibility issues.
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Any

try:
    from playwright.sync_api import sync_playwright
    from bs4 import BeautifulSoup
except ImportError:
    print("❌ Missing dependencies. Install with:")
    print("   pip install playwright beautifulsoup4 lxml")
    print("   python -m playwright install chromium")
    sys.exit(1)


VIEWPORTS = [
    {'width': 768, 'height': 1024, 'name': '768x1024'},
    {'width': 1080, 'height': 1440, 'name': '1080x1440'}
]


def load_audit_json(path: str) -> Dict:
    """Load existing visual audit JSON."""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_audit_json(data: Dict, path: str) -> None:
    """Save updated visual audit JSON."""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def analyze_xhtml_content(file_path: str) -> Dict[str, Any]:
    """Analyze XHTML file for structure and potential issues."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'xml')
    issues = []

    # Check heading hierarchy
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    if headings:
        prev_level = 0
        for h in headings:
            level = int(h.name[1])
            if prev_level > 0 and level > prev_level + 1:
                issues.append({
                    'severity': 'warning',
                    'type': 'heading_hierarchy',
                    'description': f'Heading skip: {prev_level} to {level}',
                    'node_excerpt': str(h)[:100]
                })
            prev_level = level

    # Check for images without alt
    for img in soup.find_all('img'):
        if not img.get('alt'):
            issues.append({
                'severity': 'error',
                'type': 'missing_alt',
                'description': 'Image missing alt attribute',
                'node_excerpt': str(img)[:100]
            })

    # Check for worksheets/interactive content
    has_worksheets = bool(
        soup.find(string=re.compile(r'worksheet|activity|exercise', re.I)) or
        soup.find(class_=re.compile(r'worksheet|activity|exercise', re.I))
    )

    # Check for complex layouts
    has_complex = bool(
        soup.find_all(['table', 'figure']) or
        soup.find(class_=re.compile(r'multi-column|complex|grid', re.I))
    )

    return {
        'issues': issues,
        'has_worksheets': has_worksheets,
        'has_complex_layout': has_complex,
        'heading_count': len(headings),
        'image_count': len(soup.find_all('img'))
    }


def capture_screenshots(
    page: Any,
    file_path: str,
    basename: str,
    screenshots_dir: str,
    viewport: Dict,
    has_worksheets: bool,
    has_complex: bool
) -> List[Dict]:
    """Capture screenshots for a single file at one viewport."""
    screenshots = []
    vp_name = viewport['name']
    file_url = f"file://{os.path.abspath(file_path)}"

    # Create output directory
    output_dir = os.path.join(screenshots_dir, basename)
    os.makedirs(output_dir, exist_ok=True)

    try:
        # Navigate and wait for load
        page.goto(file_url, wait_until='networkidle', timeout=30000)
        page.wait_for_load_state('load')

        # Title/top screenshot
        title_path = os.path.join(output_dir, f'title_{vp_name}.png')
        page.screenshot(path=title_path, full_page=False)
        screenshots.append({
            'path': title_path,
            'type': 'title',
            'viewport': vp_name
        })

        # Worksheet screenshot if applicable
        if has_worksheets:
            worksheet_path = os.path.join(output_dir, f'worksheets_{vp_name}_p1.png')
            page.screenshot(path=worksheet_path, full_page=True)
            screenshots.append({
                'path': worksheet_path,
                'type': 'worksheets',
                'viewport': vp_name
            })

        # Complex layout screenshot if applicable
        if has_complex:
            complex_path = os.path.join(output_dir, f'complex_{vp_name}_p1.png')
            page.screenshot(path=complex_path, full_page=True)
            screenshots.append({
                'path': complex_path,
                'type': 'complex',
                'viewport': vp_name
            })

    except Exception as e:
        print(f"  ⚠️  Screenshot error: {e}")

    return screenshots


def get_computed_styles(page: Any) -> Dict:
    """Extract computed style samples from rendered page."""
    try:
        styles = page.evaluate("""() => {
            const samples = {};
            const selectors = ['h1', 'h2', 'h3', 'p', 'li', 'img'];

            selectors.forEach(sel => {
                const el = document.querySelector(sel);
                if (el) {
                    const computed = window.getComputedStyle(el);
                    samples[sel] = {
                        fontFamily: computed.fontFamily,
                        fontSize: computed.fontSize,
                        lineHeight: computed.lineHeight,
                        color: computed.color,
                        marginTop: computed.marginTop,
                        marginBottom: computed.marginBottom
                    };
                }
            });

            return samples;
        }""")
        return styles
    except Exception as e:
        print(f"  ⚠️  Style extraction error: {e}")
        return {}


def process_file(
    file_entry: Dict,
    root_dir: str,
    screenshots_dir: str,
    browser: Any
) -> None:
    """Process a single XHTML file with all viewports."""
    file_path = file_entry['file']
    basename = file_entry['basename']

    print(f"Processing: {basename}")

    # Analyze content
    analysis = analyze_xhtml_content(file_path)
    file_entry['issues'] = analysis['issues']

    # Create browser page
    page = browser.new_page()

    all_screenshots = []

    # Process each viewport
    for viewport in VIEWPORTS:
        page.set_viewport_size({
            'width': viewport['width'],
            'height': viewport['height']
        })

        screenshots = capture_screenshots(
            page,
            file_path,
            basename,
            screenshots_dir,
            viewport,
            analysis['has_worksheets'],
            analysis['has_complex_layout']
        )
        all_screenshots.extend(screenshots)

    # Get computed styles (using first viewport)
    page.set_viewport_size({
        'width': VIEWPORTS[0]['width'],
        'height': VIEWPORTS[0]['height']
    })
    file_url = f"file://{os.path.abspath(file_path)}"
    page.goto(file_url, wait_until='networkidle', timeout=30000)
    file_entry['computed_style_samples'] = get_computed_styles(page)

    page.close()

    file_entry['screenshots'] = all_screenshots

    # Determine verdict
    critical_issues = [i for i in file_entry['issues'] if i['severity'] == 'error']
    file_entry['verdict'] = 'FAIL' if critical_issues else 'PASS'


def generate_markdown_summary(data: Dict, output_path: str) -> None:
    """Generate markdown summary report."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# EPUB Visual QA Audit Results\n\n")
        f.write(f"**Total files**: {data['total']}\n")

        pass_count = sum(1 for f in data['files'] if f.get('verdict') == 'PASS')
        fail_count = data['total'] - pass_count

        f.write(f"**PASS**: {pass_count}\n")
        f.write(f"**FAIL**: {fail_count}\n\n")

        f.write("## Summary Table\n\n")
        f.write("| File | Verdict | Issues | Screenshots |\n")
        f.write("|------|---------|--------|-------------|\n")

        for entry in data['files']:
            basename = entry['basename']
            verdict = entry.get('verdict', 'UNKNOWN')
            issue_count = len(entry.get('issues', []))
            screenshot_count = len(entry.get('screenshots', []))

            f.write(f"| {basename} | {verdict} | {issue_count} | {screenshot_count} |\n")


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(description='EPUB Visual QA Review')
    parser.add_argument('--root', required=True, help='Root directory (REBRANDED_OUTPUT)')
    parser.add_argument('--targets', required=True, help='Visual audit JSON file')
    parser.add_argument('--screenshots-dir', required=True, help='Output directory for screenshots')
    parser.add_argument('--gallery', help='Output path for gallery HTML (optional)')

    args = parser.parse_args()

    print("=" * 60)
    print("EPUB Visual QA Review - Starting")
    print("=" * 60)

    # Load targets
    audit_data = load_audit_json(args.targets)
    total = audit_data['total']

    print(f"Loaded {total} target files from {args.targets}")

    # Launch browser
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # Process each file
        for i, file_entry in enumerate(audit_data['files'], 1):
            print(f"[{i}/{total}] ", end='')
            process_file(file_entry, args.root, args.screenshots_dir, browser)

        browser.close()

    # Save updated JSON
    save_audit_json(audit_data, args.targets)
    print(f"\n✅ Updated audit JSON: {args.targets}")

    # Generate markdown summary
    md_path = args.targets.replace('.json', '.md')
    generate_markdown_summary(audit_data, md_path)
    print(f"✅ Generated summary: {md_path}")

    # Generate gallery if requested
    if args.gallery:
        generate_gallery_html(audit_data, args.gallery, args.screenshots_dir)
        print(f"✅ Generated gallery: {args.gallery}")

    print("\n" + "=" * 60)
    print("Visual QA Review Complete")
    print("=" * 60)

    return 0


def generate_gallery_html(data: Dict, output_path: str, screenshots_dir: str) -> None:
    """Generate interactive screenshot gallery HTML."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EPUB Visual QA Gallery</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background: #f5f5f5; padding: 2rem; }
        h1 { margin-bottom: 2rem; color: #333; }
        .file-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 2rem; }
        .file-card { background: white; border-radius: 8px; padding: 1.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
        .file-card h2 { font-size: 1.1rem; margin-bottom: 1rem; color: #555; }
        .screenshot-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; }
        .screenshot { width: 100%; border: 1px solid #ddd; border-radius: 4px; cursor: pointer; transition: transform 0.2s; }
        .screenshot:hover { transform: scale(1.05); }
        .verdict { display: inline-block; padding: 0.25rem 0.75rem; border-radius: 12px; font-size: 0.85rem; font-weight: 600; margin-bottom: 0.5rem; }
        .verdict-PASS { background: #d4edda; color: #155724; }
        .verdict-FAIL { background: #f8d7da; color: #721c24; }
        .modal { display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.9); z-index: 1000; align-items: center; justify-content: center; }
        .modal.active { display: flex; }
        .modal img { max-width: 90%; max-height: 90%; }
        .close { position: absolute; top: 1rem; right: 1rem; color: white; font-size: 2rem; cursor: pointer; }
    </style>
</head>
<body>
    <h1>EPUB Visual QA Gallery - 44 Chapters</h1>
    <div class="file-grid">
"""

    for entry in data['files']:
        basename = entry['basename']
        verdict = entry.get('verdict', 'UNKNOWN')
        screenshots = entry.get('screenshots', [])

        html += f'<div class="file-card">'
        html += f'<span class="verdict verdict-{verdict}">{verdict}</span>'
        html += f'<h2>{basename}</h2>'
        html += f'<div class="screenshot-grid">'

        for screenshot in screenshots[:4]:  # Show first 4 screenshots
            rel_path = os.path.relpath(screenshot['path'], os.path.dirname(output_path))
            html += f'<img src="{rel_path}" alt="{screenshot["type"]}" class="screenshot" onclick="showModal(this)">'

        html += '</div></div>'

    html += """
    </div>
    <div class="modal" id="modal" onclick="hideModal()">
        <span class="close">&times;</span>
        <img id="modal-img" src="">
    </div>
    <script>
        function showModal(img) {
            document.getElementById('modal').classList.add('active');
            document.getElementById('modal-img').src = img.src;
        }
        function hideModal() {
            document.getElementById('modal').classList.remove('active');
        }
    </script>
</body>
</html>
"""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)


if __name__ == '__main__':
    sys.exit(main())
