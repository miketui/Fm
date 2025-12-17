#!/usr/bin/env python3
"""
Bulk fix merge conflicts in XHTML files by keeping HEAD version
Uses regex to find and fix all <<<<<<< HEAD patterns
"""
import re
from pathlib import Path

# Files with conflicts
files_to_fix = [
    '/workspaces/Fm/REBRANDED_OUTPUT/xhtml/11-chapter-iii-reigniting-your-creative-fire.xhtml',
    '/workspaces/Fm/REBRANDED_OUTPUT/xhtml/16-chapter-vii-embracing-wellness-and-self-care.xhtml',
    '/workspaces/Fm/REBRANDED_OUTPUT/xhtml/23-chapter-xiii-embracing-ethics-and-sustainability-in-hairstyling.xhtml',
    '/workspaces/Fm/REBRANDED_OUTPUT/xhtml/25-chapter-xiv-the-impact-of-ai-on-the-beauty-industry.xhtml',
    '/workspaces/Fm/REBRANDED_OUTPUT/xhtml/21-chapter-xi-advanced-digital-strategies-for-freelance-hairstylists.xhtml',
    '/workspaces/Fm/REBRANDED_OUTPUT/xhtml/10-chapter-ii-refining-your-creative-toolkit.xhtml',
    '/workspaces/Fm/REBRANDED_OUTPUT/xhtml/20-chapter-x-crafting-enduring-legacies.xhtml',
    '/workspaces/Fm/REBRANDED_OUTPUT/xhtml/13-chapter-iv-the-art-of-networking-in-freelance-hairstyling.xhtml',
    '/workspaces/Fm/REBRANDED_OUTPUT/xhtml/22-chapter-xii-financial-wisdom-building-sustainable-ventures.xhtml',
    '/workspaces/Fm/REBRANDED_OUTPUT/xhtml/19-chapter-ix-stepping-into-leadership.xhtml',
    '/workspaces/Fm/REBRANDED_OUTPUT/xhtml/17-chapter-viii-advancing-skills-through-continuous-education.xhtml',
]

# Pattern to match <<<<<<< HEAD ... ======= ... >>>>>>> branch
# Keeps the HEAD version (between <<<<<<< HEAD and =======)
pattern = r'<<<<<<< HEAD\n(.*?)\n=======\n.*?\n>>>>>>> [^\n]*\n'

fixed = 0
for file_path in files_to_fix:
    try:
        path = Path(file_path)
        if path.exists():
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Replace all merge conflicts, keeping HEAD version
            new_content = re.sub(pattern, r'\1\n', content, flags=re.DOTALL)
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                fixed += 1
                print(f"✓ Fixed: {Path(file_path).name}")
    except Exception as e:
        print(f"✗ Error fixing {Path(file_path).name}: {e}")

print(f"\nTotal files fixed: {fixed}/{len(files_to_fix)}")
