#!/usr/bin/env python3
import os
import shutil
import zipfile
import subprocess
import re
from pathlib import Path
import xml.etree.ElementTree as ET

# Configuration
BASE_DIR = Path('REBRANDED_OUTPUT')
DIST_DIR = BASE_DIR / 'dist'
OPF_PATH = BASE_DIR / 'content.opf'
EPUB_NAME = 'The-Artisans-Path-Final.epub'
PDF_NAME = 'The-Artisans-Path-Final.pdf'

# Namespace map for parsing OPF
NS = {
    'opf': 'http://www.idpf.org/2007/opf',
    'dc': 'http://purl.org/dc/elements/1.1/'
}

def parse_opf():
    print(f"Parsing {OPF_PATH}...")
    tree = ET.parse(OPF_PATH)
    root = tree.getroot()
    
    manifest = {}
    for item in root.findall('.//opf:manifest/opf:item', NS):
        item_id = item.get('id')
        href = item.get('href')
        manifest[item_id] = href
        
    spine = []
    for itemref in root.findall('.//opf:spine/opf:itemref', NS):
        idref = itemref.get('idref')
        if idref in manifest:
            spine.append(manifest[idref])
        else:
            print(f"Warning: Spine item {idref} not found in manifest")
            
    return spine

def build_epub():
    print(f"Building EPUB: {EPUB_NAME}...")
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    epub_path = DIST_DIR / EPUB_NAME
    
    with zipfile.ZipFile(epub_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        # 1. Add mimetype (STORED, not compressed)
        mimetype_path = BASE_DIR / 'mimetype'
        if mimetype_path.exists():
            zf.write(mimetype_path, 'mimetype', compress_type=zipfile.ZIP_STORED)
        else:
            print("Error: mimetype file missing!")
            return

        # 2. Add Container and OPF
        zf.write(BASE_DIR / 'META-INF/container.xml', 'META-INF/container.xml')
        zf.write(OPF_PATH, 'content.opf')

        # 3. Add Assets (xhtml, images, fonts, styles)
        # We walk specific directories to avoid adding junk
        dirs_to_include = ['xhtml', 'images', 'fonts', 'styles']
        
        for dir_name in dirs_to_include:
            dir_path = BASE_DIR / dir_name
            if not dir_path.exists():
                print(f"Warning: Directory {dir_name} not found")
                continue
                
            for root, _, files in os.walk(dir_path):
                for file in files:
                    # Skip hidden files or backups
                    if file.startswith('.') or file.endswith('.backup'):
                        continue
                        
                    full_path = Path(root) / file
                    arcname = full_path.relative_to(BASE_DIR)
                    zf.write(full_path, arcname)
                    
    print(f"✅ EPUB created at: {epub_path}")

def build_pdf(spine_files):
    print(f"Building PDF: {PDF_NAME}...")
    
    # Check for wkhtmltopdf
    if shutil.which('wkhtmltopdf') is None:
        print("❌ wkhtmltopdf not found. Skipping PDF generation.")
        return

    pdf_path = DIST_DIR / PDF_NAME
    combined_html_path = BASE_DIR / 'xhtml' / 'combined_for_pdf.xhtml'
    
    # 1. Concatenate content
    combined_content = []
    head_content = ""
    
    # Standard header if we can't parse the first file
    default_head = '''<head>
    <meta charset="UTF-8" />
    <title>The Artisan's Path</title>
    <link rel="stylesheet" type="text/css" href="styles/fonts.css" />
    <link rel="stylesheet" type="text/css" href="styles/style.css" />
    <link rel="stylesheet" type="text/css" href="styles/print.css" />
    </head>'''
    
    first_file = True
    for relative_path in spine_files:
        full_path = BASE_DIR / relative_path
        if not full_path.exists():
            print(f"Warning: File not found for PDF: {full_path}")
            continue
            
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Parse HTML (simple string manipulation to avoid namespace issues with xml.etree)
            # We want what's inside <body ...> ... </body>
            # And we want the head from the first file
            
            if first_file:
                # Extract head
                m_head = re.search(r'<head>(.*?)</head>', content, re.DOTALL | re.IGNORECASE)
                if m_head:
                    head_content = m_head.group(1)
                    # Replace stylesheets to use only print.css for PDF generation
                    # Removing style.css and fonts.css to avoid complex CSS issues with wkhtmltopdf
                    head_content = re.sub(r'<link[^>]*href="[^"]*style\.css"[^>]*>', '', head_content)
                    head_content = re.sub(r'<link[^>]*href="[^"]*fonts\.css"[^>]*>', '', head_content)
                    # Ensure print.css is active for all media (remove media="print")
                    head_content = re.sub(r'(<link[^>]*href="[^"]*print\.css")[^>]*>', r'\1 />', head_content)
                    # We might need fonts.css if print.css doesn't include font faces?
                    # print.css has @font-face declarations inside it (checked via read_file).
                else:
                    head_content = default_head
                first_file = False
                
            # Extract body content
            m_body = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL | re.IGNORECASE)
            if m_body:
                body_inner = m_body.group(1)
                # Wrap in a div that enforces page break if needed, though most chapters start with one
                # We'll add a page break before each file's content just in case, except the first
                div_wrapper = f'<div class="chapter-content" style="page-break-before: always;">\n{body_inner}\n</div>'
                combined_content.append(div_wrapper)
                
        except Exception as e:
            print(f"Error processing {full_path}: {e}")

    # Create the combined HTML file
    final_html = f'''<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en">
<head>
{head_content}
</head>
<body class="combined-pdf">
{''.join(combined_content)}
</body>
</html>'''

    with open(combined_html_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
        
    print(f"Created temporary combined file: {combined_html_path}")

    # 2. Run wkhtmltopdf
    # Removing unsupported flags: --print-media-type, --footer-*
    cmd = [
        'wkhtmltopdf',
        '--page-size', 'A4',
        '--margin-top', '20mm',
        '--margin-bottom', '20mm',
        '--margin-left', '20mm',
        '--margin-right', '20mm',
        '--enable-local-file-access',
        '--title', "The Artisan's Path",
        str(combined_html_path),
        str(pdf_path)
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"✅ PDF created at: {pdf_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ PDF generation failed: {e}")
    finally:
        # Cleanup
        # if combined_html_path.exists():
        #     combined_html_path.unlink()
        pass

def main():
    if not BASE_DIR.exists():
        print(f"Error: Base directory {BASE_DIR} not found.")
        return

    spine_files = parse_opf()
    
    build_epub()
    build_pdf(spine_files)

if __name__ == '__main__':
    main()
