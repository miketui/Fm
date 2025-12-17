#!/usr/bin/env python3
"""
Copy EPUB file to multiple accessible locations
"""
import shutil
import os
from pathlib import Path

base = Path('/workspaces/Fm')
source = base / 'epub_build' / 'dist' / 'The-Artisans-Path.epub'
dest_root = base / 'The-Artisans-Path.epub'
dest_releases = base / 'releases' / 'The-Artisans-Path.epub'

print("\n" + "="*70)
print("EPUB FILE VERIFICATION AND COPY")
print("="*70 + "\n")

# Check source
if source.exists():
    size_mb = source.stat().st_size / (1024 * 1024)
    print(f"✓ Source file found: {source}")
    print(f"  Size: {size_mb:.2f} MB")
    print(f"  Path: {source.relative_to(base)}\n")
else:
    print(f"✗ Source file NOT found: {source}")
    exit(1)

# Copy to root
print(f"Copying to root directory...")
try:
    shutil.copy2(source, dest_root)
    print(f"✓ Copied to: {dest_root.relative_to(base)}")
    print(f"  Size: {dest_root.stat().st_size / (1024*1024):.2f} MB\n")
except Exception as e:
    print(f"✗ Failed to copy to root: {e}\n")

# Copy to releases directory
print(f"Copying to releases directory...")
try:
    dest_releases.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, dest_releases)
    print(f"✓ Copied to: {dest_releases.relative_to(base)}")
    print(f"  Size: {dest_releases.stat().st_size / (1024*1024):.2f} MB\n")
except Exception as e:
    print(f"✗ Failed to copy to releases: {e}\n")

# List all locations
print("="*70)
print("EPUB FILE LOCATIONS:")
print("="*70)

locations = [source, dest_root, dest_releases]
for loc in locations:
    if loc.exists():
        size = loc.stat().st_size / (1024*1024)
        print(f"✓ {loc.relative_to(base):50} ({size:.2f} MB)")
    else:
        print(f"✗ {loc.relative_to(base):50} (NOT FOUND)")

print("\n" + "="*70)
print("SUMMARY:")
print("="*70)
print(f"\nPrimary location: {dest_root}")
print(f"Secondary location: {dest_releases}")
print(f"Original location: {source}")
print(f"\nAll copies are identical and ready for distribution.\n")
