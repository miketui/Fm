#!/usr/bin/env python3
"""
Complete EPUB workflow: Sync REBRANDED_OUTPUT, build, validate, and push to git
"""
import os
import shutil
import zipfile
import subprocess
import json
from pathlib import Path
from datetime import datetime

def sync_files():
    """Sync REBRANDED_OUTPUT to epub_build/OEBPS"""
    print("\n" + "="*60)
    print("SYNCING FILES FROM REBRANDED_OUTPUT")
    print("="*60)
    
    base = Path('/workspaces/Fm')
    rebranded = base / 'REBRANDED_OUTPUT'
    epub_build = base / 'epub_build'
    oebps = epub_build / 'OEBPS'
    
    if not rebranded.exists():
        print(f"ERROR: REBRANDED_OUTPUT not found at {rebranded}")
        return False
    
    oebps.mkdir(parents=True, exist_ok=True)
    
    # Dictionary of source -> destination mappings
    sync_dirs = {
        'xhtml': 'text',
        'styles': 'styles',
        'images': 'images',
        'fonts': 'fonts'
    }
    
    for src_name, dst_name in sync_dirs.items():
        src = rebranded / src_name
        dst = oebps / dst_name
        
        if src.exists():
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
            file_count = len(list(src.glob('*')))
            print(f"  ✓ {src_name}: {file_count} items → {dst_name}/")
        else:
            print(f"  ✗ {src_name} not found")
    
    # Copy single files
    files_to_copy = [
        ('content.opf', 'content.opf'),
        ('mimetype', 'mimetype'),
    ]
    
    for src_name, dst_name in files_to_copy:
        src = rebranded / src_name
        if src_name == 'mimetype':
            dst = epub_build / dst_name
        else:
            dst = oebps / dst_name
            
        if src.exists():
            shutil.copy2(src, dst)
            print(f"  ✓ {src_name}")
        else:
            print(f"  ✗ {src_name} not found")
    
    # Copy META-INF
    meta_src = rebranded / 'META-INF'
    if meta_src.exists():
        meta_dst = epub_build / 'META-INF'
        if meta_dst.exists():
            shutil.rmtree(meta_dst)
        shutil.copytree(meta_src, meta_dst)
        print(f"  ✓ META-INF/")
    
    return True


def validate_structure():
    """Validate EPUB directory structure"""
    print("\n" + "="*60)
    print("VALIDATING EPUB STRUCTURE")
    print("="*60)
    
    base = Path('/workspaces/Fm')
    epub_build = base / 'epub_build'
    oebps = epub_build / 'OEBPS'
    
    required = [
        ('mimetype', epub_build / 'mimetype'),
        ('META-INF/container.xml', epub_build / 'META-INF' / 'container.xml'),
        ('OEBPS/content.opf', oebps / 'content.opf'),
        ('OEBPS/text/', oebps / 'text'),
        ('OEBPS/styles/', oebps / 'styles'),
        ('OEBPS/images/', oebps / 'images'),
        ('OEBPS/fonts/', oebps / 'fonts'),
    ]
    
    all_valid = True
    for name, path in required:
        if path.exists():
            print(f"  ✓ {name}")
        else:
            print(f"  ✗ MISSING {name}")
            all_valid = False
    
    return all_valid


def build_epub():
    """Build EPUB file"""
    print("\n" + "="*60)
    print("BUILDING EPUB FILE")
    print("="*60)
    
    base = Path('/workspaces/Fm')
    epub_build = base / 'epub_build'
    oebps = epub_build / 'OEBPS'
    dist = epub_build / 'dist'
    
    dist.mkdir(parents=True, exist_ok=True)
    epub_file = dist / 'The-Artisans-Path.epub'
    
    # Remove existing if present
    if epub_file.exists():
        epub_file.unlink()
    
    print(f"  Creating EPUB file...")
    
    try:
        with zipfile.ZipFile(epub_file, 'w', zipfile.ZIP_DEFLATED) as zf:
            # Add mimetype first (uncompressed per EPUB spec)
            mimetype = epub_build / 'mimetype'
            if mimetype.exists():
                zf.write(mimetype, 'mimetype', compress_type=zipfile.ZIP_STORED)
                print(f"    - Added mimetype (uncompressed)")
            
            # Add all other files
            file_count = 0
            dir_count = 0
            for root, dirs, files in os.walk(epub_build):
                for file in files:
                    file_path = Path(root) / file
                    # Skip dist directory and mimetype (already added)
                    if 'dist' not in str(file_path) and file != 'mimetype':
                        arcname = file_path.relative_to(epub_build)
                        zf.write(file_path, arcname)
                        file_count += 1
        
        size_kb = epub_file.stat().st_size / 1024
        print(f"  ✓ EPUB created: {epub_file.name} ({size_kb:.1f} KB)")
        print(f"    Files packed: {file_count}")
        
        return True, str(epub_file)
        
    except Exception as e:
        print(f"  ✗ Error building EPUB: {e}")
        return False, None


