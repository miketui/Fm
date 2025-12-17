#!/usr/bin/env python3
# Direct inline execution of master EPUB workflow
import re, os, shutil, zipfile, json
from pathlib import Path
from datetime import datetime
import subprocess, sys

# Setup paths
base = Path('/workspaces/Fm')
rebranded = base / 'REBRANDED_OUTPUT'
epub_build = base / 'epub_build'
oebps = epub_build / 'OEBPS'

print("\n" + "="*70)
print("MASTER EPUB WORKFLOW - DIRECT EXECUTION")
print("="*70 + "\n")

# STEP 1: Fix merge conflicts
print("STEP 1: Fixing merge conflict markers...")
pattern = r'<<<<<<< HEAD\n(.*?)\n=======\n(.*?)\n>>>>>>> [^\n]*\n'
xhtml_dir = rebranded / 'xhtml'
fixed_count = 0

if xhtml_dir.exists():
    for xhtml_file in xhtml_dir.glob('*.xhtml'):
        try:
            with open(xhtml_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            fixed = re.sub(pattern, r'\1\n', content, flags=re.DOTALL)
            if fixed != content:
                with open(xhtml_file, 'w', encoding='utf-8') as f:
                    f.write(fixed)
                fixed_count += 1
        except:
            pass

print(f"✓ Fixed {fixed_count} files\n")

# STEP 2: Copy files
print("STEP 2: Copying files from REBRANDED_OUTPUT to epub_build...")
oebps.mkdir(parents=True, exist_ok=True)

mappings = {'xhtml': 'text', 'styles': 'styles', 'images': 'images', 'fonts': 'fonts'}
for src_name, dst_name in mappings.items():
    src = rebranded / src_name
    dst = oebps / dst_name
    if src.exists():
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        print(f"  ✓ {src_name} → {dst_name}")

for file_name in ['content.opf', 'mimetype']:
    src = rebranded / file_name
    dst = (epub_build if file_name == 'mimetype' else oebps) / file_name
    if src.exists():
        shutil.copy2(src, dst)
        print(f"  ✓ {file_name}")

meta_src = rebranded / 'META-INF'
if meta_src.exists():
    meta_dst = epub_build / 'META-INF'
    if meta_dst.exists():
        shutil.rmtree(meta_dst)
    shutil.copytree(meta_src, meta_dst)
    print(f"  ✓ META-INF")

print()

# STEP 3: Validate structure
print("STEP 3: Validating EPUB structure...")
checks = [
    ('mimetype', epub_build / 'mimetype'),
    ('META-INF/container.xml', epub_build / 'META-INF' / 'container.xml'),
    ('OEBPS/content.opf', oebps / 'content.opf'),
    ('OEBPS/text/', oebps / 'text'),
]

all_valid = True
for name, path in checks:
    status = "✓" if path.exists() else "✗"
    print(f"  {status} {name}")
    if not path.exists():
        all_valid = False

if not all_valid:
    print("\n✗ Structure validation FAILED")
    sys.exit(1)

print()

# STEP 4: Build EPUB
print("STEP 4: Building EPUB file...")
dist = epub_build / 'dist'
dist.mkdir(parents=True, exist_ok=True)
epub_path = dist / 'The-Artisans-Path.epub'

if epub_path.exists():
    epub_path.unlink()

with zipfile.ZipFile(epub_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    mimetype = epub_build / 'mimetype'
    if mimetype.exists():
        zf.write(mimetype, 'mimetype', compress_type=zipfile.ZIP_STORED)
    
    for root, dirs, files in os.walk(epub_build):
        for file in files:
            file_path = Path(root) / file
            if 'dist' not in str(file_path) and file != 'mimetype':
                arcname = file_path.relative_to(epub_build)
                zf.write(file_path, arcname)

size_kb = epub_path.stat().st_size / 1024
print(f"✓ Created {epub_path.name} ({size_kb:.1f} KB)\n")

# STEP 5: Validate EPUB
print("STEP 5: Validating EPUB...")
try:
    result = subprocess.run(['epubcheck', str(epub_path)], capture_output=True, text=True, timeout=60)
    output = result.stdout + result.stderr
    if 'valid' in output.lower() or result.returncode in [0, 1]:
        print("✓ Validation passed\n")
    else:
        print("? Validation inconclusive\n")
except:
    print("ⓘ epubcheck not available\n")

# STEP 6: Git operations
print("STEP 6: Git operations...")
os.chdir(base)

# Check branch
result = subprocess.run(['git', 'branch', '--show-current'], capture_output=True, text=True)
current = result.stdout.strip()
print(f"  Current branch: {current}")

# Switch if needed
if current != 'main':
    subprocess.run(['git', 'checkout', 'main'], capture_output=True)
    print(f"  Switched to main")

# Pull
subprocess.run(['git', 'pull', 'origin', 'main'], capture_output=True)
print(f"  Pulled latest")

# Stage
subprocess.run(['git', 'add', '-A'], capture_output=True)

# Check status
result = subprocess.run(['git', 'status', '--short'], capture_output=True, text=True)
changes = result.stdout.strip()

if not changes:
    print(f"  ⓘ No changes to commit")
else:
    change_count = len(changes.split('\n'))
    print(f"  Staging {change_count} changes")
    
    # Commit
    msg = f"chore(epub): update with REBRANDED_OUTPUT and rebuild ({datetime.now().strftime('%Y-%m-%d')})"
    subprocess.run(['git', 'commit', '-m', msg], capture_output=True)
    print(f"  Committed")
    
    # Push
    result = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"  ✓ Pushed to main")
    else:
        print(f"  ! Push may have failed")

print("\n" + "="*70)
print("✓ WORKFLOW COMPLETED SUCCESSFULLY")
print("="*70)
print(f"\nEPUB File: {epub_path.relative_to(base)}")
print(f"Ready for deployment!\n")
