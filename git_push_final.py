#!/usr/bin/env python3
import subprocess as sp, os
os.chdir('/workspaces/Fm')
print("\n" + "="*70)
print("FINAL GIT PUSH TO MAIN")
print("="*70)

# Stage, commit, push
sp.run(['git', 'add', '-A'])
sp.run(['git', 'commit', '-m', 'chore(dist): add compiled EPUB files to distribution locations (2025-12-17)'])
r = sp.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True)

if 'fatal' not in r.stderr.lower():
    print("\n✓ PUSH SUCCESSFUL!")
    print("\nLatest commits:")
    sp.run(['git', 'log', '--oneline', '-3'])
else:
    print(f"\n⚠ Push status: {r.stderr[:200]}")

print("\n" + "="*70)
