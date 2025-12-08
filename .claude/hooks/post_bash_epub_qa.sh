#!/bin/bash
# Post-bash hook for EPUB QA commands
# Notifies user when QA pipeline commands complete and where to find results

COMMAND="$TOOL_INPUT"

# Check if this was a visual QA command
if echo "$COMMAND" | grep -q "visual_review.py\|pdf_verify.py\|css_coverage_analyzer.py\|find_44_targets.py"; then
  echo ""
  echo "════════════════════════════════════════════════════════════"
  echo "✅ EPUB QA Command Completed"
  echo "════════════════════════════════════════════════════════════"
  echo ""

  # Specific guidance based on command
  if echo "$COMMAND" | grep -q "find_44_targets.py"; then
    echo "📄 Target Discovery Complete"
    echo "   Results: docs/REBRANDED_VISUAL_AUDIT.json"
    echo "   Next: Run visual_review.py to capture screenshots"
  elif echo "$COMMAND" | grep -q "visual_review.py"; then
    echo "📸 Visual Review Complete"
    echo "   Screenshots: docs/screenshots/"
    echo "   Gallery: docs/gallery/index.html"
    echo "   Summary: docs/REBRANDED_VISUAL_AUDIT.md"
    echo "   Next: Run pdf_verify.py to check PDF parity"
  elif echo "$COMMAND" | grep -q "pdf_verify.py"; then
    echo "📋 PDF Parity Check Complete"
    echo "   Results: docs/REBRANDED_VISUAL_AUDIT.json (pdf_check fields)"
    echo "   Next: Run css_coverage_analyzer.py for stylesheet diagnostics"
  elif echo "$COMMAND" | grep -q "css_coverage_analyzer.py"; then
    echo "🎨 CSS Coverage Analysis Complete"
    echo "   Report: docs/CSS_COVERAGE.md"
    echo "   JSON: docs/CSS_COVERAGE.json"
    echo "   Next: Review unused selectors and missing definitions"
  fi

  echo ""
  echo "════════════════════════════════════════════════════════════"
fi

exit 0
