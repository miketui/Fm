#!/usr/bin/env python3
"""
Push EPUB copies and final changes to main branch
"""
import subprocess
import os
from pathlib import Path
from datetime import datetime

base = Path('/workspaces/Fm')
os.chdir(base)

print("\n" + "="*70)
print("PUSHING TO MAIN BRANCH")
print("="*70 + "\n")

# Check current branch
print("Step 1: Checking git status...")
result = subprocess.run(['git', 'branch', '--show-current'], capture_output=True, text=True)
current_branch = result.stdout.strip()
print(f"  Current branch: {current_branch}\n")

# Switch to main if needed
if current_branch != 'main':
    print("Step 2: Switching to main branch...")
    subprocess.run(['git', 'checkout', 'main'], capture_output=True)
    print("  ✓ Switched to main\n")
else:
    print("Step 2: Already on main branch ✓\n")

# Pull latest
print("Step 3: Pulling latest changes...")
result = subprocess.run(['git', 'pull', 'origin', 'main'], capture_output=True, text=True)
print("  ✓ Pulled latest\n")

# Check status
print("Step 4: Checking for changes...")
result = subprocess.run(['git', 'status', '--short'], capture_output=True, text=True)
status = result.stdout.strip()

if status:
    print(f"  Found changes to commit:\n")
    for line in status.split('\n')[:10]:
        print(f"    {line}")
    if len(status.split('\n')) > 10:
        print(f"    ... and {len(status.split('\n')) - 10} more\n")
    
    # Stage all changes
    print("Step 5: Staging all changes...")
    subprocess.run(['git', 'add', '-A'], capture_output=True)
    print("  ✓ Staged\n")
    
    # Commit
    print("Step 6: Committing changes...")
    msg = f"chore(dist): add compiled EPUB to root and releases directory ({datetime.now().strftime('%Y-%m-%d')})"
    result = subprocess.run(['git', 'commit', '-m', msg], capture_output=True, text=True)
    print(f"  ✓ Committed: {msg}\n")
else:
    print("  No changes to commit\n")

# Push to main
print("Step 7: Pushing to origin/main...")
result = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True)

if result.returncode == 0:
    print("  ✓ Successfully pushed to origin/main\n")
    success = True
else:
    print(f"  ✗ Push failed: {result.stderr[:200]}\n")
    success = False

# Show latest commits
print("Step 8: Latest commits on main:")
result = subprocess.run(['git', 'log', '--oneline', '-5'], capture_output=True, text=True)
for line in result.stdout.strip().split('\n'):
    print(f"  {line}")

print("\n" + "="*70)
if success:
    print("✓ PUSH TO MAIN COMPLETED SUCCESSFULLY")
else:
    print("⚠ PUSH COMPLETED WITH ISSUES")
print("="*70 + "\n")
