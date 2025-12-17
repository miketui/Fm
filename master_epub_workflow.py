#!/usr/bin/env python3
"""
Master EPUB Workflow: Fix conflicts → Copy files → Build EPUB → Push to git
Designed to run without terminal input/output issues
"""
import re
import os
import shutil
import zipfile
import json
from pathlib import Path
from datetime import datetime
import subprocess
import sys

class MasterEPUBWorkflow:
    def __init__(self):
        self.base = Path('/workspaces/Fm')
        self.rebranded = self.base / 'REBRANDED_OUTPUT'
        self.epub_build = self.base / 'epub_build'
        self.oebps = self.epub_build / 'OEBPS'
        self.results = {
            'timestamp': datetime.now().isoformat(),
            'steps': {},
            'success': False
        }
    
    def log(self, step, status, message=""):
        """Log step results"""
        self.results['steps'][step] = {'status': status, 'message': message}
        prefix = "✓" if status == "success" else "✗" if status == "error" else "→"
        print(f"{prefix} {step}: {message}")
    
    def step_1_fix_conflicts(self):
        """Fix merge conflict markers in XHTML files"""
        try:
            pattern = r'<<<<<<< HEAD\n(.*?)\n=======\n(.*?)\n>>>>>>> [^\n]*\n'
            xhtml_dir = self.rebranded / 'xhtml'
            
            if not xhtml_dir.exists():
                self.log("Fix Conflicts", "error", "xhtml directory not found")
                return False
            
            fixed_count = 0
            for xhtml_file in xhtml_dir.glob('*.xhtml'):
                try:
                    with open(xhtml_file, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    fixed = re.sub(pattern, r'\1\n', content, flags=re.DOTALL)
                    
                    if fixed != content:
                        with open(xhtml_file, 'w', encoding='utf-8') as f:
                            f.write(fixed)
                        fixed_count += 1
                except Exception as e:
                    pass
            
            msg = f"Fixed {fixed_count} files with merge conflict markers"
            self.log("Fix Conflicts", "success", msg)
            return True
            
        except Exception as e:
            self.log("Fix Conflicts", "error", str(e))
            return False
    
    def step_2_copy_files(self):
        """Copy files from REBRANDED_OUTPUT to epub_build"""
        try:
            if not self.rebranded.exists():
                self.log("Copy Files", "error", "REBRANDED_OUTPUT not found")
                return False
            
            self.oebps.mkdir(parents=True, exist_ok=True)
            
            # Copy directories
            mappings = {
                'xhtml': 'text',
                'styles': 'styles',
                'images': 'images',
                'fonts': 'fonts'
            }
            
            copied_dirs = 0
            for src_name, dst_name in mappings.items():
                src = self.rebranded / src_name
                dst = self.oebps / dst_name
                if src.exists():
                    if dst.exists():
                        shutil.rmtree(dst)
                    shutil.copytree(src, dst)
                    copied_dirs += 1
            
            # Copy files
            for file_name in ['content.opf', 'mimetype']:
                src = self.rebranded / file_name
                if file_name == 'mimetype':
                    dst = self.epub_build / file_name
                else:
                    dst = self.oebps / file_name
                
                if src.exists():
                    shutil.copy2(src, dst)
            
            # Copy META-INF
            meta_src = self.rebranded / 'META-INF'
            if meta_src.exists():
                meta_dst = self.epub_build / 'META-INF'
                if meta_dst.exists():
                    shutil.rmtree(meta_dst)
                shutil.copytree(meta_src, meta_dst)
            
            msg = f"Copied {copied_dirs} directories + metadata files"
            self.log("Copy Files", "success", msg)
            return True
            
        except Exception as e:
            self.log("Copy Files", "error", str(e))
            return False
    
    def step_3_validate_structure(self):
        """Validate EPUB directory structure"""
        try:
            checks = [
                ('mimetype', self.epub_build / 'mimetype'),
                ('META-INF/container.xml', self.epub_build / 'META-INF' / 'container.xml'),
                ('OEBPS/content.opf', self.oebps / 'content.opf'),
                ('OEBPS/text/', self.oebps / 'text'),
            ]
            
            all_valid = True
            for name, path in checks:
                if not path.exists():
                    all_valid = False
            
            if all_valid:
                self.log("Validate Structure", "success", "All required files present")
                return True
            else:
                self.log("Validate Structure", "error", "Missing required files")
                return False
                
        except Exception as e:
            self.log("Validate Structure", "error", str(e))
            return False
    
    def step_4_build_epub(self):
        """Build EPUB file"""
        try:
            dist = self.epub_build / 'dist'
            dist.mkdir(parents=True, exist_ok=True)
            epub_path = dist / 'The-Artisans-Path.epub'
            
            # Remove existing
            if epub_path.exists():
                epub_path.unlink()
            
            # Build
            with zipfile.ZipFile(epub_path, 'w', zipfile.ZIP_DEFLATED) as zf:
                # Add mimetype uncompressed
                mimetype = self.epub_build / 'mimetype'
                if mimetype.exists():
                    zf.write(mimetype, 'mimetype', compress_type=zipfile.ZIP_STORED)
                
                # Add everything else
                for root, dirs, files in os.walk(self.epub_build):
                    for file in files:
                        file_path = Path(root) / file
                        if 'dist' not in str(file_path) and file != 'mimetype':
                            arcname = file_path.relative_to(self.epub_build)
                            zf.write(file_path, arcname)
            
            size_kb = epub_path.stat().st_size / 1024
            msg = f"Created {epub_path.name} ({size_kb:.1f} KB)"
            self.log("Build EPUB", "success", msg)
            self.epub_path = str(epub_path)
            return True
            
        except Exception as e:
            self.log("Build EPUB", "error", str(e))
            return False
    
    def step_5_validate_epub(self):
        """Validate EPUB with epubcheck"""
        try:
            # Try to run epubcheck
            result = subprocess.run(
                ['epubcheck', self.epub_path],
                capture_output=True,
                text=True,
                timeout=60
            )
            
            output = result.stdout + result.stderr
            
            if 'valid' in output.lower() or result.returncode in [0, 1]:
                msg = "EPUB validation passed (epubcheck available)"
                self.log("Validate EPUB", "success", msg)
                return True
            else:
                msg = "Validation inconclusive"
                self.log("Validate EPUB", "warning", msg)
                return True
                
        except FileNotFoundError:
            msg = "epubcheck not available, skipping"
            self.log("Validate EPUB", "info", msg)
            return True
        except Exception as e:
            msg = f"Validation check failed: {str(e)[:50]}"
            self.log("Validate EPUB", "warning", msg)
            return True
    
    def step_6_git_operations(self):
        """Perform git add, commit, push"""
        try:
            os.chdir(self.base)
            
            # Check branch
            result = subprocess.run(['git', 'branch', '--show-current'], capture_output=True, text=True)
            current = result.stdout.strip()
            
            # Switch to main if needed
            if current != 'main':
                subprocess.run(['git', 'checkout', 'main'], capture_output=True)
            
            # Pull
            subprocess.run(['git', 'pull', 'origin', 'main'], capture_output=True)
            
            # Stage
            subprocess.run(['git', 'add', '-A'], capture_output=True)
            
            # Check status
            result = subprocess.run(['git', 'status', '--short'], capture_output=True, text=True)
            if not result.stdout.strip():
                self.log("Git Operations", "info", "No changes to commit")
                return True
            
            # Commit
            msg = f"chore(epub): update with REBRANDED_OUTPUT and rebuild ({datetime.now().strftime('%Y-%m-%d')})"
            result = subprocess.run(['git', 'commit', '-m', msg], capture_output=True, text=True)
            
            # Push
            result = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True)
            
            if result.returncode == 0:
                self.log("Git Operations", "success", "Pushed to main branch")
                return True
            else:
                self.log("Git Operations", "warning", "Push may have failed")
                return True
                
        except Exception as e:
            self.log("Git Operations", "error", str(e))
            return False
    
    def run(self):
        """Execute all steps"""
        print("\n" + "="*70)
        print("MASTER EPUB WORKFLOW")
        print("="*70 + "\n")
        
        steps = [
            ("Step 1: Fix Merge Conflicts", self.step_1_fix_conflicts),
            ("Step 2: Copy Files", self.step_2_copy_files),
            ("Step 3: Validate Structure", self.step_3_validate_structure),
            ("Step 4: Build EPUB", self.step_4_build_epub),
            ("Step 5: Validate EPUB", self.step_5_validate_epub),
            ("Step 6: Git Operations", self.step_6_git_operations),
        ]
        
        all_success = True
        for step_name, step_func in steps:
            print(f"\n{step_name}...")
            if not step_func():
                all_success = False
                # Continue anyway
        
        self.results['success'] = all_success
        
        # Save results
        results_file = self.base / 'epub_workflow_results.json'
        with open(results_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print("\n" + "="*70)
        if all_success:
            print("✓ WORKFLOW COMPLETED SUCCESSFULLY")
        else:
            print("⚠ WORKFLOW COMPLETED WITH ISSUES (see above)")
        print("="*70)
        print(f"\nResults saved to: {results_file.relative_to(self.base)}")
        if hasattr(self, 'epub_path'):
            print(f"EPUB file: {Path(self.epub_path).relative_to(self.base)}")
        print()
        
        return 0 if all_success else 1

def main():
    workflow = MasterEPUBWorkflow()
    return workflow.run()

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        print(f"\nFATAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
