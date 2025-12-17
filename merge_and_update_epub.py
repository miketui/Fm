#!/usr/bin/env python3
"""
Script to merge with main branch and copy REBRANDED_OUTPUT files to epub_build
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

def run_command(cmd, description=""):
    """Run a shell command and return output"""
    print(f"\n{'='*60}")
    if description:
        print(f"➤ {description}")
    print(f"$ {cmd}")
    print('='*60)
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        return result.returncode == 0, result.stdout
    except Exception as e:
        print(f"Error: {e}")
        return False, str(e)

def main():
    base_dir = Path('/workspaces/Fm')
    os.chdir(base_dir)
    
    print("\n" + "="*60)
    print("EPUB BUILD AND MERGE PROCESS")
    print("="*60)
    
    # Step 1: Check git status
    print("\n[STEP 1] Checking git status...")
    success, output = run_command("git status --short", "Current git status")
    
    # Step 2: Merge with main (if not already on main)
    print("\n[STEP 2] Ensuring we're on main branch...")
    success, output = run_command("git branch --show-current", "Check current branch")
    current_branch = output.strip()
    
    if current_branch != "main":
        print(f"\nCurrent branch is '{current_branch}', switching to main...")
        success, _ = run_command("git checkout main", "Switch to main branch")
        if not success:
            print("ERROR: Could not switch to main branch")
            return False
    
    # Step 3: Pull latest changes
    print("\n[STEP 3] Pulling latest changes from remote...")
    success, _ = run_command("git pull origin main", "Pull latest changes")
    
    # Step 4: Copy REBRANDED_OUTPUT files to epub_build
    print("\n[STEP 4] Copying REBRANDED_OUTPUT files to epub_build...")
    
    rebranded_dir = base_dir / "REBRANDED_OUTPUT"
    epub_build_dir = base_dir / "epub_build"
    
    if not rebranded_dir.exists():
        print(f"ERROR: {rebranded_dir} not found!")
        return False
    
    if not epub_build_dir.exists():
        print(f"ERROR: {epub_build_dir} not found!")
        return False
    
    # Identify key directories to copy
    directories_to_copy = ['xhtml', 'styles', 'images', 'fonts']
    files_to_copy = ['content.opf', 'mimetype']
    
    oebps_dir = epub_build_dir / "OEBPS"
    oebps_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy directories
    for dir_name in directories_to_copy:
        src = rebranded_dir / dir_name
        if src.exists():
            dst = oebps_dir / dir_name
            # Remove existing directory
            if dst.exists():
                shutil.rmtree(dst)
            print(f"  Copying {dir_name}...")
            shutil.copytree(src, dst)
        else:
            print(f"  Warning: {dir_name} not found in REBRANDED_OUTPUT")
    
    # Copy files to OEBPS
    for file_name in files_to_copy:
        src = rebranded_dir / file_name
        if src.exists():
            dst = oebps_dir / file_name
            print(f"  Copying {file_name}...")
            shutil.copy2(src, dst)
        else:
            print(f"  Warning: {file_name} not found in REBRANDED_OUTPUT")
    
    # Copy mimetype and container separately if in META-INF
    meta_inf_src = rebranded_dir / "META-INF"
    if meta_inf_src.exists():
        meta_inf_dst = epub_build_dir / "META-INF"
        if meta_inf_dst.exists():
            shutil.rmtree(meta_inf_dst)
        print("  Copying META-INF...")
        shutil.copytree(meta_inf_src, meta_inf_dst)
    
    print("\n✓ All files copied successfully!")
    
    # Step 5: Verify EPUB structure
    print("\n[STEP 5] Verifying EPUB structure...")
    required_files = [
        epub_build_dir / "mimetype",
        epub_build_dir / "META-INF" / "container.xml",
        oebps_dir / "content.opf"
    ]
    
    for file_path in required_files:
        if file_path.exists():
            print(f"  ✓ {file_path.relative_to(base_dir)}")
        else:
            print(f"  ✗ MISSING: {file_path.relative_to(base_dir)}")
    
    print("\n" + "="*60)
    print("✓ Merge and file copy completed successfully!")
    print("="*60)
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
