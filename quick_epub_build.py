#!/usr/bin/env python3
import shutil
import os
from pathlib import Path
import zipfile

base = Path('/workspaces/Fm')
rebranded = base / 'REBRANDED_OUTPUT'
epub_build = base / 'epub_build'
oebps = epub_build / 'OEBPS'

print("Step 1: Copying files from REBRANDED_OUTPUT to epub_build...")

# Copy xhtml
src, dst = rebranded / 'xhtml', oebps / 'text'
if src.exists():
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    print(f"✓ Copied {len(list(src.glob('*')))} XHTML files")

# Copy styles
src, dst = rebranded / 'styles', oebps / 'styles'
if src.exists() and not dst.exists():
    shutil.copytree(src, dst)
    print("✓ Copied styles")
elif src.exists():
    for f in src.glob('*'):
        shutil.copy2(f, dst / f.name)
    print("✓ Updated styles")

# Copy images  
src, dst = rebranded / 'images', oebps / 'images'
if src.exists() and not dst.exists():
    shutil.copytree(src, dst)
    print("✓ Copied images")
elif src.exists():
    for f in src.glob('*'):
        if f.is_file():
            shutil.copy2(f, dst / f.name)
    print("✓ Updated images")

# Copy fonts
src, dst = rebranded / 'fonts', oebps / 'fonts'
if src.exists() and not dst.exists():
    shutil.copytree(src, dst)
    print("✓ Copied fonts")
elif src.exists():
    for f in src.glob('*'):
        if f.is_file():
            shutil.copy2(f, dst / f.name)
    print("✓ Updated fonts")

# Copy content.opf
src = rebranded / 'content.opf'
if src.exists():
    shutil.copy2(src, oebps / 'content.opf')
    print("✓ Copied content.opf")

# Copy mimetype
src = rebranded / 'mimetype'
if src.exists():
    shutil.copy2(src, epub_build / 'mimetype')
    print("✓ Copied mimetype")

# Copy META-INF
src = rebranded / 'META-INF'
if src.exists():
    dst = epub_build / 'META-INF'
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    print("✓ Copied META-INF")

print("\nStep 2: Validating EPUB structure...")
required = [
    epub_build / 'mimetype',
    epub_build / 'META-INF' / 'container.xml',
    oebps / 'content.opf',
    oebps / 'text',
]

for item in required:
    if item.exists():
        print(f"✓ {item.relative_to(base)}")
    else:
        print(f"✗ MISSING: {item.relative_to(base)}")

print("\nStep 3: Building EPUB file...")
dist = epub_build / 'dist'
dist.mkdir(exist_ok=True)
epub_file = dist / 'The-Artisans-Path.epub'

with zipfile.ZipFile(epub_file, 'w', zipfile.ZIP_DEFLATED) as zf:
    # Add mimetype first (uncompressed)
    zf.write(epub_build / 'mimetype', 'mimetype', compress_type=zipfile.ZIP_STORED)
    
    # Add everything else
    for root, dirs, files in os.walk(epub_build):
        for file in files:
            file_path = Path(root) / file
            arcname = file_path.relative_to(epub_build)
            if str(arcname) != 'mimetype' and 'dist' not in str(arcname):
                zf.write(file_path, arcname)

size_mb = epub_file.stat().st_size / (1024 * 1024)
print(f"✓ EPUB created: {epub_file.relative_to(base)} ({size_mb:.2f} MB)")

print("\n✓ EPUB BUILD COMPLETE!")
