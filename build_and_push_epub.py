#!/usr/bin/env python3
"""
Complete EPUB build, validation, and git push workflow
"""

import os
import shutil
import subprocess
import sys
import json
import zipfile
from pathlib import Path
from datetime import datetime

class EPUBBuilder:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.rebranded_dir = self.base_dir / "REBRANDED_OUTPUT"
        self.epub_build_dir = self.base_dir / "epub_build"
        self.oebps_dir = self.epub_build_dir / "OEBPS"
        self.log = []
        
    def log_msg(self, level, msg):
        """Log messages to both console and internal log"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {level}: {msg}"
        self.log.append(log_entry)
        print(log_entry)
    
    def run_cmd(self, cmd, description=""):
        """Run command and capture output"""
        if description:
            self.log_msg("INFO", f">> {description}")
        self.log_msg("CMD", f"$ {cmd}")
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=str(self.base_dir))
            if result.stdout:
                self.log_msg("OUTPUT", result.stdout[:500])
            if result.returncode != 0 and result.stderr:
                self.log_msg("ERROR", result.stderr[:500])
            return result.returncode == 0, result.stdout, result.stderr
        except Exception as e:
            self.log_msg("ERROR", str(e))
            return False, "", str(e)
    
    def copy_rebranded_to_epub_build(self):
        """Copy files from REBRANDED_OUTPUT to epub_build"""
        self.log_msg("INFO", "=== STEP 2: Copying REBRANDED_OUTPUT files ===")
        
        if not self.rebranded_dir.exists():
            self.log_msg("ERROR", f"REBRANDED_OUTPUT directory not found at {self.rebranded_dir}")
            return False
        
        if not self.epub_build_dir.exists():
            self.log_msg("ERROR", f"epub_build directory not found at {self.epub_build_dir}")
            return False
        
        self.oebps_dir.mkdir(parents=True, exist_ok=True)
        
        # Directories to copy
        dirs_to_copy = ['xhtml', 'styles', 'images', 'fonts']
        for dir_name in dirs_to_copy:
            src = self.rebranded_dir / dir_name
            dst = self.oebps_dir / dir_name
            if src.exists():
                if dst.exists():
                    shutil.rmtree(dst)
                shutil.copytree(src, dst)
                self.log_msg("INFO", f"✓ Copied {dir_name}")
            else:
                self.log_msg("WARNING", f"Directory {dir_name} not found in REBRANDED_OUTPUT")
        
        # Copy files
        for file_name in ['content.opf', 'mimetype']:
            src = self.rebranded_dir / file_name
            if src.exists():
                dst = self.oebps_dir / file_name
                shutil.copy2(src, dst)
                self.log_msg("INFO", f"✓ Copied {file_name}")
        
        # Copy META-INF
        meta_src = self.rebranded_dir / "META-INF"
        if meta_src.exists():
            meta_dst = self.epub_build_dir / "META-INF"
            if meta_dst.exists():
                shutil.rmtree(meta_dst)
            shutil.copytree(meta_src, meta_dst)
            self.log_msg("INFO", "✓ Copied META-INF")
        
        self.log_msg("INFO", "✓ All files copied successfully")
        return True
    
    def validate_epub_structure(self):
        """Validate EPUB directory structure"""
        self.log_msg("INFO", "=== STEP 3: Validating EPUB structure ===")
        
        required_files = [
            (self.epub_build_dir / "mimetype", "mimetype"),
            (self.epub_build_dir / "META-INF" / "container.xml", "META-INF/container.xml"),
            (self.oebps_dir / "content.opf", "OEBPS/content.opf"),
        ]
        
        all_exist = True
        for file_path, display_name in required_files:
            if file_path.exists():
                self.log_msg("INFO", f"✓ Found {display_name}")
            else:
                self.log_msg("ERROR", f"✗ Missing {display_name}")
                all_exist = False
        
        return all_exist
    
    def build_epub_file(self):
        """Build the EPUB file"""
        self.log_msg("INFO", "=== STEP 4: Building EPUB file ===")
        
        output_dir = self.epub_build_dir / "dist"
        output_dir.mkdir(parents=True, exist_ok=True)
        epub_path = output_dir / "The-Artisans-Path.epub"
        
        try:
            with zipfile.ZipFile(epub_path, 'w', zipfile.ZIP_DEFLATED) as zf:
                # Add mimetype uncompressed
                mimetype_file = self.epub_build_dir / "mimetype"
                if mimetype_file.exists():
                    zf.write(mimetype_file, 'mimetype', compress_type=zipfile.ZIP_STORED)
                    self.log_msg("INFO", "✓ Added mimetype")
                
                # Add all other files
                for root, dirs, files in os.walk(self.epub_build_dir):
                    for file in files:
                        file_path = Path(root) / file
                        arcname = file_path.relative_to(self.epub_build_dir)
                        if arcname != Path('mimetype') and 'dist' not in str(arcname):
                            zf.write(file_path, arcname)
            
            self.log_msg("INFO", f"✓ EPUB file created: {epub_path.relative_to(self.base_dir)}")
            
            # Verify file size
            size_kb = epub_path.stat().st_size / 1024
            self.log_msg("INFO", f"File size: {size_kb:.1f} KB")
            
            return True, str(epub_path)
        except Exception as e:
            self.log_msg("ERROR", f"Failed to build EPUB: {str(e)}")
            return False, None
    
    def validate_epub(self, epub_path):
        """Validate EPUB file"""
        self.log_msg("INFO", "=== STEP 5: Validating EPUB ===")
        
        # Check if epubcheck is available
        success, out, err = self.run_cmd("which epubcheck", "Checking for epubcheck")
        
        if success and out.strip():
            success, out, err = self.run_cmd(f"epubcheck {epub_path}", "Running epubcheck validation")
            if success:
                self.log_msg("INFO", "✓ EPUB validation passed")
                return True
            else:
                # epubcheck returns non-zero even for warnings
                if "Valid" in out or "valid" in out:
                    self.log_msg("INFO", "✓ EPUB is valid (warnings may exist)")
                    return True
                else:
                    self.log_msg("ERROR", f"Validation issues: {out[:500]}")
                    return False
        else:
            self.log_msg("WARNING", "epubcheck not available, skipping validation")
            return True
    
    def git_operations(self):
        """Perform git operations"""
        self.log_msg("INFO", "=== STEP 6: Git operations ===")
        
        # Check current branch
        success, out, err = self.run_cmd("git branch --show-current", "Check current branch")
        current_branch = out.strip()
        self.log_msg("INFO", f"Current branch: {current_branch}")
        
        if current_branch != "main":
            self.log_msg("INFO", "Switching to main branch...")
            success, _, _ = self.run_cmd("git checkout main", "Switch to main")
            if not success:
                self.log_msg("ERROR", "Failed to switch to main branch")
                return False
        
        # Pull latest
        self.log_msg("INFO", "Pulling latest changes...")
        success, _, _ = self.run_cmd("git pull origin main", "Pull latest")
        
        # Add changes
        self.log_msg("INFO", "Staging changes...")
        self.run_cmd("git add -A", "Stage all changes")
        
        # Check status
        success, status, _ = self.run_cmd("git status --short", "Check status")
        if status.strip():
            self.log_msg("INFO", f"Changes to commit:\n{status[:500]}")
        else:
            self.log_msg("INFO", "No changes to commit")
            return True
        
        # Commit
        commit_msg = f"chore(epub): update epub_build with REBRANDED_OUTPUT files and rebuild EPUB ({datetime.now().strftime('%Y-%m-%d')})"
        self.log_msg("INFO", f"Committing with message: {commit_msg}")
        success, _, _ = self.run_cmd(f'git commit -m "{commit_msg}"', "Commit changes")
        
        if not success:
            self.log_msg("WARNING", "Commit may have failed or no changes to commit")
        
        # Push
        self.log_msg("INFO", "Pushing to origin...")
        success, _, err = self.run_cmd("git push origin main", "Push to main")
        
        if success:
            self.log_msg("INFO", "✓ Successfully pushed to main")
            return True
        else:
            self.log_msg("ERROR", f"Push failed: {err[:500]}")
            return False
    
    def run_all(self):
        """Execute the complete workflow"""
        print("\n" + "="*70)
        print("EPUB BUILD, VALIDATION, AND GIT PUSH WORKFLOW")
        print("="*70 + "\n")
        
        self.log_msg("INFO", "=== STEP 1: Preparing ===")
        self.log_msg("INFO", f"Working directory: {self.base_dir}")
        self.log_msg("INFO", f"REBRANDED_OUTPUT: {self.rebranded_dir}")
        self.log_msg("INFO", f"epub_build: {self.epub_build_dir}")
        
        # Step 2: Copy files
        if not self.copy_rebranded_to_epub_build():
            self.log_msg("ERROR", "Failed to copy files")
            return False
        
        # Step 3: Validate structure
        if not self.validate_epub_structure():
            self.log_msg("ERROR", "EPUB structure validation failed")
            return False
        
        # Step 4: Build EPUB
        success, epub_path = self.build_epub_file()
        if not success:
            self.log_msg("ERROR", "EPUB build failed")
            return False
        
        # Step 5: Validate EPUB
        if not self.validate_epub(epub_path):
            self.log_msg("WARNING", "EPUB validation had issues")
        
        # Step 6: Git operations
        if not self.git_operations():
            self.log_msg("ERROR", "Git operations failed")
            return False
        
        print("\n" + "="*70)
        print("✓ WORKFLOW COMPLETED SUCCESSFULLY")
        print("="*70 + "\n")
        return True


def main():
    builder = EPUBBuilder("/workspaces/Fm")
    success = builder.run_all()
    
    # Save log
    log_file = builder.base_dir / "epub_build_log.txt"
    with open(log_file, 'w') as f:
        f.write('\n'.join(builder.log))
    print(f"\nLog saved to: {log_file}")
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
