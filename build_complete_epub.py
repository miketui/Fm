#!/usr/bin/env python3
import os
import shutil
import zipfile
import re
from pathlib import Path
from datetime import datetime

# Configuration
SOURCE_BASE = Path('/root/repo/REBRANDED-output')
BUILD_DIR = Path('/root/repo/epub_build')
DIST_DIR = Path('/root/repo/dist')
OUTPUT_FILENAME = 'curls-and-contemplation-rebranded.epub'

# Mappings (Source -> Destination relative to OEBPS)
DIRS_TO_COPY = {
    'xhtml': 'text',
    'styles': 'styles',
    'images': 'images',
    'fonts': 'fonts'
}

def clean_build_dir():
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir(parents=True)
    (BUILD_DIR / 'META-INF').mkdir()
    (BUILD_DIR / 'OEBPS').mkdir()
    
    # Create subdirectories in OEBPS
    for dest in DIRS_TO_COPY.values():
        (BUILD_DIR / 'OEBPS' / dest).mkdir(exist_ok=True)

def create_mimetype():
    with open(BUILD_DIR / 'mimetype', 'w', encoding='utf-8') as f:
        f.write('application/epub+zip')

def create_container_xml():
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
    <rootfiles>
        <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
    </rootfiles>
</container>'''
    with open(BUILD_DIR / 'META-INF' / 'container.xml', 'w', encoding='utf-8') as f:
        f.write(xml)

def copy_assets():
    print("Copying assets...")
    for src_name, dest_name in DIRS_TO_COPY.items():
        src_path = SOURCE_BASE / src_name
        dest_path = BUILD_DIR / 'OEBPS' / dest_name
        
        if not src_path.exists():
            print(f"Warning: Source directory {src_path} does not exist!")
            continue
            
        for item in src_path.glob('*'):
            if item.is_file():
                shutil.copy2(item, dest_path / item.name)

def get_file_number(filename):
    match = re.match(r'^(\d+)', filename)
    if match:
        return int(match.group(1))
    return 9999 # Put unnumbered files at the end

def generate_opf():
    print("Generating content.opf...")
    
    # scan for files
    xhtml_dir = BUILD_DIR / 'OEBPS' / 'text'
    all_xhtml = sorted([f.name for f in xhtml_dir.glob('*.xhtml')])
    
    # Separate quotes and main files
    quote_files = set()
    main_files = []
    
    for f in all_xhtml:
        if '-quote.xhtml' in f:
            quote_files.add(f)
        else:
            main_files.append(f)
            
    # Sort main files by number
    main_files.sort(key=get_file_number)
    
    # Build Manifest and Spine
    manifest_items = []
    spine_refs = []
    
    # Add assets to manifest
    for dest_name in ['styles', 'images', 'fonts']:
        dir_path = BUILD_DIR / 'OEBPS' / dest_name
        media_type_map = {
            'css': 'text/css',
            'jpg': 'image/jpeg',
            'jpeg': 'image/jpeg',
            'png': 'image/png',
            'svg': 'image/svg+xml',
            'woff': 'font/woff',
            'woff2': 'font/woff2',
            'ttf': 'font/ttf'
        }
        
        for f in dir_path.glob('*'):
            ext = f.suffix.lower()[1:]
            media_type = media_type_map.get(ext, 'application/octet-stream')
            item_id = f"{dest_name}_{f.stem}"
            # Sanitize ID
            item_id = re.sub(r'[^a-zA-Z0-9_-]', '_', item_id)
            
            manifest_items.append(f'<item id="{item_id}" href="{dest_name}/{f.name}" media-type="{media_type}"/>')

    # Add XHTML to manifest and build spine
    # Special handling for nav.xhtml
    for filename in main_files:
        if filename == 'nav.xhtml':
            item_id = 'nav'
            props = ' properties="nav"'
        else:
            item_id = f"text_{get_file_number(filename)}_{filename.split('.')[0]}"
            item_id = re.sub(r'[^a-zA-Z0-9_-]', '_', item_id)
            props = ''
            
        manifest_items.append(f'<item id="{item_id}" href="text/{filename}" media-type="application/xhtml+xml"{props}/>')
        
        # Add to spine (except nav usually, but EPUB3 allows it. Usually nav is just manifest unless it's also a content page)
        # If nav.xhtml is the TOC page, adding it to spine is fine.
        spine_refs.append(f'<itemref idref="{item_id}"/>')
        
        # Check for corresponding quote
        # Quote filename logic: [main_stem]-quote.xhtml
        main_stem = Path(filename).stem
        quote_filename = f"{main_stem}-quote.xhtml"
        
        if quote_filename in quote_files:
            quote_id = f"{item_id}_quote"
            manifest_items.append(f'<item id="{quote_id}" href="text/{quote_filename}" media-type="application/xhtml+xml"/>')
            spine_refs.append(f'<itemref idref="{quote_id}"/>')
            quote_files.remove(quote_filename)

    # Any remaining quote files (orphan quotes?)
    for q in quote_files:
        print(f"Warning: Orphan quote file found: {q}")
        q_id = f"quote_{q.replace('.', '_')}"
        manifest_items.append(f'<item id="{q_id}" href="text/{q}" media-type="application/xhtml+xml"/>')
        spine_refs.append(f'<itemref idref="{q_id}"/>')

    # Construct OPF Content
    opf_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="BookId">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="BookId">urn:uuid:9fa5e2ef-5fd8-4f5b-9077-0b9e856cda3d</dc:identifier>
    <dc:title>Curls &amp; Contemplation</dc:title>
    <dc:language>en</dc:language>
    <meta property="dcterms:modified">{datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}</meta>
  </metadata>
  <manifest>
    {chr(10).join(manifest_items)}
  </manifest>
  <spine>
    {chr(10).join(spine_refs)}
  </spine>
</package>'''

    with open(BUILD_DIR / 'OEBPS' / 'content.opf', 'w', encoding='utf-8') as f:
        f.write(opf_content)

def zip_epub():
    print(f"Zipping to {OUTPUT_FILENAME}...")
    DIST_DIR.mkdir(exist_ok=True)
    output_path = DIST_DIR / OUTPUT_FILENAME
    
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as epub:
        # Write mimetype uncompressed
        epub.write(BUILD_DIR / 'mimetype', 'mimetype', compress_type=zipfile.ZIP_STORED)
        
        # Write everything else
        for root, dirs, files in os.walk(BUILD_DIR):
            for file in files:
                if file == 'mimetype': continue
                file_path = Path(root) / file
                arcname = file_path.relative_to(BUILD_DIR)
                epub.write(file_path, arcname)
                
    print(f"✅ EPUB Created: {output_path}")

def main():
    clean_build_dir()
    create_mimetype()
    create_container_xml()
    copy_assets()
    generate_opf()
    zip_epub()

if __name__ == '__main__':
    main()
