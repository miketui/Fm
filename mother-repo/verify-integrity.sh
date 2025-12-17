#!/bin/bash

# Verification script for Mother Repository
# Checks that all critical files and directories are present

set -e

echo "=========================================="
echo "Mother Repository Integrity Check"
echo "=========================================="
echo ""

ERRORS=0
WARNINGS=0

# Check if we're in the right directory
if [ ! -f "README.md" ] || [ ! -f "TRANSFER_COMPLETE.md" ]; then
    echo "ERROR: This script must be run from the mother-repo directory"
    exit 1
fi

echo "Checking documentation files..."

# Check documentation
for file in "README.md" "SETUP_INSTRUCTIONS.md" "CONTENTS.md" "TRANSFER_COMPLETE.md" "LICENSE" ".gitignore"; do
    if [ -f "$file" ]; then
        echo "  ✓ $file"
    else
        echo "  ✗ MISSING: $file"
        ERRORS=$((ERRORS + 1))
    fi
done

echo ""
echo "Checking REBRANDED_OUTPUT structure..."

# Check REBRANDED_OUTPUT
if [ -d "REBRANDED_OUTPUT" ]; then
    echo "  ✓ REBRANDED_OUTPUT directory exists"
    
    # Check critical files
    for file in "content.opf" "mimetype" "README.md"; do
        if [ -f "REBRANDED_OUTPUT/$file" ]; then
            echo "  ✓ REBRANDED_OUTPUT/$file"
        else
            echo "  ✗ MISSING: REBRANDED_OUTPUT/$file"
            ERRORS=$((ERRORS + 1))
        fi
    done
    
    # Check critical directories
    for dir in "META-INF" "xhtml" "fonts" "images" "pdf-pod"; do
        if [ -d "REBRANDED_OUTPUT/$dir" ]; then
            echo "  ✓ REBRANDED_OUTPUT/$dir/"
        else
            echo "  ✗ MISSING: REBRANDED_OUTPUT/$dir/"
            ERRORS=$((ERRORS + 1))
        fi
    done
    
    # Check xhtml/styles
    if [ -d "REBRANDED_OUTPUT/xhtml/styles" ]; then
        echo "  ✓ REBRANDED_OUTPUT/xhtml/styles/"
    else
        echo "  ✗ MISSING: REBRANDED_OUTPUT/xhtml/styles/"
        ERRORS=$((ERRORS + 1))
    fi
    
    # Count files
    XHTML_COUNT=$(find REBRANDED_OUTPUT/xhtml -name "*.xhtml" -type f | wc -l)
    PDF_COUNT=$(find REBRANDED_OUTPUT/pdf-pod -name "*.pdf" -type f 2>/dev/null | wc -l)
    IMG_COUNT=$(find REBRANDED_OUTPUT/images -type f 2>/dev/null | wc -l)
    FONT_COUNT=$(find REBRANDED_OUTPUT/fonts -name "*.woff2" -type f 2>/dev/null | wc -l)
    
    echo ""
    echo "  File counts:"
    echo "    XHTML files: $XHTML_COUNT (expected: 46)"
    echo "    PDF files: $PDF_COUNT (expected: 44)"
    echo "    Images: $IMG_COUNT (expected: 31)"
    echo "    Fonts: $FONT_COUNT (expected: 6)"
    
    if [ "$XHTML_COUNT" -lt 46 ]; then
        echo "    ⚠ WARNING: XHTML file count is low"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    if [ "$PDF_COUNT" -lt 44 ]; then
        echo "    ⚠ WARNING: PDF file count is low"
        WARNINGS=$((WARNINGS + 1))
    fi
else
    echo "  ✗ MISSING: REBRANDED_OUTPUT directory"
    ERRORS=$((ERRORS + 1))
fi

echo ""
echo "Checking OEBPS structure..."

# Check OEBPS
if [ -d "OEBPS" ]; then
    echo "  ✓ OEBPS directory exists"
    
    # Check critical files
    if [ -f "OEBPS/content.opf" ]; then
        echo "  ✓ OEBPS/content.opf"
    else
        echo "  ✗ MISSING: OEBPS/content.opf"
        ERRORS=$((ERRORS + 1))
    fi
    
    # Check critical directories
    for dir in "text" "styles" "fonts" "images"; do
        if [ -d "OEBPS/$dir" ]; then
            echo "  ✓ OEBPS/$dir/"
        else
            echo "  ✗ MISSING: OEBPS/$dir/"
            ERRORS=$((ERRORS + 1))
        fi
    done
else
    echo "  ✗ MISSING: OEBPS directory"
    ERRORS=$((ERRORS + 1))
fi

echo ""
echo "Checking repository size..."

# Check sizes
REBRANDED_SIZE=$(du -sm REBRANDED_OUTPUT 2>/dev/null | cut -f1)
OEBPS_SIZE=$(du -sm OEBPS 2>/dev/null | cut -f1)
TOTAL_SIZE=$(du -sm . 2>/dev/null | cut -f1)

echo "  REBRANDED_OUTPUT: ${REBRANDED_SIZE}M (expected: ~172M)"
echo "  OEBPS: ${OEBPS_SIZE}M (expected: ~11M)"
echo "  Total: ${TOTAL_SIZE}M (expected: ~183M)"

if [ "$REBRANDED_SIZE" -lt 100 ]; then
    echo "  ⚠ WARNING: REBRANDED_OUTPUT size seems low"
    WARNINGS=$((WARNINGS + 1))
fi

echo ""
echo "Checking scripts..."

# Check scripts
if [ -x "setup-repository.sh" ]; then
    echo "  ✓ setup-repository.sh (executable)"
else
    echo "  ⚠ setup-repository.sh not executable or missing"
    WARNINGS=$((WARNINGS + 1))
fi

echo ""
echo "=========================================="
echo "Verification Summary"
echo "=========================================="
echo ""

if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo "✅ SUCCESS: All checks passed!"
    echo ""
    echo "Repository is ready for GitHub upload."
    echo "Next steps:"
    echo "  1. Review README.md"
    echo "  2. Run ./setup-repository.sh to push to GitHub"
    echo "  3. Or follow manual steps in SETUP_INSTRUCTIONS.md"
    exit 0
elif [ $ERRORS -eq 0 ]; then
    echo "⚠️  WARNINGS: $WARNINGS warning(s) found"
    echo ""
    echo "Repository structure is mostly correct, but some non-critical items need attention."
    echo "You can proceed with caution."
    exit 0
else
    echo "❌ ERRORS: $ERRORS error(s) found"
    echo "⚠️  WARNINGS: $WARNINGS warning(s) found"
    echo ""
    echo "Please fix the errors before proceeding."
    exit 1
fi
