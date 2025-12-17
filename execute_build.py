#!/usr/bin/env python3
"""
Execute EPUB build pipeline
"""
import os
import sys
import shutil
import subprocess
from pathlib import Path

def main():
    os.chdir('/workspaces/Fm')
    
    print("\n" + "="*70)
    print("EPUB BUILD AND VALIDATION PIPELINE")
    print("="*70)
    
    # Step 1: Check git status
    print("\n[STEP 1] Checking git status...")
    try:
        result = subprocess.run(['git', 'status', '--short'], capture_output=True, text=True, timeout=10)
        print(result.stdout if result.stdout else "No changes")
        print("✓ Git status checked")
    except Exception as e:
        print(f"✗ Error checking git status: {e}")
    
    # Step 2: Check current branch
    print("\n[STEP 2] Checking current branch...")
    try:
        result = subprocess.run(['git', 'branch', '--show-current'], capture_output=True, text=True, timeout=10)
        current_branch = result.stdout.strip()
        print(f"Current branch: {current_branch}")
        print("✓ Branch checked")
    except Exception as e:
        print(f"✗ Error checking branch: {e}")
    
    # Step 3: Check EPUB build directory structure
    print("\n[STEP 3] Checking EPUB build directory structure...")
    epub_build = Path('/workspaces/Fm/epub_build')
    if epub_build.exists():
        print(f"✓ epub_build directory exists")
        # Count files
        xhtml_count = len(list((epub_build / 'OEBPS' / 'xhtml').glob('*.xhtml'))) if (epub_build / 'OEBPS' / 'xhtml').exists() else 0
        images_count = len(list((epub_build / 'OEBPS' / 'images').glob('*'))) if (epub_build / 'OEBPS' / 'images').exists() else 0
        styles_count = len(list((epub_build / 'OEBPS' / 'styles').glob('*.css'))) if (epub_build / 'OEBPS' / 'styles').exists() else 0
        print(f"  - XHTML files: {xhtml_count}")
        print(f"  - Images: {images_count}")
        print(f"  - CSS files: {styles_count}")
    else:
        print("✗ epub_build directory does not exist")
    
    # Step 4: Check available build scripts
    print("\n[STEP 4] Available build scripts:")
    build_scripts = [
        'build_final_package.py',
        'build_complete_epub.py',
        'build_final_epub.py',
        'build_home_epub.py',
        'build_epub.py'
    ]
    for script in build_scripts:
        script_path = Path('/workspaces/Fm') / script
        if script_path.exists():
            print(f"  ✓ {script}")
        else:
            print(f"  ✗ {script}")
    
    # Step 5: Run build_final_package.py (most complete)
    print("\n[STEP 5] Running build_final_package.py...")
    try:
        result = subprocess.run(
            [sys.executable, 'build_final_package.py'],
            capture_output=True,
            text=True,
            timeout=60
        )
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        if result.returncode == 0:
            print("✓ Build completed successfully")
        else:
            print(f"✗ Build failed with return code {result.returncode}")
    except subprocess.TimeoutExpired:
        print("✗ Build timed out")
    except Exception as e:
        print(f"✗ Error running build: {e}")
    
    # Step 6: Check for EPUB output
    print("\n[STEP 6] Checking for EPUB output...")
    dist_dir = Path('/workspaces/Fm/REBRANDED_OUTPUT/dist')
    if dist_dir.exists():
        epub_files = list(dist_dir.glob('*.epub'))
        if epub_files:
            for epub_file in epub_files:
                size_mb = epub_file.stat().st_size / (1024 * 1024)
                print(f"  ✓ {epub_file.name} ({size_mb:.2f} MB)")
        else:
            print("  ✗ No EPUB files found in dist/")
    else:
        print("  ✗ dist/ directory not found")
    
    # Step 7: Attempt validation with epubcheck
    print("\n[STEP 7] Checking for epubcheck...")
    epubcheck_paths = [
        Path('/workspaces/Fm/epubcheck/epubcheck.jar'),
        Path('/usr/bin/epubcheck'),
        Path('/usr/local/bin/epubcheck')
    ]
    epubcheck_found = None
    for path in epubcheck_paths:
        if path.exists():
            epubcheck_found = path
            print(f"  ✓ Found epubcheck at {path}")
            break
    
    if not epubcheck_found:
        print("  ✗ epubcheck not found")
    
    # Step 8: Validate EPUB if found
    if epubcheck_found and dist_dir.exists():
        epub_files = list(dist_dir.glob('*.epub'))
        if epub_files:
            print("\n[STEP 8] Running validation...")
            for epub_file in epub_files:
                print(f"\n  Validating {epub_file.name}...")
                try:
                    if str(epubcheck_found).endswith('.jar'):
                        cmd = ['java', '-jar', str(epubcheck_found), str(epub_file)]
                    else:
                        cmd = [str(epubcheck_found), str(epub_file)]
                    
                    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                    # Print last 50 lines of output
                    lines = result.stdout.split('\n')
                    for line in lines[-50:]:
                        if line.strip():
                            print(f"    {line}")
                except Exception as e:
                    print(f"  ✗ Validation error: {e}")
    
    print("\n" + "="*70)
    print("BUILD PIPELINE COMPLETE")
    print("="*70 + "\n")

if __name__ == '__main__':
    main()
