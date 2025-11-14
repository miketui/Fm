#!/bin/bash
# Post-write hook for XHTML file changes
# Runs quick validation when XHTML files are modified

FILE_PATH="$TOOL_INPUT"

# Only run on XHTML files
if [[ "$FILE_PATH" == *.xhtml ]] && [[ "$FILE_PATH" == *REBRANDED_OUTPUT* ]]; then
  echo ""
  echo "════════════════════════════════════════════════════════════"
  echo "🔍 XHTML File Modified - Running Quick Validation"
  echo "════════════════════════════════════════════════════════════"
  echo ""
  echo "File: $FILE_PATH"
  echo ""

  # Run EPUBCheck on the single file if available
  if command -v epubcheck >/dev/null 2>&1; then
    echo "Running EPUBCheck..."
    epubcheck "$FILE_PATH" 2>&1 | head -20
  else
    echo "⚠️  EPUBCheck not found - install for automated validation"
  fi

  echo ""
  echo "💡 Recommended: Re-run visual QA to verify rendering"
  echo "   python3 scripts/visual_review.py ..."
  echo ""
  echo "════════════════════════════════════════════════════════════"
fi

exit 0
