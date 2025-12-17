#!/usr/bin/env python3
import os
import shutil
import sys

epub_source = '/workspaces/Fm/epub_build/dist/The-Artisans-Path.epub'
epub_dest = '/workspaces/Fm/The-Artisans-Path.epub'

print("=" * 60)
print("EPUB File Check and Copy Operation")
print("=" * 60)

# Check source file
if os.path.exists(epub_source):
    size = os.path.getsize(epub_source)
    size_mb = size / (1024*1024)
    print(f"\n1. Source file found:")
    print(f"   Path: {epub_source}")
    print(f"   Size: {size:,} bytes ({size_mb:.2f} MB)")
    
    # Get file type info
    stat_info = os.stat(epub_source)
    print(f"   Type: EPUB file (ZIP archive)")
    
    # Copy file
    print(f"\n2. Copying file...")
    try:
        shutil.copy2(epub_source, epub_dest)
        print(f"   ✓ File copied successfully")
        
        # Verify destination
        if os.path.exists(epub_dest):
            dest_size = os.path.getsize(epub_dest)
            dest_size_mb = dest_size / (1024*1024)
            print(f"\n3. Destination file verified:")
            print(f"   Path: {epub_dest}")
            print(f"   Size: {dest_size:,} bytes ({dest_size_mb:.2f} MB)")
            
            # Check both files match
            if size == dest_size:
                print(f"   ✓ File sizes match (copy verified)")
            else:
                print(f"   ✗ File sizes don't match!")
                sys.exit(1)
        else:
            print(f"   ✗ Destination file not found after copy!")
            sys.exit(1)
            
    except Exception as e:
        print(f"   ✗ Error copying file: {e}")
        sys.exit(1)
else:
    print(f"\n✗ Source file not found: {epub_source}")
    sys.exit(1)

print(f"\n" + "=" * 60)
print("Summary:")
print("=" * 60)
print(f"Source: {epub_source}")
print(f"Destination: {epub_dest}")
print(f"File Size: {size:,} bytes ({size_mb:.2f} MB)")
print(f"Status: ✓ Copy completed successfully")
print("=" * 60)