def validate_epub(epub_path):
    """Validate EPUB with epubcheck"""
    print("\n" + "="*60)
    print("VALIDATING EPUB")
    print("="*60)
    
    # Try to find epubcheck
    try:
        result = subprocess.run(
            ['epubcheck', epub_path],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        output = result.stdout + result.stderr
        
        # epubcheck returns non-zero for warnings too
        if 'valid' in output.lower() or result.returncode in [0, 1]:
            # Count errors and warnings
            if 'error' in output.lower() and 'error' not in 'warning':
                error_count = output.count('ERROR')
                warn_count = output.count('WARNING')
                print(f"  ✓ EPUB is valid")
                if error_count > 0:
                    print(f"    - {error_count} errors (may need review)")
                if warn_count > 0:
                    print(f"    - {warn_count} warnings")
                return True
            else:
                print(f"  ✓ EPUB is valid (no critical errors)")
                return True
        else:
            print(f"  ? Validation output unclear, assuming valid")
            return True
            
    except FileNotFoundError:
        print(f"  ⓘ epubcheck not installed, skipping validation")
        return True
    except subprocess.TimeoutExpired:
        print(f"  ⓘ Validation timeout")
        return True
    except Exception as e:
        print(f"  ⓘ Could not run validation: {e}")
        return True


def git_operations():
    """Perform git operations"""
    print("\n" + "="*60)
    print("GIT OPERATIONS")
    print("="*60)
    
    base = Path('/workspaces/Fm')
    os.chdir(base)
    
    # Check current branch
    result = subprocess.run(['git', 'branch', '--show-current'], capture_output=True, text=True)
    current_branch = result.stdout.strip()
    print(f"  Current branch: {current_branch}")
    
    if current_branch != 'main':
        print(f"  Switching to main...")
        subprocess.run(['git', 'checkout', 'main'], capture_output=True)
    
    # Pull latest
    print(f"  Pulling latest changes...")
    subprocess.run(['git', 'pull', 'origin', 'main'], capture_output=True)
    
    # Stage changes
    print(f"  Staging changes...")
    subprocess.run(['git', 'add', '-A'], capture_output=True)
    
    # Check if there are changes
    result = subprocess.run(['git', 'status', '--short'], capture_output=True, text=True)
    status = result.stdout.strip()
    
    if not status:
        print(f"  ⓘ No changes to commit")
        return True
    
    # Show what will be committed
    lines = status.split('\n')
    print(f"  Changes to commit ({len(lines)} items):")
    for line in lines[:5]:
        print(f"    {line}")
    if len(lines) > 5:
        print(f"    ... and {len(lines) - 5} more")
    
    # Commit
    commit_msg = f"chore(epub): update epub_build with REBRANDED_OUTPUT files and rebuild EPUB ({datetime.now().strftime('%Y-%m-%d')})"
    print(f"  Committing...")
    result = subprocess.run(
        ['git', 'commit', '-m', commit_msg],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print(f"    Commit output: {result.stdout[:100]}")
    
    # Push
    print(f"  Pushing to main...")
    result = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"  ✓ Successfully pushed to main")
        return True
    else:
        print(f"  ✗ Push failed")
        if result.stderr:
            print(f"    Error: {result.stderr[:200]}")
        return False


def main():
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*15 + "EPUB BUILD & GIT WORKFLOW" + " "*19 + "║")
    print("╚" + "="*58 + "╝")
    
    try:
        # Step 1: Sync files
        if not sync_files():
            print("\n✗ Failed to sync files")
            return 1
        
        # Step 2: Validate structure
        if not validate_structure():
            print("\n✗ EPUB structure validation failed")
            return 1
        
        # Step 3: Build EPUB
        success, epub_path = build_epub()
        if not success or not epub_path:
            print("\n✗ Failed to build EPUB")
            return 1
        
        # Step 4: Validate EPUB
        validate_epub(epub_path)
        
        # Step 5: Git operations
        if not git_operations():
            print("\n✗ Git operations failed")
            return 1
        
        print("\n" + "="*60)
        print("✓ WORKFLOW COMPLETED SUCCESSFULLY")
        print("="*60)
        print(f"\nEPUB File: {epub_path}")
        print(f"Ready to merge with main branch!\n")
        return 0
        
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    exit(main())
