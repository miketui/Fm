#!/bin/bash
# Session start hook for EPUB QA workflow
# Displays git status, recent commits, and pending publication issues

echo "════════════════════════════════════════════════════════════"
echo "EPUB Visual QA & Publication Workflow - Session Started"
echo "════════════════════════════════════════════════════════════"
echo ""

# Show git status if available
if command -v git >/dev/null 2>&1 && [ -d .git ]; then
  echo "📋 Git Status:"
  git status --short 2>/dev/null || echo "  (git status unavailable)"
  echo ""

  echo "📝 Recent Commits:"
  git log --oneline -3 2>/dev/null || echo "  (git log unavailable)"
  echo ""
fi

# Check for pending issues
if [ -f ".claude/pending-issues.txt" ]; then
  echo "⚠️  PENDING PUBLICATION ISSUES:"
  cat ".claude/pending-issues.txt"
  echo ""
fi

# Show visual QA pipeline status if reports exist
if [ -f "docs/REBRANDED_VISUAL_AUDIT.json" ]; then
  echo "✅ Visual QA Reports Available:"
  echo "   - docs/REBRANDED_VISUAL_AUDIT.md"
  echo "   - docs/REBRANDED_VISUAL_AUDIT.json"
  echo "   - docs/gallery/index.html"
  echo ""
fi

# Remind about safe edit zones
echo "📂 Safe Edit Zones:"
echo "   ✅ scripts/, docs/, tests/, .claude/"
echo "   ⚠️  REBRANDED_OUTPUT/xhtml/*.xhtml (requires approval)"
echo "   ⚠️  REBRANDED_OUTPUT/xhtml/styles/*.css (requires approval)"
echo "   ❌ REBRANDED_OUTPUT/content.opf, mimetype (critical files)"
echo ""

echo "💡 Quick Commands:"
echo "   Run full QA:  npm run qa:full"
echo "   View reports: cat docs/REBRANDED_VISUAL_AUDIT.md"
echo "   Open gallery: docs/gallery/index.html"
echo ""

echo "════════════════════════════════════════════════════════════"

exit 0
