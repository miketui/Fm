#!/usr/bin/env python3
"""
Fix merge conflict markers in XHTML files by keeping the HEAD version
"""
import re
from pathlib import Path

def fix_merge_conflicts(file_path):
    """Remove merge conflict markers, keeping HEAD version"""
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Pattern: <<<<<<< HEAD ... ======= ... >>>>>>> branchname
    # We keep everything between <<<<<<< and =======
    pattern = r'<<<<<<< HEAD\n(.*?)\n=======\n(.*?)\n>>>>>>> [^\n]*\n'
    
    fixed = re.sub(pattern, r'\1\n', content, flags=re.DOTALL)
    
    if fixed != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(fixed)
        return True
    return False

# Fix all XHTML files in REBRANDED_OUTPUT
xhtml_dir = Path('/workspaces/Fm/REBRANDED_OUTPUT/xhtml')
fixed_count = 0

for xhtml_file in xhtml_dir.glob('*.xhtml'):
    if fix_merge_conflicts(xhtml_file):
        fixed_count += 1
        print(f"Fixed: {xhtml_file.name}")

print(f"\nTotal files fixed: {fixed_count}")
