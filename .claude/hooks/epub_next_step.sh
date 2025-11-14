#!/bin/bash
# Subagent completion hook - Suggests next step in EPUB publication workflow

# Read pipeline status from visual audit JSON if available
PIPELINE_STATUS="UNKNOWN"

if [ -f "docs/REBRANDED_VISUAL_AUDIT.json" ]; then
  # Check if all required fields are present
  HAS_SCREENSHOTS=$(jq '.files[0].screenshots' docs/REBRANDED_VISUAL_AUDIT.json 2>/dev/null)
  HAS_PDF_CHECK=$(jq '.files[0].pdf_check' docs/REBRANDED_VISUAL_AUDIT.json 2>/dev/null)

  if [ "$HAS_PDF_CHECK" != "null" ] && [ "$HAS_SCREENSHOTS" != "null" ]; then
    PIPELINE_STATUS="COMPLETE"
  elif [ "$HAS_SCREENSHOTS" != "null" ]; then
    PIPELINE_STATUS="SCREENSHOTS_DONE"
  else
    PIPELINE_STATUS="TARGETS_FOUND"
  fi
fi

# Check if CSS coverage exists
if [ -f "docs/CSS_COVERAGE.md" ]; then
  PIPELINE_STATUS="${PIPELINE_STATUS}_CSS_DONE"
fi

# Suggest next step based on status
echo ""
echo "════════════════════════════════════════════════════════════"
echo "📍 EPUB Workflow - Next Step Suggestion"
echo "════════════════════════════════════════════════════════════"
echo ""

case "$PIPELINE_STATUS" in
  TARGETS_FOUND)
    echo "✅ Target discovery complete (44 XHTML files identified)"
    echo "➡️  Next: Run epub-visual-auditor subagent"
    echo "   Command: python3 scripts/visual_review.py ..."
    ;;
  SCREENSHOTS_DONE)
    echo "✅ Visual review complete (screenshots captured)"
    echo "➡️  Next: Run pdf-verifier subagent"
    echo "   Command: python3 scripts/pdf_verify.py ..."
    ;;
  COMPLETE_CSS_DONE|COMPLETE)
    echo "✅ Visual QA pipeline complete"
    echo "➡️  Next options:"
    echo "   1. Run accessibility-checker subagent (Ace validation)"
    echo "   2. Run publication-finalizer subagent (full pre-flight)"
    echo "   3. Review reports and fix identified issues"
    ;;
  COMPLETE_CSS_DONE)
    echo "✅ Full pipeline complete including CSS coverage"
    echo "➡️  Ready for publication validation"
    echo "   Invoke: publication-finalizer subagent"
    ;;
  *)
    echo "ℹ️  Pipeline status: $PIPELINE_STATUS"
    echo "➡️  Run visual QA pipeline from step 1:"
    echo "   python3 scripts/find_44_targets.py ..."
    ;;
esac

echo ""
echo "════════════════════════════════════════════════════════════"

exit 0
